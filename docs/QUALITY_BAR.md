# QUALITY BAR: the twelve-dimension scorecard

Status: DRAFT, built 2026-08-19. Owner: founder scores, Fable verifies, both sign. Sources: founder instruction (at least ten quality parameters, covering depth, flawlessness, credibility, efficiency, and end-to-end completeness, before anything is called done), CANON.md, FACT_CARD.md (current as of this draft), 03_STRATEGY_PLAYBOOK.md sections 1 and 7, 01_MASTER_PLAN.md, 04_CLEAN_START_BUILD_KIT.md, 06_READINESS_TRACKER.md, 05_AGENT_SYSTEM.md.

Twelve dimensions below satisfy the founder's instruction with two to spare. Used three times: end of each rehearsal build, the Saturday 11:00 code freeze, and as the definition of done for every milestone.

---

## 1. How to use this

**Who scores.** Two verifier types, matched to what each dimension actually requires. Dimensions provable by reading an artifact, a log, a manifest, a script, or one document against another (D2, D3, D4, D5, D6, D8, D9, D11) get an adversarial read from Fable, the same verification role that already attacks every war room artifact before it ships (05_AGENT_SYSTEM section 2). Dimensions provable only by watching something happen live, a run, a staged failure, a projector, a spoken explanation (D1, D7, D10, D12) get checked by whichever founder is not operating the demo at that moment, so the person driving is never the person grading. D10 splits: the founder times the spoken 60-second architecture explanation, Fable audits the AWS console evidence. If only one founder is on site (03 section 7, worst case 8), Fable substitutes for the missing non-operating-founder checks; this is a fallback, not a preference, a live human watching a live run is the better check whenever both founders are present.

**When.** The full twelve-dimension table gets filled three times: RB1 (Wed 19), RB2 (Thu 20), and the Saturday freeze gate (11:00 to 12:00, section 4 below). Between those checkpoints, at each of the six build milestones inside the Friday sprint (M1 to M6, 04_CLEAN_START_BUILD_KIT section 6), check only the dimensions in scope for that milestone against their floor, as a go/no-go gate before moving to the next milestone: M2 (live extraction) touches D10; M3 (spine closed) touches D2, D3, D6; M5 (polish, replay, failure demo) touches D1, D7, D12; M6 (pitch integration) touches D8, D11. This is lighter than the full scorecard by design; it exists so a milestone is never marked done on a feeling.

**The floor rule.** A dimension scoring below its stated floor blocks the milestone or the checkpoint it was measured at. It does not generate a note and move on. At a milestone gate: fix it before starting the next milestone, or apply the ranked cut list (04 section 5) to remove the scope that cannot meet the floor in time, never patch under pressure in a way that risks the spine. At RB1 or RB2: log it in the scorecard notes cell, and it becomes the next rehearsal's opening item, exactly like a drill topic with three FAILs (06_READINESS_TRACKER section 2). At the Saturday freeze gate specifically: a sub-floor dimension is an automatic no-go for whatever claim or screen depends on it. Fix it inside the freeze window or cut the claim from the demo path. We do not carry a known sub-floor dimension onto the pitch stage and hope.

---

## 2. The twelve dimensions

### D1 Demo integrity
Rubric tie: Technical Execution and Architecture, 30%. The rubric asks directly whether the code runs live.
Test: run the rehearsed demo path on the actual demo laptop, three consecutive times, zero manual intervention (no restarts, no console fixes, no hand-edited data) between runs, each timed against the 70-second target.
Scale: 0, does not complete one full run unaided. 1, completes once, needs an intervention to run again. 2, completes twice consecutively unaided, the third run needs help or runs meaningfully over time. 3, three consecutive unaided runs, each landing near the 70-second target.
Floor: 3.
Verifies: non-operating founder.

### D2 Evidence correctness
Rubric tie: Technical Execution and Architecture, 30%. The product's name is a claim; this dimension is whether the claim is true.
Test: for every field shown in the active fixture, open the cited source region and confirm by eye that the exact value displayed as proposed actually appears there, in both live mode and replay mode.
Scale: 0, at least one binding points to a region that does not contain the value. 1, bindings point to the right document but the region is too broad to call pinned. 2, all canonical fields bind correctly, edge cases (replay mode, any newly added fixture) unverified. 3, every field in the active fixture, live and replay, binds to a region a human reading the raw source text confirms contains the exact value.
Floor: 3.
Verifies: Fable.

