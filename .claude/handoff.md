# 项目交接文档
最后更新：2026-04-07

## 项目概况
Daybreak — AI 驱动每日技术情报系统。架构清理完成，11 个改动已提交到 master，处于可发布状态。

## 当前状态
本次会话完成架构清理（P0 正确性修复 + P1 性能 + P2 可维护性），11 个 commit 已提交。27/27 测试通过。

## 关键决策（仍然有效的）
- 双仓库合并为单一 horizon-public 仓库，Daybreak 品牌，密钥通过 .env 隔离
- MCP breaking changes 不加兼容 shim（个人项目，无外部消费者）
- AI 评分并发化：asyncio.gather + Semaphore(8)，默认并发度 8，可在调用时调整
- Jekyll front matter 写入归属 StorageManager.save_docs_post()，不在 orchestrator 处理
- config.json 中 email/feishu 默认 enabled: false，避免 CI 噪音
- HZ_ 错误码前缀和 hz_ MCP tool 前缀保留：内部标识符，不影响品牌

## 已知问题
- enrichment（背景知识补充）被禁用：每篇 2 次 AI + DuckDuckGo 搜索，太慢
- ArXiv 周末无新提交时返回旧论文（已去掉 since 过滤，靠 API 排序取最新）
- 36Kr / PH 没有精确时间戳，published_at 设为 now()，无法做 since 过滤
- RSS 个别源 403 或超时正常（devblogs.microsoft.com 等）
- uv.lock 在 package name 改为 daybreak 后可能过时，需要重新生成

## 下一步（按优先级）
1. push 到 GitHub remote（Autumn1337/Daybreak）
2. 实际运行 `uv run daybreak --hours 24` 验证并发评分效果
3. 验证 GitHub Pages 在 /Daybreak baseurl 下正常渲染
4. 可选：补充 scraper/orchestrator 单元测试（P3）
5. 可选：评分标准可配置化、飞书多语言（P4）

## 关键文件
- `src/ai/analyzer.py` — 并发评分核心，重写了 analyze_batch（asyncio.gather + Semaphore）
- `src/orchestrator.py` — 主流程编排，去除 Jekyll 写入和 summarizer await，加 reset_usage
- `src/storage/manager.py` — 新增 save_docs_post，负责 Jekyll front matter
- `src/models.py` — fetched_at 使用 aware datetime（timezone.utc）
- `src/scrapers/rss.py` — 确定性 hash（hashlib.md5，跨进程稳定）
- `src/ai/client.py` — AliClient 补齐 record_usage 调用
- `tests/test_analyzer_concurrency.py` — 并发功能测试（新增）

## 验证方式
```bash
cd /e/Newspaper/horizon-public
uv run pytest tests/ -v    # 期望：27 passed
```
