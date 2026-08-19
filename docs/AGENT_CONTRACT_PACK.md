# AGENT CONTRACT PACK: what lives only in code, and dies on Thursday

Status: STABLE. Written 2026-08-19 by the co-founder session, from the running
rehearsal build. Every prompt below was captured by executing the prompt builder
against a real case, not by copying source, so what is printed here is exactly
what goes on the wire.

**Why this document exists.** The Thursday deletion carries five documents:
`UI_LANGUAGE_AND_VISUALS_SPEC.md`, `SCHEMA_PACK.md`, `BUILD_SPEC_v1.md`,
`RUNNING_COST_AND_LIMITS.md` and `CANON.md`. A gap audit against the running
build on 19 August found that the single most expensive discovery of the whole
rehearsal, the six agent prompts and the validator contracts they are judged
against, appears in none of them. `RUNNING_COST_AND_LIMITS.md` records that the
prompts were broken and that fixing them took the live path from 481 seconds to
five. It does not contain the prompts.

Rebuilding from the existing pack alone reproduces the bug it took a day to
find. This document closes that.

---

## 0. The one rule that generates most of the others

**A prompt whose example does not match its validator fails on every live model
and passes every offline test.**

The offline path computes each role's answer deterministically and never calls a
model, so a broken prompt is invisible to the test suite. Five of the six
model-backed roles shipped with a one-line stub that never stated the JSON shape
it had to return, and the sixth had an example missing two required keys. All
299 tests passed throughout.

The mechanical consequence for Friday: **write the validator and the prompt in
the same sitting, and paste the validator's own example into the prompt.** If
they are written apart, they drift, and nothing catches it until a live run.

---

## 1. Model routing, and why each role sits where it does

Verified live 2026-08-19 on the account recorded in `AWS_EVIDENCE.md`, region us-east-1. All fifteen
Anthropic models on this account are agreement-blocked. Do not plan around them.

| Role | Model | Fallback | Model in the loop |
|---|---|---|---|
| orchestrator | moonshot.kimi-k2-thinking | zai.glm-5 | No. The plan is deterministic in the shipped build |
| scope (triage) | none | none | **No, since 19 Aug** |
| extractor | amazon.nova-lite-v1:0 | amazon.nova-micro-v1:0 | Yes |
| binder | none | none | **No, by design** |
| validator | none | none | **No, by design** |
| critic | mistral.mistral-large-3-675b-instruct | qwen.qwen3-vl-235b-a22b | Yes |
| reconciler | zai.glm-5 | deepseek.v3.2 | Yes |
| narrator | amazon.nova-lite-v1:0 | amazon.nova-micro-v1:0 | Yes |
| learner | moonshot.kimi-k2-thinking | zai.glm-5 | **No. Forced to the deterministic path** |

Five of these entries are load bearing and a rebuild that gets them wrong looks
identical until it is examined on stage.

**Scope must not use a model.** It did until 19 August, and it committed the one
failure this product exists to prevent: it read a document and returned two
fields, silently dropping a third that was plainly on the page. The guard against
that was a deterministic floor of plain string matching, added underneath it. The
floor then overruled the model every time they disagreed, which means the model
could only ever lose evidence and never save work the floor was not already
saving. So the floor became the whole step. **Rebuild it as string matching over
the field labels and do not put a model back.**

**The extractor must not sit on Nova Pro.** It is the highest-volume role and the
only one that carries a whole document on every call. Nova Pro measured clean at
six concurrent on a twelve-token probe and still throttled at three in the real
run, because its binding constraint is tokens per minute, not requests. A
throttled extractor returns nothing, which is worse than a weaker model
returning something: the deterministic binder checks every quote against the
document and drops what it cannot find, so the architecture already catches a
poor reader. It cannot catch silence.

**The critic must not share a model family with the extractor.** The old fallback
pointed the critic at the same model the extractor used, so any run that fell
back had the proposer and its own critic being the same model, quietly voiding
the independence the product claims on stage. Enforce it in code, not in review:

