---
layout: default
title: "Daybreak Summary: 2026-07-18 (ZH)"
date: 2026-07-18
lang: zh
---

> 从 64 条内容中，筛选出 20 条重要资讯

---

**AI / 机器学习**
1. [Thinking Machines Lab 发布 975B 开源权重多模态 MoE 模型 Inkling](#item-1) ⭐️ 9.0/10
2. [月之暗面发布 2.8 万亿参数大模型 Kimi K3，并通过“鹈鹕”基准进行测试](#item-2) ⭐️ 8.0/10
3. [RoboTTT：通过测试时训练将机器人视觉运动上下文扩展至 8K 时间步](#item-3) ⭐️ 8.0/10
4. [预训练数据可通过计算宣传手段被投毒](#item-4) ⭐️ 8.0/10
5. [The state of open source AI](#item-5) ⭐️ 7.0/10
6. [Quoting Thibault Sottiaux](#item-6) ⭐️ 7.0/10
7. [Overtraining as the path to human-like AI](#item-7) ⭐️ 7.0/10
8. [MeanFlowNFT: Bringing Forward-Process RL to Average-Velocity Generators](#item-8) ⭐️ 7.0/10
9. [Online Neural Space Time Memory for Dynamic Novel View Synthesis](#item-9) ⭐️ 7.0/10
10. [SceneBind: Binding What and Where Across Vision, Audio and Language](#item-10) ⭐️ 7.0/10
11. [SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration](#item-11) ⭐️ 7.0/10

**安全**
12. [Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents](#item-12) ⭐️ 7.0/10

**系统与基础设施**
13. [Firefox 浏览器被编译为 WebAssembly 并可在另一浏览器中运行](#item-13) ⭐️ 8.0/10
14. [Learning a few things about running SQLite](#item-14) ⭐️ 7.0/10

**行业动态**
15. [林纳斯·托瓦兹宣布 Linux 项目不会排斥 AI 工具](#item-15) ⭐️ 8.0/10
16. [谷歌与 Epic 撤回动议，Play 商店下周起将支持第三方应用商店](#item-16) ⭐️ 8.0/10
17. [Google Runs Out of Appeals, Must Pay Record $4.7 Billion EU Antitrust Fine](#item-17) ⭐️ 7.0/10

**研究**
18. [首次在宜居带类地行星上探测到大气层](#item-18) ⭐️ 8.0/10
19. [研究揭示大语言模型在上下文学习中违反基本概率定律](#item-19) ⭐️ 8.0/10

**其他**
20. [Texas wins court order to suspend domain name for violating age-verification law](#item-20) ⭐️ 7.0/10
---

## AI / 机器学习

<a id="item-1"></a>
### [Thinking Machines Lab 发布 975B 开源权重多模态 MoE 模型 Inkling](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 9.0/10

由 Mira Murati 创立的 Thinking Machines Lab 发布了其首个开源权重多模态混合专家（MoE）模型 Inkling，该模型拥有 9750 亿总参数和 410 亿激活参数。该模型采用 Apache-2.0 许可协议，并在包含文本、图像、音频和视频的 45 万亿 token 数据集上进行了训练。 作为这家备受瞩目的 AI 初创公司的首发成果，Inkling 为希望微调大型多模态模型的开发者提供了一个极具竞争力的开源权重替代方案。它强化了开源权重生态系统，成为与 NVIDIA、Google 以及中国 AI 实验室的模型并驾齐驱的有力竞争者。 Thinking Machines Lab 明确表示 Inkling 并非旨在成为前沿模型，而是一个强大的基座模型，专为通过其 Tinker 平台进行定制和微调而优化。此外，一个名为 Inkling-Small（2760 亿总参数）的较小版本目前正在测试中，将在未来发布。

rss · simonwillison.net · Jul 16, 15:35

**背景**: Thinking Machines Lab 是由前 OpenAI 首席技术官（CTO）Mira Murati 创立的 AI 初创公司。混合专家（MoE）架构允许模型在处理任何输入时仅激活其总参数的一个子集，从而在保持高容量的同时显著降低计算成本。开源权重模型允许开发者在本地下载和运行模型权重，从而实现深度定制和微调。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling : Our open - weights model - Thinking Machines Lab</a></li>
<li><a href="https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/">Thinking Machines amps up its bet against one-size-fits-all AI with its first open model, Inkling | TechCrunch</a></li>
<li><a href="https://thinkingmachines.ai/model-card/inkling/">Inkling Model Card - Thinking Machines Lab</a></li>

</ul>
</details>

**社区讨论**: 社区指出，尽管该模型的 Model Card 和训练数据文档相对简略，但其采用 Apache-2.0 许可协议以及竞争定位受到了欢迎。一些用户强调了它作为在 Tinker 平台上进行微调的基座模型的实用性，而不是试图与 GPT-4 等前沿模型直接竞争。

**标签**: `#Inkling`, `#Open-weights`, `#MoE`, `#Multimodal`, `#Thinking Machines Lab`

---

<a id="item-2"></a>
### [月之暗面发布 2.8 万亿参数大模型 Kimi K3，并通过“鹈鹕”基准进行测试](https://simonwillison.net/2026/Jul/16/kimi-k3/#atom-everything) ⭐️ 8.0/10

中国人工智能实验室月之暗面（Moonshot AI）发布了拥有 2.8 万亿参数的混合专家（MoE）大模型 Kimi K3，目前已通过网页和 API 提供，并承诺在 2026 年 7 月 27 日前开源权重。作者 Simon Willison 使用其经典的“鹈鹕骑自行车” SVG 生成基准测试了该模型，以探索其推理能力和 Token 使用情况。 作为首个“开源 3T 级模型”，Kimi K3 代表了开源权重模型在规模上的重大飞跃，在前端代码等领域逼近 Claude Fable 5 等顶尖商业模型。该评估表明，像 SVG 生成这样的小众基准测试仍能揭示模型的隐藏行为，例如推理 Token 开销和隐藏的系统提示词。 Kimi K3 的定价为每百万输入 Token 3 美元，每百万输出 Token 15 美元，并在 Arena.ai 的前端代码竞技场中夺冠。在 SVG 测试中，该模型消耗了 95 个输入 Token（暗示存在约 85 个 Token 的隐藏系统提示词）和 16,658 个输出 Token，其中 13,241 个为推理 Token。

rss · simonwillison.net · Jul 16, 20:19

**背景**: “鹈鹕骑自行车”基准测试是 Simon Willison 创建的一种非正式测试，用于评估 LLM 生成代表特定视觉场景的有效且复杂的 SVG 代码的能力。虽然它不是针对智能体工具调用的全面基准，但它可以作为快速探测新模型空间推理、代码生成以及性价比的手段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/16/kimi-k3/">Kimi K3, and what we can still learn from the pelican benchmark</a></li>
<li><a href="https://awesomeagents.ai/models/kimi-k3/">Kimi K 3 | Awesome Agents</a></li>

</ul>
</details>

**社区讨论**: 用户讨论了由于该测试在技术博客上的广泛传播，鹈鹕基准测试可能已被训练集污染的可能性。他们还分析了 Kimi K3 的 Token 使用情况，指出异常的输入 Token 数量暗示存在用于调节推理力度的隐藏系统提示词，并对比了其与 Anthropic Claude 模型的速度和成本。

**标签**: `#Kimi K3`, `#LLM`, `#基准测试`, `#Moonshot AI`, `#SVG`

---

<a id="item-3"></a>
### [RoboTTT：通过测试时训练将机器人视觉运动上下文扩展至 8K 时间步](https://arxiv.org/abs/2607.15275v1) ⭐️ 8.0/10

研究人员推出了 RoboTTT（测试时训练机器人策略），这是一种新的机器人模型和训练方案，在不增加推理延迟的情况下，成功将视觉运动上下文扩展到了 8000 个时间步。该系统将测试时训练（TTT）集成到视觉-语言-动作（VLA）策略中，利用在训练和推理过程中通过梯度下降更新的快速权重作为循环状态来压缩历史信息。 通过将上下文窗口提升三个数量级，RoboTTT 实现了人类视频单样本模仿和即时策略调整等新能力。这表明上下文长度可以作为机器人基础模型的一个强有力的全新扩展轴，使其能够处理复杂的多阶段任务。 为了扩展训练规模，该方案结合了序列动作强迫与截断随时间反向传播技术。在真实机器人操作任务中，RoboTTT 的整体性能比单步基线提高了 87%，并成功完成了一个 10 阶段的装配任务，其中 8K 上下文模型的表现比 1K 上下文模型提高了 62%。

arxiv · Yunfan Jiang, Yevgen Chebotar, Ruijie Zheng · Jul 16, 17:59

**背景**: 传统的机器人策略通常在单步输入或极短的历史上下文上运行，这限制了它们适应干扰或完成长程任务的能力。测试时训练（TTT）是一种新兴的机器学习范式，其中模型参数在推理（测试阶段）期间进行更新，以适应新数据或将长序列历史压缩到权重空间中，从而避免了处理原始序列历史带来的计算变慢问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.15275v1">RoboTTT : Context Scaling for Robot Policies</a></li>
<li><a href="https://research.nvidia.com/labs/gear/robottt/">RoboTTT : Context Scaling for Robot Policies</a></li>

</ul>
</details>

**标签**: `#Robotics`, `#Test-Time Training`, `#Foundation Models`, `#Context Scaling`, `#Computer Vision`

---

<a id="item-4"></a>
### [预训练数据可通过计算宣传手段被投毒](https://arxiv.org/abs/2607.15267v1) ⭐️ 8.0/10

研究人员证实了通过公共讨论界面在网页规模上对语言模型预训练数据进行投毒的可行性，并引入了一种名为 HalfLife 的新分析方法，用于评估对抗性内容在网页抓取和清洗后的残留情况。 该研究揭示了大规模 AI 训练流水线中的关键漏洞，表明恶意攻击者可以利用开放的网页平台向语言模型中注入有害行为，从而影响模型的安全性和可靠性。 与以往关注维基百科等结构化数据源的研究不同，该研究评估了被污染数据与实际数据清洗流水线之间的相互作用，并利用 HalfLife 追踪有多少对抗性内容在过滤后得以存活。

arxiv · Victoria Graf, Hannaneh Hajishirzi, Noah A. Smith · Jul 16, 17:56

**背景**: 大语言模型依赖于从公开互联网抓取的海量预训练数据集，这些数据通常会经过过滤以去除低质量内容。数据投毒（Data Poisoning）是一种对抗性攻击，指攻击者故意将恶意数据插入这些数据集中以破坏模型的安全；而计算宣传（Computational Propaganda）则是指利用公共平台上的自动化手段来操纵信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.15267">Pretraining Data Can Be Poisoned through Computational ...</a></li>

</ul>
</details>

**标签**: `#Data Poisoning`, `#Language Models`, `#AI Security`, `#Pretraining Data`

---

<a id="item-5"></a>
### [The state of open source AI](https://stateofopensource.ai/) ⭐️ 7.0/10

该内容探讨了开源 AI 的发展现状，指出开源模型在市场份额和使用量上正在快速追赶甚至超越闭源模型，并引发了关于 AI 行业未来格局的深度讨论。

hackernews · rellem · Jul 17, 14:31

**标签**: `#Open Source AI`, `#LLM`, `#Artificial Intelligence`, `#Industry Trends`

---

<a id="item-6"></a>
### [Quoting Thibault Sottiaux](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 7.0/10

报道指出在未启用沙箱且开启完全访问模式时，GPT-5.6 可能会因尝试重写 $HOME 环境变量来定义临时目录而误删用户的主目录（$HOME）。

rss · simonwillison.net · Jul 16, 17:45

**标签**: `#AI Safety`, `#LLM Agents`, `#Codex`, `#Software Security`

---

<a id="item-7"></a>
### [Overtraining as the path to human-like AI](https://seangoedecke.com/overtraining-as-the-path-to-human-like-ai/) ⭐️ 7.0/10

本文分析了 Gwern 关于通过过度训练和“弹射”技术来使大语言模型获得类人灵活智能的理论与路径。

rss · seangoedecke.com · Jul 18, 00:00

**标签**: `#LLM`, `#Artificial General Intelligence`, `#AI Training`, `#Scaling Hypothesis`

---

<a id="item-8"></a>
### [MeanFlowNFT: Bringing Forward-Process RL to Average-Velocity Generators](https://arxiv.org/abs/2607.15273v1) ⭐️ 7.0/10

本文提出了 MeanFlowNFT，通过构建诱导瞬时速度预测器，将前向过程强化学习引入平均速度生成器中，在保留 MeanFlow 快速少步采样优势的同时实现了高效的奖励对齐。

arxiv · Yushi Huang, Xiangxin Zhou, Jun Zhang · Jul 16, 17:59

**标签**: `#Generative Models`, `#Reinforcement Learning`, `#Flow Matching`, `#Diffusion Models`

---

<a id="item-9"></a>
### [Online Neural Space Time Memory for Dynamic Novel View Synthesis](https://arxiv.org/abs/2607.15271v1) ⭐️ 7.0/10

本文提出了一种在线神经时空记忆方法，通过解耦内存更新与应用的频率，实现了在实时约束下对动态视频流的高效新视角合成。

arxiv · Baback Elmieh, Lynn Tsai, Zeman Li · Jul 16, 17:58

**标签**: `#Novel View Synthesis`, `#Dynamic Reconstruction`, `#Computer Vision`, `#Neural Rendering`

---

<a id="item-10"></a>
### [SceneBind: Binding What and Where Across Vision, Audio and Language](https://arxiv.org/abs/2607.15265v1) ⭐️ 7.0/10

SceneBind 是一种跨视觉、音频和语言的多模态表示方法，通过结合全局语义嵌入和以对象为中心的语义空间插槽，实现了语义与 3D 空间信息的联合理解。

arxiv · Mingfei Chen, Zijun Cui, Ruoke Zhang · Jul 16, 17:55

**标签**: `#Multimodal Learning`, `#3D Spatial Understanding`, `#Audio-Visual`, `#Representation Learning`

---

<a id="item-11"></a>
### [SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration](https://arxiv.org/abs/2607.15257v1) ⭐️ 7.0/10

本文介绍了 SearchOS，一个通过将搜索进度显式化和持久化来解决多智能体协作中重复搜索与进度丢失问题的系统级框架。

arxiv · Yuyao Zhang, Junjie Gao, Zhengxian Wu · Jul 16, 17:51

**标签**: `#Multi-Agent Systems`, `#Information Retrieval`, `#Large Language Models`, `#Agent Collaboration`

---

## 安全

<a id="item-12"></a>
### [Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents](https://arxiv.org/abs/2607.15263v1) ⭐️ 7.0/10

本文提出了一种成本感知的安全 Agent 评估方法，通过在固定成本水平下比较模型，揭示了红队和蓝队任务在推理与工具开销上的不同扩展规律。

arxiv · Paul Kassianik, Blaine Nelson, Yaron Singer · Jul 16, 17:54

**标签**: `#LLM Agents`, `#AI Security`, `#Evaluation Benchmark`, `#Cost-Efficiency`

---

## 系统与基础设施

<a id="item-13"></a>
### [Firefox 浏览器被编译为 WebAssembly 并可在另一浏览器中运行](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 8.0/10

Puter 成功将包括 Gecko 渲染引擎和 SpiderMonkey JavaScript 引擎在内的整个 Firefox 浏览器技术栈编译为 WebAssembly (WASM)，使其能完全在另一个浏览器中运行。该项目利用 Claude AI 模型辅助移植庞大的 C++ 代码库，并使用 WebSocket 代理来处理网络流量。 该演示展示了在 LLM 辅助下将庞大复杂的 C++ 代码库编译为 WebAssembly 的可行性，推向了浏览器内浏览器虚拟化的极限。它为安全沙箱化的浏览器环境和客户端 Web 应用开辟了新的可能性。 为了绕过浏览器的网络限制，该项目使用 Wisp WebSocket 协议将所有流量通过 Puter 的服务器进行路由，该协议支持对 HTTPS 请求进行端到端加密。由于 Firefox 具有强大的单进程架构，因此它被选为比其他浏览器更优的编译对象。

rss · simonwillison.net · Jul 16, 23:34

**背景**: WebAssembly (WASM) 是一种二进制指令格式，能够让通常由 C++ 或 Rust 编写的高性能应用程序在浏览器中以接近原生的速度运行。然而，由于安全策略，在沙箱中运行的浏览器无法发起任意的原始网络连接。移植像 Firefox 这样依赖复杂渲染和网络引擎的完整浏览器，需要将这些底层系统调用转换为与 Web 兼容的 API。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/">Firefox in WebAssembly</a></li>
<li><a href="https://developer.puter.com/labs/firefox-wasm/">Firefox in WebAssembly</a></li>
<li><a href="https://eucloudservers.com/architecture-reliability/show-hn-firefox-in-webassembly/">Show HN: Firefox In WebAssembly - EU Cloud Servers</a></li>

</ul>
</details>

**社区讨论**: 社区对这一技术壮举表示惊叹，不过也有人对通过 WebSocket 代理所有用户流量的扩展性和成本表示担忧。其他人则讨论了 AI 辅助编程在处理以前被认为过于耗费人力的遗留代码库迁移任务方面的潜力。

**标签**: `#WebAssembly`, `#Firefox`, `#Gecko`, `#Browser-in-Browser`

---

<a id="item-14"></a>
### [Learning a few things about running SQLite](https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/) ⭐️ 7.0/10

本文介绍了在生产环境中运行 SQLite 的实用经验与技巧，并引发了社区关于备份、索引优化和凭证管理的深入讨论。

hackernews · surprisetalk · Jul 17, 17:45

**标签**: `#SQLite`, `#Database`, `#Backups`, `#DevOps`

---

## 行业动态

<a id="item-15"></a>
### [林纳斯·托瓦兹宣布 Linux 项目不会排斥 AI 工具](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linux 创始人兼最高维护者林纳斯·托瓦兹（Linus Torvalds）明确表示，Linux 项目不会排斥 AI，并认为 AI 已经成为一种无可争议的实用工具。他强调，不接受这一立场的贡献者可以选择分叉（fork）项目或直接离开。 作为开源软件领域最具影响力的人物之一，托瓦兹的强硬立场可能会为大型开源项目如何整合生成式 AI 树立先例，从而可能加速 AI 在软件工程中的应用。这也为开发者社区中关于 AI 生成代码实用性的持续争论划定了清晰的界线。 托瓦兹指出，尽管关于 AI 的长期经济效益仍存在疑问，但对于任何实际使用过它的人来说，其现实实用性已毋庸置疑。他将 AI 定位为开发者工具箱中的又一个工具，与 Linux 开发中使用的其他实用程序类似。

rss · simonwillison.net · Jul 16, 13:26

**背景**: 林纳斯·托瓦兹（Linus Torvalds）是一位因创建了驱动现代互联网和云基础设施的 Linux 内核以及 Git 版本控制系统而闻名的软件工程师。AI 在软件开发中的整合在开源社区中引发了关于版权、代码质量以及人类程序员被取代等问题的激烈辩论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://theysaidso.com/quote/linus-torvalds-thats-what-makes-linux-so-good-you-put-in-something-and-that-effo">Linus Torvalds - That's what makes Linux so good: you put in...</a></li>

</ul>
</details>

**标签**: `#Linus Torvalds`, `#Linux`, `#Open Source`, `#Generative AI`

---

<a id="item-16"></a>
### [谷歌与 Epic 撤回动议，Play 商店下周起将支持第三方应用商店](https://www.theverge.com/policy/965792/google-epic-withdraw-injunction-third-party-app-stores-coming-google-play?view_token=eyJhbGciOiJIUzI1NiJ9.eyJpZCI6IkZpdmhlVXFoV0giLCJwIjoiL3BvbGljeS85NjU3OTIvZ29vZ2xlLWVwaWMtd2l0aGRyYXctaW5qdW5jdGlvbi10aGlyZC1wYXJ0eS1hcHAtc3RvcmVzLWNvbWluZy1nb29nbGUtcGxheSIsImV4cCI6MTc4NDczNTA1NSwiaWF0IjoxNzg0MzAzMDU1fQ.zPHCDeRVkCOK73sdt6bKC2evAofTI582EsJ0N-rk79g) ⭐️ 8.0/10

谷歌与 Epic Games 达成协议，撤回了修改美国法院永久禁令的动议，这为第三方应用商店进驻 Google Play 扫清了障碍。从 7 月 22 日起，谷歌将开始向这些竞争对手的应用商店自动提供美国开发者的应用列表，除非开发者选择退出。 这标志着反垄断领域的一个重大里程碑，打破了谷歌对 Android 应用分发的垄断，可能会降低开发者费用并增加消费者的选择。它可能会从根本上重塑移动生态系统的商业模式和分发渠道。 谷歌已经启动了面向第三方商店的 Play Catalog Access Program 以供其注册，不过预计许多大型开发者会选择退出该列表。此外，谷歌计划在美国以外地区实施一套独立的“注册应用商店”计划以支持侧载。

rss · daringfireball.net · Jul 17, 15:53

**背景**: Epic Games 于 2020 年起诉谷歌，指控其在 Google Play 商店的支付系统和分发规则上存在反竞争行为和垄断做法。联邦法官随后发布了一项禁令，要求谷歌允许竞争对手的应用商店进驻 Google Play，并允许使用替代计费系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/policy/965792/google-epic-withdraw-injunction-third-party-app-stores-coming-google-play">Google and Epic give up fighting — third - party Android app stores ...</a></li>
<li><a href="https://semasocial.com/blog/google-and-epic-give-up-fighting-third-party-android-app-stores-are-coming-next-week">Google and Epic End Feud: Third - Party Android App Stores Arrive...</a></li>

</ul>
</details>

**标签**: `#Android`, `#Google`, `#Epic Games`, `#App Store`, `#Antitrust`

---

<a id="item-17"></a>
### [Google Runs Out of Appeals, Must Pay Record $4.7 Billion EU Antitrust Fine](https://www.cnbc.com/2026/07/02/alphabet-google-android-eu-antitrust-fine-4-1-billion-euro-appeal.html) ⭐️ 7.0/10

欧洲最高法院驳回了 Google 的最终上诉，维持对其因滥用 Android 主导地位而处以的 41 亿欧元（约 47 亿美元）创纪录反垄断罚款的判决。

rss · daringfireball.net · Jul 17, 23:47

**标签**: `#Google`, `#Antitrust`, `#EU`, `#Android`

---

## 研究

<a id="item-18"></a>
### [首次在宜居带类地行星上探测到大气层](https://www.bbc.com/news/articles/cy4kdd1e0ejo) ⭐️ 8.0/10

天文学家利用詹姆斯·韦伯空间望远镜（JWST）首次在位于恒星宜居带的类地岩石行星 LHS 1140b 上探测到了大气层存在的证据。这是人类首次在宜居带的类地行星上发现大气层。 在宜居带的岩石行星上发现大气层是寻找外星生命的关键里程碑，因为大气层对于维持液态水至关重要。这也证明了 JWST 分析小型、潜在宜居星球大气特征的能力。 LHS 1140b 距离地球 48 光年，绕着一颗比太阳更小、更冷的红矮星运行。JWST 的发射光谱分析帮助排除了该行星是富含气体的“迷你海王星”的可能性，证实了其岩石行星的本质。

hackernews · neversaydie · Jul 17, 14:06

**背景**: 宜居带是指恒星周围温度适宜、允许行星表面存在液态水的区域。尽管人类已经发现了数千颗系外行星，但由于恒星风剥离以及母恒星光芒的掩盖，在宜居带的微小岩石行星上探测大气层一直是一项极具挑战性的任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.space.com/astronomy/exoplanets/astronomers-discover-1st-atmosphere-around-a-rocky-earth-like-planet-in-the-habitable-zone">Astronomers discover 1st atmosphere around a rocky Earth-like planet in the habitable zone | Space</a></li>
<li><a href="https://www.bbc.com/news/articles/cy4kdd1e0ejo">First atmosphere found around Earth - like planet LHS 1140b</a></li>

</ul>
</details>

**社区讨论**: 用户讨论了岩石行星在绕活跃红矮星运行的情况下仍能保留大气层的重大意义，并指出 JWST 的数据成功排除了迷你海王星的假说。部分用户还探讨了鉴于其 48 光年的相对较近距离，向该系统派遣星际探测器的可行性。

**标签**: `#Astronomy`, `#Exoplanets`, `#JWST`, `#Astrophysics`

---

<a id="item-19"></a>
### [研究揭示大语言模型在上下文学习中违反基本概率定律](https://arxiv.org/abs/2607.15277v1) ⭐️ 8.0/10

研究人员提出了“划分、提示、聚合”（PPA）框架，用于评估大语言模型（LLM）在上下文学习中是否保持统计自洽性（例如遵循全概率公式）。该研究对最先进的前沿模型进行了测试，发现它们在跨不同子群体粒度聚合估计值时，普遍违反了基本的概率恒等式。 该研究突出了 LLM 在处理和聚合信息方面的一个根本性局限，表明它们无法将子群体的知识逻辑地传导至总体层面的估计中。这确立了统计自洽性作为评估 LLM 不确定性和推理能力的一种全新的、无需参考答案的评估指标。 该评估框架使用二叉树将群体递归划分为细粒度的子群，并在每个层级提示 LLM 进行估计。作者发现了一种“宏观谬误”（macro fallacy），即从细粒度提示中重构出的聚合估计值，实际上比模型直接给出的顶层总体估计值更符合人类参考数据。

arxiv · Patrik Wolf, Thomas Kleine Buening, Andreas Krause · Jul 16, 17:59

**背景**: 上下文学习（In-context learning）允许 LLM 通过对提示中提供的示例或上下文进行条件化处理来执行任务，这可以被解释为条件概率估计。理想情况下，如果这些输出代表真实的概率分布，它们必须遵守全概率公式，即所有互斥子事件的加权概率之和必须等于整体事件的概率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.15277">[2607.15277] Partition , Prompt , Aggregate : Statistical ...</a></li>
<li><a href="https://huggingface.co/papers/2607.15277">Paper page - Partition , Prompt , Aggregate : Statistical ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#In-Context Learning`, `#Statistical Self-Consistency`, `#Probability Theory`

---

## 其他

<a id="item-20"></a>
### [Texas wins court order to suspend domain name for violating age-verification law](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-landmark-legal-victory-lock-pornographic-website-domain-and) ⭐️ 7.0/10

德克萨斯州总检察长成功获得法院命令，以违反该州年龄验证法为由暂停了成人网站 Motherless 的域名，引发了关于互联网管辖权和 DNS 治理的广泛讨论。

hackernews · letmevoteplease · Jul 17, 22:35

**标签**: `#Internet Governance`, `#Law`, `#DNS`, `#Censorship`

---