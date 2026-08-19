# CANON: the single fictional world every artifact must use

Status: STABLE, locked 2026-08-18. Owner: founder. Any change here propagates to every other factory artifact and must be re-verified.

**Everything on this page is SYNTHETIC and fictional.** No entity, person, fund, administrator or custodian named here exists. No real tender, bidder, customer or personal data appears anywhere in the demo corpus. This label ships on every screen, every export and every slide.

Why a canon exists: the pitch, the demo, the schema pack, the eval labels and the build spec must describe the same case, with the same numbers, in the same order. A juror who hears one number in the pitch and sees a different one on screen stops listening. One world, one set of numbers, no exceptions.

---

## 1. The fictional entity

| Role | Fictional name | Notes |
|---|---|---|
| The FME (our buyer) | Meridian Alpha Capital IFSC Private Limited | Registered FME (Non-Retail), GIFT IFSC |
| The scheme | Meridian Alpha Opportunities Fund I | Restricted Scheme, Category II AIF, USD denominated |
| Fund administrator | Northwind Fund Services (IFSC) Private Limited | Computes NAV, produces the quarterly statement |
| Custodian | Sentinel Custody Services, IFSC Branch | Confirms cash and holdings |
| Reporting period | Quarter ended 30 June 2026 | Q1 FY2026-27 |
| Return due | 21 July 2026 | 21 calendar days after quarter end, per FACT_CARD M3 |

## 2. The people (synthetic personas, not real individuals)

| Persona | Role | Function in the demo |
|---|---|---|
| Priya Ramanathan | Compliance Officer, Meridian Alpha | The maker. Assembles the return, resolves conflicts, her name attaches to every decision |
| Rajiv Menon | Principal Officer, Meridian Alpha | The checker. Second named signature under maker-checker. Legally on the hook for the signed return |
| Anita Deshmukh | Client Services Manager, Northwind (administrator) | Sends the statement, issues the revised version, never sees the ledger |

Priya is the buyer persona. Rajiv is the economic sponsor whose signature creates the demand. Full journey and emotional arc live in `PERSONA_AND_JOURNEY.md`.

## 3. The four reported fields

The return has many fields. We build four, and we say out loud that we built four on purpose.

| Field ID | Reported field | Unit | Designed outcome | Why this field is in the demo |
|---|---|---|---|---|
| F1 | Committed capital | USD | CONFLICT, cause = version | Two sources disagree because a subscription is signed but not counter-executed |
| F2 | Drawn capital | USD | CONFLICT, cause = timing | Both sources are correct as of their own cut-off. This is the field that proves the whole thesis |
| F3 | Closing NAV | USD | CONFLICT, cause = correction | The administrator restated. Only a human who knows about the restatement can pick correctly |
| F4 | Complaints closed during the quarter | count | UNSUPPORTED, abstain with no candidate | No source document contains it. Different failure mode from conflict, and it must look different on screen |

## 4. The four source documents

| Doc ID | Document | Issuer | Cut-off / version | Carries |
|---|---|---|---|---|
| D1 | Quarterly administrator statement, version 2 | Northwind | Data as at 30 Jun 2026 16:00 IST, reissued 08 Jul 2026 | F1, F2, F3 |
| D2 | Subscription register extract | Meridian Alpha (internal) | As at 30 Jun 2026 | F1 |
| D3 | Internal ledger export | Meridian Alpha (internal) | As at 30 Jun 2026 23:59 IST | F1, F2, F3 |
| D4 | Custodian holdings and cash confirmation | Sentinel | As at 30 Jun 2026 16:00 IST | F2 (cash only) |

Note the trap we designed in on purpose: D1 exists in two versions. Version 1 was issued 03 Jul 2026 and superseded on 08 Jul 2026. The internal ledger D3 was built from version 1. Nothing in either document announces this. That is exactly how it happens in practice, and it is why a silent machine pick is dangerous even when the machine is confident.

## 5. The canonical numbers (memorise these, they appear in the pitch)

| Field | D1 administrator (v2) | D2 subscription register | D3 internal ledger | D4 custodian | Correct answer | Who can know |
|---|---|---|---|---|---|---|
| F1 Committed capital | USD 42,500,000 | USD 45,000,000 | USD 42,500,000 | not carried | USD 42,500,000 | A human who knows the fourth LP has not counter-executed |
| F2 Drawn capital | USD 17,800,000 | not carried | USD 19,300,000 | USD 17,800,000 | USD 19,300,000 | A human who knows a USD 1,500,000 call landed at 17:42 IST on 30 June, after the administrator's 16:00 cut-off |
| F3 Closing NAV | USD 21,940,500 | not carried | USD 22,415,000 | cash only | USD 21,940,500 | A human who knows the administrator restated an unlisted holding on 08 July |
| F4 Complaints closed | not carried | not carried | not carried | not carried | no value may be produced | Nobody. The system must refuse |