```text
assertCriticIndependence(config):
    extractorFamily = modelFamily(config.extractor.modelId)
    criticFamily    = modelFamily(config.critic.modelId)
    if either is missing, or the two are equal:
        throw "The critic and extractor must use independent model
               families before the governed runtime starts."
```

`modelFamily` is the first two dot-separated segments with any dash suffix
stripped, so `amazon.nova-lite-v1:0` and `amazon.nova-micro-v1:0` are the same
family and cannot critique each other. The route selector retries with the
fallback and throws if no independent critic exists. It runs before the governed
runtime starts, so an independence breach is a startup failure, never a quiet
one.

**The binder and the validator contain no model at all.** That is the sentence
that survives the pitch: a model cannot verify a model. The binder locates every
quote in the source text by exact match and computes the character offsets
itself, ignoring any offsets the model claimed. The validator checks arithmetic
identities. Both are ordinary code.

**The learner is deterministic on purpose.** It passes `forceRecorded: true`, so
its one-line prompt is never sent anywhere. Do not "fix" it into a model call.
The lesson ledger is an accountability record, and a model-written lesson is a
model marking its own homework.

---

## 2. The five live prompts, captured from the running build

Captured by executing each prompt builder against `CASE-2026-Q1-MER001`, so the
document text inside them is the real synthetic corpus text a model receives.
The figures in it are the CANON section 5 values. `USD 24,700,000` is undrawn
commitment, which is committed capital minus drawn capital on that document, and
it is the identity the deterministic validator checks.

### Scope: no prompt, because there is no model

Scope was a model call until 19 August. It is now this, and nothing else:

```text
scopeDocument(document, fields):
    return {
      docId:      document.docId,
      fieldCodes: [ field.fieldCode
                    for field in fields
                    if document.text.toLowerCase()
                       contains field.label.toLowerCase() ]
    }
```

That is the entire step. It replaced a model, a prompt, a validator and a
correction path, and the measured result did not move: 24 of 24 planted archetypes
still named exactly, still zero silent picks.

### Prompt: extractor

```text
You are extracting one field from a source document for a regulatory audit tool.
Field label: Committed capital
Field code: F1
Document id: D1
Expected unit: USD

Find every candidate value for this field stated in the document text below.
For each candidate, report the value and the EXACT substring from the document
that states it, copied character for character (same spacing, punctuation and
currency symbols as written). Do not paraphrase the quote. Do not report
character offsets; they will be computed independently from your quote.
A quote that cannot be found in the document is discarded, so copy it exactly.

value must be a plain number with no currency symbol, no commas and no spaces.
Write 17800000, never "USD 17,800,000" and never 17,800,000.

Reply with strict JSON only, no prose outside the JSON. All four keys are
required every time, including the empty dropped array:
{"fieldCode": "F1", "docId": "D1", "candidates": [{"value": 17800000, "quote": "Drawn capital ..................... USD 17,800,000"}], "dropped": []}

If the document does not state this field at all, reply with the same four
keys and an empty candidates array:
{"fieldCode": "F1", "docId": "D1", "candidates": [], "dropped": []}

Document text:
"""
Northwind Fund Services (IFSC) Private Limited
Quarterly Administrator Statement
Scheme: Meridian Alpha Opportunities Fund I
Period: Quarter ended 30 June 2026
As at: 30 June 2026 16:00 IST
Version: 2 (supersedes Version 1 issued 03 July 2026)
Issued: 08 July 2026
==================================================================
SYNTHETIC TEST DOCUMENT, NOT A REAL RECORD

Committed capital ................. USD 42,500,000
Drawn capital ..................... USD 17,800,000
Closing NAV ....................... USD 21,940,500
Undrawn commitment ................ USD 24,700,000
Management fee accrued ............ USD 212,000
Distributions to date ............. USD 0
Number of investors ............... 3

Prepared by the administrator. Figures are stated as at the time above.

"""
```

### Prompt: critic

