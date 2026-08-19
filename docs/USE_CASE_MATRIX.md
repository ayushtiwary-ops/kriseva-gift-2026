# USE CASE MATRIX: one build, every angle a juror can throw

Status: DRAFT, built 2026-08-18. Owner: founder. Sources: CANON.md (locked 2026-08-18), FACT_CARD.md (compiled 2026-08-18), 03_STRATEGY_PLAYBOOK.md sections 1, 5, 7, cross-checked against 01_MASTER_PLAN.md and 04_CLEAN_START_BUILD_KIT.md for schedule and milestone facts. Every number here traces to one of those files or is marked hypothesis.

Two threats, one document. First, the build prompt releases 10:00 Friday and may not match our thesis: section 2 is the pre-decided pivot. Second, and this is the founder's specific worry, a juror says "show me a different case" mid Q&A: section 3 is the answer bank. Both threats share one defense. The spine does not move.

---

## 1. The invariant

The spine: propose, abstain, decide, confirm, seal. A model proposes a value with a source pin, or it abstains because two sources disagree or no source exists. A named human decides, with a reason. A second named human confirms. The system seals the record with a hash chain. No track pivot, no scenario, no juror question changes this sentence.

The state model does not change. Case states: `INGESTED -> EXTRACTED -> UNDER_REVIEW -> SIGNED -> SEALED`. Field states: `SUPPORTED -> CONFLICTED/UNSUPPORTED -> DECIDED -> CONFIRMED` (CANON section 7). The five hard rules the engine enforces hold in every track and every scenario in this document: a model may never decide, no decision without a named human and a non-empty reason, no signing while any field is conflicted or unsupported, the decider cannot be the confirmer, sealing breaks visibly on a single altered byte.

The evidence objects do not change: Case, Field, SourceDoc, Binding, Conflict, Decision, Signoff, ManifestEntry, RunRecord, EvalItem (BUILD_SPEC data model, 04 section 5). Whatever the released prompt calls the fields, whatever fixture a juror asks for, it is still one of these ten nouns wearing a different label.

What changes is vocabulary, the field list, and the fixture pack. That is the entire pivot budget. If a proposed pivot touches the spine, the state model, or the evidence objects, it is not a pivot, it is a rebuild, and a rebuild does not fit in the hours we have. Carry this into 10:00 Friday: the released prompt does not decide whether we can answer it. It only decides which four nouns we use.

---

## 2. The track pivot matrix

Doc 03 section 5 named five likely tracks and one rule: change the story and the fixture pack, never the spine. This expands each into a full pivot brief and adds a sixth row for the track that matches nothing on the list. All six use CANON entities: Meridian Alpha Capital IFSC Private Limited (the FME), Meridian Alpha Opportunities Fund I (the scheme), Northwind Fund Services (the administrator), Sentinel Custody Services (the custodian), Priya Ramanathan (maker), Rajiv Menon (checker). Renaming what the documents are called, per track, is a hypothesis about what reads best on stage, not a rule; the underlying entities do not change.

### Track: Risk and Compliance (base case, most likely per doc 03 section 0)
- **Reframe:** No reframe needed. This is the thesis as built: an FME's quarterly return has fields that conflict across administrator, internal and custodian records, and an AI that resolves the conflict silently creates a liability nobody can trace. ATTEST is the evidence layer that makes the entity's own sign-off defensible before the number ever reaches the regulator's pipeline.
- **Four fields become:** unchanged. F1 committed capital, F2 drawn capital, F3 closing NAV, F4 complaints closed.
- **Four source documents become:** unchanged. D1 administrator statement, D2 subscription register, D3 internal ledger, D4 custodian confirmation.
- **Conflict causes that still apply:** all four, cleanly. TIMING on F2, CORRECTION on F3, VERSION on F1, MISSING on F4.
- **What changes in the build:** nothing. This is the baseline BUILD_SPEC.
- **What changes in the pitch cold open:** nothing. Use the 03 section 2 cold open verbatim.
- **Cost to re-skin:** zero. Hypothesis: not measured, because there is nothing to re-skin.