### D3 Abstention correctness
Rubric tie: Problem Depth and Regulatory Realism, 20%, this is the mechanism that makes the regulatory story real, not a slide claiming it.
Test: run the fixture, confirm F1, F2, F3 reach CONFLICTED and F4 reaches UNSUPPORTED before any human input, then attempt to force a silent pick through a direct API call, bypassing the UI.
Scale: 0, any of the four fields auto-resolves or is silently picked. 1, all four abstain correctly through the UI, the API can be made to bypass abstention. 2, abstention holds through UI and direct API attempts, the eval harness does not separately score abstention as a metric. 3, abstention holds under both paths and the eval harness reports abstention correctness as an explicit scored number.
Floor: 3.
Verifies: Fable.

### D4 Determinism and replay
Rubric tie: Technical Execution and Architecture, 30%, this is the ReplayProvider design decision made real.
Test: run the same case twice through replay, diff the two outputs byte for byte, confirm zero difference; separately confirm there is a way to show this on stage.
Scale: 0, replay errors or differs. 1, replay works, not byte-identical (a timestamp or other non-deterministic field leaks through). 2, byte-identical, provable on stage only through a terminal command, not the UI. 3, byte-identical and provable through the UI's LIVE/RECORDED badge and a replay view a juror can watch.
Floor: 2. A confident terminal-run proof is still a real proof; the UI polish is the stretch goal, byte-identical output is the non-negotiable core, since that is what determinism actually means.
Verifies: Fable, with the operating founder confirming the on-stage flow works.

### D5 Integrity and tamper evidence
Rubric tie: Technical Execution and Architecture, 30%, and Problem Depth and Regulatory Realism, 20%, audit-grade evidence is the core value claim.
Test: export a sealed manifest, change one byte in a copy, re-run verification, confirm the system visibly flags the mismatch rather than passing silently or crashing without a message.
Scale: 0, tampering is not detected. 1, detected only in console or log output, nothing visible in the UI. 2, visibly flagged in the UI, message is generic. 3, visibly flagged with enough detail (which artifact, which hash) to be a credible stage moment.
Floor: 3. This is the named closing beat of the demo spine, CANON section 10; it does not get partial credit.
Verifies: Fable.

### D6 Governance enforcement
Rubric tie: Founder and Venture Assessment, 30%, and Problem Depth and Regulatory Realism, 20%.
Test: attempt, through the UI and through a direct API call, to (a) confirm a case where the confirmer is the same identity as the decider, (b) move a conflicted or unsupported field to DECIDED with an empty reason, (c) reach SIGNED with any field still conflicted or unsupported. All three must be rejected, per CANON's hard rules 2 through 4.
Scale: 0, any one bypass succeeds. 1, the UI blocks all three, at least one succeeds by direct API call. 2, both UI and API block all three, rejection messages are unclear or silent. 3, both UI and API block all three with a named, specific error explaining which rule was violated.
Floor: 3. These are the engine's own hard rules, not negotiable at any checkpoint.
Verifies: Fable.

### D7 Interface credibility
Rubric tie: Technical Execution and Architecture, 30%, and Honesty and Roadmap Credibility, 20%, an unfinished-looking screen undercuts an honest claim even when the claim itself is true.
Test: view all seven screens (S1 to S7) on the actual display hardware used for the pitch, confirm the five field states (SUPPORTED, CONFLICTED, UNSUPPORTED, DECIDED, CONFIRMED) are visually distinct wherever they appear in the demo path, run a contrast check on each screen.
Scale: 0, at least one screen visibly breaks on the real display (overlapping text, unstyled elements, missing content). 1, no breakage, but state distinctions are unclear or contrast fails somewhere. 2, states distinct and contrast passes, checked only on a laptop screen. 3, states distinct, contrast passes, verified on the actual projector or display that will be used live.
Floor: 2. Confirmed on the demo laptop with contrast tooling is the binding floor at every checkpoint; verification on the actual display hardware, achievable at the earliest at the Saturday 08:00 coach dry run (01_MASTER_PLAN Saturday schedule), is what pushes a 2 to a 3, worth chasing, not required to pass.
Verifies: non-operating founder.

### D8 Honesty surface
Rubric tie: Honesty and Roadmap Credibility, 20%, directly, this is the dimension for that criterion.
Test: enumerate every screen and every export, confirm each carries the word synthetic or equivalent labeling (CANON section 11); cross-check the README's SYNTHETIC/MOCKED/LIVE table against what the running app is actually doing at that moment, not what was true two hours earlier.
Scale: 0, at least one surface makes an unlabeled or false claim, for example a LIVE badge while running on replay. 1, all surfaces labeled, the README table and the live app state disagree at the moment checked. 2, all surfaces labeled and consistent with real app state, a banned word (FACT_CARD section 9) appears somewhere. 3, fully labeled, consistent with real app state, zero banned words, checked within the hour before freeze since app state can change up to the last commit.
Floor: 3. 01_MASTER_PLAN's own words: this table is worth up to 20% of the score by itself. Zero tolerance.
Verifies: Fable.

