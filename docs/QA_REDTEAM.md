# QA_REDTEAM: 30 hostile judge questions, drilled section by section

Status: STABLE. Compiled 2026-08-18. Owner: founder. Source: FACT_CARD.md (the only source of numbers), CANON.md (the only source of demo detail), PRODUCT_DECISION.md (the claims boundary), war room doc 03 section 3 (baseline, superseded and expanded here).

Every number below traces to FACT_CARD.md. Where FACT_CARD marks a number AMBER or RED, the answer carries the same hedge or drops the number. Nothing here is a new fact. This is the old facts, said under pressure.

---

## The three rules of Q&A

1. **Answer first, then evidence.** Give the judge the conclusion in the first sentence. Then the one or two facts that hold it up. Never open with a story, a caveat, or a run-up. A juror who has to wait for the point thinks you are hiding it.
2. **Never invent a number.** If it is not on FACT_CARD, it does not leave your mouth, even a round estimate, even under a friendly follow-up, even to fill a silence. A wrong guess costs more than an honest gap.
3. **Take the note rather than argue.** If a judge asserts something wrong, correct it once, calmly, with the source. If they push back again, take the note and move on. You are not going to out-argue a judge in front of a panel, and trying reads as defensive, which is the one thing this rubric punishes twice (Founder Assessment and Honesty both fall).

**The standing sentence for a question we cannot answer:**
> "I do not have a verified figure for that, and I will not invent one."

Say it flat. Do not apologise for it, do not soften it with a guess "in the ballpark." It is a complete answer, not a placeholder for a better one.

---

## SECTION A. Product and moat

### A1. "Isn't this just DRR? IFSCA is already building this. Why wouldn't they just add your idea into their own system, or expand DRR to cover it next year?"

**What they are really asking:** Have you actually read what the regulator is building, or are you pitching against a system you don't understand.

**Answer:** DRR is real and it is a serious build. IFSCA awarded just under 56 crore rupees combined: about 39.57 crore to NEC for the DRR solution itself, plus 16.4 crore to CMS Computers for a parallel ERP system, both excluding GST. IRIS RegTech runs DRR's design, development and maintenance as subcontractor, roughly seven years. What DRR does: collects returns on the web instead of by email, validates the format, gives IFSCA a dashboard. What DRR's own scope document does not list, in any of its modules: lineage, provenance, source-document evidence, or reconciliation to a golden source. And the pre-bid responses say it still accepts Excel, Word and PDF, no mandated data standard. So DRR is the regulator's pipe. It does not touch what happens before the fund opens the form: which of three disagreeing internal documents was right, and who decided that. That is our layer. If IFSCA ever mandates an evidence trail like ours, our market grows, it doesn't disappear.

**If they push:** "And if DRR's scope expands into this next year? Then we will have eight weeks, or more, of real entity-side evidence data before anyone else does. That makes us the natural partner to that expansion, not a casualty of it."

**Grade: PASS**

**Landmine:** We have not found anything in writing that says IFSCA has reserved the right to expand DRR's scope. If a judge has read a version of the concept note with a scope-expansion clause we missed, this gets harder in real time.

---

### A2. "Why can't I just point ChatGPT at three PDFs and ask it to check them? What are you actually selling that isn't a prompt?"

**What they are really asking:** Is there an actual product here, or is this a thin wrapper on a frontier model.

**Answer:** Extraction is the easy part. The product is what sits around it: the refusal protocol and the accountability record. A model that reads three documents will pick an answer, because that is what these models are built to do, fill the box. Ours is built to do the opposite on purpose. When two sources disagree, it abstains and shows both, with exactly where each came from. A named human has to give a reason before the case can move. A second, different named human has to sign off before it seals. Every one of those is workflow and governance engineering: an abstention contract, maker-checker enforced in the state machine, a hash-sealed manifest, and an eval harness that scores when the system correctly refuses, not just when it's right. A prompt does not give you any of that.

**If they push:** "Take the model away entirely and swap in a human doing manual entry. The abstention rule, the maker-checker separation, and the sealed manifest all still hold. That is how you know the product is the protocol, not the model call."

**Grade: PASS**

**Landmine:** If asked to name the exact extraction model or show a live failure case on stage, we have to be ready to demo it honestly, including a case where it abstains, not just the clean path.

---

### A3. "Name your competition. Regnology, Workiva, IRIS, Duco, Hadrius, Norm AI, they all do pieces of this already. What's actually different, or are you just newer versions of the same idea?"

**What they are really asking:** Have you done real competitive homework, or do you think you're in a category of one because you haven't looked hard enough.

**Answer:** Each of them genuinely has a piece. Regnology does regulatory data lineage for large banks and insurers. Workiva does connected reporting with controlled documents, audit trails and sign-off workflows, and announced an AI layer on top of that in 2026. IRIS RegTech is the closest and most serious: it holds the design, development and maintenance role on IFSCA's own DRR system, roughly seven years, and separately sells filing tools to regulators and administrators. Duco does automated reconciliation between data sources. Hadrius and Norm AI are newer, AI-native compliance monitoring tools, watching communications and flagging rule violations after the fact. We are aware of no product that combines field-level binding to the exact source document region, preserved disagreement instead of a silent pick, a named-human decision with a mandatory reason, and a cryptographically sealed record a third party can check without us, on the entity's own side, before submission.

**If they push:** "That sentence says 'we are aware of no product,' not 'no product exists.' We have not run an exhaustive global audit of every AI-governance startup, and I will not claim we have."

**Grade: WOBBLE**

**Landmine:** We have not done a full teardown of Hadrius or Norm AI specifically, both are recent and both move fast. If a judge has used either and knows it already does source binding, our hedge is the only thing standing between us and being caught overstating. That is exactly why the hedge is worded the way it is: "no product exists" is a claim we cannot defend, "we are aware of no product" is a claim about the boundary of our own research, and it is true either way. Losing this sentence on stage would cost less than the FACT_CARD-banned alternative would, if we ever said it and were wrong.

