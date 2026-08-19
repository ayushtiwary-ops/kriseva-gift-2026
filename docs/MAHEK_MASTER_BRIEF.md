# KRISEVA ATTEST
## Master brief for Mahek Soni

**GIFT IFIH Young Builders' Program, 21 to 22 August 2026**
Prepared 19 August 2026. Everything in this document is current as of the overnight build.

---

## How to use this

Read it once end to end. It takes about 25 minutes. Then reread sections 6, 7 and 8 the night before, because those are the ones you will be tested on.

You do not need to become an engineer. You need to be able to explain what we built, why it is arranged that way, and answer the business questions a jury will aim at you specifically. That is what this document covers.

One thing to hold on to: **you will be asked different questions from Ayush.** He will get the technical and the founder questions. You will get the business, market and operations questions, because that is your training and a jury reads a team by testing each person on their own ground. Section 7 is written for exactly that.

---

## 1. What the product is, in five sentences

A fund in GIFT City has to file a quarterly return. One number on that return often appears in several documents that disagree with each other, for legitimate reasons. Today an AI tool reads them, silently picks one, and nobody can later reconstruct which document it trusted or who approved it.

KRISEVA ATTEST is the layer that makes that defensible. The AI proposes values and shows exactly where each came from, refuses to answer when the sources disagree or when no source exists, and forces a named human to decide with a written reason. Everything, including what the AI did, is sealed into a record that visibly breaks if anyone edits it afterwards.

**The one-line version:** AI does the reading, a named human owns every judgement, and the whole trail is sealed.

---

## 2. Why this is an agentic system, and what that means

"Agentic" means the system is not one AI call. It is a set of specialised workers, each with a narrow job, coordinated by a planner, several of them running at the same time.

Ours has **nine roles**. Seven use AI models. Two are deliberately plain code with no AI at all.

**The single most important thing to understand and say:** not one of those nine can decide anything. They can propose, object, reject and explain. Only a named human can decide. That rule is enforced in the code itself, not in the instructions we give the AI, so an agent cannot talk its way around it.

### The nine roles

| # | Role | What it does, in one line |
|---|---|---|
| 1 | **Orchestrator** | The planner. Works out which documents matter for which fields and what runs in what order |
| 2 | **Triage** | Reads each document and reports which fields it probably contains, so we do not waste work |
| 3 | **Extractor** | Proposes a value and quotes the exact text it came from. Several run at once, one per document |
| 4 | **Binder** | Plain code, no AI. Checks that the quoted text genuinely exists in the document. Drops anything it cannot find |
| 5 | **Validator** | Plain code, no AI. Checks the arithmetic. Drawn capital cannot exceed committed capital, a ledger has to add up |
| 6 | **Critic** | Runs on a different AI company's model and tries to prove the extractor wrong |
| 7 | **Reconciler** | Works out why the documents disagree and writes it in plain English |
| 8 | **Narrator** | Writes the summary the human reads before deciding |
| 9 | **Learner** | Runs afterwards. Turns mistakes into rules, which a human must approve before they take effect |

### Why two of them have no AI in them

Roles 4 and 5 are ordinary code on purpose. **A model cannot be trusted to check a model.** If the AI says "I found this number in the document", we do not ask another AI whether that is true. We search the document ourselves. Arithmetic either adds up or it does not.

If someone asks you why those two are not AI, that sentence is the whole answer.

### Why the critic uses a different company's model

The extractor runs on Amazon's model. The critic runs on Mistral's. This is deliberate.

If you ask the same model to check its own work, it makes the same mistakes twice and agrees with itself. Models from different companies, trained differently, get things wrong in different places. So when they disagree, that disagreement is real information.

That gives us **two independent reasons to refuse an answer**: the documents disagree with each other, or our own AI models disagree with each other. Almost nobody checks the second one.

### The models we use, and why

