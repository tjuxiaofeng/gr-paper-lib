# 生成式推荐论文库 index

> 📌 本目录按 **生成式推荐（GR）pipeline 阶段** 组织：从物品语义化 → 生成式骨干 → 检索/排序 → LLM4Rec → 长序列 → 工业落地 → 多模态 → 基础设施 → CTR 工程。
>
> 📅 最后更新：2026-09-24
>
> 🎯 选取标准：大厂工业界实践 + Top 高校研究 + GR 方向奠基/代表工作

---

## 📚 目录

- [1. Item Tokenization / Semantic ID](#1-item-tokenization-semantic-id)
- [2. 生成式骨干 与 Scaling](#2-生成式骨干-与-scaling)
- [3. 生成式检索 / 排序方法](#3-生成式检索-排序方法)
- [4. LLM4Rec 与对齐](#4-llm4rec-与对齐)
- [5. 长序列建模](#5-长序列建模)
- [6. 工业落地系统](#6-工业落地系统)
- [7. 多模态推荐](#7-多模态推荐)
- [8. 基础设施 / 基础模型](#8-基础设施-基础模型)
- [9. CTR 训练 / 工程](#9-ctr-训练-工程)
- [10. 阅读路径建议](#10-阅读路径建议)

---

## 1. Item Tokenization / Semantic ID

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `Recommender Systems with Generative Retrieval.pdf` | Google | 2023 | 同 §1，Semantic ID 的代表作，见上 |
| `Sparse Meets Dense: Unified Generative Recommendations with Cascaded Sparse-Dense Representations.pdf` | 百度 | 2025 | 稀疏语义 ID + 稠密表示级联的统一生成式推荐（会议待核） |
| `Adapting Large Language Models by Integrating Collaborative Semantics for Recommendation.pdf` | USTC | 2023 | **LC-Rec**：Language + Codes 联合建模，semantic ID 学习 + LLM 生成 |
| `Learning Vector-Quantized Item Representation for Transferable Sequential Recommenders.pdf` | 人大 | 2022 | **VQ-Rec**：向量量化学 item code，可迁移的 semantic ID 早期工作 |
| `IDGenRec: LLM-RecSys Alignment with Textual ID Learning.pdf` | Rutgers | 2024 | **IDGenRec**：让 LLM 自学习可生成的"文本 ID"（SIGIR 2024） |
| `Generative Recommender with End-to-End Learnable Item Tokenization.pdf` | 人大 | 2025 | **ETEGRec**：端到端学习物品 tokenization，直击 semantic ID 两阶段解耦（SIGIR 2025） |
| `Semantic Convergence: Harmonizing Recommender Systems via Two-Stage Alignment and Behavioral Semantic Tokenization.pdf` | 美团 | 2025 | 两阶段对齐 + 行为语义 token 化，缓解语义/协同空间错位（AAAI 2025） |

## 2. 生成式骨干 与 Scaling

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations.pdf` | Meta | 2024 | **HSTU 原论文**。把 ranking 建模为序列生成任务，1T 参数级 Transducer，GR 方向的开山之作 |
| `RankMixer: Scaling Up Ranking Models in Industrial Recommenders.pdf` | 字节 | 2024 | 排序侧的 Scaling 架构，token-mixing 思想 |
| `Bending the Scaling Law Curve in Large-Scale Recommendation Systems.pdf` | Meta | 2026 | HSTU 的效率优化变体 |
| `Climber: Toward Efficient Scaling Laws for Large Recommendation Models.pdf` | 网易 | 2025 | 大模型推荐的 Scaling Laws 探索 |
| `TokenMixer-Large: Scaling Up Large Ranking Models in Industrial Recommenders.pdf` | 字节 | 2026 | Token-mixing 架构在工业排序的规模化 |
| `CCFormer: Efficient Cross-Field Interaction and Hierarchical Sequence Compression for Industrial Recommendation at Tencent.pdf` | 腾讯 | 2024 | 腾讯的高效 cross-field + 序列压缩 |
| `INFNet: A Task-aware Information Flow Network for Large-Scale Recommendation Systems.pdf` | 快手 | 2025 | 任务感知的信息流网络 |
| `HHFT: Hierarchical Heterogeneous Feature Transformer for Recommendation Systems.pdf` | 阿里 | 2025 | 层次异构特征 Transformer |
| `One Model to Rank Them All: Unifying Online Advertising with End-to-End Learning.pdf` | 美团 | 2025 | 广告端到端统一排序 |
| `EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling.pdf` | 阿里 | 2026 | CTR 侧的 Scaling Laws 与统一建模 |
| `Exploring Scaling Laws of CTR Model for Online Performance Improvement.pdf` | 中科院 | 2025 | CTR Scaling Laws 与在线效果的关系 |
| `HyFormer: Revisiting the Roles of Sequence Modeling and Feature Interaction in CTR Prediction.pdf` | 字节 | 2026 | 序列建模 vs 特征交叉的重新审视 |
| `Scaling Transformers for Discriminative Recommendation via Generative Pretraining.pdf` | 阿里国际 | 2025 | 用生成式预训练解锁判别式推荐的 Transformer 可扩展性（KDD 2025） |
| `Wukong: Towards a Scaling Law for Large-Scale Recommendation.pdf` | Meta | 2024 | **Wukong**：推荐的 scaling law（参数量×DCN 扩展），与大模型推荐直接相关（疑似 ICML 2024，待核） |

## 3. 生成式检索 / 排序方法

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `Towards Large-scale Generative Ranking.pdf` | 小红书 | 2025 | 生成式 ranking 的系统化综述与实践 |
| `Action is All You Need: Dual-Flow Generative Ranking Network for Recommendation.pdf` | 美团 | 2025 | Dual-Flow GR 架构，行为流 + 目标流分离 |
| `PinRec: Outcome-Conditioned, Multi-Token Generative Retrieval for Industry-Scale Recommendation Systems.pdf` | Pinterest | 2024 | Outcome-conditioned + multi-token 检索，Pinterest 落地 |
| `A Generative Re-ranking Model for List-level Multi-objective Optimization at Taobao.pdf` | 阿里 | 2024 | 淘宝生成式重排，list-level 多目标 |
| `Leveraging Passage Embeddings for Efficient Listwise Reranking with Large Language Models.pdf` | 人大 | 2025 | 用段落嵌入做高效 listwise 重排（WWW 2025） |
| `A Neural Corpus Indexer for Document Retrieval.pdf` | Microsoft | 2022 | **NCI**：生成式检索（DSI 路线）里程碑，语义 ID/约束解码源头（NeurIPS 2022） |
| `Generative Retrieval as Multi-Vector Dense Retrieval.pdf` | 山东大学 | 2024 | 从理论上把生成式检索统一为多向量稠密检索（SIGIR 2024） |
| `Learning to Rank in Generative Retrieval.pdf` | 港理工 | 2024 | 在生成式检索内引入排序损失，打通"生成即排序"（AAAI 2024） |
| `GraphRAG-IRL: Personalized Recommendation with Graph-Grounded Inverse Reinforcement Learning and LLM Re-ranking.pdf` | Purdue | 2026 | Graph + IRL + LLM 重排 |

## 4. LLM4Rec 与对齐

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `Recommendation as Language Processing (RLP): A Unified Pretrain, Personalized Prompt & Predict Paradigm (P5).pdf` | Rutgers | 2022 | **P5**：把推荐/评分预测/序列/解释/摘要统一为 text-to-text，最早的 pretrain-transfer 探索 |
| `GPT4Rec: A Generative Framework for Personalized Recommendation and User Interests Interpretation.pdf` | Amazon | 2023 | **GPT4Rec**：生成 query → 搜索 item，最早的 LLM-as-recommender 探索之一 |
| `TALLRec: An Effective and Efficient Tuning Framework to Align Large Language Model with Recommendation.pdf` | USTC | 2023 | **TALLRec**：把推荐 finetune 成 LLM 指令任务，few-shot 效果好 |
| `LLaRA: Large Language-Recommendation Assistant.pdf` | USTC | 2023 | **LLaRA**：把序列推荐的 item embedding 融入 LLM prompt |
| `Text Is All You Need: Learning Language Representations for Sequential Recommendation.pdf` | UCSD / Amazon | 2023 | **Recformer**：把物品编码为文本、用语言模型做序列推荐（KDD 2023） |
| `Bridging Items and Language: A Transition Paradigm for Large Language Model-Based Recommendation.pdf` | 新加坡国立 | 2024 | 用"过渡 token"在物品与词表间桥接，缓解 LLM 生成推荐的 ID↔语义鸿沟（KDD 2024） |
| `Towards Universal Sequence Representation Learning for Recommender Systems.pdf` | 人大 | 2022 | **UniSRec**：文本辅助的可迁移序列表示学习（KDD 2022） |
| `Representation Learning with Large Language Models for Recommendation.pdf` | 香港大学 | 2024 | **RLMRec**：用 LLM 生成的特征对齐协同信号（WWW 2024） |
| `Customizing Language Models with Instance-wise LoRA for Sequential Recommendation.pdf` | USTC | 2024 | 实例级 LoRA，把 LLM 高效适配到序列推荐（NeurIPS 2024） |
| `RecGPT: Generative Pre-training for Text-based Recommendation.pdf` | VinAI | 2024 | 面向文本推荐的生成式预训练模型 RecGPT-7B（ACL 2024） |
| `SLMRec: Distilling Large Language Models into Small for Sequential Recommendation.pdf` | Rutgers | 2025 | 把大语言模型蒸馏成小模型做序列推荐（ICLR 2025） |
| `EAGER-LLM: Enhancing Large Language Models as Recommenders through Exogenous Behavior-Semantic Integration.pdf` | 浙大 | 2025 | 外部行为-语义整合增强 LLM 推荐（WWW 2025） |
| `LLM-ESR: Large Language Models Enhancement for Long-tailed Sequential Recommendation.pdf` | 西安交大 / 腾讯 | 2024 | 双视图 LLM 增强长尾序列推荐（疑似 NeurIPS 2024，待核） |
| `E4SRec: An Elegant Effective Efficient Extensible Solution of Large Language Models for Sequential Recommendation.pdf` | 清华 | 2023 | LLM 序列推荐的高效适配（冻结主干 + 可扩展输入/输出）（疑似 AAAI 2024，待核） |
| `RecRanker: Instruction Tuning Large Language Model as Ranker for Top-k Recommendation.pdf` | 香港城市大学 | 2024 | 指令微调 LLM 做 top-k 排序（疑似 AAAI 2025，待核） |

## 5. 长序列建模

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders.pdf` | 字节 | 2025 | 工业级长序列建模，配合 GR 的必备基础 |
| `Make It Long, Keep It Fast: End-to-End 10k-Sequence Modeling at Billion Scale on Douyin.pdf` | 抖音 | 2024 | 抖音 10k 序列端到端建模，Billion 级 |

## 6. 工业落地系统

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `OneRec: Unifying Retrieve and Rank with Generative Recommender and Preference Alignment.pdf` | 快手 | 2024 | **OneRec 首篇**。检索 + 排序统一到一个生成式模型，加 iterative preference alignment |
| `OneRec Technical Report.pdf` | 快手 | 2024 | OneRec 技术报告，工程细节 |
| `OneRec-V2 Technical Report.pdf` | 快手 | 2025 | OneRec V2 迭代，规模/效果升级 |
| `MTGR: Industrial-Scale Generative Recommendation Framework in Meituan.pdf` | 美团 | 2024 | 美团工业级 GR 框架，落地经验 |
| `HLLM: Enhancing Sequential Recommendations via Hierarchical Large Language Models for Item and User Modeling.pdf` | 字节 | 2024 | **HLLM**：Item LLM + User LLM 分层建模，字节代表作 |
| `Next-User Retrieval: Enhancing Cold-Start Recommendations via Generative Next-User Modeling.pdf` | 字节 | 2025 | 生成式冷启，为下一个用户建模 |
| `MTFM: A Scalable and Alignment-free Foundation Model for Industrial Recommendation in Meituan.pdf` | 美团 | 2026 | 美团工业级推荐基础模型，alignment-free 跨域/多场景 |
| `The Tencent Advertising Algorithm Challenge 2025: All-Modality Generative Recommendation.pdf` | 腾讯 | 2026 | 腾讯广告挑战赛 2025：全模态生成式推荐数据集与榜单 |

## 7. 多模态推荐

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `AlignRec: Aligning and Training in Multimodal Recommendations.pdf` | 上海交大 | 2024 | 多模态推荐的对齐与训练 |
| `Molar: Multimodal LLMs with Collaborative Filtering Alignment for Enhanced Sequential Recommendation.pdf` | USTC | 2024 | 多模态 LLM + 协同过滤对齐做序列推荐（疑似 WWW 2025，待核） |

## 8. 基础设施 / 基础模型

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention.pdf` | DeepSeek | 2025 | **NSA**：硬件对齐的稀疏 attention，超长序列训练关键 |
| `Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free.pdf` | 阿里 | 2025 | Gated attention 变体 |
| `TokenFormer: Rethinking Transformer Scaling with Tokenized Model Parameters.pdf` | 马普所 | 2024 | 把模型参数也 tokenize，新的 scaling 范式 |
| `MambaVision: A Hybrid Mamba-Transformer Vision Backbone.pdf` | NVIDIA | 2024 | Mamba-Transformer 混合，对长序列 SSM 有参考价值 |
| `GPT-4 Technical Report.pdf` | OpenAI | 2023 | GPT-4 技报 |
| `DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models.pdf` | DeepSeek | 2024 | DeepSeek V3.2 技报 |
| `DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models.pdf` | DeepSeek | 2024 | **DeepSeekMoE**：细粒度 expert + shared expert，MMoE/PLE 可参考 |
| `Qwen2.5-1M Technical Report.pdf` | 阿里 | 2024 | Qwen2.5 1M context 技报 |

## 9. CTR 训练 / 工程

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `PPM: A Pre-trained Plug-in Model for Click-through Rate Prediction.pdf` | 京东 | 2024 | 预训练即插即用 CTR 模型 |
| `Multi-Epoch Learning for Deep Click-Through Rate Prediction Models.pdf` | 快手 | 2023 | CTR 多轮训练 |
| `Multi-Epoch learning with Data Augmentation for Deep Click-Through Rate Prediction.pdf` | 快手 | 2024 | CTR 多轮 + 数据增强 |

---

## 10. 阅读路径建议

### 🚀 想入门 GR 主线（2 小时）
1. `Actions Speak Louder...` (HSTU)：先建立"把推荐当序列生成"的心智模型
2. `Recommender Systems with Generative Retrieval.pdf`：理解 Semantic ID 与 autoregressive 检索
3. `Towards Large-scale Generative Ranking.pdf`：系统化梳理

### 🏭 想看工业落地（3 小时）
1. `OneRec-V2 Technical Report.pdf`：最新的完整工业方案
2. `MTGR: Industrial-Scale...`：美团版本
3. `HLLM: Enhancing Sequential...`：字节的分层 LLM 方案
4. `RankMixer: Scaling Up...` + `LONGER: Scaling Up...`：Scaling 与长序列基础设施

### 🧠 想深入 LLM4Rec 与 Semantic ID（2 小时）
1. `TALLRec: An Effective and Efficient Tuning Framework to Align Large Language Model with Recommendation.pdf` → `LLaRA: Large Language-Recommendation Assistant.pdf`：LLM 直接做推荐
2. `Learning Vector-Quantized Item Representation for Transferable Sequential Recommenders.pdf` → `Recommender Systems with Generative Retrieval.pdf` → `Adapting Large Language Models by Integrating Collaborative Semantics for Recommendation.pdf`：Semantic ID 的演化

### 🧰 想解决实际工程问题
| 问题 | 参考论文 |
|---|---|
| 长序列训练慢 | `Make It Long, Keep It Fast...`, `LONGER`, `Native Sparse Attention` |
| Scaling Laws 曲线怎么画 | `Climber`, `EST`, `Exploring Scaling Laws...` |
| Expert 参数怎么切 | `DeepSeekMoE`, `RankMixer`, `TokenMixer` |
| 冷启动怎么办 | `Next-User Retrieval` |
| 重排 / list-level | `A Generative Re-ranking Model... at Taobao` |

---

## 附：新增论文来源

本次（2026-09-06）新增 7 篇（编号 02/03/07/08/09/10/11），补齐 GR 早期奠基与 Semantic ID / LLM4Rec 两条支线；其余 44 篇是历史积累。

| 编号 | 论文 | arxiv |
|---|---|---|
| 02 | TIGER (Google, 2023) | https://arxiv.org/abs/2305.05065 |
| 03 | P5 (Rutgers, 2022) | https://arxiv.org/abs/2203.13366 |
| 07 | GPT4Rec (Amazon, 2023) | https://arxiv.org/abs/2304.03879 |
| 08 | TALLRec (USTC, 2023) | https://arxiv.org/abs/2305.00447 |
| 09 | LLaRA (USTC, 2023) | https://arxiv.org/abs/2312.02445 |
| 10 | LC-Rec (USTC, 2023) | https://arxiv.org/abs/2311.09049 |
| 11 | VQ-Rec (RUC, 2022) | https://arxiv.org/abs/2210.12316 |
