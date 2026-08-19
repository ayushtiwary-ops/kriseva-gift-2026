# MAHEK PACK

## 1. What is yours, in four lines

1. You drive the laptop for the full 70-second demo. Ayush narrates, you click. Every shot's recovery action in the storyboard is written for your hands, not his.
2. You deliver the honesty-table beat at 2:35 in the 3-minute pitch, the single highest-scoring ten seconds in the whole pitch.
3. You own the eval labels: every grade on whether the model proposed the right answer is yours, start to finish.
4. You are the domain-vocabulary check. If a line does not sound like something a compliance officer would actually say, you are the one who catches it before it ships.

Driving is not the junior job. Look at the ten shots in the storyboard again: every single one carries a named recovery action, and in all ten, that action belongs to you, not Ayush. He talks for 70 seconds and nothing he says can break. You are the one clicking a real, unrehearsed interface in front of a jury, and if the tamper file in shot 10 does not upload cleanly, you are the one who switches to the backup tab in under two seconds without the room noticing you did it. The demo has exactly one moving part that can fail live. That part is your hands.

## 2. The ten things to know cold

**1. The four documents.** D1 is the administrator's quarterly statement (Northwind, version 2). D2 is the subscription register (Meridian Alpha, internal). D3 is the internal ledger export (Meridian Alpha, internal). D4 is the custodian's holdings and cash confirmation (Sentinel). They disagree because each is a snapshot cut at a different moment by a different party, not because anyone made an error.

**2. Administrator versus custodian.** The administrator, Northwind, does the accounting: it computes NAV and issues the official statement. The custodian, Sentinel, independently confirms the cash and holdings actually exist. Splitting the two matters because no single firm should both do the arithmetic and vouch for it being real.

**3. Committed capital.** What an investor has signed up to contribute, the ceiling. USD 42,500,000 is correct. The subscription register shows 45,000,000 because it counts a fourth LP whose subscription is signed but not yet counter-executed, meaning not yet legally binding.

**4. Drawn capital.** What has actually been called and paid in so far. USD 19,300,000 is correct. The administrator and custodian both show 17,800,000 because their books closed at 16:00 IST on 30 June, and a 1,500,000 capital call landed at 17:42, after that cutoff. The internal ledger caught it.

**5. NAV.** Net Asset Value: what the fund is actually worth right now, assets minus liabilities. USD 21,940,500 is correct. The administrator restated this figure on 8 July after correcting an unlisted holding, and the internal ledger still carries the pre-correction number.

**6. The quarterly return and its clock.** Every FME files four times a year, 21 calendar days after quarter end: 21 April, 21 July, 21 October, 21 January. Our demo quarter ends 30 June 2026, so the return is due 21 July 2026.

**7. The missing field.** Complaints closed this quarter is not in any of the four documents. Not a disagreement, a total absence. The system marks it UNSUPPORTED and produces nothing, because a guessed zero looks like an answer and it is not one.

**8. What abstention means.** When the system has two candidate answers, or none, it does not guess. It shows every source it found, with no recommended winner, and it blocks progress until a named person picks one and writes down why.

**9. Why refusing is the product.** A confidently wrong number is what gets a fund into enforcement trouble. A system that says "I do not know, here is everything I found" is worth more to a compliance officer than one that is fast and occasionally wrong. That is the whole pitch in one sentence.

**10. Maker-checker.** The person who decides a conflicted field cannot be the person who signs it off. Priya decides, Rajiv signs, and the rule is enforced by the system itself, not by policy, which is why it would hold even behind a real login screen we have not built yet.

## 3. Her exact spoken lines

Say this once, clearly, at 2:35. Nothing else in this pack needs to be word for word.

> **"Zero customers, zero pilots, zero revenue on ATTEST. We have not spoken to a practising compliance officer yet. That is exactly what the residency is for."**

Delivery note: flat, not apologetic. Do not smile through it and do not speed up to get past it. It lands harder slow. Take a half-beat pause after "revenue on ATTEST" before the second sentence. This is the one line in the whole pitch that is supposed to sound like you are giving something up, not selling something.

## 4. The demo drive sheet

Print this side. It is what you hold, not what you say.

| Shot | Time | You click | If it breaks |
|---|---|---|---|
| 1 | 0-5s | Nothing. Sweep the cursor once across the four field rows. | Refresh once, keep sweeping. |
| 2 | 5-10s | Click the F4 row. | Click F4 again, once. |
| 3 | 10-15s | Click "Confirm no source found, escalate." Reason snippet auto-fills. Click Submit. | Click Submit once more, move on regardless of the chip. |
| 4 | 15-25s | Click the F2 row, then tabs D1, D3, D4 in order. | Skip the stuck tab, circle back to it. |
| 5 | 25-40s | Click "Review conflict." | Switch to Replay mode for this case. |
| 6 | 40-45s | Click the trace icon beside the F2 conflict. | Nothing to fix. RECORDED instead of LIVE is a designed fallback, not a failure. |
| 7 | 45-55s | Click the USD 19,300,000 / D3 card. Reason snippet auto-fills. Click Submit. | Click Submit once more, move to the next shot regardless. |
| 8 | 55-60s | Click "Send for sign-off," alt-tab to Rajiv's window, click "Confirm and sign." | Stay on the greyed Priya view, let Ayush talk, move on. |
| 9 | 60-65s | Wait for SEALED and the manifest to render. | Wait two seconds, click Verify once more. |
| 10 | 65-70s | Upload the pre-altered manifest file. | Switch immediately to the pre-recorded tab. No second live retry, ever. |

