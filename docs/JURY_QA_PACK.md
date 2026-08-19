# JURY Q&A PACK: the synthetic data, and everything built after the red team was written

Status: STABLE. Written 2026-08-19 against exactly what is in the build, verified
by running it. Every number traces to `MEASURED_RESULTS.md`, `FACT_CARD.md` or
`CANON.md`.

**This does not replace `QA_REDTEAM.md`.** That bank holds 30 hostile questions on
product, moat, market, money, team and risk, and it stands. This pack covers two
things it cannot: the synthetic-data provenance block the founder asked for in
full, and every surface built after that bank was written on the morning of
19 August.

---

## The three rules, restated because they carry the section

1. **Answer the question that was asked, in one sentence, before any context.**
2. **If the honest answer is "we do not know", that is the answer**, followed by
   what we would have to do to find out.
3. **Never defend a number we cannot source.** Say "that is a hypothesis" or say
   nothing.

The product refuses to answer when it cannot prove the answer. If we do not hold
ourselves to the same rule in the Q&A, the demo is a costume.

---

# PART A. The synthetic data

This is the block the jury will press hardest, because it is the one place where
a two-person team with no customers is most exposed. Answer it directly and it
becomes the strongest part of the pitch, because almost nobody volunteers this.

### A1. "Is any of this real?"

**No. Every entity, person, figure and document in the demo is fictional, and
every document says so on its face.**

Each source document carries the line `SYNTHETIC TEST DOCUMENT, NOT A REAL
RECORD` above its figures, so a screenshot cannot be mistaken for a real record
even out of context. Twenty fictional fund management entities, 26 cases, 115
documents, and 80 prior quarterly filings. There is no real fund, customer,
investor or person anywhere in it, and there never has been.

### A2. "So what does a demo on invented data actually prove?"

**It proves the pipeline does what the design says on ten distinct shapes of
failure, and nothing beyond that. It does not predict behaviour on a real return.**

Say the measurement, then the limit:

> "We planted ten different kinds of document disagreement across 24 cases. The
> ground truth was written by deterministic code before any model saw the case,
> so it is not the system grading itself. It named the right field with exactly
> the planted cause 24 times out of 24, and it picked a value on its own zero
> times out of 24.
>
> And I will say the obvious thing before you do: we wrote those conflicts. A
> detector scored against conflicts its own authors planted is a consistency
> check, not an accuracy claim. What it shows is that the refusal is structural
> rather than decorative. What it cannot show is what happens to a scanned page
> with a handwritten correction on it. That needs someone on the inside, and it
> is what we are asking for."

### A3. "How did you get access to fund data?"

**We did not. We have never seen a real quarterly return.**

Do not soften this. It is the credibility moment:

> "We are outsiders. No customers, no data, no introductions. We built this from
> published IFSCA circulars, the enforcement record, and the DRR tender
> documents, and from our own reading of how these filings are assembled.
> Everything you are looking at, we worked out from the outside."

### A4. "Then how did you decide what the documents should look like?"

**From what the rules require to be reported, and from the conventional shape of
each document type. Both are assumptions, and here they are.**

The four reported fields are committed capital, drawn capital, closing NAV, and
complaints closed in the quarter. The filing cadence and deadline are sourced:
21 calendar days after quarter end, four times a year, per the IFSCA circular of
31 May 2023 as amended 3 November 2023.

The corpus carries five document types: a quarterly administrator statement, an
internal ledger export, a subscription register extract, a custody and cash
confirmation, and an independent valuation certificate, plus scheme-level and
rupee summary schedules on the multi-scheme and mixed-currency entities.

**The assumption, stated plainly:** that a fund of this shape receives its
numbers from several independent parties who close their books at different
times and answer different questions. That is the assumption the entire product
rests on. It comes from the structure of the market rather than from a document
we have seen: 217 fund management entities run 360 schemes, and the fiduciary
segregation circular of 10 April 2026 forces existing schemes to comply by
30 September 2026, so one firm can no longer be fiduciary and administrator and
valuer and auditor. More independent firms means more overlapping records per
fund. **If that assumption is wrong, our product is much less useful, and it is
the first thing we would test with a real entity.**

### A5. "How close is this to real data? Be specific."

**Structurally close on purpose, cosmetically nothing like it, and we can tell you
exactly which is which.**

| | Our corpus | A real return, as best we understand it |
|---|---|---|
| Field semantics and the arithmetic between them | Same. Undrawn equals committed minus drawn, and the system checks that identity | Same |
| Several parties reporting overlapping figures at different cut-offs | Same, deliberately | Believed same, unverified by us |
| Format | Plain text, machine clean | PDF, Excel, Word, some scanned. The DRR tender itself requires multi-format submission support |
| Noise, OCR error, handwriting, stamps | **None** | Present, and we have not modelled it |
| Volume | 115 documents | About 36,000 files over five years across several desktops, for 750-plus regulated entities, per the DRR tender |
| Conflicts per quarter | Planted, one signature archetype per entity | Unknown to us. We have no base rate |

