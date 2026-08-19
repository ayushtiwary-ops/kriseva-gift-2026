# 00. MASTER PLAN: the 62 hours from now to the sprint

Status: STABLE. Written 2026-08-18 23:40 IST by Fable. Owner: founder. This supersedes nothing in war room doc 01; it sits on top of it and adds the pre-build doctrine, the AWS pre-warm, and the Track B discovery plan.

Clock check. Right now is Tuesday 18 August, 23:40 IST. The sprint starts Friday 21 August at 14:00. That is **62 hours**, of which roughly 20 are sleep and 6 are travel. Call it **36 working hours** before the prompt is even released.

---

## 1. The decision: what "90 percent built beforehand" actually means

Here is what I would actually do.

The instruction is that 90 percent of the product exists before we walk in, and that Friday is assembly. That instruction is correct, and it is achievable, with one substitution: **the 90 percent is not source code.**

The brief says it in one line: *"No pre-built repositories allowed. Code must start clean at 2:00 PM on Friday, 21 August. Git commit histories will be audited."* [Brief p.3]. Bringing code costs us the 20 percent honesty criterion, risks disqualification, and would be a strange way for an evidence-integrity company to win an audit.

So look at what actually consumes a 22-hour sprint. Writing the code is not the bottleneck. The bottleneck is deciding what to build, arguing about the data model, inventing test data at 2am, discovering AWS access is not granted at hour 12, designing screens while tired, and writing a pitch after the build. Every one of those is legal to eliminate in advance, and every one of them is what separates the teams that ship at hour 20 from the teams that ship at hour 40.

**The split, itemised:**

| Component | Pre-built by Thursday night | Built Friday |
|---|---|---|
| Problem, buyer, persona, emotional arc | 100% | none |
| Data model, state machine, JSON schemas | 100% | none |
| Synthetic data design and conflict matrix | 100% (the plan) | the generator, in 45 min |
| Eval labels and scoring protocol | 100% (the spec) | the harness |
| Screen designs, tokens, motion, copy | 100% | the markup |
| Prompt chain that generates each module | 100% | fired in sequence |
| AWS account, CLI, profiles, model access proof | 100% on our account | event account wiring |
| Pitch, demo choreography, Q&A, one-pager | 100% | rehearsal only |
| Application source code | **0%, deliberately** | 100%, clean, audited |

That is the honest 90 percent, and it is a bigger 90 percent than smuggled code would have been. A team that arrives with code still has to design the pitch, still has to invent test data that survives a domain-literate juror, and still has to explain a commit history that starts at 40,000 lines. We arrive with everything except the part that is banned, and the audited history becomes a selling point rather than a liability.

**The line I will not cross, and neither should we:** no code files, no cloned repo, no pasted source, no private fork, no reconstructing the public ATTEST prototype from memory into Friday's repo. Rehearsal code gets deleted. We keep timings and lessons, never bytes.

---

## 2. What we are actually optimising

Not "a working demo". Roughly 50 teams will have a working demo. The rubric is 30 percent technical, 30 percent founder, 20 percent problem depth, 20 percent honesty, and the organisers wrote that they are looking for founders they can back.

The pattern to beat: most teams will show a product that works on data they invented to make it work, and will answer hard questions with confident guesses. We win by being the only team in the room whose every claim survives being checked, whose demo shows the product **refusing** to answer, and whose founders say "we have talked to zero customers, here is exactly how we fix that" without flinching.

**The undeniability is built out of verifiability, not out of polish.** Polish gets us into the conversation. Checkability wins it. That is why the fact card exists and why every number on it carries a confidence flag.

The one asymmetry we own: our product's entire thesis is that a system should refuse to answer when it cannot prove the answer. If our pitch invents a number, we have refuted ourselves on stage. Conversely, every time we decline to claim something, we are demonstrating the product. That is a rare alignment between honesty and self-interest, and we should lean on it hard.

---

## 3. The 62 hours, block by block

