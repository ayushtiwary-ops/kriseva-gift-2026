# MEASURED RESULTS: the numbers, how they were produced, and what they do not prove

Status: STABLE. Produced 2026-08-19 by running the rehearsal build, not by
reading it. Every table below names the command that made it. Nothing here is an
estimate, and where a number cannot be sourced this document says so instead of
supplying one.

The reason this file exists separately from the pitch: on a synthetic corpus, the
temptation to quote a flattering number is at its highest, and the honesty
criterion is 20 percent of the score by rule. A measured result that surprises us
is worth more than a predicted one that flatters us.

---

## 1. The headline, and its exact scope

**On 24 synthetic cases carrying 10 planted failure archetypes, the system named
the right field with exactly the planted cause 24 times out of 24, and chose a
value by itself zero times out of 24.**

| Measure | Result |
|---|---|
| Cases scored | 24 |
| Planted cause reported exactly | **24 of 24** |
| Silent picks, a value chosen by software | **0 of 24** |

### Why this is not the system grading its own homework

The labels are not derived from the system's output. The corpus generator writes
`scenario.expectedField` and `scenario.expectedCause` into every case at build
time, in deterministic code, **before any model sees the case**. The scorer reads
those two fields, calls the live API, and compares.

```text
for each case in the corpus:
    planted = case.scenario.expectedField, case.scenario.expectedCause
    live    = GET /api/case/<caseId>
    field   = live.fields[planted.field]
    reported = field.conflict.cause  or  field.duplicate.cause
    correct  = (reported == planted.cause)
    silent   = (field.selectedValue is not null)
```

The one subtlety worth stating on stage if asked. Two of the ten archetypes are
duplicate documents, where the same statement arrives twice under different
filenames. The system reports those under a separate `duplicate` key and leaves
the field `SUPPORTED`, which is correct: three candidates that agree are not a
disagreement. It says the copy was counted once rather than twice. A first pass
of this scorer read only the conflict key and reported 22 of 24. The product was
right and the scorer was wrong, which is worth recording because it is the same
class of mistake as the eval label file in section 5.

### The qualifiers, and they matter

- **We wrote the conflicts.** A detector scored against conflicts its own authors
  planted is a consistency check, not an accuracy claim about real documents. It
  proves the pipeline does what the design says on ten distinct shapes of
  failure. It does not predict behaviour on a real quarterly return.
- **This ran on the recorded path**, which serves extraction from recorded model
  responses where the prompt hash matches and from a deterministic scan where it
  does not. It measures the conflict logic, not a model's reading accuracy.
- **The live path was measured separately**, on the demo case only. See section 3.
- One run per case. This says nothing about run-to-run variance on live models.

### Measured again after the architecture was simplified

On 19 August the scope step's model was removed and replaced by the deterministic
string matching that was already overruling it. The same measurement was re-run on
the same corpus, before and after.

| | Before, scope used a model | After, scope is code |
|---|---|---|
| Planted cause reported exactly | 24 of 24 | **24 of 24** |
| Silent picks | 0 of 24 | **0 of 24** |
| Tests | 299 of 299 | **299 of 299** |
| Canon conformance | 24 of 24 | **24 of 24** |
| Roles using a model | 7 of 9 | **6 of 9** |

**Nothing measurable was lost, and one model and one failure mode went with it.**
That is the honest form of a simplification claim: re-run the measurement, publish
both columns, and only call it a simplification if the result column does not move.

---

## 2. The comparison against just using a good model, which did not go how we predicted

`SCENARIO_DESIGN.md` section 3 planned to prove that a frontier model with a good
prompt cannot do this. We ran it. **It does not show that**, and the pitch has
never claimed it does.

Measured 2026-08-19, 24 Bedrock calls, 36,955 tokens, 8 fields across 2 cases,
one run per field. Each baseline got the documents, the field list, and an
explicit instruction to answer `UNCERTAIN` when sources disagree. Steelmanned,
not a strawman.

| Arm | Correct abstentions | Silent picks | Answers correct | Quotes found in the source |
|---|---|---|---|---|
| amazon.nova-pro-v1:0 | 4 of 4 | 0 | 4 of 4 | **0 of 4** |
| mistral.mistral-large-3-675b-instruct | 4 of 4 | 0 | 4 of 4 | 4 of 4 |
| zai.glm-5 | 4 of 4 | 0 | 4 of 4 | 4 of 4 |
| KRISEVA ATTEST | 4 of 4 | 0 | 4 of 4 | 7 of 7 |

**Read honestly: on this small set, told to abstain, the models abstained.** Two
of the three matched us on everything except that we located more evidence, and
we located more only because we surfaced more candidates. That is not a
scoreboard win and it must not be presented as one.

### What the table actually shows

One real separation, and it is Nova Pro at 0 of 4. Its quoted evidence could not
be found in the source document character for character. A quote that cannot be
located is a claim about a document rather than a citation of one, and on a
signed regulatory return that is the difference between evidence and assertion.
Our binder drops any candidate whose quote it cannot locate, which is why that
column is the one worth pointing at.

