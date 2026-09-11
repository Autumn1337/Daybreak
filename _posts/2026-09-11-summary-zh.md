---
layout: default
title: "Daybreak Summary: 2026-09-11 (ZH)"
date: 2026-09-11
lang: zh
---

> 从 43 条内容中，筛选出 20 条重要资讯

---

**AI / 机器学习**
1. [学者质疑 OpenAI 将未发表的数学成果用于模型训练与突破](#item-1) ⭐️ 8.0/10
2. [OpenAI 发布官方 Agents API，提供托管式 AI Agent 基础设施](#item-2) ⭐️ 8.0/10
3. [OpenAI 在发布 Navier-Stokes 方程突破时同步提供 Lean 4 形式化证明](#item-3) ⭐️ 8.0/10
4. [A positive resolution of the gap-entropy conjecture](#item-4) ⭐️ 8.0/10
5. [Cognition launches new SWE-2 model, Rivaling Fable 5.1 and GPT-Astra](#item-5) ⭐️ 7.0/10
6. [Extending Raschka's GPT-2: an MoE trained from scratch on an RTX 3090](#item-6) ⭐️ 7.0/10
7. [IdeaAMBIG: Benchmarking Implementation-Critical Gaps in Research-Idea Specifications](#item-7) ⭐️ 7.0/10
8. [Likelihood-free inference with nuisance parameters through normalizing flows](#item-8) ⭐️ 7.0/10
9. [Show-Harness: Just a VLM Agent Can Play Robots](#item-9) ⭐️ 7.0/10
10. [IBIB: A Protocol for Measuring Enterprise AI Systems by Serving Route, Not Model Identifier](#item-10) ⭐️ 7.0/10

**安全**
11. [Forgejo 发布针对仓库模板严重 RCE 漏洞的安全补丁](#item-11) ⭐️ 8.0/10
12. [Calif Research 展示 AI 辅助开发的微信零点击蠕虫“WeWorm”](#item-12) ⭐️ 8.0/10

**开发工具**
13. [Shopify 放弃 React Native，全面回归 Swift 与 Kotlin 原生开发](#item-13) ⭐️ 8.0/10
14. [Trynix.dev 利用 QEMU-WASM 在浏览器中直接运行任意 Nix 软件包](#item-14) ⭐️ 8.0/10

**系统与基础设施**
15. [微软官方将 Rust 提升为内部 Tier-1 系统开发语言](#item-15) ⭐️ 8.0/10
16. [Neki – Sharded Postgres](#item-16) ⭐️ 7.0/10

**行业动态**
17. [Automattic Minus Matt](#item-17) ⭐️ 7.0/10
18. [Hitachi launches CO2 heat pump water heaters with solar-friendly tariff controls](#item-18) ⭐️ 6.0/10

**研究**
19. [Optimal Low-Rank Quantum State Tomography with Bounded-Sample Joint Measurements](#item-19) ⭐️ 7.0/10
20. [Technique for Manipulating Satellite Photos Now Reveals Ancient Images (2025)](#item-20) ⭐️ 6.0/10
---

## AI / 机器学习

<a id="item-1"></a>
### [学者质疑 OpenAI 将未发表的数学成果用于模型训练与突破](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

在 OpenAI 宣布其内部模型对复杂数学难题取得突破后，包括 Andreas Thom 和 Tristan Buckmaster 在内的数学家提出了严重伦理质疑，询问该模型是否在未经授权和署名的情况下吸收了学者通过对话输入的未发表研究成果。 这场争议凸显了商业 AI 数据收集模式与知识产权、学术署名等传统学术规范之间的严重冲突。如果研究人员无法信任商业 AI 平台对其未发表构想的保密性，将严重破坏信任体系并阻碍 AI 在顶尖学术研究中的应用。 研究人员担心，学者输入的 Prompt 可能会在预训练或微调阶段改善大语言模型的潜空间表示，从而造成模型随后通过强化学习“独立”解决开放难题的假象。学者们正敦促 OpenAI 公开内部数据审计结果，透明证明匿名化的用户交互数据是否对其宣称的成果产生了影响。

hackernews · pred_ · Sep 10, 06:49

**背景**: 大型语言模型提供商通常会留存用户对话用于模型评估与再训练，除非用户明确选择退出。在高等数学研究中，学者常使用 AI 工具测试未验证的猜想，这在商业前沿模型的数据留存政策下引发了潜在的知识产权泄露风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.progressiverobot.com/2026/09/10/openai-math-mathematicians-want-proof-didnt-use-their-work/">OpenAI Math Risk: Mathematicians Want Definitive Proof</a></li>
<li><a href="https://archive.ph/K585q">After Buckmaster, Thom Too Accuses OpenAI of Using Unpublished Research</a></li>

</ul>
</details>

**社区讨论**: 社群讨论普遍将 OpenAI 的行为比作不守伦理的学术合作者——即盗用同僚未发表的突破性创意却不予署名。虽然部分观点认为在形式化数学上的强化学习确实可能带来独立的真突破，但多数人保持怀疑，质疑 AI 在开放难题上的迅速进展是否在很大程度上依赖于成千上万学者输入的提示词。

**标签**: `#OpenAI`, `#AI Ethics`, `#LLM`, `#Data Privacy`, `#Research`

---

<a id="item-2"></a>
### [OpenAI 发布官方 Agents API，提供托管式 AI Agent 基础设施](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 8.0/10

OpenAI 官方发布了 Agents API 及其配套的 OpenAI Agents SDK，为开发者提供托管式基础设施，用于构建、编排和运行具备状态的 AI Agent 工作流。该平台提供了内置的工具集成、状态管理和多 Agent 协同机制，免去了开发者自建运行环境与底座框架的负担。 这一发布标志着 AI Agent 基础设施正在向标准化、平台化的云服务演进。通过接管复杂的状态持久化与环境执行，OpenAI 简化了 Agent 在无服务器及云原生架构中的部署流程，同时也重新定义了 Agent 的抽象层级。 该 API 支持在无状态环境中实现状态持久化与工具管理，并提供了自托管沙箱（self-hosted sandbox）选项以缓解厂商锁定问题。底层的 Agents SDK 保持轻量且跨提供商通用，既支持 OpenAI API，也兼容 100 多种其他大语言模型。

hackernews · aquir · Sep 10, 19:43

**背景**: AI Agent 是由大语言模型（LLM）驱动的自主应用，能够通过与代码解释器或自定义 API 等外部工具交互来独立完成多步骤任务。传统上，构建可靠的 Agent 需要编写自定义的“Harness”（运行框架），用于处理状态持久化、内存管理、工具执行和错误处理，而这在 Serverless 等无状态计算环境中往往实现难度极高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.github.io/openai-agents-python/">OpenAI Agents SDK</a></li>
<li><a href="https://github.com/openai/openai-agents-python">GitHub - openai / openai - agents -python: A lightweight, powerful...</a></li>

</ul>
</details>

**社区讨论**: 开发者社区对托管 API 与利用本地 QEMU 虚拟机自建基础设施的利弊展开了讨论。尽管部分开发者对厂商锁定表达了担忧并希望能直接获取推理 Token，但也有不少人对自托管沙箱等功能表示赞赏，认为这有助于降低迁移门槛。

**标签**: `#OpenAI`, `#AI Agents`, `#LLM`, `#API`, `#DevTools`

---

<a id="item-3"></a>
### [OpenAI 在发布 Navier-Stokes 方程突破时同步提供 Lean 4 形式化证明](https://www.johndcook.com/blog/2026/09/09/formal-method-revolution/) ⭐️ 8.0/10

OpenAI 宣布证明了一个关于流体力学 Navier-Stokes 方程的长期数学难题，并同步发布了使用 Lean 4 编写的形式化证明。 将 AI 生成的数学突破与形式化证明助手相结合，为科学严谨性树立了新范式，使得复杂的数学证明能够被自动验证，而不必完全依赖漫长的人工同行评审。 尽管公众注意力大多集中在数学成果本身，但文章强调了引入 Lean 4 的关键作用，这确保了 AI 驱动的数学发现可以通过机器验证达到绝对的逻辑正确性。

rss · johndcook.com · Sep 9, 12:43

**背景**: Navier-Stokes 方程用于描述流体的运动规律，是物理与应用数学的核心基础，也是著名的千禧年大奖难题之一。Lean 4 是一种交互式定理证明器和编程语言，能够让数学家和计算机科学家将证明形式化，从而让计算机严格验证其正确性。

**标签**: `#Lean 4`, `#Formal Verification`, `#AI for Math`, `#OpenAI`, `#Navier-Stokes`

---

<a id="item-4"></a>
### [A positive resolution of the gap-entropy conjecture](https://arxiv.org/abs/2609.10529v1) ⭐️ 8.0/10

作者证明了高斯臂设置下最佳臂识别问题的 Gap-Entropy 猜想，确定了期望采样复杂度的紧致界限。

arxiv · P. M. Aronow, Nathan Kallus, Patrick Lopatto · Sep 9, 17:57

**标签**: `#Multi-Armed Bandits`, `#Theoretical ML`, `#Best-Arm Identification`, `#Information Theory`

---

<a id="item-5"></a>
### [Cognition launches new SWE-2 model, Rivaling Fable 5.1 and GPT-Astra](https://cognition.com/blog/swe-2) ⭐️ 7.0/10

Cognition 宣布推出新的 SWE-2 软件工程模型，但在社区中因新旧 Benchmark 上的巨大性能差距而引发关于模型过拟合的严重质疑。

hackernews · seelos · Sep 10, 15:29

**标签**: `#AI/ML`, `#LLM`, `#Software Engineering`, `#AI Agents`, `#Benchmarks`

---

<a id="item-6"></a>
### [Extending Raschka's GPT-2: an MoE trained from scratch on an RTX 3090](https://www.gilesthomas.com/2026/09/gpt-2-to-moe) ⭐️ 7.0/10

作者基于 Sebastian Raschka 的开源代码扩展实现了混合专家（MoE）架构，并在单张 RTX 3090 上从头训练了一个拥有 4.46 亿总参数、2.2 亿活跃参数的 GPT-2 MoE 模型。

rss · gilesthomas.com · Sep 10, 18:45

**标签**: `#Mixture of Experts`, `#LLM`, `#GPT-2`, `#PyTorch`, `#Machine Learning`

---

<a id="item-7"></a>
### [IdeaAMBIG: Benchmarking Implementation-Critical Gaps in Research-Idea Specifications](https://arxiv.org/abs/2609.10539v1) ⭐️ 7.0/10

IdeaAMBIG 是一个包含 660 个样例的基准数据集，用于评估 AI 智能体在识别和解决研究方法描述中影响代码实现的模糊性缺陷方面的能力。

arxiv · Yiling Ma, Yilun Zhao, Sihong Wu · Sep 9, 17:59

**标签**: `#AI Agents`, `#LLM Benchmarks`, `#Code Generation`, `#Reproducibility`

---

<a id="item-8"></a>
### [Likelihood-free inference with nuisance parameters through normalizing flows](https://arxiv.org/abs/2609.10534v1) ⭐️ 7.0/10

本文提出了一种利用正规化流（Normalizing Flows）进行包含干扰参数的无似然推断方法，能够自动发现接近枢轴的统计量并提高假设检验的效率与速度。

arxiv · Phil Assheton · Sep 9, 17:58

**标签**: `#Normalizing Flows`, `#Likelihood-Free Inference`, `#Statistical Inference`, `#Machine Learning`

---

<a id="item-9"></a>
### [Show-Harness: Just a VLM Agent Can Play Robots](https://arxiv.org/abs/2609.10522v1) ⭐️ 7.0/10

Show-Harness 通过构建紧凑的语义动作接口，实现了利用视觉语言模型（VLM）进行零样本或低成本微调的机器人物理控制。

arxiv · Yanzhe Chen, Zechen Bai, Zhijun Cao · Sep 9, 17:53

**标签**: `#Embodied AI`, `#Vision-Language Models`, `#Robotics`, `#Autonomous Agents`

---

<a id="item-10"></a>
### [IBIB: A Protocol for Measuring Enterprise AI Systems by Serving Route, Not Model Identifier](https://arxiv.org/abs/2609.10494v1) ⭐️ 7.0/10

论文提出了 IB2 评估协议，主张通过 Serving Route 而非仅凭 Model Identifier 来测量企业级 AI 系统的实际可用能力与可靠性。

arxiv · Blake Stenstrom, Charangan Vasantharajan, Brian Sathianathan · Sep 9, 17:31

**标签**: `#AI Evaluation`, `#Enterprise AI`, `#Benchmarks`, `#LLM`, `#AI Infrastructure`

---

## 安全

<a id="item-11"></a>
### [Forgejo 发布针对仓库模板严重 RCE 漏洞的安全补丁](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md) ⭐️ 8.0/10

Forgejo 发布了 16.0.4 版本，修复了存在于 16.0.3 及更早版本中的严重远程代码执行（RCE）漏洞。该漏洞允许恶意仓库模板在新仓库初始化过程中执行任意代码。 自托管 Git 平台中的远程代码执行漏洞会对服务器基础设施和企业流水线构成直接的严重安全威胁。使用 Forgejo 的系统管理员和 DevOps 工程师应立即升级以保护其实例安全。 该漏洞源于仓库创建工作流：Forgejo 在克隆模板后会删除 `.git` 目录，对 `.forgejo/template` 中的文件进行变量扩展，随后重新初始化 Git。恶意设计的模板扩展文件能够在 Git 初始化阶段进行干预，从而触发代码执行。

hackernews · weierstass · Sep 10, 15:57

**背景**: Forgejo 是一款热门的开源自托管 Git 服务平台，最初作为 Gitea 的社区驱动分支衍生而来。它包含模板仓库等功能，允许用户使用预定义的文件结构和变量快速创建新项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49645907">Forgejo <= 16 . 0 . 3 Critical RCE | Hacker News</a></li>
<li><a href="https://memedata.com/post/144733">Forgejo <= 16 . 0 . 3 严重远程代码执行漏洞</a></li>

</ul>
</details>

**社区讨论**: 社区讨论集中在 PR 中描述的模板扩展漏洞的技术细节上。Gitea 维护者指出 Gitea 不受这些漏洞影响，同时参与者还探讨了安全报告的透明度以及 Forgejo 关于禁止 AI 生成代码贡献的政策。

**标签**: `#Security`, `#Forgejo`, `#RCE`, `#Vulnerability`, `#Git`

---

<a id="item-12"></a>
### [Calif Research 展示 AI 辅助开发的微信零点击蠕虫“WeWorm”](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 8.0/10

Calif Research 展示了名为 WeWorm 的演示程序，这是首个能通过微信通话在 iOS 和 Android 之间传播的零点击蠕虫。在 AI 的辅助下，研究团队仅用两天时间就发现了相关漏洞并开发出远程代码执行（RCE）利用代码，随后在一周内完成了整个蠕虫的构建。 这项研究突显了生成式 AI 如何大幅加速漏洞利用的开发周期，将过去需要大型团队耗时数月的工程压缩至仅需几天。这标志着网络威胁格局的重大转变，AI 赋能的网络攻击对拥有庞大用户基础的全球即时通讯软件构成了前所未有的风险。 该攻击完全不需要受害者进行任何交互，无论接收者是否接听微信 VoIP 通话或听到声音，攻击都能成功执行。AI 工具承担了绝大部分自动化分析和利用代码撰写，人类研究人员则主要提供战略目标选择与安全测试指导。

rss · simonwillison.net · Sep 10, 00:56

**背景**: 零点击（zero-click）漏洞利用是一种无需受害者进行任何操作（如点击链接或打开附件）即可感染目标设备的网络攻击，极具隐蔽性和危险性。远程代码执行（RCE）漏洞则允许攻击者在受害者设备上远程运行任意指令，通常会导致账号或系统被完全控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.infosecurity-magazine.com/news/wechat-zeroclick-worm-hijack/">Researchers Build WeChat Zero-Click Worm Hijacking Phones via Calls - Infosecurity Magazine</a></li>
<li><a href="https://securityboulevard.com/2026/09/using-ai-calif-creates-demo-wechat-exploit-that-spreads-through-phone-calls/">Using AI, Calif Creates Demo WeChat Exploit that Spreads Through Phone Calls - Security Boulevard</a></li>
<li><a href="https://www.techtimes.com/articles/327153/20260910/wechat-zero-click-worm-built-ai-days-voip-bug-put-billion-accounts-risk.htm">WeChat Zero-Click Worm Built by AI in Days: VoIP Bug Put Billion Accounts at Risk</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Zero-Click`, `#Cybersecurity`, `#LLM`, `#Exploitation`

---

## 开发工具

<a id="item-13"></a>
### [Shopify 放弃 React Native，全面回归 Swift 与 Kotlin 原生开发](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify 宣布改变其移动开发战略，放弃 React Native 跨平台框架，全面回归使用 Swift（iOS）和 Kotlin（Android）进行原生应用开发。 作为 React Native 最具代表性的企业支持者之一，Shopify 重回原生开发对整个移动开发领域的架构选型具有风向标意义。这表明 AI 辅助编程工具大幅降低了维护多端原生代码库的门槛，直接冲击了跨平台框架的核心价值主张。 这一转变很大程度上得益于 AI 编程助手的发展，相较于五年前，AI 极大降低了同时维护 Swift 和 Kotlin 两套原生代码的阻力。全面原生化还消除了抽象层的性能损耗，实现了更小的应用包体积和更优异的运行速度。

hackernews · fnthawar2 · Sep 10, 14:09

**背景**: React Native 是由 Meta 开发的开源框架，允许开发者使用 JavaScript 和 React 同时构建 iOS 与 Android 应用。尽管跨平台框架主打多端代码共享的便利，但使用 Swift（苹果）和 Kotlin（谷歌）等官方原生语言能直接调用系统底层 API，提供最佳的运行性能与原生 UI 体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://shopify.engineering/back-to-native">Native is now the future of mobile at Shopify (2026) - Shopify</a></li>

</ul>
</details>

**社区讨论**: 社区中的原生开发者对此表示高度认同，认为跨平台抽象层在应用规模扩大后往往会成为瓶颈。许多讨论指出 AI 工具（如 Codex）能够极快地在 Swift 与 Kotlin 之间转换代码，但也强调在调试和边界处理上仍需人工工程师主导。

**标签**: `#React Native`, `#Swift`, `#Kotlin`, `#Mobile Development`, `#Shopify`

---

<a id="item-14"></a>
### [Trynix.dev 利用 QEMU-WASM 在浏览器中直接运行任意 Nix 软件包](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 8.0/10

开发者 Farid Zakaria 推出了 trynix.dev，这是一个基于浏览器的工具，利用编译为 WebAssembly 的 QEMU 虚拟机运行 x86_64 Linux 环境。用户可以通过 URL 参数直接启动并体验过去 13 年中的任意 Nix 软件包，同时项目还推出了无需服务器成本的 GitHub Action（`trynix-preview`）用于 PR 构建的实时预览。 该项目展示了结合 WebAssembly 与 Linux 模拟的巨大潜力，实现了完全在客户端进行的软件测试以及历史环境验证。此外，它消除了对专用服务器托管的需求，极大地降低了代码审查和 GitHub PR 构建预览的门槛与成本。 该基于浏览器的虚拟机运行带有串口终端界面的 x86_64 Linux 环境，涵盖了 nixpkgs 过去 13 年间超过 31 万个软件包版本。配套工具 `trynix-preview` 可自动在 PR 下留言提供体验链接，使审查者无需后端服务器基础设施，直接在浏览器中即可启动最新编译的代码。

rss · simonwillison.net · Sep 10, 23:44

**背景**: Nix 是一款纯函数式软件包管理器，以构建高度确定性和跨时间完全可复现的开发环境而闻名。QEMU 是一个开源的机器模拟器与虚拟机，现在可以通过编译为 WebAssembly（Wasm）直接在现代网页浏览器中运行原生二进制架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fzakaria.com/2026/09/04/any-nix-package-live-in-your-browser">Any Nix package , live in your browser | Farid Zakaria’s Blog</a></li>
<li><a href="https://discourse.nixos.org/t/any-nix-package-live-in-your-browser/79962">Any Nix package , live in your browser - Links - NixOS Discourse</a></li>

</ul>
</details>

**标签**: `#WebAssembly`, `#Nix`, `#DevTools`, `#QEMU`, `#GitHub Actions`

---

## 系统与基础设施

<a id="item-15"></a>
### [微软官方将 Rust 提升为内部 Tier-1 系统开发语言](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 8.0/10

微软官方宣布将 Rust 提升为其内部工程体系中的“Tier-1 语言”，为其提供开发工具、合规审查以及平台集成的全面支持。这意味着内部团队在使用 Rust 进行从本地开发到生产部署的全流程中，都能获得全套安全工具链的官方保障。 这一举措巩固了 Rust 作为底层系统编程中传统 C/C++ 成熟替代方案的地位。通过优先推行具备内存安全特性的语言，微软旨在从源头上大幅减少内存损坏类安全漏洞——这类漏洞历史上占据了微软已知安全漏洞的约 70%。 在微软内部获得 Tier-1 状态意味着工程团队拥有从开发到生产的标准化“铺平路径”（paved path），包含官方构建的工具链、质量控制工作流和合规工具。这也印证了此前关于 Rust 将更深度集成到微软原生 MSVC 编译器工具链中的传闻。

hackernews · mmastrac · Sep 10, 13:39

**背景**: 传统系统编程高度依赖 C 和 C++，这两门语言需要手动管理内存，容易引发缓冲区溢出等严重安全漏洞。Rust 是一门现代系统语言，能够在编译期强制保证内存安全，且无需承担垃圾回收（Garbage Collection）带来的性能开销。在顶级软件厂商中被列为“Tier-1”语言，意味着该语言获得了全公司层面的顶级工具链支持、资源投入和架构优先权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier-1 Language at Microsoft</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rust_(programming_language)">Rust (programming language ) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 开发者社区普遍认为，这一声明印证了 Rust 已经成长为对标 C++ 和 C# 的严肃企业级系统语言，生态成熟度显著领先于 Zig 等更年轻的新兴语言。社区还特别关注了微软试图借助自动化工具将大规模遗留 C/C++ 代码重构迁移至 Rust 的长期愿景。

**标签**: `#Rust`, `#Microsoft`, `#Systems Programming`, `#Memory Safety`, `#C++`

---

<a id="item-16"></a>
### [Neki – Sharded Postgres](https://planetscale.com/blog/introducing-neki) ⭐️ 7.0/10

PlanetScale 发布了名为 Neki 的分片 PostgreSQL 解决方案，旨在提升 Postgres 的海量数据扩展与分布式处理能力。

hackernews · simon_weber · Sep 10, 15:43

**标签**: `#PostgreSQL`, `#PlanetScale`, `#Sharding`, `#Distributed Systems`, `#Databases`

---

## 行业动态

<a id="item-17"></a>
### [Automattic Minus Matt](https://feed.tedium.co/link/15204/17444080/matt-mullenweg-automattic-leave-absence) ⭐️ 7.0/10

WordPress 母公司 Automattic 的创始人 Matt Mullenweg 已被强制休假。

rss · tedium.co · Sep 10, 05:29

**标签**: `#WordPress`, `#Automattic`, `#Matt Mullenweg`, `#Open Source`, `#Leadership`

---

<a id="item-18"></a>
### [Hitachi launches CO2 heat pump water heaters with solar-friendly tariff controls](https://www.pv-magazine.com/2026/09/07/hitachi-launches-co2-heat-pump-water-heaters-with-solar-friendly-tariff-controls/) ⭐️ 6.0/10

日立推出配备太阳能及电网电价智能控制功能的 CO2 热泵热水器，旨在优化光伏发电利用并降低用户用电成本。

hackernews · thelastgallon · Sep 9, 14:54

**标签**: `#Heat Pump`, `#Renewable Energy`, `#Smart Grid`, `#Energy Efficiency`, `#IoT`

---

## 研究

<a id="item-19"></a>
### [Optimal Low-Rank Quantum State Tomography with Bounded-Sample Joint Measurements](https://arxiv.org/abs/2609.10514v1) ⭐️ 7.0/10

本文确定了在每次测量最多作用于 $t$ 个样本的限制下，估计 $d$ 维空间中秩至多为 $r$ 的低秩量子态所需的最优样本复杂度。

arxiv · Ashwin Nayak, Xingyu Zhou · Sep 9, 17:48

**标签**: `#Quantum Computing`, `#Quantum Information`, `#Sample Complexity`, `#Theoretical Computer Science`

---

<a id="item-20"></a>
### [Technique for Manipulating Satellite Photos Now Reveals Ancient Images (2025)](https://spinoff.nasa.gov/Manipulating_Satellite_Photos_Now_Reveals_Ancient_Images) ⭐️ 6.0/10

NASA 用于处理卫星照片的解相关拉伸（DStretch）图像处理技术，被成功应用于揭示和还原褪色的古老岩画与壁画。

hackernews · gumby · Sep 10, 15:29

**标签**: `#Image Processing`, `#Remote Sensing`, `#NASA`, `#Archaeology`, `#Computer Vision`

---