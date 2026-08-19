# UX PSYCHOLOGY SPEC: the interface and experience specification for KRISEVA ATTEST

Status: DRAFT, written 2026-08-18. Owner: founder. Consumer: the Friday build agent.

> **Independent verification, 2026-08-19.** Every contrast ratio in this document was recomputed from the hex values using the WCAG 2.1 relative-luminance formula. All 14 checked pairs match the stated figures to two decimal places, and all five state foreground-on-wash pairs clear the 4.5:1 AA body-text floor.
>
> One finding worth knowing on stage: the CONFLICTED amber and the SUPPORTED teal sit at relative luminance 0.0904 and 0.0910, a gap of 0.0006. On a greyscale or washed-out projector they are indistinguishable. That is not a defect in the palette, it is the reason the redundant encoding rule in section 3 (icon plus text label plus border treatment, never colour alone) is load-bearing rather than decorative. If the build runs short of time, the redundant encoding is not the thing to cut.

Scope: seven screens, static HTML, CSS and vanilla JavaScript, no build step, roughly 22 hours.
Ground truth: `CANON.md` (the fictional world, the seven screens, the state model, the four conflict causes) and `FACT_CARD.md` (what we are allowed to say). This document does not restate their numbers except where a screen needs a concrete example to build against. If this document and `CANON.md` ever disagree, `CANON.md` wins and this file is wrong.

How to use this document: every table is a literal build instruction. Token name, value, usage. No value here is a placeholder. Where a decision was a judgement call rather than an evidenced principle, it is labelled a judgement so a build agent and a juror both know the difference.

---

## 1. The design thesis

Within three seconds a viewer, most likely a compliance officer, a principal officer, or a juror who has read a hundred fund administrator statements, must feel that this screen belongs in the same category as the documents it is checking: composed, precise, institutional, calm under scrutiny. Not excited. Not impressed. Steady. That feeling is the product, not a wrapper on the product, because the entire commercial claim of ATTEST is trustworthiness under a signature that is legally personal (a compliance officer's name attaches to every decision, per `CANON.md` section 2). A buyer who is about to stake their name on what this screen tells them will not extend goodwill to a screen that looks uncertain of itself, and no amount of correct backend logic recovers that first impression once lost. We are deliberately avoiding three registers, each for a specific reason tied to that buyer:

- **Consumer app playfulness** (rounded mascots, bouncy confirmation animations, exclamation marks, gamified progress bars). Wrong because it signals low stakes, and the one thing this interface must never imply is that the decision being recorded is low stakes.
- **Dashboard maximalism** (a chart in every corner, borrowed from generic admin templates, everything visible at once). Wrong because `CANON.md`'s entire thesis is four fields, built on purpose, not forty. A maximalist layout visually contradicts the deliberateness of the demo's own data story and works against Miller's capacity limit (see section 2 and section 5): more visible elements competing for attention when the point is that exactly four things need it.
- **Security-theatre dark mode** (black backgrounds, neon green monospace, a "hacker" aesthetic). Wrong because it borrows the visual vocabulary of a different trust claim, cryptographic mystique, when ATTEST's actual claim is auditable, human-legible, regulator-respectable process. Banks, fund administrators, and regulators overwhelmingly present their own work in restrained, light, printable documents. Matching that convention (an application of Jakob's Law, section 2.5) reads as belonging in the room; a dark hacker aesthetic reads as arriving from a different, less accountable room.

---

## 2. Trust psychology: the eight mechanisms

Each mechanism below names a real, established principle, states what it predicts, states the specific interface decision it drives in ATTEST, names the screen it governs, and, where the evidence is popular but thinner than its reputation, says so plainly. These are design judgements informed by real research, not a claim that any of this was tested on this specific product; none of it has been.

### 2.1 Procedural justice (showing the work rather than the answer)

- **Principle:** Procedural justice theory (Thibaut and Walker, 1975; developed further by Lind and Tyler, 1988). An established theory from legal and organisational psychology.
- **Predicts:** people's acceptance of and trust in an outcome depends heavily on whether the process that produced it was visible, consistent, and accountable, not only on whether the outcome itself was favourable. Visible process ("voice," transparency, explanation) builds legitimacy somewhat independently of the result.
- **ATTEST decision:** no proposed value is ever rendered as a bare number. Every value carries a visible pin to the exact source document, region, and cut-off timestamp it came from. The interface shows the working, not just the answer.
- **Screen:** S2 Evidence workspace (primary), reinforced on S1 (every value shows a source citation inline) and S4 (the trace is the process, made inspectable).
- **Honesty note:** the underlying finding is well replicated in legal and institutional-trust research. Applying it to software interface design is a reasonable, common design analogy, not a direct finding about interfaces. That leap is ours, not the theory's.

### 2.2 Calibration and the avoidance of false certainty (preserved disagreement rather than resolution)