Arithmetic sanity, so a fund-literate juror does not catch us: committed 42.5m, drawn 19.3m (45.4% called), NAV 21.94m sits above drawn capital, consistent with unrealised gains net of fees. Undrawn commitment on D1 is USD 24,700,000, which is committed 42,500,000 minus drawn 17,800,000 on that document. That identity is what the deterministic validator checks, so the figure is recorded here rather than derived on the fly. The 2.5m gap on F1 is one LP commitment. The 1.5m gap on F2 is one capital call tranche. The 474,500 gap on F3 is the restatement of one unlisted position.

## 6. The planted-conflict matrix (four distinct causes, on purpose)

| Cause | Field | The two stories | What a silent AI does | What ATTEST does | The line to say on stage |
|---|---|---|---|---|---|
| TIMING | F2 | Administrator cut off at 16:00, the call landed at 17:42 | Picks one, usually the administrator, because it looks authoritative | Abstains, shows both with their cut-off timestamps, makes the human choose | "Both documents are correct. That is the point. There is no algorithm that resolves this, only a person who knows what happened that afternoon" |
| CORRECTION | F3 | Administrator restated on 8 July, the ledger predates the restatement | Picks the higher or the more recent file, with no idea a restatement occurred | Abstains, surfaces that D1 is version 2 and D3 derives from version 1 | "The machine cannot know there was a correction. It can only know the two numbers disagree, and say so" |
| VERSION | F1 | Register counts a subscription that is signed but not counter-executed | Averages, or takes the register because it is the primary record | Abstains, shows both with exact source regions | "The register is not wrong. It is answering a different question" |
| MISSING | F4 | No document contains the field at all | Produces a plausible number, most commonly zero | Produces nothing, marks UNSUPPORTED, blocks sign-off until a human resolves it | "Zero is the most dangerous answer in regulatory reporting, because it looks like an answer" |

The four causes must look visibly different on screen. Same treatment for all four would tell a juror we built one state and relabelled it.

## 7. The state model

Case states, in order: `INGESTED` -> `EXTRACTED` -> `UNDER_REVIEW` -> `SIGNED` -> `SEALED`

Field states: `SUPPORTED` (one source, evidence bound, model proposes), `CONFLICTED` (two or more candidates, model abstains), `UNSUPPORTED` (no candidate, model abstains), `DECIDED` (a named human chose, with a recorded reason), `CONFIRMED` (a second named human signed off).

Hard rules the engine enforces and the demo shows:
1. A model may PROPOSE. A model may never DECIDE.
2. A conflicted or unsupported field cannot reach `DECIDED` without a named human and a non-empty reason string.
3. A case cannot reach `SIGNED` while any field is `CONFLICTED` or `UNSUPPORTED`.
4. The person who decides cannot be the person who signs off. Maker-checker is enforced by the engine, not by policy.
5. Sealing computes a SHA-256 chain over every artifact and every state transition. Altering one byte breaks the chain visibly.

## 8. The seven screens

| # | Screen | The one thing it proves |
|---|---|---|
| S1 | Case dashboard | Four fields, four different states, at a glance. Status is the product |
| S2 | Evidence workspace | Every proposed value is pinned to the exact source region it came from |
| S3 | Conflict decision | Both candidates stay visible. No default winner. Reason is mandatory |
| S4 | Agent trace | The model call is real and inspectable: model id, prompt hash, latency, LIVE or RECORDED badge |
| S5 | Risk and anomaly board | Deterministic indicators, each closed only by a named disposition |
| S6 | Sign-off | Two different named humans, enforced separation |
| S7 | Receipt and manifest | Portable, hash-sealed, and it breaks visibly when tampered with |

## 9. The API surface

`POST /ingest`, `POST /extract`, `GET /case/:id`, `POST /decide`, `POST /signoff`, `GET /manifest/:id`, `GET /replay/:id`, `GET /eval/run`

## 10. The demo spine (never cut, in any scenario)

ingest -> propose with source pins -> hit conflict -> abstain -> named human decides with reason -> maker-checker signs -> seal -> tamper attempt breaks the seal

If a track pivot forces the story to change, the story changes. The spine does not.

## 11. Naming and vocabulary locks

- The product is **KRISEVA ATTEST**. Never EDEST, never Edest.
- ATTEST sits **upstream of** DRR. It never "integrates with", "connects to" or "files to" anything.
- The model **proposes**. The human **decides**. The second human **confirms**. The system **seals**.
- We say **abstain**, not "fail" or "error". Abstention is a designed outcome, not a defect.
- We say **preserved disagreement**, not "conflict resolution". We do not resolve conflicts. Humans do.
- Every surface carries the word **synthetic**.

## 12. Open founder decisions that touch this canon