| Role | Model | Company | Why |
|---|---|---|---|
| Orchestrator | Kimi K2 Thinking | Moonshot | Planning is the hardest reasoning job here |
| Triage | Nova Micro | Amazon | Cheapest, and the job is simple |
| Extractor | Nova Pro | Amazon | We tested it. Fast and accurate on our documents |
| Critic | Mistral Large 3 | Mistral | Different company, so it fails differently |
| Reconciler | GLM 5 | Z.AI | Explaining why sources differ needs real reasoning |
| Narrator | Nova Lite | Amazon | Plain summarising, cheap |

All of these run on AWS Bedrock, using the credits the programme provides.

---

## 3. How the nine work together

Read this once and you can draw it on a whiteboard.

1. **Documents come in.** Four of them for our demo case: an administrator statement, a subscription register, an internal ledger, a custodian letter. Each gets a fingerprint so we can tell later if it changed.
2. **The orchestrator makes a plan.** Which documents to read for which of the four numbers we need.
3. **Triage prunes.** It says which documents plausibly contain which numbers, so we do not run every check against every document.
4. **Extractors run in parallel**, one per document, each proposing a value with a quote.
5. **The binder checks every quote against the real document.** Anything it cannot find is dropped, no matter how confident the AI was.
6. **The validator checks the sums.**
7. **The critic, on a different model, tries to prove each value wrong.**
8. **The reconciler compares what survived.** If values disagree, it works out why and says so in plain English.
9. **The narrator writes a summary.**
10. **The case is handed to a human.** Always. That is the only way the process can end.
11. **A human decides**, with a written reason. **A second human confirms.** They cannot be the same person.
12. **Everything is sealed** into a chained record: what the AI planned, what it proposed, what it objected to, what the humans decided.

**Total: 40 agent actions on our demo case, finishing in under a tenth of a second on the recorded path.**

---

## 4. The buyer: Priya, and her actual workflow

This is who we are building for. Know her better than you know the technology.

**Priya Ramanathan, Compliance Officer at a fund management entity in GIFT City.** She is one of two people who must be named to the regulator and based in the IFSC. She personally signs the quarterly return. Her Principal Officer, Rajiv, signs it too.

Two facts that define her problem, and they are worth memorising because they are the whole business case:

- **If she leaves, the regulator is told within 15 days.**
- **The records must survive 8 years.**

Her institutional memory has a 15 day expiry against an 8 year obligation. Everything she knows about why a number is what it is walks out with her.

### Her 21 days today, without us

| When | What happens | What it costs her |
|---|---|---|
| 30 June | Quarter ends. The clock starts. 21 days to file | |
| 3 July | Administrator statement arrives. It looks authoritative | She starts building the return from it |
| 8 July | The administrator quietly reissues a corrected statement | Nobody flags it. Her ledger was built from the old one |
| 10 July | Numbers do not match. She cannot tell whether that is an error or a legitimate difference | Hours of checking |
| 11 July | She emails the administrator. Gets an answer | **That email thread becomes the only record of the reasoning** |
| 15 July | The complaints field has no source document anywhere | |
| 15 July | **She types a number in anyway, because the form will not submit empty** | She signs an unverifiable figure under her own name |
| 18 July | She signs. Rajiv signs. The file goes into a folder | |
| Eleven months later | A question arrives | The reasoning exists only in her memory, or a thread she may no longer have access to |

**The moment of maximum pain is 15 July.** A cursor over an empty box, a form that refuses to submit blank, and a compliance officer inventing a fact under her own name because the alternative is missing a regulatory deadline.

### Her 21 days with us

Same quarter, same documents, same disagreements. We do not make the conflicts disappear and we do not decide anything for her. What changes is what exists afterwards.

| When | What happens now |
|---|---|
| 3 July | Documents ingested and fingerprinted |
| 8 July | The reissue is detected. The system flags that the ledger derives from a superseded version |
| 10 July | The system does not pick. It shows both values, both sources, and explains why they differ |
| 11 July | She decides, with a written reason. **The reason is in the record, not in an email** |
| 15 July | The complaints field stays empty and blocks sign-off. If she must file, she records it as an attestation: her name, her reason, no source, marked permanently different from the others |
| 18 July | Rajiv confirms. He cannot be the same person who decided |
| Eleven months later | A supervisor opens the receipt and sees which numbers were backed by documents, which was somebody's word, who decided each, and why |

