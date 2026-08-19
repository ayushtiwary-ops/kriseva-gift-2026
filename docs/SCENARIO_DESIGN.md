# SCENARIO DESIGN: eight funds, ten pain points, one proof

Written 2026-08-19 by Fable. This is the design brief that the corpus generator and the baseline harness both build from. Every scenario traces to a verified regulatory driver in `FACT_CARD.md` or the incumbent map. No invented pain.

---

## 0. The point of all this

Two jobs, and the second one matters more.

**Job one:** show that ATTEST handles many shapes of disagreement, not the one we designed for. A demo with a single hand-picked case is an anecdote. Eight funds with ten distinct failure archetypes is a product.

**Job two, and this is the one that wins:** prove with measured numbers that a frontier model with a good prompt cannot do this. Not argue it. Measure it, on our corpus, and put the table on a slide.

Everything below is synthetic. Every entity, person and figure is fictional.

---

## 1. The eight funds

Each fund exists to carry one signature pain point. They differ in size, structure and service providers so the corpus does not look like one fund copied eight times.

| # | Fund | Type | Signature scenario | Verified driver |
|---|---|---|---|---|
| F-01 | Meridian Alpha Capital | Cat II AIF, USD | **Cut-off timing.** A capital call lands after the administrator's cut-off | Administrators and entities close their books at different times. Our proven base case |
| F-02 | Kestrel Bridge Partners | Cat II AIF, USD | **Restatement.** The administrator reissues a corrected NAV after the ledger was built from version 1 | Restatements are routine and rarely announced |
| F-03 | Anantara Growth Fund | Cat III AIF, USD | **Subscription status.** Register counts a commitment signed but not counter-executed | Register and administrator answer different questions |
| F-04 | Silverpine Credit | Cat II AIF, USD | **Missing source.** A required field appears in no document at all | Complaints, breaches and similar narrative fields often have no system of record |
| F-05 | Deccan Ridge Capital | Multi-scheme FME, 3 schemes | **Consolidation error.** Scheme-level figures do not sum to the entity-level figure reported | 217 FMEs run 360 schemes, so multi-scheme entities are the norm, not the exception |
| F-06 | Coromandel Yield Fund | Cat II AIF, USD | **Fiduciary segregation.** From 30 Sep 2026 the same firm cannot be fiduciary and administrator and valuer, so a new independent valuer produces a third, differing number | IFSCA circular 10 April 2026, existing schemes comply by 30 September 2026. FACT_CARD W4 |
| F-07 | Nilgiri Opportunities | Cat II AIF, USD | **Officer turnover.** The Compliance Officer who resolved last quarter's conflict has left. The reasoning is gone | A CO change is notified within 15 days. Records must survive 8 years. FACT_CARD B2 |
| F-08 | Tamarind Structured | Cat III AIF, USD and INR | **Currency and unit drift.** The same figure is reported in USD in one document and INR in another, with no stated rate | Cross-border entities carry mixed-denomination records |

---

## 2. The ten workflow scenarios

Eight funds carry ten scenarios, because two funds carry a second archetype each. Every scenario answers the same three questions: what goes wrong today, what a silent AI does, what ATTEST does.

| # | Scenario | Today, without us | What a generic AI does | What ATTEST does |
|---|---|---|---|---|
| S1 | **Cut-off timing** | Officer sees two numbers, cannot tell error from timing, emails the administrator, the answer lives in that thread | Picks the administrator, because it looks authoritative | Abstains, shows both cut-offs, and derives that the gap equals a movement timestamped after the earlier cut-off |
| S2 | **Silent restatement** | The corrected statement arrives and nobody notices the ledger predates it | Picks the higher number, or the more recent file, with no idea a restatement happened | Abstains, surfaces that one document is version 2 and the other derives from version 1 |
| S3 | **Subscription not counter-executed** | Register total looks authoritative and is used | Takes the register, because it is the primary record | Abstains, shows both, notes the two documents share a cut-off so timing cannot explain it |
| S4 | **No source at all** | Officer types a number because the form will not submit empty | Produces a plausible number, usually zero | Produces nothing, blocks sign-off, and if filed records it as an attestation with no source, marked permanently different |
| S5 | **Consolidation mismatch** | Scheme figures are summed by hand in a spreadsheet, off by one scheme | Reports the entity figure it was given, without checking it sums | Deterministic validator catches that the parts do not equal the whole, before any human sees it |
| S6 | **Third independent valuer** | Two valuations existed, now three. Nobody knows which is the reporting one | Averages, or picks the newest | Abstains with three candidates preserved, each bound to its issuer |
| S7 | **Officer turnover** | New officer inherits a number with no record of why it was chosen | Cannot help. It has no memory of a decision it never saw | The prior decision, its reason and the named decider are in the sealed record. The new officer reads it rather than guessing |
| S8 | **Currency drift** | USD and INR figures compared without a stated rate | Converts using a rate it invented, or compares them as if same-unit | Validator flags a unit mismatch and refuses to compare until a rate with a source exists |
| S9 | **Duplicate document** | The same statement arrives twice under different filenames and is counted twice | Treats them as two sources agreeing, which raises false confidence | Identical content hash detected. Two copies of one document is not corroboration |
| S10 | **Stale source** | A prior-quarter document is reused because it was in the folder | Extracts happily, since the document looks valid | Period check catches that the document's as-at date falls outside the reporting period |