| # | Question | Default if unanswered |
|---|---|---|
| C1 | The second founder is Mahek Soni (RESOLVED 2026-08-19 by the founder). War room docs 00/01/07 say Sony; docs 08/10 and APPLICATION_UPDATE_BANK say Mahek | All factory artifacts use "Member 2" or "Mahek" per the newest documents. Founder must reconcile before the form and the badge |
| C2 | Do we show four fields or three? Three is the proven prototype scope, four adds the MISSING state | Four. The unsupported state is our strongest single screen and it costs one extra label |
| C3 | Currency shown as USD or INR | USD. GIFT IFSC funds are USD denominated and it reads as domain fluency |

---

## 13. Canon addition, 2026-08-19: the second case

Approved by Fable, founder may overrule. CANON now contains **two** cases for the same entity and scheme.

| Case | Quarter | Outcome |
|---|---|---|
| `CASE-2026-Q1-MER001` | Ended 30 June 2026 | The four conflicts above. This is the demo case |
| `CASE-2025-Q4-MER001` | Ended 31 March 2026 | All four fields supported, zero conflicts. This is the answer to "show me a normal one" |

No new entity, no new scheme, no new people. Full specification in `SCHEMA_PACK.md` section 11.

The two cases chain arithmetically, and this is the point rather than a detail: closing NAV of Q4 (USD 20,512,000) is the opening NAV on the Q1 ledger, and closing drawn capital of Q4 (USD 14,400,000) plus the 14 May call of USD 3,400,000 equals the USD 17,800,000 the Q1 administrator reports at its 16:00 cut-off, with the 17:42 call of USD 1,500,000 taking it to the ledger's USD 19,300,000.

The chain extends one quarter further back, and this figure is canonical because the filing history is anchored to it: **the Q4 ledger opens on USD 19,004,000**, which is therefore the closing NAV of the quarter ended 31 December 2025. Q4 movements are a capital call tranche 2 of USD 2,200,000 on 10 February 2026, an unrealised valuation movement of minus USD 480,000 on 18 March, and a management fee accrual of minus USD 212,000 on 31 March, summing to plus USD 1,508,000 and closing at USD 20,512,000. This was always in `scripts/generate.js`; it is written here because `UI_LANGUAGE_AND_VISUALS_SPEC.md` section I anchors thirty two synthetic filings to it and a number that load-bearing belongs in the canon rather than in a code comment.

Consequence for the pitch: the timing conflict is not an arbitrary planted disagreement. It is the arithmetic consequence of one payment landing one hour and forty-two minutes after somebody drew a line. If a juror walks the numbers, the conflict explains itself.

---

## 14. Canon addition, 2026-08-19: attestation, a distinct act from a decision

Decided by Fable during the rehearsal build, after adversarial tests exposed that a named human could type any number into any field and have it appear on the receipt looking exactly like a value bound to a source document. That makes the receipt dishonest, which defeats the product.

Two acts, deliberately kept separate.

| | A decision | An attestation |
|---|---|---|
| When | The field has candidates. Documents disagree, and a human picks between values the documents actually support | The field has no candidates at all. No document contains it. F4, complaints closed, is our case |
| Constraint | The chosen value must match one of the candidates. A value no document supports is rejected | Any value, but it must be explicitly flagged as an attestation and carry a reason |
| Field state | `DECIDED`, then `CONFIRMED` after sign-off | `ATTESTED`, then `CONFIRMED_UNSOURCED` after sign-off |
| On the receipt | `evidenceBacked: true`, with the source document named | `evidenceBacked: false`, `sourceDocId: null`, with the attesting human named |

**Why not simply refuse.** A field with no source would block sign-off forever, so the return could never be filed, and a product that cannot file a return is not a product. Real quarters have fields nobody has a document for. The honest answer is not to pretend otherwise; it is to record exactly who asserted the number and that nothing backs it.

**Why this makes the demo stronger.** The receipt now shows three values bound to documents and one that is a named person's word. A supervisor reading it knows instantly which number to question first. That distinction is the most useful thing on the page, and no competitor's audit trail draws it.

**The line to say on stage, at the receipt screen:**

> "Three of these numbers are bound to a document you can open. The fourth is not, because no document in this quarter contains it. So it is recorded as an attestation: Priya's name, her reason, and no source. If you are the supervisor reading this return eleven months from now, that is the number you ask about first, and you can see that without asking anybody."

Updated field states, superseding section 7: `SUPPORTED`, `CONFLICTED`, `UNSUPPORTED`, `DECIDED`, `ATTESTED`, `CONFIRMED`, `CONFIRMED_UNSOURCED`.

Updated hard rule 3: a case cannot reach `SIGNED` while any field is `CONFLICTED` or `UNSUPPORTED`. `ATTESTED` counts as resolved.

New manifest entry type: `HUMAN_ATTESTED`, recorded separately from `HUMAN_DECIDED`.