```text
You are the independent critic. Another model read a value out of a synthetic document.
Your job is to try to knock that reading down, not to agree with it.

Field code: F1
Field label: Committed capital
Document id: D1

The readings you are objecting to:
  1. value 17800000, quoted as "Drawn capital ..................... USD 17,800,000"

Check the document text below. Raise an objection when the quoted words are not actually there,
when the number does not match the words, when the line is about a different field, or when the
figure belongs to a different period. Raise nothing if the reading is sound. An empty objections
array is a valid and common answer, and inventing an objection is worse than raising none.

Return exactly this JSON object and nothing else, with no other keys:
  {"fieldCode": "F1", "docId": "D1",
   "objections": [], "criticismStatus": "CRITICISED"}

criticismStatus is always the exact string "CRITICISED". It records that criticism ran,
not that you found something. Send it even when objections is empty.

Each objection, if you raise any, is an object with exactly the keys fieldCode, docId, objection, reading.

--- BEGIN DOCUMENT ---
Northwind Fund Services (IFSC) Private Limited
Quarterly Administrator Statement
Scheme: Meridian Alpha Opportunities Fund I
Period: Quarter ended 30 June 2026
As at: 30 June 2026 16:00 IST
Version: 2 (supersedes Version 1 issued 03 July 2026)
Issued: 08 July 2026
==================================================================
SYNTHETIC TEST DOCUMENT, NOT A REAL RECORD

Committed capital ................. USD 42,500,000
Drawn capital ..................... USD 17,800,000
Closing NAV ....................... USD 21,940,500
Undrawn commitment ................ USD 24,700,000
Management fee accrued ............ USD 212,000
Distributions to date ............. USD 0
Number of investors ............... 3

Prepared by the administrator. Figures are stated as at the time above.

--- END DOCUMENT ---
```

### Prompt: reconciler

```text
You are reconciling one field of a synthetic regulatory return.

Field code: F1
Field label: Committed capital

The candidate readings found in the source documents:
  1. value 17800000 from document D1, true as at 2026-03-31T17:42:00+05:30, quoted as "Drawn capital ..................... USD 17,800,000"

THE RULE THAT OVERRIDES EVERYTHING ELSE. You may not choose between these values.
You do not resolve the disagreement. You describe it, and a named human decides later.
selectedValue must always be null. There is no exception.

Choose a state:
  "SUPPORTED"   exactly one distinct value was found.
  "CONFLICTED"  two or more distinct values were found.
  "UNSUPPORTED" no candidate was found at all.

If CONFLICTED, give a conflict object with a cause and a one sentence plain English explanation.
Cause is one of: TIMING, CORRECTION, VERSION, ARITHMETIC, UNIT_MISMATCH, DUPLICATE, OUT_OF_PERIOD, MODEL_DISAGREEMENT.
Use MODEL_DISAGREEMENT when two models read the same document differently. That takes priority.
If not CONFLICTED, set conflict to null and give a one sentence explanation string instead.

Return exactly this JSON object and nothing else, with no other keys:
  {"fieldCode": "F1", "state": "CONFLICTED", "selectedValue": null,
   "conflict": {"cause": "TIMING", "explanation": "..."}, "explanation": "..."}
```

### Prompt: narrator

```text
You are writing a two sentence summary of a synthetic regulatory case for a named human reviewer.

Entity: Meridian Alpha Capital IFSC Private Limited
Reportable fields on this case: 4

Hard rules, and a summary breaking any of them is discarded:
  Use the word "synthetic" explicitly. The data is fictional and the summary must say so.
  Never imply the return has been filed, approved, resolved, or acted on autonomously.
  Never use the words file, filed, files, filing, approved, approval, autonomous, resolved, or resolution.
  The software prepares and escalates. A named human decides. Say it that way.

Return exactly this JSON object and nothing else:
  {"summary": "...", "synthetic": true, "nextAction": "..."}

summary describes the state of the synthetic case. nextAction says what the named human does next.
No other keys are permitted.
```

---

## 3. The validator contracts, which are the real rules

