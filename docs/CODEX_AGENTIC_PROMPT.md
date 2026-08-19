# CODEX WORK ORDER: the agent reliability lane

Paste everything below the line into Codex, in a terminal at `~/kriseva-rehearsal-DELETE-BEFORE-21AUG/attest`.

**Why this split.** My Sonnet agents build the orchestrator and the specialist agents. Codex builds the things that prove the multi-agent system actually holds together, plus the improvement loop. Different files, no collisions. And the same logic as last time applies: the team that builds a system should not be the only team testing it, and Codex already found a real integrity hole in our hash chain by disagreeing with us.

---

## THE PROMPT

You are working in a rehearsal build of KRISEVA ATTEST at `~/kriseva-rehearsal-DELETE-BEFORE-21AUG/attest`. This directory is deleted before 21 August. Nothing here goes to the venue.

Read `docs/CONTRACT.md` in full first, including section 9. Then read `/Users/aloo/KRISEVA_AI/10_GIFT_CITY/12_HACKATHON_WARROOM/factory/AGENTIC_BUILD_PLAN.md` sections 1, 2 and 3. Those define the nine agents and the reliability requirements you are testing.

Other agents are building `src/orchestrator.js`, `src/agents/*.js`, `src/engine.js`, `src/providers.js`, `src/server.js` and `public/*` right now. **You own exactly these files and no others:**

- `src/lesson-ledger.js`
- `src/agent-trace-cli.js`
- `tests/agent-boundary.test.js`
- `tests/agent-reliability.test.js`
- `tests/trajectory.test.js`
- `scripts/agent-check.sh`
- `docs/AGENT_RUNBOOK.md`

If something you depend on does not exist yet, code against the contract, retry, and say so in your report. Never create another lane's file, not even as a stub.

Node 25, ES modules, zero npm dependencies, Node standard library only.

Build these seven things, in this order.

### 1. `tests/agent-boundary.test.js`, the tests that matter most

The product's central safety claim is that **no agent can decide anything**. Every state transition to `DECIDED`, `ATTESTED`, `CONFIRMED`, `CONFIRMED_UNSOURCED` or `SIGNED` requires a named human through the API. Prove this cannot be bypassed. Write tests that actively try to break it:

- an agent output that claims a field is DECIDED must not move the field
- an orchestrator plan that includes a decide step must be rejected
- a critic or extractor returning a payload shaped like a human decision must not be honoured
- an agent cannot sign off, cannot confirm, and cannot seal a case
- an agent cannot mark a conflicted field resolved by any route
- the maker-checker rule still holds when the decider's name arrives from an agent-produced field rather than typed by a human

For each, assert both that the attempt fails AND that the rejection message explains why in plain English. A silent rejection is a half-failure because the message appears on screen.

### 2. `tests/agent-reliability.test.js`, the failure modes

Section 2 of the build plan lists seven failure modes with mitigations. Test that each mitigation actually holds:

- a malformed agent response triggers a bounded retry and then a recorded failure, never a silent pass-through of garbage
- the retry cap is real: an agent that always returns malformed output does not loop forever
- the re-plan cap is real
- a wall-clock budget overrun escalates to a human rather than hanging
- if the critic is unavailable, candidates still flow but are visibly marked uncriticised, never silently treated as criticised
- an agent returning a quote that does not exist in the source has its candidate dropped by the deterministic binder, regardless of stated confidence
- two agents returning contradictory values causes abstention, not a silent pick of either

Where a mitigation is missing, let the test fail and report it. Do not implement the mitigation yourself. A failing test that names a real gap is the deliverable.

### 3. `tests/trajectory.test.js`, evaluating the pipeline rather than the answer

Existing eval scores the final extraction. That is outcome evaluation and it is not enough for an agent system, because a pipeline can reach the right answer through a broken path and will not stay right.

Write trajectory tests that assert the SHAPE of a run, not just its result:

