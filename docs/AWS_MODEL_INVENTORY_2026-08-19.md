# Amazon Bedrock Model Access Inventory

**Snapshot date:** 2026-08-19  
**AWS account:** `082706806837`  
**IAM principal used for the check:** `arn:aws:iam::082706806837:user/attest`  
**Region checked:** `us-east-1`

> Source: AWS CLI model-availability report supplied by the account owner. This document preserves the CLI-reported access state. Recommendations below are a practical interpretation layer, not additional AWS access claims.

## Executive summary

- **Total model entries checked:** 122
- **Usable now:** 75 (61.5%)
- **Agreement blocked:** 46 (37.7%)
- **Wrong region:** 1 (0.8%)

### Most important conclusion

All **46 agreement-blocked entries** have the same pattern in this report: `AUTHORIZED` + entitlement `AVAILABLE` + region `AVAILABLE` + agreement `NOT_AVAILABLE`. That means the visible blocker is the provider/model agreement state, not basic account authorization, entitlement eligibility, or `us-east-1` availability.

The account already has a strong usable stack across Amazon, Mistral, Meta, Qwen, OpenAI open-weight models, NVIDIA, Z.AI, Google, MiniMax, DeepSeek, Moonshot AI, and one Writer model. The major missing high-value families are the Anthropic Claude line, OpenAI GPT-5.6 Sol/Terra/Luna, Cohere, Stability AI, TwelveLabs, AI21, and Writer Palmyra X4/X5.

## How to read the statuses

| Status | Meaning in this report | Practical interpretation |
|---|---|---|
| **USABLE_NOW** | Authorized, entitlement available, region available, agreement available | Best candidate for immediate Bedrock use. Actual invocation can still depend on the model's supported inference mode and the client/tool being used. |
| **AGREEMENT_BLOCKED** | Authorized, entitlement available, region available, agreement not available | Account appears eligible, but the provider/model agreement is not active. Escalate/enable the agreement before relying on the model. |
| **WRONG_REGION** | Region availability is not available | Use another supported region if available. |

## Practical priority shortlist

This is a **derived recommendation layer** based on model names, modalities, and the access states in the CLI report. It does not change the raw AWS status.

| Best role | Model | Model ID | Current access |
|---|---|---|---|
| Primary coding / agentic engineering | Qwen3 Coder Next | `qwen.qwen3-coder-next` | **Usable now** |
| Repository-scale software engineering | Devstral 2 123B | `mistral.devstral-2-123b` | **Usable now** |
| High-end general reasoning / coding | GLM 5 | `zai.glm-5` | **Usable now** |
| Multimodal reasoning + coding | Kimi K2.5 | `moonshotai.kimi-k2.5` | **Usable now** |
| Long-form reasoning | Kimi K2 Thinking | `moonshot.kimi-k2-thinking` | **Usable now** |
| Cost-efficient agent worker | MiniMax M2.5 | `minimax.minimax-m2.5` | **Usable now** |
| General reasoning / automation | DeepSeek V3.2 | `deepseek.v3.2` | **Usable now** |
| OpenAI open-weight reasoning | gpt-oss-120b | `openai.gpt-oss-120b-1:0` | **Usable now** |
| Large agent / reasoning worker | NVIDIA Nemotron 3 Super 120B A12B | `nvidia.nemotron-super-3-120b` | **Usable now** |
| AWS-native multimodal workhorse | Nova 2 Lite | `amazon.nova-2-lite-v1:0` | **Usable now** |
| Real-time voice | Nova 2 Sonic | `amazon.nova-2-sonic-v1:0` | **Usable now** |
| Multimodal semantic search | Amazon Nova Multimodal Embeddings | `amazon.nova-2-multimodal-embeddings-v1:0` | **Usable now** |
| Text RAG embeddings | Titan Text Embeddings V2 | `amazon.titan-embed-text-v2:0` | **Usable now** |
| Frontier Claude coding / reasoning | Claude Sonnet 5 | `anthropic.claude-sonnet-5` | **Agreement blocked** |
| Long-horizon Claude agent | Claude Fable 5 | `anthropic.claude-fable-5` | **Agreement blocked** |
| Highest-end Claude reasoning | Claude Opus 5 | `anthropic.claude-opus-5` | **Agreement blocked** |
| Frontier Codex / OpenAI model | GPT-5.6 Sol | `openai.gpt-5.6-sol` | **Agreement blocked** |
| Lower-tier GPT-5.6 option | GPT-5.6 Terra | `openai.gpt-5.6-terra` | **Agreement blocked** |
| Lower-tier GPT-5.6 option | GPT-5.6 Luna | `openai.gpt-5.6-luna` | **Agreement blocked** |
| RAG reranking | Cohere Rerank 3.5 | `cohere.rerank-v3-5:0` | **Agreement blocked** |

