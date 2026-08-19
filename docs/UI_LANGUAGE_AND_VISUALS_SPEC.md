# UI LANGUAGE AND VISUALS SPEC

Status: STABLE, written 2026-08-19. Owner: founder. Verifier: this file was generated from the working rehearsal build, and every table below was extracted from the code that produced the screens, not retyped.

**Why this file exists.** The rehearsal build is deleted before travel on Thursday 20 August. Specs, schemas, prompts and synthetic data plans are explicitly permitted and are what we carry. Everything in this document was built and verified by running it on 19 August. Without this file, rebuilding from `BUILD_SPEC_v1.md` on Friday reproduces the interface a juror could not read.

**All data described here is synthetic and fictional.** Every screen carries that label.

---

## 0. The rule this whole document serves

A juror has about ten seconds to understand the first screen. The build previously showed `Committed capital, CONFLICTED`, which is jargon stacked on jargon: two unfamiliar words, and the reader disengages.

Three rules, in priority order:

1. **Never show a raw enum on screen.** Not in a chip, a tooltip, an error, or the receipt. The enums stay in the engine, the JSON and the manifest. Translate only at the display layer.
2. **A regulatory term keeps its proper name and gains a plain gloss underneath.** A domain-literate juror needs to see we know the term. Everyone else needs the sentence. Both fit.
3. **An explanation nobody clicks is not an explanation.** The one-line meaning sits on the card, never behind a hover.

Two mechanical traps found the hard way, both of which reintroduce the problem after it is fixed:

- **CSS `text-transform: uppercase` on a short label turns any word back into an enum.** `Supported` rendered as `SUPPORTED`, `Confirmed` as `CONFIRMED`, `Closed` as `CLOSED`. Six separate rules had to be found and removed. Grep for `text-transform: uppercase` before believing the job is done.
- **A state missing from the label map falls through to the raw enum.** `ATTESTED` and `CONFIRMED_UNSOURCED` were absent, so the attestation field, the one CANON section 14 calls our strongest, rendered a green `ATTESTED` chip with no value. Every lookup needs a fallback that sentence-cases an unmapped value rather than printing it.

---

## 0b. What travels on Thursday, and what does not

The hackathon bans pre-built code. Friday's repository starts empty at 14:00 and commit histories are audited. `rm -rf ~/kriseva-rehearsal-DELETE-BEFORE-21AUG` runs before travel.

| Travels | Does not travel |
|---|---|
| This document, in full | `public/app.js`, `styles.css`, `index.html` |
| Every table in it, which is the specification | `scripts/generate-history.js` and every other generator |
| The algorithms in section H, as prose and pseudocode | `public/history.json` and every generated corpus file |
| The data model in section I | The rehearsal build in any form |

**The carry pack is five documents plus three added on 19 August, and the split matters.** This document is the interface. `SCHEMA_PACK.md` and `BUILD_SPEC_v1.md` are the engineering surface. `CANON.md` is the world and every number. `RUNNING_COST_AND_LIMITS.md` is what it costs and what broke. To those, add:

| Added 19 Aug | What would otherwise be lost |
|---|---|
| `AGENT_CONTRACT_PACK.md` | The five live agent prompts, the five validator contracts they are judged against, the model routing table and why each role sits where it does, the measured concurrency and backoff constants, and the rebuild order. **None of this appeared in any carried document. It existed only in code.** |
| `MEASURED_RESULTS.md` | Every measured number and its exact scope, including the baseline comparison that did not go the way the design predicted |
| `JURY_QA_PACK.md` | The synthetic-data provenance answers, and the questions covering everything built after `QA_REDTEAM.md` was written |

A rebuild from the original five reproduces an interface a juror can read and an agent layer whose prompts have never worked. That combination passes every offline test.

The generated corpora are not carried either. They are rebuilt on Friday from the plans here and in `SCHEMA_PACK.md`, which takes about two minutes of model time on our own AWS account. Do not carry the JSON and do not carry the generators. Carry the plan and rebuild.

Everything in section H is written as an algorithm rather than as code for exactly this reason. Somebody who has read section H can rebuild the visuals from scratch in an hour. That is the point of writing it down.