### D9 Regulatory realism
Rubric tie: Problem Depth and Regulatory Realism, 20%, directly.
Test: cross-check every field name, document name, timestamp and cut-off convention on screen against CANON sections 3 and 4 and FACT_CARD's regulator-sourced facts (R1 to R8, M1 to M5); confirm no invented jargon appears that is not grounded in a real IFSCA concept.
Scale: 0, at least one field or screen uses invented or incorrect terminology a domain-literate juror would flag. 1, terminology is correct, timings or cut-offs are implausible against FACT_CARD M3's 21-day deadline. 2, terminology and timings check out but have not been pressure-tested by anyone outside the two founders. 3, terminology and timings check out and have survived at least one outside read.
Floor: 2. Terminology and timings checked against CANON and FACT_CARD is the binding floor; an outside domain-literate read (the coach, per 03 section 4, is the natural venue) pushes a 2 to a 3, and should be sought whenever the coach relationship allows it, but is not required to pass.
Verifies: Fable, primary; coach read, opportunistic secondary.

### D10 Technical execution evidence
Rubric tie: Technical Execution and Architecture, 30%, this is close to the rubric's literal wording, using the provided AWS credits.
Test: check AWS console and CloudTrail for genuine API activity (Bedrock invoke, S3 put) timestamped inside the sprint window; run one live Converse call during the check itself; time a founder giving the architecture explanation cold, every AWS service named with its purpose.
Scale: 0, no verifiable AWS usage beyond static hosting, or a "live" call that is actually replayed without disclosure. 1, AWS genuinely used (S3 at minimum), Bedrock access never worked and the honesty table discloses it, no live model call demonstrable. 2, live Bedrock call works and is demonstrable, architecture explanation runs long or misses a service. 3, live Bedrock call demonstrable on demand, AWS evidence checks out, architecture explanation lands under 60 seconds naming every service and its purpose.
Floor: 2. AWS genuinely used plus a clean spoken architecture explanation is the binding floor; live, on-demand Bedrock calls push a 2 to a 3 and are the goal, but the team's own contingency plan (04 section 7, 03 worst case 2) already accepts a disclosed ReplayProvider fallback as honest, not as a failure, so a working live call is not the passing bar by itself.
Verifies: founder (spoken test) and Fable (AWS console and CloudTrail artifact audit).

### D11 Narrative coherence
Rubric tie: Honesty and Roadmap Credibility, 20%, and Founder and Venture Assessment, 30%, a founder who cannot keep the story straight reads as unfundable regardless of the code.
Test: line up the 3-minute script, the 1-minute script, the demo storyboard and the README; confirm every number, every named persona, every claimed capability appears identically across all four documents, and cross-check every spoken number against FACT_CARD's current confidence flags, not a cached memory of what the card used to say.
Scale: 0, at least one number or claim directly contradicts across documents, or a RED, do-not-say figure (for example FACT_CARD W5b, the disputed 45% agentic-AI figure) appears anywhere in a script. 1, numbers agree, but at least one script still carries a figure FACT_CARD has since revised or hedged differently. 2, fully consistent and current apart from wording appropriate to each format. 3, fully consistent, current as of the most recent FACT_CARD edit, and every number across all four documents traces to a live FACT_CARD row.
Floor: 3. Zero tolerance. FACT_CARD's own founder-action log already names one figure (W5b) as "the single most expensive error available to us" if said in the wrong direction, in front of the regulator that published it.
Verifies: Fable.

### D12 Recoverability
Rubric tie: Founder and Venture Assessment, 30%, composure under pressure reads as founder quality, and Technical Execution, contingency engineering is part of architecture.
Test: for each of the 12 worst-case rows in 03_STRATEGY_PLAYBOOK section 7, stage the actual failure unannounced during a rehearsal (kill wifi, close the lid, raise a hostile git-audit question) and time the response against the pre-decided line.
Scale: 0, frozen or a response that contradicts the pre-decided line, on any staged failure. 1, responds within 5 seconds, drifts from the pre-decided script in a way that risks a new honesty gap. 2, correctly and promptly handles at least 9 of 12 rows staged. 3, correctly and promptly handles all 12, including at least one staged without warning.
Floor: 2, meaning at least 9 of 12 worst-case rows handled correctly and within 5 seconds when staged cold. All 12 is the target for 3 and worth pushing for at the freeze gate specifically, since Saturday is the only day it is tested for real.
Verifies: non-operating founder stages the failure; roles rotate between rehearsals so both founders practice both staging and responding.

