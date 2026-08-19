# DEMO SCRIPT: the full walkthrough, for showing anyone

Written 2026-08-19. This is the script for demoing to a person in a room, not the 70-second stage version. That one is `DEMO_STORYBOARD.md`. Use this to explain the product end to end, take questions, and find out what confuses people.

Target length: 8 to 10 minutes spoken, plus questions.

---

## Before you start, 60 seconds

One command. It rebuilds the corpus, restores all eight fictional entities, starts the
server, puts the demo case in its opening state, and runs every gate.

```bash
cd ~/kriseva-rehearsal-DELETE-BEFORE-21AUG/attest && bash scripts/demo-ready.sh
```

Open `http://localhost:4000`. It ends with either `DEMO READY` or `NOT READY`, and the
failing gate is printed directly above. Do not demo until it says ready.

**Mode note, and say this out loud when it comes up:** the demo runs on recorded model responses. That is deliberate. It is instant, it is identical every time, and the badge on the trace screen says RECORDED so nobody has to guess. The live path works and we can show it on one field in about two seconds. We do not run the full live pipeline on stage because it takes minutes, and we would rather tell you that than hide it.

---

## Part 1: the problem, 90 seconds, before you touch the laptop

Laptop closed or screen away.

> "A fund in GIFT City has to file a quarterly return three weeks after quarter end. One number on that return, drawn capital, lives in three different documents. The administrator says 17.8 million. The internal ledger says 19.3 million. The custodian agrees with the administrator.
>
> Nobody is lying. Nobody made a mistake. A capital call of 1.5 million landed at 17:42 on the 30th of June, and the administrator had already drawn its line at 16:00. Both documents are correct as at their own cut-off.
>
> Today an AI tool reads all three, picks one, and moves on. Eleven months later the regulator asks which document that number came from and who decided. The honest answer is that nobody knows."

Then, only if they are a finance person, add:

> "IFSCA took 19 enforcement actions in the first half of 2026 alone. Two ended in cancellation of registration."

---

## Part 2: the dashboard, 60 seconds

Open the app.

> "This is one quarterly return for a fictional fund. Everything you see is synthetic and it says so on every screen. Four numbers have to go on this return. Here is what we found for each."

Nothing on this screen is written in machine vocabulary. Every status is a short sentence, every regulatory term keeps its proper name and carries a plain gloss underneath, and every status carries a one-line explanation on the card rather than behind a hover. If anyone asks what a term means, the header has a "What these words mean" panel with all of it in one sentence each.

Point at each:

- **Committed capital**, *what investors have promised to put in*. Chip reads **Sources disagree**, tag reads **Counting different things**. The register counts a subscription that is signed but not counter-executed. It is not wrong, it is answering a different question.
- **Drawn capital**, *how much of that has actually been called in*. Chip reads **Sources disagree**, tag reads **Different cut-off times**. This is the timing case, and it is the one that proves the thesis.
- **Closing NAV**, *what the fund was worth at the end of the quarter*. Chip reads **Sources disagree**, tag reads **One document was corrected later**. The administrator restated on the 8th of July; the ledger was built from the version before that.
- **Complaints closed**, *how many investor complaints were resolved this quarter*. Chip reads **No source found**, tag reads **Nothing to read**. No document in this quarter contains it at all.

> "Four disagreements, four genuinely different reasons. That matters, because a system that treats them identically has not understood any of them."

Then point at the panel above the cards, "The shape of this fund".

> "Four bars, and three of them stop early and go hatched. That hatching is the part the documents do not agree on. Most dashboards in this category would draw one confident bar here, which means picking a number. Picking is the thing we refuse to do, so the picture refuses too. Watch what happens to it when a person decides."

If anyone asks whether this only works for one fund, use the entity selector in the top strip.

> "Twelve quarterly returns, eight fictional fund managers, and between them every failure mode we have designed for: different cut-offs, a late correction, two documents counting different things, parts that do not add up, two currencies with no rate given, a figure from the wrong quarter, and a field nothing covers at all. Same four numbers, same four states, same refusal."

---

## Part 3: the evidence, 90 seconds

Click into drawn capital.

> "Every proposed number is pinned to the exact place it came from. Not the document. The character range."

Click a candidate. The source text appears with the quote highlighted.

> "That highlight is verified, not trusted. The model told us where it found this. We then searched the document ourselves and confirmed the number is actually there. If we cannot confirm it, we drop the candidate. The model proposes; we check."

Then the line that lands hardest:

> "And here is what it worked out on its own. The gap between the two numbers is exactly 1.5 million. The ledger contains one movement of exactly 1.5 million, timestamped 17:42, after the administrator's 16:00 cut-off. So the system can tell you not just that they disagree, but why. Nobody wrote that sentence in. It derived it."

Then point at the box headed "If nobody looked".

> "This is the ordinary thing. Take the number the most documents agree on and move on. On this field that rule files 17.8 million, because the administrator and the custodian both say so and only the ledger disagrees. It is the most reasonable rule in the world and here it is wrong, and nothing in either document announces it. After Priya decides, this box tells you the size of the gap she just closed."

Each candidate card carries its own provenance, and it is worth reading one out loud:

> "Who wrote it, and whether that is an outside party or your own record. What moment it was true as at. When it reached you. Whether it replaced an earlier version. And the exact words on the page. That is what a supervisor eleven months from now needs, and it is the part every tool in this category leaves out."