- **Principle:** confidence calibration research in judgement and decision-making (Fischhoff and Lichtenstein's calibration work is the standard reference), and Kahneman's "illusion of validity" as the failure mode being designed against.
- **Predicts:** trust erodes faster from one confidently wrong statement than from a stated, honest "the evidence disagrees." Well-calibrated uncertainty (visible hedging that matches the actual state of the evidence) sustains trust across repeated use better than a confident point estimate that occasionally fails.
- **ATTEST decision:** when two sources disagree, S3 shows both candidates with equal visual weight and no default selection. Related judgement, grounded in default-effect research (Samuelson and Zeckhauser, 1988, on status quo bias, and Johnson and Goldstein's work on default effects in choice): nothing is ever pre-selected, because a pre-selected option is disproportionately accepted regardless of correctness, which would quietly reintroduce the "silent AI just picks one" failure this product exists to prevent. A second related judgement, grounded in anchoring (Tversky and Kahneman, 1974): candidates are always ordered by a neutral rule (document ID) rather than by which one looks more authoritative, so the interface itself does not anchor the human toward one answer.
- **Screen:** S3 Conflict decision (primary), S1 (state chips never overstate certainty).
- **Honesty note:** calibration research is robust in forecasting and expert-judgement contexts. Extending it to how a piece of software should present two disputed numbers is a design judgement grounded in that research, not a direct study of this interface pattern.

### 2.3 Automation bias and algorithm aversion (the cost of a confident wrong answer versus a visible abstention)

- **Principle:** automation bias (Skitka, Mosier, and Parasuraman's human-factors research on over-reliance on automated aids) and algorithm aversion (Dietvorst, Simmons, and Massey's well-known finding that people lose trust in an algorithm faster after seeing it err, even when it remains more accurate than the human alternative on average).
- **Predicts:** a system that occasionally states a confident wrong answer takes a disproportionate trust penalty compared to one that visibly declines to answer. People forgive "I do not know" more readily than a confidently wrong answer, especially after the first one is caught.
- **ATTEST decision:** F4 (complaints closed) has no supporting source anywhere in the corpus. ATTEST is built to render UNSUPPORTED, never a plausible default like zero. This is a structural refusal enforced by the state machine, not a UI suggestion.
- **Screen:** S1 (F4's card), S2 (F4's empty evidence view).
- **Honesty note:** automation bias is robust and widely replicated. Algorithm aversion is real but narrower than it is sometimes presented: the same research group later found it weakens when people retain some control over the algorithm's output. Treat it as directional support, not an absolute law.

### 2.4 Progressive disclosure and cognitive load theory

- **Principle:** progressive disclosure (a standard interaction-design principle, popularised in usability practice) and cognitive load theory (Sweller, 1988).
- **Predicts:** working memory is limited; presenting all available detail at once increases extraneous load and degrades comprehension. Revealing detail on demand, in the order the task actually needs it, keeps the load that remains focused on the decision itself.
- **ATTEST decision:** S2's default view shows candidate summary cards (value, source, timestamp) only; the full source document and extended metadata expand on interaction. S4's trace rows show only the essentials and expand to full prompt hash and detail one row at a time.
- **Screen:** S2 and S4 primarily, also S5's per-indicator disposition panel.
- **Honesty note:** cognitive load theory is well established in educational psychology. Its extension into interaction design is now mainstream, near-uncontroversial UX practice, though the theory's original quantitative predictions come from learning tasks, not software decision tasks. A reasonable, low-risk extrapolation, still an extrapolation.

### 2.5 Jakob's Law of internet user experience (consistency and convention as a shortcut to credibility)

- **Principle:** Jakob's Law (Jakob Nielsen): users spend most of their time on other products, so they prefer a new product to behave like the ones they already know.
- **Predicts:** matching familiar conventions lowers the interpretive burden and reads as competent by default. Violating convention forces a conscious relearning of basic navigation, which reads as amateurish regardless of the engineering underneath.
- **ATTEST decision:** S2 places the source document beside the extracted value, the pattern already familiar from document-review and invoice-approval tools. S6's sign-off page uses a conventional, centred, formal-document layout rather than an inventive dashboard widget. Buttons, forms, and tables follow standard placement throughout rather than novel interaction patterns.
- **Screen:** applies globally; most load-bearing on S2 and S6.
- **Honesty note:** this is a practitioner heuristic, not a controlled experimental law in the way Fitts's Law is. It is broadly accepted in the field and consonant with familiarity-based trust findings such as the mere-exposure effect (Zajonc, 1968), but "Jakob's Law" itself is a named aphorism, not a peer-reviewed statistical constant.

### 2.6 The von Restorff (isolation) effect (making the abstention state impossible to miss)

- **Principle:** the von Restorff effect, also called the isolation effect (Hedwig von Restorff, 1933): an item that stands out from a set of similar surrounding items is disproportionately more likely to be noticed and recalled.
- **Predicts:** if every field card looked visually similar, a CONFLICTED or UNSUPPORTED field would blend into a row of "fine" fields and could be missed at a glance. Deliberately isolating the abstained state (distinct hue family, heavier border, distinct icon) makes it disproportionately noticeable against calmer, resolved cards.
- **ATTEST decision:** on S1, CONFLICTED and UNSUPPORTED cards use a visibly louder treatment (colour family, border weight, icon) than SUPPORTED, DECIDED, or CONFIRMED cards, and are never allowed to visually recede to the same weight as a resolved field. See section 3 for the exact tokens.
- **Screen:** S1 primarily, also S5's open-indicator rows.
- **Honesty note:** the original findings come from recall experiments with lists of items, not software interfaces. Applying it to dashboard card salience is a standard, well-worn design analogy, still an extrapolation from its original memory-research context.

### 2.7 The peak-end rule (applied to the demo sequence)

- **Principle:** the peak-end rule (Kahneman, Fredrickson, Schreiber, and Redelmeier, and related work): people judge and remember an experience largely by its most intense moment and by how it ends, far more than by the average of the whole experience.
- **Predicts:** a juror's overall impression of the demo will be shaped disproportionately by the single most intense moment and by the final moment, more than by the sum of every screen in between.
- **ATTEST decision:** the demo spine (`CANON.md` section 10) ends on the tamper-check breaking the seal on S7. That moment is built to be both the most visually and motion-intense point in the entire product (specified precisely in section 6) and the closing moment of the sequence, so it is peak and end at once. Nothing after it competes for the same intensity.
- **Screen:** S7 primarily; shapes the ordering of the whole S1 to S7 sequence.
- **Honesty note:** the rule is well replicated for experiences with a duration and a felt trajectory; its original studies used physical discomfort (colonoscopy, cold-water immersion). Applying it to a software demo watched by a juror is common practice in presentation design, and it is a judgement, not a replication of the original paradigm.

### 2.8 The aesthetic-usability effect, with its limits stated honestly

- **Principle:** the aesthetic-usability effect (Kurosu and Kashimura, 1995).
- **Predicts:** people perceive a more aesthetically pleasing design as more usable and extend it more patience and goodwill, independent of the design's actual functional usability.
- **ATTEST decision:** the restrained neutral palette, the single disciplined accent, the consistent spacing scale, and tabular monospace numerals are, in part, an aesthetic investment that buys goodwill and a "considered product" read in the first three seconds, before a juror has evaluated any of the other seven mechanisms.
- **Screen:** applies globally, most load-bearing on S1, the first screen seen.
- **Honest limit:** the effect changes perceived usability and goodwill. It does not change actual error rates, actual task success, or the actual trustworthiness of the underlying data. It is real and replicated, and also modest, and it can backfire as a trust mechanism on its own: a polished interface that is later caught being wrong reads as more deceptive, not less, which loops back to section 2.3. Aesthetics buy the first three seconds. They do not buy the Q&A. Of the eight mechanisms in this section, this is deliberately the least load-bearing.

---

## 3. The colour system

Light theme is the only theme in scope for this build. **Dark theme is explicitly out of scope** (flagged for founder awareness, not yet founder-confirmed). Reasoning: building and verifying two complete themes in a 22-hour build is not achievable without cutting something load-bearing, the target register is better served by one fully considered theme than two half-finished ones, and a rushed dark theme risks landing exactly in the security-theatre register section 1 rules out.

### 3.1 Neutral base

| Token | Hex | Contrast vs. white (or stated pairing) | Usage rule |
|---|---|---|---|
| `color-bg-canvas` | `#FFFFFF` | n/a (base) | Page background, every screen |
| `color-bg-surface` | `#F6F7F8` | n/a | Card and panel backgrounds, one step off canvas |
| `color-bg-recessed` | `#EDEFF1` | n/a | Skeleton loading blocks, disabled field backgrounds, table zebra stripe |
| `color-border-subtle` | `#DEE2E6` | 1.30:1 vs. white (decorative only, not WCAG-governed) | Purely decorative dividers, table row rules. Never used as the sole boundary of an interactive element |
| `color-border-strong` | `#C3C9D0` | 1.67:1 vs. white (decorative only) | Card outer borders on neutral (non-state) cards, section rules |
| `color-border-interactive` | `#6B7280` | 4.83:1 vs. white, 4.51:1 vs. surface (meets WCAG 1.4.11 non-text 3:1) | Input field borders, any border that is itself a meaningful UI boundary, not just a divider |
| `color-text-primary` | `#1A1E24` | 16.73:1 vs. white | Body text, headings, all monetary amounts, all data |
| `color-text-secondary` | `#545B66` | 6.85:1 vs. white, 6.39:1 vs. surface | Secondary text, metadata, timestamps, helper copy |
| `color-text-tertiary` | `#7C8391` | 3.81:1 vs. white | Large text only (19px+/14px+ bold) or icon-only contexts. Never used for body-size paragraph text; it does not clear the 4.5:1 body threshold |
| `color-text-disabled` | `#9AA1AB` | 2.61:1 vs. white | Disabled control labels only. WCAG 1.4.3 exempts inactive components from contrast requirements; this value is a judgement call for baseline legibility, not a compliance claim |

### 3.2 Accent (one, used sparingly)

| Token | Hex | Contrast | Usage rule |
|---|---|---|---|
| `color-accent-600` | `#1D3557` | 12.36:1 vs. white (text/icon use); 12.36:1 for white text on this fill | Primary buttons, links, focus ring, selected-state border, the LIVE indicator dot. This is the only accent hue in the system |
| `color-accent-700` | `#17304F` | 13.36:1 vs. white; 13.36:1 for white text on this fill | Hover/active state of primary buttons only |
| `color-accent-wash` | `#E9EEF4` | text-primary on this wash: 14.34:1; accent-600 on this wash: 10.59:1 | Selected-card background (for example the chosen candidate on S3 after selection), never used as a full-page background |

Discipline rule: the accent appears on primary actions, the focus ring, selection state, and the LIVE dot, and nowhere else. If a build agent reaches for the accent for a fourth kind of thing, stop and use a neutral instead. Sparing use is what keeps it meaningful.

### 3.3 Semantic set: the five field states

Every field state carries three redundant signals: colour, an icon, and a text label. Colour is never the only encoding.

| State | Icon (shape, not colour-dependent) | Strong colour (text/icon/border) | Contrast vs. white | Wash background | Strong-on-wash contrast | Border treatment |
|---|---|---|---|---|---|---|
| SUPPORTED | Filled circle with a small pin/link glyph | `#0E5E68` (teal) | 7.45:1 | `#E4F3F5` | 6.54:1 | Solid 1px |
| CONFLICTED | Triangle with two diverging arrows | `#7A4A00` (amber) | 7.48:1 | `#FBECD1` | 6.42:1 | Solid 2px |
| UNSUPPORTED | Empty/dashed document outline | `#8A1F1A` (crimson) | 9.16:1 | `#F8E0DD` | 7.29:1 | Dashed 2px |
| DECIDED | Filled circle with a checkmark and a small pencil glyph | `#4A3178` (violet) | 10.49:1 | `#EBE4F5` | 8.47:1 | Solid 1px |
| CONFIRMED | Double checkmark inside a filled circle | `#1E6B34` (green) | 6.55:1 | `#E2F1E6` | 5.60:1 | Solid 1px, plus a small seal glyph in the card corner |

All five pass WCAG 2.1 AA (4.5:1) for body-size text and comfortably clear the 3:1 non-text threshold (WCAG 1.4.11) for icon and border use.

Display labels are sentence case, never the raw state token, in the interface: `SUPPORTED` displays as "Supported," `UNDER_REVIEW` displays as "Under review," and so on. The raw tokens from `CANON.md` section 7 (`INGESTED`, `EXTRACTED`, `UNDER_REVIEW`, `SIGNED`, `SEALED` for case state; `SUPPORTED`, `CONFLICTED`, `UNSUPPORTED`, `DECIDED`, `CONFIRMED` for field state) are the exact data vocabulary and must never be renamed in code or API, only humanised on screen.

### 3.4 The four conflict causes: distinguishable without colour alone

`CANON.md` section 6 requires TIMING, CORRECTION, and VERSION (all CONFLICTED) and MISSING (UNSUPPORTED) to look visibly different from each other, not just share one amber treatment. Redundant encoding:

| Cause | Field state | Icon | Label text | Border detail beyond the base state border |
|---|---|---|---|---|
| TIMING | CONFLICTED | Clock/stopwatch glyph | "TIMING · different cut-off" | Plain solid 2px amber border, no additional mark |
| CORRECTION | CONFLICTED | Restated document glyph (an arrow curling back onto a page) | "CORRECTION · restated after cut-off" | Solid 2px amber border plus a small corner ribbon reading "REVISED" |
| VERSION | CONFLICTED | Two stacked, offset document glyphs | "VERSION · records disagree" | Solid 2px amber border plus a doubled inner hairline evoking two overlapping documents |
| MISSING | UNSUPPORTED | Empty/ghost document glyph | "MISSING · no source contains this field" | Dashed 2px crimson border (different hue and different line style, since this is a categorically different state, not just a different cause within CONFLICTED) |

Note: the label text itself spells the cause out in words on every card. Nothing about distinguishing the four causes depends on a viewer's colour perception; a grayscale printout of S1 still reads correctly from icon shape, border style, and label text alone.

### 3.5 Model-plane indicator colours

Reuses existing tokens rather than adding new hues, to keep the palette disciplined:

| Token | Colour | Shape | Usage |
|---|---|---|---|
| LIVE dot | `color-accent-600` | Filled solid dot | The rarest, most reserved colour in the system marks the rarest, most significant claim: this model call actually happened live |
| RECORDED dot | `color-text-secondary` | Hollow/outline dot (same diameter) | Neutral, calm, not an error state. Filled-versus-hollow is the redundant, colour-independent signal |

### 3.6 Contrast summary and the projector-safety note

Every text pairing used anywhere in this system has been computed against the WCAG 2.1 relative-luminance formula, not estimated. All body-text pairings meet or exceed 4.5:1; all large-text and icon/border pairings meet or exceed 3:1, with the two explicitly noted exceptions (`color-text-tertiary`, restricted to large text only, and `color-text-disabled`, exempt under WCAG 1.4.3 as an inactive-component colour).

Conference projectors compress contrast range, wash out under ambient light, and lose black level. Mid-tone greys (roughly the 40 to 60 percent luminance band, where `color-border-subtle` and `color-border-strong` live) are the first casualty; they can visually merge into the surface around them. Rules for this build:

1. Never place a mid-tone grey as the sole differentiator between two states, or between a state and its background. Every place a mid-tone grey is used, it is already backed by icon, label, or position (see section 3.4).
2. Primary text stays true near-black (`color-text-primary`, 16.73:1 measured), not a softened dark grey, specifically because the softened version loses more relative contrast under projector compression than a true near-black does.
3. Test the actual build on the actual projector, or the closest available substitute, before the Friday demo slot, at the room's real ambient light level. No token table substitutes for a live check.
4. Avoid pairing the lightest neutral washes (`color-bg-recessed` and the semantic wash tints) with thin icon strokes or small text; prefer pure white canvas and icon strokes of at least 1.5px effective weight for anything that must read from the back of a conference room.

---

## 4. Typography

No network request, ever. System font stacks only.

| Token | Value | Usage |
|---|---|---|
| `font-family-ui` | `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif` | All interface text: labels, body, headings, buttons |
| `font-family-mono` | `ui-monospace, "SF Mono", "Cascadia Code", "Consolas", "Roboto Mono", monospace` | All monetary amounts, all hashes, all timestamps, prompt IDs |
| `type-numeric-tabular` | `tabular-nums` (applied via the numeric font-variant feature) | Defensive redundancy on every monospace numeric context. True monospace glyphs are already fixed-width, so digits align by construction; this feature flag is a fallback in case any monospace stack entry falls back further to a non-monospace font |

### 4.1 Type scale

| Role | Size (px) | Line height (px) | Weight | Letter spacing | Usage |
|---|---|---|---|---|---|
| Display / case title | 28 | 36 | 600 | -0.01em | Case identifier on S1 only |
| H1 screen title | 22 | 28 | 600 | -0.01em | Top of every screen |
| H2 section title | 17 | 24 | 600 | 0 | Panel and card headers |
| H3 field label | 14 | 20 | 600 | 0.01em | Field names, table column headers |
| Body | 15 | 22 | 400 | 0 | Reading text: descriptions, reasons, source snippets |
| Body small / metadata | 13 | 18 | 400 | 0 | Timestamps, source citations, helper text |
| Caption / eyebrow | 11 | 16 | 600 | 0.06em, uppercase | Status chip labels, the SYNTHETIC tag, section eyebrows |
| Button label | 14 | 20 | 600 | 0.01em | All buttons |
| Mono data | 14 | 20 | 500 | 0 | Amounts, hashes, timestamps inline in body-weight contexts |
| Mono data, dense | 13 | 18 | 500 | 0 | Amounts, hashes, timestamps inside dense tables (S4, S5) |

### 4.2 The tabular-monospace rule, and why it matters more than it looks like it should

Every monetary amount, every hash, and every timestamp is set in `font-family-mono` with tabular figures, full stop. No exceptions, no "just this one summary card." When a compliance officer or a juror scans a column of numbers (`CANON.md`'s own F1 to F3 candidate table is the exact shape: four sources, three of them disagreeing by a fixed number of digits), tabular monospace lets the eye align digit columns and catch a mismatch by pattern alone, the way a real reviewer checks a real statement. Proportional numerals force the eye to re-parse each figure individually, because a "1" and a "7" do not occupy the same width. This single typographic choice does more for perceived rigour than any font weight, size, or colour decision in this document, because it is the one choice that changes what the eye can actually verify, not just how the text looks. It is a direct implementation of the "showing the work" mechanism in section 2.1: alignment is itself a form of shown work.

---

## 5. Spacing, grid, and layout

### 5.1 Base unit and scale

Base unit: 4px.

| Token | Value | Usage |
|---|---|---|
| `space-4xs` | 2px | Hairline gaps: icon to its own label at caption size |
| `space-3xs` | 4px | Tightest internal padding: chip interior |
| `space-2xs` | 8px | Icon-to-text gap, tight inline spacing |
| `space-xs` | 12px | Compact control padding |
| `space-sm` | 16px | Default component padding, form field padding |
| `space-md` | 24px | Card padding, gap between related controls |
| `space-lg` | 32px | Gap between distinct sections within a panel |
| `space-xl` | 48px | Panel and pane padding, gap between major page regions |
| `space-2xl` | 64px | Page-level top margin below the header |
| `space-3xl` | 96px | Reserved. Only the most generous top-level framing, used sparingly if at all |

### 5.2 Radius and elevation

| Token | Value | Usage |
|---|---|---|
| `radius-sharp` | 0px | Table cells, the hash-chain blocks on S7. Sharp corners on the chain reinforce a ledger, not a friendly app |
| `radius-sm` | 4px | Inputs, chips, buttons |
| `radius-md` | 8px | Cards, panels |
| `shadow-overlay` | Y-offset 2px, blur 8px, colour `color-text-primary` at 12 percent opacity | The only shadow in the system. Reserved for elements genuinely floating above the page: the S2 expanded detail drawer, dropdown menus, the S5 disposition panel. Never used on a plain resting card, which is separated by a border, not a shadow |

Judgement: flat, bordered cards over floating shadow cards throughout. A shadow in this system always means "this is temporarily above the document," never "this card looks nicer." That is a deliberate restriction, not an oversight.

### 5.3 Global page structure

Two-tier persistent header on every screen, 96px total:

- Tier 1, 32px: a thin utility strip. Left: the SYNTHETIC disclosure (section 9). Right: case identity and reporting period. This strip is deliberately separated from the product's own navigation chrome, so it reads like a stamped notice on a document rather than a piece of the brand, the same way a real regulatory filing carries a printed disclosure line distinct from its letterhead.
- Tier 2, 64px: left, the product wordmark and case ID; centre or right, the six primary navigation destinations (Dashboard, Evidence, Trace, Risk, Sign-off, Receipt, corresponding to S1, S2, S4, S5, S6, S7); far right, the LIVE/RECORDED indicator when the current screen involves a model call.

S3 (Conflict decision) is deliberately **not** a seventh nav destination. It is a focused decision surface entered by the "Review" action on a CONFLICTED or UNSUPPORTED field card from S1 or S2, presented as a full-width in-place panel (not a small popup dialog, given the weight of its content: two full candidate cards plus a mandatory reason plus a named-decider identity block), and it returns to the originating screen on completion or cancel.

Max content width: 1440px, centred, with side margins that grow past that width. This keeps the product legible on a large projector canvas without the layout stretching into unreadable full-bleed rows.

### 5.4 Per-screen layout proportions

| Screen | Layout in proportion |
|---|---|
| S1 Case dashboard | Single column. Header (96px) + case-state stepper band (56px) + a single row of four field cards filling the remaining width equally (25 percent each on desktop, wrapping to a 2x2 grid only below roughly 900px of available width) |
| S2 Evidence workspace | Two column, 60/40. Left 60 percent: candidate list. Right 40 percent: source document viewer with the highlighted pin, synced to whichever candidate is focused on the left |
| S3 Conflict decision | Full-width in-place panel. Top: shared context line. Middle, roughly 40 percent of panel height: two equal-width candidate cards side by side. Below, roughly 30 percent: mandatory reason field. Bottom, roughly 10 percent, pinned: decider identity and the submit action. Remaining space is breathing room, not compressed |
| S4 Agent trace | Single dense column, no split pane (deliberately different shape from S2, so the two screens are never confused for one another at a glance). LIVE/RECORDED summary band at top, reverse-chronological log rows below, one expandable detail drawer at a time |
| S5 Risk and anomaly board | Single full-width table. Open/undispositioned rows visually lead (sorted first, and carrying the same attention-getting treatment as CONFLICTED elsewhere in the system); each row expands in place to a disposition panel |
| S6 Sign-off | Centred narrow document column, 720px max width, deliberately narrower than every other screen, to read as a formal instrument rather than a dashboard. Case summary at top, two signature blocks stacked below with a visible connecting rule between them |
| S7 Receipt and manifest | Centred document column, 720px max width, matching S6. Hash-chain visualisation as the dominant element, manifest table below it, verify and export actions below that |

### 5.5 Density and grouping

This is a professional instrument: denser than a marketing page, looser than a trading terminal. Concrete numbers: default table row height 44px, dense table row height (S4, S5 only) 36px, card internal padding `space-md` (24px), panel internal padding `space-xl` (48px). Never compress below a 36px row or expand past a 64px row anywhere in the product; both extremes break the "professional instrument" register in opposite directions.

Grouping follows Gestalt principles as a layout judgement, not a cited experimental result specific to this product: common region (a card's border defines the perceptual boundary of everything belonging to one field, per Palmer's 1992 extension of Gestalt grouping) and similarity/connectedness (a candidate card on S2 and its corresponding highlight in the source pane share the same accent treatment when linked, so the eye reads them as one unit even though they sit on opposite sides of the 60/40 split).

Field ordering on S1 is informed by the serial position effect (items in the middle of a sequence are recalled least reliably): fields needing attention are never buried in the middle position of the four-card row if the state changes at runtime causes ordering to matter (in the fixed F1 to F4 demo case, order by field ID and rely on section 3.4's isolation treatment instead; the serial-position argument matters more once field counts grow beyond four).

Note, as a design credit rather than a citation: `CANON.md` fixed the field count at four for narrative reasons, and four sits comfortably at or under Cowan's (2001) more rigorous modern refinement of Miller's (1956) working-memory estimate (roughly four chunks, revising Miller's looser "seven plus or minus two"). That is a genuinely favourable coincidence between the content decision and the psychology, not something this document engineered.

### 5.6 Minimum interactive target sizes

Minimum click and touch target: **44 by 44 CSS pixels**, with a caveat stated precisely: WCAG 2.1, the version this build's contrast claims target, does not itself mandate a minimum target size at the AA level. A 44 by 44px minimum first appears in WCAG as SC 2.5.5 Target Size (Enhanced), which is AAA. WCAG 2.2 later added SC 2.5.8 Target Size (Minimum) at AA, set at 24 by 24px, a lower bar. This build adopts the stricter 44px figure anyway, sourced from the AAA guideline and matching long-standing platform convention (Apple's Human Interface Guidelines and Google's Material Design both specify roughly a 44 to 48px baseline), because of Fitts's Law (Paul Fitts, 1954: movement time to a target is a function of the target's distance and size, formally MT = a + b·log2(2D/W)). Smaller or more distant targets measurably take longer to acquire and are more error-prone, and the decision path (S3) and the sign-off path (S6) are exactly where a mis-click carries real consequence.

| Token | Value | Usage |
|---|---|---|
| `control-height-default` | 44px | Buttons, primary form inputs, nav items, anything on the S3 or S6 critical path |
| `control-height-dense` | 32px visual, with 6px transparent hit-padding on all sides (44px effective) | Row-level icon actions inside S4 and S5's dense tables only |
| Minimum spacing between adjacent independent targets | 8px | Prevents mis-hits between neighbouring controls, a direct consequence of Fitts's Law's distractor-proximity effects |

---

## 6. Motion and timing

Hard rules, non-negotiable: nothing decorative moves. Motion communicates a state change or a causal link, never decoration. One animation runs at a time; a second motion never starts before the first has visibly settled. Every animation in this table has a reduced-motion fallback: when the operating system's reduced-motion preference is set, replace the motion with an immediate state change or, where some transition feedback is still needed, a sub-120ms opacity crossfade with no movement or scale.

### 6.1 Perceptual anchors, stated conservatively

- Under roughly 100ms: perceived as instantaneous, directly caused by the input itself (Miller, 1968; Card, Moran, and Newell, 1983; popularised as Nielsen's "0.1 second" response-time guideline). Used for hover and focus feedback.
- Roughly 100 to 400ms: perceived as a fast, connected response. The Doherty threshold (Doherty and Thompson, 1982, an IBM study) identifies system response at or below roughly 400ms as the ceiling associated with sustained user productivity and flow. Most functional transitions in this product live inside this band.
- Up to roughly 1000ms: still reads as one continuous train of thought without needing a progress indicator, though the user notices the wait (Nielsen's "1.0 second" limit, same lineage). Reserved only for the two deliberately weightier "peak" moments below.
- Beyond 1000ms: needs an explicit progress indicator or it reads as broken. Never used for a UI transition in this build.

### 6.2 Motion table

| Interaction | Duration | Easing | Communicates |
|---|---|---|---|
| Hover / focus state | 100ms | Linear | Direct, instantaneous acknowledgement of pointer or keyboard presence |
| Value proposed and pinned to its source (S2: the highlight moves and the field populates) | 240ms | Ease-out | Causality: this specific span of source text produced this specific value |
| Field state chip change (for example SUPPORTED to DECIDED) | 200ms | Ease-in-out, cross-fade with a subtle 1.0 to 1.02 to 1.0 scale | A state transition occurred; draws the eye once without alarm |
| Abstention appearing (a CONFLICTED or UNSUPPORTED chip entering) | 280ms, a single emphasis pulse (scale 1.0 to 1.04 to 1.0), never looping | Ease-out in, ease-in settle | The von Restorff moment (section 2.6): calls attention exactly once. A looping pulse would be decorative and is explicitly forbidden |
| Decision recorded (S3 submit, button morphs to a confirmation state) | 320ms | Ease-in-out | Causality: your action produced this recorded state. Long enough to read as consequential, short enough to stay inside the Doherty band |
| Seal closing (S7, on successful seal) | 560ms, a single deliberate motion (hash blocks aligning and a lock/seal glyph closing) | Slow-in, fast-settle with a slight overshoot before resting | The peak-end rule (section 2.7) permits this the longest duration of any routine transition in the product, since it is a designed high point, while staying under the 1000ms ceiling so it never reads as sluggish |
| Tamper check breaking (S7, the emotional peak of the demo) | 400ms, sharp onset, no overshoot, no bounce | Ease-in only, a "snap," not a settle | The single most consequential motion in the product. A hash block visibly cracks or misaligns, the chain link snaps open, and the affected block's colour shifts from the CONFIRMED green to the UNSUPPORTED crimson over the duration. Every link after the break also flags unverifiable in the same motion pass, because that is how a hash chain actually behaves, not a stylised approximation of it |

The tamper-break motion must be visibly different in character from the seal-closing motion (sharp versus deliberate, snap versus settle, crimson versus green), or the demo's designed peak loses its distinctness against the moment right before it.

---

## 7. The five states of every data element

Most hackathon products build only the populated state, and that omission alone is what makes them look unfinished under any kind of real use or real scrutiny. Every data element in ATTEST (a field value, a table, a trace list, a manifest entry) is specified in all five states.

| State | Specification |
|---|---|
| **Loading** | A skeleton block matching the exact footprint of the eventual content, in `color-bg-recessed`, with a slow, static opacity pulse (roughly 1200ms cycle) rather than a moving gradient sweep. A sweep-style shimmer was considered and rejected: it reads as consumer-app polish rather than the calm, composed register section 1 sets. This is a judgement, not a cited finding |
| **Empty** | Distinct from both loading and "zero." Always states the reason in plain language; never a blank space. See section 8 for the exact empty-state copy rules |
| **Populated** | The happy path. Never shown as a bare value: every populated data element carries its source citation inline, per section 2.1. This is the state every hackathon product remembers to build, and the one this document spends the least words on for exactly that reason |
| **Error** | Reserved strictly for genuine technical failures: a network call failed, ingest timed out, an API call errored. Never used for CONFLICTED or UNSUPPORTED, which are designed outcomes, not defects (`CANON.md` section 11: "we say abstain, not fail or error"). Rendered as a screen-level, dismissable banner with a retry action, deliberately not as a field-level chip, so it can never be visually confused with an abstention, which is a permanent part of the record and is never dismissable |
| **Abstained** | The union of CONFLICTED and UNSUPPORTED from section 3.3, always paired with its cause tag from section 3.4, a call to action for the human ("Review," "Resolve"), and never a numeric placeholder like "0" or a bare dash that could be mistaken for a real value. This is the direct interface expression of `CANON.md`'s own line: zero is the most dangerous answer in regulatory reporting, because it looks like an answer |

### 7.1 Skeleton and empty-state copy rules

- Skeleton blocks carry no copy at all; they are pure shape, so nothing false is ever displayed while real content loads.
- Empty-state copy always names the reason, never just the absence: "No source document contains this field," not "Nothing here yet."
- Empty-state copy never uses a mascot, an illustration, or humour. It reads like a note on a file, not a 404 page.
- Loading states over roughly 1000ms (see section 6.1) require a discernible, honest indication of progress if one is knowable; if not knowable, the skeleton alone is the honest answer, not a fabricated progress bar.

---

## 8. Microcopy rules and the copy bank

### 8.1 Voice

Precise, plain, never chatty, never apologetic. This interface is a record, not a brand. Rules:

- **Labels:** noun phrases, sentence case, no punctuation. Small eyebrow and status labels are the one exception and use uppercase with the tracked letter-spacing from section 4.1.
- **Buttons:** verb plus object. "Record decision," "Confirm sign-off," "Verify chain." Never a bare "Submit," which is too generic to say what is about to happen, and never an exclamation ("Let's go!"), which is too casual for what is about to happen.
- **Errors:** state what happened and what to do next. No blame, no apology, no exclamation marks anywhere in the product.
- **Empty states:** state the reason, per section 7.1.
- Never say "Sorry" or "Oops." Apology language implies casualness and fallibility that undercut the system-of-record register this entire document is built around.
- Never use first-person marketing voice ("We've got you covered"). The interface reports state; it does not have a personality.

### 8.2 Copy bank

These strings are written to be read aloud on stage. They also match `CANON.md` section 11's vocabulary locks exactly: propose, decide, confirm, seal; abstain, never fail or error; preserved disagreement, never conflict resolution.

**Abstention, CONFLICTED (generic template):**
> "Two sources disagree. [N] candidates found, both evidence-bound. This field needs a named decision."

**Abstention, CONFLICTED (the F2 example, populated with real canon numbers):**
> "Administrator and internal ledger disagree by USD 1,500,000. Both are correct as of their own cut-off. Choose the candidate and record why."

**Abstention, UNSUPPORTED (F4, primary line):**
> "No source document supports this field."

**Abstention, UNSUPPORTED (F4, secondary line):**
> "The system does not guess. A value is entered here only if a person can name where it comes from."

**Mandatory-reason prompt (label above the field):**
> "Reason for this decision"

**Mandatory-reason prompt (placeholder text inside the empty field):**
> "State what you know that the documents alone do not show."

**Mandatory-reason block (attempted submit with an empty reason):**
> "A reason is required before this decision can be recorded."

**Maker-checker block (same identity attempts both roles):**
> "[Name] recorded this decision and cannot also confirm it. A second named reviewer is required."

**Seal confirmation (button label):**
> "Seal case"

**Seal confirmation (result copy):**
> "Sealed. [N] artifacts, [N] transitions, one hash chain. Change one byte and it shows."

**Tamper detected (result copy):**
> "Tamper detected. The hash at [step name] no longer matches. The chain shows exactly where."

---

## 9. The synthetic-data disclosure treatment

This carries direct weight against the honesty criterion in the scoring rubric (`FACT_CARD.md` H3: Honesty and Roadmap Credibility, 20 points), so it is specified as a design requirement here, not left as an afterthought.

- **Placement:** the tier-1 utility strip described in section 5.3, present on every single screen, always visible without scrolling, never confined to a splash screen or a footer a viewer could miss.
- **Weight:** caption/eyebrow scale (11px, uppercase, tracked, `color-text-secondary`, never a semantic colour). Legible, deliberately not shouting: it never uses the UNSUPPORTED crimson or any alarm-style treatment, because a synthetic-data notice is a fact about the demo, not a warning about the product.
- **Exact copy, persistent strip:** "SYNTHETIC DATA · fictional entities only"
- **Exact copy, full form (S1 subtitle area and printed on every export):** "All entities, documents, and figures on this page are synthetic and fictional."
- **Exports and the manifest (S7):** the full-form sentence is printed directly on the exported artifact itself, not only shown in the surrounding app chrome, because an export travels without its screen once it leaves the room.

---

## 10. The LIVE versus RECORDED indicator

The model-plane state (whether a given model call actually happened during this session or is a replayed prior call) is shown wherever a model call is referenced: primarily S4's trace log, and inline wherever S2 attributes a proposed value to a model call.

- **LIVE:** filled solid dot in `color-accent-600`, label "LIVE" in tracked caption case.
- **RECORDED:** hollow/outline dot of the same diameter in `color-text-secondary`, label "RECORDED."
- Filled versus hollow is the redundant, colour-independent signal (section 3.5), so the distinction still reads in grayscale or under projector contrast compression.
- On S4, every row carries one marker or the other. There is no third, silent, unmarked default state.

**Why this is a scoring advantage, not a weakness, stated as a design judgement:** most hackathon demos either quietly present everything as live or never disclose the distinction at all. Disclosing RECORDED honestly is the interface holding itself to the identical evidentiary standard it demands of the fund data it displays: a claim is trustworthy because its provenance is shown, not asserted (section 2.1, applied reflexively to the tool's own model-plane claims). It also converts an honesty claim from something said in the pitch into something a juror can check directly on screen, which is a stronger form of the same claim.

---

## 11. Accessibility floor

The genuinely achievable non-negotiable minimum for a 22-hour build. Everything in this list ships; nothing here is a stretch goal.

- **Semantic structure:** real heading hierarchy matching section 4.1's scale (one `h1` per screen, `h2` for section headers, and so on), real landmark regions (header, nav, main), real interactive elements (`button`, `label`, `table` markup) rather than styled `div`s standing in for them.
- **Keyboard reachability of the decision and sign-off paths:** on S3, tab order must reach candidate selection, the reason field, and the submit control without a mouse. On S6, both signature actions must be reachable the same way. This is the highest-priority accessibility requirement in the document, because it is the money path: the two places a human's name attaches to a legal record.
- **Visible focus:** every focusable element gets a visible focus indicator using `color-accent-600` at a 2px outline with a small offset (12.36:1 contrast, well past the 3:1 non-text minimum). Focus outlines are never removed without a replacement; removing the default outline without one is explicitly forbidden.
- **Contrast compliance:** the verified ratios in section 3, no exceptions beyond the two explicitly noted (tertiary text restricted to large-text use; disabled text exempt under WCAG 1.4.3).
- **No colour-only encoding:** every state anywhere in the product carries icon and label alongside colour, per sections 3.3 and 3.4.
- **Reduced-motion support:** every animation in section 6 has the stated fallback; this is a small, cheap conditional check and there is no excuse to cut it under time pressure.

**Explicitly out of scope for this build**, stated plainly so nobody claims coverage that is not there: full ARIA live-region announcements for every dynamic state change (semantic HTML gives a reasonable baseline; live-region polish is a genuine nice-to-have, not a guarantee here); multi-language or right-to-left support; WCAG AAA as a target (this document targets AA throughout, deliberately, and says so); automated accessibility test tooling such as axe-core (a manual keyboard-and-contrast pass on the S3 and S6 paths is what actually happens in the time available); mobile-specific touch accessibility (this product is built and demonstrated on laptop and projector, not optimised as a mobile experience); and Windows forced-colours or high-contrast-mode testing. These are not being quietly skipped; they are named here so the team can answer an accessibility question from a juror with the true state of coverage rather than a guess.

---

## 12. Screen-by-screen visual brief

For each screen: the layout in words, the visual hierarchy in order, the one element that must dominate, the state changes it renders, and three acceptance checks a human runs to confirm it looks right.

### S1: Case dashboard

**Layout:** fixed header (section 5.3) plus a case-state stepper (`Ingested -> Extracted -> Under review -> Signed -> Sealed`) plus a single row of four field cards for F1 to F4, each showing field name, state chip with cause tag where relevant, current value or the explicit no-value treatment, and one primary action matched to state.

**Visual hierarchy:** 1) the case-state stepper (orients "where are we"), 2) the field-card grid as a whole (the product's core claim: four fields, four states, one glance), 3) individual state chips, the single most important pixels on the screen, 4) values, 5) secondary "view evidence" links.

**Dominant element:** the CONFLICTED and UNSUPPORTED cards, which must visually outweigh any SUPPORTED, DECIDED, or CONFIRMED card in the same row, by design, per the von Restorff mechanism (section 2.6).

**State changes rendered:** each card's chip moves through SUPPORTED or UNSUPPORTED, then CONFLICTED where applicable, then DECIDED, then CONFIRMED; the case-level stepper only advances to SIGNED once every field clears CONFLICTED and UNSUPPORTED, per `CANON.md`'s hard rule 3.

**Acceptance checks:**
1. With F1, F2, F3 conflicted and F4 unsupported, a person standing at the back of the room can name which fields need attention within three seconds, using chip colour, icon, and position alone, without reading body text.
2. All four conflict causes show a distinct icon and label even though three of them share the amber CONFLICTED hue.
3. No field ever displays "0," a blank cell, or a dash as a stand-in value; UNSUPPORTED always shows the explicit no-value treatment with its stated reason.

### S2: Evidence workspace

**Layout:** breadcrumb (Case > Field), then a 60/40 split: left, candidate cards (source doc ID, value, cut-off timestamp, evidence snippet); right, the source document viewer with the pin highlighting the exact region, synced to whichever candidate is focused on the left.

**Visual hierarchy:** 1) the pin or highlight in the source viewer, the screen's entire thesis, 2) the candidate cards, 3) document metadata (issuer, cut-off), 4) breadcrumb chrome.

**Dominant element:** the source-pin highlight itself, rendered in the accent colour so it is the single highest-contrast mark on the screen, consistent with the accent's reserved "look here" role from section 3.2.

**State changes rendered:** selecting a different candidate re-points the highlight using the 240ms "value pinned to source" motion from section 6.2; SUPPORTED fields show exactly one candidate; CONFLICTED fields show two or more, toggleable; UNSUPPORTED fields show an explicit empty-document state on the right pane, not a blank viewer.

**Acceptance checks:**
1. Clicking a candidate card visibly moves the highlight within one motion cycle, never an instant cut, never a second animation firing at the same time.
2. Every value on screen has a visible source citation next to it; there is no path that shows a number without a pin.
3. F4's evidence view reads as "we looked and it is not here," not as a broken or stalled page.

### S3: Conflict decision

**Layout:** shared-context line at top (for example, the administrator's 16:00 cut-off against the 17:42 capital call for F2); two equal-width candidate cards side by side in the middle, neither pre-selected; a mandatory reason field below; a pinned bottom bar with the read-only decider identity and the submit control.

**Visual hierarchy:** 1) the two candidates as one symmetrical unit, their equality is the message, 2) the reason field, weighted almost as heavily as the candidates since it is a hard rule, not a courtesy, 3) decider identity, 4) submit control.

**Dominant element:** the candidate pair as a whole. Neither card carries a "recommended" badge, star, or heavier border; this is a deliberate removal of any nudge toward one answer, per the default-bias and anchoring notes in section 2.2.

**State changes rendered:** selecting a card applies the accent-coloured selected-state border (a UI-interaction signal, not a truth claim, so it never borrows a semantic field-state colour); submit stays disabled until a candidate is selected and the reason is non-empty; on submit, the panel collapses into a compact "Decided" summary using the 320ms decision-recorded motion.

**Acceptance checks:**
1. Attempting to submit with a candidate chosen but an empty reason produces the exact copy-bank mandatory-reason message and does not submit.
2. Neither candidate card carries any visual affordance suggesting it is the "right" one before a human chooses.
3. After recording, the decider's real name is legible on screen, attached to this specific decision, not only stored in a database.

### S4: Agent trace

**Layout:** single dense column. LIVE/RECORDED summary band at top (model ID, call count this session); reverse-chronological log rows below, each row showing timestamp, model ID, prompt hash, latency, and the LIVE/RECORDED dot, all mono-set; clicking a row opens one inline detail drawer.

**Visual hierarchy:** 1) the LIVE/RECORDED badge and summary, the screen's whole reason to exist, 2) the log rows as an even, scannable rhythm, 3) mono metadata within each row, 4) expanded detail on demand.

**Dominant element:** the LIVE/RECORDED marker column, scannable as a vertical strip so a viewer can see at a glance how many calls in the session were live versus recorded.

**State changes rendered:** row expand and collapse, one row open at a time; opening a new row closes whichever was open, per the "one animation at a time" rule.

**Acceptance checks:**
1. Every row shows a visible LIVE or RECORDED marker; there is no silent third default.
2. Prompt hash and latency are both set in the dense mono style so a column of them visually aligns.
3. For any proposed value shown on S1 or S2, the matching trace row that produced it can actually be found, a real round trip, not a decorative log.

### S5: Risk and anomaly board

**Layout:** single full-width table (indicator name, description, severity, disposition chip, assigned reviewer), each row expanding in place to a disposition panel: disposition choice, mandatory note, named reviewer, mirroring S3's pattern.

**Visual hierarchy:** 1) open/undispositioned rows, sorted first and carrying the same attention-getting treatment as CONFLICTED elsewhere, 2) severity marking, 3) closed rows, which recede the way DECIDED and CONFIRMED recede in the semantic palette, 4) table chrome.