### What she is actually buying

Not saved time. **Be careful here, because this is a trap.** The whole job is maybe two to five days a year of labour. A product priced above that cannot be sold on efficiency, and any juror who does the arithmetic will catch it.

She is buying **the difference between a defensible answer and no answer, at the moment of inspection.** The person who buys hours back is an operations manager. The person who buys defensibility is the person whose name is on the signature. That is why it is priced per entity and not per seat.

---

## 5. What changed in the last 48 hours

So you are current.

1. **The system became genuinely agentic.** It was a single pipeline. It is now nine roles with a planner, running in parallel.
2. **We proved every model works.** All six configured models respond live on AWS in 161 to 266 milliseconds.
3. **We found and fixed four real bugs by running it**, not by reading it. The most serious: an independently written verifier disagreed with our own and was right. We were not validating one field of the sealed chain, so a specific forgery would have passed. It is fixed.
4. **A safety fix worth understanding.** Triage used to be able to silently prune all the work if it failed, which emptied the whole case. It now fails open: if triage does not answer, we do the work anyway. Triage exists to save cost, never to decide what evidence is allowed to exist.
5. **Attestation became a separate act from a decision.** A value backed by a document and a value that is somebody's word now look permanently different on the receipt.
6. **Two deployments.** It runs on AWS, or entirely on a laptop with no network call at all. Unplug the wifi and it keeps working.
7. **The interface stopped speaking in machine words.** Every status used to be an engineering token in capitals. A juror who does not know fund accounting saw "Committed capital, CONFLICTED" and stopped reading. Now the status is a sentence ("Sources disagree"), every regulatory term keeps its proper name and carries a plain gloss under it, and every status carries a one-line explanation on the card rather than behind a hover. The underlying data and the JSON are unchanged, so this cost us nothing in rigour. There is also a "What these words mean" panel with 29 terms defined in one sentence each.
8. **Three defects found by using it, not by reading it.** The interface had never been wired to the attestation endpoint, so the missing-field field, the one CANON calls our strongest single screen, dead-ended live with the engine's rejection text on screen. Four of the eight conflict causes rendered no explanation at all. And the app opened on the wrong case, the clean quarter with nothing to decide. All three are fixed and verified by running the demo end to end.
9. **Four prior quarters for every entity.** Thirty two filings on record, arithmetically chained so the closing position of one quarter opens the next, and anchored to the figures CANON section 13 already fixes. It has its own gate, `tools/history_check.py`.
10. **One command to get demo ready.** `bash scripts/demo-ready.sh` rebuilds everything, restores all eight entities, starts the server, seeds the case, runs every gate, and prints DEMO READY or NOT READY. It is idempotent.
11. **The corpus became reachable.** Eight fictional fund managers and twelve quarterly returns already existed in the data and nothing in the interface could get to them. There is now an entity selector in the top strip, and all twelve render clean.

---

## 5a. The two things to point at that nobody else will have

**"The shape of this fund."** A panel above the four cards that draws the fund as bars. Where the documents disagree the bar stops early and the rest is hatched, and the caption says how much is in dispute. Every dashboard in this category draws one confident bar, which means somebody picked a number. Picking is the thing we refuse to do, so the picture refuses too. When a named person decides, the band collapses to a solid bar in front of the room. That collapse is the product, made visible, and it is drawn from the same numbers on the cards so it cannot drift away from them.

**"Filing history."** Every fictional entity now carries the four quarterly returns it filed before this one. Thirty two filings, forty three disagreements, and every one of them settled by a named person with the reason still attached. The point it makes in five seconds: the same disagreement recurs every quarter, so it is not an incident, it is how that fund receives its documents. One entity, Nilgiri, changes Compliance Officer partway through. Her successor inherits the same conflict and, in every tool that exists today, none of the reasoning. IFSCA requires the change notified within 15 days and the records kept for 8 years, and the reasoning is the part that normally does not survive. All of it synthetic, and the screen says so.

