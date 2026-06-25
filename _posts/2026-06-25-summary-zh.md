---
layout: default
title: "Daybreak Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> 从 47 条内容中，筛选出 20 条重要资讯

---

**AI / 机器学习**
1. [OpenAI 联合博通推出首款定制 AI 推理芯片 Jalapeno](#item-1) ⭐️ 9.0/10
2. [Krea 发布 Krea 2：最先进的 12B 参数开源权重图像生成模型](#item-2) ⭐️ 8.0/10
3. [InSight：通过可控 VLA 模型实现机器人自主技能获取](#item-3) ⭐️ 8.0/10
4. [OpenThoughts-Agent：用于智能体模型的开源数据整理管道](#item-4) ⭐️ 8.0/10
5. [Computer use in Gemini 3.5 Flash](#item-5) ⭐️ 7.0/10
6. [GLM-5.2 is a step change for open agents](#item-6) ⭐️ 7.0/10
7. [Thoughts on Role Confusion](#item-7) ⭐️ 7.0/10
8. [FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation](#item-8) ⭐️ 7.0/10
9. [Real vs. Complex Spectral Bases for Neural Operators: The Role of Green's Function Alignment](#item-9) ⭐️ 7.0/10
10. [IV-CoT: Implicit Visual Chain-of-Thought for Structure-Aware Text-to-Image Generation](#item-10) ⭐️ 7.0/10
11. [Grading the Grader: Lessons from Evaluating an Agentic Data Analysis System](#item-11) ⭐️ 7.0/10

**开发工具**
12. [PR spam today looks like email spam in the early 2000s](#item-12) ⭐️ 7.0/10
13. [Show HN: Nub – A Bun-like all-in-one toolkit for Node.js](#item-13) ⭐️ 7.0/10
14. [simonw/browser-compat-db](#item-14) ⭐️ 7.0/10
15. [RubyLLM: A Ruby framework for all major AI providers](#item-15) ⭐️ 6.0/10

**系统与基础设施**
16. [45°C cooling design cuts data center water use to near zero](#item-16) ⭐️ 7.0/10

**行业动态**
17. [高通宣布以近 40 亿美元收购 AI 初创公司 Modular](#item-17) ⭐️ 8.0/10
18. [There are a few things that I look back on as my mistakes in the early days](#item-18) ⭐️ 7.0/10

**研究**
19. [New Bounds for the Last Iterate of the Stochastic subGradient Method](#item-19) ⭐️ 7.0/10
20. [World Models in Pieces: Structural Certification for General Agents](#item-20) ⭐️ 7.0/10
---

## AI / 机器学习

<a id="item-1"></a>
### [OpenAI 联合博通推出首款定制 AI 推理芯片 Jalapeno](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI 推出了其首款定制设计的 AI 推理芯片“Jalapeno”，该芯片是与博通（Broadcom）合作开发并由台积电（TSMC）代工制造。据报道，该芯片从设计到投产仅用了九个月，且 OpenAI 自身的 AI 模型也辅助了其设计与优化过程。 这标志着 OpenAI 在构建完整软硬件技术栈战略中迈出了关键一步，减少了对英伟达（Nvidia）昂贵 GPU 的严重依赖，并有望将推理成本降低约 50%。这加剧了 AI 巨头之间的定制芯片竞争，使 OpenAI 与谷歌、Meta 等自行设计芯片的竞争对手齐头并进。 Jalapeno 专门针对大语言模型（LLM）的推理而非训练进行了定制，Celestica 协助了其电路板和机架系统的集成。博通首席执行官指出，与传统 AI GPU 相比，该定制处理器可实现约 50% 的成本节约。

hackernews · jamdesk · Jun 24, 17:47

**背景**: AI 工作负载分为训练（教导模型）和推理（运行已训练的模型以生成响应）。随着 ChatGPT 等 AI 服务扩展到数百万用户，推理成本成为主要的运营支出，这促使各公司设计针对其特定软件架构进行优化的专用集成电路（ASIC）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/">OpenAI unveils its first custom chip , built by Broadcom</a></li>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://qz.com/openai-broadcom-jalapeno-custom-ai-chip-062426">OpenAI unveils first custom - built AI chip designed with Broadcom</a></li>

</ul>
</details>

**社区讨论**: 用户对 OpenAI 的模型加速了芯片设计过程这一说法表示怀疑，有人认为这只是营销噱头。此外，社区讨论了台积电的代工角色，并探讨了将大语言模型权重直接固化到硅片中以最大化吞吐量的技术可行性。

**标签**: `#OpenAI`, `#Custom Silicon`, `#AI Chip`, `#Broadcom`, `#Inference`

---

<a id="item-2"></a>
### [Krea 发布 Krea 2：最先进的 12B 参数开源权重图像生成模型](https://www.krea.ai/blog/krea-2-technical-report) ⭐️ 8.0/10

Krea 开源了拥有 120 亿参数的文本生成图像基础模型 Krea 2，发布了“Raw”和“Turbo”两个版本的模型权重，并附带了一份详细介绍其训练、数据清洗和基础设施的技术报告。 作为一款高性能的本地可运行模型，Krea 2（尤其是 Turbo 版本）以极快的生成速度提供了接近闭源顶尖模型的性能，推动了面向创作者和开发者的开源权重生态系统的发展。 该模型采用了 12B 参数的稠密扩散 Transformer (DiT) 骨干网络、Qwen Image VAE 以及 Qwen3-VL 文本编码器，其中 Turbo 版本经过蒸馏，仅需 8 步即可在 2 秒内生成 2K 分辨率的图像。

hackernews · mattnewton · Jun 23, 15:31

**背景**: 扩散 Transformer (DiT) 已成为最先进图像生成模型的标准架构，它将扩散模型与 Transformer 模块相结合。开源权重模型允许用户在本地（例如通过 ComfyUI）运行、微调和集成人工智能系统，而无需依赖云端 API，尽管这通常需要较强的 GPU 资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.krea.ai/blog/krea-2-technical-report">Krea 2 Technical Report - Krea</a></li>
<li><a href="https://www.krea.ai/krea-2-open-source">Krea 2 Open-Source: RAW and Turbo Image Models</a></li>
<li><a href="https://aiweekly.co/alerts/krea-releases-12b-image-weights-for-2-second-2k-generation">Krea Releases 12B Image Weights for 2-Second 2K Generation | AI Weekly</a></li>

</ul>
</details>

**社区讨论**: 用户赞扬了 Turbo 版本的速度和质量，指出其表现优于其他本地可托管模型，但也有人指出它在处理复杂的逻辑提示词时仍有困难，并质疑传统的文本生成图像模型是否已落后于新兴的智能体图生图工作流。

**标签**: `#Text-to-Image`, `#Open-Weights`, `#Generative AI`, `#Machine Learning`

---

<a id="item-3"></a>
### [InSight：通过可控 VLA 模型实现机器人自主技能获取](https://arxiv.org/abs/2606.24884v1) ⭐️ 8.0/10

研究人员推出了 InSight 框架，通过在基元动作级别使视觉-语言-动作（VLA）模型具备可控性，从而实现自主技能获取。该框架利用视觉语言模型（VLM）引导的数据飞轮来识别、尝试并整合缺失的动作基元，无需人类演示。 传统的 VLA 模型受限于其训练数据中包含的特定技能。InSight 突破了这一限制，允许机器人持续学习并组合出全新的长程任务，这显著推动了具身智能和自主机器人操控技术的发展。 该框架分两个阶段运行：首先，利用 VLM 规划分解和末端执行器位姿将演示分割为带标签的基元；其次，利用 VLM 提出低级控制以获取缺失的基元。InSight 在仿真和真实世界环境中的翻转积木、清扫和倾倒等任务上成功完成了验证。

arxiv · Maggie Wang, Lars Osterberg, Stephen Tian · Jun 23, 17:59

**背景**: 视觉-语言-动作（VLA）模型是专为机器人设计的 AI 系统，可将视觉输入和语言指令直接映射为物理动作。虽然这类模型非常强大，但其性能往往受限于缺乏细粒度的控制，以及为每个新任务收集多样化人类演示的高昂成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://insight-vla.github.io/">InSight : Self - Guided Skill Acquisition via Steerable VLAs</a></li>
<li><a href="https://arxiv.org/html/2606.24884">InSight : Self - Guided Skill Acquisition via Steerable VLAs</a></li>

</ul>
</details>

**标签**: `#VLA Models`, `#Robotics`, `#Embodied AI`, `#Skill Acquisition`

---

<a id="item-4"></a>
### [OpenThoughts-Agent：用于智能体模型的开源数据整理管道](https://arxiv.org/abs/2606.24855v1) ⭐️ 8.0/10

研究人员推出了 OpenThoughts-Agent（简称 OT-Agent），这是一个用于训练通用智能体语言模型的完全开源数据整理管道。通过进行 100 多次消融实验，他们构建了一个包含 10 万条数据的训练集并对 Qwen3-32B 进行微调，在七个智能体基准测试中实现了 44.8% 的平均准确率。 现有的智能体模型开源工作通常只针对单一基准，限制了其泛化能力。OT-Agent 通过提供系统化的数据配方和开源数据集解决了这一问题，显著提升了在多种智能体任务中的性能，超越了 Nemotron-Terminal-32B 等现有开源模型。 微调后的 Qwen3-32B 模型比之前最强的开源数据模型 Nemotron-Terminal-32B 提高了 3.9 个百分点。该项目的训练集、数据管道和模型已公开发布，以支持对智能体模型训练的进一步开源研究。

arxiv · Negin Raoof, Richard Zhuang, Marianna Nezhurina · Jun 23, 17:34

**背景**: 智能体语言模型（Agentic LLMs）是通过与外部工具、环境或数据库交互来执行复杂、多步骤任务的人工智能系统。训练这些模型需要高质量且多样化的数据，以教授它们如何进行推理、规划和执行操作，而这些数据在历史上一直难以进行系统化的整理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.24855">[2606.24855] OpenThoughts - Agent : Data Recipes for Agentic Models</a></li>
<li><a href="https://github.com/open-thoughts/OpenThoughts-Agent">GitHub - open - thoughts / OpenThoughts - Agent : Data recipes and...</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#LLM Fine-tuning`, `#Data Curation`, `#Open Source`

---

<a id="item-5"></a>
### [Computer use in Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) ⭐️ 7.0/10

Google 宣布在 Gemini 3.5 Flash 中推出“计算机使用”功能，使其能够模拟人类操作计算机界面以执行复杂任务。

hackernews · swolpers · Jun 24, 17:21

**标签**: `#Gemini`, `#Computer Use`, `#AI Agents`, `#LLM`, `#Google`

---

<a id="item-6"></a>
### [GLM-5.2 is a step change for open agents](https://www.interconnects.ai/p/glm-52-is-the-step-change-for-open) ⭐️ 7.0/10

本文分析了 GLM-5.2 模型对开源 Agent 领域带来的重大变革，并结合社区反馈探讨了其性能、成本及实际使用中的 API 限制问题。

hackernews · vantareed · Jun 23, 03:23

**标签**: `#GLM-5.2`, `#LLM`, `#AI Agents`, `#Open Source AI`

---

<a id="item-7"></a>
### [Thoughts on Role Confusion](https://www.gilesthomas.com/2026/06/role-confusion) ⭐️ 7.0/10

文章探讨了 LLM 如何通过文本语气而非结构化标签来推断角色，从而导致提示词注入和越狱漏洞的研究。

rss · gilesthomas.com · Jun 24, 20:15

**标签**: `#LLM Security`, `#Prompt Injection`, `#AI Safety`, `#Transformer`

---

<a id="item-8"></a>
### [FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation](https://arxiv.org/abs/2606.24874v1) ⭐️ 7.0/10

FLUX3D 提出了一种基于扩散对齐稀疏表示的图像到 3D 高斯泼溅生成框架，解决了传统稀疏体素方法在保留高频视觉细节上的瓶颈。

arxiv · Haorui Ji, Weizhe Liu, Hongdong Li · Jun 23, 17:52

**标签**: `#3D Gaussian Splatting`, `#Diffusion Models`, `#3D Generation`, `#Computer Vision`

---

<a id="item-9"></a>
### [Real vs. Complex Spectral Bases for Neural Operators: The Role of Green's Function Alignment](https://arxiv.org/abs/2606.24851v1) ⭐️ 7.0/10

本文引入了哈特利神经算子（HNO），通过使用实数离散哈特利变换替代复数傅里叶变换，消除了傅里叶神经算子（FNO）在处理实值 PDE 时的表示冗余。

arxiv · Jason Sulskis, Sathya Ravi · Jun 23, 17:29

**标签**: `#Neural Operators`, `#Scientific ML`, `#Fourier Neural Operator`, `#Partial Differential Equations`

---

<a id="item-10"></a>
### [IV-CoT: Implicit Visual Chain-of-Thought for Structure-Aware Text-to-Image Generation](https://arxiv.org/abs/2606.24849v1) ⭐️ 7.0/10

论文提出了 IV-CoT 框架，通过将视觉条件分解为结构到语义的级联，并结合训练期草图监督，提升了文本生成图像模型在空间布局和属性绑定等结构感知任务上的表现。

arxiv · Zixuan Li, Haokun Lin, Yicheng Xiao · Jun 23, 17:28

**标签**: `#Text-to-Image`, `#Multimodal LLMs`, `#Chain-of-Thought`, `#Computer Vision`

---

<a id="item-11"></a>
### [Grading the Grader: Lessons from Evaluating an Agentic Data Analysis System](https://arxiv.org/abs/2606.24839v1) ⭐️ 7.0/10

本文探讨了如何可靠地评估 Agent 级数据分析系统，并提出了一种结合正则匹配、LLM 评分和人工检查的三层评估级联方法。

arxiv · Tian Zheng, Kai-Tai Hsu · Jun 23, 17:18

**标签**: `#LLM Agents`, `#Model Evaluation`, `#Data Analysis`, `#Machine Learning`

---

## 开发工具

<a id="item-12"></a>
### [PR spam today looks like email spam in the early 2000s](https://www.greptile.com/blog/prs-on-openclaw) ⭐️ 7.0/10

文章讨论了当前开源项目面临的 Pull Request (PR) 垃圾信息轰炸问题，并将其与 2000 年代初的电子邮件垃圾邮件进行了对比。

hackernews · dakshgupta · Jun 24, 14:32

**标签**: `#Open Source`, `#GitHub`, `#Software Engineering`, `#Spam`

---

<a id="item-13"></a>
### [Show HN: Nub – A Bun-like all-in-one toolkit for Node.js](https://github.com/nubjs/nub) ⭐️ 7.0/10

Nub 是一个为 Node.js 设计的类似 Bun 的全能工具包，通过预加载钩子和 oxc 转译器在原生 Node.js 上提供快速的 TypeScript 支持和现代 API 填充。

hackernews · colinmcd · Jun 24, 14:14

**标签**: `#Node.js`, `#TypeScript`, `#DevTools`, `#JavaScript`

---

<a id="item-14"></a>
### [simonw/browser-compat-db](https://simonwillison.net/2026/Jun/24/browser-compat-db/#atom-everything) ⭐️ 7.0/10

Simon Willison 利用 AI 辅助编程工具将 Mozilla 的 MDN 浏览器兼容性数据转换并构建为一个支持跨域（CORS）访问的 SQLite 数据库，并托管在 GitHub 上。

rss · simonwillison.net · Jun 24, 23:59

**标签**: `#sqlite`, `#mdn`, `#github-actions`, `#datasette`, `#ai-assisted-programming`

---

<a id="item-15"></a>
### [RubyLLM: A Ruby framework for all major AI providers](https://rubyllm.com/) ⭐️ 6.0/10

RubyLLM 是一个面向 Ruby 语言的开源 AI 开发框架，旨在简化与各大主流大语言模型（LLM）提供商的集成与交互。

hackernews · doener · Jun 24, 14:41

**标签**: `#Ruby`, `#LLM`, `#AI Framework`, `#Dev Tools`

---

## 系统与基础设施

<a id="item-16"></a>
### [45°C cooling design cuts data center water use to near zero](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 7.0/10

NVIDIA 推出了一种 45°C 液冷架构设计，旨在大幅降低 AI 数据中心的能耗并使水资源消耗接近于零。

hackernews · nitin_flanker · Jun 24, 14:10

**标签**: `#Liquid Cooling`, `#Data Center`, `#NVIDIA`, `#Green Computing`, `#Infrastructure`

---

## 行业动态

<a id="item-17"></a>
### [高通宣布以近 40 亿美元收购 AI 初创公司 Modular](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/) ⭐️ 8.0/10

高通（Qualcomm）宣布已达成协议，将收购由 LLVM 创始人 Chris Lattner 联合创立的 AI 软件与基础设施初创公司 Modular，交易估值近 40 亿美元。该交易将通过高通发行最多 1920 万股普通股的方式进行。 此次收购凸显了硬件制造商通过整合软件栈以在 AI 时代进行竞争的趋势，有助于高通将其能力从边缘设备扩展到云端 AI。同时，这也引发了外界对 Modular 旗下专为 AI 设计的 Python 兼容编程语言 Mojo 自动优化和未来发展的关注。 该交易旨在加强高通在不同计算环境下的生成式和代理式 AI 原生平台。然而，鉴于硬件公司在构建软件栈方面历史上面临的挑战，将 Modular 的软件栈整合到高通的硬件生态系统中可能会面临执行上的挑战。

hackernews · timmyd · Jun 24, 13:49

**背景**: Modular 的创立旨在解决 AI 软件基础设施的碎片化问题，其最著名的成果是开发了结合 Python 易用性与 C 语言性能的 Mojo 编程语言，以及 MAX 引擎。高通是一家传统的移动芯片巨头，目前正积极向 AI、RISC-V 和云端计算领域转型，以挑战英伟达（NVIDIA）的主导地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wired.com/story/qualcomm-buys-buzzy-chip-startup-modular-for-nearly-dollar4-billion/">Qualcomm Buys Buzzy Chip Startup Modular for Nearly $4 Billion | WIRED</a></li>
<li><a href="https://investor.qualcomm.com/news-events/press-releases/news-details/2026/Qualcomm-to-Acquire-Modular/default.aspx">Qualcomm - Qualcomm to Acquire Modular</a></li>
<li><a href="https://www.modular.com/blog/qualcomm-to-acquire-modular">Modular: Qualcomm to Acquire Modular</a></li>

</ul>
</details>

**社区讨论**: 社区对这一快速收购表示惊讶，并对 Mojo 类似 Python 的设计优劣展开了辩论。部分用户质疑高通在缺乏高端训练芯片的情况下如何利用 Modular，而另一些人则认为这是高通为构建 AI 和云计算完整产品组合而采取的战略举措。

**标签**: `#Qualcomm`, `#Modular`, `#Mojo`, `#Acquisition`, `#AI Infrastructure`

---

<a id="item-18"></a>
### [There are a few things that I look back on as my mistakes in the early days](https://twitter.com/ID_AA_Carmack/status/2069799283369345247) ⭐️ 7.0/10

John Carmack 反思了他在 id Software 早期管理中的失误，特别是过度压榨员工以及未能意识到成熟公司需要更多缓冲空间，引发了关于初创公司文化和员工倦怠的深入讨论。

hackernews · shadowtree · Jun 24, 15:56

**标签**: `#John Carmack`, `#id Software`, `#Management`, `#Startup Culture`, `#Game Development`

---

## 研究

<a id="item-19"></a>
### [New Bounds for the Last Iterate of the Stochastic subGradient Method](https://arxiv.org/abs/2606.24879v1) ⭐️ 7.0/10

本文研究了一维凸 Lipschitz 目标函数下随机次梯度法最后迭代步的误差界限，并解决了一个关于其在仅有界方差假设下是否次优的开放问题。

arxiv · Guglielmo Beretta, Tommaso Cesari, Roberto Colomboni · Jun 23, 17:55

**标签**: `#Optimization`, `#Machine Learning Theory`, `#Stochastic Subgradient Method`, `#Mathematical Optimization`

---

<a id="item-20"></a>
### [World Models in Pieces: Structural Certification for General Agents](https://arxiv.org/abs/2606.24842v1) ⭐️ 7.0/10

本文提出了“结构化认证”框架，通过将受限的目标导向性能映射到智能体内部世界模型的局部转移保证上，解决了通用智能体在复杂大世界中无法实现全能的问题。

arxiv · Yikai Lu, Yifei Wu, Xinyu Lu · Jun 23, 17:21

**标签**: `#World Models`, `#AI Agents`, `#Reinforcement Learning`, `#Theoretical ML`

---