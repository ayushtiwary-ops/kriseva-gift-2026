# DEMO STORYBOARD: the 70-second live demo, shot by shot

Status: DRAFT, founder voice pass and timed rehearsal needed. Owner: founder. Built from CANON.md (locked 2026-08-18) and FACT_CARD.md (compiled 2026-08-18, updated 2026-08-19). Companion file: PITCH_3MIN.md, where this exact sequence sits inside the 0:40-1:50 window, grouped into 10-second rows that cite these shot numbers.

Every number on screen in this storyboard is a CANON.md section 5 number. Nothing here is invented for effect. Shot boundaries are set on 5-second marks on purpose, so this file and PITCH_3MIN.md can be read against the same stopwatch.

---

## The demo contract

One continuous flow. No cuts, no page reloads that could fail, no tab-switching except the two designed fallbacks named below. Rehearsed to under 70 seconds. Member 2 drives: Member 2 is the only one touching the keyboard and trackpad, clicking every element named in this document. Ayush narrates: Ayush is the only one speaking during the 70 seconds, reading the narration lines verbatim once rehearsed. This is a deliberate division, not an accident: a single narrating voice keeps the room's attention on one thread, and a single driving hand means only one person's muscle memory has to be perfect.

The case is pre-seeded before curtain-up. It is not built live on stage. Building the synthetic data live happened Friday during the sprint; what the jury watches Saturday is a saved case loaded at rehearsed state. This is disclosed, not hidden: the S1 dashboard itself carries the SYNTHETIC watermark, and Ayush's opening line in PITCH_3MIN says the documents are fictional before the demo starts.

Two of the four fields are pre-seeded ahead of curtain-up: F1 (Committed Capital) already reads "Signed off", and F3 (Closing NAV) already reads "You decided" with one signature still pending. This is a deliberate time-budget cut, not a limitation of the product: the engine resolves all four planted conflicts, but a 70-second demo cannot walk all four to completion on stage without rushing the one that matters most. F2 (Drawn Capital, the timing conflict) and F4 (Complaints Closed, the missing field) are live and untouched at curtain-up. Those two get the full treatment: conflict, abstention, decision, reason, signature.

S5 (Risk and Anomaly Board) is intentionally not shown in the 70 seconds. It exists, it is in the build, and it is fair game if a judge asks to see more in Q&A. Cutting it from the spine is the same ranked-cut discipline the build itself runs on: never cut propose-abstain-decide-sign-seal, cut everything else first.

---

## Pre-flight checklist (run in the 5 minutes before going on stage)

1. Case loaded: Meridian Alpha Opportunities Fund I, quarter ended 30 June 2026, pre-seeded state confirmed. On screen the four chips read "Signed off", "Sources disagree", "You decided" (one signature pending) and "No source found". Refresh once, confirm it renders clean.
2. Agent trace badge checked: run one throwaway call in the minutes before curtain-up and confirm it reads LIVE, not RECORDED. If Bedrock is slow or down, flip to RECORDED mode deliberately now, not discover it mid-shot.
3. Second browser window pre-logged in as Rajiv Menon (Principal Officer), pinned and ready to alt-tab to for shot 8. Do not attempt a live login on stage.
4. Reason-text entries pre-staged as one-click snippets for the two live decisions (F2 and F4), tested to insert in under 2 seconds. Nobody free-types a full sentence live under a clock.
5. Tamper file ready: a second copy of the sealed manifest with one byte already altered, saved and one click away, so shot 10 is an upload, not a live edit.
6. Recorded-backup video cued on a second tab, scrubbed to 0:00, volume checked. Includes a clean capture of the shot 10 seal-break specifically, scrubbable to on its own.
7. Hotspot on both phones on and tested as the network fallback; laptop on hotspot if venue wifi is weak, not discovered mid-demo.
8. Screen readable test: zoom level checked from the back of the room, font size bumped if the room is large.
9. Timer visible to both founders, started at Ayush's first demo word, not before.
10. Water for both founders. Laptop charged past 80 percent, charger connected and taped down.

---

## Shot list

