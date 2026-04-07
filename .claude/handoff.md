# 项目交接文档
最后更新：2026-04-07 (第二次 rename 会话结束)

## 项目概况
Daybreak — AI 驱动每日技术情报系统。品牌重命名已全部完成，项目处于可发布状态。

## 当前状态
品牌重命名两轮已全部完成：
- 第一轮（上一会话）：所有 Python 源码 Horizon → Daybreak
- 第二轮（本会话）：所有文档和静态资源 Horizon → Daybreak

25 个测试全部通过，代码和文档已对齐同一品牌。

## 关键决策（仍然有效的）
- HZ_ 错误码前缀和 hz_ MCP tool 前缀保留：内部标识符，不影响品牌
- MCP breaking changes（hz_* 参数重命名、resource URI 变更、CLI 入口重命名）为有意硬断：个人项目，无外部消费者，加兼容 shim 违反最小改动原则
- README.md 第 5/113 行、CLAUDE.md 第 98 行的上游归因链接保留：记录项目来源
- SVG 注释 "Horizon Grid Lines" 保留：指视觉地平线，非品牌名

## 已知问题
- uv.lock 需要重新生成（package name 已改为 daybreak，lock 文件可能过时）
- GitHub Pages baseurl 已改为 /Daybreak，需要 push 后验证渲染是否正确
- README_zh.md 当前是 upstream 格式换链接，可考虑重写为 Daybreak 原生风格

## 下一步（按优先级）
1. push 到 GitHub remote（github.com/Autumn1337/Daybreak）
2. 验证 GitHub Pages 在 /Daybreak baseurl 下正常渲染
3. 可选：重写 README_zh.md 为 Daybreak 原生风格

## 关键文件
- `docs/_config.yml` — GitHub Pages 配置，baseurl/url 已改为 Daybreak/autumn1337
- `docs/assets/css/daybreak.css` — 原 horizon.css，已重命名
- `docs/assets/js/daybreak.js` — 原 horizon.js，localStorage key 已改为 daybreak-lang
- `docs/daybreak-hub-design.md` — 原 horizon-hub-design.md，已重命名
- `data/config.json` — 运行时配置（含真实 webhook 和邮箱，勿提交）
- `.env` — API keys（勿提交）

## 验证方式
```bash
cd /e/Newspaper/horizon-public
uv run pytest tests/ -v    # 期望：25 passed
grep -r "Horizon" docs/ --include="*.md" --include="*.yml" --include="*.html" --include="*.css" --include="*.js"
# 期望：只剩上游归因链接和视觉地平线注释，无品牌残留
```
