# KRISEVA ATTEST

**Entity-side evidence integrity for regulatory reporting in GIFT IFSC.**
When the source documents disagree, the software refuses to pick, shows its working,
and hands the decision to a named person who signs for it.

Kriseva AI Private Limited. GIFT IFIH Young Builders' Program 2026.

---

## Open these

| | |
|---|---|
| **The working prototype** | https://kriseva-gift-backup-2026.s3.us-east-1.amazonaws.com/prototype/index.html |
| **The submission hub** | https://kriseva-gift-backup-2026.s3.us-east-1.amazonaws.com/index.html |
| **The pitch deck** | [deck/index.html](deck/index.html) |
| **The 2 minute demo video** | https://kriseva-gift-backup-2026.s3.us-east-1.amazonaws.com/video.html |
| **The whole system in one page** | [docs/ARCHITECTURE_SIMPLE.md](docs/ARCHITECTURE_SIMPLE.md) |
| **The product, workflow and every role** | [docs/PRODUCT_AND_WORKFLOW.md](docs/PRODUCT_AND_WORKFLOW.md) |
| **Pitches** | [3 minute](docs/PITCH_3MIN.md) &middot; [1 minute](docs/PITCH_1MIN.md) |
| **What we need from IFSCA and GIFT IFIH** | [docs/RESIDENCY_ASK.md](docs/RESIDENCY_ASK.md) |
| **Every measured number** | [docs/MEASURED_RESULTS.md](docs/MEASURED_RESULTS.md) |

The prototype is the real product with all 26 cases and every screen. The application code
is embedded unmodified; only the network layer is replaced by responses captured from the
running server, so nothing is reimplemented to make the demo work. It is labelled a recorded
walkthrough on every screen.

---

## NOTICE, on what was built when

The Young Builders' Program brief states: *"No pre-built repositories allowed. Code must start
clean at 2:00 PM on Friday, 21 August. Git commit histories will be audited."*

We are stating our position before anyone has to ask for it.

- **This repository contains no application source code.** It holds documents, specifications,
  measured results, the pitch and the deck.
- **The prototype linked above is a pre-event rehearsal build.** It was built to find out what
  breaks, it is deleted before travel, and none of its code enters the sprint repository.
- **What we carry into the sprint is documents only**: specifications, schemas, prompts and the
  synthetic data plan. All of it is published here, before the sprint, in
  [docs/AGENT_CONTRACT_PACK.md](docs/AGENT_CONTRACT_PACK.md). Nothing we carry is unpublished.
- **The sprint repository starts empty at 14:00 on Friday 21 August** and is built live.

An evidence-integrity company cannot win by gaming an audit.

---

## How it works, in one line

**Read it. Check it. Refuse to guess.** Six steps that matter. Three use a model, three are
plain code, and the plain code ones are the ones that check. A model cannot check a model.

Across the whole run: **9 roles, 4 of which use a model, and of the 40 steps a case takes,
exactly 20 contain no model at all.** The Trace screen counts that itself.

On 19 August we removed a model. The scope step used to be one, and on a live run it read a
document and returned two fields, silently dropping a third that was plainly on the page. We
put deterministic string matching underneath it as a floor, then noticed the floor was
overruling the model every time they disagreed, which means the model could only ever lose
evidence. So we deleted it and re-ran the measurement. **24 of 24 before, 24 of 24 after, zero
silent picks in both.** Nothing measurable was lost and one failure mode went with it.
[The whole system in one page](docs/ARCHITECTURE_SIMPLE.md).

## What we measured

| | |
|---|---|
| Planted failure archetypes named exactly | **24 of 24** |
| Silent picks, a value chosen by software | **0 of 24** |
| A complete nine-role case | 3.3 to 7.9 seconds, 40 agent actions, about 14,700 tokens |
| Screens verified on the deployed build | 182, across all 26 cases |
| Tests, canon conformance, filing history | 299 of 299, 24 of 24, 9 of 9 |
| Four-pillar prediction against the published rubric | **90.1**, technical execution 92.5 |
| Roles using a model | **4 of 9**, reduced from 7 on 19 August with no measured loss |

Ground truth is written into every case by deterministic code **before any model sees it**, so
the system is not grading its own homework. We wrote the conflicts, which makes this a
consistency check rather than an accuracy claim about real documents, and we say so throughout.

**We predicted a frontier model with a good prompt could not do this. We ran it, and it could.**
Three frontier models, told to abstain on disagreement, abstained correctly on every conflicted
field with zero silent picks. We publish that table rather than the one we hoped for.
[Measured results, section 2](docs/MEASURED_RESULTS.md).

---

## What is not built

- **Per-field regulatory rule mapping.** Stated as absent on screen. We will not invent a citation.
- **A local open-weight model on the offline path.** The provider interface exists; the wiring does not.
- **Any contact with real data.** We have never seen a real quarterly return. Every entity,
  document, person and figure here is fictional and labelled fictional on its face.
- **A dollar cost.** The account has no pricing API access, so any price would be recalled
  rather than sourced. The token count is the honest number.

Nine defects were found by using the product rather than reading it, all of which survived 299
passing tests. All nine are published in [docs/DEFECT_LEDGER_2026-08-19.md](docs/DEFECT_LEDGER_2026-08-19.md).

---

## Contents

| Path | What it is |
|---|---|
| [docs/ARCHITECTURE_SIMPLE.md](docs/ARCHITECTURE_SIMPLE.md) | The whole system in one page, and how to explain it in ten, thirty or sixty seconds |
| [docs/RESIDENCY_ASK.md](docs/RESIDENCY_ASK.md) | Six asks in exact numbers: introductions, documents, hours, supervision, the 18 people to sit near, and the AWS credits, with what each unblocks and what we commit to by 30 October |
| [docs/MEASURED_RESULTS.md](docs/MEASURED_RESULTS.md) | Every number, its method, its scope, and the four things it does not prove |
| [docs/DEFECT_LEDGER_2026-08-19.md](docs/DEFECT_LEDGER_2026-08-19.md) | Nine defects found by use, and the rule each one produced |
| [docs/AGENT_CONTRACT_PACK.md](docs/AGENT_CONTRACT_PACK.md) | The agent prompts, the validator contracts, model routing, and the rebuild order |
| [docs/RUNNING_COST_AND_LIMITS.md](docs/RUNNING_COST_AND_LIMITS.md) | Measured rate limits per model, tokens per case, and what broke on the live path |
| [docs/SCENARIO_DESIGN.md](docs/SCENARIO_DESIGN.md) | The ten failure archetypes and the regulatory driver behind each |
| [docs/CANON.md](docs/CANON.md) | The fictional world: every entity, document and number in the demo |
| [deck/index.html](deck/index.html) | Ten slides |

---

## Data statement

Every entity, scheme, person, document and figure in this repository and in the prototype is
**fictional**. Twenty fictional fund management entities, 26 cases, 115 source documents, 80
prior quarterly filings. Every document carries the line `SYNTHETIC TEST DOCUMENT, NOT A REAL
RECORD` above its figures, so a screenshot cannot be mistaken for a real record out of context.

**No real fund, customer, investor, entity or personal data appears anywhere.**

---

Ayush Tiwary and Mahek &middot; Kriseva AI Private Limited
