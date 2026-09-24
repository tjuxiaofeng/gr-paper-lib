# 生成式搜推论文库 index

> 📌 本目录按 **生成式推荐（GR）pipeline 阶段** 组织：从 Semantic ID → 生成式骨干 → 检索/排序 → LLM4Rec → 长序列 → 工业落地 → 多模态 → 基础设施 → CTR 工程。
>
> 📅 最后更新：2026-09-24
>
> 🎯 选取标准：大厂工业界实践 + Top 高校研究 + GR 方向奠基/代表工作

---

## 📚 目录

- [1. Semantic ID](#1-semantic-id)
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

## 1. Semantic ID

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `Recommender Systems with Generative Retrieval.pdf` | Google | 2023 | 推荐 | 工业 | generative retrieval, Semantic ID, sequence-to-sequence, codewords, cold-start |
| `Sparse Meets Dense: Unified Generative Recommendations with Cascaded Sparse-Dense Representations.pdf` | 百度 | 2025 | 推荐 | 工业 | generative retrieval, cascaded sparse-dense representations, Semantic ID, dense retrieval, BeamFusion |
| `Adapting Large Language Models by Integrating Collaborative Semantics for Recommendation.pdf` | USTC | 2023 | 推荐 | 学术 | LLM-based recommendation, collaborative semantics, item indexing, vector quantization, alignment tuning |
| `Learning Vector-Quantized Item Representation for Transferable Sequential Recommenders.pdf` | 人大 | 2022 | 推荐 | 学术 | transferable sequential recommender, vector-quantized item representation, item code, contrastive pre-training, cross-domain fine-tuning |
| `IDGenRec: LLM-RecSys Alignment with Textual ID Learning.pdf` | Rutgers | 2024 | 推荐 | 学术 | generative recommendation, textual ID learning, LLM alignment, foundation model, zero-shot |
| `Generative Recommender with End-to-End Learnable Item Tokenization.pdf` | 人大 | 2025 | 推荐 | 学术 | generative recommendation, item tokenization, end-to-end learning, sequence-item alignment, preference-semantic alignment |
| `Semantic Convergence: Harmonizing Recommender Systems via Two-Stage Alignment and Behavioral Semantic Tokenization.pdf` | 美团 | 2025 | 推荐 | 工业 | two-stage alignment, behavioral semantic tokenization, Alignment Tokenization, LLM, collaborative semantics |
| `FORGE: Forming Semantic Identifiers for Generative Retrieval in Industrial Datasets.pdf` | 浙大 / 阿里 | 2025 | 推荐 | 工业 | semantic identifiers, generative retrieval, SID construction, SID evaluation metrics, benchmark |
| `EAGER: Two-Stream Generative Recommender with Behavior-Semantic Collaboration.pdf` | 浙大 / 华为 | 2024 | 推荐 | 工业 | generative retrieval, two-stream generation, behavior-semantic collaboration, semantic tokens, contrastive learning |
| `TokenRec: Learning to Tokenize ID for LLM-based Generative Recommendation.pdf` | 港理工 | 2024 | 推荐 | 学术 | ID tokenization, LLM-based recommendation, vector quantization, generative retrieval, collaborative filtering |
| `Multi-Aspect Cross-modal Quantization for Generative Recommendation.pdf` | 北航 / 美团 | 2025 | 推荐 | 工业 | generative recommendation, cross-modal quantization, semantic IDs, multimodal alignment, codebook |
| `Reasoning over Semantic IDs Enhances Generative Recommendation.pdf` | 新加坡国立 / USTC | 2026 | 推荐 | 学术 | generative recommendation, semantic IDs, SID-language alignment, LLM reasoning, reinforced optimization |
| `Tokenize Once, Recommend Anywhere: Unified Item Tokenization for Multi-domain LLM-based Recommendation.pdf` | Yonsei University | 2025 | 推荐 | 学术 | item tokenization, multi-domain recommendation, mixture-of-experts, codebook, LLM-based recommendation |
| `Bi-Level Optimization for Generative Recommendation: Bridging Tokenization and Generation.pdf` | USTC / 北航 | 2025 | 推荐 | 学术 | generative recommendation, bi-level optimization, item tokenization, meta-learning, gradient surgery |
| `From IDs to Semantics: A Generative Framework for Cross-Domain Recommendation with Adaptive Semantic Tokenization.pdf` | 西交利物浦大学 / University of Liverpool | 2025 | 推荐 | 学术 | cross-domain recommendation, generative recommendation, semantic IDs, domain-adaptive tokenization, prefix-tree decoding |
| `Mitigating Collaborative Semantic ID Staleness in Generative Retrieval.pdf` | ITMO University | 2026 | 推荐 | 学术 | generative retrieval, semantic IDs, SID staleness, temporal drift, SID alignment |
| `S$^2$GR: Stepwise Semantic-Guided Reasoning in Latent Space for Generative Recommendation.pdf` | 快手 | 2026 | 推荐 | 工业 | generative recommendation, semantic IDs, latent reasoning, stepwise semantic guidance, codebook optimization |
| `Semantic IDs for Recommender Systems at Snapchat: Use Cases, Technical Challenges, and Design Choices.pdf` | Snap | 2026 | 推荐 | 工业 | semantic IDs, recommender systems, residual quantization, item identifiers, ranking features |
| `Generative Next POI Recommendation with Semantic ID.pdf` | 电子科大 | 2025 | 推荐 | 学术 | next POI recommendation, semantic IDs, generative recommendation, residual quantized VAE, LLM-based recommendation |
| `Bridging Textual-Collaborative Gap through Semantic Codes for Sequential Recommendation.pdf` | 人大 | 2025 | 推荐 | 学术 | sequential recommendation, semantic codes, vector quantization, textual-collaborative fusion, code masking |
| `ActionPiece: Contextually Tokenizing Action Sequences for Generative Recommendation.pdf` | UCSD / Google | 2025 | 推荐 | 工业 | generative recommendation, contextual tokenization, action sequences, item features, set permutation regularization |
| `Intent-Driven Semantic ID Generation for Grounded Conversational News Recommendation.pdf` | 中山大学 / 腾讯 | 2026 | 推荐 | 工业 | conversational news recommendation, semantic ID generation, Generate-then-Match, Chain-of-Thought distillation, cold-start |
| `Diffusion Generative Recommendation with Continuous Tokens.pdf` | 香港城市大学 / 国防科大 | 2025 | 推荐 | 学术 | generative recommendation, continuous tokens, diffusion model, sigma-VAE tokenizer, item tokenization |
| `MVIGER: Multi-View Variational Integration of Complementary Knowledge for Generative Recommender.pdf` | Yonsei University / Korea University | 2024 | 推荐 | 学术 | generative recommender, prompt template, item index, variational framework, complementary knowledge |
| `Inductive Generative Recommendation via Retrieval-based Speculation.pdf` | UCSD | 2024 | 推荐 | 学术 | generative recommendation, inductive recommendation, retrieval-based speculation, drafter-verifier, guided re-drafting |
| `Differentiable Semantic ID for Generative Recommendation.pdf` | University of Glasgow / 山东大学 | 2026 | 推荐 | 学术 | generative recommendation, semantic ID, differentiable semantic indexing, Gumbel noise, codebook collapse |
| `APAO: Bridging the Training-Inference Gap in Generative Recommendation via Adaptive Prefix-Aware Optimization.pdf` | 清华 / 泉城实验室 | 2026 | 推荐 | 学术 | generative recommendation, training-inference inconsistency, beam search, prefix-level optimization, worst-prefix optimization |
| `UNGER: Generative Recommendation with A Unified Code via Semantic and Collaborative Integration.pdf` | 华为 / 华科 | 2025 | 推荐 | 工业 | generative recommendation, unified code, semantic and collaborative integration, quantization, knowledge distillation |
| `Towards Distribution Matching between Collaborative and Language Spaces for Generative Recommendation.pdf` | 安徽大学 / The University of Queensland | 2025 | 推荐 | 学术 | generative recommendation, distribution matching, pre-trained language models, probabilistic meta-network, cross-space alignment |
| `GRAM: Generative Recommendation via Semantic-aware Multi-granular Late Fusion.pdf` | Samsung | 2025 | 推荐 | 学术 | generative recommendation, multi-granular late fusion, semantic-to-lexical translation, LLM, item relationships |

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
| `Collaborative Memory Augmentation for Generative Recommendation.pdf` | 人大 / 字节 | 2026 | 推荐 | 工业 | generative recommendation, collaborative memory augmentation, latent context compression, target-aware retrieval, gated cross-attention |
| `Preference Diffusion for Recommendation.pdf` | 华东师大 / 新加坡国立 | 2024 | 推荐 | 学术 | diffusion models, preference ranking, recommender systems, BPR, direct preference optimization |
| `Understanding Generative Recommendation with Semantic IDs from a Model-scaling View.pdf` | Michigan State University / Snap | 2025 | 推荐 | 工业 | generative recommendation, semantic IDs, scaling laws, LLM-as-recommender, quantization tokenizer |
| `Beyond the Flat Sequence: Hierarchical and Preference-Aware Generative Recommendations.pdf` | 哈工大 / 华为 | 2026 | 推荐 | 工业 | generative recommender, HSTU, hierarchical sequence modeling, masked item modeling, sparse attention |
| `DiffGRM: Diffusion-based Generative Recommendation Model.pdf` | 快手 | 2025 | 推荐 | 工业 | generative recommendation, discrete diffusion, semantic IDs, parallel decoding, item tokenization |
| `Massive Memorization with Hundreds of Trillions of Parameters for Sequential Transducer Generative Recommenders.pdf` | Meta / Yale University | 2025 | 推荐 | 工业 | generative recommender, sequential transducer, virtual sequential target attention, user history summarization, long-sequence modeling |
| `Equip Pre-ranking with Target Attention by Residual Quantization.pdf` | 阿里 / 上海交大 | 2025 | 推荐 | 工业 | pre-ranking, target attention, residual quantization, industrial recommendation, efficiency |
| `OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender.pdf` | NTU / 字节 | 2025 | 推荐 | 工业 | unified Transformer, feature interaction, sequence modeling, causal attention, KV caching |
| `From Scaling to Structured Expressivity: Rethinking Transformers for CTR Prediction.pdf` | 阿里 | 2025 | 推荐 | 工业 | structured expressivity, CTR prediction, Field-Aware Transformer, Basis-Composed Hypernetwork, scaling law |
| `FuXi-$γ$: Efficient Sequential Recommendation with Exponential-Power Temporal Encoder and Diagonal-Sparse Positional Mechanism.pdf` | 南开 / 华为 | 2025 | 推荐 | 工业 | sequential recommendation, exponential-power temporal encoder, diagonal-sparse positional mechanism, long-sequence recommendation, Ebbinghaus forgetting curve |
| `Principled Synthetic Data Enables the First Scaling Laws for LLMs in Recommendation.pdf` | Meta | 2026 | 推荐 | 工业 | scaling law, synthetic data, LLM, continual pre-training, pedagogical curriculum |
| `MixFormer: Co-Scaling Up Dense and Sequence in Industrial Recommenders.pdf` | 字节 | 2026 | 推荐 | 工业 | co-scaling, feature interaction, sequence modeling, unified Transformer, user-item decoupling |
| `FuXi-$α$: Scaling Recommendation Model with Feature Interaction Enhanced Transformer.pdf` | USTC / 华为 | 2025 | 推荐 | 工业 | scaling law, feature interaction, Adaptive Multi-channel Self-attention, Multi-stage FFN, sequential recommendation |
| `Killing Two Birds with One Stone: Unifying Retrieval and Ranking with a Single Generative Recommendation Model.pdf` | USTC / 华为 | 2025 | 推荐 | 工业 | generative recommendation, unifying retrieval and ranking, ranking-driven enhancer, gradient-guided adaptive weighter, sequence generation |
| `STAR-Rec: Making Peace with Length Variance and Pattern Diversity in Sequential Recommendation.pdf` | 香港城市大学 / 南科大 | 2025 | 推荐 | 学术 | sequential recommendation, state-space modeling, mixture-of-experts, preference-aware attention, length variance |

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
| `Towards Context-aware Reasoning-enhanced Generative Searching in E-commerce.pdf` | USTC / 快手 | 2025 | 搜索 | 工业 | generative search, context-aware recommendation, reasoning-enhanced recommendation, self-evolving post-training, debiased GRPO |
| `Constrained Auto-Regressive Decoding Constrains Generative Retrieval.pdf` | 山东大学 / Leiden University | 2025 | 搜索 | 学术 | generative retrieval, constrained auto-regressive decoding, beam search, generalization, out-of-distribution corpora |
| `Semantic-Enhanced Differentiable Search Index Inspired by Learning Strategies.pdf` | 中科院 / 国科大 | 2023 | 搜索 | 学术 | differentiable search index, document identifiers, semantic enhancement, learning strategies, document retrieval |
| `Transformer Memory as a Differentiable Search Index.pdf` | Google | 2022 | 搜索 | 工业 | differentiable search index, document identifiers, transformer memory, text-to-text retrieval, zero-shot generalization |
| `Lost in Decoding? Reproducing and Stress-Testing the Look-Ahead Prior in Generative Retrieval.pdf` | Univ. of Amsterdam | 2026 | 搜索 | 学术 | generative retrieval, look-ahead prior, planning-guided decoding, beam search, plan drift |
| `A Parametric Memory Head for Continual Generative Retrieval.pdf` | Univ. of Amsterdam | 2026 | 搜索 | 学术 | generative retrieval, continual learning, parametric memory head, catastrophic forgetting, docid decoding |
| `Model Editing for New Document Integration in Generative Information Retrieval.pdf` | 山东大学 / Univ. of Amsterdam | 2026 | 搜索 | 学术 | generative information retrieval, model editing, document identifiers, new document integration, catastrophic forgetting |
| `ZeroGR: A Generalizable and Scalable Framework for Zero-Shot Generative Retrieval.pdf` | CMU / 山东大学 | 2025 | 搜索 | 学术 | zero-shot generative retrieval, docid generation, instruction tuning, reverse annealing decoding, information retrieval |
| `Lightweight and Direct Document Relevance Optimization for Generative Information Retrieval.pdf` | Univ. of Amsterdam | 2025 | 搜索 | 学术 | generative information retrieval, document relevance optimization, pairwise ranking, token-level misalignment, docid generation |
| `Generative Retrieval Meets Multi-Graded Relevance.pdf` | 中科院 / 国科大 | 2024 | 搜索 | 学术 | generative retrieval, multi-graded relevance, constrained contrastive training, document identifiers, relevance grades |
| `Planning Ahead in Generative Retrieval: Guiding Autoregressive Generation through Simultaneous Decoding.pdf` | UMass Amherst / Amazon | 2024 | 搜索 | 工业 | generative retrieval, planning ahead, simultaneous decoding, document identifiers, autoregressive generation |
| `TOME: A Two-stage Approach for Model-based Retrieval.pdf` | 人大 / 百度 | 2023 | 搜索 | 工业 | model-based retrieval, document identifiers, tokenized URLs, two-stage generation, scaling laws |
| `DeGRe: Dense-supervised Generative Reranking for Recommendation.pdf` | 浙大 / 阿里 | 2026 | 搜索 | 工业 | generative reranking, dense supervision, listwise recommendation, lookahead planning, online generation |
| `Replication and Exploration of Generative Retrieval over Dynamic Corpora.pdf` | 山东大学 / 百度 | 2025 | 搜索 | 工业 | generative retrieval, dynamic corpora, docid design, text-based docids, multi-docid |
| `One Pass, Any Order: Position-Invariant Listwise Reranking for LLM-Based Recommendation.pdf` | RMIT University | 2026 | 搜索 | 学术 | listwise reranking, permutation invariance, position bias, RoPE, structured attention mask |
| `Multi-Layer Ranking with Large Language Models for News Source Recommendation.pdf` | University of Warwick / King's College London | 2024 | 搜索 | 学术 | expert recommendation, multi-layer ranking, in-context learning, NewsQuote |
| `ReasonRank: Empowering Passage Ranking with Strong Reasoning Ability.pdf` | 人大 / 百度 | 2025 | 搜索 | 工业 | passage ranking, listwise ranking, reasoning-intensive, reinforcement learning, training data synthesis |
| `Learning from Emptiness: De-biasing Listwise Rerankers with Content-Agnostic Probability Calibration.pdf` | USTC / 阿里 | 2026 | 搜索 | 工业 | listwise reranking, position bias, probability calibration, training-free, entropy-adaptive contrastive |
| `From Relevance to Authority: Authority-aware Generative Retrieval in Web Search Engines.pdf` | Sungkyunkwan Univ / NAVER | 2026 | 搜索 | 学术 | generative retrieval, authority-aware retrieval, multimodal authority scoring, web search, GenIR |
| `How Generative AI Disrupts Search: An Empirical Study of Google Search, Gemini, and AI Overviews.pdf` | NJIT / NTU | 2026 | 搜索 | 学术 | generative search, AI Overviews, Gemini, search visibility, source retrieval |
| `Personalized Deep Research: A User-Centric Framework, Dataset, and Hybrid Evaluation for Knowledge Discovery.pdf` | 香港城市大学 / 华为 | 2026 | 搜索 | 工业 | personalized deep research, user profile modeling, dual-stage retrieval, hybrid evaluation, knowledge discovery |
| `Very Efficient Listwise Multimodal Reranking for Long Documents.pdf` | Mitsubishi Research Institute | 2026 | 搜索 | 学术 | listwise multimodal reranking, vision-centric retrieval, multimodal retrieval-augmented generation, query-image early interaction, single forward pass |
| `Layer-wise Token Compression for Efficient Document Reranking.pdf` | Amazon | 2026 | 搜索 | 工业 | document reranking, token compression, cross-encoder reranker, listwise LLM reranker, length-invariant representations |
| `Generative Retrieval for Unsupervised Text-Based Person Search.pdf` | 苏州大学 / 哈工大 | 2026 | 搜索 | 学术 | text-based person search, unsupervised, generative retrieval, tiered description generation, Gaussian Mixture Model |
| `Exploring Training and Inference Scaling Laws in Generative Retrieval.pdf` | 新加坡国立 / 港理工 | 2025 | 搜索 | 学术 | generative retrieval, scaling law, inference-time compute, contrastive entropy, n-gram |
| `Alleviating LLM-based Generative Retrieval Hallucination in Alipay Search.pdf` | 上海交大 / 蚂蚁 | 2025 | 搜索 | 工业 | generative retrieval, hallucination, knowledge distillation, decision agent, LLM |
| `Generative Retrieval and Alignment Model: A New Paradigm for E-commerce Retrieval.pdf` | 京东 | 2025 | 搜索 | 工业 | e-commerce retrieval, generative retrieval, text identifier, co-alignment, query-product scoring |
| `AcuRank: Uncertainty-Aware Adaptive Computation for Listwise Reranking.pdf` | Seoul National University / UCSB | 2025 | 搜索 | 学术 | listwise reranking, uncertainty-aware, adaptive computation, Bayesian TrueSkill, accuracy-efficiency trade-off |
| `Evaluating Generative Ad Hoc Information Retrieval.pdf` | Leipzig University / The University of Queensland | 2023 | 搜索 | 学术 | generative retrieval, evaluation methodology, ad hoc retrieval, user model, generated responses |
| `ListT5: Listwise Reranking with Fusion-in-Decoder Improves Zero-shot Retrieval.pdf` | Seoul National University / LG AI Research | 2024 | 搜索 | 学术 | listwise reranking, Fusion-in-Decoder, zero-shot retrieval, tournament sort, lost-in-the-middle |
| `Listwise Generative Retrieval Models via a Sequential Learning Process.pdf` | 中科院 / 国科大 | 2024 | 搜索 | 学术 | generative retrieval, listwise, sequential learning process, docid, relevance calibration |
| `Event GDR: Event-Centric Generative Document Retrieval.pdf` | 清华 / 山西大学 | 2024 | 搜索 | 学术 | generative document retrieval, event-centric, event taxonomy, identifier construction, document representation |
| `Bottleneck-Minimal Indexing for Generative Document Retrieval.pdf` | Waseda University | 2024 | 搜索 | 学术 | generative document retrieval, indexing, rate-distortion, mutual information, bottleneck |
| `T2Ranking: A large-scale Chinese Benchmark for Passage Ranking.pdf` | 清华 / 中关村实验室 | 2023 | 搜索 | 学术 | passage ranking, Chinese benchmark, graded relevance, passage retrieval, re-ranking |
| `A Unified Generative Retriever for Knowledge-Intensive Language Tasks via Prompt Learning.pdf` | 中科院 / 国科大 | 2023 | 搜索 | 学术 | generative retriever, knowledge-intensive language tasks, prompt learning, n-gram identifier, multi-task |
| `Multiview Identifiers Enhanced Generative Retrieval.pdf` | 港理工 / Microsoft | 2023 | 搜索 | 工业 | generative retrieval, multiview identifiers, synthetic identifiers, docid, passage ranking |

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
| `Hierarchical Residual Policy Optimization for Generative Recommendations.pdf` | 香港城市大学 / 快手 | 2026 | 推荐 | 工业 | generative recommendations, semantic identifiers (SIDs), post-training, token-level credit assignment, hierarchical residual policy optimization |
| `Think2Go: Generative Next POI Recommendation with LLM Reasoning.pdf` | 大连理工 / 武大 | 2026 | 推荐 | 学术 | next POI recommendation, semantic IDs, LLM reasoning, test-time scaling, reinforcement learning |
| `OpenP5: An Open-Source Platform for Developing, Training, and Evaluating LLM-based Recommender Systems.pdf` | Rutgers | 2023 | 推荐 | 学术 | LLM-based recommendation, open-source platform, item indexing, sequential recommendation, generative recommender systems |
| `AlphaFuse: Learn ID Embeddings for Sequential Recommendation in Null Space of Language Embeddings.pdf` | USTC / 新加坡国立 | 2025 | 推荐 | 学术 | sequential recommendation, ID embeddings, language embeddings, null space, singular value decomposition |
| `R$^2$ec: Towards Large Recommender Models with Reasoning.pdf` | 港理工 / 新加坡国立 | 2025 | 推荐 | 学术 | large recommender models, LLM reasoning, dual-head architecture, reinforcement learning, reasoning chain |
| `Leveraging Memory Retrieval to Enhance LLM-based Generative Recommendation.pdf` | USTC / 新加坡国立 | 2024 | 推荐 | 学术 | generative recommendation, memory retrieval, long-term interests, LLM-based recommendation, next-item generation |
| `Generative Archetype-Grounded Item Representations for Sequential Recommendation.pdf` | 香港中文大学 / McGill University | 2026 | 推荐 | 学术 | sequential recommendation, item representations, generative archetype, behavioral calibration, LLM |
| `RAIE: Region-Aware Incremental Preference Editing with LoRA for LLM-based Recommendation.pdf` | 中山大学 / 厦门大学 | 2026 | 推荐 | 学术 | LLM-based recommendation, incremental preference editing, LoRA, preference drift, catastrophic forgetting |
| `FeDecider: An LLM-Based Framework for Federated Cross-Domain Recommendation.pdf` | UIUC | 2026 | 推荐 | 学术 | federated cross-domain recommendation, LLM-based recommendation, low-rank update disentanglement, domain-specific adapters, personalized aggregation |
| `Token-level Collaborative Alignment for LLM-based Generative Recommendation.pdf` | USTC / Rutgers | 2026 | 推荐 | 学术 | generative recommendation, collaborative filtering, token-level alignment, soft label alignment, next-token prediction |
| `LLM Reasoning for Cold-Start Item Recommendation.pdf` | UT Austin | 2025 | 推荐 | 学术 | cold-start item recommendation, LLM reasoning, supervised fine-tuning, reinforcement learning fine-tuning, hybrid fine-tuning |
| `AgentDR: Dynamic Recommendation with Implicit Item-Item Relations via LLM-based Agents.pdf` | Amazon / University of Michigan | 2025 | 推荐 | 工业 | LLM-based agents, item-item relations, substitute and complement relationships, full-catalog ranking, hallucination mitigation |
| `Every Preference Has Its Strength: Injecting Ordinal Semantics into LLM-Based Recommenders.pdf` | KAIST | 2026 | 推荐 | 学术 | ordinal preference, semantic anchors, collaborative filtering signals, hybrid CF-LLM, preference strength |
| `Beyond Static Best-of-N: Bayesian List-wise Alignment for LLM-based Recommendation.pdf` | USTC / 浙大 | 2026 | 推荐 | 学术 | list-wise alignment, Best-of-N, Bayesian framework, LLM4Rec, ranking metrics |
| `ProMax: Exploring the Potential of LLM-derived Profiles with Distribution Shaping for Recommender Systems.pdf` | 安徽大学 / 电子科大 | 2026 | 推荐 | 学术 | LLM-derived profiles, distribution shaping, dense retrieval, user profiles, implicit feedback |
| `Filling the Gaps: Selective Knowledge Augmentation for LLM Recommenders.pdf` | POSTECH / Korea University | 2026 | 推荐 | 学术 | knowledge gap problem, selective knowledge augmentation, training-free recommender, context efficiency, knowledge probing |
| `ItemRAG: Item-Based Retrieval-Augmented Generation for LLM-Based Recommendation.pdf` | Seoul National University | 2025 | 推荐 | 学术 | retrieval-augmented generation, item-level retrieval, cold-start recommendation, co-purchase, LLM-based recommendation |
| `SPRINT: Scalable and Predictive Intent Refinement for LLM-Enhanced Session-based Recommendation.pdf` | UIUC / Korea University | 2025 | 推荐 | 学术 | session-based recommendation, LLM profiling, intent prediction, scalability, hallucination mitigation |
| `Mixture-of-Experts Knowledge Graph Retrieval-Augmented Generation for Multi-Agent LLM-based Recommendation.pdf` | 港理工 / 新加坡国立 | 2026 | 推荐 | 学术 | knowledge graph retrieval-augmented generation, Mixture-of-Experts, multi-agent, contrastive learning, policy optimization |
| `Enriching Semantic Profiles into Knowledge Graph for Recommender Systems Using Large Language Models.pdf` | Inha University / Sogang University | 2026 | 推荐 | 学术 | semantic profiles, knowledge graph, LLM, profile-aware KG aggregation, preference matching |
| `ReRec: Reasoning-Augmented LLM-based Recommendation Assistant via Reinforcement Fine-tuning.pdf` | 港理工 | 2026 | 推荐 | 学术 | reinforcement fine-tuning, reasoning-augmented recommendation, reward shaping, curriculum learning, recommendation assistant |
| `Mirroring Users: Towards Building Preference-aligned User Simulator with User Feedback in Recommendation.pdf` | NTU / 浙大 | 2025 | 推荐 | 学术 | user simulation, preference alignment, user feedback, data distillation, uncertainty estimation |
| `What Makes LLMs Effective Sequential Recommenders? A Study on Preference Intensity and Temporal Context.pdf` | Dartmouth College / 字节 | 2025 | 推荐 | 工业 | preference intensity, temporal context, preference optimization, sequential recommendation, reward margins |
| `AgentSociety Challenge: Designing LLM Agents for User Modeling and Recommendation on Web Platforms.pdf` | 清华 / 香港科技大学（广州） | 2025 | 推荐 | 学术 | LLM agents, user modeling, agent benchmark, interactive environment simulator, web platforms |
| `Uncertainty Quantification and Decomposition for LLM-based Recommendation.pdf` | POSTECH / Korea University | 2025 | 推荐 | 学术 | uncertainty quantification, uncertainty decomposition, reliability, uncertainty-aware prompting, LLM-based recommendation |
| `SPRec: Self-Play to Debias LLM-based Recommendation.pdf` | USTC / 香港科技大学 | 2024 | 推荐 | 学术 | self-play, debiasing, DPO, fairness, filter bubble |
| `Beyond Utility: Evaluating LLM as Recommender.pdf` | 清华 / 泉城实验室 | 2024 | 推荐 | 学术 | LLM-as-recommender, evaluation framework, candidate position bias, hallucination, history length sensitivity |
| `Reason4Rec: Deliberative User Preference Alignment of Large Language Models for Recommendation.pdf` | USTC / 中关村学院 | 2025 | 推荐 | 学术 | deliberative recommendation, preference alignment, reasoning, step-wise experts |
| `CoLLM: Integrating Collaborative Embeddings into Large Language Models for Recommendation.pdf` | USTC | 2023 | 推荐 | 学术 | collaborative embeddings, LLMRec, cold-start, warm-start, token embedding space |
| `X-Cross: Dynamic Integration of Language Models for Cross-Domain Sequential Recommendation.pdf` | Ben-Gurion University | 2025 | 推荐 | 学术 | cross-domain sequential recommendation, LoRA, language model integration, low-rank adapters |
| `Bridge the Domains: Large Language Models Enhanced Cross-domain Sequential Recommendation.pdf` | 西安交大 / 香港城市大学 | 2025 | 推荐 | 学术 | cross-domain sequential recommendation, LLM, contrastive regularization, hierarchical profiling, overlap dilemma |
| `Process-Supervised LLM Recommenders via Flow-guided Tuning.pdf` | USTC / 香港科技大学 | 2025 | 推荐 | 学术 | GFlowNet, process supervision, token-level reward propagation, popularity bias, diversity |
| `Pre-train, Align, and Disentangle: Empowering Sequential Recommendation with Large Language Models.pdf` | 香港城市大学 / 腾讯 | 2024 | 推荐 | 工业 | sequential recommendation, LLM, alignment, disentanglement, cold-start |
| `Review-driven Personalized Preference Reasoning with Large Language Models for Recommendation.pdf` | Yonsei University / Korea University | 2024 | 推荐 | 学术 | review-based recommendation, preference reasoning, rating prediction, explainability, distillation |
| `Can LLMs Outshine Conventional Recommenders? A Comparative Evaluation.pdf` | 港理工 / 华为 | 2025 | 推荐 | 工业 | benchmark, item representation, CTR prediction, sequential recommendation, semantic identifier |
| `LLM2Rec: Large Language Models Are Powerful Embedding Models for Sequential Recommendation.pdf` | 新加坡国立 / USTC | 2025 | 推荐 | 学术 | sequential recommendation, embedding model, collaborative filtering, supervised fine-tuning, item embeddings |
| `GORACS: Group-level Optimal Transport-guided Coreset Selection for LLM-based Recommender Systems.pdf` | 复旦 | 2025 | 推荐 | 学术 | coreset selection, optimal transport, data selection, fine-tuning efficiency |
| `Lost in Sequence: Do Large Language Models Understand Sequential Recommendation?.pdf` | NAVER / UCSD | 2025 | 推荐 | 学术 | sequential recommendation, sequential information, knowledge distillation, CF-SRec, LLM4Rec |
| `Knowledge Graph Retrieval-Augmented Generation for LLM-based Recommendation.pdf` | 港理工 / University of Birmingham | 2025 | 推荐 | 学术 | knowledge graph, retrieval-augmented generation, structure information, hallucination, K-RagRec |
| `RecLM: Recommendation Instruction Tuning.pdf` | 香港大学 / 腾讯 | 2024 | 推荐 | 工业 | recommendation instruction tuning, reinforcement learning, collaborative filtering, model-agnostic |
| `LLMEmb: Large Language Model Can Be a Good Embedding Generator for Sequential Recommendation.pdf` | 西安交大 / 香港城市大学 | 2024 | 推荐 | 学术 | item embeddings, sequential recommendation, contrastive fine-tuning, long-tail problem, collaborative signals |
| `Can Small Language Models be Good Reasoners for Sequential Recommendation?.pdf` | 北邮 / 中科院 | 2024 | 推荐 | 学术 | knowledge distillation, chain-of-thought, sequential recommendation, small language models, reasoning |
| `Sequential Recommendation with Latent Relations based on Large Language Model.pdf` | 清华 / 美团 | 2024 | 推荐 | 工业 | latent relations, sequential recommendation, relation-aware, discrete state VAE, LLM |
| `Data-efficient Fine-tuning for LLM-based Recommendation.pdf` | 新加坡国立 / 香港大学 | 2024 | 推荐 | 学术 | data pruning, few-shot fine-tuning, influence score, coreset selection |
| `On Generative Agents in Recommendation.pdf` | 新加坡国立 / 清华 | 2023 | 推荐 | 学术 | user simulator, generative agents, LLM-empowered agents, filter bubble, recommendation simulator |
| `Large Language Models meet Collaborative Filtering: An Efficient All-round LLM-based Recommender System.pdf` | NAVER | 2024 | 推荐 | 学术 | collaborative filtering, LLM-based recommender, cold-start, warm-start, model-agnostic |
| `Leveraging LLM Reasoning Enhances Personalized Recommender Systems.pdf` | UC Berkeley / Google | 2024 | 推荐 | 工业 | LLM reasoning, chain-of-thought, reasoning evaluation, personalized recommendation |
| `Stealthy Attack on Large Language Model based Recommendation.pdf` | 中科院 / 国科大 | 2024 | 推荐 | 学术 | adversarial attack, textual content, stealthiness, security vulnerability |
| `GoalRank: Group-Relative Optimization for a Large Ranking Model.pdf` | 快手 / 国科大 | 2025 | 推荐 | 工业 | group-relative optimization, generator-only ranking, one-stage ranking, scaling law, reward model |
| `Uncertainty-aware Generative Recommendation.pdf` | USTC | 2026 | 推荐 | 学术 | generative recommendation, uncertainty, preference optimization, confidence alignment, risk-aware |
| `One Model for All: Large Language Models are Domain-Agnostic Recommendation Systems.pdf` | 武大 | 2023 | 推荐 | 学术 | domain-agnostic recommendation, LLM, multi-domain, cold-start, item representation |

## 5. 长序列建模

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders.pdf` | 字节 | 2025 | 推荐 | 工业 | long-sequence modeling, scaling law, global token, token merge module, industrial recommender |
| `Make It Long, Keep It Fast: End-to-End 10k-Sequence Modeling at Billion Scale on Douyin.pdf` | 抖音 | 2024 | 推荐 | 工业 | long-sequence modeling, STCA, Request Level Batching, length-extrapolative training, scaling law |
| `Mixture of Sequence: Theme-Aware Mixture-of-Experts for Long-Sequence Recommendation.pdf` | Meta | 2026 | 推荐 | 工业 | mixture-of-experts, long-sequence recommendation, theme-aware routing, multi-scale fusion, session hopping |
| `Long-Sequence Recommendation Models Need Decoupled Embeddings.pdf` | 清华 / 腾讯 | 2024 | 推荐 | 工业 | long-sequence recommendation, decoupled embeddings, attention, representation, embedding dimension |
| `Context-based Fast Recommendation Strategy for Long User Behavior Sequence in Meituan Waimai.pdf` | 北邮 / 美团 | 2024 | 推荐 | 工业 | long user behavior sequence, context-based recommendation, prototype, temporal graph, CTR prediction |

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
| `DaV-Gen: End-to-End Generative Retrieval via Draft-and-Verify.pdf` | 阿里 | 2026 | 推荐 | 工业 | generative retrieval, Draft-and-Verify, multi-stage cascade architectures, end-to-end generation, contrastive loss |
| `GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation.pdf` | 京东 / Waseda University | 2026 | 推荐 | 工业 | generative retrieval, page-wise next-token prediction, semantic IDs, token merger, preference alignment |
| `DualGR: Generative Retrieval with Long and Short-Term Interests Modeling.pdf` | USTC / 快手 | 2025 | 推荐 | 工业 | generative retrieval, long-short term interests, semantic ID decoding, exposure-aware next-token prediction, dual-branch routing |
| `SIGMA: A Semantic-Grounded Instruction-Driven Generative Multi-Task Recommender at AliExpress.pdf` | 阿里国际 | 2026 | 推荐 | 工业 | generative recommendation, instruction-following, multi-task recommendation, item tokenization, semantic grounding |
| `Beyond Item IDs: Scaling Short-Form-Video Recommendation via Semantic-Native Long Sequence Modeling.pdf` | Google | 2026 | 推荐 | 工业 | semantic ID, long sequence modeling, short-form video recommendation, Global-Aware Compression Transformer, cold-start |
| `From Modularity to Unity: Towards Industrial-Scale Generative Recommendation.pdf` | 京东 | 2026 | 推荐 | 工业 | generative recommendation, unified ranking framework, causal behavior multi-task attention, gradient interference, dual-encoder tokenization |

## 7. 多模态推荐

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `AlignRec: Aligning and Training in Multimodal Recommendations.pdf` | 上海交大 | 2024 | 推荐 | 学术 | multimodal recommendation, alignment, content-ID alignment, representation misalignment, pre-training |
| `Molar: Multimodal LLMs with Collaborative Filtering Alignment for Enhanced Sequential Recommendation.pdf` | USTC | 2024 | 推荐 | 学术 | multimodal LLM, collaborative filtering, sequential recommendation, post-alignment, multimodal item representation |
| `Multimodal Large Language Models with Adaptive Preference Optimization for Sequential Recommendation.pdf` | 合肥工业大学 / 新加坡国立 | 2025 | 推荐 | 学术 | multimodal LLM, sequential recommendation, preference optimization, DPO, hardness-aware sampling |
| `Token-Efficient Item Representation via Images for LLM Recommender Systems.pdf` | Amazon | 2025 | 推荐 | 工业 | item representation, token efficiency, image-based representation, LLM recommender |
| `SynGR: Unleashing the Potential of Cross-Modal Synergy for Generative Recommendation.pdf` | 北航 | 2026 | 推荐 | 学术 | generative recommendation, cross-modal synergy, multimodal, synergistic information, item semantics |
| `Hierarchical Time-Aware Mixture of Experts for Multi-Modal Sequential Recommendation.pdf` | USTC / 南航 | 2025 | 推荐 | 学术 | multi-modal sequential recommendation, mixture of experts, temporal embedding, multi-task learning, contrastive learning |
| `FindRec: Stein-Guided Entropic Flow for Multi-Modal Sequential Recommendation.pdf` | 香港城市大学 / 北航 | 2025 | 推荐 | 学术 | multi-modal sequential recommendation, information disentanglement, Stein kernel, cross-modal expert routing, Mamba |

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
| `Gated Bidirectional Linear Attention for Generative Retrieval.pdf` | Yandex | 2026 | 通用 | 学术 | gated bidirectional linear attention, generative retrieval, linear-time attention, hybrid encoder, long user histories |
| `Vectorizing the Trie: Efficient Constrained Decoding for LLM-based Generative Retrieval on Accelerators.pdf` | Google / Yale University | 2026 | 通用 | 工业 | constrained decoding, generative retrieval, trie, compressed sparse row, cold-start |
| `RASTP: Representation-Aware Semantic Token Pruning for Generative Recommendation with Semantic Identifiers.pdf` | 浙大 | 2025 | 通用 | 学术 | semantic token pruning, generative recommendation, semantic identifiers, attention centrality, token importance |
| `Efficiency Unleashed: Inference Acceleration for LLM-based Recommender Systems with Speculative Decoding.pdf` | 上海交大 / 华为 | 2024 | 通用 | 工业 | speculative decoding, inference acceleration, draft-then-verify, retrieval pool, recommendation knowledge generation |
| `BlossomRec: Block-level Fused Sparse Attention Mechanism for Sequential Recommendations.pdf` | 香港城市大学 / Rutgers | 2025 | 通用 | 学术 | sparse attention, sequential recommendation, block-level fused sparse attention, long-term and short-term interests, learnable gated output |
| `Unleashing the Potential of Sparse Attention on Long-term Behaviors for CTR Prediction.pdf` | 中科院 / 国科大 | 2026 | 通用 | 学术 | CTR prediction, sparse self-attention, long-term behaviors, scaling law, relative temporal encoding |
| `CollectiveKV: Decoupling and Sharing Collaborative Information in Sequential Recommendation.pdf` | 华为 / 清华 | 2026 | 通用 | 工业 | KV cache, sequential recommendation, cross-user KV sharing, collaborative signals, inference latency |
| `Hyena Operator for Fast Sequential Recommendation.pdf` | 武汉理工 / 武汉纺织大学 | 2026 | 通用 | 学术 | sequential recommendation, Hyena operator, polynomial-based kernel parameterization, gated convolutions, Legendre orthogonal polynomials |
| `Efficient Inference for Large Language Model-based Generative Recommendation.pdf` | 新加坡国立 / 清华 | 2024 | 通用 | 学术 | generative recommendation, speculative decoding, top-K verification, draft model alignment, inference acceleration |

## 9. CTR 训练 / 工程

| 文件 | 机构 | 年份 | 一句话价值 |
|---|---|---|---|
| `PPM: A Pre-trained Plug-in Model for Click-through Rate Prediction.pdf` | 京东 | 2024 | 推荐 | 工业 | CTR prediction, pre-trained plug-in model, multimodal features, cold-start, end-to-end training |
| `Multi-Epoch Learning for Deep Click-Through Rate Prediction Models.pdf` | 快手 | 2023 | 推荐 | 工业 | multi-epoch learning, data augmentation, embedding overfitting, CTR prediction, MEDA |
| `Multi-Epoch learning with Data Augmentation for Deep Click-Through Rate Prediction.pdf` | 快手 | 2024 | 推荐 | 工业 | multi-epoch learning, data augmentation, embedding overfitting, CTR prediction, catastrophic forgetting |
| `Pre-train and Fine-tune: Recommenders as Large Models.pdf` | 香港中文大学 / 阿里 | 2025 | 推荐 | 工业 | fine-tuning, information bottleneck, information-aware adaptive kernel, pre-trained recommender, multi-domain |
| `ESANS: Effective and Semantic-Aware Negative Sampling for Large-Scale Retrieval Systems.pdf` | 阿里国际 | 2025 | 推荐 | 工业 | negative sampling, embedding-based retrieval, dense interpolation, semantic-aware clustering, false negatives |

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