**Dominant element:** whichever indicator rows remain open.

**State changes rendered:** a row's disposition chip moves from the "open" amber family to the "closed" green family only once a named reviewer records a disposition and a note.

**Acceptance checks:**
1. No indicator reaches "closed" without a named reviewer and a non-empty note; this is enforced, not merely implied by the copy.
2. Open and closed rows are distinguishable in a grayscale printout, by icon and label, not fill colour alone.
3. Every closed row visibly shows who closed it and when; nothing auto-closes silently.

### S6: Sign-off

**Layout:** centred 720px document column. Case summary at top (fund name, period, the four fields in their final DECIDED state); two signature blocks below, Maker shown read-only once complete, Checker as the active input, blocked with the maker-checker message if the same identity is presented for both.

**Visual hierarchy:** 1) the maker-checker separation itself, the screen's whole thesis, 2) the case summary, what is being attested to, 3) individual field values, 4) chrome.

**Dominant element:** the two signature blocks, visually linked by a connecting rule, making clear these are two separate, required, named acts, not one action with a second click.

**State changes rendered:** the checker block moves from disabled and blocked (with the maker-checker copy-bank message) to active only when a genuinely different identity is present; on confirmation, both blocks lock and timestamp.

**Acceptance checks:**
1. Presenting the same identity for both roles visibly blocks with the exact maker-checker message; it does not simply grey out without explanation.
2. Both names, both roles, and both timestamps are simultaneously visible at the moment of completion, one never replacing the other.
3. The screen reads, to a regulator-minded viewer, like a document they would be willing to sign, not like a web form.

