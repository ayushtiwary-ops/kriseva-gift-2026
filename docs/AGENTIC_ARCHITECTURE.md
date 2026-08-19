# AGENTIC ARCHITECTURE: what we have, what we do not, and what to build

Written 2026-08-19 by Fable. This is a decision document, not a description.

---

## 1. The honest current state

**KRISEVA ATTEST is not currently an agentic system.** It is a deterministic pipeline with one model call per field. Specifically:

| What we have | What it actually is |
|---|---|
| `extract` | A loop. For each field, for each document, one model call asking for candidate values. No planning, no tool use, no iteration |
| `classifyFields` | Deterministic rules in code. No model involved |
| The decision and sign-off flow | A state machine with human input. No autonomy anywhere, by design |
| The manifest chain | Hashing. No intelligence |

There is no planner, no orchestrator, no agent that chooses its next action, no tool calling, no reflection, and no memory across steps. If a juror asks "show me the agents", the truthful answer today is that there are none.

The hackathon theme is Agentic AI in Financial Services. So this is a real gap in theme fit, and theme fit sits inside the 20% Problem Depth criterion and colours how the 30% Technical criterion is read.

---

## 2. The trap to avoid

The obvious move is to bolt on a multi-agent framework and call it agentic. Do not do that, for two reasons.

**It contradicts our own pitch.** Our entire argument is that AI must not act autonomously in regulated reporting: it proposes, it abstains, a named human decides. A jury that hears "autonomous agents handle the return" thirty seconds after hearing "AI must never decide" has caught us contradicting ourselves, and that is fatal on the 20% honesty criterion.

**Sophisticated jurors see through decoration.** Plug and Play looks at a lot of demos. Five agents passing messages to do what one function call could do is a pattern they have seen and dismissed.

---

## 3. The resolution, and it is genuinely strong

We are not anti-agentic. **We are the accountability layer that makes agentic AI deployable in a regulated workflow.**

The argument, in the order to say it:

1. Agentic systems are arriving in regulated reporting. IFSCA's own July 2026 survey names agentic AI as the next frontier.
2. The blocker is not capability. It is that nobody can prove what an agent did, which evidence it used, or who is accountable for the outcome.
3. So the useful thing to build is not another agent. It is the substrate that makes agent work inspectable, replayable and attributable.
4. And the way to prove that substrate works is to run a genuinely agentic system on top of it, and show that every action it took is in a tamper-evident record.

That reframes the question from "are you agentic" to "what makes agentic AI safe enough to use here", which is a better question and one we are uniquely positioned to answer.

**But we still have to show agents.** Positioning without a demo is a speech.

---

## 4. The architecture to build

Seven agents, one orchestrator, running in parallel, and the hard boundary preserved: **every agent may propose, no agent may decide.**

### The orchestrator

Plans the case rather than following a fixed loop. Given a case, it decides which documents are relevant to which fields, dispatches work in parallel, watches for failures, re-plans when a step returns nothing usable, and decides when it has enough evidence to hand the case to a human. It maintains an explicit plan object that is itself written to the manifest, so a reviewer can see what the system intended to do, not just what it did.

Critically, the orchestrator's terminal action is always the same: hand to a human. It has no authority to resolve a conflict, and that limit is enforced in the engine, not in its prompt.

### The specialists, running in parallel

| Agent | Job | Can it decide? |
|---|---|---|
| **Document triage** | Reads each source and reports which fields it plausibly carries, so the orchestrator does not run every field against every document | No |
| **Extraction** (N parallel, one per document) | Proposes candidate values with quoted evidence | No |
| **Evidence binding** | Verifies each quote exists in the source, computes exact spans, drops anything unverifiable | No, it only rejects |
| **Validation** | Runs deterministic checks: arithmetic coherence, period consistency, units, cross-field relationships such as drawn not exceeding committed | No, it only flags |
| **Reconciliation** | Compares candidates across documents, classifies the disagreement, writes the plain-English explanation | No |
| **Critic** | Adversarial. Takes each proposed value and tries to refute it from the source. Runs on a different model family from the extractor, so its disagreement is genuinely independent | No, it only objects |
| **Narrator** | Writes the human-readable summary a reviewer reads before deciding | No |

### Why the critic matters most

