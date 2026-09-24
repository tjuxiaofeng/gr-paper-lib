# 生成式推荐论文库 index

> 📌 本目录按 **生成式推荐（GR）pipeline 阶段** 组织：从物品语义化 → 生成式骨干 → 检索/排序 → LLM4Rec → 长序列 → 工业落地 → 多模态 → 基础设施 → CTR 工程。
>
> 📅 最后更新：2026-09-24
>
> 🎯 选取标准：大厂工业界实践 + Top 高校研究 + GR 方向奠基/代表工作

---

## 📚 目录

- [1. 物品语义化](#1-物品语义化)
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

## 1. 物品语义化

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `Recommender Systems with Generative Retrieval.pdf` | Google | 2023 | 推荐 | 工业 | generative retrieval, Semantic ID, sequence-to-sequence, codewords, cold-start |
| `Sparse Meets Dense: Unified Generative Recommendations with Cascaded Sparse-Dense Representations.pdf` | 百度 | 2025 | 推荐 | 工业 | generative retrieval, cascaded sparse-dense representations, Semantic ID, dense retrieval, BeamFusion |
| `Adapting Large Language Models by Integrating Collaborative Semantics for Recommendation.pdf` | USTC | 2023 | 推荐 | 学术 | LLM-based recommendation, collaborative semantics, item indexing, vector quantization, alignment tuning |
| `Learning Vector-Quantized Item Representation for Transferable Sequential Recommenders.pdf` | 人大 | 2022 | 推荐 | 学术 | transferable sequential recommender, vector-quantized item representation, item code, contrastive pre-training, cross-domain fine-tuning |
| `IDGenRec: LLM-RecSys Alignment with Textual ID Learning.pdf` | Rutgers | 2024 | 推荐 | 学术 | generative recommendation, textual ID learning, LLM alignment, foundation model, zero-shot |
| `Generative Recommender with End-to-End Learnable Item Tokenization.pdf` | 人大 | 2025 | 推荐 | 学术 | generative recommendation, item tokenization, end-to-end learning, sequence-item alignment, preference-semantic alignment |
| `Semantic Convergence: Harmonizing Recommender Systems via Two-Stage Alignment and Behavioral Semantic Tokenization.pdf` | 美团 | 2025 | 推荐 | 工业 | two-stage alignment, behavioral semantic tokenization, Alignment Tokenization, LLM, collaborative semantics |

## 2. 生成式骨干 与 Scaling

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations.pdf` | Meta | 2024 | 推荐 | 工业 | generative recommenders, sequential transduction, HSTU, scaling law, high-cardinality features |
| `RankMixer: Scaling Up Ranking Models in Industrial Recommenders.pdf` | 字节 | 2024 | 推荐 | 工业 | feature interaction, token mixing, Sparse-MoE, MFU, scaling |
| `Bending the Scaling Law Curve in Large-Scale Recommendation Systems.pdf` | Meta | 2026 | 推荐 | 工业 | scaling law, long-sequence modeling, sparse attention, sequential recommendation, co-design |
| `Climber: Toward Efficient Scaling Laws for Large Recommendation Models.pdf` | 网易 | 2025 | 推荐 | 工业 | scaling law, multi-scale sequence extraction, dynamic temperature modulation, KV caching, inference acceleration |
| `TokenMixer-Large: Scaling Up Large Ranking Models in Industrial Recommenders.pdf` | 字节 | 2026 | 推荐 | 工业 | token mixing, Sparse Per-token MoE, extreme-scale recommendation, inter-layer residuals, scaling |
| `CCFormer: Efficient Cross-Field Interaction and Hierarchical Sequence Compression for Industrial Recommendation at Tencent.pdf` | 腾讯 | 2024 | 推荐 | 工业 | cross-field feature interaction, hierarchical sequence compression, long-sequence modeling, industrial recommendation, scaling law |
| `INFNet: A Task-aware Information Flow Network for Large-Scale Recommendation Systems.pdf` | 快手 | 2025 | 推荐 | 工业 | feature interaction, task-aware modeling, multi-task learning, categorical tokens, cross attention with proxy |
| `HHFT: Hierarchical Heterogeneous Feature Transformer for Recommendation Systems.pdf` | 阿里 | 2025 | 推荐 | 工业 | CTR prediction, heterogeneous feature Transformer, semantic feature partitioning, high-order feature interaction, Hiformer |
| `One Model to Rank Them All: Unifying Online Advertising with End-to-End Learning.pdf` | 美团 | 2025 | 推荐 | 工业 | end-to-end generative ranking, multistage cascading architecture, advertising externalities, cluster attention, RecFormer |
| `EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling.pdf` | 阿里 | 2026 | 推荐 | 工业 | CTR prediction, scaling law, unified modeling, lightweight cross-attention, content sparse attention |
| `Exploring Scaling Laws of CTR Model for Online Performance Improvement.pdf` | 中科院 | 2025 | 推荐 | 学术 | CTR prediction, scaling law, unified attention block, online distillation, sparse self-attention |
| `HyFormer: Revisiting the Roles of Sequence Modeling and Feature Interaction in CTR Prediction.pdf` | 字节 | 2026 | 推荐 | 工业 | CTR prediction, sequence modeling, feature interaction, query decoding, token mixing |
| `Scaling Transformers for Discriminative Recommendation via Generative Pretraining.pdf` | 阿里国际 | 2025 | 推荐 | 工业 | generative pretraining, discriminative recommendation, sparse parameter freezing, overfitting, scaling law |
| `Wukong: Towards a Scaling Law for Large-Scale Recommendation.pdf` | Meta | 2024 | 推荐 | 工业 | scaling law, stacked factorization machines, synergistic upscaling, any-order interactions, model complexity |

## 3. 生成式检索 / 排序方法

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `Towards Large-scale Generative Ranking.pdf` | 小红书 | 2025 | 推荐 | 工业 | generative ranking, generative architecture, industrial-scale recommendation, GenRank |
| `Action is All You Need: Dual-Flow Generative Ranking Network for Recommendation.pdf` | 美团 | 2025 | 推荐 | 工业 | generative ranking, dual-flow mechanism, HSTU, user behavior sequences, scaling law |
| `PinRec: Outcome-Conditioned, Multi-Token Generative Retrieval for Industry-Scale Recommendation Systems.pdf` | Pinterest | 2024 | 推荐 | 工业 | generative retrieval, outcome-conditioned generation, multi-token generation, industrial-scale recommendation, diversity |
| `A Generative Re-ranking Model for List-level Multi-objective Optimization at Taobao.pdf` | 阿里 | 2024 | 推荐 | 工业 | generative re-ranking, list-level multi-objective optimization, ordered regression, diversity |
| `Leveraging Passage Embeddings for Efficient Listwise Reranking with Large Language Models.pdf` | 人大 | 2025 | 搜索 | 学术 | passage reranking, listwise reranking, LLM, passage embeddings, context compression |
| `A Neural Corpus Indexer for Document Retrieval.pdf` | Microsoft | 2022 | 搜索 | 工业 | document retrieval, neural corpus indexer, sequence-to-sequence, semantic document identifiers, prefix-aware weight-adaptive decoder |
| `Generative Retrieval as Multi-Vector Dense Retrieval.pdf` | 山东大学 | 2024 | 搜索 | 学术 | generative retrieval, multi-vector dense retrieval, document identifiers, relevance alignment matrix, term matching |
| `Learning to Rank in Generative Retrieval.pdf` | 港理工 | 2024 | 搜索 | 学术 | generative retrieval, learning-to-rank, ranking loss, passage identifiers, learning gap |
| `GraphRAG-IRL: Personalized Recommendation with Graph-Grounded Inverse Reinforcement Learning and LLM Re-ranking.pdf` | Purdue | 2026 | 推荐 | 学术 | inverse reinforcement learning, GraphRAG, LLM re-ranking, heterogeneous knowledge graph, persona-guided fusion |

## 4. LLM4Rec 与对齐

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `Recommendation as Language Processing (RLP): A Unified Pretrain, Personalized Prompt & Predict Paradigm (P5).pdf` | Rutgers | 2022 | 推荐 | 学术 | text-to-text paradigm, personalized prompt, pretraining, unified recommendation, language grounding |
| `GPT4Rec: A Generative Framework for Personalized Recommendation and User Interests Interpretation.pdf` | Amazon | 2023 | 推荐 | 工业 | generative recommendation, search query generation, multi-query beam search, cold-start, interpretability |
| `TALLRec: An Effective and Efficient Tuning Framework to Align Large Language Model with Recommendation.pdf` | USTC | 2023 | 推荐 | 学术 | instruction tuning, LLM alignment, recommendation, cross-domain generalization, parameter efficiency |
| `LLaRA: Large Language-Recommendation Assistant.pdf` | USTC | 2023 | 推荐 | 学术 | sequential recommendation, hybrid prompting, ID embeddings, curriculum learning, LLM |
| `Text Is All You Need: Learning Language Representations for Sequential Recommendation.pdf` | UCSD / Amazon | 2023 | 推荐 | 学术 | language representations, sequential recommendation, bi-directional Transformer, cold-start, item attributes |
| `Bridging Items and Language: A Transition Paradigm for Large Language Model-Based Recommendation.pdf` | 新加坡国立 | 2024 | 推荐 | 学术 | LLM-based recommendation, item indexing, generation grounding, multi-facet identifiers, substring indexing |
| `Towards Universal Sequence Representation Learning for Recommender Systems.pdf` | 人大 | 2022 | 推荐 | 学术 | universal sequence representation learning, transferable representations, parametric whitening, mixture-of-experts adaptor, contrastive pre-training |
| `Representation Learning with Large Language Models for Recommendation.pdf` | 香港大学 | 2024 | 推荐 | 学术 | LLM-empowered representation learning, cross-view alignment, user/item profiling, collaborative signals, mutual information maximization |
| `Customizing Language Models with Instance-wise LoRA for Sequential Recommendation.pdf` | USTC | 2024 | 推荐 | 学术 | sequential recommendation, instance-wise LoRA, mixture-of-experts, parameter-efficient fine-tuning, negative transfer |
| `RecGPT: Generative Pre-training for Text-based Recommendation.pdf` | VinAI | 2024 | 推荐 | 工业 | text-based recommendation, generative pre-training, LLM, instruction tuning, rating prediction |
| `SLMRec: Distilling Large Language Models into Small for Sequential Recommendation.pdf` | Rutgers | 2025 | 推荐 | 学术 | knowledge distillation, small language models, sequential recommendation, layer redundancy, model compression |
| `EAGER-LLM: Enhancing Large Language Models as Recommenders through Exogenous Behavior-Semantic Integration.pdf` | 浙大 | 2025 | 推荐 | 学术 | generative recommendation, LLM-based recommender, dual-source item indices, multiscale alignment, annealing adapter |
| `LLM-ESR: Large Language Models Enhancement for Long-tailed Sequential Recommendation.pdf` | 西安交大 / 腾讯 | 2024 | 推荐 | 学术 | sequential recommendation, long-tail recommendation, LLM semantic embeddings, dual-view modeling, retrieval augmented self-distillation |
| `E4SRec: An Elegant Effective Efficient Extensible Solution of Large Language Models for Sequential Recommendation.pdf` | 清华 | 2023 | 推荐 | 学术 | LLM-based recommendation, sequential recommendation, ID-based recommendation, pluggable parameters, frozen LLM |
| `RecRanker: Instruction Tuning Large Language Model as Ranker for Top-k Recommendation.pdf` | 香港城市大学 | 2024 | 推荐 | 学术 | instruction tuning, LLM as ranker, top-k recommendation, adaptive sampling, hybrid ranking |

## 5. 长序列建模

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders.pdf` | 字节 | 2025 | 推荐 | 工业 | long-sequence modeling, scaling law, global token, token merge module, industrial recommender |
| `Make It Long, Keep It Fast: End-to-End 10k-Sequence Modeling at Billion Scale on Douyin.pdf` | 抖音 | 2024 | 推荐 | 工业 | long-sequence modeling, STCA, Request Level Batching, length-extrapolative training, scaling law |

## 6. 工业落地系统

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `OneRec: Unifying Retrieve and Rank with Generative Recommender and Preference Alignment.pdf` | 快手 | 2024 | 推荐 | 工业 | generative retrieval, sparse Mixture-of-Experts, session-wise generation, preference alignment, DPO |
| `OneRec Technical Report.pdf` | 快手 | 2024 | 推荐 | 工业 | end-to-end generative recommendation, scaling law, reinforcement learning, MFU, cascaded architecture |
| `OneRec-V2 Technical Report.pdf` | 快手 | 2025 | 推荐 | 工业 | decoder-only architecture, preference alignment, duration-aware reward shaping, generative recommendation, scaling |
| `MTGR: Industrial-Scale Generative Recommendation Framework in Meituan.pdf` | 美团 | 2024 | 推荐 | 工业 | generative recommendation, scaling law, HSTU, cross features, Group-Layer Normalization |
| `HLLM: Enhancing Sequential Recommendations via Hierarchical Large Language Models for Item and User Modeling.pdf` | 字节 | 2024 | 推荐 | 工业 | sequential recommendation, hierarchical LLM, item modeling, user modeling, scalability |
| `Next-User Retrieval: Enhancing Cold-Start Recommendations via Generative Next-User Modeling.pdf` | 字节 | 2025 | 推荐 | 工业 | cold-start, next-user generation, lookalike, generative modeling, transformer |
| `MTFM: A Scalable and Alignment-free Foundation Model for Industrial Recommendation in Meituan.pdf` | 美团 | 2026 | 推荐 | 工业 | industrial recommendation foundation model, multi-scenario, cross-domain, alignment-free, heterogeneous tokens |
| `The Tencent Advertising Algorithm Challenge 2025: All-Modality Generative Recommendation.pdf` | 腾讯 | 2026 | 推荐 | 工业 | generative recommendation, all-modality, benchmark dataset, multi-modal sequence generation, advertising |

## 7. 多模态推荐

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `AlignRec: Aligning and Training in Multimodal Recommendations.pdf` | 上海交大 | 2024 | 推荐 | 学术 | multimodal recommendation, alignment, content-ID alignment, representation misalignment, pre-training |
| `Molar: Multimodal LLMs with Collaborative Filtering Alignment for Enhanced Sequential Recommendation.pdf` | USTC | 2024 | 推荐 | 学术 | multimodal LLM, collaborative filtering, sequential recommendation, post-alignment, multimodal item representation |

## 8. 基础设施 / 基础模型

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention.pdf` | DeepSeek | 2025 | 通用 | 工业 | sparse attention, long-context modeling, hardware-aligned optimization, hierarchical sparse strategy, end-to-end training |
| `Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free.pdf` | 阿里 | 2025 | 通用 | 工业 | gated attention, sigmoid gate, sparsity, attention sink, long-context extrapolation |
| `TokenFormer: Rethinking Transformer Scaling with Tokenized Model Parameters.pdf` | 马普所 | 2024 | 通用 | 学术 | tokenized model parameters, natively scalable architecture, token-parameter attention, progressive scaling |
| `MambaVision: A Hybrid Mamba-Transformer Vision Backbone.pdf` | NVIDIA | 2024 | 通用 | 工业 | hybrid Mamba-Transformer backbone, vision, self-attention, long-range spatial dependencies, hierarchical architecture |
| `GPT-4 Technical Report.pdf` | OpenAI | 2023 | 通用 | 工业 | GPT-4, multimodal, post-training alignment, predictable scaling, Transformer |
| `DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models.pdf` | DeepSeek | 2024 | 通用 | 工业 | DeepSeek Sparse Attention, reinforcement learning, agentic post-training, long-context, reasoning |
| `DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models.pdf` | DeepSeek | 2024 | 通用 | 工业 | mixture-of-experts, expert specialization, fine-grained expert segmentation, shared experts, MoE |
| `Qwen2.5-1M Technical Report.pdf` | 阿里 | 2024 | 通用 | 工业 | long-context modeling, length extrapolation, sparse attention, chunked prefill, 1M tokens |

## 9. CTR 训练 / 工程

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `PPM: A Pre-trained Plug-in Model for Click-through Rate Prediction.pdf` | 京东 | 2024 | 推荐 | 工业 | CTR prediction, pre-trained plug-in model, multimodal features, cold-start, end-to-end training |
| `Multi-Epoch Learning for Deep Click-Through Rate Prediction Models.pdf` | 快手 | 2023 | 推荐 | 工业 | multi-epoch learning, data augmentation, embedding overfitting, CTR prediction, MEDA |
| `Multi-Epoch learning with Data Augmentation for Deep Click-Through Rate Prediction.pdf` | 快手 | 2024 | 推荐 | 工业 | multi-epoch learning, data augmentation, embedding overfitting, CTR prediction, catastrophic forgetting |

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