The prompt asks. The validator decides. A role whose output fails its validator
is retried and then escalated, so these are the actual product rules and the
prompts above are only their polite form. Rebuild the validators first.

### Critic

Allowed keys, and nothing else: `fieldCode`, `docId`, `objections`,
`criticismStatus`. Each objection allows only `fieldCode`, `docId`, `objection`,
`reading`. `criticismStatus` must be the exact string `CRITICISED`, always, even
when the objections array is empty, because it records that criticism ran rather
than that something was found.

The critic is then swept for any key in
`{value, chosenDocId, decidedBy, attestedBy, signedBy, decision, attestation,
signoff, selectedValue, human, humanDecision}`, any `state` in
`{DECIDED, ATTESTED, CONFIRMED, CONFIRMED_UNSOURCED, SIGNED, SEALED}`, and any
`resolved: true`, recursively at every depth. A critic that resolves anything is
rejected. **The critic may attack a reading. It may never settle one.**

### Reconciler, the most constrained role in the system

Allowed keys: `fieldCode`, `state`, `selectedValue`, `conflict`, `explanation`.
`selectedValue` must be `null`. There is no exception and no override.
`state` must be one of `SUPPORTED`, `UNSUPPORTED`, `CONFLICTED`.

Then the rule that is the whole product, and the one to write first on Friday:

> If two models returned different readings for the same field, the output must
> be `CONFLICTED` with cause `MODEL_DISAGREEMENT`, and the explanation must name
> **both** model ids and **both** readings, formatted with thousands separators.

The validator reconstructs the reading set from the candidates and the
objections itself and compares. A reconciler that quietly harmonises two models
into one answer is rejected by code that does not read its explanation. This is
the single most important guard in the build and the one a juror should be shown
failing on purpose.

### Narrator

Allowed keys: `summary`, `synthetic`, `nextAction`. `synthetic` must be `true`,
and the combined text must contain the word "synthetic".

Every string at every depth is then tested against
`/\bfile(?:d|s)?\b|\bfiling\b|\bapproved\b|\bapproval\b|\bautonomous\b|\bresolved\b|\bresolution\b/i`
and rejected on a match. The software prepares and escalates; a named human
decides. A summary that says the return was filed is discarded even if it is
otherwise perfect.

### Extractor

Requires `fieldCode`, `docId`, `candidates`, `dropped`. All four keys every
time, including the empty `dropped` array. This is the one whose original
example omitted two of its own required keys, so a model that followed the
instruction exactly was rejected on every attempt.

### Scope, which is now the floor and nothing else

Requires `{docId, fieldCodes}` where `fieldCodes` may be empty.

> **Scope may narrow the work. It may never lose evidence.**

Plain string matching runs across the document for every field label. That is the
whole rule, and it is now the whole step.

It began as a model with the string matching added underneath it as a floor, after
the model read the administrator statement and returned F1 and F2, silently
dropping F3, although the document plainly contains `Closing NAV
....................... USD 21,940,500`. A pruning step that can quietly drop a
field is worse than an extraction error, because there is no candidate to check
and no disagreement to preserve, so nothing downstream can detect it.

**Then the floor made the model redundant.** The floor overruled it every time the
two disagreed, which means the model could never narrow anything the floor did not
already agree to narrow. It could only lose evidence. It was removed on 19 August,
and the measured result did not move.

The general lesson, and it is the one to carry: **when a deterministic guard has
to overrule a model on every disagreement, the model is not adding judgement, it
is adding risk. Delete it.**

### Binder and validator, no model

The binder ignores any character offsets the model claims and locates each quote
in the source text itself, dropping any candidate whose quote is not found
character for character. The validator checks the accounting identity
(undrawn commitment equals committed capital minus drawn capital, per document)
and flags `EVIDENCE_UNBOUND` when a stored quote no longer matches its
coordinates in the source. Both are ordinary code and there is no prompt to
carry.

---

## 4. Transport constants, measured on this account

Do not copy a quota from a documentation page. It describes somebody else's
allowance. `scripts/rate-probe.js` fires N calls at once per model and steps N
up until throttling starts.

