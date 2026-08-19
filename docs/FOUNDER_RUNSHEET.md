# AYUSH: what to do from tomorrow morning, in order

Status: STABLE. Written 2026-08-20. **Everything is built. Nothing is left to make.**
From here your only jobs are running the demo and being able to answer anything.

---

## The one link that contains everything

**https://kriseva-gift-backup-2026.s3.us-east-1.amazonaws.com/index.html**

If your laptop dies, that link is the entire submission: the working prototype,
the video, the deck, every document, and the ask.

---

## Thursday 20 August, about 3 hours of work total

Do them in this order. Each one is timed.

### 1. Watch the video. 2 minutes.
Watch it once as a stranger. It is the story you are going to tell, in the order
you are going to tell it. Everything else on this sheet is that story with more
detail.

### 2. Read the architecture page. 10 minutes.
`docs/architecture-simple.html`. **Learn only this**: six steps that matter,
three use a model, three are plain code, and the plain code ones are the ones
that check. Then the number: 20 of the 40 steps in a run contain no model at all.

If you can say that without thinking, you can survive any technical question,
because every follow-up hangs off it.

### 3. Drill the Q&A bank. 60 minutes, and this is the one that matters.
`docs/master-qa-bank.html`. **87 questions.** Cover the answers. Say each one out
loud. If it takes more than fifteen seconds you do not know it yet.

Do sections 1, 3 and 8 twice. Section 1 is the first thirty seconds, section 3 is
the architecture, section 8 is the hostile ones. Those three carry the room.

**Section 9 is the do-not-say list. Read it last thing at night.**

### 4. Run the demo three times. 20 minutes.
```bash
cd ~/kriseva-rehearsal-DELETE-BEFORE-21AUG/attest && bash scripts/demo-ready.sh
```
Wait for `DEMO READY`, then open `http://localhost:4000` and walk the spine three
times without notes: dashboard → drawn capital → complaints → trace → sign-off →
receipt → tamper. Third time, say the pitch over it.

### 5. Read the 3 minute pitch out loud, twice, on a timer. 15 minutes.
`docs/pitch-3min.html`. It is written to be spoken at an unhurried pace. If you
finish under 2:40 you are rushing. If you pass 3:00 cut the Trace narration to
one sentence.

### 6. Read the 1 minute pitch once. 5 minutes.
`docs/pitch-1min.html`. Four short paragraphs. Do not try to compress the 3 minute
version; say fewer things properly.

### 7. Send Mahek her message. 2 minutes.
It is written for you at `MESSAGE_TO_MAHEK.md`. Copy, paste, send.

### 8. Delete the rehearsal build. 1 minute.
**Before you travel. Not on Friday morning.**
```bash
rm -rf ~/kriseva-rehearsal-DELETE-BEFORE-21AUG
```
Everything survives: the hub, the video, the prototype on AWS, the private source
repo, and the carry pack. What you are deleting is the local working copy that
must not travel.

---

## Friday, before 14:00

Nothing to build. Three things to check.

| Check | How |
|---|---|
| The backup link loads on venue wifi | Open it in the browser you will present in, then **leave the tab open** |
| The pinned video URL plays | `/video/v4-lewis/KRISEVA_ATTEST_demo.mp4`, a path no cache has seen |
| The carry pack is on your laptop | `AGENT_CONTRACT_PACK.md`, `UI_LANGUAGE_AND_VISUALS_SPEC.md`, `SCHEMA_PACK.md`, `BUILD_SPEC_v1.md`, `CANON.md`, `RUNNING_COST_AND_LIMITS.md` |

Then at 14:00 the repository starts empty and you build from the pack.

---

## Saturday, the two pitches

**Round 1, 14:00.** 3 minutes plus 7 minutes of Q&A. All fifty teams, parallel
panels, strict timer. Top 20 advance.
- You: the machine, the numbers, the ask.
- Mahek: Priya's day, the demo narration, and stopping you if you say a number
  that is not in the fact card.

**Round 2, 17:00.** 1 minute plus 4 minutes, Grand Jury, Top 20. Top 15 announced
at closing.
- One minute means four short paragraphs. Say fewer things properly.

---

## The five sentences to have ready at all times

1. "Every system built for this picks a number. Ours refuses to."
2. "Nine roles, forty steps. Half those steps contain no model at all, because a model cannot check a model."
3. "The records must survive eight years. The reasoning survives fifteen days. That gap is the company."
4. "We have never seen a real quarterly return. Everything still missing is something only access can fix."
5. "We predicted a frontier model could not do this. We ran it, and it could. We are showing you that table anyway."

---

## If something goes wrong

`BACKUP_RUNBOOK.md`, one page, on your phone. The short version:

| If this fails | Open this |
|---|---|
| Laptop, port, server or local build | the prototype URL on AWS |
| AWS | the GitHub Pages mirror |
| All networks | the video, offline on your phone |

**Say it plainly when you switch.** "The laptop is not cooperating, so I am
opening the deployed build. Same product, same numbers, all synthetic." A calm
switch reads as preparation. An apology reads as a failure.