### Shot 1, 0-5s
**Screen:** S1, Case dashboard
**Action:** Dashboard already loaded, cursor idle. SYNTHETIC watermark visible top-right of the screen. Member 2's cursor sweeps left to right, once, across the four field cards without clicking: F1 Committed capital (green chip, "Signed off"), F2 Drawn capital (amber chip, "Sources disagree", tag "Different cut-off times"), F3 Closing NAV (blue chip, "You decided", tag "One document was corrected later", "1 of 2 signatures"), F4 Complaints closed (grey dashed chip, "No source found", tag "Nothing to read"). Every chip carries a plain one-line explanation under it, and every field label carries a plain gloss under it, so nothing on the sweep needs translating.
**Narration:** "One fund, one quarterly return. Four fields, four states, one screen."
**Proves:** Technical Execution (30): the state model is real and visibly differentiated, not one screen relabelled four times. Problem Depth (20): a live regulatory case with four distinct evidence problems in one artifact.
**Fallback:** If the dashboard is blank or slow to render, Member 2 hits refresh once (session stays logged in, should be instant). Ayush says: "Give us one second, the case is loading," and keeps talking through the field count while it resolves. If still broken after 5 seconds, cut to the recorded backup (see protocol below).

### Shot 2, 5-10s
**Screen:** S2, Evidence workspace (field F4, Complaints Closed)
**Action:** Member 2 clicks the F4 row. Evidence workspace opens showing an empty state: "0 of 4 source documents contain this field." No source pins, no candidate value, no text-entry box for a number.
**Narration:** "Complaints closed this quarter. Not in any document. Most tools still hand you a number."
**Proves:** Honesty & Roadmap Credibility (20): abstention shown live, not claimed. Problem Depth (20): the missing-field failure mode is a distinct case from a conflict, and it looks different on screen.
**Fallback:** If the empty-state panel fails to render, Member 2 clicks the F4 row again once. Ayush says: "This is the field with nothing behind it, that's the whole point, one more second." If still broken, narrate the empty state verbally without the screen and move straight to shot 3's decision language, then catch up visually at shot 4.

### Shot 3, 10-15s
**Screen:** S2 to S3 transition, field F4
**Action:** Member 2 clicks Review on the F4 card. The screen that opens is titled "Put your name to a number", not "Choose between the sources": there is nothing to choose between, so the words change. Member 2 types the number, a pre-staged reason snippet inserts in one click, and clicks "Record this as my word". The chip flips from "No source found" to "Your word, no document", with Priya Ramanathan's name attached and no source document named.
**Narration:** "Watch it refuse. Zero is the most dangerous answer here, because zero looks like an answer. Priya cannot decide this one, because there is nothing to decide between. She can only put her own name to it, and the receipt will say so."
**Proves:** Founder & Venture Assessment (30): this is a designed product judgment call, not a missing feature. Honesty (20): the CANON line on missing data, spoken live over the actual UI behaviour it describes. Technical Execution (30): a decision and an attestation are separate acts in the engine, and the interface refuses to blur them.
**Fallback:** If Submit hangs, Member 2 clicks once more. Ayush says: "That decision is Priya's, recorded either way, let's keep moving," and proceeds to shot 4 without waiting for the visual confirmation to catch up on screen.

### Shot 4, 15-25s
**Screen:** S2, Evidence workspace (field F2, Drawn Capital)
**Action:** Member 2 clicks the F2 row. Evidence workspace opens with three source tabs, each showing a highlighted pinned region: D1 Northwind administrator statement (USD 17,800,000, cut-off 30 Jun 2026 16:00 IST), D3 internal ledger export (USD 19,300,000, cut-off 30 Jun 2026 23:59 IST), D4 Sentinel custodian confirmation (USD 17,800,000, cut-off 30 Jun 2026 16:00 IST). Member 2 clicks each tab in turn, D1, D3, D4.
**Narration:** "Drawn capital, the number investors care about most. Three sources. Administrator: seventeen point eight million. Custodian: seventeen point eight. Ledger: nineteen point three. Each one pinned to its source."
**Proves:** Technical Execution (30): evidence binding to exact source regions is the architecture, shown live, not asserted. Problem Depth (20): real fund-reporting documents disagree with each other, and this is what that looks like.
**Fallback:** If a source tab fails to load its highlighted region, Member 2 skips to the next tab and back. Ayush keeps narrating the numbers from memory (they are on the fact card) without waiting on the highlight to render, and folds the missed tab into shot 5's framing instead.

