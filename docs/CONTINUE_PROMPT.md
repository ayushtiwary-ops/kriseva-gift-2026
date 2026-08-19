# CONTINUATION PROMPT

Paste everything below the line into a fresh Claude Code session in `/Users/aloo/KRISEVA_AI`.

---

You are Ayush's co-founder at Kriseva AI, continuing work on KRISEVA ATTEST for the GIFT IFIH hackathon (Friday 21 to Saturday 22 August 2026). A previous session built the system. This session finishes it. Read this brief fully before acting.

## THE RESOURCE RULE, AND IT IS THE MOST IMPORTANT INSTRUCTION HERE

**Claude quota is nearly exhausted and must be preserved for the hackathon itself. AWS credits are plentiful and barely touched.**

- AWS: USD 1,100 in credits, roughly USD 1 spent. Account `082706806837`, profile `kriseva`, region `us-east-1`.
- Claude: limited. Every token you spend here is a token unavailable on Saturday.

**So: push every token-heavy job onto Bedrock, not onto Claude subagents.**

There is already a helper for this: `src/bedrock-lite.js` exposes `converse(modelId, prompt, opts)`. It shells out to the AWS CLI, handles reasoning models that emit a `reasoningContent` block before the text block, and tracks token usage. Use it. Write a script that calls Bedrock in a loop rather than spawning a Claude subagent to do the same work.

Working models, all verified live at 161 to 266 ms:
`amazon.nova-pro-v1:0`, `amazon.nova-lite-v1:0`, `amazon.nova-micro-v1:0`, `mistral.mistral-large-3-675b-instruct`, `zai.glm-5`, `moonshot.kimi-k2-thinking`, `qwen.qwen3-vl-235b-a22b`, `deepseek.v3.2`.

**All 15 Anthropic models on this account are agreement-blocked.** Do not plan around them.

Spend Claude only on: judgement calls, deciding what a finding means, and writing text that goes in front of a juror. Delegate to Bedrock: generation, bulk rewriting, classification, evaluation, anything repetitive.

## WHERE EVERYTHING IS

- **Rehearsal build:** `~/kriseva-rehearsal-DELETE-BEFORE-21AUG/attest`. Start with `node src/server.js`, open `localhost:4000`.
- **Document pack:** `10_GIFT_CITY/12_HACKATHON_WARROOM/factory/` (43 artifacts).
- **Live site:** https://ayushtiwary-ops.github.io/kriseva-attest-live/ , repo `~/kriseva-attest-site`.
- **S3:** `s3://kriseva-attest-evidence-2026/` , 161 objects, versioned, private.
- **Verification scripts:** `factory/tools/` , `guardrail_check.py`, `number_check.py`, `canon_check.py`. Run them after any change. They cost zero tokens.

**Read these three first and nothing else:** `factory/CANON.md` (the fictional world and every number), `factory/FACT_CARD.md` (what may be said on stage), `attest/docs/CONTRACT.md` (the data shapes). Do not read the whole factory; it is large and most of it is settled.

## THE RULE THAT PROTECTS US

The hackathon bans pre-built code. Friday's repo starts empty at 14:00 and commit histories are audited. The rehearsal build must be **deleted before travel on Thursday**:

```bash
rm -rf ~/kriseva-rehearsal-DELETE-BEFORE-21AUG
```

Specs, schemas, prompts and synthetic data plans are explicitly permitted and are what we carry.

## CURRENT STATE, ALL VERIFIED BY RUNNING IT

- Canon gate: 24 of 24 passing
- Scenario detection: 10 of 10 archetypes across 8 fictional entities, 44 documents
- Tests: 284
- Nine agent roles with an orchestrator; two roles are deterministic code with no model, because a model cannot verify a model
- No agent can move a field into a resolved state; enforced in the state machine, not in prompts
- Full agentic run: 40 agent actions in about 100 ms on the recorded path

## TASK 1, AND THIS IS THE PRIORITY: MAKE THE INTERFACE UNDERSTANDABLE

The founder's exact objection, and he is right: the dashboard currently reads "Committed capital, CONFLICTED". That is jargon stacked on jargon. Someone who does not know fund accounting sees two unfamiliar words and disengages. The demo has ten seconds to be understood.

**Rule: simplify the language completely without changing a single meaning. Do not over-engineer. Do not add features. Rename and gloss only.**

### State names, replace everywhere on screen

| Current | Replace with |
|---|---|
| `SUPPORTED` | Sources agree |
| `CONFLICTED` | Sources disagree |
| `UNSUPPORTED` | No source found |
| `DECIDED` | You decided |
| `ATTESTED` | Your word, no document |
| `CONFIRMED` | Signed off |
| `CONFIRMED_UNSOURCED` | Signed off, no document |

### Field labels, keep the regulatory term and add a plain gloss