---

### A4. "Our fund administrator already produces most of these numbers for thirty clients, or our Big Four firm sells this as a retainer. Why wouldn't they just bolt on a feature and make you irrelevant in one release?"

**What they are really asking:** Is your moat a real structural gap, or a feature request sitting in someone else's backlog.

**Answer:** They might. Genuinely, that is a live risk and not a talking point. Two structural reasons it is harder than it sounds. First, an administrator attesting to the provenance of its own output is marking its own homework, and from 30 September 2026 the fiduciary-segregation circular forbids one entity from being a scheme's fiduciary and also its administrator, valuer or auditor. That pushes toward more independent parties holding overlapping records, not fewer, which is the opposite of what a bolt-on feature from one of those parties can fix. Second, a Big Four retainer sells a person's assurance, and a person's institutional memory has a fifteen-day expiry, that's the notification window when a Compliance Officer changes, against an eight-year record-retention requirement. Neither of those is proof we win. They are the two reasons I'd bet on us if I were forced to.

**If they push:** "If either of them ships a real, independent, cross-provider version of this before we get real customer conversations done, that is one of our own named triggers to kill this and say so."

**Grade: WOBBLE**

**Landmine:** This is an argument, not evidence. Nobody has tested whether an administrator or a Big Four firm actually wants to build this, and if one of them already has it in a private roadmap, we would not know.

---

### A5. "'Abstain,' 'maker-checker,' 'preserved disagreement,' this sounds like consultant language for 'the AI doesn't actually work.'"

**What they are really asking:** Is refusal a designed safety behaviour, or a euphemism for a broken extraction pipeline.

**Answer:** Fair challenge, so let's be precise about what abstention actually means here. It does not mean the model failed to answer. It means the model looked at the evidence and correctly reported that the evidence itself disagrees, which is a true fact about the documents, not a limitation of the model. The dangerous version of this product is the one that always answers: frontier models on financial-analyst-style tasks score in the low-to-mid sixties percent on public benchmarks, reviewed by people from Goldman, Silver Lake and Citadel. That means roughly a third of the time, a model that always answers is wrong and confident about it. Our position is that "I don't know which of these two numbers is right" is a correct output when that is the true state of the world, and a silent guess is the actual defect, not the abstention.

**If they push:** "Show me a case where it abstains and shouldn't have. Fair ask, and it's exactly what our eval harness exists to catch, we just don't have a measured false-abstain rate yet."

**Grade: PASS**

**Landmine:** We have no measured false-abstain rate. If asked "how often does it abstain when it shouldn't," the honest answer is we don't know yet, not a defensible-sounding estimate.

---

### A6. "What's quantum-proof about any of this? Everyone says their crypto is future-proof until it isn't."

**What they are really asking:** Are you overselling the cryptography the way everyone at a hackathon oversells the cryptography.

**Answer:** Nothing, and we're not claiming otherwise. This isn't our track and I won't bluff it. We hash with SHA-256 today, that's it. What we did think about: the manifest format is algorithm-agile by design, meaning the hash algorithm is a labelled field, not baked into the structure, so it can be swapped without redesigning the whole evidence format. That's a sensible engineering choice, not a security guarantee about the next twenty years of cryptography. If a track prompt specifically wants quantum resistance, that's not where we'd spend our 22 hours.

**If they push:** "No, we have not implemented any post-quantum signature scheme, and I'd be suspicious of any team at this hackathon who claims they have in a weekend."

**Grade: PASS**

**Landmine:** None beyond the obvious, this answer only works if we actually resist the temptation to bluff further when pushed a second time.

---

## SECTION B. Market and buyer

### B1. "Does this even work outside GIFT City? What's your cross-border story, or is this a one-regulator toy?"

**What they are really asking:** Is the idea bigger than the one jurisdiction you happened to pick for the hackathon, or does it collapse the moment you leave GIFT IFSC.

**Answer:** The protocol generalises, the specifics don't, and I want to be honest about which is which. Abstain-on-conflict, named-human-decides, maker-checker, sealed manifest, none of that is IFSCA-specific, it's a pattern for any regulated entity reporting into any jurisdiction from multiple internal sources. Where it gets real is cross-border reporting, where the same fund has to satisfy a home regulator and a host regulator with evidence that has to survive two separate inspections. A portable, hash-sealed manifest is exactly the kind of proof that travels between two regulatory contexts without depending on either one's system. But today, everything we've built and tested is against one regulator's one return, in GIFT City. Cross-border is a shape the architecture supports, not something we've built or shown working.

**If they push:** "No, we have not tested against a second jurisdiction's format. That's a residency-stage claim, not a today claim."

**Grade: WOBBLE**

**Landmine:** This entire answer is architectural reasoning with zero demonstrated cross-border evidence. A judge who asks "show me" has no demo to see.

---

### B2. "You've talked to zero customers. Why should any of us take this seriously?"

**What they are really asking:** Is this venture-shaped conviction, or a founder in love with a problem nobody has confirmed.

**Answer:** Zero. No customers, no pilots, no design partners, no revenue. I'm not going to dress that up. Everything in this pitch is reconstructed from primary documents, circulars, enforcement orders, fee schedules, published fact sheets, not from a conversation with a person who does this job. That is the single biggest gap in the project, and it's also exactly what the residency is for: real proximity, for weeks, to people whose job legally requires them to sit inside GIFT City. Take this as evidence of discipline rather than avoidance: we built and rehearsed a full falsification plan, named triggers that would kill this idea, before we had a single customer conversation to bias us. That's the order I'd want a founder to work in.

