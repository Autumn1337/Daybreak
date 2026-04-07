# 项目交接文档
最后更新：2026-04-07（架构清理 + 运行验证会话结束）

## 项目概况
Daybreak — AI 驱动每日技术情报系统。架构清理已完成，pipeline 已验证可正常运行。

## 当前状态
架构清理 11 个 commit 已 push 到 master，pipeline 实际运行验证通过：
- 51 items 抓取 → 42 items scored ≥ 6.0 → 报告生成成功
- Token 用量正常：82,359 tokens（input 44k, output 38k）
- 并发评分可用，默认并发度调整为 5（代理 muxufo.com 的甜点）

### 本次完成的改动（12 commits on master）

**P0 正确性修复：**
1. `datetime.utcnow` → `datetime.now(timezone.utc)`（models.py, orchestrator.py）
2. RSS ID 稳定性：`hash()` → `hashlib.md5().hexdigest()[:12]`（rss.py）
3. AliClient 补齐 `record_usage` 调用（client.py）
4. CI deploy-docs.yml: `checkout@v6` → `@v4`
5. config.example.json: 占位符 email/feishu 改为 `enabled: false`

**P1 性能：**
6. AI 评分并发化：`analyze_batch` 从串行改为 `asyncio.gather + Semaphore(5)`

**P2 可维护性：**
7. `DailySummarizer.generate_summary` 从 async 改为 sync
8. Token 计数器每次 pipeline 运行前 `reset_usage()`
9. Jekyll front matter 写入迁移到 `StorageManager.save_docs_post()`
10. MCP service.py 删除冗余 `asyncio.iscoroutine` 检查
11. `BaseScraper` config 类型标注修正为 `Any`

**配置管理：**
12. config.json 分离为 config.example.json（git 跟踪）+ config.json（gitignored）

## 配置管理

| 文件 | 内容 | git 跟踪 |
|---|---|---|
| `data/config.example.json` | 模板，占位符值 | 是 |
| `data/config.json` | 真实配置（代理地址、webhook） | 否（.gitignore） |
| `.env` | API keys | 否（.gitignore） |

当前 config.json 状态：
- AI: provider=openai, model=gemini-3-flash-preview, base_url=http://muxufo.com/v1
- 飞书: enabled=true, webhook 已配置
- 邮件: enabled=false（占位符地址）
- 评分阈值: 6.0

## 已知问题
- 代理并发度超过 5 会触发 rate limit，默认已调为 5
- RSS 2 个源 403（rachelbythebay.com, tedunangst.com），是正常的
- 品牌重命名的 docs/ 文件变更仍在 working tree 未提交（上次会话遗留）

## 验证方式
```bash
cd /e/Newspaper/horizon-public
uv run pytest tests/ -v    # 期望：27 passed
uv run daybreak --hours 24  # 实际运行
```

## 下一步（按优先级）
1. 补充 scraper/orchestrator 单元测试（P3）
2. 评分标准可配置化（从 prompt 提取到 config.json）
3. 飞书消息多语言支持
4. Enrichment 重新评估（只对 score ≥ 8.5 的条目做）
5. 提交 working tree 中遗留的品牌重命名文件
