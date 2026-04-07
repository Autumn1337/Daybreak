# Daybreak MCP

Daybreak includes a built-in MCP server that exposes the native Daybreak pipeline as staged tools and read-only resources.

The MCP layer does not reimplement Daybreak business logic. It reuses the existing fetch, score, filter, enrich, and summarize modules from the main codebase.

## Tools

| Tool | Description |
| --- | --- |
| `hz_validate_config` | Validate Daybreak config and required environment variables |
| `hz_fetch_items` | Fetch and deduplicate content into the `raw` stage |
| `hz_score_items` | Score items from a stage into `scored` |
| `hz_filter_items` | Filter scored items into `filtered` |
| `hz_enrich_items` | Enrich filtered items into `enriched` |
| `hz_generate_summary` | Generate markdown from a stage |
| `hz_run_pipeline` | Run fetch -> score -> filter -> enrich -> summarize |
| `hz_list_runs` | List recent run artifacts |
| `hz_get_run_meta` | Read metadata for a run |
| `hz_get_run_stage` | Read items from a run stage |
| `hz_get_run_summary` | Read a generated summary |
| `hz_get_metrics` | Read in-memory server metrics |

## Resources

- `daybreak://server/info`
- `daybreak://metrics`
- `daybreak://runs`
- `daybreak://runs/{run_id}/meta`
- `daybreak://runs/{run_id}/items/{stage}`
- `daybreak://runs/{run_id}/summary/{language}`
- `daybreak://config/effective`

## Install and Start

```bash
uv sync
uv run daybreak-mcp
```

The server runs over stdio and is intended to be launched by an MCP client.

## Run Artifacts

Each run writes artifacts under `data/mcp-runs/<run_id>/`:

- `meta.json`
- `raw_items.json`
- `scored_items.json`
- `filtered_items.json`
- `enriched_items.json`
- `summary-<lang>.md`

## Design Principles

1. Keep Daybreak as the single source of business logic.
2. Preserve staged re-entry so a run can continue from intermediate artifacts.
3. Default to no extra side effects unless explicitly requested.

## Client Setup

See [integration.md](integration.md).