**If they push:** "No, I haven't spoken to a single practising compliance officer. Not one. Ask me again in eight weeks and I'll either have five conversations or I'll tell you we killed it."

**Grade: PASS**

**Landmine:** None, structurally, this is the answer FACT_CARD explicitly instructs us to say flat and early because it scores on honesty. The only way to lose points here is to look uncomfortable saying it.

---

### B3. "Your demo conflicts are planted. Of course your system catches them, you wrote the fiction to make yourself look good."

**What they are really asking:** Is this a rigged demo, and do you understand that it's rigged.

**Answer:** Yes, entirely, and we planted it on purpose, that's not a confession, it's the point of a demo. Every document, every number, every name in our demo is fictional and labelled synthetic on every screen. We designed four distinct causes of disagreement on purpose: a timing gap between a cut-off and a capital call landing after it, a correction the administrator issued later, a version mismatch between a signed and a counter-executed subscription, and one field with no source at all. Each one looks different on screen because in the real world they are different failure modes, and a system that handled all four the same way would be lying about having built one thing and relabelling it four times. What the demo proves is that the state machine and the refusal logic run correctly on a known, designed case. It proves nothing about accuracy on a real fund's real, messy documents, and we say that ourselves, unprompted.

**If they push:** "Would it catch a conflict we didn't design in advance, on a real fund's real documents? Unknown. That's exactly what an evaluation harness with a held-out set is for, and we don't have one running against real data yet."

**Grade: PASS**

**Landmine:** None, if we stay disciplined. The failure mode here is sounding defensive about something that is, honestly, just how demos work. Own it fast and move to what it doesn't prove.

---

### B4. "What's the exit and scale story? How does this become a big company, what's the second market, what does a buyer actually buy?"

**What they are really asking:** Is 217 entities a real business, or a hackathon-sized wedge with no path past it.

**Answer:** The wedge is 217 FMEs. The market is the 1,147 registrations across every IFSCA vertical, eleven capital-market-intermediary categories, sixteen IBU returns, monthly returns from finance companies and lessors, all with the same underlying shape: numbers that originate with someone else and get reassembled by hand under a deadline. That's the second market, and it's inside the same regulator, so it's the same relationship, the same trust, the same manifest format, extended sideways rather than a new go-to-market. What a buyer would actually be buying, if this works, isn't a customer list, it's the standard: if the manifest format becomes how evidence gets exchanged between funds, administrators and eventually a supervisor, the acquirer is buying the format and the position, not just the software. That's a long-run thesis, not a plan, and I'd rather say that plainly than dress it up as a roadmap slide.

**If they push:** "No term sheet, no acquirer conversation, nothing. This is a shape of an argument, not a forecast."

**Grade: WOBBLE**

**Landmine:** This entire answer depends on the manifest format actually getting adopted by someone other than us, which has not happened and which we cannot claim credit for in advance.

---

## SECTION C. Money

### C1. "What's your business model?"

**What they are really asking:** Do you actually have a plan for revenue, or is "we'll figure out pricing later" hiding behind the demo.

**Answer:** Hypothesis, and I'll say that word every time I say the number: per entity per year, not per seat, 3 to 12 lakh rupees, priced against defensibility rather than hours worked. Per seat pricing would punish a customer for looping in more reviewers, and more reviewers is exactly the behaviour this product needs. The volume driver is schemes, not entities, 360 schemes sit inside 217 FMEs, so a fund administrator or a multi-scheme FME is a bigger account on the same base price. That's the shape. Whether anyone actually pays it, and where inside that band, is exactly what residency discovery is for, and I'll tell you in eight weeks whether we validated it or killed it.

**If they push:** "No signed customer, no letter of intent, no verbal yes from a buyer. This is a priced hypothesis, not a deal in progress."

**Grade: WOBBLE**

**Landmine:** Every number in this answer is explicitly labelled hypothesis on our own fact card. If we say it even once without the word, we've broken our own rule in front of the people scoring us on honesty.

---

### C2. "What does it actually cost you to serve one customer? What's your gross margin? What does implementation cost?"

**What they are really asking:** Have you done the arithmetic that turns a nice demo into an actual company, or is this all top-line thinking.

**Answer:** Honestly, we don't have a real number, because we have never implemented this for anyone. What I can tell you is the shape, not the figure. Inference runs on cloud infrastructure, so marginal cost per document is small, but we have not measured it at any volume that means anything. The real cost driver in year one isn't infrastructure, it's founder time: onboarding a regulated customer, understanding their document set, handling their edge cases. That means gross margin in the first several customers should look bad on paper, and that's expected, not a red flag, it only becomes a red flag if it still looks bad once we're not hand-holding every account. I'm not going to hand you a margin percentage I made up to sound investor-ready.

**If they push:** "What would implementation cost a customer? Unknown. We have never done one."

**Grade: WOBBLE**

**Landmine:** If a judge asks for the actual number, twice, and won't accept "we haven't measured it," this is where the interview gets uncomfortable. The honest answer doesn't get better under repetition, it just has to hold.

---

### C3. "Defend the price. Why that number, who actually signs the cheque, what budget line does it come from, and why not half of it?"

**What they are really asking:** Is this price reverse-engineered from a number that sounded fundable, or does it map to a real budget and a real signer.

**Answer:** The signer is the Compliance Officer or the Principal Officer, both IFSCA-mandated, both required to sit inside the IFSC, and the signature on the return is personal to them, not the fund. That's who owns the budget conversation, because their name is the one on the line if the number is wrong. Why 3 to 12 lakh and not half: because regulatory fees are noise next to what an FME already carries, 4.77 crore rupees of locked-up net worth alone, so this isn't competing with a small compliance line item, it's competing with the cost of the officer's own exposure. The one real anchor we have is that Indian companies already pay 15,000 to 60,000 rupees a month, one published benchmark, for GST compliance with a far simpler failure mode than losing your registration. Half our number sits below that anchor for a harder problem. That's the defence. It is still unpriced against an actual buyer.