## A. Field states

| Enum in the engine and the JSON | What the screen says | The one line under it |
|---|---|---|
| SUPPORTED | Sources agree | Only one document contains this number. You can open the exact line it came from. |
| CONFLICTED | Sources disagree | The documents give different numbers. They may all be correct. A person has to choose. |
| UNSUPPORTED | No source found | No document in this quarter contains this number. Nothing is filled in, because a guess would look like an answer. |
| DECIDED | You decided | A named person chose between the numbers the documents contain, and wrote down why. |
| ATTESTED | Your word, no document | No document contains this number. A named person asserted it, and the receipt says so. |
| CONFIRMED | Signed off | A second named person, not the one who decided, has confirmed this number. |
| CONFIRMED_UNSOURCED | Signed off, no document | Confirmed by a second named person, but it still rests on one person's word. |

## B. Why the documents disagree

| Enum in the engine and the JSON | What the screen says | The one line under it |
|---|---|---|
| TIMING | Different cut-off times | Each document was drawn up at a different moment. A payment landed in between. |
| CORRECTION | One document was corrected later | The issuer reissued a document with a restated figure. The other one predates it. |
| VERSION | Counting different things | Both documents are correct. They are answering different questions. |
| MISSING | Nothing to read | No document in this quarter contains this number. |
| ARITHMETIC | The parts do not add up | The parts stated in the document do not sum to the stated total. |
| UNIT_MISMATCH | Different currencies, no rate given | The two documents use different currencies and neither gives a conversion rate. |
| DUPLICATE | Same document twice | The same document was supplied more than once and the copies are not identical. |
| OUT_OF_PERIOD | From the wrong quarter | The figure found belongs to a different quarter than the one being filed. |

## C. The four reported fields

| Field | Gloss under the regulatory term |
|---|---|
| F1 | what investors have promised to put in |
| F2 | how much of that has actually been called in |
| F3 | what the fund was worth at the end of the quarter |
| F4 | how many investor complaints were resolved this quarter |

## D. Manifest entry types

| Manifest entry type | What the receipt says |
|---|---|
| DOCUMENT_INGESTED | Document read in |
| VALUE_PROPOSED | Number proposed |
| ABSTAINED | Refused to pick |
| HUMAN_DECIDED | A person decided |
| HUMAN_ATTESTED | A person gave their word |
| SIGNED_OFF | Second person signed off |
| CASE_SEALED | Sealed |

## E. Risk severity

| Severity in the code | What the risk board says |
|---|---|
| high | Needs attention |
| medium | Worth a look |
| low | Fine |

## F. The decide screen speaks twice

| Element | When the field has candidates (a decision) | When it has none (an attestation) |
|---|---|---|
| title | Choose between the sources | Put your name to a number |
| reasonLabel | Why you are choosing this one | Where this number comes from, in your own words |
| reasonHint | Say what you know that the documents alone do not show. A reason is required. | No document backs this. Your reason is the only account of where it came from, so it is required. |
| identity | Deciding as | Recorded by |
| submit | Record decision | Record this as my word |

## G. The glossary, 32 terms

