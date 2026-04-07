# Daybreak (Horizon fork)

AI 驱动的每日技术情报系统。从 HN / RSS / Reddit / ArXiv 抓取 → AI 评分筛选 → 中文摘要 → 飞书 + 邮件推送。

## 项目结构

```
src/
├── main.py              # CLI 入口，uv run daybreak
├── orchestrator.py      # 核心流程编排：抓取 → 去重 → 评分 → 生成报告 → 推送
├── models.py            # Pydantic 数据模型：ContentItem, Config, 各源配置
├── scrapers/            # 数据源抓取器，每个继承 BaseScraper
│   ├── base.py          # ABC：async fetch(since) -> List[ContentItem]
│   ├── hackernews.py    # HN Firebase API
│   ├── rss.py           # RSS/Atom，asyncio.gather 并发，Semaphore(10)
│   ├── reddit.py        # Reddit JSON API（无 OAuth）
│   ├── arxiv.py         # ArXiv API，3 级 fallback
│   ├── producthunt.py   # PH GraphQL + hydration fallback
│   ├── kr36.py          # 36Kr HTML 爬虫（当前 disabled）
│   ├── wallstreetcn.py  # 华尔街见闻 JSON API（当前 disabled）
│   └── v2ex.py          # V2EX JSON API（当前 disabled）
├── ai/
│   ├── client.py        # AIClient ABC + 6 个 provider 实现（含 Gemini 代理支持）
│   ├── analyzer.py      # AI 评分：0-10 分 + 中文摘要 + 标签
│   ├── enricher.py      # 背景知识补充（当前 disabled，性能原因）
│   ├── summarizer.py    # Markdown 报告渲染（纯模板，无 AI）
│   └── prompts.py       # 所有 prompt 模板
├── services/
│   ├── emailer.py       # SMTP 邮件发送
│   └── feishu.py        # 飞书 Webhook 卡片推送（自动分页）
├── storage/manager.py   # 文件存储：config / summaries / subscribers
├── mcp/                 # MCP server 集成（非核心路径）
└── setup/               # 交互式配置向导
```

## 运行方式

```bash
uv run daybreak --hours 24     # 抓取过去 24 小时的内容
uv run daybreak --hours 48     # 扩大到 48 小时
```

GitHub Actions 每天 UTC 23:51（北京 07:51）自动运行。

## 配置

- `data/config.json` — 所有配置（AI、数据源、过滤、推送）
- `.env` — API keys（GEMINI_API_KEY, EMAIL_PASSWORD）
- `data/subscribers.json` — 邮件订阅者列表

## AI 配置

当前使用 OpenAI 兼容格式通过 muxufo.com 代理调用 gemini-3-flash-preview。config.json 中：
- `provider: "openai"` — 走 OpenAI SDK
- `base_url: "http://muxufo.com/v1"` — 代理地址
- `api_key_env: "GEMINI_API_KEY"` — 从 .env 读取

切换模型只需改 config.json，不需要改代码。

## 数据流

```
orchestrator.run()
  1. fetch_all_sources()      → 并发抓取所有 enabled 源
  2. merge_cross_source_duplicates()  → URL 去重
  3. _analyze_content()       → AI 评分（每条一次调用）
  4. 按 ai_score >= threshold 过滤
  5. merge_topic_duplicates() → AI 语义去重（一次调用）
  6. _enrich_important_items() → 背景补充（当前跳过）
  7. _generate_summary()      → 渲染 Markdown 报告
  8. 推送：邮件 + 飞书 + GitHub Pages
```

## 添加新数据源

1. 在 `models.py` 添加 SourceType 枚举值和配置模型
2. 在 `src/scrapers/` 创建新文件，继承 `BaseScraper`，实现 `async fetch(since) -> List[ContentItem]`
3. 在 `orchestrator.py` 的 `fetch_all_sources()` 中注册
4. 在 `mcp/horizon_adapter.py` 的 `VALID_SOURCES` 和 `apply_source_filter` 中注册
5. 在 `config.json` 中添加配置

## 已知限制

- enrichment（背景知识补充）被禁用：每篇文章 2 次 AI + DuckDuckGo 搜索，太慢
- ArXiv 周末无新提交时返回旧论文（已去掉 since 过滤，靠 API 排序取最新）
- 36Kr / PH 没有精确时间戳，published_at 设为 now()，无法做 since 过滤
- RSS 个别源 403 或超时是正常的（devblogs.microsoft.com 等）

## 关键约定

- scraper 的 `fetch(since)` 应过滤掉 `published_at < since` 的条目（有真实时间戳时）
- ContentItem.url 必须是有效 URL（Pydantic HttpUrl 验证）
- AI 调用通过 `create_ai_client(config.ai)` 工厂函数，不要直接实例化
- config.json 是运行时配置，.env 是密钥，不要混用