## Suggested immediate working stack

If you need to work **today without waiting for AWS agreement approvals**, this is the cleanest shortlist:

1. **Qwen3 Coder Next** for coding-heavy agents and repetitive software work.
2. **Devstral 2 123B** for repository-scale software engineering and refactoring.
3. **GLM 5** for high-end general reasoning, planning, and agent workflows.
4. **Kimi K2.5** for multimodal reasoning, UI/document understanding, and coding.
5. **Kimi K2 Thinking** for deeper text reasoning.
6. **MiniMax M2.5** as a scalable worker model for agent fleets.
7. **DeepSeek V3.2** for general reasoning and automation.
8. **gpt-oss-120b** for OpenAI open-weight reasoning workloads.
9. **Nova 2 Lite** for AWS-native text/image/video processing.
10. **Nova 2 Sonic** for real-time voice.
11. **Nova Multimodal Embeddings** and **Titan Text Embeddings V2** for retrieval/search infrastructure.

The highest-priority agreement unlocks remain **Claude Sonnet 5, Claude Fable 5, Claude Opus 5, GPT-5.6 Sol, GPT-5.6 Terra, GPT-5.6 Luna, Cohere Rerank 3.5, and the Stability image suite**.

## Usable-now entries by provider

- **Amazon:** 28
- **Mistral AI:** 13
- **Meta:** 7
- **Qwen:** 5
- **NVIDIA:** 4
- **OpenAI:** 4
- **Google:** 3
- **MiniMax:** 3
- **Z.AI:** 3
- **DeepSeek:** 2
- **Moonshot AI:** 2
- **Writer:** 1

## Agreement-blocked entries by provider

- **Anthropic:** 15
- **Stability AI:** 13
- **Cohere:** 8
- **OpenAI:** 3
- **TwelveLabs:** 3
- **AI21 Labs:** 2
- **Writer:** 2

# Complete model inventory

## A. Usable now