- **AIF** Alternative Investment Fund, a pooled fund that is not a mutual fund, often used for private equity and credit investments.
- **Abstain** When the software refuses to pick a number because it cannot prove which one is right. A designed outcome, not a breakdown.
- **Attestation** A number personally signed by a named individual, used when a document does not contain the number itself.
- **Candidate** A number found in a document, kept together with the exact words it came from and the moment that document was true.
- **Capital call** A request from the fund to investors to pay in part of their promised investment.
- **Case identifier** The reference for one quarterly return by one fund. It carries the quarter and the entity, so CASE-2026-Q1-MER001 is the first quarter return for the Meridian entity.
- **Closing NAV** The net asset value of the fund on the last day of the reported quarter.
- **Committed capital** The total amount investors have legally agreed to invest in the fund over its lifetime.
- **Compliance Officer** The designated person at the fund management entity responsible for regulatory filings, required to be based in the IFSC.
- **Custodian** An outside firm that holds the fund cash and securities and confirms independently what is there.
- **Cut-off** The specific time at which a document's information is considered accurate, excluding any subsequent events.
- **Document code (D1, D2, D3, D4)** A short code for each source document on this case. The evidence screen shows the full title, who wrote it, and the moment it was true.
- **Drawn capital** The portion of committed capital that the fund has requested and received from investors.
- **Escalate** To hand a decision to a named person because the software is not allowed to make it.
- **FME** Fund Management Entity, the company that runs the fund and files the return.
- **Field code (F1, F2, F3, F4)** A short code for each of the four numbers on this return. F1 is committed capital, F2 drawn capital, F3 closing net asset value, F4 complaints closed.
- **Fund administrator** An independent firm hired to calculate the fund's value and produce the quarterly statement.
- **Hash chain** A sequence where each record carries a fingerprint of the one before it, so changing any earlier record breaks every fingerprint after it.
- **IFSC** International Financial Services Centre, a special financial zone with its own rules and regulator.
- **IFSCA** International Financial Services Centres Authority, the regulator for the IFSC that receives the quarterly return.
- **LP** Limited Partner, an investor in the fund, distinct from the fund managers.
- **Maker-checker** A control mechanism where two different people are required to make and approve a decision.
- **Manifest** The ordered log of everything that happened to this case, with a fingerprint on each step.
- **NAV** Net Asset Value, the worth of the fund after subtracting its debts.
- **Principal Officer** The senior person at the fund management entity who holds legal responsibility for the return.
- **Quarterly return** The report that a fund management entity must submit to the regulator four times a year, 21 days after the quarter ends.
- **Restatement** The act of reissuing a document with corrected information, replacing the previous version.
- **SHA-256** A standard way of turning any data into a short fixed-length fingerprint. The same input always gives the same fingerprint, and any change gives a completely different one.
- **Sealed** The point after sign-off where the whole case is fingerprinted end to end and can no longer be changed without it showing.
- **Subscription register** The fund's internal record of investors and their agreed investment amounts.
- **Synthetic data** Artificial data used for demonstration purposes, with no real fund, person, or investor involved.
- **Undrawn commitment** The portion of committed capital that has not yet been requested by the fund.
---

## H. The visuals, and the rule they all obey

**No dependency.** `CONTRACT.md` section 2 forbids npm packages and CDN assets, and the venue may have no network. Every visual below is hand-written HTML, CSS or inline SVG. There is no chart library. This is not a compromise: a charting dependency would be the only third-party code in a product whose entire pitch is auditability.

**Every visual is drawn from the same numbers on the same screen.** Nothing is precomputed and stored. A picture and the number beside it cannot disagree if the picture is derived from the number.

**The rule that makes these ours:** where the sources disagree, do not draw a line. Draw the range, and say it is a range. Every dashboard in this category draws one confident bar, which means somebody picked a number. Picking is the thing this product refuses to do, so the picture refuses too.

### H1. The disagreement bar, on each field card

A number line was tried first and abandoned. On a narrow card the value labels collided, and the shape of "42.5 against 45" is invisible on a linear axis because they are only six percent apart.

What works: split each bar at the **lowest** value any source gives.

```
lo   = lowest distinct candidate value
hi   = highest distinct candidate value
for each distinct value v:
    agreed   width = (lo / hi) as a percentage of the bar    solid, muted
    disputed width = ((v - lo) / hi) as a percentage of the bar  hatched, in the conflict colour
caption: "in dispute, <hi - lo>"
```

Group candidates by value first. Three candidates carrying two distinct numbers is a two-way disagreement, and the card must not say "3 candidates" as though it were three-way. Say "2 different numbers across 3 places in the documents".

If every source agrees there is one bar, fully solid, captioned "Every source that carries this field says the same number."

### H2. "The shape of this fund", above the four cards

Four rows: promised by investors, actually called in, still to be called, worth at quarter end. Each row is a bar on a shared scale, where the scale maximum is the largest value on the case.

