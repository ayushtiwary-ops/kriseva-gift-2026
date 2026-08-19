# MASTER Q&A BANK: drill this, not the pitch

Status: STABLE. Written 2026-08-20. **This supersedes nothing.** `QA_REDTEAM.md`
holds 30 long-form strategy answers and `JURY_QA_PACK.md` holds the synthetic-data
block. This is the drill sheet: every question we can think of, with an answer
short enough to actually say.

**How to use it.** Cover the right column. Read a question. Say the answer out
loud. If it takes more than fifteen seconds you do not know it yet.

**Three rules that make a bad question survivable:**

1. **Answer in one sentence first.** Context after, and only if they want it.
2. **"I do not know" is a complete answer**, followed by what you would do to find out.
3. **Never defend a number you cannot source.** Say "that is a hypothesis" or say nothing.

---

# SECTION 1. The first thirty seconds

The five most likely openers, in order of likelihood.

| # | Question | Answer |
|---|---|---|
| 1.1 | "What does it do, in one line?" | "When the source documents for a regulatory filing disagree, it refuses to pick a number, shows you why they disagree, and hands the decision to a named person who signs for it." |
| 1.2 | "Who is the customer?" | "The Compliance Officer at a fund management entity in GIFT IFSC. 217 of them today, running 360 schemes. She signs the filing personally, and that is why she would pay us." |
| 1.3 | "What is the problem, concretely?" | "Four numbers go on a quarterly return. They arrive from five parties who close their books at different times, so they disagree, and nothing in the documents says so." |
| 1.4 | "Why is that hard? Just check them." | "She does check. Nothing tells her they disagree, so finding it is the work. And when she resolves it, the reasoning lives in an email reply that leaves when she does." |
| 1.5 | "What is the one thing you would want me to remember?" | "The records must survive eight years. The reasoning survives fifteen days. That gap is the company." |

---

# SECTION 2. The product

| # | Question | Answer |
|---|---|---|
| 2.1 | "Why not just pick the most common number?" | "On our demo case that rule files 17.8 million and it is the wrong one. Nothing announces it. A silent pick is the only error nobody downstream can catch." |
| 2.2 | "Isn't abstaining just refusing to do the job?" | "The job is not producing a number. The job is producing a number somebody can defend. We do the part that is hard to defend and hand over the part only a person can carry." |
| 2.3 | "So a human still does all the work?" | "She does the deciding, which is one minute. We do the finding, which is three days." |
| 2.4 | "What if it abstains on everything?" | "Then it is useless and we would know immediately. On our corpus it abstains where we planted a conflict and resolves where we did not, 24 out of 24." |
| 2.5 | "What happens with a field no document contains?" | "It cannot be decided. It can only be attested, by a named person putting their name to a number with no source, and it is marked that way permanently." |
| 2.6 | "Can it be overridden?" | "A person can decide anything they want. They cannot do it without writing a reason and having a second person confirm, and they cannot make the disagreement disappear from the record." |
| 2.7 | "What stops the same person doing both?" | "The sign-off endpoint rejects it. Priya decides, Rajiv confirms, and if you try it as Priya it refuses in front of you." |
| 2.8 | "What is in the evidence bundle?" | "Every source document, full hashes, the decisions and reasons, and an independent Python verifier inside the bundle so nobody has to run our software to check our work." |
| 2.9 | "Why does that matter?" | "If you need our software to verify our output, it is not evidence. It is a claim." |
| 2.10 | "Can you show me it breaking?" | "Yes. Click tamper on the receipt screen and the chain breaks visibly, and it names the first entry that fails." |
| 2.11 | "What is the actual output? A file?" | "A prepared return with every figure traceable, plus a sealed evidence bundle. We do not file. A person files." |
| 2.12 | "Does it integrate with anything?" | "Not yet. Today it takes documents. Integration is a residency question, and the honest answer is we do not know which systems matter until we have talked to twelve entities." |

---

# SECTION 3. The architecture