The critic is where the AWS credits earn their place. If Nova Pro extracts a value and Mistral Large 3, reading the same source, disagrees, the extraction is unreliable regardless of what the documents say. A system whose thesis is "refuse when you cannot prove it" must refuse there too.

That gives us two independent grounds for abstention, and we can say both on stage:

> "We abstain when the documents disagree. We also abstain when our own extractors disagree with each other. The second one is the harder problem and almost nobody checks it."

### The part nobody else has

**Every agent action is written to the same hash-chained manifest as every human action.** The agent trace is not a debug log next to the audit trail. It is the audit trail.

So the receipt shows, in one sealed chain: what the orchestrator planned, which agent proposed which value from which document region, which agent objected and why, what the system abstained on, which named human decided, who confirmed, and a hash that breaks if any of it is altered afterwards.

That is the differentiated object. Plenty of teams will run agents. The question a regulator asks is not whether your agents work. It is whether you can prove what they did eleven months later, and whether that proof survives someone wanting it to say something else.

---

## 5. How this compares to serious agentic systems

Honest assessment against what a mature agentic stack has:

| Capability | Mature systems | Us, after this build |
|---|---|---|
| Planning and decomposition | Yes | Yes, orchestrator with an explicit plan object |
| Parallel execution | Yes | Yes, extraction and critic fan out per document |
| Tool use | Yes | Yes, document retrieval, arithmetic validators, span verification |
| Reflection and self-critique | Yes | Yes, the critic agent, on a different model family |
| Guardrails | Usually prompt-level | Enforced in the engine. An agent cannot decide even if it tries |
| Human in the loop | Often optional | Mandatory and non-bypassable |
| Observability and tracing | Yes, as logs | Yes, as a tamper-evident sealed chain |
| Evaluation | Sometimes | Yes, 67 labelled items scoring abstention correctness separately |
| Long-horizon autonomy | Yes | **No, and deliberately not** |
| Learning from production feedback | Sometimes | **No** |

We would be genuinely comparable on seven of nine, better on guardrails and tracing, and deliberately absent on the two that a regulated workflow should not have.

**What not to claim.** We do not have long-horizon autonomy, self-modification, or online learning. If asked, say so plainly and explain that a system which changes its own behaviour between filings is not something a Principal Officer can sign.

---

## 6. Cost to build

Most of this is reorganisation, not new invention. The pieces already exist:

| Component | Status |
|---|---|
| Extraction agents | Exists, needs wrapping as parallel dispatch |
| Evidence binding agent | Exists, the locator with its five-strategy cascade |
| Reconciliation agent | Exists, `classifyFields` plus the cause derivation |
| Validation agent | Partly exists, deterministic checks need extending |
| **Orchestrator** | **New. This is the real work** |
| **Critic agent** | **New, but it is one model call on a second family** |
| **Narrator** | New, small |
| Manifest entries for agent actions | Extend the existing entry types |
| Agent-trace screen showing the plan and the fan-out | Extend the existing S4 screen |

Estimate: 400 to 600 new lines, plus reorganising about 200. Roughly 3 to 5 hours of agent-driven build, which fits inside the sprint and can be rehearsed today.

**Sequencing, and this is not negotiable:** the base demo must pass the canon gate first. An agentic layer on a demo whose numbers do not match the pitch is worth nothing.

---

## 7. What changes in the pitch

The demo gains one beat, roughly eight seconds, on the agent-trace screen:

> "Seven agents ran on this case, in parallel. This one proposed the value. This one checked the quote actually appears in the document. This one, running on a different model family, disagreed. So the system abstained and asked a human. Every one of those actions is in the sealed chain you are about to see, and if anyone edits one of them afterwards, the seal breaks."

And the answer to the theme question becomes:

> "Everyone here is building agents. The reason agents are not in regulated reporting yet is not that they cannot read a document. It is that nobody can prove what they did afterwards. We built the layer that makes agentic AI defensible, and then we ran seven agents on top of it to show it works."

---

## 8. The recommendation

Build it, after the canon gate passes, with the boundary intact.

The version of this that loses is a multi-agent diagram with no accountability story. The version that wins is an accountability substrate with a real agentic system running on it, where the agent trace and the audit trail are the same sealed object.

We are one orchestrator and one critic away from the second one.
