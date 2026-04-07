---
layout: default
title: Source Presets
---

# Horizon

<div id="lang-zh" class="lang-section" markdown="1">

## 预设信息源库

Horizon 内置了一套精心整理的信息源预设库，覆盖多个技术领域。运行 `horizon-wizard` 向导时，系统会根据你的兴趣自动匹配合适的源。

你也可以直接浏览下方列表，手动将感兴趣的源添加到 `data/config.json`。

---

### 🤖 人工智能 / 机器学习

| 类型 | 信息源 | 说明 |
|------|--------|------|
| Reddit | r/MachineLearning | 机器学习研究讨论 |
| Reddit | r/LocalLLaMA | 本地大模型社区 — 模型发布、评测、部署技巧 |
| RSS | Simon Willison | LLM 工具与实验 |
| GitHub | @karpathy | AI 教育者与研究者 |
| GitHub | vllm-project/vllm | 高吞吐量大模型推理引擎 |
| RSS | 量子位 | AI 资讯与前沿报道（微信公众号） |
| RSS | 新智元 | AI 资讯、模型发布与行业洞察（微信公众号） |

### 🖥️ 系统 / 基础设施

| 类型 | 信息源 | 说明 |
|------|--------|------|
| RSS | LWN.net | Linux 与内核新闻 |
| Reddit | r/linux | Linux 社区讨论 |
| RSS | Brendan Gregg | 性能与系统 |
| GitHub | @torvalds | Linux 之父 |

### 🔒 安全 / 隐私

| 类型 | 信息源 | 说明 |
|------|--------|------|
| Reddit | r/netsec | 信息安全社区 |
| RSS | Krebs on Security | 安全调查报道 |
| RSS | Schneier on Security | 安全分析与评论 |

### 🌐 Web 开发

| 类型 | 信息源 | 说明 |
|------|--------|------|
| Reddit | r/webdev | Web 开发社区 |
| Reddit | r/javascript | JavaScript 讨论与新闻 |
| RSS | CSS-Tricks | 前端技巧与技术 |

### 🔤 编程语言 / 编译器

| 类型 | 信息源 | 说明 |
|------|--------|------|
| Reddit | r/ProgrammingLanguages | 编程语言设计与理论 |
| Reddit | r/rust | Rust 编程社区 |
| GitHub | rust-lang/rust | Rust 语言版本发布 |
| GitHub | ziglang/zig | Zig 语言版本发布 |

### 🤖 嵌入式 / 机器人 / 硬件

| 类型 | 信息源 | 说明 |
|------|--------|------|
| Reddit | r/robotics | 机器人研究与项目 |
| Reddit | r/embedded | 嵌入式系统开发 |
| RSS | Hackaday | 硬件创客与项目 |

### 🛠️ 开源 / 开发工具

| 类型 | 信息源 | 说明 |
|------|--------|------|
| RSS | GitHub Trending | 每日热门仓库 |
| Reddit | r/commandline | 命令行工具与技巧 |
| GitHub | neovim/neovim | Neovim 编辑器版本发布 |

### 🔬 科学 / 学术研究

| 类型 | 信息源 | 说明 |
|------|--------|------|
| Reddit | r/science | 科学新闻与讨论 |
| RSS | Nature | 最新研究亮点 |
| RSS | Quanta Magazine | 通俗科学报道 |

---

## 🤝 贡献你的信息源

我们非常欢迎社区贡献！如果你有优质的信息源想要分享：