### Track: Fraud
- **Reframe:** The same four numbers stop being a filing problem and become a suspicious-activity problem: a drawn-capital figure that will not reconcile against the custodian's cash, or a NAV correction landing right after a redemption request, is exactly what a fraud analyst is trained to distrust. ATTEST's abstention becomes the analyst's queue: every unresolved conflict is a named disposition, never a silent close.
- **Four fields become:** F1 committed capital becomes subscription authenticity (signed but not countersigned reads as a red flag, not a timing note); F2 drawn capital becomes cash-movement reconciliation; F3 closing NAV becomes a valuation-integrity indicator; F4 complaints closed becomes an unresolved-complaint count.
- **Four source documents become:** D1 becomes the system-of-record valuation report; D2 becomes the subscription and KYC register; D3 becomes the internal transaction ledger; D4 becomes the independent cash confirmation. The custodian cross-check is, if anything, a more natural fit in fraud framing than in the base case.
- **Conflict causes that still apply:** all four. MISSING (F4) is arguably a stronger fit here: an unlogged complaint reads as suppression, not administrative gap.
- **What changes in the build:** labels and copy only. Screen text, field names, the risk-board framing sentence. Zero schema change, zero engine change.
- **What changes in the pitch cold open:** "A fund's numbers disagree across three systems of record. Today an AI reads them and picks one silently. In fraud review, that silent pick is exactly how manipulation survives an audit."
- **Cost to re-skin:** hypothesis, about 2 to 3 sprint hours (copy and label changes across seven screens plus script rewrites, no data-model work).

### Track: Cross-border payments
- **Reframe:** A payment, or the report describing it, has to survive two regulators reading two different sets of records, cut at different times in different time zones, and today nothing proves the entity's number was defensible in either jurisdiction. ATTEST's sealed manifest becomes the portable proof that travels with the transaction, not a record that only satisfies one side.
- **Four fields become:** F1 becomes remittance amount instructed; F2 becomes amount settled to beneficiary (a natural TIMING fit: correspondent cut-off versus settlement confirmation across time zones); F3 becomes the FX rate or valuation applied at settlement; F4 becomes sanctions-screening exceptions closed.
- **Four source documents become:** D1 becomes the correspondent bank advice; D2 becomes the originating payment instruction; D3 becomes the internal treasury ledger; D4 becomes the beneficiary-bank confirmation.
- **Conflict causes that still apply:** all four. TIMING is the strongest natural fit here, CORRECTION fits an amended FX rate, VERSION fits an instruction amended but not yet countersigned, MISSING fits an unlogged screening exception.
- **What changes in the build:** labels and copy. Numbers stay in USD, which CANON already fixes for GIFT IFSC (section 12, C3), so no currency-conversion logic is needed even though the story crosses borders.
- **What changes in the pitch cold open:** "A payment record has to satisfy two regulators who never compare notes with each other. We show you what happens when their two versions of the record disagree, and who is allowed to decide which one stands."
- **Cost to re-skin:** hypothesis, about 3 to 4 sprint hours (copy, plus one new explanatory sentence per screen for the two-jurisdiction framing).

### Track: Treasury intelligence
- **Reframe:** A treasury desk pulls cash and facility numbers from a bank statement, a facility register and an internal ledger cut at different times of the same day, and a wrong number here moves a board decision, not just a filing deadline. ATTEST proposes the treasury numbers with evidence and abstains the instant two sources disagree, instead of quietly trusting whichever statement arrived first.
- **Four fields become:** F1 becomes committed facility or credit-line amount; F2 becomes drawn or utilised balance; F3 becomes closing cash position; F4 becomes covenant breaches closed in the quarter.
- **Four source documents become:** D1 becomes the bank statement; D2 becomes the facility or credit register; D3 stays the internal treasury ledger (only because it already was one); D4 becomes the counterparty or lender confirmation.
- **Conflict causes that still apply:** all four, cleanly. This track is structurally the closest relative of the base case: still a quarterly number pulled from administrator-like, internal, and third-party-confirmation sources.
- **What changes in the build:** labels only, and fewer of them than any other pivot, since committed, drawn and closing position are already close to natural treasury vocabulary.
- **What changes in the pitch cold open:** "A treasury report is built from three records that were never cut at the same moment. We show you the one number that should stop a sign-off, and who has to sign anyway."
- **Cost to re-skin:** hypothesis, about 1 to 2 sprint hours, the cheapest pivot on this list.

