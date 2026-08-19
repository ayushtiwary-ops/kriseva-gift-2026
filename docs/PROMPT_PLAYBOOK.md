# PROMPT PLAYBOOK: KRISEVA ATTEST sprint, GIFT IFIH hackathon

Status: DRAFT v1. Owner: founder approves, this playbook is the ordered set of prompts the team fires at the coding agents across the 22-hour build (Friday 21 Aug 14:00 to Saturday 22 Aug 12:00).

> **Name placeholder, resolve before Friday.** Every occurrence of `Mahek Soni` in this document is the second founder's name. The war room documents disagree: docs 00, 01, 04, 05 and 07 say Sony; docs 08 and 10 and `APPLICATION_UPDATE_BANK.md` say Mahek. This name is typed literally into every `M<milestone>: ... [by <name>]` commit from that lane and appears in the audited git history, so it must be settled before 14:00 Friday. Substitute it once, here and in `REPO_FIRST_COMMIT_PACK.md`, and check it matches the badge and the government ID.


This document contains no code. Every block below is a prompt: English instructions that a coding agent reads on the day and answers by writing new code. Nothing in this file is meant to run. If a block looks like it could be pasted into an interpreter, that is a mistake in this document, not a feature of it.

Two documents are the contract for everything built Friday: `docs/BUILD_SPEC_v1.md` and `docs/SCHEMA_PACK.md`. This playbook references their sections by name. It does not repeat their content, and it does not substitute for reading them.

---

## Section A: How to run this playbook

"The conductor" below means whichever human is physically driving a lane at that moment: Ayush on Claude Code, Ayush on Codex A (seat 1, second terminal), or Mahek Soni on Codex B (seat 2, her own machine). All three humans follow the same operating rules. Claude Code additionally carries the build-conductor role across the whole sprint per `05_AGENT_SYSTEM.md` section 3: it owns scaffolding, hard integration, Bedrock wiring, and the nastiest bugs, and it is where architecture calls and milestone go/no-go decisions get made when a human needs a second opinion.

1. **Give the agent the spec section, not a vibe.** Never say "build the conflict screen." Say "build screen S3 exactly as `BUILD_SPEC_v1.md` section 5 describes it, with the acceptance checks listed there." Every prompt in Section C and Section D names the exact `BUILD_SPEC_v1.md` or `SCHEMA_PACK.md` section it is drawing from. If a prompt does not name a section, do not fire it until it does.

2. **Acceptance checks go IN the prompt.** Every prompt text block below already tells the agent what "done" looks like, in the agent's own words, before it hands back control. This is not decoration. An agent that knows the finish line stops earlier and drifts less. Do not strip this part out to save paste time.

3. **Review by behaviour first, then by diff.** When the agent says it is done: run it, click it, watch it fail the way it should fail. Only after the behaviour looks right do you open the diff. Then ask the agent to explain its own diff in two or three sentences and challenge exactly one line or one decision in it. An agent that cannot explain its own change is an agent whose change you should not trust yet.

4. **Commit every 20 to 30 minutes.** A fired prompt that runs for an hour without a commit is a fired prompt that is about to lose an hour of work to a bad edit. Break long prompts into checkpoints if the agent's own plan runs past 30 minutes; commit at each checkpoint using the convention in Section B.

