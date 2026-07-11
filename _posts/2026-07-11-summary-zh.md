---
layout: default
title: "Daybreak Summary: 2026-07-11 (ZH)"
date: 2026-07-11
lang: zh
---

> 从 45 条内容中，筛选出 20 条重要资讯

---

**AI / 机器学习**
1. [GPT-5.6 Sol Ultra 产出循环双覆盖猜想的数学证明](#item-1) ⭐️ 10.0/10
2. [OpenAI 发布全新 GPT-5.6 模型系列：Luna、Terra 和 Sol](#item-2) ⭐️ 9.0/10
3. [OpenCoF：通过帧链推理提升视频生成模型的逻辑能力](#item-3) ⭐️ 8.0/10
4. [扩散模型中的 Score 准确度无法保证采样数值稳定性](#item-4) ⭐️ 8.0/10
5. [降维与网络科学的结合：利用 UMAP 内部 kNN 图进行数据分析](#item-5) ⭐️ 8.0/10
6. [Introducing Muse Spark 1.1](#item-6) ⭐️ 7.0/10
7. [UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks](#item-7) ⭐️ 7.0/10
8. [Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation](#item-8) ⭐️ 7.0/10
9. [MulTTiPop: A Multitrack Transcription Dataset for Pop Music](#item-9) ⭐️ 7.0/10
10. [SLORR: Simple and Efficient In-Training Low-Rank Regularization](#item-10) ⭐️ 7.0/10
11. [AI 2040: Plan A](#item-11) ⭐️ 6.0/10

**开发工具**
12. [Good Tools Are Invisible](#item-12) ⭐️ 7.0/10

**系统与基础设施**
13. [QuadRF：开源相控阵无线电实现射频信号可视化与无人机追踪](#item-13) ⭐️ 8.0/10
14. [Unboxed: Zig](#item-14) ⭐️ 7.0/10
15. [The case of the mysterious changes to integers when there shouldn’t have been any code generation effect](#item-15) ⭐️ 6.0/10

**行业动态**
16. [Apple 起诉 OpenAI 及前员工，指控其窃取硬件商业机密](#item-16) ⭐️ 9.0/10
17. [Meta 默认允许 AI 重用 Instagram 公开账户内容](#item-17) ⭐️ 8.0/10
18. [New York City to to ban deceptive subscription practices](#item-18) ⭐️ 7.0/10
19. [Shocking No One, Fidji Simo, Would-Be Usurper, Is Out at OpenAI](#item-19) ⭐️ 7.0/10

**其他**
20. [The tech of 'Terminator 2' – an oral history (2017)](#item-20) ⭐️ 6.0/10
---

## AI / 机器学习

<a id="item-1"></a>
### [GPT-5.6 Sol Ultra 产出循环双覆盖猜想的数学证明](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf) ⭐️ 10.0/10

OpenAI 的 GPT-5.6 Sol Ultra 模型利用 64 个协作子智能体，在不到一小时的时间内生成了图论中长期存在的“循环双覆盖猜想”的形式化证明。 这标志着 AI 推理能力的重大突破，展示了大型语言模型解决复杂且具有数十年历史的理论数学猜想的能力，而不仅仅是寻找反例或解决常规问题。 该证明是通过极具针对性的 Prompt 实现的，该 Prompt 指令模型拒绝模糊的乐观态度；然而，该结果目前尚缺乏独立的同行评审或形式化证明助手的验证。

hackernews · scrlk · Jul 10, 18:29

**背景**: 循环双覆盖猜想于 20 世纪 70 年代提出，假设每个有限的无桥无向图都存在一组循环，使得每条边恰好被覆盖两次。在图论中，“桥”是指删除后会增加图中连通分量数量的边。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kingy.ai/blog/openai-gpt-5-6-sol-ultra-cycle-double-cover-proof-claim/">OpenAI's 64-Subagent Cycle Double Cover Proof Claim</a></li>
<li><a href="https://cryptobriefing.com/openai-gpt-5-6-sol-ultra-math-proof/">OpenAI's GPT-5.6 Sol Ultra proves 50-year-old math conjecture in under an hour</a></li>

</ul>
</details>

**社区讨论**: 用户注意到该模型高度依赖 Prompt 工程来保持思路正确，并讨论了该证明是利用了专家忽视的“巧妙技巧”，还是代表了一种新型的自动化理论构建。

**标签**: `#GPT-5.6`, `#Mathematics`, `#Graph Theory`, `#AI Reasoning`, `#OpenAI`

---

<a id="item-2"></a>
### [OpenAI 发布全新 GPT-5.6 模型系列：Luna、Terra 和 Sol](https://simonwillison.net/2026/Jul/9/gpt-5-6/#atom-everything) ⭐️ 9.0/10

OpenAI 发布了全新的旗舰级 GPT-5.6 模型系列，包含 Luna、Terra 和 Sol 三种尺寸，主打长程 Agent 工作流。这些模型拥有 100 万 token 的上下文窗口和 128,000 的最大输出 token 限制，并引入了编程式工具调用（Programmatic Tool Calling）等全新 API 功能。 该发布显著降低了复杂推理任务的成本，其中 GPT-5.6 Sol 在 Agents' Last Exam 基准测试中超越了 Anthropic 的 Claude Fable 5。这标志着大语言模型（LLM）的竞争焦点正转向 Agent 效率和原生多 Agent 编排。 模型每百万输入/输出 token 的定价分别为 Luna $1/$6、Terra $2.50/$15 和 Sol $5/$30。尽管它们在 Agent 基准测试中表现优异，但 GPT-5.6 Sol 在 SWE-Bench Pro 上的得分为 64.6%，低于 Claude Fable 5 的 80%，而 OpenAI 声称该基准测试中约有 30% 的任务存在缺陷。

rss · simonwillison.net · Jul 9, 19:46

**背景**: AI Agent 是由大语言模型（LLM）驱动的系统，能够自主规划、使用工具并执行多步骤任务以实现特定目标。随着大模型的发展，对其评估已从简单的问答转向复杂的长程工作流，并通过 SWE-Bench Pro（针对软件工程）和 Agents' Last Exam 等基准测试进行检验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/9/gpt-5-6/">The new GPT-5.6 family: Luna, Terra, Sol</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT-5.6: Frontier intelligence that scales with your ambition | OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#LLM`, `#AI Agents`

---

<a id="item-3"></a>
### [OpenCoF：通过帧链推理提升视频生成模型的逻辑能力](https://arxiv.org/abs/2607.08763v1) ⭐️ 8.0/10

研究人员推出了 OpenCoF 框架，包含 OpenCoF-17K 数据集和 Wan-CoF 模型，旨在实现视频生成中的“帧链”（Chain-of-Frame, CoF）推理。该框架使模型能够通过 11 个不同任务族中视频帧的时间演变来进行逻辑推理。 该研究推动视频生成从追求视觉美感转向逻辑一致性，帮助 AI 更好地理解物理定律和因果序列。它建立了一种模拟人类时序理解的多模态推理新范式。 该框架利用专门的视觉和文本推理标记（Tokens）在模型深度和去噪步骤中组织中间状态。基于 Wan2.2-I2V-A14B 架构构建的 Wan-CoF 在四个视频推理基准测试中表现出显著提升。

arxiv · Xinyan Chen, Ziyu Guo, Renrui Zhang · Jul 9, 17:58

**背景**: 传统的思维链（CoT）推理主要基于文本，帮助模型逐步解决问题。OpenCoF 将这一概念扩展到视觉领域，其中的“步骤”由必须遵循逻辑或物理规则的连续视频帧表示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.08763">OpenCoF : Learning to Reason Through Video Generation</a></li>
<li><a href="https://opencof.github.io/">OpenCoF : Learning to Reason Through Video Generation</a></li>

</ul>
</details>

**标签**: `#Video Generation`, `#Reasoning`, `#Multimodal AI`, `#Chain-of-Thought`

---

<a id="item-4"></a>
### [扩散模型中的 Score 准确度无法保证采样数值稳定性](https://arxiv.org/abs/2607.08757v1) ⭐️ 8.0/10

研究人员证明，在前向扩散过程中获得的高 Score 准确度不足以保证离散化逆向时间采样过程中的数值稳定性。他们证实，即使在前向边缘误差极小的情况下，Euler-Maruyama 离散化仍可能导致正矩发散，并提出了一种利用去噪器投影的缓解策略。 这一发现挑战了生成式人工智能中“低训练误差会自动确保稳定采样”的常见假设，为设计鲁棒的扩散模型提供了关键的理论指导。它解释了为什么扩散模型有时会产生异常或发散的输出，并提供了一种实用的投影方法来防止这些失效。 研究表明，即使使用有界的全局 Lipschitz 去噪器，离散化路径的终点仍可能在所有 Wasserstein 距离 $W_p$ 下发散。然而，将学习到的去噪器投影到包含数据支撑集的已知有界闭凸集上，不仅能保持逐点准确性，还能确保 Wasserstein 收敛。

arxiv · Yiwei Zhou · Jul 9, 17:55

**背景**: 扩散模型通过逆转前向加噪过程来生成数据，这依赖于估计表示数据对数密度梯度的“Score 函数”。在生成过程中，通常使用 Euler-Maruyama 等数值离散化方法来求解逆向时间随机微分方程。传统上，人们假设在训练期间最小化 Score 匹配误差自然会带来准确且稳定的样本生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.08757">[2607.08757] Score Accuracy Along the Forward Diffusion Does ...</a></li>
<li><a href="https://arxiv.org/html/2607.08757">Score Accuracy Along the Forward Diffusion Does Not Certify ...</a></li>

</ul>
</details>

**标签**: `#Diffusion Models`, `#Numerical Stability`, `#Score Matching`, `#Generative AI`, `#Stochastic Differential Equations`

---

<a id="item-5"></a>
### [降维与网络科学的结合：利用 UMAP 内部 kNN 图进行数据分析](https://arxiv.org/abs/2607.08746v1) ⭐️ 8.0/10

研究人员提出了一种通过将 PageRank 和 k-core 分解等网络科学算法直接应用于 UMAP 内部的 k-最近邻 (kNN) 图来分析高维数据的方法。这种方法允许在不依赖可能失真的 2D 或 3D 视觉投影的情况下进行数据理解。 该技术提供了一种更准确地探索复杂数据集的方法，为传统的视觉化和聚类方法提供了强有力的补充。它使数据科学家能够在更有效地保留原始高维结构的同时，识别代表性样本和密集簇。 该研究利用 PageRank 识别中心数据点，利用 k-core 分解将密集核心区域与边缘分离，并利用聚类系数检测紧密邻域。在 MNIST 和 Fashion MNIST 上的实验表明，这些基于图的分析方法与 k-medoids 和 HDBSCAN 等专业方法相比具有竞争力。

arxiv · Duen Horng Chau, Donghao Ren, Fred Hohman · Jul 9, 17:47

**背景**: UMAP（均匀流形近似与投影）是一种流行的降维工具，它在将数据投影到可视化空间之前，首先构建一个 k-最近邻 (kNN) 图来建模数据关系。虽然最终的 2D 图表被广泛使用，但它经常会引入失真，从而误导对底层数据流形的理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.08746">[2607.08746] Dimensionality Reduction Meets Network Science ...</a></li>
<li><a href="https://umap-learn.readthedocs.io/">UMAP : Uniform Manifold Approximation and Projection for Dimension...</a></li>

</ul>
</details>

**标签**: `#UMAP`, `#Dimensionality Reduction`, `#Network Science`, `#Data Visualization`, `#Machine Learning`

---

<a id="item-6"></a>
### [Introducing Muse Spark 1.1](https://simonwillison.net/2026/Jul/9/muse-spark-1-1/#atom-everything) ⭐️ 7.0/10

Meta 发布了 Muse Spark 1.1 模型，首次提供 API 支持并提升了 Agent 与电脑操作能力，同时 Simon Willison 释出了相应的 LLM CLI 插件。

rss · simonwillison.net · Jul 9, 16:24

**标签**: `#Meta`, `#LLM`, `#AI Agent`, `#Generative AI`

---

<a id="item-7"></a>
### [UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks](https://arxiv.org/abs/2607.08768v1) ⭐️ 7.0/10

UniClawBench 是一个包含 400 个双语任务的基准测试，旨在通过技能使用、探索、长上下文推理等五大核心能力评估主动型 Agent 在真实环境中的表现。

arxiv · Zhekai Chen, Chengqi Duan, Kaiyue Sun · Jul 9, 17:59

**标签**: `#AI Agents`, `#Benchmark`, `#LLM`, `#Multimodal`, `#Evaluation`

---

<a id="item-8"></a>
### [Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation](https://arxiv.org/abs/2607.08758v1) ⭐️ 7.0/10

本文介绍了 IG-Bench，这是一个旨在评估 AI 系统在科学思想传承、演变推理及基于学术谱系生成新想法能力的基准测试。

arxiv · Yifan Zhou, Qihao Yang, Yan Li · Jul 9, 17:55

**标签**: `#AI4Science`, `#LLM Benchmark`, `#Scientific Reasoning`, `#Knowledge Graphs`

---

<a id="item-9"></a>
### [MulTTiPop: A Multitrack Transcription Dataset for Pop Music](https://arxiv.org/abs/2607.08756v1) ⭐️ 7.0/10

MulTTiPop 是一个包含 3.5 小时流行音乐片段及其对应多轨 MIDI 的数据集，旨在评估和推动自动音乐转录技术的发展。

arxiv · Nathan Pruyne, Benjamin Stoler, William Chen · Jul 9, 17:55

**标签**: `#Automatic Music Transcription`, `#Dataset`, `#Machine Learning`, `#Music Information Retrieval`

---

<a id="item-10"></a>
### [SLORR: Simple and Efficient In-Training Low-Rank Regularization](https://arxiv.org/abs/2607.08754v1) ⭐️ 7.0/10

SLORR 是一种简单、无状态且保持架构不变的训练中低秩正则化框架，通过 GPU 友好的近似计算显著提升了神经网络的可压缩性。

arxiv · David González-Martínez, Shiwei Liu · Jul 9, 17:51

**标签**: `#Model Compression`, `#Low-Rank Factorization`, `#Deep Learning`, `#Regularization`

---

<a id="item-11"></a>
### [AI 2040: Plan A](https://ai-2040.com/) ⭐️ 6.0/10

AI 2040: Plan A 是一份关于未来二十年人工智能演进及其对社会、经济和治理影响的投机性路线图。

hackernews · kschaul · Jul 9, 16:21

**标签**: `#AI Forecasting`, `#Future of Work`, `#AI Governance`, `#Speculative Technology`

---

## 开发工具

<a id="item-12"></a>
### [Good Tools Are Invisible](https://www.gingerbill.org/article/2026/07/10/good-tools-are-invisible/) ⭐️ 7.0/10

文章阐述了“工具隐形”的设计理念，认为优秀的工具应通过减少认知负担，使用户能够无缝地专注于其核心工作任务。

hackernews · theanonymousone · Jul 10, 10:32

**标签**: `#UI/UX Design`, `#Developer Experience`, `#Productivity`, `#Design Philosophy`

---

## 系统与基础设施

<a id="item-13"></a>
### [QuadRF：开源相控阵无线电实现射频信号可视化与无人机追踪](https://www.jeffgeerling.com/blog/2026/quadrf-can-spot-drones-and-see-wifi-through-my-wall/) ⭐️ 8.0/10

QuadRF 是一款基于树莓派 5 和 FPGA 板卡构建的新型开源相控阵无线电系统，能够实时可视化射频信号。它允许用户穿墙定位无线发射源的物理位置，并追踪飞行中的无人机。 通过将先进的波束成形和射频可视化技术引入易于获取的开源平台，QuadRF 让以往仅限于军工和政府机构的能力走向大众。这将对爱好者和专业人士的隐私保护、安全审计以及无人机探测产生深远影响。 该设备在 4.9 至 6.0 GHz 的 C 波段频率范围内工作，并利用皮秒级定时进行先进的信号处理。它允许用户将射频数据流式传输并解码到外部计算机，以进行更深层次的流量分析。

hackernews · jeffgeerling.com · Jul 10, 15:59

**背景**: 软件定义无线电（SDR）用软件取代了传统的硬件无线电组件，使单一设备能够接收广泛的频率。相控阵系统利用多个天线在无需物理移动的情况下电子化地引导无线电波束，这对于定位信号源和追踪运动物体至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jeffgeerling.com/blog/2026/quadrf-can-spot-drones-and-see-wifi-through-my-wall/">QuadRF can spot drones and see WiFi through my wall</a></li>
<li><a href="https://www.crowdsupply.com/scale-rf/quadrf">QuadRF | Crowd Supply</a></li>
<li><a href="https://hackaday.com/2026/06/20/seeing-the-world-in-radio-waves-with-the-quadrf/">Seeing The World In Radio Waves With The QuadRF | Hackaday</a></li>

</ul>
</details>

**社区讨论**: 该项目的创作者分享了演示视频，并表示正在根据反馈改进用户界面。其他评论者对“穿墙看 WiFi”的表述展开了讨论，并探讨了检测隐藏发射源以及为声音构建类似定向系统等潜在应用。

**标签**: `#SDR`, `#Wireless`, `#Open Source`, `#Hardware`, `#Privacy`

---

<a id="item-14"></a>
### [Unboxed: Zig](https://nesbitt.io/2026/07/09/unboxed-zig.html) ⭐️ 7.0/10

本文详细分析了 Zig 语言包管理器的运作机制、分类方式、治理模型及其面临的安全威胁模型。

rss · nesbitt.io · Jul 9, 10:00

**标签**: `#Zig`, `#Package Management`, `#Systems Programming`, `#Supply Chain Security`

---

<a id="item-15"></a>
### [The case of the mysterious changes to integers when there shouldn’t have been any code generation effect](https://devblogs.microsoft.com/oldnewthing/20260710-00/?p=112514) ⭐️ 6.0/10

本文探讨了一个在不应该产生代码生成影响的情况下，整数发生神秘变化的底层调试案例。

rss · devblogs.microsoft.com/oldnewthing · Jul 10, 14:00

**标签**: `#Debugging`, `#C++`, `#Compiler`, `#Windows`

---

## 行业动态

<a id="item-16"></a>
### [Apple 起诉 OpenAI 及前员工，指控其窃取硬件商业机密](https://9to5mac.com/2026/07/10/apple-sues-openai-trade-secret-theft/) ⭐️ 9.0/10

Apple 正式对 OpenAI、io Products 以及前高管 Tang Tan 和 Chang Liu 提起重大诉讼，指控其系统性地窃取硬件设计商业机密。诉状称，OpenAI 的领导层指示新员工盗取机密信息并规避安全协议，以此加速其消费级硬件业务的发展。 这标志着 Apple 与 OpenAI 之间竞争的重大升级，可能会危及双方在 Apple Intelligence 方面的现有合作。此举还针对了由传奇设计师 Jony Ive 领导的 OpenAI 硬件扩张计划，在潜在的 IPO 之前制造了法律障碍。 具体指控包括 Tang Tan 指导招聘人员隐瞒跳槽至 OpenAI 的行为，以及 Chang Liu 盗取 Apple 笔记本电脑。Apple 还声称 OpenAI 利用专有的金属精加工技术误导供应商，使其误以为获得了 Apple 的授权。

rss · daringfireball.net · Jul 10, 21:01

**背景**: Tang Tan 曾担任 Apple 负责 iPhone 和 Apple Watch 产品设计的副总裁，而 Jony Ive 曾长期担任 Apple 的首席设计官。OpenAI 通过以 65 亿美元收购 Ive 的初创公司 io Products 进入硬件领域，该公司将数十名 Apple 前工程师整合到了其团队中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/07/10/apple-openai-lawsuit-trade-secrets.html">Apple sues OpenAI alleging trade secret theft, says scheme was 'at every level'</a></li>
<li><a href="https://techcrunch.com/2026/07/10/apple-sues-openai-over-alleged-trade-secret-theft/">Apple sues OpenAI over alleged trade secret theft | TechCrunch</a></li>
<li><a href="https://9to5mac.com/2026/07/10/apple-sues-openai-trade-secret-theft/">Apple sues OpenAI , accuses ex- employees of stealing trade secrets</a></li>

</ul>
</details>

**社区讨论**: 评论者强调了证据的严重性，例如包含机密数据的电子邮件，并认为这可能会对 OpenAI 的声誉和 IPO 计划造成重大打击。一些人对在 Apple 工作多年的资深员工会因涉嫌此类违规行为而赌上职业生涯感到惊讶。

**标签**: `#Apple`, `#OpenAI`, `#Lawsuit`, `#Trade Secrets`, `#Hardware`

---

<a id="item-17"></a>
### [Meta 默认允许 AI 重用 Instagram 公开账户内容](https://www.nytimes.com/2026/07/08/technology/meta-instagram-ai.html?unlocked_article_code=1.wVA.Q5Do.Uvg5yPwCEB5H) ⭐️ 8.0/10

Meta 推出了 Muse Image AI 生成器，允许用户基于 Instagram 公开照片创建图像。默认情况下，所有拥有公开账户的成年用户都已自动加入此内容共享功能。 该政策凸显了科技公司利用用户数据发展生成式 AI 的激进态势，引发了关于隐私和知情同意的辩论。它迫使用户必须主动管理设置，以防止个人照片被用作 AI 训练材料或创作素材。 用户可以通过 Meta AI 独立聊天机器人访问此功能，以提取已发布的照片。尽管 Meta 提供了退出途径，但“默认加入”的做法被批评为违反了用户预期。

rss · daringfireball.net · Jul 9, 14:10

**背景**: 生成式 AI 依赖海量数据集来学习模式和风格。Meta 庞大的用户生成内容生态系统提供了独特的竞争优势，但使用这些数据往往与传统的隐私规范和版权理解相冲突。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/07/08/technology/meta-instagram-ai.html">How to Prevent Meta From Using Your Instagram Images in A . I .</a></li>
<li><a href="https://daringfireball.net/linked/2026/07/09/meta-instagram-ai-defaults">Meta Sets Default for Instagram Accounts to Permit Content ...</a></li>

</ul>
</details>

**社区讨论**: 社区对此反应冷淡且持怀疑态度，一些评论家将 Meta 对待用户的方式比作对待“附庸”。对于在未经明确、逐次许可的情况下使用个人照片生成新 AI 内容的伦理影响，人们表示了极大担忧。

**标签**: `#AI Ethics`, `#Meta`, `#Instagram`, `#Privacy`, `#Generative AI`

---

<a id="item-18"></a>
### [New York City to to ban deceptive subscription practices](https://www.theguardian.com/us-news/2026/jul/10/new-york-city-deceptive-subscriptions-ban) ⭐️ 7.0/10

纽约市宣布了一项旨在禁止欺骗性订阅和隐藏费用的新法规，要求商家提供简便的“一键取消”服务。

hackernews · randycupertino · Jul 10, 18:26

**标签**: `#Subscription`, `#Regulation`, `#Consumer Protection`, `#SaaS`

---

<a id="item-19"></a>
### [Shocking No One, Fidji Simo, Would-Be Usurper, Is Out at OpenAI](https://www.wsj.com/tech/openai-top-executive-fidji-simo-to-step-down-c3daca47?st=NfBZTe) ⭐️ 7.0/10

OpenAI 二号人物 Fidji Simo 因健康原因辞去全职职务并转任顾问，此前她曾被视为 Sam Altman 的潜在竞争者，同时 OpenAI 宣布将战略重心转向 AI 编程工具。

rss · daringfireball.net · Jul 10, 00:35

**标签**: `#OpenAI`, `#Fidji Simo`, `#Sam Altman`, `#AI Strategy`, `#Corporate Governance`

---

## 其他

<a id="item-20"></a>
### [The tech of 'Terminator 2' – an oral history (2017)](https://vfxblog.com/2017/08/23/the-tech-of-terminator-2-an-oral-history/) ⭐️ 6.0/10

本文回顾了电影《终结者 2》中液态金属等经典视觉特效背后的技术创新与计算机图形学发展历程。

hackernews · markus_zhang · Jul 10, 16:48

**标签**: `#Computer Graphics`, `#VFX`, `#History of Technology`, `#CGI`

---