### Shot 5, 25-40s
**Screen:** S3, Conflict decision (field F2)
**Action:** Member 2 clicks "Review conflict." Conflict decision screen loads with two candidate cards side by side: D1/D4 at USD 17,800,000 (cut-off 16:00 IST) and D3 at USD 19,300,000 (cut-off 23:59 IST). Neither card is pre-highlighted, no "recommended" badge on either.
**Narration:** "Two documents. Two correct answers. The administrator's books closed at four PM on the thirtieth. A capital call landed at seventeen forty-two that afternoon. The ledger caught it, the statement could not. Both documents are correct. No algorithm resolves this, only a person who knows what happened that afternoon."
**Proves:** Problem Depth & Regulatory Realism (20): this is the star conflict, the whole thesis in one screen: two sources can both be right and still disagree. Founder & Venture Assessment (30): this is the line a judge remembers, and it is the reason the company exists. This shot carries the most time of any in the demo, on purpose.
**Fallback:** If the conflict-decision screen fails to load both cards, Member 2 flips to the pre-loaded Replay mode for this exact case (a real, disclosed feature, not an improvised patch). Ayush says: "Same case, recorded run, identical numbers, let me pull it up," and narrates over the replayed screen without breaking stride.

### Shot 6, 40-45s
**Screen:** S4, Agent trace
**Action:** Member 2 clicks the trace icon beside the F2 conflict. A panel slides in showing: model ID, prompt hash, latency in milliseconds, and a badge reading LIVE in green.
**Narration:** "This panel is the model call. Model ID, prompt hash, latency, a LIVE badge."
**Proves:** Technical Execution & Architecture (30): the model call is real, inspectable, and running on the day, meeting the rubric's "live, not canned" requirement directly. Honesty (20): the LIVE/RECORDED badge is the honesty mechanism made visible.
**Fallback:** If the badge reads RECORDED instead of LIVE because the live call actually failed, do not panic and do not hide it. Ayush says: "That badge just told us the truth, this one served from the recorded fixture, not live, that's the safeguard working exactly as built." Keep moving. This turns a technical failure into a proof of the honesty claim.

### Shot 7, 45-55s
**Screen:** S3, Decision submission (field F2)
**Action:** Member 2 clicks the USD 19,300,000 / D3 candidate card. A mandatory reason field appears. Pre-staged reason snippet inserts in one click ("Capital call of USD 1,500,000 landed 17:42 IST, 30 Jun 2026, after administrator's 16:00 cut-off. Ledger reflects actual drawn position."). Member 2 clicks "Record decision". The chip flips to "You decided", Priya Ramanathan's name and timestamp attached, and the band on "The shape of this fund" collapses to a single bar in front of the room.
**Narration:** "Priya picks nineteen point three million. Her reason goes on the record. The field moves to Decided. Her name is on it, permanently."
**Proves:** Founder & Venture Assessment (30): a named human making a defensible, evidenced call is the product's actual value proposition. Technical Execution (30): the mandatory non-empty reason string is an enforced rule, not a text box that could be left blank.
**Fallback:** If Submit hangs, Member 2 clicks once more. Ayush says: "The system will not let that field move without her name and her reason, that's the rule, watch the next screen," and continues into shot 8 regardless of whether the chip visibly updates in time.

