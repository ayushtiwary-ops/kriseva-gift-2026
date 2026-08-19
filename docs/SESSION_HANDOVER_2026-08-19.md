# SESSION HANDOVER, 19 August 2026

For the founder, on waking. Everything below was verified by running it. Nothing here is a plan.

**Start here:**

```bash
cd ~/kriseva-rehearsal-DELETE-BEFORE-21AUG/attest && bash scripts/demo-ready.sh
```

It rebuilds the corpus, restores all eight fictional entities, starts the server, seeds the demo case, runs every gate, and prints `DEMO READY` or `NOT READY`. Idempotent. Then open `http://localhost:4000`.

---

## 1. The objection you raised, and what it looks like now

You said "Committed capital, CONFLICTED" is jargon stacked on jargon, and a juror disengages. That is fixed, and the fix went further than a rename because the rename exposed things underneath it.

The card now reads:

> **Committed capital**
> *what investors have promised to put in*
> `Sources disagree`
> The documents give different numbers. They may all be correct. A person has to choose.
> 2 different numbers across 3 places in the documents, each tied to the exact line it came from.
> `Counting different things` Both documents are correct. They are answering different questions.

Verified mechanically: **84 screens across 12 entities, zero raw enums, zero broken values.** The full mapping is in `UI_LANGUAGE_AND_VISUALS_SPEC.md`.

Two traps worth knowing, because both reintroduce the problem after it is fixed. CSS `text-transform: uppercase` turns any short label back into an enum, and six separate rules had to be found. And a state missing from the label map falls through and prints its own key, which is how `ATTESTED` reached the screen.

---

## 2. Six defects found by using the build, not reading it

Full detail in `DEFECT_LEDGER_2026-08-19.md`. The one that mattered most:

**The interface was never wired to the attestation endpoint.** The engine has enforced attestation as a separate act since the contract amendment. The frontend posted every field to `/api/decide`, which correctly refuses an unsourced field. On stage, on the screen CANON calls our strongest, you would have clicked through and got a raw engine rejection containing the literal string `attest()`, and the field would never have resolved. Reproduced through the UI, then fixed, then re-verified end to end.

The others: four of eight conflict causes rendered no explanation at all; the app opened on the clean comparison quarter instead of the demo case; the progress stepper contradicted the cards; `reset.sh` dropped ten of twelve entities.

---

## 3. What is new, and what it is for

| Thing | What it does | Why it earns its place |
|---|---|---|
| **The shape of this fund** | Four bars above the cards. Where sources disagree the bar stops early and goes hatched | Every dashboard in this category draws one confident bar, which means picking. Picking is what we refuse. When a person decides, the band collapses in front of the room |
| **The shortcut we refuse to take** | Computes what an ordinary system would file: the number most documents agree on | On drawn capital that rule files 17.8m and is wrong, and nothing announces it. This is the pain, made concrete, without claiming what is correct before a person decides |
| **Filing history** | Four prior quarters for all eight entities. 32 filings, 43 disagreements, 75 officer notes | One quarter shows the product works. Five show what it is like to live with. The same conflict recurs every quarter, so it is structural, not an incident |
| **Entity switcher** | Twelve cases, eight entities, in the top strip | The corpus already existed. Nothing in the interface reached it, so the product looked like it handled one fund |
| **Glossary** | 32 terms, one sentence each, plus dotted-underline terms in place | A juror who does not know what NAV stands for never has to say so out loud |
| **Provenance on every candidate** | Who wrote it, whether they are an outside party or you, when it was true, when it reached you, whether it replaced a version, and the exact words | All of it was already in the JSON and simply was not rendered |

**The strongest single story** is Nilgiri Opportunities in the History screen. Three quarters settled by one Compliance Officer. She leaves. Her successor inherits the same conflict and, in every tool that exists, none of the reasoning. IFSCA requires the change notified in 15 days and records kept 8 years, and the reasoning is the part that normally dies. Worth switching entities on stage for.

---

## 4. Gates, all green

| Gate | Result |
|---|---|
| `npm test` | 284 of 284 |
| `tools/canon_check.py` | 24 of 24 |
| `tools/history_check.py` | 9 of 9 (new) |
| `scripts/demo-check.sh` | 8 of 8 |
| Browser sweep, 12 entities x 7 screens | 84 screens, 0 problems |

One honest caveat: the test suite failed once at 283 of 284 while the browser sweep was driving the server concurrently. **Not reproduced in seven subsequent runs, including under deliberate concurrent load. Cause not established.** Do not run `npm test` while driving the demo, and it has not recurred.

`canon_check.py` needed one change and it is the only gate touched. It did not know about `ATTESTED` or `CONFIRMED_UNSOURCED`, which CANON added on 19 August, so attesting F4 (a scripted demo step) made it report a failure on a correct build.

---

## 5. What travels on Thursday

The rehearsal build is deleted. Everything built today is captured in two new documents so Friday can rebuild it:

- **`UI_LANGUAGE_AND_VISUALS_SPEC.md`** (also as PDF). Every label, the full glossary, every visual algorithm as pseudocode, the history data model, and the defects. Generated from the working code, not retyped. `BUILD_SPEC_v1.md` now opens by pointing at it, because building from the engineering spec alone reproduces the interface a juror could not read.
- **`DEFECT_LEDGER_2026-08-19.md`**. What using it found that reading it did not.

Do not carry the generators or the generated JSON. Carry the plan and rebuild; it is about two minutes of model time.

---

## 6. Resource use

Claude was spent on judgement: deciding what a finding meant, what to reject, and text a juror reads. Everything repetitive went to Bedrock: **167 calls, roughly 114,000 tokens**, across Nova Lite, Nova Pro, Mistral Large, GLM, DeepSeek and Kimi. That covered the plain-language pass, the 32-term glossary, 75 officer notes, and two five-model adversarial reviews.

The red team was run twice, five independent models with different lenses each time. Several findings were rejected as wrong: one model invented numbers, another wanted us to auto-pick the administrator's figure, which is precisely the failure we exist to refuse.

---

## 7. What I did not do

- **The live agentic run is fixed. 481 seconds is now 3 to 8 seconds.** Full detail in `RUNNING_COST_AND_LIMITS.md`. The headline: five of six model-backed roles had no real prompt, only a one-line stub that never stated the JSON shape it had to return. The recorded path computes each role deterministically and never calls a model, so the demo worked perfectly while the live path had never functioned. A live run now completes 40 agent actions in about five seconds, resolves all four fields exactly as CANON specifies, and passes 24 of 24 canon checks. Measured cost: about 14,700 tokens per case, recorded per agent action.
- **Correction: the wall-clock budget DOES enforce.** The brief I started from said it did not, and that was stale. `src/orchestrator.js` sets one deadline for the whole run (`Date.now() + plan.budget.wallClockMs`), races every step against the remaining time with an `AbortController`, and returns a `TIMEOUT` run that escalates to a named human. Verified by running the test on its own: a permanently hanging agent against a 30 millisecond budget escalates in 36 milliseconds instead of hanging. **Stop disclosing this as a weakness.** Eight of the hundred review perspectives independently flagged it as a missing safety control, which means we were being marked down for a control we actually have and were volunteering a fault that does not exist.
- **The offline path still uses recorded responses, not a local open-weight model.** The provider interface exists, the wiring does not.
- **I did not expand beyond eight entities.** The corpus has 12 cases, 8 entities, 54 documents, 10 archetypes and 32 historical filings. More entities adds marginal demo value and real risk: every number is one more thing a fund-literate juror can catch. Your call if you want more.