- A **settled** field draws a solid bar and is captioned "settled by <name>".
- An **unsettled** field draws solid up to its low value, then a hatched band out to its high value.
- "Still to be called" is committed minus drawn. Two ranges subtracted widen: the honest reading is `committed_high - drawn_low` at the top and `committed_low - drawn_high` at the bottom. Never state a single tidy number here; it invents precision the documents do not support.
- Footer states the called percentage as a range: `drawn_low / committed_high` to `drawn_high / committed_low`.

**The moment this exists for:** when a named person decides, the band collapses to a solid bar in front of the room, the dependent rows narrow, and the percentage tightens. That collapse is the product, made visible. Verified live: deciding drawn capital moved the range from 39.6-45.4% to 42.9-45.4% and turned the bar green.

### H3. "The shortcut we refuse to take", on each conflicted field

Computed in the browser, deterministically, with no model involved. The point is not a clever guess, it is the most ordinary guess there is.

```
naivePick(field) = the value carried by the most documents
                   (null if fewer than two distinct values, or on a tie)
```

Before a decision: state what that rule would file, and on the strength of which documents, and that no document on the case can settle whether it is right.

After a decision: state the naive value, the filed value, and the gap between them.

**Never assert the naive rule is wrong before a person decides.** Before a person decides, nobody can know. That restraint is the argument.

On this corpus the rule gets committed capital right and drawn capital and closing NAV wrong. On drawn capital it files USD 17,800,000, because the administrator and the custodian both say so and only the ledger disagrees. It is the most reasonable rule available and it is wrong, and nothing in either document announces it.

### H4. The provenance card, on the evidence screen

Everything below was already in the case JSON and simply was not rendered. The card shows, for every candidate:

| Line | Source |
|---|---|
| The value | `candidate.value` with the unit |
| How many documents agree | derived: "also in D3", or "only this document says this" |
| Document code and full title | `document.docId`, `document.title` |
| Who wrote it | `document.issuer`, plus "your own record" or "issued by an outside party" by comparing issuer to `case.entity` |
| True as at | `candidate.cutoffAt` |
| Reached us | `document.issuedAt` |
| Whether it replaced something | `document.supersedesDocId` |
| The exact words | `candidate.quote`, with the source pane highlighting `charStart` to `charEnd` |

Internal against external matters to a compliance officer: an outside party's record and your own ledger carry different weight in a dispute.

### H5. The filing history trend

Five points: four filed quarters plus the open one. Three series: promised (dashed), called in (solid, with a light area fill), worth at quarter end (green).

The four filed quarters draw as **dots**. The open quarter draws as a **vertical band** from its low to its high value, because its numbers are still a range. Same rule as everywhere else.

SVG mechanics that matter: use a plain `viewBox` and let CSS size it. Do **not** use `preserveAspectRatio="none"`, which stretches text horizontally. Put axis labels in HTML underneath, not in the SVG, and match the label container's horizontal padding to the chart's `padX / width` ratio or every label sits beside the point it names rather than under it.

### H6. Risk meters

Each indicator carries a `ratio` and a `meterOf` string ("3 of 4 fields"). Indicators where more is worse carry `inverted: true` and colour from the conflict palette. Severity words are "Needs attention", "Worth a look", "Fine", never HIGH or MEDIUM.

---

## H7. Every verdict is clickable, and clicking it shows the working

The single most important addition. Before this, the product stated conclusions: "Counting different things. Both documents are correct, answering different questions." A reader had no way to ask on what basis. A hundred-perspective review found that thirty six reviewers wanted the software to pick a value and ten asked for something it already did, which is what happens when a design decision is invisible at the point it is being made.

**Every state chip and every cause tag is a button.** It carries a small underlined "how?" and opens a drawer.

### What the drawer contains, in this order

1. **The numbers, and where each came from.** Value, document code and title, and the moment that document was true as at.
2. **The tests that were applied, in the order they were applied.** See below.
3. **Who stands behind each document.** Issuer, whether it is your own record or an outside party's, and who a person would actually contact. The demo entity names the administrator's client services manager, per CANON section 2. Every other entity states the contact by role, because inventing a name for nineteen fictional entities would be inventing evidence.
4. **What happens next, and who does it.** Before a decision: a named person chooses, the software will not, and a second person who cannot be the first then confirms. After: who settled it, their reason in their own words, and whether it has been confirmed.