| Provider | Model | Model ID | Lifecycle | Inputs | Outputs | Inference | Status |
|---|---|---|---|---|---|---|---|
| Amazon | Amazon Nova Multimodal Embeddings | `amazon.nova-2-multimodal-embeddings-v1:0` | ACTIVE | TEXT,IMAGE,AUDIO,VIDEO | EMBEDDING | ON_DEMAND | **USABLE_NOW** |
| Amazon | Nova 2 Lite | `amazon.nova-2-lite-v1:0` | ACTIVE | TEXT,IMAGE,VIDEO | TEXT | INFERENCE_PROFILE | **USABLE_NOW** |
| Amazon | Nova 2 Lite | `amazon.nova-2-lite-v1:0:256k` | ACTIVE | TEXT,IMAGE,VIDEO | TEXT | PROVISIONED | **USABLE_NOW** |
| Amazon | Nova 2 Sonic | `amazon.nova-2-sonic-v1:0` | ACTIVE | SPEECH | SPEECH,TEXT | ON_DEMAND | **USABLE_NOW** |
| Amazon | Nova Canvas | `amazon.nova-canvas-v1:0` | LEGACY | TEXT,IMAGE | IMAGE | ON_DEMAND,PROVISIONED | **USABLE_NOW** |
| Amazon | Nova Lite | `amazon.nova-lite-v1:0:24k` | ACTIVE | TEXT,IMAGE,VIDEO | TEXT | PROVISIONED | **USABLE_NOW** |
| Amazon | Nova Lite | `amazon.nova-lite-v1:0:300k` | ACTIVE | TEXT,IMAGE,VIDEO | TEXT | PROVISIONED | **USABLE_NOW** |
| Amazon | Nova Lite | `amazon.nova-lite-v1:0` | ACTIVE | TEXT,IMAGE,VIDEO | TEXT | ON_DEMAND,INFERENCE_PROFILE | **USABLE_NOW** |
| Amazon | Nova Micro | `amazon.nova-micro-v1:0:24k` | ACTIVE | TEXT | TEXT | PROVISIONED | **USABLE_NOW** |
| Amazon | Nova Micro | `amazon.nova-micro-v1:0:128k` | ACTIVE | TEXT | TEXT | PROVISIONED | **USABLE_NOW** |
| Amazon | Nova Micro | `amazon.nova-micro-v1:0` | ACTIVE | TEXT | TEXT | ON_DEMAND,INFERENCE_PROFILE | **USABLE_NOW** |
| Amazon | Nova Premier | `amazon.nova-premier-v1:0:8k` | LEGACY | TEXT,IMAGE,VIDEO | TEXT | Not reported | **USABLE_NOW** |
| Amazon | Nova Premier | `amazon.nova-premier-v1:0:20k` | LEGACY | TEXT,IMAGE,VIDEO | TEXT | Not reported | **USABLE_NOW** |
| Amazon | Nova Premier | `amazon.nova-premier-v1:0:1000k` | LEGACY | TEXT,IMAGE,VIDEO | TEXT | Not reported | **USABLE_NOW** |
| Amazon | Nova Premier | `amazon.nova-premier-v1:0:mm` | LEGACY | TEXT,IMAGE,VIDEO | TEXT | Not reported | **USABLE_NOW** |
| Amazon | Nova Premier | `amazon.nova-premier-v1:0` | LEGACY | TEXT,IMAGE,VIDEO | TEXT | INFERENCE_PROFILE | **USABLE_NOW** |
| Amazon | Nova Pro | `amazon.nova-pro-v1:0` | ACTIVE | TEXT,IMAGE,VIDEO | TEXT | ON_DEMAND,INFERENCE_PROFILE | **USABLE_NOW** |
| Amazon | Nova Pro | `amazon.nova-pro-v1:0:24k` | ACTIVE | TEXT,IMAGE,VIDEO | TEXT | PROVISIONED | **USABLE_NOW** |
| Amazon | Nova Pro | `amazon.nova-pro-v1:0:300k` | ACTIVE | TEXT,IMAGE,VIDEO | TEXT | PROVISIONED | **USABLE_NOW** |
| Amazon | Nova Reel | `amazon.nova-reel-v1:0` | LEGACY | TEXT,IMAGE | VIDEO | ON_DEMAND | **USABLE_NOW** |
| Amazon | Nova Reel | `amazon.nova-reel-v1:1` | LEGACY | TEXT,IMAGE | VIDEO | ON_DEMAND | **USABLE_NOW** |
| Amazon | Nova Sonic | `amazon.nova-sonic-v1:0` | LEGACY | SPEECH | SPEECH,TEXT | ON_DEMAND | **USABLE_NOW** |
| Amazon | Titan Embeddings G1 - Text | `amazon.titan-embed-text-v1:2:8k` | ACTIVE | TEXT | EMBEDDING | PROVISIONED | **USABLE_NOW** |
| Amazon | Titan Embeddings G1 - Text | `amazon.titan-embed-text-v1` | ACTIVE | TEXT | EMBEDDING | ON_DEMAND | **USABLE_NOW** |
| Amazon | Titan Multimodal Embeddings G1 | `amazon.titan-embed-image-v1:0` | ACTIVE | TEXT,IMAGE | EMBEDDING | PROVISIONED | **USABLE_NOW** |
| Amazon | Titan Multimodal Embeddings G1 | `amazon.titan-embed-image-v1` | ACTIVE | TEXT,IMAGE | EMBEDDING | ON_DEMAND | **USABLE_NOW** |
| Amazon | Titan Text Embeddings V2 | `amazon.titan-embed-text-v2:0:8k` | ACTIVE | TEXT | EMBEDDING | Not reported | **USABLE_NOW** |
| Amazon | Titan Text Embeddings V2 | `amazon.titan-embed-text-v2:0` | ACTIVE | TEXT | EMBEDDING | ON_DEMAND | **USABLE_NOW** |
| DeepSeek | DeepSeek V3.2 | `deepseek.v3.2` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| DeepSeek | DeepSeek-R1 | `deepseek.r1-v1:0` | ACTIVE | TEXT | TEXT | INFERENCE_PROFILE | **USABLE_NOW** |
| Google | Gemma 3 12B IT | `google.gemma-3-12b-it` | ACTIVE | TEXT,IMAGE | TEXT | ON_DEMAND | **USABLE_NOW** |
| Google | Gemma 3 27B PT | `google.gemma-3-27b-it` | ACTIVE | TEXT,IMAGE | TEXT | ON_DEMAND | **USABLE_NOW** |
| Google | Gemma 3 4B IT | `google.gemma-3-4b-it` | ACTIVE | TEXT,IMAGE | TEXT | ON_DEMAND | **USABLE_NOW** |
| Meta | Llama 3 70B Instruct | `meta.llama3-70b-instruct-v1:0` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Meta | Llama 3 8B Instruct | `meta.llama3-8b-instruct-v1:0` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Meta | Llama 3.1 70B Instruct | `meta.llama3-1-70b-instruct-v1:0` | ACTIVE | TEXT | TEXT | INFERENCE_PROFILE | **USABLE_NOW** |
| Meta | Llama 3.1 8B Instruct | `meta.llama3-1-8b-instruct-v1:0` | ACTIVE | TEXT | TEXT | INFERENCE_PROFILE | **USABLE_NOW** |
| Meta | Llama 3.3 70B Instruct | `meta.llama3-3-70b-instruct-v1:0` | ACTIVE | TEXT | TEXT | INFERENCE_PROFILE | **USABLE_NOW** |
| Meta | Llama 4 Maverick 17B Instruct | `meta.llama4-maverick-17b-instruct-v1:0` | ACTIVE | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **USABLE_NOW** |
| Meta | Llama 4 Scout 17B Instruct | `meta.llama4-scout-17b-instruct-v1:0` | ACTIVE | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **USABLE_NOW** |
| MiniMax | MiniMax M2 | `minimax.minimax-m2` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| MiniMax | MiniMax M2.1 | `minimax.minimax-m2.1` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| MiniMax | MiniMax M2.5 | `minimax.minimax-m2.5` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Mistral AI | Devstral 2 123B | `mistral.devstral-2-123b` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Mistral AI | Magistral Small 2509 | `mistral.magistral-small-2509` | ACTIVE | TEXT,IMAGE | TEXT | ON_DEMAND | **USABLE_NOW** |
| Mistral AI | Ministral 14B 3.0 | `mistral.ministral-3-14b-instruct` | ACTIVE | TEXT,IMAGE | TEXT | ON_DEMAND | **USABLE_NOW** |
| Mistral AI | Ministral 3 8B | `mistral.ministral-3-8b-instruct` | ACTIVE | TEXT,IMAGE | TEXT | ON_DEMAND | **USABLE_NOW** |
| Mistral AI | Ministral 3B | `mistral.ministral-3-3b-instruct` | ACTIVE | TEXT,IMAGE | TEXT | ON_DEMAND | **USABLE_NOW** |
| Mistral AI | Mistral 7B Instruct | `mistral.mistral-7b-instruct-v0:2` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Mistral AI | Mistral Large (24.02) | `mistral.mistral-large-2402-v1:0` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Mistral AI | Mistral Large 3 | `mistral.mistral-large-3-675b-instruct` | ACTIVE | TEXT,IMAGE | TEXT | ON_DEMAND | **USABLE_NOW** |
| Mistral AI | Mistral Small (24.02) | `mistral.mistral-small-2402-v1:0` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Mistral AI | Mixtral 8x7B Instruct | `mistral.mixtral-8x7b-instruct-v0:1` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Mistral AI | Pixtral Large (25.02) | `mistral.pixtral-large-2502-v1:0` | ACTIVE | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **USABLE_NOW** |
| Mistral AI | Voxtral Mini 3B 2507 | `mistral.voxtral-mini-3b-2507` | ACTIVE | SPEECH,TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Mistral AI | Voxtral Small 24B 2507 | `mistral.voxtral-small-24b-2507` | ACTIVE | SPEECH,TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Moonshot AI | Kimi K2 Thinking | `moonshot.kimi-k2-thinking` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Moonshot AI | Kimi K2.5 | `moonshotai.kimi-k2.5` | ACTIVE | TEXT,IMAGE | TEXT | ON_DEMAND | **USABLE_NOW** |
| NVIDIA | NVIDIA Nemotron 3 Super 120B A12B | `nvidia.nemotron-super-3-120b` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| NVIDIA | NVIDIA Nemotron Nano 12B v2 VL BF16 | `nvidia.nemotron-nano-12b-v2` | ACTIVE | TEXT,IMAGE | TEXT | ON_DEMAND | **USABLE_NOW** |
| NVIDIA | NVIDIA Nemotron Nano 9B v2 | `nvidia.nemotron-nano-9b-v2` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| NVIDIA | Nemotron Nano 3 30B | `nvidia.nemotron-nano-3-30b` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| OpenAI | GPT OSS Safeguard 120B | `openai.gpt-oss-safeguard-120b` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| OpenAI | GPT OSS Safeguard 20B | `openai.gpt-oss-safeguard-20b` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| OpenAI | gpt-oss-120b | `openai.gpt-oss-120b-1:0` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| OpenAI | gpt-oss-20b | `openai.gpt-oss-20b-1:0` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Qwen | Qwen3 32B (dense) | `qwen.qwen3-32b-v1:0` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Qwen | Qwen3 Coder Next | `qwen.qwen3-coder-next` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Qwen | Qwen3 Next 80B A3B | `qwen.qwen3-next-80b-a3b` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Qwen | Qwen3 VL 235B A22B | `qwen.qwen3-vl-235b-a22b` | ACTIVE | TEXT,IMAGE | TEXT | ON_DEMAND | **USABLE_NOW** |
| Qwen | Qwen3-Coder-30B-A3B-Instruct | `qwen.qwen3-coder-30b-a3b-v1:0` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Writer | Writer Palmyra Vision 7B | `writer.palmyra-vision-7b` | ACTIVE | TEXT,IMAGE | TEXT | ON_DEMAND | **USABLE_NOW** |
| Z.AI | GLM 4.7 | `zai.glm-4.7` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Z.AI | GLM 4.7 Flash | `zai.glm-4.7-flash` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |
| Z.AI | GLM 5 | `zai.glm-5` | ACTIVE | TEXT | TEXT | ON_DEMAND | **USABLE_NOW** |

