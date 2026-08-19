# PITCH, 3 MINUTES, ROUND 1

Status: STABLE. Rewritten 2026-08-19 against the simplified build. Every number
traces to `PRODUCT_AND_WORKFLOW.md` or `MEASURED_RESULTS.md`.

Round 1 is a **3 minute pitch and 7 minutes of Q&A**, all teams, strict timer.

**Word budget: about 420 words spoken.** Everything below is written to be said
at an unhurried pace, not read fast.

---

## 0:00 to 0:20, the cold open

> "A fund in GIFT City has to file four numbers to the regulator every quarter.
> Committed capital, drawn capital, net asset value, complaints closed.
>
> Those four numbers arrive from five different parties. The administrator, the
> internal ledger, the subscription register, the custodian, the valuer. They
> close their books at different times, so **they disagree**, and nothing in any
> of the documents tells you that."

*[On screen: the dashboard. Three of the four bars stop early and go hatched.]*

---

## 0:20 to 0:40, the claim

> "Every system built for this picks a number. Ours refuses to.
>
> On this fund, the ordinary rule, take the figure most documents agree on,
> files seventeen point eight million for drawn capital. **That is the wrong
> number, and nothing announces it.** The right one is nineteen point three, and
> only a person who knows a capital call landed at 17:42, after the
> administrator's four o'clock cut-off, can know that.
>
> A silent pick is the only error nobody downstream can catch, because there is
> no disagreement left to find."

---

## 0:40 to 1:50, the demo

*[Click drawn capital.]*

> "Every number is pinned to the exact line it came from, with who wrote it and
> what moment it was true. This one says the sources disagree, and here is why:
> both are correct, at different cut-offs."

*[Click the complaints field.]*

> "This one is different. **No document contains it at all.** So it cannot be
> decided. It can only be attested, by a named person putting their name to a
> number with no source, and it is marked that way permanently."

*[Open the Trace screen.]*

> "Nine steps. **Four of them use a model. Five are plain code.** Three different
> models from three different companies: Amazon reads, Mistral attacks the
> reading, Z.ai describes the disagreement.
>
> And the three steps that decide whether a number survives have no model in
> them at all. Does the quoted line actually exist in the document? Does the
> arithmetic tie? That is string matching and subtraction. **A model cannot check
> a model.**"

*[Decide, then sign-off, then tamper.]*

> "A named person decides in writing. A second person, who cannot be the first,
> signs off. Then the record seals, and if a byte changes the chain breaks
> visibly."

---

## 1:50 to 2:20, why us and why now

> "We are outsiders. No customers, no data, no introductions. We built this from
> published IFSCA circulars and our own reading.
>
> The timing is not ours. The fiduciary segregation circular means that from the
> thirtieth of September, one firm can no longer be fiduciary and administrator
> and valuer. **More independent firms means more disagreement per return.** And
> the regulator's own DRR system is at least six quarterly cycles away, so those
> filings get made the old way in the meantime."

---

## 2:20 to 2:40, the honest slide

> "Three things you should know before you ask.
>
> **We predicted a frontier model with a good prompt could not do this. We ran it
> and it could.** Three models, told to abstain on disagreement, all abstained
> correctly. We are showing you that table rather than the one we hoped for.
>
> **Per-field regulatory rule mapping is not built.** It says so on the screen. We
> will not invent a citation.
>
> **And every document you just saw is fictional**, and says so on its face."

---

## 2:40 to 3:00, the ask

> "We took two models out of this system this week and the measured result did
> not move. Twenty-four out of twenty-four planted failures caught, zero silent
> picks, before and after.
>
> Everything still missing is something only access can fix. Twelve
> introductions, twenty quarters of real redacted documents, twenty hours with
> the officers who sign, and two hours with supervision on which rule requires
> which field.
>
> **We got this far with no access. Give us sixty days with it.**"

---

## The three sentences that must survive if everything else is cut

1. **"Every system built for this picks a number. Ours refuses to."**
2. **"Nine steps, four use a model, five are plain code, and the ones that check
   are the ones without a model. A model cannot check a model."**
3. **"We have never seen a real quarterly return. Everything still missing is
   something only access can fix."**

---

## If you are running behind at 2:00

Cut the Trace screen narration to one sentence: *"Nine steps, four use a model,
five are plain code, and the checking ones have no model."* Keep the demo and the
ask. **Never cut the honest slide**, it is 20 percent of the score.

## If you are ahead at 1:10

Add the History screen: *"Five quarters on this fund. The same disagreement every
quarter. It is not an incident, it is how this fund receives its documents."*
Then the officer turnover story: *"Three quarters settled by one Compliance
Officer. She leaves. In every tool that exists, her successor inherits the number
and none of the reasoning."*
