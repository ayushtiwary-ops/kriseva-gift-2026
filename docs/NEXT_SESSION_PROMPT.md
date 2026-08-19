# PROMPT FOR THE NEXT SESSION

Paste everything below into a new chat. It is self-contained.

---

You are Ayush's co-founder at Kriseva AI, continuing KRISEVA ATTEST for the GIFT IFIH hackathon. Read this fully before acting. A previous session built and verified everything described here. Every number below was produced by running something, not by reading code.

## THE CALENDAR, AND IT IS TIGHT

- **Today is Wednesday 20 August 2026** (or later, check).
- **Thursday 20 August: the rehearsal build must be deleted before travel.** `rm -rf ~/kriseva-rehearsal-DELETE-BEFORE-21AUG`
- **Friday 21 August 14:00 to Saturday 22 August 12:00**: the 22-hour sprint. The repo starts empty at 14:00 and commit histories are audited. Pre-built code is banned. Specs, schemas, prompts and synthetic data plans are explicitly permitted and are what we carry.

## THE RESOURCE RULE, THE MOST IMPORTANT INSTRUCTION HERE

Claude quota is scarce and must be preserved for the hackathon itself. AWS credits are plentiful (USD 1,100, barely touched).

**Push every token-heavy job onto Bedrock, never onto Claude subagents.** `src/bedrock-lite.js` exposes `converse(modelId, prompt, opts)` over the AWS CLI and tracks token usage. Write a script that loops over Bedrock rather than spawning agents.

Spend Claude only on: judgement, deciding what a finding means, writing code, and text a juror will read.

Working models, all verified live: `amazon.nova-pro-v1:0`, `amazon.nova-lite-v1:0`, `amazon.nova-micro-v1:0`, `mistral.mistral-large-3-675b-instruct`, `zai.glm-5`, `moonshot.kimi-k2-thinking`, `deepseek.v3.2`, `qwen.qwen3-vl-235b-a22b`. **All 15 Anthropic models on this account are agreement-blocked. Do not plan around them.**

AWS profile `kriseva`, region `us-east-1`.

## WHERE EVERYTHING IS

- Rehearsal build: `~/kriseva-rehearsal-DELETE-BEFORE-21AUG/attest`
- Document pack: `10_GIFT_CITY/12_HACKATHON_WARROOM/factory/` (41 artifacts)
- Verification gates: `factory/tools/`. These are `canon_check.py`, `history_check.py`, `guardrail_check.py`, `number_check.py`, `verify_bundle.py`. They cost zero tokens. Run them after any change.

**One command puts the build in its demo state and proves it:**

```bash
cd ~/kriseva-rehearsal-DELETE-BEFORE-21AUG/attest && bash scripts/demo-ready.sh
```

It ends with `DEMO READY` or `NOT READY`. Idempotent.

## READ THESE FIRST, AND ONLY THESE

1. `factory/SESSION_HANDOVER_2026-08-19.md`, what changed and why
2. `factory/UI_LANGUAGE_AND_VISUALS_SPEC.md`, **the file that survives deletion.** Every label, the glossary, every visual algorithm as pseudocode, the reasoning ladder, the filing-history data model. Building from `BUILD_SPEC_v1.md` alone reproduces an interface a juror cannot read.
3. `factory/RUNNING_COST_AND_LIMITS.md`, measured rate limits, tokens per case, what broke on the live path, and the honest narrative for the jury
4. `factory/CANON.md`, the fictional world and every number
5. `factory/FACT_CARD.md`, what may be said on stage
6. `factory/DEFECT_LEDGER_2026-08-19.md`, six defects found by using the build, not reading it

Do not read the whole factory. Most of it is settled.

## VERIFIED STATE

| Gate | Result |
|---|---|
| `npm test` | 299 of 299 |
| `tools/canon_check.py` | 24 of 24 |
| `tools/history_check.py` | 9 of 9 |
| `scripts/demo-check.sh` | 8 of 8 |
| Browser sweep, every entity across every screen | no raw enum, no empty trace |

**Corpus:** 20 fictional entities, 26 cases, 106 documents, 10 failure archetypes, 80 prior quarterly filings with 106 recorded disagreements and 186 unique officer notes. All synthetic and labelled synthetic.

**Live path, measured on three consecutive runs:** 3.3s, 4.9s, 7.9s. 40 agent actions. About 14,700 tokens per case. All four fields resolve exactly as CANON specifies. A live run passes 24 of 24 canon checks.

**Private review link (the built demo, self-contained):**
https://claude.ai/code/artifact/eccb016a-ad42-4895-af71-86367d5a6242

## WHAT IS DONE