5. **Stuck 20 minutes, change altitude.** If the same prompt has not produced a working result after 20 minutes of back and forth, do not keep refining the wording. Go up a level (re-read the relevant `BUILD_SPEC_v1.md` section out loud, confirm the human understood it correctly before the agent ever saw it) or go down a level (ask the agent to solve a smaller piece in isolation: one function's worth of behaviour, one endpoint, one field). Staying at the same altitude and rephrasing the same prompt for the third time is how 45 minutes disappears.

6. **Two failed iterations, the approach is wrong.** If you have fired a prompt, corrected it, fired the correction, and it still fails the same acceptance check on the second retry, stop iterating on wording. The prompt is not the problem; the plan behind it is. Re-read the spec section, question whether the data model or the API shape it describes is what you actually need, and if necessary escalate to Claude Code as conductor for an architecture call before trying a third time.

7. **No prompt fires before its spec section is open on screen.** Literally: the human firing the prompt has `BUILD_SPEC_v1.md` (or `SCHEMA_PACK.md`) open, scrolled to the named section, before they paste. This is what makes rule 1 real instead of aspirational. If the section is not open, the prompt is not ready.

8. **Idle lane, do not invent scope.** A lane with no assigned prompt in a given milestone window (M2 has no Codex A prompt; M6 has almost none) uses the spare time to hard­en the previous milestone's deliverable, more fixtures, more edge cases, more tests, or to get the next milestone's spec section read and understood before its first prompt fires. It does not pull forward a prompt whose "Depends on" has not been committed yet, and it does not start building something this playbook did not ask for.

9. **A fired prompt can produce more than one commit.** The 25 build prompts in Section C are scoped to a deliverable, not to a single commit. A prompt that takes 40 minutes with one review-and-fix cycle in the middle should produce two commits, both following the convention in Section B, both authored by the human who reviewed.

10. **Status is DONE, PARTIAL, or BLOCKED.** Never "should be working" and never "basically done." If it is not DONE, say which of the acceptance checks below the prompt still fails, and say so before moving to the next prompt in the chain.


---

## Section B: The standing preamble

Paste this exact block at the top of every new agent session, in every lane, before the first milestone prompt of that session. It does not need to be repeated before every single prompt inside the same continuous session, only when a session starts fresh (a new terminal, a cleared context, a new day). If you are ever unsure whether the agent still holds this context, paste it again; it costs one paragraph and it prevents an entire wrong-direction hour.

> You are working inside a fresh git repository for KRISEVA ATTEST, created empty today for a 22-hour hackathon build at the GIFT IFIH event. ATTEST is an evidence and decision-integrity layer for regulatory reporting: it never resolves a disagreement between sources on its own, it proposes a value with a pinned source, surfaces disagreement when sources conflict, and requires a named human to decide and a second named human to confirm before anything is treated as final. Say "abstain," never "fail" or "error," when the system declines to guess. Say "preserved disagreement," never "conflict resolution." The product name is KRISEVA ATTEST, never any other spelling or short form. ATTEST sits upstream of DRR; never describe it as integrating with, connecting to, or filing to anything. Every case in this build is fictional: a synthetic fund manager, a synthetic fund administrator, a synthetic custodian, and synthetic people, drawn only from `docs/SCHEMA_PACK.md`, which is this repository's complete and only source of truth for entity names, personas, and numbers. No real company, fund, person, or number appears anywhere in this codebase, and every screen that shows data must make its synthetic nature visible. If a name or number you need is not in `SCHEMA_PACK.md`, it does not exist yet; stop and ask rather than inventing one or recalling one from general knowledge of how funds work.
>
> The contract for what you build is two files in this repository: `docs/BUILD_SPEC_v1.md` (the engineering spec: data model, API, screens, eval protocol, manifest spec, deployment steps, test plan, cut list) and `docs/SCHEMA_PACK.md` (the synthetic data: field definitions, document templates, planted-conflict matrix, generation rules, eval label format). When a prompt in this session names a section of either file, open and read that exact section before you write anything. If a requirement is not covered by the named section and is not obvious from the surrounding architecture, stop and ask the human instead of inventing a plausible-sounding answer. Guessing a requirement and writing code against the guess is the single most expensive mistake you can make today, because it costs a review cycle to catch and another to unwind.
>
> Every line of code you write in this repository is written new, today, from the spec files described above. Do not retrieve, recall, paraphrase, port, or reconstruct any source code from any prior Kriseva repository, from the public ATTEST prototype repository, or from any other pre-existing codebase, even one you may have seen before, even if you believe you can improve on it, even if it would be faster. The only pre-existing material that belongs in this repository is the small set of docs committed in the first commit under `docs/` (the spec, the schema pack, the wireframe PDF) and `NOTICE.md`, which discloses exactly that fact. This is a hard rule, not a style preference: the event brief requires a clean git history with no pre-built code, and the team is treating that audit as something to welcome, not something to route around.
>
> Repository layout, keep every lane consistent with this:
> - `NOTICE.md` and `README.md` at the repository root.
> - `docs/` holds `BUILD_SPEC_v1.md`, `SCHEMA_PACK.md`, and the wireframe PDF, committed before any code.
> - `backend/` holds the single Node.js service: its source, its `providers/` for the ModelProvider implementations, and `runs/` for the JSONL run log.
> - `frontend/` holds the static HTML, CSS, and vanilla JavaScript for the seven screens. No framework, no bundler, no build step.
> - `fixtures/` holds the synthetic source documents and the generator that produces them.
> - `eval/` holds the labelled evaluation set and the eval harness output.
> If a prompt asks you to create something and the right home for it is not obvious from this list, propose a location that fits the pattern and say so out loud in your summary rather than silently picking one.
>
> Tech constraints, do not deviate without asking: one Node.js service on the backend (bare `http` or Express, not both). The frontend is static HTML, CSS, and vanilla JavaScript with no build step and no framework. Do not add a new npm dependency, a new AWS service, or a new external API beyond what the named spec section calls for without asking the human first; if you believe you need one, say what it is, why, and what it costs, and wait for a yes.
>
> Commit convention: `M<milestone>: <what> [by <name>]`, for example `M2: add BedrockProvider Converse wiring [by Ayush]`. The name is the human who reviewed the diff, not necessarily the human who typed the prompt. Do not write the commit yourself unless the human has already reviewed and explicitly told you to commit; when you do, use this exact format.
>
> When you finish a task, state clearly whether it is DONE, PARTIAL, or BLOCKED, and list which of the prompt's own acceptance checks pass and which do not. Do not say "should work" or "this should be fine." If you are blocked or uncertain about a requirement, stop and ask rather than filling the gap with an assumption.


---

## Section C: The prompt sequence, M1 through M6

Twenty-five prompts, three lanes, six milestones, mapped to the hour-by-hour table in `04_CLEAN_START_BUILD_KIT.md` section 6. Lane names below: **Claude Code** (build conductor, Ayush's primary machine), **Codex A** (Codex seat 1, Ayush's second terminal), **Codex B** (Codex seat 2, Mahek Soni's machine). Every prompt assumes Section B's standing preamble is already live in that session.

### Milestone M1: repo init, scaffold, synthetic generator (Hour 0-2, Fri 14:00-16:00)

#### M1-P1
- **Lane:** Claude Code
- **Milestone:** M1
- **Goal:** Create the empty repository's first commit: the disclosure notice and the pre-event docs, nothing else.
- **Depends on:** Nothing. First prompt of the day.

> We are starting a brand new git repository, empty, right now, at the official start time of the build. Initialize git in this directory. Create `NOTICE.md` at the repository root disclosing, per the event brief's own instruction, exactly which artifacts in this repository predate today's build: `docs/BUILD_SPEC_v1.md` (engineering spec, drafted this week), `docs/SCHEMA_PACK.md` (synthetic data schema pack, drafted this week), and the wireframe PDF in `docs/`, reused from the team's public pre-event ATTEST prototype. Include a link to that public pre-event prototype repository in `NOTICE.md` so the audit trail is one click away, not something a judge has to take our word for. Then create the `docs/` folder and place the already-prepared `BUILD_SPEC_v1.md`, `SCHEMA_PACK.md`, and wireframe PDF inside it exactly as provided; do not edit their content. This first commit contains documentation files only. Do not create, scaffold, or touch any source code file in this commit, even a placeholder one; that starts with the next prompt. Write this fresh: draft `NOTICE.md` yourself in your own words from the facts above, do not copy wording from any prior repository's notice file even if one exists publicly.

**Acceptance checks:**
1. `git log` shows exactly one commit, and its timestamp is after 14:00 on the official start day.
2. `NOTICE.md` exists at the repository root and names every pre-event artifact with one line each on what it is and that it predates the event.
3. `NOTICE.md` contains a working link to the public pre-event ATTEST prototype repository.
4. `docs/` contains `BUILD_SPEC_v1.md`, `SCHEMA_PACK.md`, and the wireframe PDF, and nothing else.
5. No file with a source-code extension appears anywhere in this commit.

**Expected minutes:** 15-20

**Failure mode:** the agent scaffolds a backend or frontend folder in the same commit "to save a step." **Fallback prompt:** "Undo any non-doc file you just added. This commit is docs and `NOTICE.md` only, nothing else, per the brief's own audit rule. Confirm with `git status` before committing."

---

#### M1-P2
- **Lane:** Claude Code
- **Milestone:** M1
- **Goal:** Stand up the empty backend service and static frontend skeleton so every later prompt has a home to write into.
- **Depends on:** M1-P1 committed.

> Working from the repository layout in the standing preamble, create the project scaffold. In `backend/`, write the smallest possible single Node.js service that starts and answers a health check; no business endpoints yet, not even a stub for `/ingest` or `/extract`, those come in later milestones from their own spec sections. In `frontend/`, write a static `index.html`, one shared stylesheet, and a simple navigation shell listing the seven screens named in `BUILD_SPEC_v1.md` section 5 as placeholder links or placeholder sections; no real data wiring yet, no framework, no build step, plain HTML/CSS/vanilla JS only, per the tech constraints in the standing preamble. Create empty `fixtures/` and `eval/` folders, each with a one-line stub file explaining what will live there later. Use the glossary in `BUILD_SPEC_v1.md` section 2 for naming so every later prompt in every lane uses the same words for the same things. Do not add any dependency beyond what is strictly needed to start an HTTP server; if you think you need one, name it and ask before adding it. This scaffold is new code, written from the standing preamble's tech constraints and the glossary in `BUILD_SPEC_v1.md` section 2; do not carry over boilerplate from any earlier Kriseva service.

**Acceptance checks:**
1. Starting the backend service locally succeeds and its health check route responds.
2. Opening `frontend/index.html` in a browser shows a shell page listing all seven screen names from `BUILD_SPEC_v1.md` section 5, each an empty placeholder.
3. `fixtures/` and `eval/` exist and contain only their one-line stub files.
4. No endpoint beyond the health check exists in the backend yet.
5. The dependency manifest lists nothing beyond the minimum needed to start the server; nothing was added without asking.

**Expected minutes:** 30-40

**Failure mode:** the agent reaches for a frontend framework or a heavier backend framework "because it's faster." **Fallback prompt:** "Strip this back to plain HTML/CSS/vanilla JS on the frontend and bare `http` or a single minimal framework on the backend, per the tech constraints in the standing preamble. Remove anything else you added and re-run the health check."

---

#### M1-P3
- **Lane:** Codex A
- **Milestone:** M1
- **Goal:** Write the synthetic data generator that produces the four source documents from `SCHEMA_PACK.md`.
- **Depends on:** M1-P1 committed.

> Read `SCHEMA_PACK.md`'s field definitions, document templates, and generation rules sections in full before writing anything. Write a generator script, living under `fixtures/`, that produces the four synthetic source documents it describes (the administrator statement, the subscription register extract, the internal ledger export, and the custodian holdings and cash confirmation), following the document templates and CSV column specs exactly as `SCHEMA_PACK.md` states them. The generator must read its field values and its planted-conflict encoding from `SCHEMA_PACK.md`'s own generation rules, not from numbers you recall or infer; if a value is not explicit in the schema pack, stop and ask rather than guessing a plausible one. Seed the generator so re-running it produces byte-identical output. Every generated document must carry a visible synthetic/fictional disclosure marker, matching the project's naming and vocabulary locks. This is new code, written now, from the schema pack only; do not adapt a generator from any other project you may know of.

**Acceptance checks:**
1. Running the generator once produces the four source documents under `fixtures/` with no errors.
2. Every generated document carries a visible synthetic/fictional disclosure marker.
3. Running the generator twice with the same seed produces byte-identical files.
4. The values in each generated document match `SCHEMA_PACK.md`'s field definitions exactly, spot-checked against at least three of the four fields.
5. No real company, fund, custodian, or person name appears anywhere in the output.
6. The generator finished inside its 45-minute target.

**Expected minutes:** 35-45 (target under 45, per the week's own rehearsal benchmark)

**Failure mode:** the generator produces plausible but incorrect numbers because the agent filled a gap from general knowledge of how funds work instead of the schema pack. **Fallback prompt:** "Stop guessing. Open `SCHEMA_PACK.md`'s field definitions section side by side with your output, list every value that does not match it exactly, and fix only those."

---

#### M1-P4
- **Lane:** Codex A
- **Milestone:** M1
- **Goal:** Generate fixture pack v1 and verify it against the canonical numbers and the planted-conflict matrix before any other lane depends on it.
- **Depends on:** M1-P3 committed.

> Run the generator from the previous prompt to produce fixture pack v1. Then write a small, separate verification script, not a UI, whose only job is to check fixture pack v1 against `SCHEMA_PACK.md` and print one pass or fail line per check: that each field's value in each document that carries it matches the schema exactly; that each of the four planted-conflict causes (a version disagreement, a timing disagreement, a correction disagreement, and one field with no supporting document at all) is present and distinguishable in the output, not collapsed into one generic "documents disagree" state; and that the fourth field is confirmed absent from every document, since that absence is the intended design, not a bug to fix. Print every check's result, do not skip or summarize silently. This verification script is new code, written from `SCHEMA_PACK.md` only.

**Acceptance checks:**
1. The verification script runs and prints one explicit pass or fail line per check.
2. All value-match checks pass against `SCHEMA_PACK.md`.
3. Each of the four planted-conflict causes is confirmed present and individually distinguishable, four separate pass lines, not one.
4. The fourth field is confirmed present in zero documents.
5. A human has read the full pass/fail output and spot-checked it by eye against the canonical entities and numbers before declaring fixture pack v1 usable by other lanes.

**Expected minutes:** 15-20

**Failure mode:** the verification script only checks that files exist and are non-empty, a green light that proves nothing. **Fallback prompt:** "This only checks presence. Rewrite it to compare every generated value against the exact number in `SCHEMA_PACK.md` and fail loudly, one line per field, on any mismatch."


### Milestone M2: model plane, run recording, first live extraction (Hour 2-5, Fri 16:00-19:00)

#### M2-P1
- **Lane:** Claude Code
- **Milestone:** M2
- **Goal:** Define the ModelProvider interface and implement BedrockProvider against it using the Converse API with the model id read from environment.
- **Depends on:** M1-P2 committed. Runs in parallel with M2-P2; both implement the same interface from the spec directly, neither waits on the other's code.

> Read the model plane description in `BUILD_SPEC_v1.md` section 3 before writing anything. Define `ModelProvider` as a small, clean interface that any implementation can satisfy: something that takes an extraction request and returns a structured result. The interface itself must not mention Bedrock, AWS, or Converse anywhere; it is provider-neutral by design, because a second implementation is being built right now in a different lane against this same interface. Then implement `BedrockProvider`, using AWS SDK v3's Converse API, reading which model to call from an environment variable, never a hardcoded model id or region. When Bedrock returns an access-denied or permission error, make that surface as a distinct, identifiable error type, not a generic crash, so the rest of the system can react to it later. This is new code written from the spec section only; do not reuse provider-wiring code from any earlier Kriseva project even if the shape looks similar.

**Acceptance checks:**
1. The `ModelProvider` interface is defined in one place, documented well enough that another lane could implement it without reading this file's internals.
2. Changing the environment variable and restarting the service changes which Bedrock model gets called, with no code edit.
3. Once credentials are live, calling `BedrockProvider` returns a result matching the shape `BUILD_SPEC_v1.md` section 3 describes.
4. An access-denied response from Bedrock produces a distinct, catchable error, not a crash or a silent empty result.
5. No model id, AWS region, or credential value is hardcoded anywhere in the source.

**Expected minutes:** 45-60

**Failure mode:** the agent hardcodes a specific model id to get something working fast, or blends Bedrock-specific details into the interface itself so a second implementation cannot cleanly conform to it. **Fallback prompt:** "Separate the interface from this implementation completely. The interface file must not mention Bedrock, Converse, or AWS anywhere; anything provider-specific belongs only inside `BedrockProvider`."

---

#### M2-P2
- **Lane:** Codex B
- **Milestone:** M2
- **Goal:** Implement ReplayProvider against the same interface, and the run recorder that logs every provider call.
- **Depends on:** M1-P2 committed. Runs in parallel with M2-P1.

> Read the model plane description in `BUILD_SPEC_v1.md` section 3. Implement `ReplayProvider`, conforming to the exact same `ModelProvider` interface a parallel lane is implementing for Bedrock right now; given the same input twice, it must return byte-identical output both times, with no randomness anywhere. It serves its answers from a run log of recorded calls. Alongside it, implement the run recorder: a wrapper that captures every call made through any `ModelProvider` implementation and appends one entry to the run log containing a prompt hash, the call's parameters, its response, and its latency, exactly as `BUILD_SPEC_v1.md` sections 3 and 8 describe. No live call may exist yet at this point in the day, so hand-write one clearly labeled seed entry in the run log, explicitly marked as a seed fixture and not a real run, so you can prove `ReplayProvider` serves it deterministically before the first genuine live extraction happens later today. This is new code written from the spec only; do not port a fixture-serving pattern from any other project.

**Acceptance checks:**
1. `ReplayProvider` satisfies the exact same interface `BedrockProvider` does; calling code can swap between them with no changes outside the providers folder.
2. The same input against `ReplayProvider` returns byte-identical output on every call.
3. The run recorder appends one entry per provider call, containing a prompt hash, parameters, response, and latency.
4. A clearly labeled seed entry exists in the run log, and `ReplayProvider` can serve it correctly before any live Bedrock call has happened.
5. Nothing in `ReplayProvider` or the run recorder imports or references AWS or Bedrock-specific code.

**Expected minutes:** 45-55

**Failure mode:** `ReplayProvider` gets built as a special case bolted onto `BedrockProvider` instead of a clean, independent implementation of the same interface. **Fallback prompt:** "These two providers must be fully interchangeable behind one interface. If swapping which one is active touches any file outside the providers folder, that boundary is broken; fix the interface, not the caller."

---

#### M2-P3
- **Lane:** Claude Code
- **Milestone:** M2
- **Goal:** Wire `POST /extract` end to end so it makes one real extraction call and returns a proposed value with a pinned source region.
- **Depends on:** M2-P1 and M2-P2 both committed. Live Bedrock access should be confirmed from the 11:00 AWS briefing before this prompt is fired for real; if it is not yet confirmed, build and test this against the seed entry from M2-P2 and note that live confirmation is still pending.

> Implement `POST /extract` exactly as `BUILD_SPEC_v1.md` section 4 describes it. Given a case and a single field, call the currently configured `ModelProvider` with an extraction request built from the relevant source document, and return a result containing both a proposed value and a specific source region, the exact location in the source document the value came from. A proposed value with no source region is not an acceptable result under any circumstance; treat "I couldn't find a region" as a signal to abstain, never as a reason to guess one. Route every call through the run recorder from the previous prompt so it lands in the run log automatically, with no extra step. Expect to iterate on the wording of the extraction request you send to the model several times within this same prompt, against fixture pack v1, until it reliably returns a usable source region for a single-source field; that iteration is expected and normal, keep refining within this prompt rather than stopping after the first attempt. This endpoint does not decide between conflicting sources and does not touch any field that has more than one candidate source; that begins in M3. Write this fresh from the spec section; do not reuse an extraction prompt template from the public ATTEST prototype.

**Acceptance checks:**
1. Calling `POST /extract` for a single-source field against fixture pack v1 returns a proposed value and a specific, non-empty source region pointing at the real location in the source document.
2. The call produces a new entry in the run log automatically, with prompt hash, parameters, response, and latency all present.
3. Calling it a second time produces a second, distinct run log entry rather than a cached or skipped one.
4. No response ever contains a proposed value with a missing, empty, or fabricated source region.
5. The endpoint does not attempt to resolve or select between any multi-source field; those fields are untouched by this prompt.

**Expected minutes:** 50-70

**Failure mode:** the model returns a plausible value with no usable source region, and under time pressure the fix is to invent a region rather than treat the gap correctly. **Fallback prompt:** fire rescue prompt R2 in Section D.


### Milestone M3: the evidence engine spine, and the first three screens (Hour 5-10, Fri 19:00-Sat 00:00)

This is the biggest milestone in the sprint. Engine work (P1-P3) and screens work (P4-P6) can run concurrently once their own dependencies are committed; they do not have to run strictly in prompt-ID order end to end, only within their own track.

#### M3-P1
- **Lane:** Claude Code
- **Milestone:** M3
- **Goal:** Implement the field state machine and conflict detection so disagreeing sources land a field in CONFLICTED, a field with no source lands in UNSUPPORTED, and nothing ever auto-resolves either.
- **Depends on:** M2-P3 and M1-P4 both committed.

> Read `BUILD_SPEC_v1.md` section 3's Field and Conflict schemas and section 6's planted-conflict matrix before writing anything. Implement the field state machine: a field is SUPPORTED when exactly one source carries it, CONFLICTED when two or more sources carry it and disagree, UNSUPPORTED when no source carries it at all. Run every field in a case through this classification using fixture pack v1's four source documents. This is the single most important rule in the whole system, so implement it deliberately: nothing in this code path ever picks a winner among disagreeing candidates, averages them, prefers one source over another, or invents a value for an unsupported field. A CONFLICTED or UNSUPPORTED field's only job here is to preserve every candidate value with its own source region attached and sit there, unresolved, until a human decides in a later milestone. Verify your classification against `BUILD_SPEC_v1.md` section 6's planted-conflict matrix field by field; each of the four fields in fixture pack v1 has a specific, different, intended outcome, and getting the right count of CONFLICTED fields without the right fields being the ones actually conflicted is a failure, not a near miss. Write this fresh from the spec sections; do not adapt a resolution or matching algorithm you recall from any other system.

**Acceptance checks:**
1. Running fixture pack v1's four fields through this logic produces the exact state each one is designed to produce, cross-checked field by field against `BUILD_SPEC_v1.md` section 6, not eyeballed.
2. A CONFLICTED field's result includes every disagreeing candidate value, each with its own source region, not just one value chosen quietly.
3. The UNSUPPORTED field's result contains no fabricated value of any kind, empty or placeholder included.
4. A manual walk-through of the code confirms there is no tie-breaking, averaging, or default-preference branch anywhere in this path.
5. Re-running the classification against fixture pack v1 a second time reproduces identical results for all four fields.

**Expected minutes:** 60-80

**Failure mode:** under time pressure, a quiet tie-breaker gets added "so something shows up on screen" instead of nothing. **Fallback prompt:** "Remove any tie-breaking or default-value logic entirely. If a CONFLICTED or UNSUPPORTED field renders with no chosen value and that looks broken, that is a screens problem for the next prompt to solve, not a reason to add a hidden default here."

---

#### M3-P2
- **Lane:** Codex A
- **Milestone:** M3
- **Goal:** Implement the decision endpoint requiring a named human and a non-empty reason, and enforce maker-checker so the decider cannot also be the signer.
- **Depends on:** M3-P1 committed.

> Read `BUILD_SPEC_v1.md` section 3's Decision and Signoff schemas and section 4's API table entries for `/decide` and `/signoff`. Implement `POST /decide`: reject any call missing a named human or carrying an empty or blank reason string, with no field state change on rejection; on a valid call, transition a CONFLICTED or UNSUPPORTED field to DECIDED and record which human decided, their reason, and which candidate they chose. Implement maker-checker enforcement inside `POST /signoff` itself, not only in the frontend: reject a signoff where the signing human is the same named human who made any of the decisions being signed off on, and reject any signoff while any field in the case is still CONFLICTED or UNSUPPORTED. Test the reject paths as deliberately as the accept path; a maker-checker rule nobody tried to break is a rule nobody has actually verified. This is new backend logic written from the named spec sections; do not reuse decision or approval-flow code from any prior Kriseva or ATTEST codebase.

**Acceptance checks:**
1. Calling `/decide` with no named human, or an empty reason, is rejected and the field's state does not change.
2. Calling `/decide` with a named human and a real reason moves the field to DECIDED and records both the human and the reason.
3. Calling `/signoff` with the same human who made the decision is rejected by the backend itself, called directly, not just blocked by a disabled button.
4. Calling `/signoff` with a different named human succeeds once every field is DECIDED or naturally SUPPORTED.
5. Calling `/signoff` while any field is still CONFLICTED or UNSUPPORTED is rejected and the case state does not advance.
6. A manual test using CANON's own maker and checker persona names produces the correct accept and reject outcomes in both directions.

**Expected minutes:** 55-70

**Failure mode:** maker-checker is enforced only in the frontend, and a direct call to the backend endpoint bypasses it entirely. **Fallback prompt:** "This check has to live in the endpoint itself. Call `/signoff` directly, skipping the UI, with the same human as decider, and confirm the server rejects it before you call this done."

---

#### M3-P3
- **Lane:** Codex A
- **Milestone:** M3
- **Goal:** Implement the SHA-256 manifest chain over every artifact and state transition, and a tamper check that visibly breaks when one byte changes.
- **Depends on:** M3-P2 committed.

> Read `BUILD_SPEC_v1.md` section 8's manifest and hash spec in full. Implement `GET /manifest/:id` per section 4's API table, computing a SHA-256 chain over every artifact belonging to the case (source documents, proposed values, decisions, signoffs) and every state transition it passed through, exactly as section 8 specifies how the chain is built. Then implement a tamper check: a way to re-verify a previously issued manifest against the case's current data and detect any change since the manifest was issued, down to a single byte. Prove it works before calling this done: alter one byte in one artifact after sealing, run the tamper check, and confirm it flags the change in a way a non-technical judge could understand at a glance, not just a raw hash string that means nothing to a stranger. Write the chain construction and the tamper check fresh from section 8; do not port a hashing or manifest implementation from any earlier project.

**Acceptance checks:**
1. `GET /manifest/:id` returns a hash chain covering every artifact and every state transition for a fully decided and signed case.
2. Requesting the manifest twice with no change in between produces an identical chain both times.
3. Altering one byte in any single artifact after the manifest was issued causes the tamper check to fail, specifically and visibly, not silently.
4. The tamper failure is legible to a non-engineer: it says what broke in plain terms, not only a hash mismatch.
5. The manifest can be exported and re-verified without the original live case still running, proving it is genuinely portable.

**Expected minutes:** 50-65

**Failure mode:** the "tamper check" recomputes nothing and only compares the manifest to a stored copy of itself, so it can never fail. **Fallback prompt:** "This must recompute a fresh hash from the case's current artifacts and compare it against the sealed chain, not compare the seal to itself. Change one real byte and show the check catch it before you call this done."

---

#### M3-P4
- **Lane:** Codex B
- **Milestone:** M3
- **Goal:** Build the case dashboard screen (S1): all four fields and their states visible at a glance.
- **Depends on:** M3-P1 committed.

> Read `BUILD_SPEC_v1.md` section 5's entry for screen S1 and its acceptance checks. Build it as static HTML, CSS, and vanilla JavaScript, calling the backend's `GET /case/:id`. Every field's current state (SUPPORTED, CONFLICTED, UNSUPPORTED, DECIDED, CONFIRMED) must be immediately visible without clicking into another screen, and the different states must be visually distinct from each other in shape or label, not only in colour; a CONFLICTED field and an UNSUPPORTED field need to read as different things at a glance, the same way the project's own design principle says the four planted-conflict causes must look visibly different rather than like one state relabelled. The synthetic disclosure must be visible on this screen, not buried in a footer. This is new frontend code written from the spec section; do not reuse markup or styling from the public ATTEST prototype's wireframes beyond what the wireframe PDF itself, already committed to `docs/`, is meant to guide.

**Acceptance checks:**
1. Loading the dashboard for a fully extracted case shows all four fields and each one's current state without any further clicks.
2. The different field states are visually distinct in shape or label, not just recoloured versions of the same badge.
3. A CONFLICTED field and an UNSUPPORTED field are distinguishable from each other at a glance.
4. The synthetic disclosure is visible on the screen itself.
5. Changing a field's state through the API and reloading the dashboard reflects the change immediately, with no stale cached view.

**Expected minutes:** 30-40

**Failure mode:** every state gets the same badge shape in a different colour, so a judge skimming fast cannot tell CONFLICTED from UNSUPPORTED. **Fallback prompt:** "Colour alone isn't enough here. Give each state its own label and its own shape or icon, not just a different colour on an identical pill."

---

#### M3-P5
- **Lane:** Codex B
- **Milestone:** M3
- **Goal:** Build the evidence workspace screen (S2): every proposed value pinned to its exact source region.
- **Depends on:** M2-P3 and M3-P4 both committed.

> Read `BUILD_SPEC_v1.md` section 5's entry for screen S2. Build it so that opening a field from the dashboard shows every candidate value proposed for it, each one visibly connected to the exact region of the source document it came from, shown or highlighted in context, not just named as a citation. For a CONFLICTED field, show every disagreeing candidate side by side with its own source and its own cut-off or version detail, so a reviewing human can see why they disagree, not only that they do. For the UNSUPPORTED field, show clearly that no candidate exists at all, in a way that reads as intentional rather than broken. Build this fresh from the spec section; do not reuse markup, styling, or data-binding code from the public ATTEST prototype beyond the wireframe PDF's layout guidance.

**Acceptance checks:**
1. Opening the workspace for a single-source field shows its one proposed value and its exact source region, visibly linked, not two unrelated text blocks.
2. Opening it for the CONFLICTED fields shows every disagreeing candidate side by side, each with its own source region, with none pre-selected or visually favoured.
3. Opening it for the UNSUPPORTED field clearly communicates that nothing was found, not a blank or broken-looking screen.
4. Which document, and where relevant which version, each candidate came from is visible without extra clicks.
5. The synthetic disclosure is visible on this screen.

**Expected minutes:** 35-45

**Failure mode:** candidates show up as plain text with a document name label, but the source region itself is never actually shown or highlighted, so "pinned to source" is true in the data model but not on screen. **Fallback prompt:** "A document name next to a value is not a pin. Show or highlight the actual region of the source the value came from, not just which document it's in."

---

#### M3-P6
- **Lane:** Codex B
- **Milestone:** M3
- **Goal:** Build the conflict decision screen (S3): every candidate stays visible, no default winner, reason mandatory.
- **Depends on:** M3-P2 and M3-P5 both committed.

> Read `BUILD_SPEC_v1.md` section 5's entry for screen S3. Build it so every candidate for a CONFLICTED or UNSUPPORTED field stays visible with equal visual weight; none is pre-selected or marked as recommended. The human must actively choose a candidate (or, for the UNSUPPORTED case, actively confirm there is nothing to choose) and type a non-empty reason before submitting is possible. Wire submission to `POST /decide` from the engine work in this milestone, and surface the backend's own rejection clearly on screen if the reason is empty or the human name is missing, rather than trusting browser-side validation alone to be the only line of defence. Write this screen fresh from the spec section; do not reuse decision-form markup or validation code from any prior repository.

**Acceptance checks:**
1. Loading the screen for a CONFLICTED field shows every candidate with equal visual weight; none is pre-selected.
2. Submitting with no candidate chosen, or with an empty reason, is blocked in the browser, and separately confirmed rejected if sent straight to the backend.
3. Submitting a valid choice with a named human and a real reason succeeds, and the field shows as DECIDED after reload.
4. The recorded reason and the deciding human's name remain visible after the decision is made.
5. The synthetic disclosure is visible on this screen.

**Expected minutes:** 35-45

**Failure mode:** the browser blocks an empty reason, but a direct call to the backend endpoint still succeeds with one, meaning the real enforcement only lives in JavaScript. **Fallback prompt:** "Confirm the backend itself rejects an empty reason independent of the browser. If it doesn't, that's a regression in M3-P2, fix it there before touching this screen again."


### Milestone M4: eval harness, risk board (Hour 10-15, Sat 00:00-05:00)

This window carries the nap schedule (one founder 02:00-04:30, the other 04:30-07:00 spilling into M5); it is deliberately lighter on prompts than M3. The awake human still reviews every commit before it lands, nap or no nap.

#### M4-P1
- **Lane:** Codex A
- **Milestone:** M4
- **Goal:** Expand the synthetic generator's output into the full labelled evaluation set the eval harness will score against.
- **Depends on:** M1-P3 committed.

> Read `SCHEMA_PACK.md`'s eval label format section and `BUILD_SPEC_v1.md` section 7's eval protocol. Extend the generator, or write a sibling script alongside it, to emit between 50 and 100 labelled items in the exact format `SCHEMA_PACK.md` specifies, covering a realistic mix of SUPPORTED, CONFLICTED, and UNSUPPORTED outcomes per section 7's protocol, not one skewed toward easy items. For CONFLICTED and UNSUPPORTED items, the ground-truth label is "abstain is correct," not a specific expected value; do not label these with a value you happen to think is right. Every ground-truth label must trace back to the project's canonical numbers and planted-conflict matrix; none are invented. In your summary, flag the items you are least confident about so a human review can be fast and targeted instead of a blind re-check of all of them. This extension is new code written from the two named spec sections; do not import a labelled-eval-set generator from any other project.

**Acceptance checks:**
1. The labelled set contains between 50 and 100 items, matching `SCHEMA_PACK.md`'s eval label format field for field.
2. CONFLICTED and UNSUPPORTED items are labelled "abstain is correct," never given a specific expected value.
3. Every ground-truth value traces back to the project's canonical numbers; a spot check of five items confirms none were invented.
4. The mix of outcome types is realistic per `BUILD_SPEC_v1.md` section 7, not skewed toward easy single-source items.
5. A human has reviewed the set and signed off on it before it is handed to the eval harness.

**Expected minutes:** 40-55

**Failure mode:** the labelled set leans almost entirely on easy SUPPORTED items, so the eval score looks better than the system's real behaviour on the cases that actually matter. **Fallback prompt:** "Rebalance this set. It needs to stress conflicts and unsupported cases in realistic proportion; a set built to flatter the score is worse than no eval at all."

---

#### M4-P2
- **Lane:** Claude Code
- **Milestone:** M4
- **Goal:** Run the labelled set through the extraction and abstention pipeline and emit one results table scoring both extraction accuracy and abstention correctness.
- **Depends on:** M4-P1, M3-P1, and M2-P2 all committed.

> Read `BUILD_SPEC_v1.md` section 7's eval protocol and scoring rules in full. Implement `GET /eval/run` per section 4's API table: run every item in the labelled set through the same extraction and conflict-detection pipeline already built, using `ReplayProvider` so the run is deterministic, repeatable, and costs no Bedrock credits. Score two separate things, exactly as section 7 defines them: whether the extracted value matches ground truth on SUPPORTED items, and whether the system correctly abstained, rather than silently picking a value, on CONFLICTED and UNSUPPORTED items. A silent pick on a planted-conflict item is a failure and must show as one in the table; do not average it away into a single blended accuracy percentage that hides which failure mode occurred. Output one table the pitch can show as is. Write the harness fresh from section 7; do not reuse a scoring or eval-runner implementation from any prior Kriseva or ATTEST codebase.

**Acceptance checks:**
1. `GET /eval/run` processes every item in the labelled set without making any live Bedrock call.
2. The results table reports extraction accuracy and abstention correctness as two separate, clearly labelled numbers, not one blended score.
3. Running the harness twice in a row produces identical results, confirming it runs on `ReplayProvider`.
4. At least one deliberately planted conflict item is confirmed, by name, as correctly abstained in the output.
5. Any item where the system silently guessed instead of abstaining is listed individually in the table, not folded into an aggregate.

**Expected minutes:** 60-80

**Failure mode:** the harness reports one blended accuracy number that can go up even when the system guesses instead of abstaining on a planted conflict, hiding the exact failure the product exists to prevent. **Fallback prompt:** "Split this into two numbers: extraction accuracy and abstention correctness. List every item where the system guessed instead of abstaining, by name, directly in the table."

---

#### M4-P3
- **Lane:** Codex B
- **Milestone:** M4
- **Goal:** Build the risk and anomaly board screen (S5): deterministic indicators, each closed only by a named disposition.
- **Depends on:** M3-P2 committed.

> Read `BUILD_SPEC_v1.md` section 5's entry for screen S5. Build a screen that surfaces risk indicators computed directly from real case data already produced by the engine (fields still CONFLICTED or UNSUPPORTED, a case pending signoff, a case whose manifest is not yet sealed), not a new hidden scoring model and not static example content. Each indicator can only be closed by a named human providing a disposition, in the same spirit as the decision endpoint's mandatory reason; a checkbox with no name and no explanation attached does not satisfy this. This screen and its underlying indicator logic are new code written from section 5; do not reuse risk-board markup or logic from any earlier project.

**Acceptance checks:**
1. The board lists every currently open indicator for a case, computed from live case data, with nothing hardcoded as a permanent demo placeholder.
2. Reproducing the same case state twice produces the same set of open indicators both times.
3. Attempting to close an indicator without a named human and a disposition is rejected.
4. Closing an indicator with a named human and a disposition removes it from the open list and records who closed it and why.
5. The synthetic disclosure is visible on this screen.

**Expected minutes:** 40-55

**Failure mode:** the board ships with a handful of static, hardcoded example risks that never move no matter what the underlying case data does, because wiring live indicators ran out of time. **Fallback prompt:** "These must come from live case data. If time is short, cut the number of indicator types to two or three real ones instead of keeping a longer list of fake ones."


### Milestone M5: AWS hosting, remaining screens, failure-mode demo, polish (Hour 15-19, Sat 05:00-09:00)

#### M5-P1
- **Lane:** Claude Code
- **Milestone:** M5
- **Goal:** Deploy the working system to AWS following the deployment steps and the answers confirmed at the 11:00 briefing.
- **Depends on:** M3-P6 committed.

> Read `BUILD_SPEC_v1.md` section 9's AWS deployment steps. Before touching AWS, confirm with the human exactly what the 11:00 briefing settled: credits amount, account type, region, which hosting path is simpler given the credits (S3 and CloudFront, or a single small EC2 or App Runner instance), and whether S3 Object Lock is available or only plain versioning. Do not assume any of these; ask if they were not written down. Then set up: an S3 bucket for manifests and fixtures with versioning on, static hosting for the frontend via whichever path was confirmed, an IAM user or role scoped to least privilege for exactly what this service needs and nothing broader, CloudTrail left on, and an AWS Budgets alarm set at 50 percent of the confirmed credits so they cannot silently run out mid-sprint. This is new deployment configuration written from the spec section and the briefing's answers, not copied from any prior project's infrastructure setup.

**Acceptance checks:**
1. The frontend and backend are reachable at a public URL, not only on localhost.
2. The S3 bucket for manifests and fixtures has versioning enabled, matching what the briefing confirmed.
3. The IAM identity used by the deployed service holds only the permissions it actually calls, not a broad policy.
4. CloudTrail is confirmed on for the account and region in use.
5. An AWS Budgets alarm exists, set at 50 percent of the confirmed credits.
6. A manifest generated on the deployed instance and one generated locally for the same case produce the identical hash chain.

**Expected minutes:** 70-100

**Failure mode:** AWS setup friction (a permissions error, a service not enabled for the event account) burns the window and nothing deploys. **Fallback prompt:** if the blocker is Bedrock or credential-specific, fire rescue prompt R1 in Section D. Otherwise: "Stop chasing the ideal path. Deploy only the static frontend to S3 with public read, keep the backend reachable through a tunnel for the live demo, and say exactly that in the honesty table; a smaller, honestly labelled deployment beats a bigger broken one."

---

#### M5-P2
- **Lane:** Codex B
- **Milestone:** M5
- **Goal:** Build the agent trace screen (S4): model id, prompt hash, latency, and a LIVE or RECORDED badge per call, with replay of any past run.
- **Depends on:** M2-P2 committed.

> Read `BUILD_SPEC_v1.md` section 5's entry for screen S4. Build a screen listing real entries from the run log, each showing its model id, prompt hash, latency, and a clearly labelled LIVE or RECORDED badge read from that specific entry, never a badge fixed once for the whole screen. Selecting a past run replays it through `ReplayProvider` and reproduces the exact result it originally returned, proving the system is inspectable rather than a black box. Write this fresh from section 5; do not reuse trace-viewer or replay UI code from the public ATTEST prototype.

**Acceptance checks:**
1. The screen lists real entries from the run log, not placeholder rows.
2. Each entry shows its model id, prompt hash, latency, and a clearly labelled LIVE or RECORDED badge.
3. A LIVE entry and a RECORDED entry are visually distinguishable at a glance.
4. Selecting a past run and replaying it reproduces the identical response it originally returned.
5. The synthetic disclosure is visible on this screen.

**Expected minutes:** 45-60

**Failure mode:** the LIVE/RECORDED badge is set once at build time instead of read per entry, so every run shows the same badge regardless of how it was actually produced. **Fallback prompt:** "Read the badge from each individual run log entry, not a fixed value for the whole screen. Show one LIVE and one RECORDED run side by side with different badges before calling this done."

---

#### M5-P3
- **Lane:** Codex A
- **Milestone:** M5
- **Goal:** Build the sign-off screen (S6): a second named human, different from the decider, confirms the case.
- **Depends on:** M3-P2 committed.

> Read `BUILD_SPEC_v1.md` section 5's entry for screen S6. Build a screen showing every field's decided value, the deciding human's name, and their reason, all visible before signoff is attempted. Require the signing human's name, wire submission to `POST /signoff`, and surface the backend's actual rejection message on screen, in something close to its own words, whenever maker-checker blocks the attempt; a generic "signoff failed" message defeats the purpose of a screen whose whole job is to make the rule visible. Build this screen fresh from section 5; do not reuse sign-off markup or logic from any prior repository.

**Acceptance checks:**
1. The screen shows every field's decided value, deciding human, and reason before signoff.
2. Attempting signoff as the same human who decided produces a specific, readable on-screen explanation of why it was rejected.
3. Signing off as a different named human succeeds once every field is DECIDED or SUPPORTED.
4. Attempting signoff while any field is still CONFLICTED or UNSUPPORTED is blocked with a clear on-screen reason.
5. The synthetic disclosure is visible on this screen.

**Expected minutes:** 30-40

**Failure mode:** every rejection shows the same generic error text, so a judge watching maker-checker fire cannot tell which rule actually stopped the signoff. **Fallback prompt:** "Show the real reason the backend gave, close to word for word, not a generic failure message. The rule being visible is the entire point of this screen."

---

#### M5-P4
- **Lane:** Codex A
- **Milestone:** M5
- **Goal:** Build the receipt and manifest screen (S7): the sealed hash chain and a live, repeatable tamper demonstration.
- **Depends on:** M3-P3 committed.

> Read `BUILD_SPEC_v1.md` section 5's entry for screen S7. Build a screen showing the sealed manifest for a signed case: its hash chain, presented so a non-technical judge can follow it, the case's key identifying details, and the synthetic disclosure. Add a one-click, on-screen action that triggers the tamper check live: it mutates a copy of the case's data by one byte and re-runs verification in front of the viewer, showing the chain visibly break with no page reload needed to see the before-and-after. After triggering it, the untampered state must be showable again so the demo is repeatable without restarting the whole case. Write this screen fresh from section 5; do not reuse manifest-viewer or tamper-demo code from the public ATTEST prototype.

**Acceptance checks:**
1. The screen shows the sealed manifest's hash chain for a fully signed case.
2. The synthetic disclosure and the case's key identifying details are visible on this screen.
3. Triggering the tamper demonstration visibly and immediately shows the chain breaking, on screen, without a manual file edit.
4. The untampered state can be shown again afterward without restarting the case.
5. The manifest can be exported or downloaded from this screen in a portable form.

**Expected minutes:** 35-45

**Failure mode:** the tamper demonstration requires hand-editing a file on disk mid-demo, too fragile and slow to run live in front of judges. **Fallback prompt:** "Build a one-click, on-screen tamper trigger that mutates a copy of the data and re-runs the check. Nobody should touch a file system live in front of judges."

---

#### M5-P5
- **Lane:** Claude Code
- **Milestone:** M5
- **Goal:** Prove the abstention mechanism catches a genuinely wrong model output, through the real engine, with nothing staged.
- **Depends on:** M3-P1 and M2-P2 both committed.

> Read `BUILD_SPEC_v1.md` section 10's demo script mapping for how this moment fits the pitch. Construct one scenario, served through `ReplayProvider` so it is repeatable on demand, where the model proposes an incorrect or overconfident value, for example guessing a number for the field that has no supporting document at all. Prove that the exact same conflict-detection and abstention logic already built earlier today, with no special case added for this scenario, catches it and blocks it from being silently accepted. If the general engine does not catch it on its own, that is a real bug in the engine to fix, not a demo to fake around with scenario-specific code. Configure this scenario fresh from fixture pack v1 and the spec; do not reuse a failure-mode or demo-rigging script from any prior project.

**Acceptance checks:**
1. The wrong-answer scenario is served through `ReplayProvider` and reproduces identically on every run.
2. The code path that catches this scenario is the exact same one used for every other field, with no added special case for this scenario specifically.
3. Running this scenario through the M4 eval harness also flags it correctly, confirming the same logic is doing the work.
4. A human watching can see, on screen, the exact moment the system declines the model's proposed value.
5. The scenario replays on demand with no manual data-fixing between runs.

**Expected minutes:** 30-45

**Failure mode:** under time pressure, the only reliable way to make the "catch" work is to special-case this one scenario, defeating the point of the demo entirely. **Fallback prompt:** "If this only works because of code written specifically for this scenario, remove that code. Either the real engine catches this because abstention genuinely applies, or this is not a truthful demo to run in front of judges."

---

#### M5-P6
- **Lane:** Codex B
- **Milestone:** M5
- **Goal:** Pass over all seven screens for consistent styling, loading states, and error states now that all seven exist.
- **Depends on:** M5-P2, M5-P3, and M5-P4 all committed.

> With all seven screens now built, pass over them for visual consistency (shared spacing, type, and colour use, following the wireframe PDF already committed under `docs/`), deliberate loading states so nothing flashes as broken before data arrives, and readable error states so a backend failure shows a human-readable message rather than a raw stack trace on screen. This is a styling and edge-state pass only; do not change behaviour built in any earlier prompt. If you find an actual behaviour bug while polishing, stop and flag it to the human rather than quietly fixing engine logic inside this pass. Any styling code you add here is written fresh for this pass; do not import a CSS framework, theme, or component library from any other project, including the public ATTEST prototype, beyond the wireframe PDF's guidance.

**Acceptance checks:**
1. All seven screens share consistent spacing, typography, and colour language.
2. Loading a screen before its data arrives shows a deliberate loading state, not a flash of broken layout.
3. Forcing a backend error (for example, requesting a case id that does not exist) shows a readable message on every screen that calls the backend.
4. Re-running each earlier screen prompt's own acceptance checks still passes; nothing regressed.
5. The synthetic disclosure styling is consistent across all seven screens.

**Expected minutes:** 45-60

**Failure mode:** a polish pass quietly changes engine-facing behaviour while "cleaning up" a component, breaking an earlier acceptance check without anyone noticing until the demo. **Fallback prompt:** "Re-run every earlier screen prompt's acceptance checks right now. If anything regressed, revert the specific change that broke it and keep only the styling."

---

#### M5-P7
- **Lane:** Codex A
- **Milestone:** M5
- **Goal:** Draft the README's structure and setup instructions, leaving the honesty table itself for M6.
- **Depends on:** M5-P1 committed.

> Draft `README.md`: one plain-language paragraph on what the project is, with no banned marketing language; how to run it locally, backend, frontend, generator, and eval harness, in order, tested from a clean checkout rather than written from memory of the plan; how to switch between LIVE and RECORDED model providers using the environment variable M2-P1 and M2-P2 actually built. Leave a clearly marked placeholder section for the SYNTHETIC/MOCKED/LIVE honesty table; do not fill it in now, it needs the finished system's true state and would go stale before it is used. Draft this README's wording fresh; do not copy phrasing from any prior Kriseva or ATTEST README.

**Acceptance checks:**
1. Following the README's setup instructions from a clean checkout actually works, tested by a human, not assumed.
2. The LIVE/RECORDED environment variable is documented accurately, matching the real implementation.
3. No banned marketing language appears anywhere in the README.
4. A clearly marked, empty placeholder exists for the honesty table.
5. The project's synthetic, fictional nature is stated plainly near the top of the README.

**Expected minutes:** 20-30

**Failure mode:** the README describes how the system was supposed to work rather than how it actually works, because it was written from the plan instead of tested against the real setup. **Fallback prompt:** "Follow your own instructions from a clean checkout right now, and fix every step that doesn't actually work as written."


### Milestone M6: pitch integration, honesty table, rehearsal (Hour 19-21, Sat 09:00-11:00)

Both founders are on pitch and rehearsal work in this window; the agent lanes are mostly idle or on docs, by design. Only two prompts fire here.

#### M6-P1
- **Lane:** Claude Code
- **Milestone:** M6
- **Goal:** Fill in the SYNTHETIC/MOCKED/LIVE honesty table with the system's true, final state and finalize the README.
- **Depends on:** M5-P7 committed, and the rest of the system frozen enough to describe truthfully.

> Go through every screen in the running system and every claim the pitch might make, and for each one, mark it plainly as SYNTHETIC (fictional data, always true here), MOCKED or RECORDED (a replayed fixture standing in for a live call), or LIVE (a real Bedrock call happening right now), matching `BUILD_SPEC_v1.md` section 10's demo script mapping so the table and the actual demo flow agree line for line. Do not round up: if something sometimes runs live and sometimes falls back to replay depending on the connection, say exactly that rather than choosing the more impressive label. Fold this table into the placeholder section left in the README, then read the whole README start to finish for accuracy against the system as it behaves right now, not as it was planned to behave this morning. Write the honesty table's wording fresh from what you actually observe; do not copy phrasing from any prior Kriseva or ATTEST honesty table or disclosure document.

**Acceptance checks:**
1. Every row in the honesty table corresponds to a real, currently running part of the system, checked live rather than written from memory of the plan.
2. No row is rounded up to a more impressive label than what is actually true right now.
3. The honesty table's claims match `BUILD_SPEC_v1.md` section 10's demo script mapping line for line.
4. The full README contains no banned marketing language and no em dash anywhere.
5. A human has walked the running system screen by screen and confirmed each honesty table row against what they actually saw.

**Expected minutes:** 30-40

**Failure mode:** the honesty table gets written from the original plan rather than from what the system does right now at freeze time, and a claim quietly goes stale before the pitch. **Fallback prompt:** "Walk the running system screen by screen, right now, and rewrite each row from what you actually observe, not from what the plan said this morning."

---

#### M6-P2
- **Lane:** Codex B
- **Milestone:** M6
- **Goal:** Add a deterministic reset mechanism for rehearsal, and confirm the full spine runs offline end to end for the screen-recording backup.
- **Depends on:** M5-P2 and M3-P3 both committed.

> Add a reset or reseed action, clearly separated from the product's real API surface so a judge never mistakes it for a product feature, that returns a case to its freshly extracted, pre-decision state on demand. This lets the team rehearse the full demo spine (ingest, propose with source pins, hit conflict, abstain, a named human decides with reason, maker-checker signs, seal, a tamper attempt breaks the seal) as many times as needed with no hand-editing of data between run-throughs. Then, with the network disabled entirely, confirm the whole spine runs start to finish purely on `ReplayProvider`, since the screen-recording backup must survive a venue with no live connection at all. This reset mechanism is new code in service of rehearsal; it is not a substitute for the humans actually rehearsing the pitch three times, which stays a human task outside this prompt.

**Acceptance checks:**
1. Triggering the reset returns a case to its pre-decision state, confirmed by loading the dashboard afterward.
2. The reset can be triggered repeatedly with no manual data cleanup in between runs.
3. With the network fully disabled, the demo spine runs start to finish using only `ReplayProvider`, with no errors caused by an absent connection.
4. The reset mechanism is clearly separated from the real product API surface.
5. The screen-recording backup, captured after this prompt, plays back the complete spine with no visible gaps or errors.

**Expected minutes:** 30-40

**Failure mode:** the "offline" run still depends on one stray network call (a font, an icon, an accidental fetch) that only surfaces once the recording is attempted with the network genuinely off. **Fallback prompt:** "Disable the network fully, not just the Bedrock call, and reload from scratch. Find and fix whatever still tries to reach out; the recording backup has to survive a venue with no signal."


---

## Section D: The rescue prompts

Short, break-glass prompts for the five situations most likely to actually happen. Fire the matching one the moment you recognize the situation; do not wait for a milestone boundary. Whoever hit the blocker fires it, in whichever lane they are in.

#### R1: Bedrock access denied

**Fire when:** `BedrockProvider` throws its access-denied error (built in M2-P1), or the 11:00 briefing itself reveals model access has not actually landed for this account yet.

> Bedrock access is currently denied or unconfirmed. Confirm `ReplayProvider` is the active default provider right now, using the environment variable switch already built; this should be a configuration change, not new code. Add a clearly visible on-screen note wherever the system would otherwise claim LIVE, stating plainly that it is running on recorded fixtures because Bedrock access is not yet confirmed. Do not attempt another live call until a human confirms access has actually been granted. If any code change is genuinely needed beyond configuration, write it fresh from the spec; do not fall back to a fixture-serving shortcut copied from elsewhere. Do not spend personal API credit as a workaround; any such spend needs founder sign-off first, per standing company rule.

---

#### R2: the model returns a value with no usable source region

**Fire when:** `/extract` returns a proposed value but its source region is empty, generic, or clearly not a real location in the document.

> A proposed value came back with no usable source region. Tighten the extraction request so a specific, checkable source region is a mandatory part of the response shape, not an optional extra. Treat any response missing a genuine region as equivalent to having no candidate at all for that source: it must flow into the CONFLICTED or UNSUPPORTED path like a missing source would, never get accepted as SUPPORTED with a placeholder or invented region standing in for a real one. Re-run against fixture pack v1 and confirm every field currently accepted as SUPPORTED now carries a real, checkable region before calling this fixed. Fix this with new code written from the named spec section; do not port a region-extraction workaround from any other project.

---

#### R3: the frontend and backend disagree on a shape

**Fire when:** a screen renders wrong or breaks because what the frontend expects from an endpoint does not match what the backend actually returns.

> Stop patching either side to match the other side's guess. Open `BUILD_SPEC_v1.md`'s data model section (section 3) and API table (section 4) together, confirm the exact field names and types they specify for this endpoint, and regenerate whichever side, frontend call, backend response, or both, does not match the spec exactly. The spec is the tie-breaker here, not whichever side happens to have been written more recently. Regenerate the mismatched side fresh from the spec; do not patch it by copying a shape from any other codebase you may know.

---

#### R4: a test suite will not go green with 90 minutes left

**Fire when:** it is roughly 90 minutes from freeze and a failing automated test is eating review cycles that should be going toward the demo path.

> Stop iterating on this test. Verify the actual behaviour by hand instead: run it, click it, per the review discipline in Section A. If the real behaviour is correct and only the test's own assertion or setup is wrong, mark the test as a known skip with a one-line reason in the commit message and move on. If the real behaviour is genuinely wrong, that is a cut-list decision, not more time spent chasing this one test; escalate to rescue prompt R5 instead. A passing demo beats a passing test suite with 90 minutes on the clock. If any code change is needed to mark the skip or fix real behaviour, write it fresh from the spec; do not patch in a workaround copied from elsewhere.

---

#### R5: "we are behind, apply the cut list"

**Fire when:** a milestone is running significantly over its hour budget and the team needs to protect the core spine rather than the full scope.

> We are behind schedule. Stop all new-feature work immediately. Apply `BUILD_SPEC_v1.md` section 12's ranked cut list in order: cut public API polish first, then risk-board depth, then the second document type, then hosting niceties. Do not cut any of the following, under any circumstance: the live model call, the conflict-abstain-decide-seal loop, manifest integrity, the honesty table, or the end-to-end demo path. Report back exactly which items you cut and what remains standing, so the humans can decide whether further cuts are needed. Any change you make while cutting scope is a subtraction or a simplification of code already written today; do not paper over a cut by pulling in a pre-built replacement from elsewhere.


---

## Section E: The freeze checklist (Hour 21-22, Sat 11:00-12:00)

No agent prompts fire in this hour. This is a human-only checklist, read together, out loud, before anyone walks to the judging room.

1. **Sweep for uncommitted work.** Anything left uncommitted from M6 gets one last honest commit, correct `M<milestone>: <what> [by <name>]` convention, correct author, nothing bundled in under a vague message.
2. **Confirm milestone tags exist.** Tags M1 through M6 should already exist from earlier in the day, each pointing at the commit where that milestone's own acceptance checks last passed, not all bunched at the final commit. Backfill any that were missed, against the correct historical commit, not against tonight's last commit.
3. **Tag the freeze.** Add one final tag marking the freeze point itself, after the sweep commit lands.
4. **Push everything.** Confirm the remote has every commit and every tag, not just the local copy.
5. **Read the git history back, start to finish, as the audit will read it.** The first commit is docs and `NOTICE.md` only, timestamped after 14:00 Friday. Every commit after it follows the naming convention and carries a real human name. No commit is timestamped before the official start. No single commit after the first introduces a suspiciously large, fully formed feature with no earlier partial commits building up to it; a fixture pack generated in one shot is expected and fine, a complete seven-screen UI appearing whole in one commit is not, and the team should be ready to explain any commit a judge points at.
6. **Confirm no rehearsal-branch material leaked in.** This week's timed rehearsal builds lived on throwaway branches that were deleted; confirm none of their commits or branches made it into the history being pushed.
7. **Cross-check `NOTICE.md` one more time** against the actual `docs/` folder and the actual commit history: every pre-event artifact it names is really there, and nothing else in the repository predates 14:00 Friday.
8. **Confirm the README's honesty table still matches the live system**, not the state it was in when M6-P1 was fired; if anything changed since, fix the table now, in this checklist, without firing a new agent prompt for a one-line edit.
9. **Grep the full history for anything resembling a secret, key, or token** and confirm nothing of the kind was ever committed.
10. **Run the full demo spine once more, end to end:** ingest, propose with source pins, hit conflict, abstain, a named human decides with reason, maker-checker signs, seal, tamper attempt breaks the seal. Live if Bedrock is up, replay if it is not, and know which one you are about to show.
11. **Confirm the screen-recording backup is saved in at least two places** (both laptops, or a laptop plus cloud storage), so one device failing does not take the fallback down with it.
12. **Note the AWS credit and budget-alarm state** in case a mentor asks, and in case the account needs pausing after judging.
13. **Read the six milestone tags back out loud, in order,** M1 through M6, each earlier than the next, as the last check before leaving for the judging room.

---

## Open founder decisions

| # | Question | What this playbook did in the meantime |
|---|---|---|
| 1 | `CANON.md` section 12, item C1: "Is the second founder Mahek or Mahek Soni? War room docs 00/01/07 say Mahek Soni; docs 08/10 and APPLICATION_UPDATE_BANK say Mahek." | This playbook mirrors `04_CLEAN_START_BUILD_KIT.md` section 6 and `05_AGENT_SYSTEM.md` section 3 exactly as instructed, and both name "Mahek Soni" throughout for the Codex seat 2 lane and its human lead. Every lane, human-lead, and commit-author reference to the second founder in this playbook therefore reads "Mahek Soni." `CANON.md`'s own stated default, if this is left unanswered, is "Member 2" or "Mahek." The founder needs to reconcile this before Friday, since it changes the literal name typed into `[by <name>]` on every commit Codex B produces, and it should match whatever name goes on the form and the badge. |

