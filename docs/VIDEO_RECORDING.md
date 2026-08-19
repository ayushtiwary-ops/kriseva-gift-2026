# RECORDING THE 1:45 WALKTHROUGH VIDEO

Written 2026-08-19. The shot list and narration are in `MAHEK_MASTER_BRIEF.md` section 6. This is the how.

**What I cannot do:** render a finished MP4 with a voice track. I can write the script, set the demo to the exact state each shot needs, and tell you precisely what to click. The recording and the voice are twenty minutes of your time.

**Why that twenty minutes is worth spending rather than skipping:** this video is the thing Mahek rewatches on the train. It also becomes the recorded backup if the live demo fails on stage, which the storyboard already plans for. Two uses, one recording.

---

## Setup, 3 minutes

One command. It rebuilds the corpus, restores all eight fictional entities, starts the
server, puts the demo case in its opening state, and then runs every gate and tells you
whether it passed.

```bash
cd ~/kriseva-rehearsal-DELETE-BEFORE-21AUG/attest && bash scripts/demo-ready.sh
```

It ends with either `DEMO READY` or `NOT READY`. If it says NOT READY, do not record. The
failing gate is printed directly above that line.

It is idempotent, so run it again any time you think the state has drifted, including
between takes.

**Browser setup:** one window, no tabs bar clutter, no bookmarks bar, zoom at 100%, window at roughly 1440 wide. Hide your dock. Close Slack and mail so no notification lands mid-take.

---

## Recording, macOS

Press **Cmd + Shift + 5**, choose "Record Selected Portion", drag around the browser window only, and record.

Record **silent video first**, following the shot list. Do not try to narrate while clicking; it always sounds rushed and you will retake five times.

Then record the narration separately as audio, reading the script at a calm pace, and lay it over in iMovie or QuickTime. The script is written to fit the shot timings when read unhurried.

---

## The shot list, with exact clicks

From `MAHEK_MASTER_BRIEF.md` section 6. This adds what to click.

| Time | Click this | Narration beat |
|---|---|---|
| 0:00-0:10 | Nothing. Hold on the dashboard, still. Let "The shape of this fund" sit on screen | Four numbers have to go on this return. Three of the four bars stop early and go hatched |
| 0:10-0:20 | Nothing. Cursor traces the hatched section of one bar | That hatching is the part the documents do not agree on. Most dashboards would draw one confident bar here, which means picking |
| 0:20-0:30 | Scroll to the four cards. Let the four chips sit: Sources disagree, Sources disagree, Sources disagree, No source found | Four numbers, four states, no machine words on screen |
| 0:30-0:44 | Click drawn capital. On the evidence screen, click one candidate. The highlight lands in the source text | Every number pinned to the exact line, and who wrote it, and what moment it was true |
| 0:44-0:54 | Hold on the explanation, then on the "If nobody looked" box | The 1.5 million at 17:42. It derived that. And here is what an ordinary system would have filed instead |
| 0:54-1:04 | Click the complaints field. The screen is titled "Put your name to a number" | No document contains it. She cannot decide this one, she can only put her name to it |
| 1:04-1:14 | Open the trace screen. Scroll the spine slowly, pausing on the two steps marked "deterministic, no model in this step" | Nine roles. Two of them contain no model at all, because a model cannot verify a model |
| 1:14-1:24 | Open the History screen. Hold on the trend, then the quarter table | Five quarters. The same disagreement, every quarter. It is not an incident, it is how this fund receives its documents |
| 1:24-1:36 | Decision screen. Try submit with no reason (it refuses). Type a reason, decide. Watch the band collapse on the dashboard. Then attempt sign-off as Priya (refused), then as Rajiv | Named human, written reason, maker-checker. The band collapses the moment she decides |
| 1:36-1:45 | Receipt screen. Click tamper. The chain breaks | The seal, and what breaking looks like |

**Pacing note:** three moments need to breathe. 0:54 (the refusal), 1:24 (the band collapsing), and 1:41 (the break). Hold each an extra beat. Everything else can move.

**If you are short on time,** cut the History beat at 1:14 first. It is the strongest new material but it is also the only beat that is not on the demo spine, and the spine is never cut.

---

## If a shot goes wrong

Do not restart the whole take. Record that shot again separately and cut it in. Nine short clips edited together looks identical to one long take, and it takes a quarter of the time.

---

## The one thing to check before you call it done

Watch it once with the sound off. If somebody who has never seen the product cannot follow what is happening from the pictures alone, the shots are too fast. The narration should reinforce the video, not carry it.