One rule covers all ten rows: one retry, then move on. Never two.

## 5. Eight likely questions with her answers

**What actually is a fund administrator?**
"The firm a fund pays to keep the books: track money coming in, calculate NAV each period, send the official statement. In our demo that is Northwind. They are not the fund and not the regulator, just the record keeper."

**Why do the documents disagree?**
"Because each one is cut at a different moment by a different party. A capital call landed after the administrator's cutoff, so the ledger caught it and the statement did not. Both were right when they were made."

**What does the product do when it is not sure?**
"It stops and shows you everything it found, with no recommended answer, instead of guessing. A named person has to pick and write down why. We built it to refuse rather than hand you a confident wrong number."

**What did you personally build?**
"I own every evaluation label the model gets graded against, and I checked every field against how a compliance officer actually talks, not how an engineer assumes they talk. That vocabulary work is in the product right now."

**You are an MBA. What did you actually contribute technically?**
"I did not write the engine. I wrote the labels that grade whether its answers are right, and I drive tonight's demo, which means I know every screen well enough to keep it alive under pressure. That is ownership, not a codebase line count."

**What is the difference between committed capital and drawn capital?**
"Committed is what an investor has signed up to give, the ceiling. Drawn is what has actually been called and paid in so far. In our fund that is 42.5 million committed against 19.3 million drawn."

**Why does a custodian exist separately from an administrator?**
"The administrator does the accounting. The custodian independently confirms the cash and holdings are actually there. Splitting the two means no single firm can both do the arithmetic and vouch for it being real."

**What is NAV, and why does it matter here?**
"Net Asset Value: what the fund is actually worth right now, assets minus liabilities. It is the number investors watch most closely, and in our case the administrator's own number changed after a correction, the kind of change only a person catches."

## 6. What to say when she does not know

The sentence, exact, every time: **"I do not have a verified figure for that, and I will not invent one."**

Why it scores: the rubric gives 20% to Honesty & Roadmap Credibility. A founder who invents a plausible-sounding number under pressure fails that criterion instantly, and usually invisibly, because the room cannot check it live. A founder who states the boundary of what she knows, on the record, in front of a regulator's own event, proves the product's central claim about herself before she says another word.

The handoff, so it never reads as a rescue: **"Ayush, that one is yours, you have the source."** Say it forward, not sideways. Do not glance at him first and do not drop your voice. You are naming which of you holds which fact, the same division the product itself enforces between the person who decides and the person who signs.

## 7. The three-hour prep plan

**0:00-0:45, drive sheet.** Run all ten shots on the actual build, twice through, no narration. Extra reps on shot 5 and shot 10, they carry the most weight and the least room for a second failure.

**0:45-1:00, break.**

**1:00-1:45, the ten things.** Read them once aloud. Then get quizzed out of order, no notes, until every answer comes back in under fifteen seconds.

**1:45-2:15, the eight questions.** Speak every answer aloud, timed. If an answer runs past 45 words, cut it live in the moment. Do not build a separate shorter version to memorise.

**2:15-2:30, the honesty line and the not-knowing sentence.** Repeat both until they come out flat and automatic, not performed.

**2:30-3:00, one combined run.** Drive the demo for real while Ayush narrates for real, deliver the honesty beat at its actual place in the pitch, timed against a clock, start to finish.

**Skip entirely:** the 23,000-word pack, the technical benchmarks in FACT_CARD section 8 (that is Ayush's ground if a technical juror pushes), Ayush's narration lines, and the risk-and-anomaly screen, which is not shown in the 70 seconds at all.

## 8. One-page cheat card

**The four fields, at curtain-up**
F1 Committed Capital: CONFIRMED. F2 Drawn Capital: CONFLICTED, you take it live to DECIDED. F3 Closing NAV: DECIDED, one signature pending. F4 Complaints Closed: UNSUPPORTED, you take it live to DECIDED.

**The four documents, and who issues each**
D1 Administrator statement, v2: Northwind. D2 Subscription register: Meridian Alpha, internal. D3 Internal ledger export: Meridian Alpha, internal. D4 Custodian confirmation: Sentinel.

**Five numbers, never wrong**
1. Committed capital: USD 42,500,000.
2. Drawn capital, the correct answer: USD 19,300,000.
3. Closing NAV: USD 21,940,500.
4. Filing clock: 21 calendar days after quarter end.
5. The cutoff gap: administrator closed books 16:00 IST, the capital call landed 17:42 IST, both 30 June.

**Your line, 2:35**
"Zero customers, zero pilots, zero revenue on ATTEST. We have not spoken to a practising compliance officer yet. That is exactly what the residency is for."

**When you do not know**
"I do not have a verified figure for that, and I will not invent one."