---

## 3. The rehearsal scorecard

| Dimension | Floor | RB1 Wed Score | RB1 Notes | RB2 Thu Score | RB2 Notes | Freeze Score | Freeze Notes |
|---|---|---|---|---|---|---|---|
| D1 Demo integrity | 3 | | | | | | |
| D2 Evidence correctness | 3 | | | | | | |
| D3 Abstention correctness | 3 | | | | | | |
| D4 Determinism and replay | 2 | | | | | | |
| D5 Integrity and tamper evidence | 3 | | | | | | |
| D6 Governance enforcement | 3 | | | | | | |
| D7 Interface credibility | 2 | | | | | | |
| D8 Honesty surface | 3 | | | | | | |
| D9 Regulatory realism | 2 | | | | | | |
| D10 Technical execution evidence | 2 | | | | | | |
| D11 Narrative coherence | 3 | | | | | | |
| D12 Recoverability | 2 | | | | | | |

---

## 4. The freeze gate

The exact checklist, run 11:00 to 12:00 Saturday, ending in go or no-go.

1. Stop all feature work. Announce freeze verbally to both founders and any active agent session; no new commits except fixes identified in this checklist.
2. Run the full twelve-dimension scorecard if not already refreshed in the 09:00 to 11:00 window; confirm every dimension meets its floor. Any sub-floor dimension goes to step 3.
3. For any dimension below floor, apply the ranked cut list (04 section 5) rather than attempting new feature work under time pressure: cut scope to protect the floor, never patch in a way that risks the spine.
4. Git history read-back: read the full commit log top to bottom, out loud, the way a juror auditing it would. Confirm the first commit is the docs and NOTICE.md commit, confirm messages follow the `M<milestone>: what [by <human>]` convention, confirm no timestamps before 14:00 Friday, confirm author identity is correct on both machines.
5. Confirm milestone tags M1 through M6 exist and point at the right commits.
6. README honesty table verification: read the SYNTHETIC/MOCKED/LIVE table line by line against the current running state of the app, not what was true two hours ago. Fix any drift immediately, for example if Bedrock died at hour 19 and the app is now on ReplayProvider, the table and the on-screen badges must say RECORDED.
7. Sweep every screen, every export, every pitch script, and the README for the word synthetic where required, for any banned word (FACT_CARD section 9), and for em dashes.
8. FACT_CARD sweep: grep every pitch script, the README and the one-pager for any figure FACT_CARD currently flags RED, and specifically for the disputed W5b agentic-AI phrasing in either direction. Confirm zero matches, or that a match is an approved safe substitute (for example W5c's framing). Repeat this exact grep at every checkpoint, not just once, since FACT_CARD can change between rehearsals.
9. Confirm the demo path (per DEMO_STORYBOARD once built) has been rehearsed 3 times consecutively today on the exact laptop and display that will be used live (D1 check).
10. Capture the recorded backup: screen-record one full clean run of the demo end to end on the exact setup, label the file clearly, confirm it plays back, confirm both founders know how to trigger it within 5 seconds if live fails.
11. Tag the final commit and push everything to the remote so it survives a laptop failure.
12. Run D5 (tamper check) and D6 (governance bypass attempts) one final time against the frozen, pushed code, not a local-only copy, to confirm what is actually running behaves correctly.
13. Both founders independently state go or no-go. Go requires unanimous agreement and zero dimensions below floor. Disagreement or any sub-floor dimension is automatically no-go for that claim or screen: fix or cut, never override.
14. Record the go/no-go decision and timestamp in the readiness tracker (doc 06) or an equivalent freeze log, with any cuts made noted.

---

## 5. The five defects that would cost us the most

Ranked, opinionated on purpose.

**1. A silent pick disguised as a proposal.** This is the single failure that falsifies the product's entire reason for existing, in the exact moment jurors are watching, with no recovery possible inside a live demo whose whole pitch is "we never do that." Early warning sign: in rehearsal, a field reaches DECIDED, or shows one confident value, without ever visibly passing through CONFLICTED or UNSUPPORTED first. Rehearsal check: D3's test, run before every rehearsal begins, not only at the end.

**2. Speaking a disputed statistic in the wrong direction.** FACT_CARD W5b flags this explicitly, our own internal documents currently render a figure as "45% exploring agentic AI" while a re-checked secondary source renders it as the opposite, and the card's own words call this "the single most expensive error available to us" if said backwards, in front of the regulator that published the survey. Unlike a technical glitch, this is a fully avoidable, self-inflicted error: the fix is silence until F4 resolves it, not a rebuild. Early warning sign: any rehearsal run where a founder states a specific agentic-adoption percentage in either direction, or any script still carrying the uncorrected phrasing. Rehearsal check: D11's test, plus the literal grep in freeze-gate step 8, run before every rehearsal, not only at freeze.

**3. Evidence binding that is wrong or fuzzy.** If a value shown as proposed from a source does not actually appear in the pinned region, and a technical juror checks it live, plausible given the 30% technical-execution weight and a likely domain-literate jury, the product's own name is falsified live. Early warning sign: any binding region that requires the viewer to trust the claim rather than visibly read the cited number. Rehearsal check: D2's test, done by a reader who does not already know the answer, on every field, in both live and replay mode.

**4. A governance bypass that survives in the API even though the UI blocks it.** A technical judge exploring "core track requirements" may poke the API directly. If maker-checker can be defeated by calling the decide and signoff endpoints directly as the same user, the entire accountability claim is theater, not engineering. Early warning sign: validation logic that lives only in frontend code, not in backend route handlers. Rehearsal check: D6's test, done with raw HTTP calls, not only by clicking through the UI.

**5. A live demo failure with a slow or undisclosed recovery.** The failure itself is expected and already planned for (03 section 7, worst case 5). The cost is a fumbling or undisclosed recovery: it wastes seconds in a Q&A-scored round, and if undisclosed, becomes a live-caught honesty violation worse than the original glitch. Early warning sign: a rehearsal plan that only ever practices the happy path and never rehearses the failure-to-recording switch itself. Rehearsal check: D12's staged, unannounced failure drill.

---

## Open founder decisions

**Q1.** Section 2 sets a passing floor of 2, not 3, for five dimensions: D4 (byte-identical replay without requiring UI polish), D7 (laptop-verified contrast without requiring projector verification), D9 (terminology checked internally without requiring an outside domain-literate read), D10 (AWS genuinely used and explainable without requiring a live Bedrock call on demand), and D12 (9 of 12 worst-case rows handled, not all 12). This keeps them achievable inside the 22-hour build. Does the founder accept these five as the real bar, or raise any of them to 3 given what is riding on Saturday?

---

## Founder-side adjudication of the two open decisions (Fable, 2026-08-19)

### The five floors set at 2 rather than 3

**Decision: raise D9 and D12 to a floor of 3. Leave D4, D7 and D10 at 2.**

The right way to split these is not by how much they matter. All five matter. It is by which currency they consume.

| Dimension | Currency it spends | Call |
|---|---|---|
| D9 Regulatory realism | Preparation time, which we have | **Raise to 3.** Field names, document types, timings and vocabulary cost zero sprint hours. They are already fixed in CANON and SCHEMA_PACK. This is 20% of the rubric available for the price of getting our own words right, and a domain-literate juror detects a wrong word instantly |
| D12 Recoverability | Rehearsal time, which we have | **Raise to 3.** Every failure response is a rehearsal, not a build. A demo that breaks and recovers in five seconds reads as preparedness and can score better than one that never breaks. A demo that breaks and flounders is fatal. The gap between those two outcomes is one afternoon of drilling |
| D4 Determinism and replay | Sprint hours, scarce | Hold at 2 |
| D7 Interface credibility | Sprint hours, scarce | Hold at 2 |
| D10 Technical execution evidence | Sprint hours plus event dependencies outside our control | Hold at 2 |

The principle to carry into Friday: anything that can be bought with preparation gets a floor of 3, because preparation is the resource we still have and sprint hours are the one we do not.

### The second case, and a correction to how it was costed

**Decision: approved, and it is not 3 to 5 sprint hours.**

The estimate treats this as build work. It is not. Authoring a second case is specification work, and specification is legal to do before Friday and costs zero sprint time. Once SCHEMA_PACK describes a second case, the generator that gets written at M1 emits it from the same rules with different parameters. Marginal sprint cost is closer to 20 to 30 minutes, almost all of it verification rather than authoring.

Priority within that: the clean case with no conflicts is the one that must exist. A juror asking "show me a normal one, where nothing is wrong" and hearing that we only built the exception path is a bad moment, and it is the single cheapest scenario to cover. The extra conflicting candidate is second priority and genuinely cuttable.

Action: SCHEMA_PACK carries a second case as a named deliverable, marked as generated at M1 from the same rules. If SCHEMA_PACK as drafted does not include it, that is the one addition to make before the spec is locked.
