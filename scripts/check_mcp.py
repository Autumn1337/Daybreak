#!/usr/bin/env python3
"""Local smoke check for Daybreak MCP integration."""

from __future__ import annotations

import asyncio
import json

from src.mcp.daybreak_adapter import resolve_daybreak_path
from src.mcp.server import hz_get_metrics
from src.mcp.service import DaybreakPipelineService


async def _main() -> None:
    daybreak_path = resolve_daybreak_path()
    service = DaybreakPipelineService()
    validation = await service.validate_config(
        daybreak_path=str(daybreak_path),
        check_env=False,
    )
    metrics = hz_get_metrics()

    payload = {
        "ok": True,
        "daybreak_path": str(daybreak_path),
        "config_path": validation["config_path"],
        "enabled_sources": validation["enabled_sources"],
        "languages": validation["ai"]["languages"],
        "metrics_ok": metrics["ok"],
        "metrics_tool": metrics["tool"],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(_main())