### S7: Receipt and manifest

**Layout:** centred 720px document column, matching S6. Manifest table (artifact, hash, linked state transition) at top; the literal hash-chain visualisation below it (a vertical sequence of linked blocks, one per state transition); a prominent "Verify chain" action; export actions; the full-form synthetic disclosure line printed directly on the document.

**Visual hierarchy:** 1) the hash-chain visualisation, the screen's whole reason to exist, 2) the verify action, 3) the manifest table, 4) export actions, 5) the synthetic disclosure line, present but not shouting, per section 9.

**Dominant element:** the chain itself, and specifically whichever link is broken during a tamper demonstration; this is the emotional peak of the demo (section 2.7) and carries the single most dramatic motion in the product (section 6.2).

**State changes rendered:** sealed (every link solid, CONFIRMED green, a closed seal glyph) transitions to tamper-checked-and-broken (the affected link switches to the UNSUPPORTED crimson break treatment with the 400ms snap motion; every subsequent link in the chain also flags unverifiable in the same pass, matching how a real hash chain actually behaves).

**Acceptance checks:**
1. Before tampering, every link reads as sealed using the CONFIRMED treatment; after tampering, the break is legible from the back of the room in under three seconds, the strictest bar in the product, since this is the money screen.
2. The synthetic disclosure line is present and legible directly on any exported artifact, not only in the live app.
3. The break motion is visibly different in character from every other motion in the product; it must not reuse the seal-closing easing or duration, or the designed peak loses its distinctness.