### Track: Financial inclusion or customer experience (worst fit)
- **Reframe:** An onboarding or KYC decision gets partly made by AI today, and the applicant-facing fields, income, source of funds, a risk rating, come from documents that do not always agree, so the same abstain-decide-confirm spine becomes an accountable override trail instead of a silent auto-approval. Say plainly this is the weakest natural fit on this page, before a juror has to point it out.
- **Four fields become:** F1 becomes declared income or net worth; F2 becomes source-of-funds amount; F3 becomes risk score or rating; F4 stays complaints or disputes closed, this one barely changes.
- **Four source documents become:** D1 becomes the KYC declaration form; D2 becomes the supporting bank statement; D3 becomes the internal onboarding case file; D4 becomes the third-party verification report.
- **Conflict causes that still apply, honestly:** TIMING and MISSING map cleanly (a stale bank statement, an unlogged complaint). CORRECTION and VERSION are strained: an onboarding file rarely has a formal restated-version-2 the way a fund administrator statement does. On this track we would be authoring a conflict cause the domain does not naturally produce, and a domain-literate juror may notice. Say so rather than paper over it.
- **What changes in the build:** more than any other pivot. Labels, plus a persona adjustment (Priya's compliance-officer framing has to shift toward reviewing an onboarding exception rather than a quarterly return), plus we would likely thin the CORRECTION and VERSION scenarios rather than force them.
- **What changes in the pitch cold open:** "An AI approves or declines an applicant today, often on its own. We show you what happens when the documents behind that decision disagree, and why a silent approval is the most dangerous outcome, not the fastest one."
- **Cost to re-skin:** hypothesis, about 4 to 5 sprint hours, the most expensive pivot on this list. Attempt only if forced, matching doc 03 section 5's own "only if forced" framing.

### Track: wildcard, none of these
- **Reframe:** Do not reskin the fixture at all. Keep the Meridian Alpha case exactly as built and reframe the narrative one level up: whatever the released track asks for, the underlying failure is the same one we already solve, an AI reads conflicting evidence and decides silently, and we show exactly that failure and exactly how we close it, using the clearest worked example we have. Say this is a generalization on stage, not a hidden mismatch.
- **Four fields become:** unchanged, presented explicitly as a worked illustration rather than a literal fit to the released prompt.
- **Four source documents become:** unchanged.
- **Conflict causes that still apply:** all four, because nothing about the fixture changes.
- **What changes in the build:** nothing.
- **What changes in the pitch cold open:** only the framing sentence at the top. "Whatever this track asks for, here is the failure underneath it that we already solve. Watch." Then run the unmodified demo.
- **Cost to re-skin:** zero for the fixture. If, and only if, the released prompt genuinely cannot host the spine at all (not "does not match our story" but "there is no evidence-and-accountability shape here to demonstrate"), doc 03 section 5's own escalation applies: stop, and take the decision to the founder at 10:45 with two options on paper. That escalation, not a rebuild, is the real cost of this row.

**Decision rule and deadline.** At 10:00 Friday, both founders write the released prompt down verbatim. Match it against the six rows above within the hour. If one row is a clear fit, say so and move on. If two rows are plausible, take the cheaper one unless the pitch narrative is meaningfully stronger on the other, in which case the founder presenting Round 1 makes the call, not a discussion. If no row fits at all, use the wildcard row's escalation. Either way, the pivot is locked by 11:00, when the AWS briefing starts, and it is not reopened after that regardless of a better idea arriving at hour 6. Route architecturally once. Relitigating a locked pivot mid-sprint is exactly the kind of symptom-shifting the sprint cannot afford.

---

## 3. The in-Q&A scenario bank

Twelve scenarios: the ten the founder named as the minimum, plus two governance scenarios that belong next to them. Format per scenario: the ask, whether we show it live or describe it, the answer or demo path, and the honest boundary, stated out loud rather than hidden.

**1. A third conflicting document.**
Ask: "What if there were three sources disagreeing, not two?"
Show: describe only, no fixture built for this today.
Answer: the conflict object already holds two or more candidates by design (CANON section 7 defines CONFLICTED as "two or more candidates"). A third document renders as a third card on the same screen, not a new feature.
Boundary: the data model supports it; the three-card layout has not been visually tested under time pressure, and we say that if pushed rather than claim polish we have not rehearsed.

**2. A document in a different format.**
Ask: "What if one source was a scan or a photo instead of clean text?"
Show: describe only, unless the fixture shortlist in section 4 changes this.
Answer: extraction runs through the same model path regardless of input format; the binding still points at a source region, though confidence changes with scan quality, not the architecture.
Boundary: FACT_CARD T2 is the honest ceiling: a 2025 benchmark put the best multimodal model near 96% on clean invoices and near 87% on scanned receipts, with real degradation on noisy scans. We have not benchmarked our own pipeline on scanned input, and we say that rather than borrow someone else's number.

**3. A document with no timestamp.**
Ask: "What if a source doesn't say when it was produced?"
Show: describe only.
Answer: a TIMING-cause conflict needs a timestamp to resolve. Without one, the field cannot leave CONFLICTED, and the honest behavior is to keep abstaining and say why, not guess a date. This is a strength, not a hole: the system degrades safely.
Boundary: we have not built a distinct missing-timestamp UI treatment; it renders as an ordinary abstained conflict without a date badge, which is correct but not polished.

**4. Two documents that agree (the boring happy path).**
Ask: "Show me a field where the sources just agree. Does this work when there's no drama?"
Show: live, and it costs nothing new. D1 and D4 already independently agree on the pre-cutoff figure for F2 (both show USD 17,800,000, CANON section 5), while D3 is the correct outlier. The evidence workspace already renders this corroboration.
Answer: point at the two matching source pins for F2 live, then be candid about the next sentence.
Boundary: all four fields we chose are deliberately exceptional (CANON section 3: "we build four, and we say out loud that we built four on purpose"). A field that is SUPPORTED end to end, with a single source and zero conflict, is not currently in the fixture pack. That gap and its fix are named in section 4 below.

**5. A deliberately wrong model output.**
Ask: "What if the model is just confidently wrong?"
Show: live. This is the planned M5 failure-mode demo (04_CLEAN_START_BUILD_KIT hour 15 to 19): the model proposes an incorrect value on purpose, caught by abstention.
Answer: a wrong-but-plausible proposal is caught one of two ways: the source-binding check (the cited region does not actually contain the proposed value), or the eval harness's labeled scoring (BUILD_SPEC's eval protocol scores abstention correctness explicitly).
Boundary: we catch wrong outputs through binding verification and labeled evaluation, not because the model knows it is wrong. A hallucinated value paired with a source citation that superficially seems to match it is the one failure class we are not claiming to have solved, and we say so if asked directly.