- a plan was created before any extraction ran
- triage actually pruned the work matrix, so fewer extraction calls happened than documents multiplied by fields
- every proposed value has a corresponding evidence-binding step
- every conflicted field has at least one critic objection or an explicit note that criticism was unavailable
- escalation to a human happened exactly once per case and was the terminal step
- the manifest contains agent entries in a causally sensible order: plan before proposal, proposal before objection, objection before reconciliation, reconciliation before human decision
- no manifest gap: every agent action that influenced an outcome left an entry

That last one is the important one. An action that changed the result but left no trace is the exact failure the product exists to prevent.

### 4. `src/lesson-ledger.js`, the improvement loop's data layer

Per build plan section 0. Pure data and rules, no model calls.

- `recordLesson({caseId, fieldCode, kind, evidence, whatWentWrong})` where kind is one of `ABSTENTION`, `HUMAN_OVERRODE_PROPOSAL`, `EVAL_FAILURE`, `VALIDATION_FAILURE`. Appends to `data/lesson-ledger.jsonl`.
- `proposeRule(lesson)` produces a rule object: an id, a plain-English statement, a machine-checkable predicate expressed as data rather than code, the lessons that motivated it, `status: 'PROPOSED'`, and a null approver.
- `approveRule(ruleId, approvedBy)` requires a non-empty human name, sets status `ACTIVE`, stamps a version, and refuses to activate a rule with no approver. **Rules never self-activate.**
- `activeRuleSet()` returns the current versioned set plus its version string, so the manifest can record which rules were in force for a case.
- `regressionCheck(rule, historicalCases)` re-runs the rule against past cases and reports what it would have changed. A rule that breaks a previously correct outcome is rejected automatically.

Write `data/lesson-ledger.jsonl` seeded with three real lessons from last night, because they are genuine and it makes the demo honest:
1. the custodian letter mentioning "capital calls" caused the drawn-capital figure to be offered as evidence for committed capital
2. one extractor model does not reproduce source text exactly, so exact quote matching dropped every candidate
3. a forged stored `previousEntryHash` was accepted as intact because the link field was never checked

### 5. `src/agent-trace-cli.js`, the independent trace reader

Standalone. `node src/agent-trace-cli.js data/case-<id>.json` prints the full agent trajectory from the manifest alone, without importing the orchestrator: what was planned, which agent proposed what from which document region, who objected, what was escalated, which rule-set version was in force, and which named humans acted.

Then it independently verifies the chain over those entries and reports any gap between what the case state claims and what the manifest can prove. **This is the artifact we hand a sceptic**, so it must not depend on the code that produced the trace.

### 6. `scripts/agent-check.sh`, the pre-stage check for the agentic path

Extends the existing `demo-check.sh` idea to the multi-agent run. Under 30 seconds, one line per check, verdict in the first characters, non-zero exit on any failure. Check: the orchestrator produced a plan, all nine agent roles are reachable, each is on its configured model, extraction and criticism genuinely ran in parallel rather than sequentially, the critic used a different model family from the extractor, every agent action is in the manifest, the chain verifies, the boundary tests pass, and the active rule-set version is recorded.

The parallelism check matters: if extraction and criticism ran sequentially, we do not have a parallel system and should not say we do.

### 7. `docs/AGENT_RUNBOOK.md`

One page. How to run the agentic path, how to read a trace, what each agent does in one line, the three most likely failures with fixes, and how to approve a lesson into a rule.

---

Constraints on everything. No em dashes anywhere including comments and error messages. Do not use the words cutting-edge, revolutionary, seamless, disruptive, transformative, world-class, state-of-the-art, unlock or empower. All data is synthetic and must stay labelled synthetic. Every user-visible string is plain English a compliance officer would understand. No dependencies.

Run everything you write. A file is not done because it exists, it is done when you have run it and read the output. Where another lane's gap makes a test fail, report the gap precisely rather than working around it.

Reply with: the exact commands that prove each of the seven items, the test counts, every gap you found in another lane, and the single thing you would fix first if you had one more hour.