**If they push:** "Would we take half, from a real buyer, today? Yes, and we'd write down why, and use it as the first real data point instead of the hypothesis."

**Grade: WOBBLE**

**Landmine:** The GST anchor is one published benchmark, not a market study, and B9 says this price is only arguable above roughly USD 20 million of scheme AUM. A judge who does that segmentation math live will find the bottom of the market where our price doesn't work yet.

---

### C4. "I did the arithmetic. A compliance officer's entire quarterly workload costs less than what you're charging. Your product costs more than the problem it solves."

**What they are really asking:** Have you actually run the labour math yourself, or did we just catch you selling efficiency you can't deliver.

**Answer:** You're right, and we ran that arithmetic before you did. A fully loaded compliance officer at 25 lakh a year, that's a stated assumption, costs about 10,000 rupees a working day. Even at five full days a quarter on this return, the entire labour content of the problem is 2 lakh rupees a year. Our price is above that at every plausible assumption. So no, this cannot be sold as time saved, and we don't sell it that way. Here's the reframe: the buyer isn't purchasing hours back, they're purchasing the difference between a defensible answer and no answer, at the moment an inspector asks for one. The person who buys hours back is an operations manager. The person who signs the return, personally, with an eight-year retention clock and a fifteen-day handover window if they quit, is buying something else entirely.

**If they push:** "Does that reframe actually survive a real procurement conversation, or is it a story we tell ourselves? Unknown, and it's the first thing discovery has to test, not assume."

**Grade: PASS**

**Landmine:** None on the arithmetic itself, it's airtight because we did it against ourselves first. The risk is entirely in whether the "defensibility over hours" reframe survives contact with an actual budget owner, which nobody has tested.

---

### C5. "IFSCA's own fines are tiny, median about a lakh and a half, and most enforcement carries no money at all. Why would anyone pay lakhs a year to avoid a fine that small?"

**What they are really asking:** Is the enforcement risk you keep citing actually big enough to justify anyone paying you.

**Answer:** Because the money was never the real cost. Of 25 published enforcement actions, only six carried a penalty at all, median about 1.5 lakh rupees, and eighteen carried no money whatsoever. Two ended in cancellation of registration. That last number is the one that matters, not the fines. A cancelled FME registration isn't a cost you budget around, it's the business ending in that jurisdiction. Regulatory fees and fines are noise next to what it actually costs to be an FME: crores in locked-up net worth, key personnel, SEZ premises. Nobody prices this product against the fine. They'd price it, if they price it at all, against the tail risk of losing the licence that the whole operation sits on.

**If they push:** "Has anyone actually lost a registration over exactly this kind of unresolved conflicting-document problem? We don't have a case that specific. Two cancellations are on the record; we have not mapped either one's cause in that much detail."

**Grade: PASS**

**Landmine:** We have not traced either cancellation back to a provable-document-failure root cause specifically. If a judge asks "which of the two cancellations was caused by exactly this," we don't have that answer.

---

## SECTION D. Technical

### D1. "What's your accuracy? Give me a number."

**What they are really asking:** Are you going to hand me a marketing statistic, or do you actually understand why that number is dangerous to quote right now.

**Answer:** We publish no accuracy figure, and I'd be suspicious of anyone at our stage who hands you one. We have an eval harness that runs against labelled synthetic sets, and we'll show you those results, denominator visible, on the slide. We claim no production accuracy until it's measured against a design partner's real documents, because a synthetic set we built ourselves is not evidence of real-world performance, it's evidence the harness runs. The honest reason to care about this: on published finance-task benchmarks, reviewed by people from Goldman, Silver Lake and Citadel, the best frontier models score in the low-to-mid sixties percent. That means any tool that always answers is wrong and confident roughly a third of the time. Our answer to that isn't a better number, it's a system that abstains instead of guessing when the evidence doesn't support one answer.

**If they push:** "What happens when the model is confidently wrong, not just uncertain, and doesn't flag it? That's the actual failure mode our eval harness has to catch, and we don't yet have a measured rate for it. Saying we're immune to it would be the exact lie this product exists to prevent."

**Grade: PASS**

**Landmine:** The recorded run in our public prototype used a Claude Haiku model, a smaller model than judges may assume. Friday's live build runs on whatever Bedrock grants us that day. We must not let anyone leave the room thinking Friday's demo used the same, or a bigger, model than the recorded one implies.

---

### D2. "Where's your real data? Everything here is synthetic, right? So what does the demo actually prove?"

**What they are really asking:** Are you hiding behind fake data because you're not confident this survives contact with a messy real document.

**Answer:** Correct, entirely synthetic, and it says so on every screen. By design, not by accident: regulated fund documents are confidential, we have no legal basis to touch a real one yet, and we'd rather ship an honest synthetic demo than a real one we obtained the wrong way. What the demo proves: the state machine runs correctly on a known case, four fields, four different evidence states, source binding works, the seal breaks visibly on tampering, and a named human decision is required before sign-off. What it does not prove: accuracy on a real fund's real, messy, inconsistent paperwork, buyer demand, or willingness to pay. We built an eval harness specifically so a fund could eventually validate against their own data inside their own perimeter, without ever handing us the underlying documents.

**If they push:** "When do you get real data? Not until a design partner explicitly permits it, under a scoped agreement, after legal review of custody. We are not collecting confidential documents during discovery conversations either."

**Grade: PASS**

**Landmine:** None structural, this is the correct and rehearsed answer. The only way to lose points is hesitating before admitting "entirely synthetic," which reads as reluctant rather than by-design.