**The two lines to say out loud:** we modelled the structure and not the mess,
and we have no idea what the real base rate of conflict is. A published benchmark
in 2025 put the best multimodal model at about 96 percent on clean invoices and
about 87 percent on scanned receipts, which is the gap between our corpus and a
real one. We are on the clean side of it.

### A6. "How did you actually make the corpus? Did an AI write your evidence?"

**Deterministic code owns every number, every planted conflict and every content
hash. A model writes only the surrounding prose.**

This split is the whole answer, and it is worth being precise about:

> "If a model had written the figures, the conflicts would be whatever the model
> felt like producing that run, and the demo would be unreproducible. So the
> generator computes every number and every planted disagreement in ordinary
> code. A small model writes only the paragraph of covering text around them, so
> the documents read like documents instead of like a fixture file. On the last
> build that was 104 calls, and none of them touched a figure."

### A7. "Your conflicts are planted. Of course your system catches them."

**Yes. That is why we also measured the case where we handed the same documents
to a frontier model with a good prompt, and it did fine.**

This is the answer that wins the room, because it is the one they do not expect:

> "We ran the same corpus through three frontier models on Bedrock, each told
> explicitly to answer UNCERTAIN when sources disagree. All three abstained
> correctly on every conflicted field. Zero silent picks. We predicted they would
> fail and they did not, and we are showing you that table rather than the one we
> hoped for.
>
> One column separated them. On evidence localisation, one of the three could not
> produce a single quote that actually appeared in the source document, character
> for character. A quote you cannot find in the document is a claim about it, not
> a citation of it.
>
> So we are not going to tell you a model cannot read a page. What none of those
> three produced is a named decider, a written reason, a second signature, or the
> same answer eleven months from now, because that is not a text-generation
> problem."

Full table and its limits in `MEASURED_RESULTS.md` section 2. **The sample is
eight fields at one run each. Do not let it be quoted as a benchmark in either
direction, including ours.**

### A8. "Why should I believe the demo is not just a recording?"

**Part of it is a recording, and here is exactly which part.**

> "The offline path replays recorded model responses where it has one and falls
> back to plain deterministic string matching where it does not. That is what
> keeps the demo working on a venue network. The live path is real: nine roles,
> five models across four companies, 40 agent actions, and it completes a full
> case in between three and eight seconds on three consecutive measured runs. We
> can run it live if you want it, and it costs about fourteen thousand seven
> hundred tokens, which the system records per action rather than estimating."

Do not claim the offline path uses a local open-weight model. The provider
interface exists; the wiring does not.

### A9. "What would change your mind about any of this?"

**A real corpus where the conflicts are rare.**

> "Our whole thesis is that a fund receives overlapping records from parties that
> disagree more often than anyone admits. If we got access to a real entity's
> last eight quarters and found that conflicts are rare and mostly trivial, the
> product is a nice audit trail attached to a problem nobody has. That is the
> first thing we would measure, and we would rather find out in a residency than
> after eighteen months of building."

---

# PART B. The surfaces built after the red team bank was written

Nothing in `QA_REDTEAM.md` covers these, because none of them existed when it was
written.

### B1. "Why should I trust a verdict the machine printed?"

**You should not, which is why every verdict on screen is clickable and opens the
working.**

Clicking any verdict shows, in order: the numbers with their sources, the ordered
tests that were run, which were ruled out and why, which fired, which were never
reached, who stands behind each document and who to contact about it, and what
happens next. A juror does not have to take the conclusion on faith, and neither
does a compliance officer eleven months later.

### B2. "What stops your agents running away with it?"

**One deadline for the whole run, enforced, and it escalates rather than
finishing badly.**

The orchestrator sets a single wall-clock deadline, default 30 seconds, hard
ceiling 60. Every step races the remaining time. A step still running at the
deadline returns a timeout and the case escalates to a named human. Verified by
running it: a permanently hanging agent against a 30 millisecond budget escalates
in 36 milliseconds. Retry budget is 0 to 2 per step, re-plans 0 to 1, and a plan
outside those bounds is rejected before the run starts.

### B3. "Your own AI decides what is worth reading. What if it skips something?"

**It did, on the first live run, and that is why there is a floor under it.**

The strongest technical story in the build:

> "With a working prompt, our triage model read the administrator statement and
> returned two fields, silently dropping a third that was plainly on the page.
> Nothing downstream could have caught it, because if the field is never
> extracted there is no candidate to check and no disagreement to preserve.
>
> That is the exact failure we exist to prevent, committed by our own system. So
> now plain string matching runs across every document for every field label,
> independently of the model, and anything it finds is added back whatever the
> model said. Triage may narrow the work. It may never lose evidence. And when
> the floor overrules the model, the run says so on screen in words, because a
> correction nobody can see is indistinguishable from the model having been
> right."

### B4. "Who checks the checker?"

**Nobody, and that is the point: two of the nine roles contain no model at all.**

