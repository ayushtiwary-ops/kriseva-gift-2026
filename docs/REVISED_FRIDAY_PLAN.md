# REVISED FRIDAY PLAN: no Codex, and the dual deployment story

Written 2026-08-19. Supersedes the lane assignments in `PROMPT_PLAYBOOK.md`. Everything else in that document still stands.

---

## 1. What changed, and it is significant

**Both Codex seats are exhausted until 25 August.** The hackathon is 21 to 22 August. So Codex is gone for the event.

`PROMPT_PLAYBOOK.md` assumes three concurrent agent lanes: Claude Code plus two Codex seats. That plan is now wrong. Friday runs on one lane with a limited quota, and the quota resets at 10:30 on Saturday, which is inside the sprint but only 90 minutes before the 12:00 code freeze.

This is the single biggest change to the Friday plan and it has to be absorbed now rather than discovered at hour 4.

### What it means concretely

| Before | Now |
|---|---|
| 3 parallel lanes, 30 prompts | 1 lane, prompts run in sequence |
| Agents write most code | Agents write the hard parts, humans type the mechanical parts |
| Quota not a constraint | Quota is the binding constraint until 10:30 Saturday |

### The revised approach

**Spend the quota on the spine, type the rest by hand.** Ranked:

1. **Agent budget goes to:** the evidence engine, the manifest chain, the orchestrator, the provider and SigV4 signing. These are the parts where a subtle bug is invisible and expensive, and where we already know exactly what breaks.
2. **Type by hand:** the document generator, the case JSON, the screens markup, the README, the NOTICE. All mechanical, all specified to the character in the factory documents. I wrote the generator by hand last night in one pass, so this is proven.
3. **Do not spend a single agent call on:** anything already decided in the factory pack. The spec is written. Friday is transcription, not design.

**The 10:30 Saturday reset is a planned resource, not a surprise.** Hold the eval harness, the risk board and any polish for after it. Get the spine, the demo path and the honesty table done before quota runs out, because those are the things that cannot be cut.

### The rehearsal insight that matters most

The build we did overnight took roughly 6 hours of agent time across 15 agents, of which 3 produced nothing. On one lane with limited quota, assume **half the throughput and twice the care**. The factory pack is what makes that survivable: nothing needs deciding on the day.

---

## 2. The dual deployment story

New requirement, and it is a genuinely strong addition to the pitch because it answers the objection every regulated buyer raises first.

### The claim

**The same system runs two ways: on AWS, or entirely inside the customer's own machine with no network call at all. Same evidence guarantees, same audit trail, same refusal behaviour. Only the model plane changes.**

### Why this is credible rather than a slide

It is already true, and it is true by accident of good design rather than by marketing. The `ModelProvider` interface has two implementations from day one:

- `BedrockProvider`: calls AWS Bedrock over the network
- `ReplayProvider`: runs entirely locally with no network call whatsoever

The demo already runs the local path by default. When the founder demos with no AWS environment variables set, **the product is running fully offline and producing identical results.** That is not a promise about the future, it is what happens when you unplug the wifi.

### What is honestly true today, and what is not

**True today:**
- Everything except the model call runs locally: the evidence engine, conflict detection, abstention, the hash chain, the manifest, the verifier, the eval harness.
- The offline path produces byte-identical results to the recorded cloud path.
- Swapping the model plane is one environment variable.
- No customer document ever has to leave the customer's machine for the accountability layer to work.

**Not true today, and say so:**
- We have not wired a local open-weight model as the extractor. The offline path currently uses recorded responses and a deterministic scan, not a local LLM.
- The step from here to a genuinely local LLM is small (the provider interface already exists) but it is a step we have not taken, and we will not claim it.

### The honest sentence for stage

> "There are two deployments. On AWS, extraction runs on Bedrock. On premise, the same product runs with no network call at all, because the model sits behind an interface with two implementations and we built both. Right now the offline path uses recorded responses rather than a local open-weight model, and wiring one in is a change to a single module. The part that matters, the evidence engine and the sealed record, is identical in both and never leaves the customer's machine either way."

### Why this wins the objection

The first question a compliance officer asks about any AI tool is where their documents go. Most answers are a security page and a promise. Ours is: **unplug the network and watch it keep working.** That is demonstrable in the room, in about four seconds, and it is the single most persuasive thing we can do for a regulated buyer.

**Demo move, worth rehearsing:** turn off wifi, run the case, show identical output. Then say the honest boundary above.

---

## 3. The revised Friday hour plan

| Hours | What | Quota |
|---|---|---|
| 0-2 | Repo, NOTICE, docs commit, generator typed by hand, fixture pack | Low, mostly typing |
| 2-5 | Provider and SigV4, first live Bedrock call, run recorder | **High. Spend here** |
| 5-10 | Evidence engine, conflict causes, manifest chain, tamper check | **High. Spend here** |
| 10-15 | Screens, typed from the UX spec | Medium |
| 15-19 | Orchestrator and critic, if quota remains. Otherwise the pipeline path and disclose it | Medium |
| 19-21 | Pitch integration, honesty table, rehearsal, recorded backup | Low |
| 21-22 | Freeze, tag, push, history read-back | None |

**After the 10:30 Saturday reset:** eval harness, risk board, polish, and the agentic layer if it was cut. Nothing on that list is load-bearing for the demo.

**Cut order, revised for one lane:** cut the orchestrator before the critic, cut the critic before the eval harness, cut the eval harness before the risk board. **Never cut:** live model call, the abstain-decide-seal loop, the manifest, the honesty table, the offline fallback.

---

## 4. What to tell the coach on Friday at 12:00

> "We lost our second toolchain to a quota reset two days ago, so we are building on one lane instead of three. Our spec was written before the event, so what we lost is throughput, not direction. We have cut the plan to the spine and we know exactly what we will drop if we run short."

Coaches remember teams that name a constraint precisely and have already replanned around it.