**6. A field the model is confident about but that fails a deterministic check.**
Ask: "What if the answer looks right but breaks a rule you check separately?"
Show: live, using the arithmetic sanity already built into the canonical numbers (CANON section 5: committed 42.5m, drawn 19.3m, 45.4% called, NAV above drawn is consistent with unrealised gains net of fees).
Answer: the risk and anomaly board (S5) runs deterministic indicators independent of the model, and any breach becomes a named disposition regardless of how confident the model was.
Boundary: today's deterministic checks are the arithmetic sanity rules built for this fixture, not a general rules engine. We have not built a configurable rules DSL, and if asked whether this generalizes to arbitrary regulatory rules, the honest answer is not yet.

**7. A duplicate document submitted twice.**
Ask: "What if the same statement gets uploaded twice by mistake?"
Show: describe only.
Answer: ingestion should be idempotent on document identity, since a duplicate must never count as a second, independent corroborating source, that would manufacture false agreement, the opposite of scenario 4.
Boundary: hash-based dedup is a straightforward extension of the sealing manifest's own SHA-256 use, but it is not built or rehearsed today. Ingesting the same file twice would currently just ingest it twice. We name this as a known gap, not a solved case, if asked.

**8. A stale source from a prior quarter.**
Ask: "What if someone uploads last quarter's statement by accident?"
Show: describe only.
Answer: every source document already carries its own cut-off metadata (CANON section 4). A document whose period does not match the case's reporting period is visible immediately in the evidence workspace next to the citation, and could become a deterministic risk-board block.
Boundary: we display the period metadata today. We do not hard-block ingestion of an out-of-period document. That is a reasonable next build, not current behavior.

