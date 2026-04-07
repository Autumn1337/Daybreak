# Decisions — Daybreak

## 2026-04-07: 合并双仓库为单一 Daybreak 仓库

**背景**: 项目原本维护两个目录——`Horizon/`（私有，含真实密钥和 Horizon 品牌）和 `horizon-public/`（公开，Daybreak 品牌，脱敏配置）。两者代码逻辑完全相同，仅品牌名和占位符不同。

**决策**: 合并为一个仓库，以 Daybreak 品牌为准。

**理由**:
- 双仓库每次改代码都要手动同步，维护成本高
- 密钥已通过 `.env` + `.gitignore` 隔离，无泄露风险
- 品牌差异可通过一次性改名消除

**执行方式**: 彻底改名——类名（`HorizonOrchestrator` → `DaybreakOrchestrator`）、文件名（`horizon_adapter.py` → `daybreak_adapter.py`）、变量名、环境变量、MCP URI 全部统一为 Daybreak。保留 `HZ_` 错误码前缀和 `hz_` MCP tool 前缀作为内部标识符。

**影响**: 公开仓库 github.com/Autumn1337/Daybreak 需要 push 更新。原 `Horizon/` 目录废弃。

## 2026-04-07: MCP breaking changes 不加兼容 shim

选项：A（硬断，直接删旧接口） / B（加过渡期 shim，保持向后兼容）
选择：A
理由：个人项目，无不受控的外部消费者，加 shim 违反最小改动原则，一次性迁移不值得维护额外代码。