---

### D3. "You're a defence-procurement company. Why does any of that skill actually transfer to fund compliance? Different regulator, different documents, different failure mode."

**What they are really asking:** Is the "existing engine" claim real reuse, or a founder story stretched to cover a cold start.

**Answer:** Fair, and the honest scope of the claim is narrower than "we've done this before." Kriseva's existing product does deterministic, auditable document evaluation in defence procurement, source-bound evidence, human-in-the-loop decisions, an audit trail that survives scrutiny. ATTEST points that same discipline at a different document set. What transfers is the pattern: multiple independent parties producing overlapping records, a human who has to reconcile them under a deadline, and a system that should refuse rather than guess when the records disagree. What does not automatically transfer: the domain knowledge of fund administration, NAV computation, capital calls, or IFSCA's specific taxonomy, and we are not fund accountants by background. We have not measured how much code or logic actually carries over, so I won't give you a reuse percentage. What you're watching Friday is how much of it actually holds up when we build the fund-specific pieces from a clean repo in 22 hours.

**If they push:** "So how much is genuinely new build versus reused pattern? We have not measured it. That is a fair thing to be skeptical about until we can show you the diff."

**Grade: WOBBLE**

**Landmine:** We have never opened the old codebase and counted what actually reuses versus what's rebuilt from scratch for this domain. Any specific reuse claim beyond "the pattern transfers" is unverified.

---

### D4. "Data privacy and custody. Where does customer data actually live, what happens in a breach, and why would a regulated entity hand you their documents at all?"

**What they are really asking:** Have you thought about the thing that kills every RegTech deal, or does that come after the demo works.

**Answer:** Today, honestly, this is the least settled part of the plan, and I'd rather say that than describe an architecture we haven't committed to. In the demo, every document is synthetic, so there's nothing to protect. Friday's live extraction runs on AWS Bedrock, cloud infrastructure, because live AWS usage is part of what this track rewards. For a real regulated customer, data custody is an open architecture decision we have not locked, and I will not promise on this stage that it runs entirely on a customer's own machine when I can't yet prove that under questioning. What is locked: no real regulated document touches our systems until a design partner explicitly permits it, under a scoped agreement, with legal review of the custody position and the DPDP angle done first, not after. A breach response plan doesn't exist yet, because there is nothing real in the system to breach.

**If they push:** "So is this on-device or cloud, pick one. We genuinely have not decided, and I would rather tell you that than pick the answer that sounds better in the room."

**Grade: WOBBLE**

**Landmine:** This is the sharpest live tension in our own materials: earlier research leaned toward on-device deployment specifically so data never leaves the customer's infrastructure, while the hackathon build plan runs live extraction on AWS Bedrock. If a judge has seen both framings, or simply asks us to pick one, we do not have a reconciled answer yet.

---

## SECTION E. Team and execution

### E1. "Why this problem, why now, and why should it be the two of you?"

**What they are really asking:** Is there a real, timed reason this matters this year, or is this just a hackathon-convenient story.

**Answer:** Why now, in one sentence: adoption is sprinting, accountability is flat, and enforcement is climbing. As reported in IFSCA's own July 2026 survey, 65% of GIFT IFSC entities are into generative AI, only 17% have it in production, and only 35% run a formal AI audit, up from 10% the year before. Meanwhile enforcement went from roughly two actions a year to 19 in the first half of 2026. That gap between adoption and accountability is the market, and it's the regulator's own number, not ours. Why us: Kriseva already builds deterministic, auditable document evaluation in defence procurement, a different regulator, the same discipline, source-bound evidence, human sign-off, an audit trail that survives scrutiny. We published a working seven-screen prototype of this exact pattern on 12 August, before this hackathon existed for us, and didn't copy a line of it into today's build. Why two of us, here, in person: because conviction plus the ability to ship fast is what this stage actually tests.

**If they push:** "Isn't 'we already had a prototype' proof this isn't really a 22-hour build? No, it's proof we understood the pattern before we understood this specific regulator. What starts clean at 14:00 Friday is the fund-specific build, and the commit history shows that."

**Grade: PASS**

**Landmine:** If a judge has read IFSCA's AI survey PDF directly and we haven't, and they ask about the agentic AI adoption figure specifically, we say only that the report names agentic AI as the next frontier with a small cohort at pilot or production stage. We do not have a percentage we can defend for that one number, and saying the wrong one, in front of the regulator that published it, is the single costliest mistake available to us in this room.

---

### E2. "Two people cannot build, sell, and support enterprise software for a regulated industry. Full stop."

**What they are really asking:** Have you thought past the demo to what happens when a real customer calls with a real problem at 6pm on a Friday.

**Answer:** At this stage, honestly, correct, and I'm not going to pretend two people is a support organisation. What two people can do: build the thing you're about to watch run live, and go have the discovery conversations that tell us whether this is worth scaling support for at all. What two people cannot do, and we're not claiming to: run a helpdesk for fifty regulated funds simultaneously. The team-size rule for this programme allows up to four, and the honest plan is that support and scale are a problem we earn the right to solve once we have paying customers who need it, not a problem we solve speculatively in a pitch deck. Building a support org for zero customers would be the wrong twenty hours to spend this week.

**If they push:** "So what's the actual plan past ten customers? We don't have one yet, and building one before we have ten customers would be premature for a two-person team."

**Grade: WOBBLE**

**Landmine:** There is no support model, staffing plan, or SLA commitment anywhere in our materials. If pushed for specifics beyond "we'll figure it out at that scale," we have nothing further to offer.

---

### E3. "This is AI-written code. I don't trust software I can't see a human actually wrote, line by line."

**What they are really asking:** Do you understand what you shipped, or did you just approve whatever the agent handed you.