1. Fork [Horizon 仓库](https://github.com/thysrael/Horizon)
2. 编辑 `data/presets.json`，在合适的领域下添加你的源
3. 提交 Pull Request

**贡献指南**：

- 确保信息源**活跃且定期更新**
- 信息源应有**较高的信噪比**
- 同时提供 `description`（英文）和 `description_zh`（中文）
- 添加合适的 `tags` 便于关键词匹配
- 在合适的 `domain` 下添加，或创建新的 domain

示例格式：

```json
{
  "type": "rss",
  "description": "Your source description",
  "description_zh": "你的信息源描述",
  "tags": ["topic1", "topic2"],
  "config": {
    "name": "Source Name",
    "url": "https://example.com/feed.xml",
    "category": "your-category"
  }
}
```

</div>

<div id="lang-en" class="lang-section" markdown="1">

## Source Preset Library

Horizon includes a curated library of information source presets across multiple technology domains. When you run the `horizon-wizard` wizard, it automatically matches sources to your interests.

You can also browse the list below and manually add sources to your `data/config.json`.

---

### 🤖 AI / Machine Learning

| Type | Source | Description |
|------|--------|-------------|
| Reddit | r/MachineLearning | Top ML research discussions |
| Reddit | r/LocalLLaMA | Local LLM community — model releases, benchmarks, deployment tips |
| RSS | Simon Willison | LLM tools and experiments |
| GitHub | @karpathy | AI educator and researcher |
| GitHub | vllm-project/vllm | High-throughput LLM serving engine |
| RSS | QbitAI (量子位) | Chinese AI news and research coverage |
| RSS | AI新智元 | Chinese AI news, model releases and industry insights |

### 🖥️ Systems / Infrastructure

| Type | Source | Description |
|------|--------|-------------|
| RSS | LWN.net | Linux and kernel news |
| Reddit | r/linux | Linux community discussions |
| RSS | Brendan Gregg | Performance and systems |
| GitHub | @torvalds | Linux creator |

### 🔒 Security / Privacy

| Type | Source | Description |
|------|--------|-------------|
| Reddit | r/netsec | Information security community |
| RSS | Krebs on Security | Investigative security journalism |
| RSS | Schneier on Security | Security analysis and commentary |

### 🌐 Web Development

| Type | Source | Description |
|------|--------|-------------|
| Reddit | r/webdev | Web development community |
| Reddit | r/javascript | JavaScript discussions and news |
| RSS | CSS-Tricks | Frontend tips and techniques |

### 🔤 Programming Languages / Compilers

| Type | Source | Description |
|------|--------|-------------|
| Reddit | r/ProgrammingLanguages | Programming language design and theory |
| Reddit | r/rust | Rust programming community |
| GitHub | rust-lang/rust | Rust language releases |
| GitHub | ziglang/zig | Zig language releases |

### 🤖 Embedded / Robotics / Hardware

| Type | Source | Description |
|------|--------|-------------|
| Reddit | r/robotics | Robotics research and projects |
| Reddit | r/embedded | Embedded systems development |
| RSS | Hackaday | Hardware hacking and projects |

### 🛠️ Open Source / DevTools

| Type | Source | Description |
|------|--------|-------------|
| RSS | GitHub Trending | Daily popular repositories |
| Reddit | r/commandline | Command line tools and tips |
| GitHub | neovim/neovim | Neovim editor releases |

### 🔬 Science / Research

| Type | Source | Description |
|------|--------|-------------|
| Reddit | r/science | Science news and discussions |
| RSS | Nature | Latest research highlights |
| RSS | Quanta Magazine | Accessible science journalism |

---

## 🤝 Contribute Your Sources

We welcome community contributions! If you have high-quality sources to share:

1. Fork the [Horizon repository](https://github.com/thysrael/Horizon)
2. Edit `data/presets.json` and add your source under the appropriate domain
3. Submit a Pull Request

**Contribution guidelines**:

- Ensure the source is **actively maintained** and regularly updated
- It should have a **high signal-to-noise ratio**
- Provide both `description` (English) and `description_zh` (Chinese)
- Add appropriate `tags` for keyword matching
- Place it under a fitting `domain`, or create a new one

Example format:

```json
{
  "type": "rss",
  "description": "Your source description",
  "description_zh": "你的信息源描述",
  "tags": ["topic1", "topic2"],
  "config": {
    "name": "Source Name",
    "url": "https://example.com/feed.xml",
    "category": "your-category"
  }
}
```

</div>
