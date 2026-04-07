"""Error definitions for Daybreak MCP service."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class DaybreakMcpError(Exception):
    """Structured exception with stable error code."""

    code: str
    message: str
    details: Any = None

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.code}: {self.message}"