## B. Agreement blocked

| Provider | Model | Model ID | Lifecycle | Inputs | Outputs | Inference | Status |
|---|---|---|---|---|---|---|---|
| AI21 Labs | Jamba 1.5 Large | `ai21.jamba-1-5-large-v1:0` | LEGACY | TEXT | TEXT | ON_DEMAND | **AGREEMENT_BLOCKED** |
| AI21 Labs | Jamba 1.5 Mini | `ai21.jamba-1-5-mini-v1:0` | LEGACY | TEXT | TEXT | ON_DEMAND | **AGREEMENT_BLOCKED** |
| Anthropic | Claude 3 Haiku | `anthropic.claude-3-haiku-20240307-v1:0:48k` | LEGACY | TEXT,IMAGE | TEXT | PROVISIONED | **AGREEMENT_BLOCKED** |
| Anthropic | Claude 3 Haiku | `anthropic.claude-3-haiku-20240307-v1:0:200k` | LEGACY | TEXT,IMAGE | TEXT | PROVISIONED | **AGREEMENT_BLOCKED** |
| Anthropic | Claude 3 Haiku | `anthropic.claude-3-haiku-20240307-v1:0` | LEGACY | TEXT,IMAGE | TEXT | ON_DEMAND | **AGREEMENT_BLOCKED** |
| Anthropic | Claude Fable 5 | `anthropic.claude-fable-5` | ACTIVE | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Anthropic | Claude Haiku 4.5 | `anthropic.claude-haiku-4-5-20251001-v1:0` | ACTIVE | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Anthropic | Claude Opus 4.1 | `anthropic.claude-opus-4-1-20250805-v1:0` | LEGACY | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Anthropic | Claude Opus 4.5 | `anthropic.claude-opus-4-5-20251101-v1:0` | ACTIVE | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Anthropic | Claude Opus 4.6 | `anthropic.claude-opus-4-6-v1` | ACTIVE | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Anthropic | Claude Opus 4.7 | `anthropic.claude-opus-4-7` | ACTIVE | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Anthropic | Claude Opus 4.8 | `anthropic.claude-opus-4-8` | ACTIVE | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Anthropic | Claude Opus 5 | `anthropic.claude-opus-5` | ACTIVE | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Anthropic | Claude Sonnet 4 | `anthropic.claude-sonnet-4-20250514-v1:0` | LEGACY | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Anthropic | Claude Sonnet 4.5 | `anthropic.claude-sonnet-4-5-20250929-v1:0` | ACTIVE | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Anthropic | Claude Sonnet 4.6 | `anthropic.claude-sonnet-4-6` | ACTIVE | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Anthropic | Claude Sonnet 5 | `anthropic.claude-sonnet-5` | ACTIVE | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Cohere | Command R | `cohere.command-r-v1:0` | LEGACY | TEXT | TEXT | ON_DEMAND | **AGREEMENT_BLOCKED** |
| Cohere | Command R+ | `cohere.command-r-plus-v1:0` | LEGACY | TEXT | TEXT | ON_DEMAND | **AGREEMENT_BLOCKED** |
| Cohere | Embed English | `cohere.embed-english-v3:0:512` | ACTIVE | TEXT | EMBEDDING | PROVISIONED | **AGREEMENT_BLOCKED** |
| Cohere | Embed English | `cohere.embed-english-v3` | ACTIVE | TEXT | EMBEDDING | ON_DEMAND | **AGREEMENT_BLOCKED** |
| Cohere | Embed Multilingual | `cohere.embed-multilingual-v3:0:512` | ACTIVE | TEXT | EMBEDDING | PROVISIONED | **AGREEMENT_BLOCKED** |
| Cohere | Embed Multilingual | `cohere.embed-multilingual-v3` | ACTIVE | TEXT | EMBEDDING | ON_DEMAND | **AGREEMENT_BLOCKED** |
| Cohere | Embed v4 | `cohere.embed-v4:0` | ACTIVE | TEXT,IMAGE | EMBEDDING | ON_DEMAND,INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Cohere | Rerank 3.5 | `cohere.rerank-v3-5:0` | ACTIVE | TEXT | TEXT | ON_DEMAND | **AGREEMENT_BLOCKED** |
| OpenAI | GPT-5.6 Luna | `openai.gpt-5.6-luna` | ACTIVE | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| OpenAI | GPT-5.6 Sol | `openai.gpt-5.6-sol` | ACTIVE | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| OpenAI | GPT-5.6 Terra | `openai.gpt-5.6-terra` | ACTIVE | TEXT,IMAGE | TEXT | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Stability AI | Stable Image Conservative Upscale | `stability.stable-conservative-upscale-v1:0` | ACTIVE | TEXT,IMAGE | IMAGE | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Stability AI | Stable Image Control Sketch | `stability.stable-image-control-sketch-v1:0` | ACTIVE | TEXT,IMAGE | IMAGE | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Stability AI | Stable Image Control Structure | `stability.stable-image-control-structure-v1:0` | ACTIVE | TEXT,IMAGE | IMAGE | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Stability AI | Stable Image Creative Upscale | `stability.stable-creative-upscale-v1:0` | ACTIVE | TEXT,IMAGE | IMAGE | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Stability AI | Stable Image Erase Object | `stability.stable-image-erase-object-v1:0` | ACTIVE | TEXT,IMAGE | IMAGE | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Stability AI | Stable Image Fast Upscale | `stability.stable-fast-upscale-v1:0` | ACTIVE | TEXT,IMAGE | IMAGE | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Stability AI | Stable Image Inpaint | `stability.stable-image-inpaint-v1:0` | ACTIVE | TEXT,IMAGE | IMAGE | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Stability AI | Stable Image Outpaint | `stability.stable-outpaint-v1:0` | ACTIVE | TEXT,IMAGE | IMAGE | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Stability AI | Stable Image Remove Background | `stability.stable-image-remove-background-v1:0` | ACTIVE | TEXT,IMAGE | IMAGE | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Stability AI | Stable Image Search and Recolor | `stability.stable-image-search-recolor-v1:0` | ACTIVE | TEXT,IMAGE | IMAGE | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Stability AI | Stable Image Search and Replace | `stability.stable-image-search-replace-v1:0` | ACTIVE | TEXT,IMAGE | IMAGE | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Stability AI | Stable Image Style Guide | `stability.stable-image-style-guide-v1:0` | ACTIVE | TEXT,IMAGE | IMAGE | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Stability AI | Stable Image Style Transfer | `stability.stable-style-transfer-v1:0` | ACTIVE | TEXT,IMAGE | IMAGE | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| TwelveLabs | Marengo Embed 3.0 | `twelvelabs.marengo-embed-3-0-v1:0` | ACTIVE | TEXT,IMAGE,SPEECH,VIDEO | EMBEDDING | INFERENCE_PROFILE,ON_DEMAND | **AGREEMENT_BLOCKED** |
| TwelveLabs | Marengo Embed v2.7 | `twelvelabs.marengo-embed-2-7-v1:0` | LEGACY | TEXT,IMAGE,SPEECH,VIDEO | EMBEDDING | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| TwelveLabs | Pegasus v1.2 | `twelvelabs.pegasus-1-2-v1:0` | ACTIVE | TEXT,VIDEO | TEXT | INFERENCE_PROFILE,ON_DEMAND | **AGREEMENT_BLOCKED** |
| Writer | Palmyra X4 | `writer.palmyra-x4-v1:0` | ACTIVE | TEXT | TEXT | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |
| Writer | Palmyra X5 | `writer.palmyra-x5-v1:0` | ACTIVE | TEXT | TEXT | INFERENCE_PROFILE | **AGREEMENT_BLOCKED** |