---

## Part 4: the refusal, 60 seconds. This is the product.

Go to complaints closed.

> "No document reports this. So the system produces nothing.
>
> Today, a compliance officer facing this box types a number, because the form will not submit empty, and signs it under her own name. Zero is the most dangerous answer in regulatory reporting, because it looks like an answer.
>
> Here it stays empty and blocks sign-off. If she still has to file, she records it as an attestation: her name, her reason, and no source. On the receipt it looks different from the other three, permanently."

---

## Part 5: the agents, 90 seconds

Open the trace screen.

> "Nine roles ran on this case. Not one of them can decide anything.
>
> A planner worked out which documents matter for which fields. Triage pruned the work. Extractors ran in parallel, one per document. A binder verified every quote against the source. A validator checked the arithmetic, and that one is deterministic code, not a model, because a model cannot be trusted to verify a model. A critic ran on a different model family from the extractor, specifically so it can disagree independently. A reconciler explained the disagreements. A narrator wrote the summary.
>
> The models are Amazon Nova, Mistral, GLM and Kimi. Three different families, on purpose. If we ran the same model twice we would get correlated errors, and the criticism would be theatre."

Then the point:

> "Every one of those actions is in the same sealed record as the human's decision. The agent trace is not a log next to the audit trail. It is the audit trail."

---

## Part 6: the human, 60 seconds

Go to the conflict decision screen.

> "Neither value is preselected. There is no default and no recommendation, because the moment we recommend, we have made the decision and just moved the blame."

Try to submit without a reason. It refuses.

> "A decision without a written reason is not an audit trail, it is a number."

Enter a reason, decide. Then try to sign off as the same person.

Read the refusal aloud:

> "Priya cannot sign off because Priya already decided a field on this case, and maker-checker requires the person who confirms to be someone other than the person who decided."

> "That is enforced in the engine. Not in the interface, not in a policy document, not in a prompt. You cannot click your way around it."

Sign off as Rajiv.

---

## Part 7: the seal, 90 seconds. The ending.

Open the receipt.

> "Every step is hash-chained. Three of these numbers are bound to a document you can open. The fourth is a named person's word with nothing behind it, and it is marked that way."

Click tamper.

> "Now somebody edits one number after the fact."

Refresh the chain. It breaks visibly.

> "It names the exact entry that broke and every entry after it, because each link depends on the one before. That is a real hash chain, not a picture of one."

Then the closer:

> "And we did not just test that ourselves. We had a second, independently written verifier check our work. It disagreed with us, and it was right: we were not validating one field of the chain. We fixed it. You can run that verifier without running our product."

```bash
node src/verify-cli.js data/case-CASE-2026-Q1-MER001.json
```

---

## Part 8: the track record, 60 seconds. Use this when they ask "so what"

Click **History**.

> "This fund has filed four quarterly returns before this one. Same four numbers every time. Look at the middle column."

Point at the disagreements column.

> "The same disagreement, every single quarter. That is the thing worth understanding. It is not an incident, it is how this fund receives its documents: an administrator who closes at four, a ledger that keeps running until midnight. Nobody is going to fix that, because nobody is doing anything wrong."

Then point at the rightmost column, the numbers with no document.

> "And every quarter, one number with nothing behind it. Complaints closed. Four quarters, four times somebody had to put their own name to a number, because the form will not submit empty."

If you are showing Nilgiri rather than Meridian, switch to it and point at the note.

> "This one is the case I would want you to look at. Three quarters settled by one compliance officer. She left. Her successor inherits the same conflict and, in every tool that exists today, none of the reasoning, because it lived in her head and an email thread. Here it is still on the record, in her words, against her name, and it will still be there in eight years, which is how long these records have to survive."

Then the honest boundary:

> "Everything in that history is synthetic. We built it to show the shape of the problem over time. We have not run a real quarter for a real fund, and we will not claim we have."

---

## The five questions you will actually get, and the answers

**"Is the AI accurate?"**
> "I do not have an accuracy number I would defend, and I am not going to invent one. What I can show you is the eval harness: 67 labelled items, and it scores whether the system correctly refused separately from whether it extracted correctly. Abstaining on a genuine conflict counts as correct. Silently picking counts as a failure even when the number happens to be right."

**"Why not just use one good model?"**
> "For extraction you could. The reason for a second model family is criticism. If the same model checks its own work you get correlated errors. Different lineages disagree in different places, and disagreement is the signal we act on."

**"What if the agents get it wrong?"**
> "Then a human sees a conflict instead of a wrong answer. That is the whole design. The system is built so that its failure mode is asking rather than guessing."

**"Could I run this on my own data?"**
> "Not today, and I would not want you to. Everything here is synthetic by design. The next step is running it inside a fund's own perimeter on their real documents, and that is what the residency is for."

**"How long did this take?"**
> "The specification took a week. The code was written in one sitting, from that specification, by agents, with a human reviewing every change before it was committed. The commit history shows it."

---

## What to watch for while they use it

Say nothing. Write down every moment they hesitate. Specifically:

- Do they understand the four states without being told?
- Do they notice the abstention, or scroll past it?
- Does anyone try to click a value before reading the reason?
- Does the tamper moment land, or need explaining?
- What do they ask first when you stop talking?

The first question they ask unprompted is the one the pitch should already have answered.
