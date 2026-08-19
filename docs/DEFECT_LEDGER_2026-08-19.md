# DEFECT LEDGER: what using the product found that reading it did not

Written 2026-08-19. Every entry below was found by clicking, not by review, and every one was reproduced before it was fixed. Recorded because the pattern matters more than the individual bugs: **six defects, all invisible from the code, all obvious within one minute of using the thing.**

The rule this supports: verify by running, never by reading.

---

| # | Defect | How it would have failed on stage | Class |
|---|---|---|---|
| 1 | The frontend was never wired to `POST /api/attest`. The decide panel posted every field to `/api/decide`, which correctly refuses an unsourced field | On the screen CANON section 14 calls our strongest, the founder clicks through and gets a raw engine rejection containing the literal string `attest()`. The field never resolves. The demo dead-ends | Integration gap between two lanes that each worked |
| 2 | `CAUSE_META` mapped four causes; the corpus produces seven | On four of the ten archetypes the screen silently never said why the documents disagreed. No error, just absence | Incomplete map with an empty-string fallback |
| 3 | The app booted into `cases[0]` from a directory listing, which sorts the clean comparison quarter first | The opening screen shows four identical green cards instead of the four planted conflicts. Ten seconds of juror attention spent on the wrong case | Implicit ordering assumption |
| 4 | `ATTESTED` and `CONFIRMED_UNSOURCED` were missing from `STATE_META` | An attested field rendered a raw `ATTESTED` chip, coloured green as though it agreed with a source, showing no value at all | Missing map entry with a fallback that printed the key |
| 5 | The case state never advances past `INGESTED` after a governed run | The progress stepper said "Ingested" above four extracted fields, and the analysis button stayed clickable and returned a rejection on click | Display trusting a label over the content |
| 6 | `reset.sh` deleted every `data/case-*.json` and regenerated only two | Running the documented reset drops ten of the twelve entities from the picker. The product looks like it handles one fund | Cleanup broader than the rebuild that follows it |

---

## Three more, found on the evening of 19 August by scoring and deploying the build rather than trusting it

| # | Defect | How it would have failed on stage | Class |
|---|---|---|---|
| 7 | `data/eval-labels.json` contradicts CANON. Most of its labels name cases that were never generated. Four mark F1 on the demo case as needing one answer when CANON designs it as a version conflict, so a correct abstention scores as a miss. Two transpose which field has no source | A judge opens `data/` and finds our own eval file reporting 50 percent abstention correctness and 0 percent field recall on a build that passes 24 of 24 canon checks. No verbal correction recovers that | An answer key that drifted from the design it grades |
| 8 | The corpus generator writes document prose with a model, so regenerating the corpus changes every document, every prompt and every prompt hash. Replay fixtures are keyed by prompt hash | Extraction silently moves from replaying recorded model output to plain deterministic string matching. The demo still works, which is exactly why nobody notices, and a claim about what the offline path does becomes untrue without anyone editing it | A cache keyed on something that quietly moves |
| 9 | Agent run status had no label map at all in the interface. `REJECTED_BY_GUARD` rendered raw on the Trace screen of most entities | The founder opens Trace to show the guard refusing an agent that tried to remove a preserved conflict. That is the single most important thing the system does, and it reads as a machine word. Found only by sweeping the cloud-deployed build, after the local sweep had been declared clean | A display map that was never written, not one that fell short |

**Defect 7 is the same class as defect 2 and defect 4**, which is why it matters
more than its own severity. All of them are a lookup out of step with the data it was
written against: a cause map short of the corpus, a state map short of CANON, a
label set short of CANON, and in defect 9 a map that was never written at all. That is the third instance, so it is a
rule rather than an incident, and it is written into
`AGENT_CONTRACT_PACK.md` section 8 as a build-order item: **anything that maps or
grades the corpus is derived from CANON, never hand-written, and a gate fails when
it names something the corpus does not contain.**

## The near miss worth recording, because it cuts the other way

The first scorer written to measure the archetype corpus reported 22 of 24 and
blamed the product for missing both duplicate-document cases. The product was
right. It reports a duplicate under its own key and leaves the field
`SUPPORTED`, because several candidates agreeing is not a disagreement, and the
scorer only read the conflict key.

Recorded because it is the same failure as defect 7 pointed at ourselves: a
measuring instrument that drifted from the design it measures. **Two iterations
of an unexplained result means the instrument is suspect, not only the subject.**
Had that number been published without checking the field object, we would have
walked into the room disclosing a defect that does not exist, which is exactly
what happened with the wall-clock budget and cost us on eight review perspectives.

---

## The one that is not a code defect

`tools/canon_check.py` treated only `DECIDED` and `CONFIRMED` as states a field may legitimately advance into. `ATTESTED` and `CONFIRMED_UNSOURCED` were added to CANON on 19 August, after the gate was written. Attesting F4 is a scripted step of the demo, so walking the demo and then running the gate reported **`1 of 24 checks FAILED` on a build that was correct**.

A gate that cries wolf minutes before a pitch is worse than no gate, because the founder either ignores it, in which case it is useless, or believes it, in which case it costs them the pitch. Gates need updating when the canon they check moves.

---

## What this says about the process

Every one of these survived: a written contract, a nine-role agentic architecture, 284 passing tests, and a 24-check conformance gate. The tests assert on source text and on engine behaviour. None of them opened the product and clicked the thing a juror would click first.

The cheap fix is not more tests. It is a scripted pass over every entity and every screen that asserts two things: no raw enum reaches the screen, and no screen renders empty where it should render content. That sweep found defects 2, 4 and 5 in under a minute, and it is the reason `scripts/demo-ready.sh` exists.

**Three instances of one class is a rule.** Defects 2 and 4 are the same class: a lookup map that fell short of the data and printed nothing, or printed its own key. The codified rule, now in `UI_LANGUAGE_AND_VISUALS_SPEC.md` section 0: every display lookup needs a fallback that sentence-cases an unmapped value, and every map must cover everything the corpus can produce.