### The ladder, and the rule that makes it honest

The engine determines a conflict cause through an ordered ladder of deterministic tests. The order is fixed and the order matters:

1. **Do the parts add up to the total?** (`ARITHMETIC`)
2. **Is every number in the same currency?** (`UNIT_MISMATCH`) Checked before timing, because two numbers in different currencies are not evidence of anything until the units agree.
3. **Were the documents drawn up at different moments?** (`TIMING`) Different cut-offs alone are not sufficient. The engine additionally requires the later document to contain movements after the earlier cut-off summing to **exactly** the difference. That exactness is the strongest thing on the screen: the gap is USD 1,500,000 and the ledger holds one movement of exactly USD 1,500,000, at 17:42.
4. **Do two documents disagree while describing the same moment?** (`VERSION`) Only reachable once timing is ruled out, which is what licenses the conclusion that they are counting different things.
5. **Did one document replace an earlier version after another was built from it?** (`CORRECTION`)

Plus `MISSING` (no candidates at all, which short-circuits everything), `DUPLICATE`, and `OUT_OF_PERIOD`.

**Three states per rung, and getting this wrong is worse than saying nothing.** A first version described every rung as though it had passed, which made a ladder of eliminations read as a ladder of agreements. Each rung must render as exactly one of:

- **Ruled out**, with the reason it was ruled out. "The units agree, so the difference is real and not a conversion artefact."
- **Fired**, with the verdict it produced.
- **Never reached.** "The ladder stopped at test 3, so this test was not run and nothing here was examined." Rungs below the firing test were never evaluated, and claiming otherwise is a lie about the machine's own working.

**The verdict is never recomputed on the display layer.** It comes from the engine, and the drawer only lays out the evidence each rung looked at. An explanation that can drift away from the decision it explains is worse than no explanation.

## H8. The evidence bundle, and verifying it without our software

The receipt exports a bundle that a stranger can verify. It carries:

- Full 64-character SHA-256 hashes throughout, never the truncated form the screen shows.
- Every source document **in full text**, with its `contentHash`. Without the documents a third party can confirm the chain is internally consistent and nothing more; they cannot confirm the payloads correspond to real documents, which is the only question an auditor actually has.
- Every reported field with `evidenceBacked` true or false, the source document, the person, their reason, and the confirmer.
- Numbered instructions for verifying it without running anything of ours.

`tools/verify_bundle.py` verifies it and shares no code with the product. On a sealed demo case it confirmed 4 of 4 document hashes, 70 of 70 chain links, 70 of 70 full-length hashes, and separated the one number resting on a person's word from the three bound to documents. **Hand that script to anybody who asks whether the audit trail is real.** It is a stronger answer than any claim.

## H9. The visual system

Constraints unchanged: no npm package, no CDN, no web font, offline capable. Light theme only, because the product is read beside paper documents.

- **An elevation ladder of three steps**, no more. A surface resting on the page, one lifted under the pointer, one floating above everything. Each is two shadows, a tight contact shadow and a wide ambient one, because a single blurred shadow reads as fog rather than height.
- **The page is a sheet on a recessed ground**, so content has an edge rather than bleeding into browser chrome.
- **A state-coloured spine on the leading edge of each card**, three pixels wide. Colouring the whole card shouts when four are on screen at once; colouring the edge is legible at a glance and lets the numbers hold the middle.
- **Tabular figures everywhere by default** (`font-variant-numeric: tabular-nums` on `body`). Numbers that do not line up vertically are harder to compare, and comparing them is the entire task.
- **One focus ring, everywhere**, so keyboard use is never a second-class path.
- **The header is sticky**, so the entity you are looking at never scrolls out of reach.
- Every transition is behind `prefers-reduced-motion`.

**One trap.** `opacity` on an element fades its own text as well as its background. A filled "how?" pill built that way rendered an invisible label. Use a translucent background or underlined text, never element opacity on something containing text.

