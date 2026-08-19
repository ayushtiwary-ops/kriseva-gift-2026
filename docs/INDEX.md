# INDEX: status of the GIFT hackathon resource factory

Status table for the pre-hackathon artifact set, generated 2026-08-19.

---

## 1. Status table

| Artifact | What it is | Size (KB) | Status | Last updated |
|----------|-----------|-----------|--------|--------------|
| [00_MASTER_PLAN_72H.md](00_MASTER_PLAN_72H.md) | 72-hour build sequence, roles, AWS pre-warm, Track B discovery | 13.1 | DONE | 2026-08-18 23:47 |
| [CANON.md](CANON.md) | Fixed demo case details, entity data, four field specs, product language | 11.1 | PARTIAL | 2026-08-19 00:41 |
| [FACT_CARD.md](FACT_CARD.md) | Verified facts and assumptions, pricing hypothesis, regulatory context | 21.1 | DONE | 2026-08-19 00:24 |
| [QUALITY_BAR.md](QUALITY_BAR.md) | 12 quality dimensions with measured floors, adjudication of D9 and D12 | 24.7 | DONE | 2026-08-19 00:28 |
| [REPO_FIRST_COMMIT_PACK.md](REPO_FIRST_COMMIT_PACK.md) | First commit structure, honesty table, six milestone tags, six open decisions | 9.8 | PARTIAL | 2026-08-18 23:49 |
| [AWS_RUNBOOK.md](AWS_RUNBOOK.md) | Console commands, budget setup, credit placeholders, spend approval mechanism | 33.5 | PARTIAL | 2026-08-18 23:55 |
| [LOGISTICS.md](LOGISTICS.md) | Transportation, hotels, meal budget, timing, five founder input fields | 24.5 | PARTIAL | 2026-08-18 23:55 |
| [ONE_PAGER.md](ONE_PAGER.md) | Printed pitch summary, team line, contact footer placeholder | 3.6 | PARTIAL | 2026-08-19 00:45 |
| [PERSONA_AND_JOURNEY.md](PERSONA_AND_JOURNEY.md) | Buyer archetype, three adjudicated decisions, stage language guidance | 29.9 | DONE | 2026-08-19 00:59 |
| [PITCH_1MIN.md](PITCH_1MIN.md) | One-minute grand jury pitch, three hooks, Round One callback adjudication | 7.5 | PARTIAL | 2026-08-19 00:50 |
| [PITCH_3MIN.md](PITCH_3MIN.md) | Three-minute demo pitch, pricing caveat adjudication, 15-second sections | 17.6 | PARTIAL | 2026-08-19 00:50 |
| [DEMO_STORYBOARD.md](DEMO_STORYBOARD.md) | 70-second demo sequence by shot, narration and maker-checker adjudications | 20.7 | PARTIAL | 2026-08-19 00:50 |
| [BUILD_SPEC_v1.md](BUILD_SPEC_v1.md) | Generator, fixture corpus, quality checks, schema and storyboard ownership | 74.1 | PARTIAL | 2026-08-19 00:11 |
| [SCHEMA_PACK.md](SCHEMA_PACK.md) | Case definition, four document templates, second case definition and adjudication | 57.6 | DONE | 2026-08-19 00:41 |
| [UX_PSYCHOLOGY_SPEC.md](UX_PSYCHOLOGY_SPEC.md) | Interaction design, layout principles, proof-point bindings for each field | 62.1 | DONE | 2026-08-19 00:03 |
| [QA_REDTEAM.md](QA_REDTEAM.md) | Red team questions, claim receipts, proofing evidence, case credibility checks | 55.8 | DONE | 2026-08-19 00:25 |
| [USE_CASE_MATRIX.md](USE_CASE_MATRIX.md) | Q&A bank, four use case scenarios with founder response frameworks | 28.7 | DONE | 2026-08-19 00:23 |
| [UI_LANGUAGE_AND_VISUALS_SPEC.md](UI_LANGUAGE_AND_VISUALS_SPEC.md) | Plain-language mapping, the glossary, every visual algorithm, the filing history model, and the defects found by using the build | 23.3 | DONE | 2026-08-19 14:30 |
| [NEXT_SESSION_PROMPT.md](NEXT_SESSION_PROMPT.md) | Paste this into a new chat to continue. Self-contained: calendar, resource rule, verified state, open items, next steps | 8.3 | DONE | 2026-08-19 17:40 |
| [RUNNING_COST_AND_LIMITS.md](RUNNING_COST_AND_LIMITS.md) | Measured rate limits per model, tokens per case, what broke on the live path and why, and the honest version to say to a juror | 8.1 | DONE | 2026-08-19 17:10 |
| [SESSION_HANDOVER_2026-08-19.md](SESSION_HANDOVER_2026-08-19.md) | Read first. What changed on 19 Aug, the gates, what travels Thursday, and what was deliberately not done | 7.2 | DONE | 2026-08-19 15:05 |
| [DEFECT_LEDGER_2026-08-19.md](DEFECT_LEDGER_2026-08-19.md) | Eight defects found by using the build rather than reading it, what each would have cost on stage, and the codified rule | 6.6 | DONE | 2026-08-19 22:20 |
| [AGENT_CONTRACT_PACK.md](AGENT_CONTRACT_PACK.md) | **Carry pack.** The five live agent prompts verbatim, the validator contracts that are the real rules, model routing and why, measured transport constants, and the Friday rebuild order. Everything that existed only in code | 27.4 | DONE | 2026-08-19 22:10 |
| [MEASURED_RESULTS.md](MEASURED_RESULTS.md) | Every measured number with its exact scope: 24 of 24 planted archetypes, zero silent picks, the baseline comparison that went against our prediction, and the four things none of it proves | 10.4 | DONE | 2026-08-19 22:15 |
| [JURY_QA_PACK.md](JURY_QA_PACK.md) | The synthetic-data provenance answers the founder asked for, plus Q&A on every surface built after QA_REDTEAM was written | 18.3 | DONE | 2026-08-19 22:18 |
| [PROMPT_PLAYBOOK.md](PROMPT_PLAYBOOK.md) | Ordered agent prompts for 22-hour build, M1-M6 milestones, commit naming | 74.3 | PARTIAL | 2026-08-19 00:42 |