The binder and the validator are ordinary code. The binder ignores whatever
character offsets the model claims and locates every quote in the source text
itself, dropping any candidate whose quote is not there character for character.
The validator checks the accounting identity: undrawn commitment equals committed
capital minus drawn capital, per document. A model cannot verify a model.

Separately, the critic and the extractor are forced onto independent model
families, and that is checked at startup rather than in review. If no independent
critic route is available the system refuses to start, because a model
criticising its own reading is not criticism.

### B5. "What happens to the other numbers when the human picks one?"

**The system shows which of them no longer tie.**

After a decision, the deterministic identity checks re-run and reveal the numbers
that are now inconsistent. Choosing the ledger's drawn capital figure changes what
undrawn commitment has to be, and the screen says so rather than leaving a
quietly broken return.

### B6. "Can anyone verify your evidence bundle without your software?"

**Yes, and the verifier is inside the bundle.**

The evidence bundle carries full hashes, every source document, and its own
independent Python verifier. A regulator, an auditor or an opposing party can
check the chain without installing anything of ours and without trusting us. If
they had to run our software to check our work, it would not be evidence.

### B7. "One quarter proves nothing. What does living with this look like?"

**Five quarters, on every entity, and the same disagreement recurs.**

80 prior filings across 20 entities, carrying 106 recorded disagreements and 187
officer notes. The point the history screen makes is that the same conflict
returns every quarter on the same fund, so it is structural rather than an
incident.

**The single strongest story on stage** is Nilgiri Opportunities. Three quarters
settled by one Compliance Officer. She leaves. Her successor inherits the same
conflict and, in every tool that exists today, none of the reasoning. A change of
Compliance Officer is notified to IFSCA within 15 days and the records have to
survive 8 years, and the reasoning is the part that normally dies. Worth switching
entities for.

---

# PART C. The questions about our own numbers

### C1. "What is your accuracy? Give me a number."

**24 of 24 on planted archetypes, 0 of 24 silent picks, and that number means
less than it sounds like.**

Give the number, then dismantle it yourself before they do. The scope is in
`MEASURED_RESULTS.md` section 1: our conflicts, our corpus, recorded path, one
run per case. Then pivot to the number that does mean something: zero silent
picks, because a silent pick is the only failure in this product that nobody
downstream can detect.

### C2. "You have 299 passing tests. Did they catch anything real?"

**No, and that is the most useful thing we learned.**

> "Six defects survived a written contract, a nine-role architecture, 299 passing
> tests and a 24-check conformance gate. Every one of them was found within a
> minute of actually using the product, and none by reading the code. The worst
> was that the interface had never been wired to the endpoint the demo's best
> screen depends on, so on stage it would have shown a juror a raw engine
> rejection.
>
> The fix was not more tests. It was a scripted pass over every entity and every
> screen asserting two things: no machine word reaches the screen, and no screen
> renders empty where it should render content. That found three of the six in
> under a minute."

### C3. "Your own eval file says 50 percent. Explain that."

**The label file is wrong and the product is right, and we can show you exactly
how.** Do not bluff this one.

Three faults: most of its labels point at cases that were never generated; four
labels mark a field as needing a single answer when CANON designs it as a version
conflict, so the product correctly abstains and is scored as a miss; and two
labels transpose which field has no source. The labels predate the final case
design and were never re-derived.

`MEASURED_RESULTS.md` section 5 carries the detail, and the fix is a five-line
gate that fails when a label names a case absent from the corpus or asserts a
state CANON contradicts. **That file does not travel to Friday.**

### C4. "What does it cost to run?"

About 14,700 tokens for a complete nine-role case, recorded per agent action
rather than estimated. **No dollar figure**, because the IAM user has no pricing
API access, so any price would be recalled rather than sourced. The token count
is the honest number and the cost follows at whatever the published rate is that
day.

### C5. "What did you build in 22 hours versus before?"

**No application code existed before the sprint started, by rule, and the commit
history is auditable.** What we carried in is what the rules permit:
specifications, schemas, prompts, and the synthetic data plan. See
`AGENT_CONTRACT_PACK.md`, which is that carry pack, and `REPO_FIRST_COMMIT_PACK.md`.

---

# PART D. The four sentences that survive if everything else is cut

1. **"The product refuses to answer when it cannot prove the answer."**
2. **"Two of the nine roles contain no model at all, because a model cannot
   verify a model."**
3. **"We have never seen a real quarterly return. Everything here we worked out
   from the outside, and the parts we could not work out are marked as not built
   rather than guessed at."**
4. **"We predicted a frontier model would fail this and it did not. We are showing
   you that table anyway."**

---

## What not to say, under any pressure

- No dollar cost. We cannot source the price.
- Not production ready. It has run one corpus of synthetic documents.
- The measured rate limits are ours, on our account, on that day. They are not
  anyone else's allowance.
- The offline path is not a local open-weight model.
- Per-field regulatory rule mapping is not built. **Do not invent a citation.**
  The screen already says it is absent, and that is the correct answer.
- Never present the baseline table as a win.