**Answer:** We build with agents, and we govern them under the same rule we're selling: an agent may propose, a named human has to review and commit. Every change in Friday's history has a human's name attached, deciding to keep it, not just accepting a diff. That's not a defence of the practice in the abstract, it's the same architecture as the product, propose, don't decide, and a human owns the outcome. If that governance model is good enough to put in front of a regulator for fund reporting, it's good enough for our own build process, and we'd rather be caught practising it than just pitching it.

**If they push:** "Show me a commit where a human actually changed what the agent proposed, not just approved it. Fair ask, and it's exactly what the audited history from Friday is for, that's a live answer, not a rehearsed one."

**Grade: PASS**

**Landmine:** This only holds if the actual commit history from Friday shows real human editing, not just a stream of accepted agent commits. If the history looks like unreviewed approvals, this answer becomes evidence against us instead of for us.

---

### E4. "I looked at your commit history. This is too much to have genuinely built in 22 hours. Something doesn't add up."

**What they are really asking:** Are you hiding pre-written code, which the rules of this hackathon explicitly forbid.

**Answer:** Look at the timestamps, that's the actual answer, not our word for it. Code starts clean at 14:00 Friday, and commit histories get audited, we know that going in and we're not fighting it, we're leaning on it. What makes 22 hours enough: we're not writing extraction logic from a blank page, we're applying a pattern, propose, abstain on conflict, named human decides, maker-checker signs, seal, that we already understood from a prototype we published on 12 August with public code, before this event. Nothing from that repo gets copied in, but the shape of the problem doesn't have to be relearned live. If you still don't buy it, name a feature and we'll build it in front of you right now.

**If they push:** "How many tests does the build actually have? Our published prototype documents over 150 automated checks; Friday's fund-specific build is new code and starts its own count from zero."

**Grade: PASS**

**Landmine:** The offer to "build a feature live" is only as good as our ability to actually do it under pressure. If we make that offer and then fumble it, it's worse than never having offered.

---

### E5. "Who is legally responsible when the human decides wrong? And what happens to you if that person turns around and sues you?"

**What they are really asking:** Have you actually thought about your own liability exposure, or only about how the product looks on stage.

**Answer:** Two different questions, and I'll answer both. The regulatory responsibility never moves: the Compliance Officer and Principal Officer sign the return personally today, and nothing about our product changes whose name is on it, we're not built or described as replacing that signature or making the regulatory call ourselves. Our own liability exposure as a vendor, the professional-liability boundary, the TechFin and ancillary-services perimeter, what happens if we're sued, that is a named, explicit gate in our own product decision that we have not cleared yet. We have written down that we need scoped legal advice on exactly that question before we can call this a company rather than an experiment, and we haven't gotten it yet. I would rather tell you it's an open gate than pretend a two-person team already has outside counsel signed off on liability.

**If they push:** "So you'd operate with an unresolved liability position? No. It's a named stop condition. If legal advice says the operating model doesn't work, we stop and redesign it, not push through."

**Grade: WOBBLE**

**Landmine:** No lawyer has reviewed our liability position, our data-custody position, or our operating-model boundary. This is a named, undone gate in our own decision log, not a hypothetical risk.

---

## SECTION F. Honesty and risk

### F1. "Does your tool take the Compliance Officer off the hook? What about liability if the human decides wrong?"

**What they are really asking:** Does this quietly shift regulatory responsibility onto software, in a way that would actually be dangerous.

**Answer:** No, by design, and that's enforced in the system, not just in how we describe it. A model may propose a value. It may never decide one. Where two sources disagree or nothing supports a field, the system abstains and a named human has to give a reason before the case can move at all, and a second, different named human has to confirm before it seals. The Compliance Officer and Principal Officer carry exactly the accountability they carry today, nothing about our product is described as determining compliance, replacing either of them, or making the regulatory call itself. What changes isn't who's responsible, it's how complete the record of their decision is when someone asks about it later.

**If they push:** "Could a human just rubber-stamp whatever the machine proposes, and responsibility becomes theoretical? That's a real risk with any decision-support tool, and the only defence is that the reason field is mandatory and named, so a rubber stamp is visible as one, not hidden as a properly reasoned decision."

**Grade: PASS**

**Landmine:** "Mandatory reason field" stops a silent auto-approve from being invisible. It does not stop a human from writing a lazy, low-effort reason and clicking through anyway. We have no defence against that beyond the record showing exactly who did it.

---

### F2. "What don't you know right now that, if it turned out to be true, would kill this company?"

**What they are really asking:** Do you actually have a falsification plan, or just confidence.

**Answer:** We wrote these down before we had any customer conversations to bias us, specifically so we couldn't rationalise them away later. Three named triggers, on record. If three or more practising compliance officers tell us the return is immaterial, takes consistently under two hours, or their administrator already fully absorbs it without separate budget, we're wrong, and we stop. If IRIS, NEC, DRR, or an administrator turns out to already provide equivalent filer-side source provenance and entity-controlled evidence custody, the wedge is gone. And if the legal operating route turns out to be unavailable or disproportionate for a team our size, we stop regardless of how the market questions answer. Any one of those, confirmed, and we re-run this decision rather than push through on momentum. We'd rather find out in week four of the residency than after raising money on an idea that was already dead.

**If they push:** "Has any of the three happened yet? No. None of the three is confirmed. That's exactly why they're written down as tests, not conclusions."

**Grade: PASS**

**Landmine:** Having the triggers written down is not the same as having the discipline to actually act on them when one fires. That's untested, because none has fired yet.

---

### F3. "You keep saying 'hypothesis.' Isn't that just a hedge so nothing you say can ever be proven wrong?"

**What they are really asking:** Is your honesty performance, or does it actually constrain you.