## C. Wrong region

| Provider | Model | Model ID | Lifecycle | Inputs | Outputs | Inference | Status |
|---|---|---|---|---|---|---|---|
| Amazon | Titan Text Embeddings v2 | `amazon.titan-embed-g1-text-02` | ACTIVE | TEXT | EMBEDDING | ON_DEMAND | **WRONG_REGION** |

# Provider-level view

| Provider | Usable now | Agreement blocked | Wrong region | Total entries |
|---|---:|---:|---:|---:|
| AI21 Labs | 0 | 2 | 0 | 2 |
| Amazon | 28 | 0 | 1 | 29 |
| Anthropic | 0 | 15 | 0 | 15 |
| Cohere | 0 | 8 | 0 | 8 |
| DeepSeek | 2 | 0 | 0 | 2 |
| Google | 3 | 0 | 0 | 3 |
| Meta | 7 | 0 | 0 | 7 |
| MiniMax | 3 | 0 | 0 | 3 |
| Mistral AI | 13 | 0 | 0 | 13 |
| Moonshot AI | 2 | 0 | 0 | 2 |
| NVIDIA | 4 | 0 | 0 | 4 |
| OpenAI | 4 | 3 | 0 | 7 |
| Qwen | 5 | 0 | 0 | 5 |
| Stability AI | 0 | 13 | 0 | 13 |
| TwelveLabs | 0 | 3 | 0 | 3 |
| Writer | 1 | 2 | 0 | 3 |
| Z.AI | 3 | 0 | 0 | 3 |