### Tonight, Tuesday 18 August, remaining hours
| # | Block | Owner | Done-check |
|---|---|---|---|
| T1 | Attendance form submitted if not already done, per doc 07 | Founder | Screenshot in `receipts/` |
| T2 | Reconcile the Member 2 naming inconsistency (docs 00/01/07 say Sony, docs 08/10 and APPLICATION_UPDATE_BANK say Mahek) | Founder | One name written into doc 07 |
| T3 | Answer the Readiness Round 1 questions, doc 06 section 3 | Both | Written answers in doc 06 |
| T4 | Book Thursday travel and Thursday-night hotel | Founder | Confirmations saved |
| T5 | Sleep 7 hours | Both | Non-negotiable, Friday is a 22-hour day |

### Wednesday 19 August: rehearsal build 1 and the money questions
| Time | Block | Owner |
|---|---|---|
| 08:30-09:30 | Money questions out loud: unit economics, pricing, the labour-arithmetic attack, the moat sentence | Founder |
| 10:00-20:00 | **Rehearsal build 1.** Ten hours, fresh empty throwaway repo, only the factory documents open. Target: reach M3 equivalent (live extraction, conflict, decision, manifest exporting, three screens). Log every milestone time | Both |
| 20:00-20:45 | Retro. Log timings and the top three stalls into doc 06. Update the prompt playbook where it stalled | Founder + Fable |
| 20:45-21:15 | Q&A drill, money questions only, Member 2 firing | Both |
| 21:15 | **Delete the rehearsal code.** All of it. Keep only timings and lessons | Founder |

Rehearsal rule that matters more than any other: **the conductor does not type.** If a founder writes code by hand for more than ten minutes, that is a routing failure. Re-prompt instead. Friday's speed comes from prompt quality, and Wednesday is where prompt quality gets tested.

### Thursday 20 August: sharpen, pre-warm, travel
| Time | Block | Owner |
|---|---|---|
| 09:30-13:30 | **Rehearsal build 2**, scoped to only the segments that stalled Wednesday. Usually AWS wiring and the eval harness. Delete after | Both |
| 09:30-13:30 | In parallel: print the factory pack, run the fact card verification actions F1 to F4 | Member 2 |
| 14:00-15:00 | Pitch dress rehearsal. Two full 3-minute runs, one 1-minute run, one solo run each, timer visible. Then **freeze the scripts** | Both |
| 15:00-15:45 | The gauntlet. Twelve hostile questions from QA_REDTEAM, no invented numbers, every answer under 45 seconds | Both |
| 16:00-17:00 | **AWS pre-warm** on Kriseva's own account, per AWS_RUNBOOK section 1. Both laptops. Prove one live model call end to end | Founder |
| 17:00-18:00 | Pack per LOGISTICS. Environment checklist on both machines | Both |
| 18:00 onward | Travel. Hotel within 15 minutes of the venue. Sleep 7 hours | Both |

### Friday 21 August: the day
| Time | Block | Note |
|---|---|---|
| 06:30-08:30 | Morning timeline per LOGISTICS section 7 | Buffer built in |
| 08:30 | Report, badge, **claim seating near power** with the extension cable | Do this before anything else |
| 10:00-11:00 | **Prompt release.** Both founders write it down verbatim. Run the pivot matrix in USE_CASE_MATRIX | Decision locked by 11:00 |
| 11:00-12:00 | **AWS briefing.** Work the nine questions in AWS_RUNBOOK section 2. Get model access confirmed in the room and run one Converse call before leaving it | This hour decides whether hour 12 is calm or fatal |
| 12:00-13:00 | Coach assignment. Hand the one-pager, ask the three questions, book Saturday 08:00 for a dry run | |
| 13:00-14:00 | Lunch, final task board, both laptops on power | |
| 14:00 | **Sprint starts.** M1 through M6 per BUILD_SPEC section 0 and PROMPT_PLAYBOOK | |

Nap discipline: one founder 02:00 to 04:30, the other 04:30 to 07:00. The awake founder reviews and commits agent output. Heroic zero-sleep loses a 30 percent founder assessment at 14:00 Saturday.

---

## 4. The AWS decision, and it matters more than it looks

We hold our own AWS account with USD 1,100 in credits, and Bedrock access there is currently granted for Sonnet-class Claude models only. A request for larger frontier models is with AWS and may not land before Friday.

**Recommendation: build on the event-provided account, keep ours as a pre-warmed hot standby.**