**Answer:** It constrains us, and I can show you exactly how. Every number we might say tonight is graded before we walk in: green if it's verified against a primary source, amber if it's single-sourced and has to be said with a caveat, red if we're not allowed to say it at all until a specific action closes it, and hypothesis if it's ours and unvalidated, and the word "hypothesis" has to be spoken out loud every time. There are numbers on our own reference card right now we are not permitted to say tonight because we haven't verified them ourselves yet. That's not a hedge, a hedge would be vague language that lets us claim anything later. A graded, falsifiable label is the opposite, it's a commitment to being provably wrong in a specific, checkable way if we're wrong.

**If they push:** "Give me an example of a number you're currently not allowed to say. There's a widely reported percentage on agentic AI adoption in this ecosystem that our own internal documents state two opposite ways, and until we resolve which is correct, we say neither."

**Grade: PASS**

**Landmine:** This answer is only as strong as our actual discipline in the room. One invented number in the next four minutes, after this speech, ends the credibility of everything above it.

---

### F4. "If you had to bet your own money on this company today, would you?"

**What they are really asking:** Strip away the pitch, do you actually believe this, or are you performing conviction.

**Answer:** Yes, and here's the honest shape of that bet, not a bigger claim than it deserves. Every layer of this idea is unproven right now: whether the buyer feels this pain the way we think, whether anyone pays for it, whether an administrator or a Big Four firm already owns the job. Stack enough unverified layers and the probability this is a real business, today, is genuinely low, and I'd rather say that than round it up to sound fundable. What I'd bet on isn't today's probability, it's the cost of finding out. Eight weeks of real conversations with the people who actually do this job is the cheapest possible way to move that number, up or down, and I would rather spend eight weeks proving myself wrong fast than a year building on an assumption nobody checked.

**If they push:** "So you might come back from residency and kill it? Yes, and I'd tell this exact panel that, not just my co-founder."

**Grade: PASS**

**Landmine:** None numeric, since this answer deliberately avoids quoting a probability we can't source. The risk is tonal: this only lands if it sounds like conviction, not like a rehearsed line about being willing to fail.

---

## SECTION G. Closing

### G1. "If you had to cut everything except one thing, what's the one part of this that, if it goes, the product is dead?"

**What they are really asking:** Do you know what you actually built, or is this a features list you're hoping holds together.

**Answer:** One line, and it never gets cut regardless of what else does: ingest, propose with a source pin, hit a conflict, abstain, a named human decides with a reason, a second named human signs off, seal, and a tamper attempt breaks the seal visibly. Everything else, the risk board, the API surface, a second document type, is negotiable against the clock. That sequence is not, because it's the entire claim in one motion: a model that proposes but never decides, a disagreement that stays visible instead of getting silently resolved, and a record that proves what happened without needing us to vouch for it. If a track pivot forces the story to change Friday morning, the story changes. That sequence does not.

**If they push:** "What's the actual first thing you'd cut under time pressure? The API surface, then risk-board depth. Never the conflict-abstain-decide-seal loop, and never the honesty labelling on screen."

**Grade: PASS**

**Landmine:** None, this is a locked internal decision, not a claim about the world. The only failure mode is not actually holding the line under real Friday-night time pressure.

---

### G2. "Alright, different question. What do you actually need from us, from the residency, if you get it?"

**What they are really asking:** Do you know exactly what to ask for, or would you waste eight weeks figuring out what you needed.

**Answer:** Access to talk to people, specifically. At minimum five workflow conversations: two accountable FME compliance or principal officers, two fund administrators, and one independent compliance provider, and I'd take more if offered. Proximity to 217 entities that are legally required to sit inside one square kilometre is the actual scarce resource here, not the stipend. Second: if IFSCA staff or programme mentors will spend even thirty minutes on the regulatory-reporting side of this, that's worth more to us than most things money buys. On the prize itself: the scheme publishes reimbursable grants in the 15 to 50 lakh range as of the current published guidance, and we have applied for nothing and been promised nothing, so that's not what's driving this ask. We arrive with working software and we leave with either validated buyers or a thesis we can honestly say we killed. Both outcomes are a real return on eight weeks of your programme.

**If they push:** "What if the conversations kill the thesis in week two, not week eight? Then we say so immediately, in writing, and ask what else in your ecosystem we should be looking at instead. That's a better use of the residency than riding out a dead idea to the deadline."

**Grade: PASS**

**Landmine:** The specific grant figures are published guidance, re-confirmed against secondary sources but not against the March 2026 sandbox framework directly. If a programme officer in the room knows those amounts changed, we need to update in real time, not argue.

---

## The five that will actually get asked, ranked

Opinionated, in order, with why. If drilling time runs short before Friday, drill these five until they're boring, then work outward.

**1. C4, the efficiency trap ("you cost more than the problem you replace").** This is the single most likely question in the room because it takes a judge thirty seconds of mental arithmetic to find, and both accelerator brain and regulator brain can run it. It is also our best-armed answer, because we ran the arithmetic against ourselves before anyone else could. A question this findable, with an answer this rehearsed, is exactly where founders win or lose the room.

**2. B2, zero customers.** It is the default first question any investor-minded judge asks any pre-revenue founder, and the rubric explicitly scores Honesty & Roadmap Credibility at 20%. It costs nothing to prepare for and everything to fumble. Every hackathon panel we can find a pattern for asks some version of this in the first two minutes.

**3. A1, isn't this just DRR.** IFSCA is the hackathon's named regulatory partner. A room that includes anyone regulator-adjacent will reach for "hasn't the regulator already solved this" before they reach for anything else, because it's the most obvious objection to the entire category, not just to us.

**4. E3 and E4 together, AI-written code and the git-audit attack.** The brief itself states commit histories will be audited, which means the organisers pre-announced this exact scrutiny. Any judge who actually reads the rubric will treat this as a check they're supposed to perform, not an optional dig.