# High-value blocked models to escalate

These are the blocked models with the clearest strategic relevance based on this report:

| Provider | Model | Model ID | Reported blocker |
|---|---|---|---|
| Anthropic | Claude Sonnet 5 | `anthropic.claude-sonnet-5` | Agreement `NOT_AVAILABLE` |
| Anthropic | Claude Fable 5 | `anthropic.claude-fable-5` | Agreement `NOT_AVAILABLE` |
| Anthropic | Claude Opus 5 | `anthropic.claude-opus-5` | Agreement `NOT_AVAILABLE` |
| Anthropic | Claude Opus 4.8 | `anthropic.claude-opus-4-8` | Agreement `NOT_AVAILABLE` |
| OpenAI | GPT-5.6 Sol | `openai.gpt-5.6-sol` | Agreement `NOT_AVAILABLE` |
| OpenAI | GPT-5.6 Terra | `openai.gpt-5.6-terra` | Agreement `NOT_AVAILABLE` |
| OpenAI | GPT-5.6 Luna | `openai.gpt-5.6-luna` | Agreement `NOT_AVAILABLE` |
| Cohere | Rerank 3.5 | `cohere.rerank-v3-5:0` | Agreement `NOT_AVAILABLE` |
| Cohere | Embed v4 | `cohere.embed-v4:0` | Agreement `NOT_AVAILABLE` |
| TwelveLabs | Marengo Embed 3.0 | `twelvelabs.marengo-embed-3-0-v1:0` | Agreement `NOT_AVAILABLE` |
| TwelveLabs | Pegasus v1.2 | `twelvelabs.pegasus-1-2-v1:0` | Agreement `NOT_AVAILABLE` |

The Stability AI image-editing family is also agreement-blocked across the entries returned in this report.

# Notes and caveats

- Multiple rows can represent the **same model family with different inference/configuration variants**. For example, Nova models appear with on-demand, inference-profile, or provisioned variants. The total `122` is therefore a count of model entries/IDs, not 122 unique model families.
- `USABLE_NOW` is the classification produced by the supplied availability-check script. It is a strong access signal, but a specific client such as Codex, Claude Code, Cursor, or a custom SDK may support only certain model IDs or Bedrock APIs.
- `LEGACY` models are included because AWS returned them in the report, but they should generally not be the first choice for new builds unless compatibility or a specific feature requires them.
- A blank inference field in the original CLI output is rendered here as **Not reported**.
- The single wrong-region entry is `amazon.titan-embed-g1-text-02`; the report says its agreement is available but `us-east-1` is not.

# Recommended next action

1. Start productive work immediately with the usable-now stack.
2. Send AWS the exact agreement-blocked evidence for the frontier models you need.
3. Re-run the availability report after AWS changes the account agreement state.
4. Version this file after every access change so you maintain a clean record of what your AWS credits can actually reach.