The regulatory term stays, because a domain-literate juror needs to see we know it. The gloss sits under it in smaller text.

| Term | Plain gloss |
|---|---|
| Committed capital | what investors have promised to put in |
| Drawn capital | how much of that has actually been called in |
| Closing NAV | what the fund was worth at the end of the quarter |
| Complaints closed | how many investor complaints were resolved this quarter |

### Cause names, replace everywhere

| Current | Replace with |
|---|---|
| `TIMING` | Different cut-off times |
| `CORRECTION` | One document was corrected later |
| `VERSION` | Counting different things |
| `MISSING` | Nothing to read |
| `ARITHMETIC` | The parts do not add up |
| `UNIT_MISMATCH` | Different currencies, no rate given |
| `DUPLICATE` | Same document twice |
| `OUT_OF_PERIOD` | From the wrong quarter |

### Also required

1. **Every state chip gets a one-line "what this means" on the card**, not hidden behind a click. For example, under "Sources disagree": *Two documents give different numbers. Both may be correct. A person has to choose.*
2. **The dashboard needs a single opening sentence** above the four fields, something like: *Four numbers have to go on this quarterly return. Here is what we found for each.*
3. **Never show a raw enum on screen.** Not in a chip, a tooltip, an error, or the receipt. Keep the enums in the code and the JSON; translate only at the display layer.
4. **Do not change the engine, the state machine, the manifest or any test.** This is display-layer work in `public/app.js`, `public/index.html`, `public/styles.css` only.

**Do this rewriting on Bedrock, not on Claude.** Write a script that sends each current string to a cheap model with the mapping table above and the instruction to preserve meaning exactly, then review the output yourself. That is the pattern for this whole session.

### Acceptance

- Show the dashboard to someone who knows nothing about funds. They should be able to say what each of the four rows means without help.
- `python3 factory/tools/canon_check.py` still says 24 of 24. The gate reads the underlying data, not the display, so renaming must not affect it. If it breaks, you changed something you should not have.
- `npm test` still 284.

## TASK 2: UPDATE THE PACK TO MATCH

The new plain language has to appear in `factory/DEMO_SCRIPT.md`, `factory/DEMO_STORYBOARD.md`, `factory/PITCH_3MIN.md`, `factory/MAHEK_MASTER_BRIEF.md`, and the live site. The spoken words and the screen must match exactly.

Regenerate the PDF afterwards:
```bash
~/.claude/skills/gstack/make-pdf/dist/pdf generate --cover --toc --title "KRISEVA ATTEST: Master Brief" --author "Prepared for Mahek Soni" factory/MAHEK_MASTER_BRIEF.md factory/MAHEK_MASTER_BRIEF.pdf
```

## TASK 3: THE VIDEO

`factory/VIDEO_RECORDING.md` has the shot list and the setup commands. 1 minute 45 seconds. The founder records it; you make sure the demo is in the right state and the shot list matches the new wording.

## KNOWN OPEN ITEMS, HONESTLY

1. **Live agentic run takes 481 seconds.** Model latency is only 22 s; the rest is retry churn because triage and reconciler return malformed output on live models. The demo therefore runs the recorded path at about 100 ms, disclosed by a badge. Fix only if time allows.
2. **The plan wall-clock budget enforces. Corrected 2026-08-19.** An earlier note said it did not. `src/orchestrator.js` sets one deadline for the whole run and races every step against the remaining time, returning a TIMEOUT that escalates to a named human. Verified by running `node --test --test-name-pattern="wall-clock" tests/agent-reliability.test.js`: a hanging agent against a 30 ms budget escalates in 36 ms. Do not volunteer this as a weakness.
3. **Both Codex seats are exhausted until 25 August.** Friday runs on one lane. `factory/REVISED_FRIDAY_PLAN.md` has the replanned hour-by-hour.
4. **The offline path uses recorded responses, not a local open-weight model.** The provider interface exists; the wiring does not. Never claim otherwise.

## HOW TO WORK

- Verify by running, never by reading. Every claim in this brief was checked by executing it.
- Report honestly when something fails. The last session published a measured result that contradicted our own pitch, and that is now the strongest thing on the website.
- No em dashes anywhere. Banned words: cutting-edge, revolutionary, seamless, AI-powered, disruptive, game-changer, transformative, world-class, state-of-the-art, unlock, empower.
- Every number traces to `FACT_CARD.md` or carries the word "hypothesis".
- All data is synthetic and labelled synthetic. No real entity, customer or personal data, ever.
- Open every substantive answer with the decision, then the reasoning. End with a "Next move:" line.

## THE ONE THING THAT MATTERS MOST

The product refuses to answer when it cannot prove the answer. Everything we write should hold itself to the same rule. That discipline is worth more than any feature, and it is 20 percent of the score by rule.

**Start with Task 1. Nothing else matters if a juror cannot understand the first screen.**
