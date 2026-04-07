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

## 2026-04-07: 架构清理方案选择

选项：A（仅修 P0 bug）/ B（P0 + P1 性能 + P2 可维护性一次到位）
选择：B
理由：项目处于可发布状态，一次性清理技术债比分多次做更高效。11 个改动互不干扰，风险可控。

## 2026-04-07: AI 评分并发策略

选项：A（保持串行，减少 API 并发压力）/ B（asyncio.gather + Semaphore 控制并发度）
选择：B，默认并发度 8
理由：评分是 pipeline 最慢环节（N 条内容 = N 次串行 API 调用），并发化预期 5-10x 提速。Semaphore 限制并发度防止 API 过载。concurrency 参数可在调用时调整。
