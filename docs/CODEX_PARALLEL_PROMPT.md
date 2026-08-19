# CODEX PARALLEL WORK ORDER

Written 2026-08-19. Purpose: give Codex a lane that runs at the same time as the Claude lanes without either one stepping on the other.

## How to run it

Open a second terminal. Change into the rehearsal build directory. Start Codex. Paste the block below the line.

```bash
cd ~/kriseva-rehearsal-DELETE-BEFORE-21AUG/attest
```

**File ownership is the whole trick.** Five Claude lanes already own `scripts/generate.js`, `src/engine.js`, `src/manifest.js`, `src/server.js`, `src/providers.js`, `src/recorder.js`, `src/eval.js`, `public/*` and `tests/engine.test.js`, `tests/manifest.test.js`, `tests/eval.test.js`. Codex owns a completely different set, listed in the prompt. Nothing overlaps, so nothing collides.

Codex's lane is the hardening lane: the things that make the difference between a demo that survives one run and a demo that survives a hostile juror asking for a second one.

---

## THE PROMPT (paste everything below this line)

You are working inside a rehearsal build of KRISEVA ATTEST, at `~/kriseva-rehearsal-DELETE-BEFORE-21AUG/attest`. This build is deleted before 21 August. Nothing here goes to the venue.

Read `docs/CONTRACT.md` in full before writing anything. It defines the data shapes, the API and the rules the engine enforces. It is short.

Five other agents are working in this directory right now, in parallel with you. **You own exactly these files and no others:**

- `src/verify-cli.js`
- `src/seed-demo.js`
- `tests/integration.test.js`
- `tests/rules.test.js`
- `scripts/demo-check.sh`
- `scripts/reset.sh`
- `docs/RUNBOOK.md`

If you need something from another file, read it and code against it. Never edit it. If a file you depend on does not exist yet, wait, retry, and code against `docs/CONTRACT.md` in the meantime. Do not create another lane's file even as a stub.

Node 25, ES modules, zero npm dependencies, Node standard library only.

Build these six things, in this order.

**1. `src/verify-cli.js`, a standalone verifier.**

Run as `node src/verify-cli.js data/case-CASE-2026-Q1-MER001.json`. It reads an exported case or receipt file, recomputes the entire SHA-256 manifest chain independently, and prints whether the evidence is intact. If the chain is broken it names the first `sequenceIndex` that fails, what kind of entry it was, and how many entries after it are therefore also unverifiable.

This matters more than it looks. It is the artifact that lets someone check our evidence without running our product, and that is the difference between a claim and a proof. Import only `canonicalJson` from `src/manifest.js` and recompute everything else yourself, so the verifier is genuinely independent of the engine that produced the file. Exit code 0 when verified, 1 when broken.

**2. `src/seed-demo.js`, the one-command demo reset.**

Run as `node src/seed-demo.js`. It drives the local API from a cold start to the exact state the demo begins in: case ingested, extraction complete, four fields sitting in their four different states, nothing decided yet. It must be idempotent, so running it twice gives the same state, and it must finish in under five seconds.

The reason this exists: during rehearsal you will run the demo twenty times. Resetting by hand twenty times is where mistakes and wasted minutes come from.

**3. `tests/rules.test.js`, adversarial tests of the product's actual promises.**

Not happy-path tests. Write tests that try to break the rules the product sells. At minimum, prove that each of these is impossible:

- Signing off while any field is still conflicted or unsupported.
- The same named person both deciding a field and signing the case off.
- Recording a decision with an empty reason, a whitespace-only reason, or a missing reviewer name.
- A field ending up with a value that no source document supports.
- A conflicted field silently resolving to one candidate without a human decision.
- Mutating a sealed case without the manifest chain detecting it.
- Two candidates with the same value being reported as a conflict (they agree, so that is not a conflict).

For each, assert that the attempt is rejected AND that the rejection message says why in plain English. A rejection with an unhelpful message is a half-failure, because that message appears on screen.

**4. `tests/integration.test.js`, the whole loop end to end.**

Start the server on a test port, then drive the complete path over HTTP: ingest, extract, inspect, attempt an invalid decide, make a valid decide on all conflicted and unsupported fields, attempt sign-off by the decider and confirm it is refused, sign off by a second person, fetch the manifest and confirm verified is true, call the tamper endpoint, fetch the manifest again and confirm verified is false with the correct broken index. Tear the server down cleanly. Skip gracefully with a clear message if the server files are not ready yet.

**5. `scripts/demo-check.sh`, the pre-stage pre-flight.**

A shell script that runs in under 30 seconds and prints a checklist with a pass or fail against each line: server responds, both cases load, the four fields are in the four expected states, the model provider mode (LIVE or RECORDED) and which model id, the manifest verifies, the tamper path breaks it, the verifier CLI agrees, and the eval results file exists. Exit non-zero if any line fails.

This is what gets run five minutes before walking on stage. Make the output readable at a glance by a tired person, one line per check, the verdict in the first characters of the line.

**6. `scripts/reset.sh` and `docs/RUNBOOK.md`.**

`reset.sh` deletes generated state, regenerates the corpus, restarts clean. `RUNBOOK.md` is one page: how to start it, how to reset it, how to run the demo, what each script does, and the three most likely failures with their fixes.

Constraints on everything you write. No em dashes anywhere, including comments and error messages. Do not use the words cutting-edge, revolutionary, seamless, disruptive, transformative, world-class, state-of-the-art, unlock or empower. Every user-visible string is plain English a compliance officer would understand. No dependencies. Small functions, plain names, no cleverness.

Run everything you write. Do not report a file as finished because it exists. Report it as finished when you have run it and read the output. If something fails because another lane has not landed yet, say so specifically rather than working around it by writing their file.

When you are done, reply with: the exact commands that prove each of the six items works, the count of tests passing, and any place where the contract was ambiguous and you had to choose.

---

## Why this split works

The Claude lanes build the product. Codex builds the things that prove the product does what we say, plus the operational scaffolding that makes twenty rehearsal runs cheap.

There is a second reason to give this lane to Codex specifically. The adversarial tests in item 3 are written by an agent that did not write the engine. An engine's author tends to test what they built; a stranger tests what was promised. That is a better test suite, and it is also, on the day, a good answer to a juror who asks how we know the rules actually hold.
