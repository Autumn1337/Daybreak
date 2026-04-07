# 🌅 Daybreak Daily

**AI-powered daily tech briefing — 从 10+ 数据源抓取、AI 评分筛选、中文摘要、多渠道推送。**

基于 [Thysrael/Horizon](https://github.com/Thysrael/Horizon) 二次开发，新增中文数据源、飞书推送、Gemini 代理支持等功能。

## Features

- **4 大信息源**：Hacker News、93 个技术博客 RSS（Karpathy 推荐清单）、Reddit (ML/LocalLLaMA)、ArXiv AI/ML 论文
- **AI 智能筛选**：Gemini / GPT / Claude / DeepSeek 多模型支持，0-10 分评分 + 阈值过滤
- **跨源去重**：URL 去重 + AI 语义去重，同一新闻不会重复出现
- **中文摘要**：评分阶段直接生成中文 summary，无需额外翻译步骤
- **多渠道推送**：飞书卡片（自动分页）+ 邮件 + GitHub Pages
- **GitHub Actions 自动化**：每天定时运行，零运维

## 相比原版 Horizon 新增的功能

| 功能 | 说明 |
|---|---|
| ArXiv Scraper | 3 级 fallback 策略，周末也能抓到论文 |
| 飞书推送 | Webhook 卡片消息，自动分页 |
| 中文摘要 | analyzer 直接输出中文，不依赖 enrichment |
| RSS 并发优化 | asyncio.gather + Semaphore(10)，93 源并发抓取 |
| Gemini 代理支持 | GeminiClient 支持 base_url 代理（OpenAI 兼容格式） |
| OPML 工具 | 一键从 Karpathy RSS 清单生成配置 |

## Quick Start

```bash
# 克隆
git clone https://github.com/YOUR_USERNAME/daybreak-daily.git
cd daybreak-daily

# 安装依赖
uv sync  # 或 pip install -e .

# 配置
cp .env.example .env
# 编辑 .env，填入你的 API Key

# 编辑 data/config.json，配置：
# - AI provider 和模型
# - 信息源开关
# - 飞书 webhook URL
# - 邮件地址

# 运行
uv run daybreak --hours 24
```

## 配置说明

### .env

```
GEMINI_API_KEY=your-api-key        # AI 模型 API Key
EMAIL_PASSWORD=your-app-password    # Gmail App Password（可选）
```

### data/config.json

```jsonc
{
  "ai": {
    "provider": "openai",           // openai / gemini / anthropic / ali
    "model": "gemini-2.5-flash",    // 模型名称
    "base_url": null,               // 代理地址，直连填 null，代理填 "http://your-proxy.com/v1"
    "api_key_env": "GEMINI_API_KEY",
    "languages": ["zh"]             // 摘要语言
  },
  "filtering": {
    "ai_score_threshold": 6.0,      // 评分阈值，低于此分的文章被过滤
    "time_window_hours": 24
  },
  "feishu": {                       // 飞书推送（可选）
    "webhook_url": "https://open.feishu.cn/open-apis/bot/v2/hook/your-id",  // 群机器人 Webhook
    "enabled": true                 // 是否启用
  }
}
```

### RSS 源管理

项目自带 Karpathy 推荐的 93 个技术博客 RSS 源。如需更新：

```bash
uv run python scripts/generate_rss_config.py
# 将 data/rss_feeds.json 的内容复制到 config.json 的 sources.rss 中
```

## GitHub Actions 自动化

仓库已配置 `.github/workflows/daily-summary.yml`，设置方法：

1. 在 repo Settings → Secrets → Actions 添加 `GEMINI_API_KEY` 和 `EMAIL_PASSWORD`
2. cron 默认 UTC 23:51（北京 07:51），按需修改
3. 报告自动部署到 GitHub Pages + 发送邮件/飞书

## Architecture

```
数据源 (并发抓取)          AI 评分          推送
┌─────────┐
│ HN      │──┐
│ RSS×93  │──┤   ┌──────────┐   ┌────────────┐
│ Reddit  │──┼──→│ 去重+评分 │──→│ 飞书/邮件   │
│ ArXiv   │──┘   │ (Gemini) │   │ GitHub Pages│
└─────────┘      └──────────┘   └────────────┘
```

## Credits

- [Thysrael/Horizon](https://github.com/Thysrael/Horizon) — 原版项目
- [Karpathy RSS List](https://gist.github.com/emschwartz/e6d2bf860ccc367fe37ff953ba6de66b) — 92 个 HN 热门博客 RSS 源

## License

MIT