**9. A case with no conflicts at all.**
Ask: "Walk me through a completely clean quarter. Does the system just wave it through?"
Show: describe today, live if the fixture shortlist item in section 4 gets built.
Answer: a clean case moves through the identical spine: every field proposes as SUPPORTED, no field needs a DECIDE step because nothing abstained, both named humans still confirm at sign-off, and the case still seals with a full manifest. Governance does not relax because nothing conflicted, that is the point, this is standard operating procedure, not a conflict-only feature.
Boundary: we have not built a second, fully clean case yet. Today's fixture pack is the one Meridian Alpha case with four deliberately exceptional fields. Proving the boring-quarter claim live needs one more fixture, the top pick in section 4.

**10. A case where the human decides against the evidence.**
Ask: "What if your compliance officer picks the number your own fact card calls wrong?"
Show: live. The engine cannot and must not stop this; the human's authority is real, not cosmetic.
Answer: DECIDE accepts any candidate value plus a mandatory reason string. The system does not silently override or flag the human's choice as wrong; it records who, what, when and why, exactly what a regulator would later inspect.
Boundary: this is a deliberate design choice, not a gap. ATTEST is an accountability layer, not a compliance-truth oracle, and it will faithfully seal a bad decision alongside a bad reason. Maker-checker, a second named human checking the first, is the safeguard, not an ATTEST judgment call.

**11. An attempt to bypass maker-checker.**
Ask: "What stops one person from deciding and signing off on their own call?"
Show: live. Attempt the forbidden action on stage: same identity for decide and confirm.
Answer: CANON's hard rule 4 is enforced by the engine: the confirmer's identity cannot match the decider's identity, and the attempt is rejected, not merely discouraged by policy.
Boundary: enforcement is by identity match on our two named demo personas, Priya decides, Rajiv confirms. We are not simulating enterprise authentication or SSO; identity is asserted by whichever named user is active in the demo session, and we say that plainly rather than imply a security posture we have not built.

**12. Tampering with a sealed manifest.**
Ask: "Prove the seal means something, don't just tell me."
Show: live. This is the closing beat of the demo spine itself (CANON section 10).
Answer: export the sealed receipt, change one byte in a copy, re-run verification, show the hash chain fail visibly.
Boundary: the hash chain proves the artifact was not altered after sealing. It cannot and does not prove the underlying source documents were truthful before ingestion. Worth saying out loud so nobody mistakes tamper-evidence for fact-verification.

---

## 4. The prepared-fixture shortlist

Method, stated plainly so the ranking is checkable: score each scenario on likelihood a juror asks (1 low to 3 high, weighted toward what the 20% Problem Depth and Regulatory Realism and 30% Founder and Venture Assessment criteria reward) times ease to prepare (1 hard to 3 cheap). Highest product wins.

Scenarios 10, 11 and 12 need zero new fixture, they are pure live choreography on the existing case; they need rehearsal time, not data-authoring time, and are excluded from this ranking. Scenarios 5 and 6 are already inside the planned M5 milestone and the canonical arithmetic, so they carry zero incremental fixture cost either.

That leaves seven scenarios that would need genuinely new fixture content: 1, 2, 3, 4, 7, 8, 9. Ranked, decisively:

1. **A second, fully clean case (scenario 9), top priority.** Likelihood 3: "does it only do drama" is close to the single most natural regulatory-realism question on this list, and the founder named it explicitly as a must-show. Ease 2: needs a second small fund case authored end to end with all four fields SUPPORTED, reusing CANON's entity style as a second fictional fund, not a rebuild of the engine. Hypothesis: about 2 to 3 sprint hours to author and label, most of it writing plausible non-conflicting numbers and one short document set.

2. **One more candidate value on an existing field (scenario 1), second priority.** Likelihood 2: a technical juror probing depth. Ease 3: the data model is already N-way per CANON's own definition of CONFLICTED, so this is one more paragraph of synthetic document text on top of F1 or F2, not new engineering. Hypothesis: about 1 sprint hour.

3. **A genuinely boring fifth field (part of scenario 4), third priority, only if time remains.** The agreement itself (D1 and D4 on F2) already exists for free and needs no build, only a rehearsed line. What is missing is a field that never enters CONFLICTED at all. Likelihood 2, ease 2. Hypothesis: about 1 to 2 sprint hours. Build this only after the second clean case above; it is a smaller, partly redundant version of the same proof once scenario 9's fixture exists.