**"If nobody looked."** On each conflicted field, the interface computes what an ordinary system would have filed: take the number the most documents agree on. On drawn capital that rule files USD 17,800,000, because the administrator and the custodian both say so and only the ledger disagrees. It is the most reasonable rule available and on this field it is wrong, and nothing in either document announces it. After the human decides, the box states the size of the gap they just closed. We never assert the ordinary rule is wrong before a person decides, because before a person decides nobody can know. That restraint is the point.

---

## 6. The video: 1 minute 45 seconds

This is the shooting script. It matches this document section for section, so watching it and reading this should feel like the same explanation.

**To record it:** start the demo (`npm start`, open `localhost:4000`), start a screen recording, and follow the shot list. Roughly 20 minutes including retakes. Record the narration separately and lay it over, because reading while clicking always sounds rushed.

| Time | On screen | Narration |
|---|---|---|
| 0:00-0:12 | Title card: KRISEVA ATTEST, and the words "all data synthetic" | "A fund in GIFT City files a quarterly return every three months. One number on it can appear in four different documents, and those documents disagree." |
| 0:12-0:25 | The four documents, scrolling briefly | "The administrator says seventeen point eight million. The internal ledger says nineteen point three. Nobody is lying. A capital call arrived at 5:42pm, after the administrator drew its line at 4pm." |
| 0:25-0:35 | Dashboard, four fields with four different state chips | "Four numbers. Four different states. Three disagreements, each for a different reason, and one field no document mentions at all." |
| 0:35-0:50 | Evidence screen, click a candidate, highlight appears in source | "Every proposed number is pinned to the exact characters it came from. The AI told us where it found it. We then searched the document ourselves to confirm. If we cannot confirm it, we drop it." |
| 0:50-1:02 | The reconciler explanation on drawn capital | "And it works out why. The gap is exactly one and a half million. The ledger contains one movement of exactly that amount, timestamped after the administrator's cut-off. Nobody wrote that sentence. It derived it." |
| 1:02-1:14 | The unsupported field, empty, blocking sign-off | "This field has no source anywhere. So the system produces nothing. Today a compliance officer types a number here because the form will not submit empty. Zero is the most dangerous answer in regulatory reporting, because it looks like an answer." |
| 1:14-1:26 | Agent trace screen, the roles listed | "Nine roles ran on this case. A planner, triage, extractors in parallel, a binder, a validator, a critic on a different company's model, a reconciler, a narrator. Not one of them can decide anything." |
| 1:26-1:36 | Decision screen: reason required, then maker-checker refusal | "A named human decides, with a written reason. A second named human confirms, and the system refuses if they are the same person." |
| 1:36-1:45 | Receipt, then tamper, chain breaks visibly | "Then it seals. Change one byte afterwards and the seal breaks, and it names the exact entry that broke." |

**Total 1:45.** If you need 2:00, add fifteen seconds at 1:14 on the two deterministic roles and why they have no AI in them.

---

## 7. The questions you will get, and they are business questions

A jury tests a team by asking each person about their own ground. Ayush gets the technical and founder questions. **You have an MBA, so you get the market, model and operations questions.** These are yours. Learn these eight.

**"How big is this market?"**
> "I will give you a countable market rather than a modelled one. 217 fund management entities running 360 schemes in GIFT City today, and 1,147 registered entities across all IFSCA verticals. Every one of them files periodic returns assembled from documents that can disagree. We are not going to show you a top-down number we cannot defend."

**"What is the business model?"**
> "Hypothesis, and I will flag it as a hypothesis: an annual licence per entity, priced against the risk of an indefensible filing rather than hours saved. Fund administrators become a channel, because one administrator serves many funds. We validate or kill that in the residency."

**"Why can you not sell this on time saved?"**
> "Because the arithmetic does not work and we would rather say so. The whole task is a few days of work a year. Our price sits above that. She is not buying hours back, she is buying the difference between a defensible answer and no answer at the moment of inspection. The person who buys hours is an operations manager. The person who buys defensibility is the one whose name is on the signature."

**"Who actually signs the cheque?"**
> "The Principal Officer, we think. The Compliance Officer feels the pain, but the Principal Officer carries the personal accountability for the signed return. That distinction is a hypothesis and it is the first thing we test in the residency."