The reason is one line of rubric text: *"Met core track requirements using provided AWS credits?"* [Brief p.5]. Building the whole thing on our own account and mentioning it on stage invites a juror to ask why we did not use what was provided, and the honest answer would be weak. Use theirs. Ours exists so that if their credits are late or their Bedrock access is refused, we are running inside ten minutes instead of dead.

**Two consequences to design around now:**

1. **The demo must be excellent on a Sonnet-class model.** Do not build anything that depends on a larger model arriving. If the bigger models land, the demo gets better. If they do not, nothing changes. This is a design constraint, not a hope.
2. **Prove the call path on Thursday, on our own account.** Then Friday's only unknown is credentials, which is a two-minute problem rather than a two-hour one.

Never say "AWS partnership". We hold startup credits.

---

## 5. Track B: the reason this is worth more than the trophy

The falsification gate in PRODUCT_DECISION.md requires at least five workflow conversations: two accountable FME officers, two fund administrators, one independent compliance provider. Today we have **zero**. That is the single biggest hole in the company thesis and it is stated openly on the fact card.

For two days, we will be in a building full of exactly those people, plus coaches selected for industry experience, plus jurors, plus AWS staff, plus roughly 50 other teams who are future GIFT City cohort-mates and possible design partners.

**Target: leave Saturday with 10 named contacts, each with a specific next step, and at least 2 of them able to answer workflow questions about fund reporting.** That is a harder target than the trophy and it survives any judging outcome.

Rules while doing it: no confidential data collected, no claims beyond the synthetic prototype, no implying customer status to anyone. Ask about their workflow, not about our product. The best question we can ask a compliance person is not "would you buy this". It is "walk me through the last quarter-end close".

Sequencing gate, stated plainly: this week displaces the Eureka follow-ups and the content cadence through Saturday 22 August. That is accepted and it reverses on Sunday.

---

## 6. Risk register, updated tonight

| # | Risk | Pre-decided response | Owner |
|---|---|---|---|
| 1 | Released prompt does not fit ATTEST | Pivot matrix in USE_CASE_MATRIX, decision by 11:00, spine never changes | Founder |
| 2 | Event Bedrock access refused or delayed | Build against the provider abstraction, swap when access lands, our own account as standby, Replay provider as final fallback with an honest on-stage disclosure | Founder |
| 3 | We overclaim under pressure in Q&A | The fact card is the only permitted source of numbers. The standing sentence: "I do not have a verified figure for that, and I will not invent one" | Both |
| 4 | Demo breaks on stage | Five-second switch to the recorded backup, announced as a recording | Member 2 |
| 5 | Git audit challenges our speed | Show the commit cadence, the agent tooling used openly, the public pre-event prototype we did not copy from, and offer a live change on request | Founder |
| 6 | The 251 versus 152 test-count discrepancy in our own documents | Fact card action F2. Run the suite, count, or say "an automated check suite" with no number | Founder, Thursday |
| 7 | Wifi fails | Both phone hotspots tested Thursday, offline deterministic replay in the demo | Both |
| 8 | Fatigue destroys the Saturday pitch | Enforced nap windows, code freeze at 11:00 Saturday with no exceptions | Both |

---

## 7. The one thing that would most change the outcome

If one practising IFSC compliance officer speaks to us before Saturday, every founder-criterion answer changes from reconstructed to observed. The fact-check pack made this same point on 12 August and it is still the highest-value unclaimed item on the board. LinkedIn, the venue itself, or an introduction through a coach on Friday afternoon. Fifteen minutes is enough.

---

## 8. Standing rules for the week

- Fable decides, architects and verifies. Sonnet and Haiku agents draft and generate. Excellence comes from routing, not from lowering the bar.
- Nothing ships on first draft. Every artifact gets an adversarial pass before it is marked DONE.
- No real tender, bidder, customer or personal data anywhere near this event.
- Every claim traces to a source or carries an explicit hypothesis label.
- Status labels are DONE, PARTIAL, BLOCKED. Never "should be fine".

**Next move:** run rehearsal build 1 on Wednesday at 10:00 with the factory pack as the only open documents. The trade-off is a full working day spent on code that gets deleted, and it is worth it, because the timings from that day are the only honest evidence we will have about whether the 22-hour plan is real.
