# KRISEVA ATTEST: the product, the workflow, and every role

Status: STABLE. Written 2026-08-19 from the running build. Every count in this
document was produced by running a case and reading the trace, not from intent.

**This is the document to learn.** If you know only this one, you can answer
almost any question a jury asks.

---

## 1. The product in four sentences

A fund in GIFT IFSC has to file four numbers to the regulator every quarter.
Those numbers arrive from five different parties who close their books at
different times, so they disagree, and nothing in the documents says so.

**Every system built for this picks one number and files it. We refuse to pick.**

We show every number pinned to the exact line it came from, name why the sources
disagree, and hand the decision to a person who signs for it in writing.

---

## 2. The problem, in numbers

| | |
|---|---|
| Fund management entities in GIFT IFSC | **217** |
| Schemes they run between them | **360** |
| Deadline after quarter end | **21 calendar days**, four times a year |
| Numbers on the return | **4**: committed capital, drawn capital, closing NAV, complaints closed |
| Parties those numbers come from | **5**: administrator, internal ledger, subscription register, custodian, valuer |
| Who signs | The Compliance Officer and the Principal Officer, **personally** |
| Notice period when a Compliance Officer leaves | **15 days**. Records must survive **8 years** |

**The gap:** the records survive 8 years. The reasoning behind each number lives
in an email thread and leaves with the person.

---

## 3. The workflow, end to end

```text
  DOCUMENTS IN                                       A FILING OUT
       |                                                   ^
       v                                                   |
  +---------+   +---------+   +--------+   +----------+   +--------+
  |  SCOPE  |-->| EXTRACT |-->|  BIND  |-->| VALIDATE |-->| CRITIC |
  |  code   |   |  model  |   |  code  |   |   code   |   | model  |
  +---------+   +---------+   +--------+   +----------+   +--------+
   which docs    read the      is the       does the        try to
   name which    numbers and   quote        arithmetic      knock the
   fields        quote the     really       tie?            reading
                 line          there?                       down
                                                                |
                                                                v
                                                        +--------------+
                                                        |  RECONCILE   |
                                                        |    model     |
                                                        | describe the |
                                                        | disagreement |
                                                        | CANNOT pick  |
                                                        +--------------+
                                                                |
                                                                v
   +-----------------------------------------------------------------+
   |  A NAMED PERSON decides in writing                              |
   |  A SECOND NAMED PERSON signs off (cannot be the first)          |
   |  The whole trail is hash chained into a receipt that breaks     |
   |  visibly if a single byte changes                               |
   +-----------------------------------------------------------------+
```

**Say it as:** *"Read it. Check it. Refuse to guess."*

---

## 4. Every role, what it does, and which model

Measured on one complete case: **40 agent actions, 9 roles, 4 of them using a
model, 5 of them plain code.**

| # | Role | Actions per case | Model | Company | What it does, in one line |
|---|---|---|---|---|---|
| 1 | **Orchestrator** | 2 | **none** | | Writes the plan and holds one wall-clock deadline for the whole run |
| 2 | **Scope** | 4 | **none** | | Matches each field name against each document's text to see which documents carry which fields |
| 3 | **Extractor** | 8 | `amazon.nova-lite-v1:0` | Amazon | Reads every candidate number and quotes the exact line it came from |
| 4 | **Binder** | 7 | **none** | | Searches the source for that quote. Not there character for character, and the number is thrown away |
| 5 | **Validator** | 7 | **none** | | Checks the accounting identities. Undrawn commitment must equal committed minus drawn |
| 6 | **Critic** | 7 | `mistral.mistral-large-3-675b-instruct` | Mistral | Tries to knock the reading down. Forced onto a different company from the extractor |
| 7 | **Reconciler** | 4 | `zai.glm-5` | Z.ai | Describes the disagreement and names its cause. **Forbidden in code from choosing a value** |
| 8 | **Narrator** | 1 | `amazon.nova-lite-v1:0` | Amazon | Writes the two-sentence handoff to the named person |
| 9 | **Learner** | on a lesson | **none** | | Records what went wrong so it can become a proposed rule a human approves |

**Three different models from three different companies.** Amazon, Mistral and
Z.ai, on Bedrock, on our own AWS account.

### The five that contain no model, and why that is the point

**A model cannot check a model.** Scope, Bind and Validate are the three steps
that decide whether a number survives, and none of them contains a model. They
are string matching and arithmetic. The Orchestrator's plan and the Learner's
ledger are deterministic for the same reason: a model that writes its own plan
and grades its own lessons is marking its own homework.