### Shot 8, 55-60s
**Screen:** S6, Sign-off (fields F2 and F4)
**Action:** Member 2 clicks "Send for sign-off." Sign-off screen shows both of Priya's decisions with their reasons. An attempt to sign while still in Priya's session is visibly disabled (greyed "Sign" button, tooltip: "maker cannot check their own decision"). Member 2 alt-tabs to the pre-logged-in Rajiv Menon window. Member 2 clicks "Confirm and sign" as Rajiv.
**Narration:** "Priya cannot sign her own decision. The system blocks it. Rajiv Menon signs second. Two names. Enforced."
**Proves:** Technical Execution & Architecture (30): maker-checker enforced in the engine. Problem Depth & Regulatory Realism (20): this is the same separation-of-duties discipline IFSCA already requires of the Compliance Officer and Principal Officer roles (FACT_CARD B1).
**Fallback:** If the Rajiv window fails to respond, Member 2 stays on the greyed-out Priya view. Ayush narrates the rule directly to the room without the second click completing: "That grey button is the rule. One more name has to sign, and it cannot be her," and proceeds to shot 9 describing the sealed end-state.

### Shot 9, 60-65s
**Screen:** S7, Receipt and manifest
**Action:** Case status flips to SEALED. Manifest view loads: SHA-256 hash string visible, chained list of every artifact and state transition, green "Verified" badge. SYNTHETIC watermark visible on the exported view.
**Narration:** "The case seals. Every artifact chained into one hash."
**Proves:** Technical Execution & Architecture (30): SHA-256 manifest chaining over every artifact and transition, a concrete integrity mechanism, not a claim.
**Fallback:** If the manifest view is slow to render, Member 2 waits exactly 2 seconds and clicks Verify once more. Ayush keeps talking: "Hashing the whole chain takes a second, that's real computation," which buys the render time honestly.

### Shot 10, 65-70s
**Screen:** S7, Tamper check
**Action:** Member 2 uploads the pre-prepared, one-byte-altered copy of the manifest. Verified badge flips from green to red: "TAMPERED. Hash mismatch at [artifact]." The broken link in the chain highlights visibly.
**Narration:** "Now, watch. One byte. The chain breaks. Visibly."
**Proves:** Technical Execution (30) and Honesty & Roadmap Credibility (20) together: this is the single moment that proves the tamper-evidence claim live instead of asserting it, and it is designed as the emotional peak of the whole pitch.
**Fallback:** This is the most protected shot in the demo. If the upload fails or the badge does not flip within 2 seconds, Member 2 switches immediately to the second tab with the pre-recorded seal-break clip, scrubbed and ready. Ayush says: "Here's that same break, captured earlier today so you see it clean," and lets the clip finish before moving on. Do not attempt a second live retry on this shot; the recorded clip is faster and just as honest.

---

## Timing check

5 + 5 + 5 + 10 + 15 + 5 + 10 + 5 + 5 + 5 = 70 seconds. Every shot lands on a 5-second mark, so this file and PITCH_3MIN.md's 10-second-increment rows can be checked against each other directly. Shot 5 (the F2 timing conflict, the star) carries the largest single block on purpose. Rehearsal will find where the sequence actually runs long; if it does, the cut order is: tighten shot 4's third tab click first, then shot 1's sweep, then shot 6's trace read. Never cut shot 2-3 (the abstention beat) or shot 10 (the tamper break); those two are why this storyboard exists.

Total narration across all ten shots is 193 words (counted, not estimated) across 70 seconds, which is 165 words per minute, a natural, clearly-enunciated pitch pace. Shots 1, 9 and 10 run deliberately slower than the average for weight (the open and the tamper break); shots 3, 4 and 5 run closer to the average with short, plain-word fragments that speak faster than their word count suggests. Confirm the real number with a stopwatch at the first rehearsal; if Run 1 in the log below comes in over 75 seconds, the fix is cutting words per the order above, not talking faster.

---

## The ten-second version (if a judge cuts you off)

"Four numbers, three documents each, and they disagree. The model will not guess. A named human decides, a second signs, and tampering after that breaks visibly." (25 words, about 9-10 seconds at a brisk, clear pace.) Use this only if explicitly told to compress; otherwise run the full sequence.

---

## Recorded-backup protocol

**When to switch:** if any single shot's live element has not recovered within 5 seconds of its first failure (one retry attempted, per that shot's fallback above), stop retrying and switch to the recorded backup video for the remainder of the demo. Do not attempt to resume live mid-sequence; finish the demo on the recording rather than toggling back and forth.