**5. C2 and C3 together, unit economics and pricing defence.** Founder & Venture Assessment is 30% of the score, the single largest category, and every number behind our price is explicitly labelled hypothesis on our own fact card. A sharp business-minded judge will find the softest part of the pitch fastest, and this is it.

---

## Open gaps needing founder decisions

Each of these cannot be closed by rereading the documents. Each needs the founder to decide, verify, or ask a specific person, before Friday.

1. **Does IFSCA's July 2026 AI survey report 45% of entities exploring agentic AI, or 45% not yet exploring it?** Our own internal documents state it one way; a re-check on 18 August found a secondary source stating the opposite. FACT_CARD marks this RED, unsayable in either direction, until the founder locates the primary PDF or resolves the conflict. This is the single most time-sensitive open item on the whole card, due today.

2. **Is the second founder's name Mahek Soni (RESOLVED) in every public-facing artifact, including the ones we say out loud on stage?** CANON.md records that some war room documents say Sony and others say Mahek, and does not resolve which is correct. This has to be settled before any team question gets answered by name.

3. **Is the real-product data-custody architecture on-device or cloud-based via AWS Bedrock?** Earlier research argues for on-device specifically so a regulated customer's documents never leave their own infrastructure. The hackathon build plan commits to live AWS Bedrock extraction for the Technical Execution score. No document reconciles these, and they are two different promises to a privacy-focused buyer.

4. **Has `npm test` been run against the public ATTEST repo to confirm the check suite still reports 251, or does the pitch say "over 150" all the way through Saturday?** This is a five-minute task with its own same-day deadline that, as of this writing, has not been closed.

5. **Is the hackathon's Top-3 prize the Innovation Sandbox or the FinTech Sandbox?** The public programme page and press coverage name these differently, and under the March 2026 framework they may be two different things with different terms. Only the organiser can answer this.

6. **Do the FinTech Incentive Scheme grant amounts (15, 30, 50 lakh) still hold under the 16 March 2026 Sandbox Framework?** They are corroborated across secondary sources into mid-2026 but not confirmed against the superseding framework directly. Only the organiser, asked in person, closes this.

7. **What is our actual unit economics answer: a labelled hypothesis number for gross margin and implementation cost, or a permanent "unmeasured"?** No document, including FACT_CARD, contains even a hedged figure here. Right now C2 has no number to fall back on at all, and the founder needs to decide whether to construct one honestly before Friday or commit fully to answering with nothing.

8. **Has scoped legal advice been sought on the TechFin and Ancillary Services perimeter, data custody, and our own professional-liability boundary?** PRODUCT_DECISION.md names this as a required gate before company-wedge approval and attaches no owner or date to it. The founder needs to decide whether any informal opinion is reachable before Friday or whether "not yet reviewed" is the answer we carry onto the stage.

---

## Adjudicated answers to two open decisions (Fable, 2026-08-19)

Two of the open decisions above are not research gaps. They are decisions, and leaving them open until Saturday would be a mistake because both are likely to be asked. Decided here; founder may overrule.

### Decision A: the data-custody contradiction (open decision 3)

**The apparent contradiction.** Earlier research argued for keeping regulated documents inside the customer's perimeter. The hackathon build runs live extraction on AWS Bedrock. A juror who has read both would call that inconsistent.

**It is not inconsistent, and the answer is a strength.** The architecture already separates the model plane from the evidence engine through the `ModelProvider` interface (BUILD_SPEC section 3, doc 04 section 3). That boundary is the whole answer.

**The spoken answer, roughly 35 seconds:**

> "Today's demo runs the model on Bedrock, because the data is synthetic and because that is the infrastructure this event provided. For a real fund, that is the wrong default and we know it. The model call sits behind a provider interface, so the model plane runs wherever the customer's rules require: their own cloud account, their own VPC, or on premise. The evidence engine, the conflict logic, the manifests and the sign-off do not change based on where the model runs. We have not built either deployment, so treat that as design intent, not a claim. What I can show you is that the boundary exists in the code today, because we needed it for offline replay anyway."

**Why this scores.** It converts a privacy objection into a demonstration of architectural foresight, and the last sentence is checkable on screen. Do not claim we have built a customer-perimeter deployment. We have not.

**Grade: PASS**, conditional on never overstating the deployment.

### Decision B: unit economics (open decision 7)

**The call: give a labelled hypothesis, not a refusal.** "We have not measured it" is the right answer about accuracy, where a wrong number is dangerous. It is the wrong answer about unit economics to an accelerator jury, because it reads as not having thought about the business. Plug and Play backs founders who know their own cost structure even when the numbers are unproven.

**The spoken answer, roughly 45 seconds, every number labelled hypothesis:**

> "Marginal cost to serve is small and I can bound it: it is model inference plus storage, and inference on a bounded set of fields per quarter is cents, not rupees. So gross margin on paper looks like software margin. I do not think that is the interesting number, and I would not want you to score us on it. The number that decides whether this is a product or a consulting business is implementation cost per customer: how many days it takes to map one fund's document set and get their first return through. That is a hypothesis I cannot price yet, and it is the first thing the residency answers. If it is under a week, this is a product. If it is a month, it is a services business wearing a product's clothes, and I would rather find that out in October than in year two."

**Why this scores.** It names the metric that actually determines the business model, admits the unknown precisely, and states a falsification threshold. That is founder-assessment material.

**Grade: PASS**, conditional on the word "hypothesis" being spoken and no rupee figure being invented for implementation cost.

### Remaining open decisions unchanged

Decisions 1, 2, 4, 5, 6 and 8 above still need the founder or an external answer. Decision 1 (the 45% agentic direction) and decision 2 (Member 2's name) are the two that must close before Thursday.