## H10. Packaging the build as a single file

`scripts/build-static.js` inlines the CSS, the data and `app.js` into one HTML file that runs with no server. Two uses: a review link, and demo-day insurance if the laptop or the port fails on stage. `app.js` is embedded byte for byte and only `window.fetch` is shimmed, serving responses captured by actually driving the real server.

**The bug worth remembering.** `String.prototype.replace` with a **string** replacement interprets `$&`, `$1`, `` $` `` and `$'` inside it. `app.js` legitimately contains `'\$&'` in the glossary escaping regex, so splicing it in as a replacement string substituted the matched `<script>` tag into the middle of that regex. The bundle was the right size, looked fine, and failed only as an SVG parse error tens of thousands of characters later. **Always pass a replacer function.** The build now parses every inlined script block with `new Function` before it is allowed to write the file, and refuses to write it otherwise.

---

## I. Filing history: the data model

Four prior quarterly returns for every fictional entity. Thirty two filings, forty three disagreements, seventy five officer notes, all synthetic. Generated by `scripts/generate-history.js` into `public/history.json` and gated by `tools/history_check.py`.

**One quarter shows the product works. Five quarters show what it is like to live with**, which is the question a fund manager actually asks. It is also where a recurring conflict stops looking like an incident and starts looking like a structural fact about how that fund receives its documents.

### Shape

```json
{ "synthetic": true,
  "quarters": [ { "key": "Q1-FY2526", "label": "...", "periodEnd": "2025-06-30", "dueDate": "2025-07-21" } ],
  "entities": {
    "F-01": {
      "entity": "...", "scheme": "...", "administrator": "...",
      "principalOfficer": "...", "currentOfficer": "...",
      "officerChange": { "after": "Q3-FY2526", "from": "...", "to": "..." },
      "quarters": [ {
        "quarterKey": "...", "label": "...", "periodEnd": "...", "dueDate": "...",
        "committed": 42500000, "drawn": 14400000, "nav": 20512000, "complaints": 2,
        "filedAt": "...", "daysBeforeDue": 4, "documentsReceived": 4,
        "conflicts":    [ { "cause": "TIMING", "field": "F2", "resolvedBy": "...", "reason": "..." } ],
        "attestations": [ { "field": "F4", "by": "...", "reason": "..." } ],
        "decidedBy": "...", "confirmedBy": "...", "sealHash": "..."
      } ] } } }
```

### The rules the generator must obey

1. **Deterministic code owns every number.** A seeded LCG, keyed off a hash of the fund id, so regenerating produces byte-identical output. If the numbers moved between runs the seal hashes would move with them, and the one thing this product sells would look unreliable.
2. **Walk backward from the current position**, subtracting an explicit list of movements. The chain then closes by construction and no quarter can silently disagree with its neighbour.
3. **Anchor the demo entity to CANON.** These five are not free choices, they are already stated in CANON section 13 and `scripts/generate.js`:
   - Q4 FY2025-26: committed 42,500,000, drawn 14,400,000, closing NAV 20,512,000, complaints closed 2
   - Q3 FY2025-26 closing NAV 19,004,000, because that is what opens the Q4 ledger
4. **Drawn capital never decreases and never exceeds committed.** Committed only grows forward in time.
5. **A model writes only the officer's note**, never a number. Cheap model, high temperature, and a rotating circumstance so the notes differ. A first pass at temperature 0.3 produced thirty two notes that all began "Both documents were accurate as of their respective cut-off dates", which is exactly the failure this generator exists to avoid. Vary the circumstance (first time seeing it, recurs every quarter, called the administrator, found it near the deadline, a colleague flagged it) and the voice, and forbid the phrasing the first pass overused. Result: 75 unique notes from 75.
6. **Every quarter carries the entity's signature conflict**, because that is what a recurring structural problem looks like, plus a second unrelated one about 45 percent of the time, because real quarters are not tidy.
7. **Complaints closed has no source document in any quarter**, so every quarter carries one attestation. Four quarters, four times somebody had to put their own name to a number.

### The officer turnover archetype

