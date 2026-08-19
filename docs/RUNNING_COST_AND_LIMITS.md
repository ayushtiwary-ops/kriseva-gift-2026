# WHAT IT COSTS TO RUN, AND WHY IT DOES NOT FALL OVER

Status: STABLE. Measured 2026-08-19 on our own AWS account, region us-east-1. Every number here was produced by running the thing, and the scripts that produced them are named so anybody can re-run them.

Nothing in this document is an estimate. Where a figure cannot be sourced, it says so.

---

## 1. One complete case, measured

A full governed run over the demo case: nine roles, a written plan, extraction, deterministic binding, deterministic validation, independent criticism, reconciliation, and a narrated handoff to a named human.

| | Measured |
|---|---|
| Agent actions | 40 |
| Wall-clock, three consecutive live runs | 3.3 s, 4.9 s, 7.9 s |
| Input tokens | 13,699 |
| Output tokens | about 1,000 |
| Total tokens | about 14,700 |
| Models involved | 5, across 4 different companies |

Input tokens came back identical to the token across three runs, because the prompts and documents are fixed. Only the output varies.

**We do not quote a dollar figure.** The IAM user has no pricing API access, so any price would be recalled rather than sourced. The token count is the honest number, and the cost follows from it at whatever the published rate is on the day. Every agent action now records its own token usage, so the cost of a case is computed from the receipt rather than asserted.

---

## 2. The rate limits, measured rather than looked up

`scripts/rate-probe.js` fires N calls at once at each model and steps N up until throttling starts.

| Model | Highest concurrency with zero throttling |
|---|---|
| amazon.nova-micro-v1:0 | 12, still clean |
| amazon.nova-lite-v1:0 | 12, still clean |
| amazon.nova-pro-v1:0 | 6 clean. At 8, seven of eight calls were throttled |

**The number that matters is not the published quota, it is what this account answers today.** A documentation page describes somebody else's allowance.

### The trap in that table

The probe used a twelve token prompt. The extractor sends a whole document. Nova Pro passed the probe at six concurrent and still throttled at three in the real run, because the binding constraint on that model is **tokens** per minute, not requests. A request-rate measurement flattered it.

That is why the extractor was moved off Nova Pro. It is the highest-volume role and the only one that carries a document on every call, so it was the worst possible fit for the most token-limited model.

---

## 3. What we changed so it stops falling over

Every item below was found by running the live path and reading what came back.

| Problem, measured | Change |
|---|---|
| 16 of 27 agent calls failed with "Too many requests" | A concurrency gate **per model**, set below each measured ceiling. One global gate was wrong: the limits are per model, so a shared gate throttled the constrained model and starved the ones with headroom |
| Retrying a throttled call immediately | Exponential backoff **with jitter**. Without jitter, parallel callers back off in lockstep and collide again on the next wave |
| A backed-off call held a slot for 19 seconds and starved 24 others | Total backoff capped at 4 seconds. Inside a bounded budget, a throttled call must fail fast and free its slot. Backing off politely past the deadline is a slower way to fail that takes the rest of the run down with it |
| The extractor sat on the most token-limited model | Moved to Nova Lite, which measures clean at 12 concurrent |

---

## 4. The bug underneath all of it

The speed was never the real problem.

**Five of the six model-backed roles had no real prompt.** Triage was the single sentence `Classify relevant synthetic fields for document D1.` It never stated the JSON shape it was required to return and never included the document. The others were the same. Only the extractor had a written prompt, and its example did not match its own validator, so a model that followed the instruction exactly was rejected as malformed on every attempt.

This survived because the recorded path computes each role's answer deterministically and never calls a model. **The demo worked perfectly and the live path had never functioned.** Every offline test passed.

The lesson is general, and it is now in the spec: *a prompt whose example does not match its validator fails on every live model and passes every offline test.*

---

## 5. Triage may narrow the work. It may never lose evidence.

With real prompts, triage started working, and immediately did something worse than failing.

It read the administrator statement and returned F1 and F2, silently omitting F3, although the document plainly contains `Closing NAV ....................... USD 21,940,500`. The field was never extracted, and the case reported closing NAV as having one source when it had two.

**A pruning step that can quietly drop a field is the exact failure this product exists to prevent**, and it is worse than an extraction error, because nothing downstream can detect it. There is no candidate to check and no disagreement to preserve.

So the model's answer is now a floor and never a ceiling. Plain string matching runs across the document for every field label, and anything it finds is added back whatever the model said. The model can narrow the work only where deterministic code agrees there is nothing to find.

When the floor overrules the model it says so on the run, in words:

> Deterministic check restored F3 on D1. The document names those fields and the triage model omitted them. Triage may narrow the work, never lose evidence.

On the demo case it fires twice, restoring F3 on D1 and F1 on D4. **The correction is visible, because a correction nobody can see is indistinguishable from the model having been right.**

---

## 6. Where it ended up

| | Before | After |
|---|---|---|
| Live wall-clock | 481 s, as recorded in the brief. 29 s when re-measured | 3.3 s to 7.9 s |
| Agent calls that succeeded | 2 of 27 | 41 of 42 |
| Fields resolved on the live path | none. Every field came back empty | all four, matching CANON exactly |
| Canon conformance on a live run | not reached | 24 of 24 |

The one remaining failure in a live run is the guard refusing an agent that tried to remove a preserved conflict. That is the product working. It is the single most important rule in the system, and it is now demonstrable against a live model rather than a recording.

---

## 7. Saying this to a juror

The honest version, which is also the strongest one:

> "We are outsiders. We have never seen a real quarterly return, we have no customers, and we built this from published circulars and our own reading. We ran it on a starter AWS account with ordinary on-demand limits, and the first live run failed almost completely: two of twenty seven model calls succeeded.
>
> So we measured our own limits instead of reading a documentation page, moved the heaviest role off the most constrained model, gated each model separately at its measured ceiling, and made every retry back off with jitter and fail fast rather than hold a slot. A complete nine-role case now runs in about five seconds and costs about fourteen thousand seven hundred tokens, and we record the tokens per action so the cost comes off the receipt rather than a slide.
>
> The most useful thing we found had nothing to do with speed. Our triage model quietly dropped a field that was plainly in the document. Nothing downstream could have caught it, because there is no candidate to check and no disagreement to preserve. So triage can now only ever narrow work that plain code agrees is unnecessary, and when it is overruled the run says so in words.
>
> That is what we could work out from the outside. The parts we could not work out are the ones we have marked as not built rather than guessed at: which rule requires which field, and what real documents look like when they are scanned, handwritten on, or wrong. Those need someone on the inside. That is what we are asking for."

**What not to say.** Do not claim a dollar cost, because we cannot source the price. Do not claim the live path is production ready; it runs the demo case in five seconds and has been exercised on one corpus of synthetic documents. Do not imply the rate limits we measured apply to any account but ours.
