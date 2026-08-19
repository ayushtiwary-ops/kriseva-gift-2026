# AGENTIC BUILD PLAN: from correct pipeline to governed multi-agent system

Written 2026-08-19 by Fable. Execution plan, not a concept note. Companion to `AGENTIC_ARCHITECTURE.md` which holds the design rationale.

---

## 0. The one thing in the brief I am changing, and why it makes us stronger

The instruction is that every agent should be self-evolving, learn from its own mistakes, and never repeat one.

**The naive version of that would lose us the competition.** An agent that silently changes its own behaviour between filings is precisely the thing a Principal Officer cannot sign. If a supervisor asks "why did the system behave differently in Q2 than in Q1", and the honest answer is "it learned something and we do not know exactly what", the entire accountability argument collapses. We would have spent the pitch arguing for auditability and then demonstrated the opposite.

**The correct version is better, and almost nobody does it.**

Mistakes become **explicit, versioned, human-approved deterministic rules**. Not weight updates. Not silently mutating prompts. Not a vector store the system quietly consults.

The mechanism is a **Lesson Ledger**:

1. Every abstention, every human override of a proposed value, and every eval failure is captured as a candidate lesson, with the case, the field, the evidence and what went wrong.
2. A **Learner agent** reads the ledger and proposes a new deterministic rule in plain English plus a machine-checkable form. For example: "when the custodian letter mentions capital calls, do not treat it as evidence for committed capital", which is a real bug we hit last night.
3. **A named human approves or rejects the rule.** Nothing activates without that.
4. Approved rules are versioned, and the manifest records which rule-set version was in force for every case.
5. The eval harness re-runs against every historical case to prove the new rule fixes what it claims and breaks nothing else. A rule that fails regression is rejected automatically.

So the system genuinely does not repeat a mistake, and the reason it does not is inspectable, reversible, and attributable to a person who approved it.

**The sentence this buys us on stage:**

> "The system improves by turning its own mistakes into rules a human approved, versioned, with a regression test attached. When the regulator asks why it behaved differently this quarter than last, we hand them the rule, the date, and the name of the person who signed it off. Every other self-improving system answers that question with a shrug."

That is a genuine differentiator and it is the honest version of what was asked for.

---

## 1. The system

**One orchestrator, seven specialists, model-diverse, all parallel where possible, none able to decide.**

### The absolute boundary

Enforced in the engine, not in prompts: **no agent output can move a field to `DECIDED`, `ATTESTED`, `CONFIRMED` or `SIGNED`.** Those transitions require a named human through the API. An agent that tries is rejected by the state machine. This is what makes the whole thing safe to run autonomously.

### The agents

| # | Agent | Job | Parallel? | Can it change state? |
|---|---|---|---|---|
| 0 | **Orchestrator** | Builds a plan: which documents matter for which fields, what runs in what order, what to retry, when to escalate. Re-plans on failure. Terminal action is always "hand to human" | No, it is the conductor | No |
| 1 | **Triage** | Reads each document, reports which fields it plausibly carries. Prunes the work matrix so we do not run every field against every document | Yes, one per document | No |
| 2 | **Extractor** | Proposes candidate values with quoted evidence | Yes, one per document-field pair | No |
| 3 | **Evidence binder** | Verifies each quote exists in the source, computes exact spans, drops the unverifiable | Yes | No, rejects only |
| 4 | **Validator** | Deterministic checks: arithmetic coherence, period consistency, units, drawn not exceeding committed, ledger sums | Yes | No, flags only |
| 5 | **Critic** | Adversarial. Tries to refute each proposed value from the source. Runs on a different model family from the extractor | Yes, one per candidate | No, objects only |
| 6 | **Reconciler** | Compares surviving candidates, classifies the disagreement, writes the plain-English explanation | No, needs everything | No |
| 7 | **Narrator** | Writes the human-readable case summary a reviewer reads before deciding | No | No |
| 8 | **Learner** | Offline. Reads the Lesson Ledger, proposes new rules for human approval | No, runs between cases | No |

### Why the critic is the centre of gravity

Two independent grounds for abstention, not one:

- The documents disagree with each other (what we have today)
- Our own extractors disagree with each other (new)

The second requires genuine model diversity. Sampling the same model twice gives correlated errors. Using a different training lineage gives less correlated ones. That is the whole reason the 75-model Bedrock access matters, and it converts a constraint into a capability.

---

## 2. Making it not fall over

This is where most multi-agent demos die, so it gets designed rather than hoped for.

| Failure mode | Our mitigation |
|---|---|
| Error compounding across steps | Every agent output passes a schema check before the next agent sees it. Malformed output is a bounded retry, then a recorded failure, never a silent pass-through |
| Context loss between handoffs | Agents never pass free text to each other. They pass typed objects defined in the contract. The orchestrator holds the state |
| Infinite loops | Hard caps: 2 retries per agent call, 1 re-plan per case, wall-clock budget per case. Exceeding any cap escalates to a human, which is a valid and honest terminal state |
| Cascading hallucination | The evidence binder is deterministic code, not a model. A value that cannot be located in the source is dropped regardless of how confident any agent was |
| Coordination overhead making it slower than one call | Triage prunes the matrix. Extraction and criticism fan out concurrently. Target: full case under 20 seconds |
| One agent failing takes down the case | Every agent has a degraded mode. If the critic is unavailable, candidates proceed marked "uncriticised" and that is visible on screen. Never silently skipped |
| Nondeterminism ruining a demo | Temperature 0 everywhere, plus the existing replay provider. Every run is recorded and can be replayed byte-identically |

