"""Tests for MiniMax AI client."""

from __future__ import annotations

import os
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.ai.client import MiniMaxClient, create_ai_client
from src.models import AIConfig, AIProvider


def _make_config(**overrides) -> AIConfig:
    defaults = {
        "provider": AIProvider.MINIMAX,
        "model": "MiniMax-M2.7",
        "api_key_env": "MINIMAX_API_KEY",
        "temperature": 0.3,
        "max_tokens": 4096,
    }
    defaults.update(overrides)
    return AIConfig(**defaults)


class TestMiniMaxClientInit:
    def test_creates_instance_with_valid_config(self, monkeypatch):
        monkeypatch.setenv("MINIMAX_API_KEY", "test-key")
        client = MiniMaxClient(_make_config())
        assert client.model == "MiniMax-M2.7"
        assert client.max_tokens == 4096

    def test_raises_when_api_key_missing(self, monkeypatch):
        monkeypatch.delenv("MINIMAX_API_KEY", raising=False)
        with pytest.raises(ValueError, match="Missing API key"):
            MiniMaxClient(_make_config())

    def test_uses_default_base_url(self, monkeypatch):
        monkeypatch.setenv("MINIMAX_API_KEY", "test-key")
        client = MiniMaxClient(_make_config())
        assert str(client.client.base_url).rstrip("/").endswith("api.minimax.io/v1")

    def test_uses_custom_base_url(self, monkeypatch):
        monkeypatch.setenv("MINIMAX_API_KEY", "test-key")
        client = MiniMaxClient(_make_config(base_url="https://api.minimaxi.com/v1"))
        assert "minimaxi.com" in str(client.client.base_url)


class TestMiniMaxClientComplete:
    @pytest.mark.asyncio
    async def test_basic_completion(self, monkeypatch):
        monkeypatch.setenv("MINIMAX_API_KEY", "test-key")
        client = MiniMaxClient(_make_config())

        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = '{"score": 8}'
        mock_response.usage.prompt_tokens = 10
        mock_response.usage.completion_tokens = 5

        with patch.object(
            client.client.chat.completions, "create", new_callable=AsyncMock
        ) as mock_create:
            mock_create.return_value = mock_response
            result = await client.complete(system="test", user="hello")

        assert result == '{"score": 8}'
        call_kwargs = mock_create.call_args[1]
        assert call_kwargs["model"] == "MiniMax-M2.7"
        # response_format should NOT be present (MiniMax doesn't support it)
        assert "response_format" not in call_kwargs

    @pytest.mark.asyncio
    async def test_temperature_zero_clamped(self, monkeypatch):
        monkeypatch.setenv("MINIMAX_API_KEY", "test-key")
        client = MiniMaxClient(_make_config())

        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "ok"
        mock_response.usage.prompt_tokens = 10
        mock_response.usage.completion_tokens = 5

        with patch.object(
            client.client.chat.completions, "create", new_callable=AsyncMock
        ) as mock_create:
            mock_create.return_value = mock_response
            await client.complete(system="test", user="hello", temperature=0.0)

        call_kwargs = mock_create.call_args[1]
        assert call_kwargs["temperature"] > 0


class TestFactoryFunction:
    def test_creates_minimax_client(self, monkeypatch):
        monkeypatch.setenv("MINIMAX_API_KEY", "test-key")
        config = _make_config()
        client = create_ai_client(config)
        assert isinstance(client, MiniMaxClient)

    def test_minimax_provider_enum(self):
        assert AIProvider.MINIMAX.value == "minimax"
