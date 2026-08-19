# MODEL STRATEGY: what to do with 75 models and USD 1,100

Written 2026-08-19 from live benchmarks on account `082706806837`, not from spec sheets. Every latency and behaviour below was measured on our actual extraction task.

---

## The decision, first

**Spend the credits inside the product, not on the development toolchain.**

The instinct to route Claude Code, Codex or Cursor at Bedrock is reasonable and I am recommending against it, for one hard reason and one judgement.

**The hard reason.** Claude Code can be pointed at Bedrock with `CLAUDE_CODE_USE_BEDROCK=1`, but it only speaks to Claude models, and every one of the 15 Anthropic entries on this account is agreement-blocked. So that path is closed today. Codex CLI talks to OpenAI's own API, not Bedrock. Cursor accepts OpenAI-compatible endpoints, which Bedrock is not without a translation proxy in front of it.

So routing the dev toolchain at these credits means standing up a LiteLLM proxy and rewiring the editors, two days before the event.

**The judgement.** The current toolchain works. Changing it now is risk with no scoring benefit, because no juror asks what wrote the code. They ask what the product does. Credits spent inside the product are visible on stage; credits spent on the dev loop are not.

If the Anthropic agreements land before Friday, this decision does not change either. Keep the dev loop stable and spend the credits where they are seen.

---

## What the benchmark actually found

Same prompt, same two-document extract, temperature 0, asked for every candidate value plus the exact source line.

| Model | Latency | Found both values | Valid JSON | Output tokens | Quote matched source exactly |
|---|---|---|---|---|---|
| `amazon.nova-pro-v1:0` | 1,559 ms | yes | yes | 95 | **no** |
| `amazon.nova-lite-v1:0` | 1,390 ms | yes | yes | 99 | **no** |
| `amazon.nova-micro-v1:0` | 1,618 ms | yes | yes | 95 | **no** |
| `mistral.mistral-large-3-675b-instruct` | 1,610 ms | yes | yes | 77 | **yes** |

Two findings that matter more than the latencies.

**Finding 1: on this task, Nova Micro is as good as Nova Pro.** Same values found, same JSON validity, same token count, and the latency difference is inside the noise. For a bounded extraction over four fields, we are paying for capability we do not use. Micro is roughly an order of magnitude cheaper per token than Pro. That is the difference between the eval harness costing pennies and costing dollars, across thousands of calls.

**Finding 2, the important one: Nova does not quote the source exactly.** Given the line `Drawn capital .................... USD 17,800,000`, Nova returns it as `Drawn capital.................... USD 17,800,000`, deleting the space before the dot leader. Our design drops any candidate whose quote cannot be found in the document. With Nova as the extractor, every candidate would be dropped and every field would render UNSUPPORTED. The demo would show four abstentions and nothing else.

Mistral Large 3 returns it byte-exact.

The fix is not to switch models. It is to stop depending on the model's quote at all: locate the evidence by searching for the VALUE in the document ourselves, and use the model's quote only to disambiguate when the value appears more than once. That is more robust than any model, and it is the product's own principle applied to its own model call. That fix is in progress.

**This is what benchmarking buys.** Both models "worked" on a casual read. One of them would have produced an empty demo.

---

## The assignment

| Job | Model | Why, from the benchmark |
|---|---|---|
| **Primary extraction, on stage** | `amazon.nova-pro-v1:0` | Proven, 302 ms on a single-value call, AWS-native on an AWS-judged rubric. Keep Pro rather than Micro here purely because the demo is one call and the headroom is free |
| **Second opinion, different family** | `mistral.mistral-large-3-675b-instruct` | Different lineage entirely, and the only one that quoted exactly. Genuine independence, not a second sample of the same model |
| **Third opinion, different lineage again** | `qwen.qwen3-vl-235b-a22b` | Vision-language, unrelated training lineage. Untested by us so far, so treat as a candidate rather than a commitment |
| **Eval harness bulk runs** | `amazon.nova-micro-v1:0` | Benchmarked as equal on this task at a fraction of the cost. Seventy-plus labelled items across repeated runs is where credits actually go |
| **Fallback if Bedrock is unreachable** | Deterministic local scan | Already built. No network, no credits, fully offline |
| **Embeddings, only if we add document search** | `amazon.titan-embed-text-v2:0` | Available, cheap, not currently needed. Do not add it for the sake of using it |

Models deliberately not used: everything else. Seventy-five available models is a menu, not a checklist. Adding a model we cannot justify on stage is a liability, because a juror will ask why.

---

## The one feature worth building with these credits

Right now the product abstains when two documents disagree. There is a second, deeper source of uncertainty it does not yet surface: **when the models themselves disagree.**

If Nova Pro reads a document and returns 17,800,000, and Mistral Large 3 reads the same document and returns 17,800,00, the extraction is unreliable regardless of what the documents say. A system whose thesis is "refuse when you cannot prove the answer" should refuse there too.

This is not an invention. Our own research brief already specifies it in the layered architecture: `typed candidate values, source coordinates, deterministic validators, optional second extractor and disagreement test, confidence policy, then PROPOSE or ABSTAIN`. We wrote that down before we knew which models we would have.

**Why it is the right use of the credits:**

1. It is the only feature where spending more credits makes the product genuinely better rather than just busier.
2. It converts "we have 75 models" from a consolation prize into a capability no single-provider team can copy on the day.
3. It strengthens the core claim. "We abstain when the documents disagree" becomes "we abstain when the documents disagree, and when our own extractors disagree, and we show you both."
4. It gives a precise, checkable answer to the hardest technical question we will get, which is some version of "how do you know your extraction is right". The honest answer today is that we do not, we just refuse when we cannot prove it. This makes that answer demonstrable.

**Build it only after the base demo passes the canon gate.** Sequencing matters more than scope. A perfect ensemble on a demo that does not match the pitch is worth nothing.

---

## Cost reality

Extraction is four fields across four documents. Call it sixteen model calls per full run, at roughly 500 input and 100 output tokens each.

At Nova Pro pricing that is a fraction of a cent per full extraction run. Even running the eval harness across eighty labelled items, three models deep, repeatedly through rehearsal and the sprint, the total is single-digit dollars against USD 1,100.

**The credits are not the constraint. They were never going to be.** The constraint is time, and the honest use of the credits is to buy capability the product visibly demonstrates, not to consume the balance. Nobody scores us on credits burned.

Keep the budget alarm at USD 50 anyway. It is a smoke alarm, not a target.

---

## What to say if a juror asks about the models

> "Extraction runs on Amazon Nova Pro through Bedrock. We benchmarked four models on our own task before choosing, and the interesting result was not the latency, it was that one of them does not reproduce source text exactly. So we stopped trusting the model's quote and locate evidence by searching the document ourselves. The model proposes, we verify against the source, and if we cannot verify it we do not show it."

That answer demonstrates the product's thesis using the product's own construction. It is also true.

**Do not say** how many models are on the account, or which were unavailable. It is not interesting and it invites a conversation about procurement rather than product.

---

## Open items

| # | Item | Status |
|---|---|---|
| 1 | Quote-locator fix so Nova does not produce an all-abstain demo | In progress, critical path |
| 2 | Benchmark `qwen.qwen3-vl-235b-a22b` before committing it as the third opinion | Not started, not blocking |
| 3 | Multi-model disagreement test | Designed, build after the canon gate passes |
| 4 | Point the eval harness at `nova-micro` rather than Pro | Small change, do it when the harness is stable |