### The observability answer

**Every agent action writes to the same hash-chained manifest as every human action.** New entry types: `PLAN_CREATED`, `AGENT_PROPOSED`, `AGENT_OBJECTED`, `AGENT_REJECTED_EVIDENCE`, `VALIDATION_FAILED`, `ESCALATED_TO_HUMAN`, `RULE_VERSION_APPLIED`.

The agent trace is not a debug log sitting beside the audit trail. It is the audit trail, and it is tamper-evident. That is the thing no competitor has.

---

## 3. Model assignment

Diversity is deliberate. Two agents that must disagree independently must not share a lineage.

| Agent | Model | Why | Fallback |
|---|---|---|---|
| Orchestrator | `moonshot.kimi-k2-thinking` | Planning and decomposition is the hardest reasoning task here, and this is a reasoning-first model | `zai.glm-5` |
| Triage | `amazon.nova-micro-v1:0` | Trivial classification, called once per document, cheapest available | `amazon.nova-lite-v1:0` |
| Extractor | `amazon.nova-pro-v1:0` | Benchmarked by us: correct values, valid JSON, 302 ms on a single call | `mistral.mistral-large-3-675b-instruct` |
| Evidence binder | none, deterministic code | A model cannot be trusted to verify a model. This is the one place that must be arithmetic | none |
| Validator | none, deterministic code | Same reasoning | none |
| **Critic** | `mistral.mistral-large-3-675b-instruct` | **Different lineage from the extractor**, and benchmarked as the one that quotes source byte-exact | `qwen.qwen3-vl-235b-a22b` |
| Reconciler | `zai.glm-5` | Needs to reason about why sources differ, a genuine reasoning task | `deepseek.v3.2` |
| Narrator | `amazon.nova-lite-v1:0` | Plain summarisation, cheap | `amazon.nova-micro-v1:0` |
| Learner | `moonshot.kimi-k2-thinking` | Runs rarely, needs to generalise from failures into a rule | `zai.glm-5` |

Three families for the three roles that must think independently: Amazon for extraction, Mistral for criticism, Moonshot and Z.AI for planning and reconciliation. **Confirm each against the model-fit research before locking.**

---

## 4. Cost

Per full case, roughly: 1 planning call, 4 triage, 16 extraction, 16 critic, 4 reconciliation, 1 narration. Call it 42 model calls at roughly 2,000 input and 300 output tokens.

That is about 84,000 input and 12,600 output tokens per case. Even at the more expensive models in the mix, that lands in the low tens of cents per full agentic run.

**Against USD 1,100 in credits, we can afford thousands of full runs.** Money is not the constraint and never was. The eval harness at 67 labelled items, run repeatedly across rehearsal and the sprint, is still comfortably inside single-digit dollars.

The real budget is wall-clock. A 20-second case, run 30 times in rehearsal, is 10 minutes. That is the number that matters.

---

## 5. Execution plan

**Precondition, already met: the canon gate passes 24 of 24.** Do not start this until that is true, and re-run it after every block.

| Block | What | Hours | Owner |
|---|---|---|---|
| A | Agent contract: typed inputs and outputs for all nine agents, new manifest entry types, the state-transition guard that makes agent decisions impossible | 1.0 | Fable specifies, Sonnet writes |
| B | Orchestrator: plan object, parallel dispatch, retry and re-plan caps, escalation | 1.5 | Sonnet |
| C | Critic agent on a second model family, plus the disagreement rule that triggers abstention | 1.0 | Sonnet |
| D | Triage and narrator, the two cheap agents | 0.5 | Sonnet |
| E | Agent trace screen: show the plan, the fan-out, who objected, all in the sealed chain | 1.0 | Sonnet |
| F | Lesson Ledger and the Learner agent, with human approval gate and regression check | 1.5 | Sonnet |
| G | Trajectory evaluation: extend the eval harness to score the pipeline, not just the extraction | 1.0 | Sonnet |
| H | Integration, canon gate, demo rehearsal | 1.0 | Fable |

**Total 8.5 hours of agent-driven build.** Achievable today, and the whole point of doing it today is that Friday becomes a repeat.

Cut order if time runs short: F first (the ledger is the most impressive and the least essential to a working demo), then G, then D. **Never cut the boundary guard in block A, the critic in block C, or the manifest integration.**

---

## 6. What we claim and what we do not

**Claim, because it is demonstrable:** nine agents, an orchestrator that plans and re-plans, parallel execution, model diversity across three families, deterministic evidence verification, adversarial criticism, mandatory human decision, tamper-evident tracing of every agent action, and an improvement loop where every change is human-approved and versioned.

**Do not claim:** long-horizon autonomy, online learning, self-modification, or any accuracy figure that is not on the eval slide with its denominator visible.

If asked why we lack autonomy: "Because a system that changes its own behaviour between filings is not something a Principal Officer can sign. Our improvement loop is deliberately slower and deliberately human-gated, and that is a feature of the regulated context, not a limitation of the engineering."

---

## 7. Why this wins rather than merely qualifies

Most teams on an agentic track will show agents doing a task. The question a regulator-adjacent jury actually has is not whether agents can do the task. It is whether anyone can prove what they did afterwards.

We will be the only team whose agent trace and audit trail are the same sealed object, whose agents are structurally incapable of making the decision, and whose self-improvement is itself auditable.

That is not a better demo of the same thing. It is a different answer to the question.