---

## 13. The build-order shortcut

Ranked, for a few hours of actual visual-design implementation time inside the 22-hour sprint. Be decisive: this order is not a menu.

1. **The five-state semantic colour system with redundant icon and label encoding (section 3.3, 3.4).** Touches every screen, is the literal expression of "status is the product," and is the single highest-leverage visual decision in the document.
2. **Typography scale plus the tabular-monospace rule for all numbers, hashes, and timestamps (section 4).** Cheap: font stacks and a type scale are a handful of custom properties. The perceived-rigour payoff is large relative to the effort.
3. **S1 dashboard and S3 conflict decision, built fully before touching S4 or S5.** S1 sets the three-second first impression; S3 proves the core "no false certainty" thesis. Both are on the demo spine; neither is optional.
4. **The spacing scale and the S2 60/40 layout (section 5).** Establishes the "considered layout" feel that the rest of the product inherits.
5. **S7's seal and tamper-break visualisation (section 6.2, section 12 S7).** This is explicitly the emotional peak of the demo and must not be cut, but it is a single dramatic moment rather than a workhorse screen, so it can be built after the screens used continuously through the demo.
6. **S6 sign-off, the maker-checker block specifically.**
7. **S4 agent trace and S5 risk board.** Real, on the spine, but more supporting evidence than thesis-carrying; simplify these first if time is short (see the cut list below) rather than cutting them entirely.
8. **Full motion pass beyond the two peak moments (seal closing, tamper break).** Every other transition in section 6.2 can degrade to a fast, simple opacity crossfade without violating any rule in this document, since the hard rule is that motion communicates state change, not that motion is required to exist. An absent secondary animation is never a violation. A wrong one is.
9. **The keyboard and focus pass on the S3 and S6 paths specifically (section 11).** Do this before a general accessibility sweep; it is the non-negotiable floor, everything else in section 11 is explicitly lower priority by its own terms.

**What to cut first if time runs out**, in order, and what is never eligible to be cut:

1. Cut first: all non-peak motion. Replace with instant state swaps. Motion was never the trust mechanism in this document; evidence pinning and preserved disagreement are.
2. Cut second: S4's expandable detail drawer. Ship the flat log only.
3. Cut third: S5's per-row inline expansion. Ship a flat table with a single shared disposition dialog instead of per-row panels.
4. Cut fourth: skeleton-loading states on any screen not actually demoed from a cold load. Keep them on S1 and S2, which do load real content live; skip them on screens reached instantly via navigation during the demo.
5. **Never eligible to be cut, regardless of remaining time:** anything in section 11's accessibility floor, the five field-state colours with their redundant encoding, the tabular-monospace rule for numbers, the mandatory-reason enforcement on S3, the maker-checker enforcement on S6, and the SYNTHETIC disclosure on every screen and export. These are not visual polish; they are the product's actual claim, and cutting any of them under time pressure would be cutting the thing being demonstrated, not the demonstration of it.

---

*This document is the visual, typographic, spatial, motion, and copy specification. It does not restate `CANON.md`'s data model, API surface, or state-machine rules beyond what a screen needs to render correctly, and it defers to `CANON.md` on any conflict.*
