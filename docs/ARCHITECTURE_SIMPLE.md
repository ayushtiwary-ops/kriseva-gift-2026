# THE WHOLE SYSTEM, IN ONE PAGE

Status: STABLE. Rewritten 2026-08-19 after the architecture was simplified.
This is the only architecture document to memorise. Everything else is detail.

---

## Say this

> **"Read it. Check it. Refuse to guess."**

Three stages. Six steps. **Three of the six use a model. The other three are
plain code, and the plain code ones are the ones that check.**

That last sentence is the product. A model cannot check a model.

---

## The six steps

| | Step | What it does | Model? |
|---|---|---|---|
| **READ** | 1. Scope | Finds which documents mention which fields, by matching the field name in the text | **No** |
| | 2. Extract | A model reads every number for those fields and quotes the line it came from | Yes |
| **CHECK** | 3. Bind | Looks for that exact quote in the document. If it is not there, the number is thrown away | **No** |
| | 4. Validate | Checks the arithmetic ties. Undrawn must equal committed minus drawn | **No** |
| | 5. Criticise | A second model, from a different company, tries to knock the reading down | Yes |
| **REFUSE** | 6. Reconcile | Where the numbers disagree, describes the disagreement and its cause. **Forbidden from choosing** | Yes |
| | | Then a named person decides in writing, a second person signs off, and the record is sealed | Human |

---

## How to explain each step in one sentence

**1. Scope.** "Before we read anything, plain code looks for the field name in
each document. No model. It used to be a model, and we took it out, because a
model that narrows the work can quietly drop a field, and ours did."

**2. Extract.** "A model reads the numbers and has to quote the exact line."

**3. Bind.** "We go and look for that quote in the document. If it is not there,
character for character, we throw the number away. That is not a model, that is
string matching."

**4. Validate.** "Undrawn commitment has to equal committed minus drawn. That is
arithmetic, not an opinion."

**5. Criticise.** "A second model, from a different company, tries to knock the
first one's reading down. Enforced in code: if the two ever end up on the same
model family, the system refuses to start."

**6. Reconcile.** "Where the documents disagree, it writes down what the
disagreement is and why. It is not allowed to pick. If it tries, the guard blocks
it and you see that on the screen."

**Then a person.** "A named human decides in writing, a second person signs off,
and the record is sealed so an edit breaks the chain."

---

## The three questions you will be asked, and the answers

**"Why is scope not a model?"**
> "It was. On a live run the triage model read the administrator statement and
> returned two fields, silently dropping a third that was plainly on the page.
> Nothing downstream could catch it, because if a field is never extracted there
> is no candidate to check and no disagreement to preserve. We put deterministic
> string matching underneath it as a floor, and then we noticed the floor was
> overruling the model every time they disagreed. So the model could only ever
> lose evidence, never save work the floor was not already saving. We removed it."

**"Why do you need two models?"**
> "Because a model checking its own reading is not a check. The one that reads
> and the one that criticises are forced onto different model families, and that
> is verified when the system starts, not in code review. If no independent
> critic is available, it refuses to run."

**"What actually stops it from just picking a number?"**
> "Code, not instruction. The reconciler's output is rejected if it contains a
> chosen value, a resolved state, or anything that looks like a human decision,
> checked at every level of the object. On a live run you can watch that guard
> fire. It shows on the Trace screen as blocked."

---

## What changed on 19 August, and why

**Before:** nine named roles, seven of them wired to models.
**Now:** nine roles still exist in the record, but only **six use a model**, and
only **six matter on stage**. Three of those six are plain code.

The three that never mattered on stage are infrastructure, and should be called
that rather than called agents:

| Role | What it really is |
|---|---|
| Orchestrator | The plan and the time budget. It is deterministic. Call it "the budget", not an agent |
| Narrator | One paragraph handing the case to a named person |
| Learner | The lesson ledger. Deterministic, and it must stay that way, because a model writing its own lessons is marking its own homework |

**Nothing was lost by simplifying.** Measured before and after, on the same
corpus: 24 of 24 planted failure archetypes still named exactly, still zero
silent picks, 299 of 299 tests passing, 24 of 24 canon checks. One fewer model,
one fewer failure mode, and a story that fits in a breath.

---

## If you have ten seconds

> "Six steps. Three use a model, three are just code, and the code ones do the
> checking. Where the documents disagree, it refuses to pick and hands it to a
> named person who signs for it."

## If you have thirty seconds

Add:

> "The number has to be quoted from the document, and we go and check the quote
> is really there before we keep it. The model that reads and the model that
> criticises come from different companies, and the system will not start if they
> do not. And the step that describes the disagreement is forbidden from
> resolving it, in code, so you can watch the guard block it."

## If you have one minute

Add the failure that proves it:

> "Our own scoping model dropped a field that was plainly on the page. Nothing
> downstream could have caught it. So we replaced it with plain string matching
> and took the model out. That is the whole thesis in one incident: the parts
> that check must not be the parts that guess."