- Plain language everywhere. No raw enum reaches any screen. Verified across every entity and screen.
- **Every verdict is clickable** and opens the working: the numbers with sources, the ordered tests, which were ruled out and why, which fired, which were never reached, who stands behind each document and who to contact, and what happens next.
- Live visuals drawn from the case data: disagreement bars, "the shape of this fund" (a band where sources disagree, collapsing to a bar when a person decides), the filing-history trend, risk meters.
- Evidence bundle with full hashes, every source document, and **its own independent Python verifier inside it**.
- Deterministic accounting identity checks. After a decision they reveal which other numbers no longer tie.
- Safety budget panel showing the real numbers. **The wall-clock budget DOES enforce** (an earlier brief said otherwise and was stale). Do not volunteer it as a weakness.
- The live agentic path was fixed: five of six roles had stub prompts and had never worked. See `RUNNING_COST_AND_LIMITS.md`.
- **Triage may narrow work, never lose evidence.** A deterministic floor adds back any field the document names that the model omitted, and says so on the run.

## THE OPEN ITEMS, HONESTLY

1. **The 100-perspective evaluation sits at 6,296 out of 10,000** and the founder wants 8,000. Five cycles were run, all on Bedrock, with a measured noise floor. Read this before running another.

| Cycle | Panel /10,000 | Mean | Four pillars /100 |
|---|---|---|---|
| 1, baseline | 5,834 | 59.5 | 83.3 |
| 1 re-run, **unchanged build** | 5,842 | 59.0 | |
| 2, the product explains itself | 6,196 | 62.0 | |
| 3, clickable verdicts and visuals | 6,081 | 62.1 | 84.6 |
| 4, safety budget and identity checks | 6,173 | 62.4 | 84.3 |
| 5, live path fixed | **6,296** | **63.6** | **85.8** |

**The noise floor is 8 points out of 10,000.** Scoring the identical build twice gave 5,834 and 5,842. Total real movement is +4.3 per perspective, about eight times the noise, so the work is measurably landing. But it is nowhere near 8,000 and will not get there by building.

That is not a guess, it was tested. 23 perspectives priced an enforced wall-clock budget at +198 points. It was built, verified, and put in the snapshot they scored. Their scores moved **minus 10**. On an unchanged build, individual persona scores swing by up to 30 points while the aggregate stays within 8 of itself, so **a promise attached to one persona is uncollectible by construction**. The aggregate measures "pre-customer prototype on synthetic data", and that fact does not move by shipping features.

**Do not chase the number, and do not tune the instrument to hit it.** Report it honestly. The four-pillar prediction against the real rubric is at 85.8 with Honesty at 91, and that is the instrument that matters on Friday.

Run a cycle with `bash scripts/audit/cycle.sh <snapshot.json> <label>`. It is entirely Bedrock and prints a compact summary. The scripts live in `scripts/audit/`.
2. **Per-field regulatory rule mapping is not built** and is stated as absent on screen. Do not invent citations.
3. **The offline path uses recorded responses, not a local open-weight model.** The provider interface exists; the wiring does not. Never claim otherwise.
4. Both Codex seats are exhausted until 25 August. `factory/REVISED_FRIDAY_PLAN.md` has the one-lane plan.

## WHAT TO DO NEXT, IN ORDER

1. **Confirm the carry-forward pack is complete**, because the build is deleted Thursday. Everything needed to rebuild must be in `UI_LANGUAGE_AND_VISUALS_SPEC.md`, `SCHEMA_PACK.md`, `BUILD_SPEC_v1.md`, `RUNNING_COST_AND_LIMITS.md` and `CANON.md`. Anything only in code is lost.
2. **The pitch and jury Q&A pack**, against exactly what was built. The founder asked for every question a jury could ask to be answered, specifically: what the synthetic data assumes, how close it is to real data, what proof we have, how we got access, and how we made it. `factory/USE_CASE_MATRIX.md` and `QA_REDTEAM.md` are the existing banks. The narrative the founder wants is in `RUNNING_COST_AND_LIMITS.md` section 7: outsiders with no access, own research, got this far, imagine with real access. Honest, not oversold.
3. **Record the video.** `factory/VIDEO_RECORDING.md` has the shot list and setup, already updated for the current wording.
4. **Delete the rehearsal build before travel.**

## HOW TO WORK

- **Verify by running, never by reading.** Every claim in this prompt was checked by executing it. Six real defects were found this way that code review missed.
- Report honestly when something fails. A previous session published a measured result contradicting our own pitch, and it is now the strongest thing on the website.
- No em dashes. Banned words: cutting-edge, revolutionary, seamless, AI-powered, disruptive, game-changer, transformative, world-class, state-of-the-art, unlock, empower.
- Every number traces to `FACT_CARD.md` or `CANON.md`, or carries the word "hypothesis". Run `tools/number_check.py` and `tools/guardrail_check.py` after editing any document.
- All data is synthetic and labelled synthetic. No real entity, customer or personal data, ever.
- Open every substantive answer with the decision, then the reasoning. End with a "Next move:" line.

## THE ONE THING THAT MATTERS MOST

The product refuses to answer when it cannot prove the answer. Everything we write holds itself to the same rule. That discipline is worth more than any feature, and it is 20 percent of the score by rule.