Measured 2026-08-19, us-east-1, on the account recorded in `AWS_EVIDENCE.md`:

| Model | Clean at | Gate set to | Why the gate is lower |
|---|---|---|---|
| amazon.nova-micro-v1:0 | 12 concurrent | 8 | Headroom for a busier account on the day |
| amazon.nova-lite-v1:0 | 12 concurrent | 8 | Same |
| amazon.nova-pro-v1:0 | 6 concurrent, 7 of 8 throttled at 8 | **3** | The probe used a twelve-token prompt. The real constraint is tokens per minute, not requests, so a request-rate probe flattered it |

```text
default in-flight per unmeasured model : 4
throttle retries                       : 4
throttle base                          : 300 ms, doubling, each interval
                                         plus up to half of itself as jitter
throttle total cap                     : 4000 ms across all retries, per call
```

Four rules, and each one was learned by getting it wrong first.

1. **The gate is per model, never global.** One shared gate throttles the
   constrained model and starves the ones with headroom at the same time.
2. **Backoff carries jitter.** Without it, parallel callers back off in lockstep
   and collide again on the next wave. Add up to half of each interval.
3. **Total backoff is capped, and the cap is small.** The first attempt used a
   400ms base doubled five times, so a throttled call slept through twelve
   seconds of ladder while holding one of only four slots. Three stuck calls
   starved twenty four others until the wall-clock budget killed the run. Inside
   a bounded budget a throttled call has to fail fast and free its slot.
   **Backing off politely past the deadline is a slower way to fail that takes
   the rest of the run down with it.**
4. **Both the gate and the sleep respect the AbortSignal**, or the wall-clock
   budget stops bounding anything.

### The wall-clock budget, and it does enforce

`src/orchestrator.js` sets one deadline for the whole run at
`Date.now() + plan.budget.wallClockMs`, default 30000, hard ceiling 60000. Every
step races the remaining time against an `AbortController`. A step that starts
past the deadline, or is still running at it, returns a `TIMEOUT` run and the
case escalates to a named human.

Verified by running it: a permanently hanging agent against a 30 millisecond
budget escalates in 36 milliseconds instead of hanging.

An earlier brief said this did not enforce and that was stale. **Do not volunteer
it as a weakness.** Eight of a hundred review perspectives independently marked
us down for a missing safety control we actually have.

Plan budget bounds: `maxRetriesPerStep` 0 to 2, `maxReplans` 0 to 1,
`wallClockMs` positive and at most 60000. A plan outside those bounds is
rejected before the run starts.

---

## 5. The offline path, stated exactly

The provider picks LIVE only when all four of `BEDROCK_MODEL_ID`, `AWS_REGION`,
`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` are present. Otherwise it runs
`ReplayProvider`, and the mode is printed on startup either way.

`ReplayProvider` hashes the prompt, looks for a fixture with that exact hash
**and `mode: 'LIVE'`**, and takes the last match because the fixture file is
append only. If there is no match it falls through to `deterministicScan`, which
is pure string matching over the document.

Two consequences, and both must be said out loud rather than discovered:

- **Only a genuine live recording is a usable fixture.** A previous RECORDED
  entry is the deterministic scan's own log line, not a model response, and
  replaying it parses to zero candidates in silence.
- **Changing a prompt invalidates every fixture keyed to it.** The corpus
  generator writes document prose with a model, so regenerating the corpus
  changes the document text, which changes the prompt, which changes the hash,
  which silently moves extraction from fixture replay to deterministic scan. The
  demo still works, which is exactly why nobody notices.

**Say this, and do not overstate it:** the provider interface for a local
open-weight model exists. The wiring does not. The offline path is recorded
responses plus a deterministic scan, and it is not a local model.

---

## 6. What the corpus generator owns

`scripts/generate-scenarios.js` builds 24 cases across 20 fictional entities and
10 pain archetypes. The split of responsibility is the part to preserve:

- **Deterministic code owns every number, every planted conflict and every
  content hash.** Nothing a model writes can change a figure.