**The exact sentence to say while switching:** "We're moving to a recording of this exact case, captured earlier today, so you see the real result." Say it once, plainly, and keep narrating over the video using the same shot narration lines timed to the recorded action. Never let the room wonder whether what they are watching is live; the sentence above removes the ambiguity in one breath.

**After the switch:** finish the remaining shots narrated over the recording at the same pace. Do not apologise more than once. Do not attempt to explain what went wrong technically during the pitch; that conversation belongs in Q&A if asked.

---

## Rehearsal log

Fill this in after every timed run. Do not skip a row because the run went badly; the bad runs are the useful data.

| Run # | Date | Total time achieved | Shot(s) that stalled | Cause | Fix applied | Ready? (Y/N) |
|---|---|---|---|---|---|---|
| 1 | Thu 20 Aug | | | | | |
| 2 | Thu 20 Aug | | | | | |
| 3 | Thu 20 Aug | | | | | |
| 4 | Sat 22 Aug, 08:00 coach dry run | | | | | |
| 5 | Sat 22 Aug, pre-Round 1 | | | | | |
| 6 | Sat 22 Aug, pre-Round 2 (10s + 1min versions only) | | | | | |

---

## Open founder decisions

1. This storyboard has Member 2 driving (clicking) and Ayush narrating (speaking) for the full 70 seconds, per this task's explicit brief. That conflicts with 10_AYUSH_3DAY_COMMAND_PACK.md ("Mahek narrates demo, you [Ayush] open and close") and 03_STRATEGY_PLAYBOOK.md's unassigned "one person drives, the other narrates, decide roles Wed." Exact question: should Member 2, not Ayush, speak the narration lines during the 70-second demo window, matching the command-pack convention, with Ayush silent until the demo ends?
2. Shot 8's maker-checker beat assumes a second, pre-logged-in browser window for Rajiv Menon is technically supported by the build. Exact question: will the engine allow two simultaneous named-user sessions on one laptop for this demo, or does signing as the second user require an actual logout and login that cannot be pre-staged?
3. C1 from CANON.md is unresolved and affects every spoken reference to "Priya" and "Rajiv" versus whichever human plays Member 2 on stage. Exact question: The second founder is Mahek Soni (RESOLVED 2026-08-19 by the founder)., so the badge, the form, and this storyboard's stage directions can all use one name?

---

## Adjudication of two open decisions (Fable, 2026-08-19)

### Who narrates the demo

**Decision: keep it as drafted. Ayush narrates the demo. Member 2 drives the laptop and delivers the honesty beat at 2:35.**

This contradicts `10_AYUSH_3DAY_COMMAND_PACK.md`, which says Member 2 narrates the demo while Ayush opens and closes. Founder may overrule, and should if Wednesday's rehearsal shows Member 2 narrating better. The reasoning for overriding it here:

1. Narration carries the claims and the rubric hits. Driving is mechanical and rehearsable; narrating to a timer while a juror stares is not. Put the harder job on the person who has drilled the fact card hardest and who takes Q&A anyway.
2. One voice from 0:00 to 2:35 removes two handoffs, at 0:40 and 1:50, which are the two most likely places to lose the timer.
3. Member 2 still speaks, and speaks at the best possible moment. The honesty table beat is the single highest-scoring ten seconds in the pitch, and it lands better from the person who built the screens than from the founder claiming his own work is honest.
4. Doc 03's rule is satisfied either way: one drives, one narrates, never both talking.

Consequence for rehearsal: run it both ways once on Wednesday, time both, and lock it Wednesday night. Do not relitigate it Thursday.

### The maker-checker signature switch (shot 8)

**Decision: no logout and no login during the demo, ever.**

Named users are selected from a list. Authentication is mocked, and the honesty table already declares it mocked. Switching from Priya deciding to Rajiv signing is selecting a different named user, which is instant.

This is not a shortcut, and the answer if a juror asks is straightforward: maker-checker is enforced in the engine, not in the login. The rule that the decider cannot be the signer is a check on the case state, and it would hold identically behind a real identity provider. What we have not built is authentication, and we say so.

The practical reason matters as much as the principled one. A login screen inside a 70-second run is a failure point with a password field, on a venue network, in front of a timer. There is no version of that which improves the demo.