**Subtotals:** DONE: 7 artifacts | PARTIAL: 11 artifacts

---

## 2. Open founder decisions, consolidated and deduplicated

Twenty-one raw entries were extracted from the artifacts. After removing duplicates of the same question and items already resolved, the real list is below. Five artifacts each raised the second-founder name; that is one decision, not five.

### A. Blocking, must close before Thursday 20 August

| # | Decision | Why it blocks | Source |
|---|---|---|---|
| A1 | **The second founder is Mahek Soni (RESOLVED 2026-08-19 by the founder).** | Highest-leverage single item here. It is typed into the attendance form, the badge, the hotel booking, the printed one-pager that jurors keep, the pitch cue cards, and every `[by <name>]` commit in an audited git history. Five artifacts carry a placeholder waiting on it | CANON, LOGISTICS, ONE_PAGER, PITCH_3MIN, PROMPT_PLAYBOOK |
| A2 | **Settle the 45% agentic-AI direction, or leave it unsaid** | Our own documents say "45% exploring agentic AI"; the re-checked source says "45% are not yet exploring". Opposite claims about the survey published by the regulator in the room. Currently marked unsayable. Also requires correcting the three war room docs that carry the disputed phrasing, so it is not memorised and then spoken | FACT_CARD W5b, F4, F4b |
| A3 | **Origin city for travel** | Nothing in LOGISTICS can be booked without it, and it is Tuesday night | LOGISTICS |
| A4 | **Repo licence, and whether the sprint repo is public during the event** | Goes into the first commit. Recommendation on the second part: public, because the commit history is the honesty argument and a juror who can check it live is worth more than a tidy private repo | REPO_FIRST_COMMIT_PACK |
| A5 | **Overnight AWS spend ceiling and who approves it** | Needs deciding while both founders are awake, not at 03:00 | AWS_RUNBOOK |

### B. Small, but close them Thursday

