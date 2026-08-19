# BUILD STATUS, in plain words and numbers

Written 2026-08-19. Updated as lanes land.

## The one-sentence version

We are building a small web app with 8 parts. 19 planning documents are finished. The app itself is being built right now by 6 agents working in parallel, and you should be able to demo it to another human later today.

---

## What the thing actually is

A web page and a small server that run on your laptop. Nine fake documents go in. The app reads them, says what it found and where it found it, refuses to answer when the documents disagree, makes you sign your name to every judgement, and then seals the whole thing with a hash that visibly breaks if anyone edits it afterwards.

That is the whole product. Everything else is detail.

---

## The 8 parts, and what each one is

| # | Part | In plain words | Size |
|---|---|---|---|
| 1 | Document generator | Makes 9 fake documents for 2 quarters. Same numbers every time it runs | ~300 lines |
| 2 | Evidence engine | The rules. Decides if a field is fine, conflicted, or has no source at all | ~250 lines |
| 3 | Manifest and hashing | The seal. Chains every step together so tampering shows | ~200 lines |
| 4 | Server and API | 10 web addresses the page talks to | ~350 lines |
| 5 | Model plane | Talks to AWS Bedrock. Falls back to recorded answers if AWS is missing | ~300 lines |
| 6 | The 7 screens | What the jury looks at | ~900 lines |
| 7 | Eval harness | Scores the system on ~70 labelled items, including whether it correctly refused | ~250 lines |
| 8 | Hardening | Independent verifier, adversarial tests, one-command demo reset, pre-flight check | ~400 lines |

Roughly 3,000 lines of code in total. That is a small app. The reason it is small is that we spent last night deciding exactly what it does, so nothing gets built twice.

---

## What is finished right now

| Thing | Status | Number |
|---|---|---|
| Planning documents | **DONE** | 19 artifacts, 94,000 words, all machine-checked, zero violations |
| The fictional world (one fund, 4 fields, 4 conflicts, 2 cases) | **DONE** | Locked in CANON |
| Every number we may say on stage, with sources | **DONE** | 1 unresolved item left, down from 4 |
| 3-minute pitch, 1-minute pitch, 70-second demo | **DONE** | Timings verified by script |
| Mahek's role, lines and drive sheet | Building now | |
| Parts 1 to 8 above | Building now | 6 agents running in parallel |
| AWS account setup | **Waiting on you.** 30 minutes, needs your login | See AWS_SETUP_TONIGHT.md |

---

## Time and resources

**Time to a demo you can show someone:** the 6 agents are running now. Expect 1 to 3 hours for the parts, then about 1 hour for me to integrate and fix what does not fit together. So a working demo in roughly 2 to 4 hours from now, without you doing anything.

**Your time, and only yours, needed for:**

| Task | Minutes | Why only you |
|---|---|---|
| AWS setup steps 2 and 3 | 10 | Requires your console login and your access keys. I do not handle credentials |
| Watch the demo once and tell me what is wrong | 15 | You are the one who knows what a juror will hate |
| Decide the 4 remaining open questions | 10 | Listed in INDEX.md section 2 |

That is 35 minutes of your time to get to a demo-able product.

**Money:** zero. The app runs on your laptop. AWS costs pennies for a few model calls, against USD 1,100 of credits you already hold. The budget alarm in the AWS doc is set at USD 50 as a smoke alarm.

**Token cost:** the parts are built by Sonnet agents, not by the expensive model. Checking is done by two Python scripts that cost nothing to run.

---

## What "90% done before the hackathon" actually means now

| Layer | Pre-built? | What happens Friday |
|---|---|---|
| What to build and why | 100% | Nothing. It is decided |
| The fictional data and its conflicts | 100% as a plan | Generator gets rewritten in ~30 min |
| The rules and the state machine | Designed and now proven to work | Rewritten from the spec |
| The screens, colours, motion, copy | 100% specified | Rewritten from the spec |
| The prompts that generate all of it | 100%, 30 prompts | Pasted in sequence |
| AWS account, CLI, model access | 100% after tonight | 10 minutes on the event account |
| Pitch, demo, Q&A, one-pager | 100% | Rehearsed only |
| **The actual code files** | **0%, deliberately** | **Written fresh, clean history** |

The code we write tonight gets deleted Thursday. What survives is that we will have done it once, so Friday is repetition rather than invention. That is what makes 22 hours enough.

---

## The rule that protects all of it

The build lives at `~/kriseva-rehearsal-DELETE-BEFORE-21AUG/`. It is outside the KRISEVA_AI folder on purpose, it has no git repository in it, and the folder name is a delete instruction.

**Delete it Thursday before you travel:**

```bash
rm -rf ~/kriseva-rehearsal-DELETE-BEFORE-21AUG
```

The hackathon rule is that code starts clean at 14:00 Friday and commit histories are audited. Building it tonight is not against that rule. Carrying it in would be. Doc 04 already planned exactly this rehearsal for today.

---

## What you get out of demoing it today

This is the actual reason to build it now, and it is worth more than the practice:

1. You find out which screen confuses a real person in the first 10 seconds.
2. You hear the questions we did not predict, and they go into the Q&A bank.
3. You find out whether the 70-second demo is actually 70 seconds when a human is watching and asking things.
4. You learn which feature is missing before Friday, when adding it is free, rather than at hour 15 when it is not.

Show it to two or three people who do not know the product. Say nothing while they use it. Write down every moment they hesitate.