**S9 and S10 are the two that most impress a technical juror**, because both are cases where a confident AI gets *more* confident for the wrong reason. Duplicate documents look like corroboration. A stale document looks like a valid source.

---

## 3. The comparison that proves the claim

This is the centrepiece. Not an argument, a measurement.

### The experiment

Run the identical corpus through two systems:

- **Arm A, the baseline:** a single frontier-class model on Bedrock, given a genuinely good prompt. Not a strawman. Give it the documents, the field list, and explicit instruction to say "UNCERTAIN" if sources disagree. Steelman it.
- **Arm B, ATTEST:** the full governed pipeline.

Score both on the same labelled set.

### The five measures

| # | Measure | Why it decides the argument |
|---|---|---|
| M1 | **Abstention correctness** | On fields where sources genuinely disagree, how often did each system refuse instead of picking? This is the whole product in one number |
| M2 | **Silent-pick rate** | How often did it produce a confident single value where two valid ones existed? Every silent pick is an undetectable error in a signed regulatory return |
| M3 | **Evidence-localisation success** | Of the quotes it gave, how many actually appear in the source document? We already know a live model returns quotes that do not match the source character for character |
| M4 | **Run-to-run determinism** | Ask the same question three times. How often does the answer change? A regulator asking "what did the system say" must get one answer |
| M5 | **Independent verifiability** | Can a third party confirm the output without re-running the system? |

### What we expect, and we report whatever we actually get

Predicted, to be replaced with measured values:

- M1: the baseline abstains rarely, because models are trained to be helpful. ATTEST abstains by contract.
- M2: the baseline picks silently on most conflicts.
- M3: the baseline's quotes will fail exact matching a meaningful share of the time. We have already observed this.
- M4: the baseline varies across runs even at temperature 0 on some model families. ATTEST replays byte-identically.
- M5: baseline no, ATTEST yes.

**If the numbers come back against us, we publish them anyway and say so.** A measured result that surprises us is worth more than a predicted one that flatters us, and the honesty criterion is 20% of the score.

### The one-line version for stage

> "We ran the same documents through a frontier model with a good prompt, and through our system. Same corpus, same labels. Here is the table."

That sentence ends the "why not just use Claude" question permanently, in a way no amount of architecture talk can.

---

## 4. Why we cannot be replaced, stated without the numbers

The numbers carry it. These are the sentences that frame them.

**The model is not the product.** Any competent model can read a number off a page. Extraction is a solved problem and we do not claim it as a differentiator.

**Four things a prompt cannot give you, however good the model:**

1. **A refusal you can rely on.** A model asked for a number produces a number. Refusing on conflict has to be enforced outside the model, in code that cannot be talked out of it.
2. **Evidence you can check.** A model's quote is a claim about the document, not the document. We verify every quote against the source and drop what we cannot find. That is arithmetic, not persuasion.
3. **An accountability record.** A named human, a written reason, a second signature, and a seal that breaks on edit. No prompt produces that, because it is not a text-generation problem.
4. **The same answer twice.** A regulator asking what the system reported eleven months ago needs one answer, not a fresh sample.

**The honest boundary, and say it:** if all a fund wanted was values extracted from documents, they should use a frontier model directly and we would tell them so. What they cannot get that way is a filing they can defend when somebody asks who decided.

---

## 5. Build order

| # | What | Owner |
|---|---|---|
| 1 | Extend the generator to eight funds and ten scenarios | Agent |
| 2 | Extend eval labels to cover every scenario | Agent |
| 3 | Build the baseline harness, Arm A versus Arm B | Agent |
| 4 | Run it on Bedrock, capture real numbers | Fable |
| 5 | Write the comparison into the pitch and the fact card | Fable |

Rule: the canon gate must still pass on the original Q1 case after all of this. The new scenarios are additions, never modifications. The demo case does not change.