One entity, Nilgiri, changes Compliance Officer after Q3. The first three quarters were settled by one person; her successor inherits the same recurring conflict. IFSCA requires the change notified within 15 days and the records kept for 8 years (FACT_CARD B2, GREEN). The reasoning is the part that normally does not survive, because it lived in one person's head and an email thread. Here every quarter still carries the reason in her own words, against her own name. This is the strongest single story in the history and it is worth switching entities on stage to show it.

---

## J. Three defects this pass found by using the product, not by reading it

Recorded because each one was invisible from the code and obvious the moment somebody clicked.

1. **The attestation screen dead-ended.** The engine has enforced attestation as a separate act since `CONTRACT.md` amendment 9. The frontend had never been wired to `POST /api/attest`, so the decide panel posted to `/api/decide`, which correctly refused. On stage, on the screen CANON calls our strongest, the founder would have got a raw error containing the literal string `attest()` and the field would never have resolved. **Wire both endpoints, and route on `field.state === 'UNSUPPORTED'`.**
2. **Four of the eight conflict causes rendered nothing.** `CAUSE_META` held four entries; the corpus produces seven. `ARITHMETIC`, `UNIT_MISMATCH`, `DUPLICATE` and `OUT_OF_PERIOD` fell through to an empty string, so on four of the ten archetypes the screen never said why the documents disagreed. **Map every cause the corpus can produce, and fall back to a sentence-cased value, never to nothing.**
3. **The app opened on the wrong case.** It loaded `cases[0]` from a directory listing, which sorts the clean Q4 comparison quarter ahead of the demo case. The opening screen showed four identical green cards. **Name the demo case explicitly and fall back to the first.**

And two smaller ones worth the same treatment:

4. **The case state never advances past `INGESTED` after a governed run**, so the progress stepper said "Ingested" above four extracted fields, and the "Run governed analysis" button stayed clickable and returned a rejection. Derive the displayed position from the field states, never below the stored state, and disable the button on analysed content rather than on the state label.
5. **`reset.sh` deleted every `data/case-*.json` and regenerated only two**, dropping ten of the twelve entities from the picker. Restore the scenario corpus from `data/scenarios/` after a reset.

---

## K. What a run of 40 agent actions actually shows, said honestly

On the recorded path, 34 of 40 steps report under a millisecond. A technical juror reads a column of zeros as fabricated, and they are right to. The answer is not to invent plausible latencies. It is to say what the number measures.

Of the 40 steps in the demo case: **16 contain no model at all**, because the binder and the validator are plain code, on purpose, since a model cannot be the thing that verifies a model. The other 26 replay a response recorded from the model named beside them, across six different models. The times are how long each step took in that run, which on the recorded path is disk read time.

Say that on the screen, computed from the run records rather than asserted. It converts the weakest-looking column into the strongest architectural claim on the page.

---

## L. Verification

Nothing in this document is a plan. All of it ran on 19 August 2026 and was checked by executing it.

```bash
cd ~/kriseva-rehearsal-DELETE-BEFORE-21AUG/attest && bash scripts/demo-ready.sh
```

Rebuilds the corpus, restores all eight entities, starts the server, seeds the demo case, runs every gate, and prints `DEMO READY` or `NOT READY`. Idempotent.

| Gate | What it proves | Result on 19 Aug |
|---|---|---|
| `npm test` | engine, manifest, agent runtime, frontend contracts | 284 of 284 |
| `tools/canon_check.py` | the screen matches CANON | 24 of 24 |
| `tools/history_check.py` | the filing history chains and closes onto CANON | 9 of 9 |
| `scripts/demo-check.sh` | ingest, extract, manifest, tamper, standalone verifier | 8 of 8 |
| Browser sweep | 12 entities across 5 screens, no raw enum, no empty agent trace | clean |

**The canon gate needed one change**, and it is the only gate that was touched: `advanced` did not include `ATTESTED` or `CONFIRMED_UNSOURCED`, which CANON added on 19 August. Attesting F4 is a scripted demo step, and doing it made the gate report `1 of 24 checks FAILED` on a build that was correct. A gate that cries wolf minutes before a pitch is worse than no gate.