| # | Question | Answer |
|---|---|---|
| 3.1 | "Walk me through the system." | "Read it, check it, refuse to guess. Six steps that matter: scope, extract, bind, validate, criticise, reconcile. Then a person decides." |
| 3.2 | "How many agents?" | "Nine roles. Four use a model. Of the 40 steps a case takes, exactly 20 contain no model at all, and the screen counts that itself." |
| 3.3 | "Which ones have no model?" | "Scope, bind, validate, the plan, and the lesson ledger. The three that decide whether a number survives are all plain code." |
| 3.4 | "Why is that a design choice and not a limitation?" | "Because a model cannot check a model. If the thing verifying the quote is the same class of thing that produced it, you have added a second opinion, not a check." |
| 3.5 | "Which models, and why those?" | "Amazon Nova Lite reads, Mistral Large 3 criticises, Z.ai GLM-5 reconciles. Three companies on purpose, and the reader and critic are forced onto different ones." |
| 3.6 | "Forced how?" | "Checked when the system starts. If no independent critic route is available it refuses to boot. It is not a code review rule, it is a startup failure." |
| 3.7 | "Why not one big frontier model?" | "We tried. It did fine. What it did not give us is a refusal enforced in code, a quote checked against the source, and a named decider. Those are not text-generation problems." |
| 3.8 | "You removed agents. Why?" | "Two of them were adding risk without adding judgement. We deleted them and re-ran the measurement: 24 of 24 before and after, zero silent picks before and after." |
| 3.9 | "Which two, exactly?" | "Scope had a model that silently dropped a field. And the orchestrator and learner carried model ids they never actually called, so we corrected the config to say so." |
| 3.10 | "That last one sounds like you were overstating." | "We were, in our own configuration file, and we found it by measuring a real run instead of reading the config. It is in the defect ledger as defect nine." |
| 3.11 | "What runs in parallel?" | "Extraction across documents, and criticism of readings already produced. That is why 40 steps finish in three to eight seconds." |
| 3.12 | "What stops a runaway loop?" | "One wall-clock deadline for the whole run, default 30 seconds, hard ceiling 60. Every step races the remaining time. A step still running at the deadline escalates to a person." |
| 3.13 | "Is that actually enforced or just configured?" | "Enforced. We tested it with a permanently hanging agent against a 30 millisecond budget and it escalated in 36 milliseconds." |
| 3.14 | "How do you handle rate limits?" | "A concurrency gate per model, set below the ceiling we measured on our own account, and exponential backoff with jitter capped at four seconds total so a throttled call frees its slot." |
| 3.15 | "Why per model and not global?" | "Because the limits are per model. One shared gate throttled the constrained model and starved the ones with headroom at the same time." |
| 3.16 | "What happens if a model is down?" | "Each role has a fallback route on a different model, and the fallback still has to satisfy the independence rule. If it cannot, the case escalates rather than degrading quietly." |

---

# SECTION 4. The data, and this is where they will push

| # | Question | Answer |
|---|---|---|
| 4.1 | "Is any of this real?" | "No. Twenty fictional entities, 26 cases, 115 documents, all synthetic, and every document says so on its face." |
| 4.2 | "Then what does the demo prove?" | "That the pipeline does what the design says on ten distinct shapes of failure. Nothing more. It does not predict behaviour on a real return." |
| 4.3 | "You planted the conflicts." | "We did, and I will say it before you do. It is a consistency check, not an accuracy claim." |
| 4.4 | "How did you get fund data?" | "We did not. We have never seen a real quarterly return. Everything here we worked out from published circulars and our own reading." |
| 4.5 | "So how did you decide what documents look like?" | "From what the rules require to be reported and the conventional shape of each document type. Both are assumptions and I can tell you exactly which." |
| 4.6 | "What is your core assumption?" | "That a fund receives its numbers from several independent parties who close at different times. If that is wrong, we are much less useful, and it is the first thing we would test." |
| 4.7 | "How close is your corpus to reality?" | "Structurally close, cosmetically nothing like it. We modelled the structure and not the mess. Ours is plain text; a real one is PDF, Excel, Word and scanned." |
| 4.8 | "What is your conflict base rate?" | "We do not have one. Nobody does, publicly. Producing it is ask one of the residency and we would publish it whatever it says." |
| 4.9 | "Did an AI write your evidence?" | "Deterministic code owns every number, every planted conflict and every hash. A model writes only the covering prose, so the documents read like documents." |
| 4.10 | "Why does that split matter?" | "If a model wrote the figures, the conflicts would be whatever it felt like that run and the demo would be unreproducible." |
| 4.11 | "How do I know the ground truth isn't circular?" | "The generator writes the expected field and cause into the case before any model sees it. The scorer reads that and calls the API. It is not the system grading itself." |
| 4.12 | "Show me a case you get wrong." | "On the eval label set we shipped, four labels contradict our own canon and the product is scored as failing. The product is right and the labels are wrong, and both are published." |