**"How do you sell to a regulated fund? What is the go to market?"**
> "Two routes. Direct to the entity, which is slow and high trust. Or through fund administrators, who already serve many funds and could offer it as part of their service. We do not know which is faster and that is a discovery question, not a claim."

**"What is your unit economics?"**
> "Marginal cost is small and I can bound it. A full run is model calls and storage, cents rather than rupees. The number that actually decides whether this is a product or a consulting business is implementation cost per customer: how many days to map a fund's document set. If that is under a week it is a product. If it is a month it is a services business wearing a product's clothes. I would rather find that out in October than in year two."

**"You have talked to how many customers?"**
> "Zero. Not one practising compliance officer. Everything we have is reconstructed from primary regulatory documents, published enforcement records and job postings. That is the single biggest gap in what we are showing you, and closing it is the first thing we would do with the residency."

**"What did you personally build?"**
> Answer with specifics and no apology. You own the evaluation labels, the honesty disclosure, the domain vocabulary check, and you drive the demo. Say what those are concretely. Driving the demo is not the junior job. The person driving is the reason it does not break.

---

## 8. The two interviews are different. Prepare differently.

### Round 1: three minute pitch, seven minutes of questions, all fifty teams

The pitch is scripted. Your speaking part is the honesty beat at 2:35, which is ten seconds and the highest scoring ten seconds in the whole pitch, because 20% of the score is honesty about what is real and what is not.

**In the seven minutes of questions**, expect a mix. Panels here are moving fast across many teams. Questions tend to be broad: what is it, who buys it, is it real, what did you build.

Your job: **be visibly a second founder, not a second presenter.** Answer at least two questions yourself, fully, without looking at Ayush. A jury that sees one person answer everything scores the team as one person.

### Round 2: one minute pitch, four minutes of questions, top twenty only

The organisers say most of the Round 2 score is the questions. The minute exists mostly to buy the right ones.

**This panel is more senior and will probe harder.** Expect follow-ups rather than fresh questions: they will pick one thing and go three levels deep. If they choose the business model, that is yours and you should take it rather than deferring.

**Two rules for both rounds:**

1. **Never invent a number.** If it is not in the fact card, the answer is "I do not have a verified figure for that, and I am not going to invent one." That answer scores. A confident guess that turns out wrong costs far more than an admission.
2. **Handing off is fine, deferring is not.** "Ayush built that layer, he should answer the detail" is strong. Looking at him and going quiet is not.

---

## 9. What to say when you do not know

Use this exact sentence:

> "I do not know that, and I would rather tell you than guess."

Then, if you can, add what you would do to find out.

This is not a fallback. It is on brand. Our entire product exists because a system that guesses when it should refuse is dangerous. A founder who does the same thing is making the pitch for us.

---

## 10. Cheat card

Print this. Carry it.

**The four numbers, and never get these wrong**

| Field | The disagreement |
|---|---|
| Committed capital | 42.5 million versus 45 million. The register counts a subscription signed but not counter-executed |
| Drawn capital | 17.8 million versus 19.3 million. A 1.5 million call landed at 17:42, after the 16:00 cut-off |
| Closing NAV | 21,940,500 versus 22,415,000. The administrator restated on 8 July |
| Complaints closed | No source anywhere. The system refuses |

**The four documents**

Administrator statement (Northwind). Subscription register (the fund). Internal ledger (the fund). Custodian letter (Sentinel).

**The market numbers**

217 fund management entities. 360 schemes. 1,147 registered entities across all IFSCA verticals. 19 enforcement actions in the first half of 2026.

**The two facts that make the business**

A compliance officer's departure is notified in 15 days. The records must survive 8 years.

**Your spoken line, at 2:35**

> "This table is why you can trust the rest. Synthetic, mocked, or live, every screen labelled. Zero customers, zero pilots, on ATTEST, on purpose."

**When you do not know**

> "I do not know that, and I would rather tell you than guess."

---

*All data in this document and in the product is synthetic. The fund, the people and the numbers are fictional. Kriseva AI Private Limited claims no customers, no pilots, no revenue, no measured accuracy and no relationship with IFSCA.*