---

## 5. How they work together, in order

1. **Orchestrator** writes a plan: which documents, which fields, in what order,
   with a retry budget and a single deadline for the whole run. Deterministic.
2. **Scope** narrows the work. For each document it checks whether the text
   contains each field's name. Nothing else. If it finds nothing, the document is
   skipped for that field.
3. **Extractor** is called once per document-and-field pair that survived scope.
   It returns candidate values, each with the exact quoted line.
4. **Binder** takes each quote and looks for it in the source document,
   character for character. It computes the character offsets itself and ignores
   anything the model claimed. **A quote it cannot find is dropped.**
5. **Validator** checks the arithmetic across the surviving candidates, per
   document. A mismatch is flagged, not corrected.
6. **Critic** runs on a different company's model and is given the reading and
   the document, and asked to attack it. An empty objection list is a valid
   answer; inventing an objection is worse than raising none.
7. **Reconciler** looks at what survived. One distinct value is `SUPPORTED`. Two
   or more is `CONFLICTED`, with a named cause. None is `UNSUPPORTED`. Its output
   is rejected by code if it contains a chosen value or a resolved state.
8. **Narrator** writes the handoff, and is blocked from any wording that implies
   the return was filed, approved or resolved.
9. **A named person** decides in writing. **A second named person**, who cannot be
   the first, signs off. The record is hash chained and sealed.

**Two things run in parallel** because they do not depend on each other:
extraction across documents, and criticism of readings already produced. That is
why 40 actions complete in three to eight seconds.

---

## 6. What is enforced in code rather than asked for politely

This list is the product. Everything else is presentation.

| Rule | How it is enforced |
|---|---|
| A quote that is not in the document does not count | The binder searches for it and drops the candidate. No model involved |
| The software may never choose between conflicting values | The reconciler's output is rejected if it contains a selected value or a resolved state, checked at every level of the object |
| The critic may not be the same model family as the extractor | Verified when the system starts. If no independent critic exists, **it refuses to run** |
| Narrowing the work may never lose evidence | Scope is plain string matching. There is no model that could drop a field |
| A run may not exceed its time budget | One deadline for the whole run, every step raced against the remaining time. A step still running at the deadline escalates to a person |
| The same person may not decide and sign off | Rejected at the sign-off endpoint |
| A field with no source may be attested but never decided | Separate endpoint, separate state, shown differently on screen |

---

## 7. What we measured

| | |
|---|---|
| Planted failure archetypes named with exactly the right cause | **24 of 24** |
| Times the software chose a value by itself | **0 of 24** |
| One complete case | **3.3 to 7.9 seconds**, 40 actions, about **14,700 tokens** |
| Tests, canon conformance, filing history | **299 of 299**, **24 of 24**, **9 of 9** |
| Screens swept on the deployed build | **182**, across all 26 cases, zero problems |
| Four-pillar prediction against the published rubric | **90.1** |

Ground truth is written into every case by deterministic code **before any model
sees it**, so the system is not grading its own homework.

**And the honest limit:** we wrote those conflicts. It is a consistency check
across ten failure shapes, not an accuracy claim about real documents. We have
never seen a real quarterly return.

---

## 8. How many roles were reduced, and when

| Date | Roles using a model | What changed |
|---|---|---|
| Before 19 Aug | **7 of 9** | |
| 19 Aug, morning | 7 of 9 | Five of the seven had stub prompts and had never worked. Fixed |
| 19 Aug, evening | **6 of 9** | **Scope's model removed.** The deterministic floor underneath it was overruling it on every disagreement, so it could only lose evidence |
| 19 Aug, late | **4 of 9** | **Orchestrator and Learner corrected to no-model.** Both carried a model id they never called. The config was overstating our own model count |

**From 7 to 4.** Two were deleted because they added risk without adding
judgement, and two were never really there and the configuration was wrong about
it. Measured before and after each change: 24 of 24, zero silent picks, 299 tests
passing, every time.

> "We took models out and the numbers did not move. That is the strongest thing
> we can say about whether they were doing anything."

---

## 9. The number the screen shows

A case takes **40 steps**. The Trace screen counts them and says, in its own
words: **20 contain no model at all.**

Exactly half the run is plain code, and it is the half that checks. That sentence
is generated from the run rather than typed, so it cannot drift away from what
actually happened.