---

# SECTION 5. The measurements

| # | Question | Answer |
|---|---|---|
| 5.1 | "What is your accuracy?" | "24 of 24 planted archetypes named with exactly the right cause, and zero silent picks. And that number means less than it sounds like, because we wrote the failures." |
| 5.2 | "Which number should I actually care about?" | "Zero silent picks. It is the only failure in this product that nobody downstream can detect." |
| 5.3 | "How fast?" | "Three point three to seven point nine seconds for a complete nine-role case, measured on three consecutive live runs." |
| 5.4 | "What does it cost per case?" | "About 14,700 tokens, recorded per agent action. No dollar figure, because our account has no pricing API access and I will not quote a price I cannot source." |
| 5.5 | "Did you test against just using a model?" | "Yes, and it went against us. Three frontier models, told to abstain on disagreement, all abstained correctly with zero silent picks." |
| 5.6 | "So your product is unnecessary?" | "On eight fields at one run each, told exactly what to do, they complied. One of the three could not produce a single quote that was actually in the document. And none produced a named decider or a record." |
| 5.7 | "Why publish a result against yourself?" | "Because we measured it. A result that surprises us is worth more than a prediction that flatters us, and honesty is 20 percent of the score by rule." |
| 5.8 | "How many tests?" | "299 unit and browser tests, 24 canon conformance checks, 9 filing-history checks. All green, re-run after every change." |
| 5.9 | "Did the tests catch your bugs?" | "No. Nine defects were found by using the product, and all nine survived the tests. That is the most useful thing we learned." |
| 5.10 | "Give me an example." | "The interface was never wired to the attestation endpoint. On stage I would have clicked and shown a juror a raw engine rejection." |
| 5.11 | "Why should I trust your numbers?" | "Do not. Run the gates yourself; they are in the repo. And the eval file we shipped reports us failing, which we left in and explained." |

---

# SECTION 6. Market, money and moat

| # | Question | Answer |
|---|---|---|
| 6.1 | "How big is this market?" | "I can give you a countable market, not a modelled one. 217 entities today, 1,147 across all IFSCA verticals, and the same evidence shape in every one." |
| 6.2 | "That is tiny." | "In GIFT IFSC today, yes. The shape repeats in every regime that files periodic returns from multi-party records. We would rather earn the second market than model it now." |
| 6.3 | "What is the price?" | "Hypothesis: 3 to 12 lakh per entity per year, priced against defensibility rather than hours. Unvalidated. We validate or kill it in the residency." |
| 6.4 | "Why would they pay that?" | "Because the signature is personal. They are not buying time saved, they are buying the ability to show why, to somebody asking eleven months later." |
| 6.5 | "IFSCA is building DRR. Aren't you redundant?" | "DRR is the regulator's front door. We sit on the entity side, before the filing. None of the ten named DRR modules is lineage, provenance or reconciliation." |
| 6.6 | "When does DRR land?" | "Awarded January 2026, pre-bid responses say 18 months to go-live, so second half of 2027 at the earliest with migration after. At least six more quarters get filed the old way." |
| 6.7 | "Administrators could build this." | "They could, and they are also our most plausible channel. One administrator serves many funds. The conflict is that they are one of the disagreeing parties." |
| 6.8 | "Big Four could bolt it on." | "They sell this as a retainer today. None of the twelve firms we checked publishes a fee schedule. That is a services business, and services do not produce a replayable record." |
| 6.9 | "What is your moat?" | "Not the model. The refusal enforced in code, the evidence you can check without us, and eventually the base rate nobody else has measured." |
| 6.10 | "What is your unfair advantage?" | "We do defence procurement evidence work today. Same discipline, different regulator." |
| 6.11 | "Why has nobody done this?" | "Because the incentive is to produce a number, not to refuse. Refusing is a worse demo and a better product, and it only sells to someone who signs personally." |

---

# SECTION 7. Team, execution and the audit