### The honest answer when a juror asks "so why not just use the model"

Say this, and do not reach past it:

> "We ran that experiment and we will show you the table. Told to abstain, the
> models abstained, on eight fields, once each. So we are not going to claim a
> model cannot read a document, because we measured it and it can.
>
> Three things did not come out of the prompt, and they are what we sell. The
> refusal is enforced in code that cannot be talked out of it, rather than
> requested from a model that complied this time at a sample size of eight. Every
> quote is checked against the source and dropped if it is not there, which is
> the one column where a frontier model scored zero. And none of the three
> produces a named decider, a written reason, a second signature, or the same
> answer eleven months later, because that is not a text-generation problem."

**What not to say.** Do not claim the baselines failed. Do not quote the
localisation column as though 7 of 7 beats 4 of 4; the denominators differ
because we proposed more candidates. Do not present eight fields at n=1 as an
accuracy benchmark in either direction.

---

## 3. What one complete case costs and how long it takes

Measured on the live path, three consecutive runs, from `RUNNING_COST_AND_LIMITS.md`.

| | Measured |
|---|---|
| Agent actions | 40 |
| Wall clock, three consecutive live runs | 3.3 s, 4.9 s, 7.9 s |
| Input tokens | 13,699 |
| Output tokens | about 1,000 |
| Total tokens | about 14,700 |
| Models involved | 5, across 4 companies |
| Canon conformance on a live run | 24 of 24 |

Input tokens came back identical to the token across three runs, because the
prompts and documents are fixed. Only the output varies.

**No dollar figure.** The IAM user has no pricing API access, so any price would
be recalled rather than sourced. Every agent action records its own token usage,
so the cost of a case comes off the receipt at whatever the published rate is on
the day.

---

## 4. The corpus, counted rather than remembered

Counted directly from `data/` and `public/history.json` on 2026-08-19.

| | Count |
|---|---|
| Fictional entities | 20 |
| Cases | 26 |
| Source documents | **115** |
| Failure archetypes | 10 |
| Prior quarterly filings | 80 |
| Recorded disagreements across those filings | 106 |
| Unique officer notes | **187** |

Two corrections to figures carried in the handover brief: the document count is
115, not 106, and the officer-note count is 187, not 186. Both were recounted
from the files. Use these.

All of it is synthetic and labelled synthetic. No real entity, fund, customer or
person appears anywhere in it.

---

## 5. The eval file that libels the product, and what to do about it

`data/eval-results.json` in the rehearsal build reports:

> Coverage 11.9 percent. Abstention correctness 50 percent. Field recall 0 percent.

On a build that passes 299 of 299 tests and 24 of 24 canon checks. **The product
is not wrong. The label file is**, in three separate ways:

1. 59 of its 67 labels reference cases that were never generated.
2. Four labels mark F1 on the demo case as a field that should resolve to a
   single value of 42,500,000. CANON says F1 is a version conflict. The product
   correctly abstains and is scored as a miss, four times over.
3. Two labels put the missing field at F3. CANON puts the correction conflict at
   F3 and the missing field at F4. They are transposed.

The labels predate the final demo-case design and were never re-derived against
it. Re-running the eval does not fix it, because the corpus is right and the
answer key is wrong.

**Do not ship this file, and do not quote a number from it.** The rule for the
Friday rebuild is in `AGENT_CONTRACT_PACK.md` section 7: labels are derived from
CANON and from `scenario.expectedCause`, never hand-written, and the gate fails
if a label names a case absent from the corpus or asserts a state CANON
contradicts. That is five lines and it catches all three faults.

If a judge opens `data/` and finds a self-reported 50 percent, no verbal
correction recovers it.

---

## 6. Gate results as shipped

Run 2026-08-19 on the restored build, in this order, all green.

| Gate | Result |
|---|---|
| `npm test` | 299 of 299 |
| `tools/canon_check.py` | 24 of 24 |
| `tools/history_check.py` | 9 of 9, 80 filings, 106 conflicts |
| `tools/guardrail_check.py` | clean on every document this session touched |
| `tools/number_check.py` | clean on every document this session touched |
| `scripts/demo-ready.sh` | DEMO READY |

One caveat carried forward from the handover and still true: the test suite
failed once at 283 of 284 while a browser sweep was driving the server
concurrently. Not reproduced in seven subsequent runs, cause not established. Do
not run `npm test` while driving the demo.

---

## 7. The four things these numbers do not prove

Say these before a juror finds them.

1. **Nothing here involves a real document.** Every figure is measured on a
   corpus we wrote. It shows the system does what the design says. It does not
   show what happens to a scanned page with a handwritten correction on it.
2. **The archetype result is a consistency check.** Ten shapes of failure, all
   planted by us, all detected. A tenth archetype we did not think of is not in
   the denominator.
3. **The baseline comparison is eight fields at one run each.** It is too small
   to support a claim in either direction, including ours.
4. **Per-field regulatory rule mapping is not built.** Which rule requires which
   field is stated as absent on screen and stays that way. We are not inventing
   a citation to fill it.