- **A model writes only the surrounding prose**, so the documents read like
  documents rather than like a fixture file. Measured on the last build: 104
  calls to `amazon.nova-lite-v1:0`, none fell back.

Every case therefore carries its own ground truth, written before any model saw
it:

```json
"scenario": {
  "id": "S2",
  "name": "Silent restatement",
  "expectedField": "F3",
  "expectedCause": "CORRECTION",
  "pain": "The administrator reissued a corrected valuation after the internal ledger had already been built from the earlier version."
}
```

**Keep that block.** It is the only non-circular label set in the build, and it
is what makes the measured result in `MEASURED_RESULTS.md` an honest number
rather than the system grading its own homework.

Duplicate detection needs one thing to survive the rebuild: every document
carries a real `contentHash`, and the collapse only trusts a hash-shaped value,
so a fixture or placeholder is never mistaken for content identity. Two
candidates whose documents share a hash are collapsed to one and reported under
a **separate `duplicate` key, not as a conflict**, because three candidates
agreeing is not a disagreement. The field stays `SUPPORTED` and says why it was
counted once instead of twice.

---

## 7. The eval trap, which cost nothing to build and would have cost the pitch

`data/eval-results.json` in the rehearsal build reports coverage 11.9 percent,
abstention correctness 50 percent and field recall 0 percent, on a build that
passes 24 of 24 canon checks and 299 of 299 tests.

The product is not wrong. **The label file is.** Three separate faults:

1. 59 of 67 labels reference cases that were never built
   (a `CASE-2026-Q4-MER001` that was never generated, plus seven `CASE-EVAL-*` placeholders).
2. Four labels mark F1 on the demo case as `shouldAbstain: false` with a true
   value of 42,500,000. CANON section 4 says F1 is a **version conflict**. The
   product correctly abstains and is scored as a miss, four times.
3. Two labels mark F3 as the missing field. CANON says F3 is a correction
   conflict and **F4** is the field with no source. F3 and F4 are transposed.

The labels predate the final demo-case design and were never re-derived. Nothing
caught it because nothing checked the labels against CANON.

**The rule for Friday, and it is five lines of code:** the eval gate fails if any
label names a case absent from the corpus, or asserts a state that CANON
contradicts. Labels are derived from CANON and from `scenario.expectedCause`,
never hand-written. A repository whose own eval file says the product fails half
the time is a self-inflicted wound, and a judge who opens `data/` finds it
before we do.

---

## 8. Rebuild order for Friday

The lane order that avoids every trap above.

| # | Build | Why here |
|---|---|---|
| 1 | Field states, conflict causes, the label map with a sentence-casing fallback | Every display map must cover everything the corpus can produce. Two of the six rehearsal defects were a map falling short and printing its own key |
| 2 | The five validators in section 3 | They are the rules. Everything else serves them |
| 3 | The five prompts in section 2, **in the same sitting**, pasting each validator's own example into its prompt | Written apart, they drift, and no offline test catches it |
| 4 | Binder and validator, deterministic, no model | A model cannot verify a model, and this is the sentence the pitch rests on |
| 5 | The triage floor | Before triage is allowed to narrow anything |
| 6 | Corpus generator, deterministic numbers, model prose, `scenario` block preserved | Ground truth must exist before anything is measured |
| 7 | Per-model gate, jittered backoff, capped total, AbortSignal respected | Only needed once calls go live, and painful to retrofit |
| 8 | `assertCriticIndependence` at startup | A startup failure, never a quiet one |
| 9 | Eval labels derived from CANON, with the two consistency checks | So the repo cannot ship a number that libels the product |

**Then the sweep that is worth more than more tests.** Every entity, every
screen, asserting two things: no raw enum reaches the screen, and no screen
renders empty where it should render content. That sweep found three of the six
rehearsal defects in under a minute, and 299 passing tests found none of them,
because the tests assert on source text and engine behaviour and none of them
ever opened the product and clicked the thing a juror clicks first.