| # | Question | Answer |
|---|---|---|
| 7.1 | "Why you two?" | "We removed two models from our own system this week because they added risk without judgement, and we published the before and after. That discipline is the product." |
| 7.2 | "Two people cannot do this." | "Not at scale. We can get to a measured base rate and two pilots in sixty days, and that is what we are asking for." |
| 7.3 | "This is AI-written code." | "Much of it is, and the tests, the gates and the defect ledger are how we know what it does. Nine defects are published because we found them by using it." |
| 7.4 | "22 hours is not enough to build this." | "The repository starts empty at 2pm Friday and the history is auditable. What we carried in is documents, and all of it is published openly, before the sprint." |
| 7.5 | "You had a working prototype before." | "Yes, a rehearsal build, and we say so. It is deleted before travel, none of its code enters the sprint repo, and the carry pack is public so you can see exactly what we brought." |
| 7.6 | "That still sounds like an advantage." | "It is. Rehearsing is allowed; carrying code is not. We published what we carried so you can check which one we did." |
| 7.7 | "Who is liable if the number is wrong?" | "The person who signed, exactly as today. What changes is that they can show what they knew and why they chose it. We are not selling indemnity." |
| 7.8 | "What if your tool causes the error?" | "It cannot select a value, so it cannot select a wrong one. It can fail to surface a candidate, which is why the scope step has no model in it." |
| 7.9 | "What is your biggest risk?" | "That conflicts are rare and trivial in real data. Then this is a nice audit trail attached to a problem nobody has." |
| 7.10 | "What would make you quit?" | "Eight quarters of real data showing the base rate is near zero. We would say so publicly and stop." |

---

# SECTION 8. The nasty ones

| # | Question | Answer |
|---|---|---|
| 8.1 | "This is a wrapper around an API." | "Half the steps in a run contain no model at all, and those are the ones that decide whether a number survives. A wrapper cannot refuse." |
| 8.2 | "Your demo is scripted." | "The walkthrough is, and it says recorded walkthrough on every screen. The live path runs in about five seconds and I can run it now on any of the 26 cases." |
| 8.3 | "You are hiding behind 'hypothesis'." | "Only on things we have not tested, and I have told you which. Everything else has a number and a method you can re-run." |
| 8.4 | "What don't you know?" | "The base rate, what real documents look like, which rule requires which field, and whether anyone will pay. Those are the four asks." |
| 8.5 | "Nothing here is defensible technology." | "Agreed on the extraction. The defensible part is that the refusal is structural, and that is a design commitment, not an algorithm." |
| 8.6 | "Prove it refuses when it matters." | "Open the trace and you can watch the guard block a reconciler that tried to remove a preserved conflict. It shows as blocked on the screen." |
| 8.7 | "Why should a regulator care?" | "Because today they receive a number with no way to ask how it was chosen, and the person who knows has left." |
| 8.8 | "You are pre-revenue with fake data pitching a regulator." | "Yes. That is exactly why we are asking for access rather than money." |
| 8.9 | "Give me one reason to pick you over the other 49 teams." | "We ran the experiment designed to prove our own thesis, it came back against us, and we put it on the slide." |
| 8.10 | "Sell me in ten seconds." | "Four numbers, five sources, one personal signature. When they disagree, everything else picks. We refuse, and we show you why." |

---

# SECTION 9. What never to say

Memorise this list. Breaking one of these costs more than any answer gains.

- **No dollar cost per case.** We cannot source the price.
- **No rupee or dollar TAM.** We do not have a defensible one.
- **Never "production ready".** One corpus of synthetic documents.
- **Never claim the offline path uses a local model.** It is recorded responses plus a deterministic scan.
- **Never invent a regulatory citation.** Per-field rule mapping is not built and the screen says so.
- **Never present the baseline comparison as a win.** Eight fields at one run each.
- **Never imply a customer, pilot, endorsement or partnership.** We have none.
- **Never say the 45 percent agentic figure**, in either direction. Sources conflict.
- **Never say the rate limits we measured apply to any account but ours.**
- **Never name a real entity's enforcement history on stage.**

---

# SECTION 10. When you do not know

Say one of these, exactly. All three are stronger than a guess.

> "I do not know. Here is how I would find out, and it is one of the four things we are asking for."

> "That is a hypothesis, not a measurement. I will tell you when we have tested it."

> "We measured that and it went against us. Do you want the table?"