| # | Decision | Source |
|---|---|---|
| B1 | Saturday night: book a flexible hold now, or decide Saturday afternoon | LOGISTICS |
| B2 | Who physically holds and photographs receipts across both days | LOGISTICS |
| B3 | Which contact goes in the printed one-pager footer: phone, email, or both | ONE_PAGER |
| B4 | Confirm the exact public pre-event repo URL to name in NOTICE.md, and verify the link is live | REPO_FIRST_COMMIT_PACK |
| B5 | Run `npm test` once on the public ATTEST repo to confirm the suite still reports 251. Until then the safe phrasing is "over 150 automated checks" | FACT_CARD F2 |

### C. Not decisions. Questions to ask at the venue

| # | Question | Who to ask |
|---|---|---|
| C1 | Is the event AWS account dedicated to us or shared across teams | AWS staff, 11:00 briefing |
| C2 | Do the FinTech Incentive Scheme grant amounts survive the 16 March 2026 Sandbox Framework | Programme staff |
| C3 | Is the Top 3 prize the Innovation Sandbox or the FinTech Sandbox? They are different things under the 2026 framework | Programme staff |
| C4 | Does the grand jury see Round One scoring notes, and is any artifact of ours in front of them in Round Two | Programme staff |

### D. Already resolved, listed so they are not reopened

| Item | Resolution |
|---|---|
| Three fields or four | Four. The unsupported state is the strongest single screen and costs one label. Built as four throughout |
| Currency shown as USD or INR | USD. GIFT IFSC funds are USD denominated and it reads as domain fluency |
| Who writes SCHEMA_PACK and DEMO_STORYBOARD | Both written and verified. The question was raised while they were still drafting |
| Who narrates the demo | Adjudicated: the founder narrates, Member 2 drives and delivers the honesty beat. Contradicts doc 10, so run both once on Wednesday and freeze that night |
| DRR contract value | Closed. Primary award notice retrieved, read and saved to `receipts/`. Now quotable |
| The 152 versus 251 test count | Closed. 154 unit plus 97 browser. The 152 was an earlier snapshot |

## 3. Decisions already adjudicated

1. DEMO_STORYBOARD.md (2 adjudications): narration assignment, maker-checker switch
2. PERSONA_AND_JOURNEY.md (3 adjudications): fabrication moment placement, shared names flagging, one-person compliance claim
3. PITCH_1MIN.md (1 adjudication): Round One callback rewrite
4. PITCH_3MIN.md (1 adjudication): pricing caveat placement
5. QUALITY_BAR.md (2 adjudications): five dimension floors, second case costing
6. SCHEMA_PACK.md (1 adjudication): second scheme decision, build clean case instead

---

## 4. Reading order

1. 00_MASTER_PLAN_72H.md: Founder owns the 72-hour sequence and AWS pre-warm
2. FACT_CARD.md: All numbers and claims trace here, all other artifacts depend on it
3. CANON.md: Demo entity and field definitions locked; three unresolved questions at the boundary
4. PERSONA_AND_JOURNEY.md: Buyer context and three adjudicated decisions on stage language
5. PITCH_3MIN.md: Full demo pitch with pricing caveat already resolved
6. PITCH_1MIN.md: Grand jury pitch with Round One callback adjudication
7. DEMO_STORYBOARD.md: 70-second sequence with narration and maker-checker settled
8. ONE_PAGER.md: Printed handout, two founder decisions on name and contact
9. QA_REDTEAM.md: Red team questions and proofing evidence, no open decisions
10. USE_CASE_MATRIX.md: Four use case scenarios and Q&A bank, no open decisions
11. BUILD_SPEC_v1.md: Generator and fixture specs; one question on ownership and timing
12. SCHEMA_PACK.md: Case definition and second case adjudication; clean case now specified
13. UX_PSYCHOLOGY_SPEC.md: Interaction design and proof-point bindings, no open decisions
14. PROMPT_PLAYBOOK.md: Agent prompts and milestone tags; one naming decision pending
15. AWS_RUNBOOK.md: Console commands and budget setup; two spend decisions open
16. REPO_FIRST_COMMIT_PACK.md: Commit structure and honesty table; three repo decisions open
17. QUALITY_BAR.md: 12 quality floors and two adjudications on dimensions and second case
18. LOGISTICS.md: Transportation, hotels, timing; five founder input fields and name decision

---

## 5. Totals

- Total artifacts: 18
- Total size: 507.1 KB
- DONE: 7
- PARTIAL: 11
- Total unresolved open founder decisions: 21