Scenarios 2 (different format), 3 (no timestamp), 7 (duplicate), and 8 (stale quarter) are deliberately not shortlisted. Each is either genuinely more engineering than data (7 needs dedup logic, not a fixture), higher risk to rehearse under time pressure (2 needs an image asset and an untested path), or low enough likelihood that the prepared-to-describe answer already given in section 3 is the better use of the hours (3 and 8).

---

## 5. The expansion story beyond the demo

Three horizons, each a hypothesis, none a claim. FACT_CARD's own rule applies without exception: no TAM number, no time-saved number, no revenue projection stated as a forecast.

**Horizon 1: the same return, all its fields, not just the four we built.**
What would have to be true: the propose-bind-abstain treatment holds up across every field in the actual quarterly return, not only the four hand-picked ones; the four conflict causes (timing, correction, version, missing) generalize across dozens of fields without new failure modes; the risk board's deterministic rule set grows with the field count without becoming unmanageable; performance and UX hold at full field count.
What we do not claim: that we have tested this at full field count, that four fields prove forty behave the same way, or any accuracy number at that scale. We have none.

**Horizon 2: other IFSCA return types, across the entities FACT_CARD counts.**
Grounding: FACT_CARD M2, 1,147 registered entities across all IFSCA verticals; M5, eleven capital-market-intermediary categories, sixteen IBU returns, monthly returns from finance companies and lessors.
What would have to be true: the evidence-conflict pattern found in fund quarterly returns, multiple internal and external documents disagreeing, actually recurs in those other return types, not just the one we chose; the four causes would need validating against real examples from at least a sample of the other categories; pricing and buyer economics need separate validation per entity type, since deadline cadence and budget authority differ.
What we do not claim: that we have spoken to a single non-fund entity type yet, FACT_CARD K5 is explicit that we have not spoken to a practising compliance officer at all; that 1,147 is an addressable customer count today, FACT_CARD already bans TAM claims outright; any expansion revenue number.

**Horizon 3: the general case of any AI-assisted regulated workflow.**
What would have to be true: the propose, abstain, decide, confirm, seal spine is genuinely domain-agnostic rather than fund-reporting specific; maker-checker and hash-sealing port cleanly to regimes outside IFSCA and GIFT City; the legal and audit context in those other regimes gets researched fresh, since IFSCA's specific rules do not travel with the software.
What we do not claim: that we have validated anything outside GIFT IFSC; that this is a general-purpose compliance platform today rather than an architecture with a plausible next step; any platform-status claim of any kind.

---

## 6. The scenarios we refuse

Four categories, decline on stage in these words, not improvised words, because the exact wording is what keeps the refusal from sounding evasive.

**Real regulated data.** "We do not use real regulated data anywhere in this build, and we would decline it if it were offered to us on this stage. Every document you are looking at is fictional, generated from a schema we designed. That is not a limitation we are apologizing for. It is the rule the company is built on."

**Implying we file or determine compliance.** "We do not file anything, and we do not determine compliance. ATTEST sits upstream of the regulator's own reporting pipeline. The named human decides and signs. We make that decision defensible. We do not make it for them." (CANON section 11: ATTEST never integrates with, connects to, or files to anything.)

**An accuracy number we have not measured.** "I do not have a verified figure for that, and I will not invent one on this stage. We publish evaluation results on labelled synthetic sets. We claim no production accuracy until it is measured with design partners." (FACT_CARD T4 and the card's own governing rule.)

**Speculating on IFSCA's intentions.** "I cannot speak for the regulator's intentions, and I would rather say that plainly than guess. What I can tell you is what IFSCA has published." Then cite only named FACT_CARD facts (for example R1's own words on desktop storage, or R4's DRR scope), and stop there. Everything past their published words is our inference, not their position, and we label it as inference if we say it at all.

---

## Open founder decisions

**Q1.** Section 4 recommends spending an estimated 3 to 5 sprint hours (hypothesis) authoring a second clean case plus one more conflicting candidate before Friday, work that sits outside the locked BUILD_SPEC and the ranked cut list in 04 section 5. Does the founder approve this as additional pre-sprint scope, and if yes, does it happen before Friday as fixture-authoring alongside SCHEMA_PACK.md, or inside the sprint at M1 alongside fixture pack v1?
