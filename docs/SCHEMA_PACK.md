# SCHEMA PACK: the Hour-0 synthetic data plan for KRISEVA ATTEST

Status: DRAFT v1, written 2026-08-19. Owner: founder approves, this is what the Friday build agent generates the fixture corpus from.

Ground truth order: `CANON.md` is the fictional world and wins on any conflict. `FACT_CARD.md` is every number allowed on stage (mostly irrelevant to this document, which deals in synthetic fixture data, not pitch facts). `BUILD_SPEC_v1.md` section 3 already defines the runtime JSON Schemas (Case, Field, SourceDoc, Binding, Conflict, Decision, Signoff, RunRecord, ManifestEntry, EvalItem) that this fixture pack must load into; this document does not redefine those, it feeds them. `BUILD_SPEC_v1.md` section 6 sketches the generation rules and defers the full field-by-field spec to this file by name. This document is that file. `REPO_FIRST_COMMIT_PACK.md` names this file as one of the three pre-event artifacts committed at 14:05 Friday.

This document contains no application source code. JSON Schema blocks, CSV column tables, CLI commands and worked examples are specifications, not code, per the hackathon brief's own pre-build allowance (`04_CLEAN_START_BUILD_KIT.md` section 1). The generator script itself gets written live on Friday, from this document.

---

## 1. Purpose and the Hour-0 contract

**What this document is for.** The official brief permits teams to arrive with synthetic data schemas ready to generate at Hour 0, and explicitly bans arriving with pre-built code (`04_CLEAN_START_BUILD_KIT.md` section 1, quoting brief p.3: "No pre-built repositories allowed. Code must start clean at 2:00 PM on Friday, 21 August. Git commit histories will be audited."). The line this document must not cross: it specifies exactly what to generate, in exactly what shape, so precisely that a coding agent can write the generator script from it in under 45 minutes, but it contains no generator code itself. Field definitions, document templates, the conflict matrix, generation rules stated in English, CSV layouts and a JSON Schema for the output manifest: all permitted pre-event preparation. A `.js` or `.py` file that does the generating: written live, Friday, milestone M1.

**What gets generated, in order.**

1. Load generator config: fixed seed (Section 5), output root path, canon entity constants.
2. Materialize the canon case (`CASE-2026-Q1-MER001`): the four fictional entities, the five physical documents (D1 has two versions, see Section 3), the four fields F1 to F4, every planted value fixed byte-for-byte from `CANON.md` section 5. Never touches the random stream.
3. Write the canon case's four ground-truth `EvalItem` rows (one per field) into the eval label set.
4. Generate the eval-corpus filler cases (Section 6): additional lightweight cases, each with one to two documents and a handful of fields, drawing on the seeded random stream within the parameter bounds in Section 5.
5. Write each filler field's ground-truth `EvalItem` row at the moment it is planted, not inferred afterward.
6. Emit the five CSV artifacts (Section 7): the D2 register itself plus four index/label CSVs.
7. Hash every generated file (SHA-256), assemble `manifest.json` against the schema in Section 9.
8. Print a one-screen summary (counts, seed, total elapsed time) and stop. The generator does not call any model, network endpoint, or AWS service; it is a pure, offline, deterministic file-writer.

**File layout.**

```
fixtures/
  manifest.json                                 <- Section 9 schema
  documents/
    CASE-2026-Q1-MER001/
      D1_administrator_statement_v1_SUPERSEDED.txt
      D1_administrator_statement_v2.txt
      D2_subscription_register.csv
      D3_internal_ledger_export.txt
      D4_custodian_confirmation.txt
    CASE-EVAL-0001/
      ...  (1-2 lightweight document files, same naming convention)
    CASE-EVAL-0002/
      ...
    ...
  csv/
    documents_index.csv
    fields.csv
    bindings.csv
    eval_labels.csv
```

Document file extension follows `BUILD_SPEC_v1.md` section 3.3's own `SourceDoc.storageUri` example (`s3://<BUCKET_NAME>/<caseId>/<sourceDocId>.txt`): every document generated as structured plain text, including the ones styled to look like a PDF statement or an XLSX export, is written as `.txt`. Only D2, which is genuinely a flat register, is written as real `.csv`. This local `fixtures/` tree is what M2's AWS step syncs into the S3 bucket named in `AWS_RUNBOOK.md` (`kriseva-attest-manifests-<EVENT_ACCOUNT_ID>`), key-for-key: local `documents/<caseId>/<file>` becomes `s3://<BUCKET_NAME>/<caseId>/<sourceDocId>.txt`.

**The target.** Fixture pack complete, hashed, manifested and passing every check in Section 10, within 45 minutes of the sprint start (14:00 to 14:45 Friday), inside milestone M1 (`04_CLEAN_START_BUILD_KIT.md` section 6). This is the single number that makes this document's level of detail worth the pre-event hours: a generator that a coding agent has to design from scratch on the day does not finish in 45 minutes; one it transcribes from a spec this explicit does.

**The legality note, stated once here so nobody has to re-argue it mid-sprint.** The brief instructs teams to arrive with synthetic data schemas ready to generate at Hour 0 (`04_CLEAN_START_BUILD_KIT.md` section 1). This document is that schema, plus the generation rules, plus the CSV layouts, plus the eval label format: all specification, expressed in English and JSON Schema. No JavaScript, Python, HTML or CSS function or file lives anywhere in this document. The generator that reads this spec and produces `fixtures/` is written after 14:00 Friday, inside the fresh, empty, audited repository, same as every other line of application code.

---

## 2. The reported-field definitions

Four fields, exactly as fixed in `CANON.md` section 3. No fifth canon field. (The eval corpus is allowed to invent additional field codes beyond F1 to F4 for scoring variety, per `BUILD_SPEC_v1.md` section 3.2's own `fieldCode` note; see Section 6.)

| | F1 | F2 | F3 | F4 |
|---|---|---|---|---|
| **Field id** | F1 | F2 | F3 | F4 |
| **Human label** | Committed capital | Drawn capital | Closing NAV | Complaints closed during the quarter |
| **Data type** | Integer | Integer | Integer | Integer |
| **Unit** | USD | USD | USD | COUNT |
| **Currency** | USD | USD | USD | not applicable |
| **Valid range (generation bound)** | hypothesis: USD 500,000 to USD 250,000,000 per case | hypothesis: 0 to that case's committed-capital value (drawn cannot structurally exceed committed); filler "called percentage" sampled hypothesis 15% to 70% | hypothesis: for filler rows, 70% to 160% of that case's drawn capital, to stay plausible net of fees and unrealised gains | hypothesis: 0 to 25, for the minority of filler cases where this field is deliberately made SUPPORTED |
| **Precision / rounding** | Whole USD, no cents | Whole USD, no cents | Whole USD, no cents | Whole integer count |
| **Derivable from other fields?** | No | No | No | No |
| **Why not derivable** | Independently sourced per document; the arithmetic relationship in `CANON.md` section 5 (called percentage, NAV above drawn capital) is a plausibility constraint the generator must respect, not a formula that computes one field from another | same | same | same |
| **Designed outcome state (canon case)** | CONFLICTED, cause VERSION | CONFLICTED, cause TIMING | CONFLICTED, cause CORRECTION | UNSUPPORTED, zero candidates |
| **IFSCA-return context, plain English** | The total capital LPs have contractually committed to the scheme as of the reporting date; one of the primary quantum figures a fund management entity reports each quarter | Cumulative capital actually called down from LPs and received by the scheme as of the reporting date; the figure that shows how much of the committed pool is actually at work | The scheme's net asset value as struck by the fund administrator as of quarter end, after any restatement; the figure LPs and the regulator use to judge scheme performance and size | Count of investor or client complaints the FME closed during the reporting quarter; an investor-protection field, not a capital or valuation field |

Two notes that apply to all four rows. First, "valid range" above governs the generator's random stream for filler rows only; the four canon anchor values (Section 5 of `CANON.md`) are fixed constants written byte-identically every run regardless of any range or seed. Second, the IFSCA-return context descriptions are deliberately generic. `FACT_CARD.md` carries no verified citation to an exact IFSCA quarterly-return form, schedule or annexure number, so this document does not invent one. If a juror asks which exact form field this maps to, the honest answer is that this demo does not claim to reproduce IFSCA's actual form layout, only the reporting concept.

Currency choice (USD throughout) follows `CANON.md` section 12, item C3: the founder's own stated default, "USD. GIFT IFSC funds are USD denominated and it reads as domain fluency." Nothing to decide here; it is already settled.

---

## 3. The four source-document templates

Design rule stated once, up front: the four documents use four visibly different shapes on purpose. A generator that emits four documents with the same layout and just swaps the numbers teaches an extractor nothing about reading real, inconsistent paperwork, and it looks exactly like what it is on stage. D1 is a multi-page, multi-section administrator statement. D2 is a flat CSV register, one row per LP. D3 is a multi-tab spreadsheet-style export. D4 is a one-page formal confirmation letter, mostly prose, with one small table. All four render as structured plain text (`BUILD_SPEC_v1.md` section 3, source regions are addressed as page plus character-offset span into extracted text, not PDF bounding boxes; there is no scanned-image layer anywhere in this build).

**Important file-count note for the acceptance checklist:** the canon case ships **five** physical document files, not four, because D1 exists in two versions (`CANON.md` section 4's own trap). "Four source documents" means four document slots, D1 to D4. D1 version 1 (superseded) must still be materialized as a real file, because `BUILD_SPEC_v1.md` section 3.3's `supersedesDocId` field has to point at an actual prior `SourceDoc` record, not a conceptual one. A generator that only ever writes D1 v2 silently breaks the evidentiary trail behind the CORRECTION conflict.

### D1: Quarterly administrator statement (version 1, superseded, and version 2, current)

| | |
|---|---|
| Issuer | Northwind Fund Services (IFSC) Private Limited |
| Document title (as printed) | "Meridian Alpha Opportunities Fund I, Quarterly Scheme Statement, Quarter Ended 30 June 2026" |
| File format generated | PDF-like structured text (`.txt`), letterhead-and-sections layout |
| Version 1 | Issued 03 Jul 2026. Pre-restatement NAV. This is the version D3 was internally built from |
| Version 2 | Reissued 08 Jul 2026, `supersedesDocId` pointing at v1's `sourceDocId`. Post-restatement NAV. This is "D1" as referenced everywhere else in the canon materials |
| Cut-off (both versions) | Data as at 30 Jun 2026, 16:00 IST |
| Page/section structure | Page 1: letterhead and statement header (issuer, scheme, quarter, "as at" timestamp, version stamp, reissue note on v2 only). Pages 1 to 2: Section A, Capital Account Summary. Pages 2 to 3: Section B, Net Asset Value Statement. Page 3: Section C, Notes to this Statement (carries the plain-language restatement disclosure on v2 only). Page 4: signature block and footer |
| Fields carried, with printed label | "Total Committed Capital (USD)" -> F1. "Cumulative Capital Drawn (USD)" -> F2, printed with "Cut-off: 30 Jun 2026, 16:00 IST" directly beside it. "Closing Net Asset Value (USD)" -> F3 |
| Header metadata | Issuer: Northwind Fund Services (IFSC) Private Limited. Statement as at: 30 Jun 2026, 16:00 IST. Version: 1 or 2. v2 only: "This statement supersedes the version issued 03 Jul 2026." Page count: 4 (hypothesis, a short statement). Document reference: synthetic id, e.g. `NWD/MER001/2026Q1/V2` |
| Signatory | Anita Deshmukh, Client Services Manager, Northwind Fund Services (IFSC) Private Limited |

Labelled example block, version 2, using only CANON numbers:

```
NORTHWIND FUND SERVICES (IFSC) PRIVATE LIMITED
Quarterly Scheme Statement
Meridian Alpha Opportunities Fund I | Quarter Ended 30 June 2026
Data as at: 30 Jun 2026, 16:00 IST | Version: 2 (this version issued 08 Jul 2026,
supersedes version 1 issued 03 Jul 2026)
Document ref: NWD/MER001/2026Q1/V2

SECTION A: CAPITAL ACCOUNT SUMMARY
  Total Committed Capital (USD) ............................ 42,500,000
  Cumulative Capital Drawn (USD) ............................ 17,800,000
     Cut-off: 30 Jun 2026, 16:00 IST

SECTION B: NET ASSET VALUE STATEMENT
  Closing Net Asset Value (USD) ............................. 21,940,500

SECTION C: NOTES TO THIS STATEMENT
  This statement supersedes the version issued 03 Jul 2026. The valuation
  of one unlisted holding has been restated in this version.

Prepared by: Anita Deshmukh, Client Services Manager, Northwind Fund
Services (IFSC) Private Limited.               Page 4 of 4
SYNTHETIC DOCUMENT. No real entity, fund or person.
```

### D2: Subscription register extract

| | |
|---|---|
| Issuer | Meridian Alpha Capital IFSC Private Limited (internal, investor-relations record) |
| Document title | "Subscription Register Extract, Meridian Alpha Opportunities Fund I, As at 30 June 2026" |
| File format generated | Genuine CSV, one row per LP commitment, no totals row (the total is a sum the reader, human or model, must compute; the register itself never states it) |
| Cut-off | As at 30 Jun 2026 |
| Structure | Header row plus four LP rows |
| Columns | `lpId, lpName, commitmentAmountUsd, subscriptionAgreementStatus, subscriptionDate, counterExecutionDate` |
| Fields carried | F1 only, as the sum of `commitmentAmountUsd` across all four rows |
| Header metadata | Issuer, "as at" date, and a comment line marking the file synthetic, since a raw CSV has no letterhead |
| The trap | LP-04's `subscriptionAgreementStatus` is "Signed - Not Counter-Executed" and its `counterExecutionDate` is blank. The register counts it anyway; the administrator and the ledger do not |

Labelled example, using CANON's stated totals (45,000,000 register total; 42,500,000 administrator/ledger total; the 2,500,000 gap is exactly LP-04, per `CANON.md` section 5's "the 2.5m gap on F1 is one LP commitment"). The per-LP split among LP-01 to LP-03 is a hypothesis, illustrative only; only the fund-level totals and the fact that LP-04 is the disputed one are canon:

```
# SYNTHETIC DOCUMENT. No real entity, fund or person.
# Meridian Alpha Capital IFSC Private Limited, internal, as at 30 Jun 2026
lpId,lpName,commitmentAmountUsd,subscriptionAgreementStatus,subscriptionDate,counterExecutionDate
LP-01,Investor One (synthetic),20000000,Countersigned,2025-11-04,2025-11-18
LP-02,Investor Two (synthetic),15000000,Countersigned,2025-11-06,2025-11-20
LP-03,Investor Three (synthetic),7500000,Countersigned,2026-01-15,2026-01-29
LP-04,Investor Four (synthetic),2500000,Signed - Not Counter-Executed,2026-06-22,
```

(20,000,000 + 15,000,000 + 7,500,000 = 42,500,000, matching D1/D3. Adding LP-04's 2,500,000 gives the register's 45,000,000. Both figures are exact CANON section 5 anchors; only the row-level split of the 42,500,000 is illustrative.)

### D3: Internal ledger export

| | |
|---|---|
| Issuer | Meridian Alpha Capital IFSC Private Limited (internal, ledger system) |
| Document title | "Internal Ledger Export, Capital and NAV, Meridian Alpha Opportunities Fund I, As at 30 June 2026, 23:59 IST" |
| File format generated | XLSX-style structured text (`.txt`): three named tabs rendered as labelled sections, each with its own column header row, simulating a spreadsheet export copy-pasted into a text extract |
| Cut-off | As at 30 Jun 2026, 23:59 IST (the latest cut-off of any of the four documents; this is what lets it catch the late capital call) |
| Structure | Tab 1, "Capital Summary" (one summary block: committed capital, drawn capital). Tab 2, "NAV Roll-Forward" (opening NAV, movements, closing NAV, pre-restatement because this export was built from D1 version 1). Tab 3, "Cash Ledger" (dated cash transaction rows, including the late capital call) |
| Fields carried | F1 (42,500,000, matches D1 v2/D3 view of committed capital), F2 (19,300,000, includes the late call), F3 (22,415,000, pre-restatement) |
| Header metadata | Issuer, "as at" timestamp, and critically: **no version stamp of any kind**. Nothing in D3 announces that it was compiled before the 08 Jul restatement. That silence is itself the CORRECTION trap; the absence of a marker is the marker |
| The trap | Tab 3's cash ledger carries a capital-call line timestamped 30 Jun 2026, 17:42 IST, for USD 1,500,000, which lands after D1/D4's 16:00 IST cut-off |

Labelled example, using CANON numbers exactly (17,800,000 + 1,500,000 = 19,300,000; 21,940,500 + 474,500 = 22,415,000, the exact pre-restatement gap CANON states):

```
MERIDIAN ALPHA CAPITAL IFSC PRIVATE LIMITED - INTERNAL LEDGER EXPORT
Meridian Alpha Opportunities Fund I | As at: 30 Jun 2026, 23:59 IST
SYNTHETIC DOCUMENT. No real entity, fund or person.

[TAB 1: CAPITAL SUMMARY]
metric,valueUsd
Committed Capital,42500000
Cumulative Drawn Capital,19300000

[TAB 2: NAV ROLL-FORWARD]
lineItem,valueUsd
Opening NAV (01 Apr 2026),20512000
Net Movements for Quarter,1903000
Closing NAV,22415000

[TAB 3: CASH LEDGER]
transactionDate,transactionTime,description,amountUsd
2026-05-14,10:03:00+05:30,Capital call tranche 3,3400000
2026-06-30,17:42:00+05:30,Capital call tranche 4 (late booking),1500000
2026-06-30,18:05:00+05:30,Management fee accrual,-212000
```

(Tab 2's opening NAV and quarter movement figures are illustrative filler, hypothesis, chosen only so the roll-forward arithmetic is internally consistent; the closing figure of 22,415,000 is the exact CANON anchor.)

### D4: Custodian holdings and cash confirmation

| | |
|---|---|
| Issuer | Sentinel Custody Services, IFSC Branch |
| Document title | "Custodian Cash and Holdings Confirmation, Meridian Alpha Opportunities Fund I, As at 30 June 2026, 16:00 IST" |
| File format generated | PDF-like structured text (`.txt`), but a **one-page confirmation letter**, not a multi-section statement: mostly prose, addressed, signed, with one small table. Deliberately the shortest and least tabular of the four documents, so it does not read as "D1 again with a different logo" |
| Cut-off | As at 30 Jun 2026, 16:00 IST (same cut-off as D1) |
| Structure | Salutation and addressee block. One confirmation paragraph, prose, not a table. A small "Holdings and Cash Schedule" table. Signature block |
| Fields carried | F2, cash only (17,800,000). No F1, no F3: a custodian confirms cash and holdings, not commitments or NAV |
| Header metadata | Issuer, "as at" timestamp, page count 1, document reference (synthetic id) |
| Signatory | "Authorised Signatory, Sentinel Custody Services, IFSC Branch." No invented personal name: `CANON.md` section 2's persona table names exactly three people (Priya, Rajiv, Anita), and this document does not add a fourth |

Labelled example, using the CANON cash figure exactly:

```
SENTINEL CUSTODY SERVICES, IFSC BRANCH
As at: 30 Jun 2026, 16:00 IST | Ref: SEN/MER001/2026Q1/C1
SYNTHETIC DOCUMENT. No real entity, fund or person.

Attn: Priya Ramanathan, Compliance Officer
Meridian Alpha Capital IFSC Private Limited

We confirm that, as custodian to Meridian Alpha Opportunities Fund I, the
cash and holdings positions recorded in our books as at the date above are
as follows.

HOLDINGS AND CASH SCHEDULE
  Cash and Cash Equivalents Held (USD) ...................... 17,800,000

This confirmation is provided as at the date stated above and does not
reflect any transaction after that time.

Authorised Signatory
Sentinel Custody Services, IFSC Branch                    Page 1 of 1
```

---

## 4. The planted-conflict matrix

Expanded from `CANON.md` section 6 into a build table. Conflict ids follow the field they attach to; F4's row is deliberately **not** prefixed `CONF-`, because `BUILD_SPEC_v1.md` section 3.5 already establishes an architectural rule this document must not contradict: MISSING is not a `Conflict` cause. A field with zero candidates goes straight to `UNSUPPORTED` with no `Conflict` record at all. Calling F4's row `ABSENCE-F4` instead of `CONF-F4` keeps that distinction visible at the id level, not just in prose.

| Conflict id | Cause | Field | Documents that disagree | Value A | Value B | Why both are legitimate | Detectable via | What the system must display |
|---|---|---|---|---|---|---|---|---|
| CONF-F1 | VERSION | F1 | D2 (register) vs. D1 v2 and D3 | D2: USD 45,000,000 | D1/D3: USD 42,500,000 | The register counts a subscription that is signed but not yet counter-executed (LP-04); the administrator and the ledger both count only counter-executed subscriptions | LP-04's row in D2 shows status "Signed - Not Counter-Executed" with a blank counter-execution date; D1 and D3 carry no line item for it at all | Both candidate values, each tagged with its source document and, for D2, the exact LP row that explains the gap. No default selection |
| CONF-F2 | TIMING | F2 | D1 v2 and D4 (cut off 16:00 IST) vs. D3 (cut off 23:59 IST) | D1/D4: USD 17,800,000 | D3: USD 19,300,000 | The administrator and custodian both cut off at 16:00 IST; a USD 1,500,000 capital call landed at 17:42 IST, after that cut-off but the same calendar day, and only the internal ledger (23:59 IST cut-off) captured it | The 17:42 IST timestamp on the capital-call line in D3's Cash Ledger tab, versus the explicit "16:00 IST" cut-off printed on D1 and D4 | Both candidate values, each with its own cut-off timestamp shown side by side |
| CONF-F3 | CORRECTION | F3 | D1 v2 (restated) vs. D3 (built from D1 v1) | D1 v2: USD 21,940,500 | D3: USD 22,415,000 | The administrator restated an unlisted holding on 8 July; D1 v2 reflects it, D3 was compiled before the restatement and carries no marker that it is now stale | D1's own header states "Version 2, this version issued 08 Jul 2026, supersedes version 1 issued 03 Jul 2026"; D3 carries no version stamp at all, and that absence is itself the tell | Both candidate values, plus a visible flag that D1 is version 2 and D3 predates the correction |
| ABSENCE-F4 | MISSING | F4 | None. All four documents checked | no candidate | no candidate | No source document in the return package contains a complaints-closed figure at all; this is an absence, not a disagreement between two values | Absence of any F4-labelled field across all four documents' extracted text, confirmed by checking D1 through D4 | An explicit "not found in any source, sources checked: D1, D2, D3, D4" state, zero candidates, never a default of zero |

Why all four causes must render visibly differently, stated from the data side (the visual treatment itself is `UX_PSYCHOLOGY_SPEC.md`'s job, not this document's): the entire pitch claim is that ATTEST preserves disagreement instead of quietly resolving it. That claim only survives contact with a skeptical judge if the four planted situations are actually four different situations a person can independently verify from the raw documents, not one trick copied four times with the labels swapped. If a generator plants "value X vs value Y" with no distinguishing timestamp, version stamp, or genuine absence behind each one, the underlying extraction task becomes trivially guessable and stops testing anything. Concretely: CONF-F1 is detectable by a status column, CONF-F2 by a timestamp comparison, CONF-F3 by a version-stamp comparison (including a version stamp's absence), and ABSENCE-F4 by checking every document and finding nothing. Four different detection mechanisms, not four coats of paint on one mechanism.

---

## 5. Faker-style generation rules

Rules stated in English, then a parameter table. No code.

**Rule zero, above all others: the canon case never touches the random stream.** Every entity name, document value, timestamp and version marker in the canon case (`CASE-2026-Q1-MER001`, documents D1 to D4, fields F1 to F4) is a hardcoded constant in the generator, copied directly from `CANON.md` section 5. It must come out byte-identical on every run, regardless of seed, regardless of code changes elsewhere in the generator. Only the eval-corpus filler cases (Section 6) consume the seeded random stream.

**Deterministic seeding.** The generator takes one fixed seed value, checked into its own config (a suggested example: `20260821`, the sprint start date; any fixed constant works, the only rule is that it never changes once fixtures have been demoed or recorded). The same seed plus the same generator version must reproduce the entire fixture set, canon case plus filler corpus, byte-for-byte identical, every run, on either laptop. This matters for a judged demo for three concrete reasons: Thursday's rehearsal, Friday's live build, and the `ReplayProvider`'s recorded fixtures (`BUILD_SPEC_v1.md` section 9) all have to agree with each other, or a judge who asks "run it again" during Q&A could get a dashboard that no longer matches the screen recording or the rehearsed script. A generator whose output drifts between runs is the opposite of what this company is pitching.

**Entity name generation, constrained to CANON.** The canon roster (Meridian Alpha Capital IFSC Private Limited, Meridian Alpha Opportunities Fund I, Northwind Fund Services (IFSC) Private Limited, Sentinel Custody Services IFSC Branch, Priya Ramanathan, Rajiv Menon, Anita Deshmukh) is closed. Nothing else in the corpus invents a new fictional company, fund, administrator, custodian or named person. The eval-corpus filler cases (Section 6) reuse this exact same roster, styled as additional synthetic reporting periods for the same entities, rather than inventing new company universes. Filler LP rows beyond LP-04 use a numbered code (`LP-05`, `LP-06`, ...), never a new invented company name, since a numbered code is an identifier, not a fictional entity. This keeps every filler case fully inside the "use only entities from CANON.md" guardrail without needing a founder decision. A second **scheme** name (as opposed to a second reporting period for the existing scheme) is a different kind of change and is flagged in "Open founder decisions" at the end of this document.

**Date generation inside the quarter.** The canon reporting quarter is 1 Apr 2026 to 30 Jun 2026 (Q1 FY2026-27, per `CANON.md` section 1). Every transaction-level date inside a case's documents falls within that case's own reporting quarter, except: the administrator's reissue timestamp for a CORRECTION-cause case, which lands deliberately just after quarter end (matching CANON's own 03 Jul issued, 08 Jul reissued pattern), and the 21-days-after-quarter-end return-due date, which is contextual information only and never itself a generated field value. Filler cases get their own quarter windows; the generator does not need to pin a specific calendar quarter for each one; sequential, plausible reporting periods are an implementation detail for Friday, not a fact this document needs to assert.

**Amount generation, canon anchors fixed, filler varies.** The eight canon numbers (F1: 42,500,000 / 45,000,000 / 42,500,000; F2: 17,800,000 / 19,300,000 / 17,800,000; F3: 21,940,500 / 22,415,000; plus the three gap amounts 2,500,000, 1,500,000, 474,500) are written as literal constants, never sampled, never rounded, never reformatted in a way that changes the parsed value. Filler amounts (LP-level breakdowns that must sum to a fixed total, other cash-ledger lines, other holdings) are sampled under the fixed seed within the ranges in Section 2's field table.

**LP and investor row counts.** Canon D2: four rows, fixed, matching `CANON.md` section 5's own "the fourth LP" framing exactly. Filler register-style documents: hypothesis, three to six rows.

**Realistic noise.** See the parameter table below. The governing rule: noise may vary formatting, never the underlying parsed value, and noise never touches a canon anchor value or its printed label, since the four canon conflicts must extract cleanly and reliably for the live demo to work the same way every rehearsal.

**The rule that the four canon conflicts are planted deterministically, never randomised.** Restated for emphasis because it is the single most important rule in this section: CONF-F1, CONF-F2, CONF-F3 and ABSENCE-F4 in the canon case are hardcoded, not the output of "pick a random cause for this field." The eval corpus (Section 6) is where causes get assigned per field, and even there, each planted conflict draws only from the three legitimate causes (TIMING, CORRECTION, VERSION) or the MISSING pattern, never a fifth invented cause.

### Parameter table

| Parameter | Value | Type | Notes |
|---|---|---|---|
| Seed | example: `20260821` | fixed constant | Never changes after fixtures are demoed or recorded |
| Canon cases | 1 | fixed, sourced (`CANON.md`) | `CASE-2026-Q1-MER001` |
| Canon documents (physical files) | 5 | fixed, sourced (`CANON.md` section 4, D1 v1 and v2) | Represents 4 document slots, D1-D4 |
| Canon fields | 4 | fixed, sourced (`CANON.md` section 3) | F1-F4 |
| Canon D2 LP rows | 4 | fixed, sourced (`CANON.md` section 5, "the fourth LP") | LP-01 to LP-04 |
| Filler eval cases | 20 | hypothesis, design choice | Inside `BUILD_SPEC_v1.md` section 6's sourced range of 15 to 25 |
| Fields per filler case | 2 to 4, average 3 | hypothesis | Keeps generation cheap; "a handful of fields" per `BUILD_SPEC_v1.md` section 6 |
| Documents per filler case | 1 to 2 | hypothesis | Filler documents reuse the D1/D2/D3/D4 renderer that matches whichever archetype the field is styled as coming from |
| Filler LP rows (where applicable) | 3 to 6 | hypothesis | |
| Total eval items, target band | 50 to 100 | sourced (`04_CLEAN_START_BUILD_KIT.md` section 5; `BUILD_SPEC_v1.md` section 6) | |
| Total eval items, planned actual | approx. 65 | hypothesis, design choice, worked in Section 6 | Comfortably inside the sourced band |
| Monetary precision | whole USD integers, no cents | sourced (`BUILD_SPEC_v1.md` section 6) | Every canon number is already round |
| Timestamp format | ISO 8601 with explicit offset, e.g. `+05:30` for IST | sourced (`BUILD_SPEC_v1.md` section 6, matches CANON's own "17:42 IST" style) | |
| Thousands-separator style | 70% comma-separated, 20% plain digits, 10% spelled unit ("42.5 million") | hypothesis | Spelled form always states the unit word; never bare "42.5" |
| Currency prefix style | "USD" prefix majority, "$" symbol in a minority of filler-only documents | hypothesis | Canon case stays 100% "USD" prefix throughout, matching `CANON.md` section 12 item C3 |
| Simulated scan noise | applied to 15% of filler documents only | hypothesis | Never applied to any of the five canon documents; text-level only (a header comment plus a few stray character substitutions in non-critical prose), consistent with `BUILD_SPEC_v1.md` section 3's decision that fixtures are structured plain text, not rendered images |
| Layout jitter (line wraps, blank lines) | filler documents only | hypothesis | The five canon documents render in one fixed layout, unchanged run to run |

---

## 6. Volume and scale plan

| | Count | Basis |
|---|---|---|
| Canon case | 1 | sourced |
| Canon documents | 5 physical files across 4 slots | sourced |
| Canon fields / eval items | 4 | sourced |
| Filler eval cases | 20 | hypothesis, inside sourced 15-25 range |
| Filler documents | approx. 30 (1-2 per filler case) | hypothesis |
| Filler eval items | approx. 60 (20 cases x 3 fields average) | hypothesis |
| **Total eval items** | **approx. 64** | canon 4 + filler ~60, inside the sourced 50-100 band with headroom |
| **Total documents in corpus** | **approx. 35** | 5 canon + approx. 30 filler |

**Demo set versus eval set.** The demo set is the canon case alone: one case, five files, four fields, the only thing ever shown live on stage, in the recorded backup, or walked through in rehearsal. Its numbers are memorised (`FACT_CARD.md` and `CANON.md` section 5) and never regenerate differently. The eval set is the demo set's four ground-truth rows plus all filler-case rows, approximately 64 items total, used exclusively by `GET /eval/run` to produce the scoring table (`BUILD_SPEC_v1.md` section 7). No individual filler case is ever named or shown on a slide; they exist only to give the harness enough sample size to make the seven eval metrics statistically meaningful rather than a coin flip on four items.

**Scale-up path, if there is spare time.** In priority order, and each one reversible without touching the canon case:

1. Grow the filler corpus toward the top of the 50-100 band (from approx. 64 items toward approx. 95), by adding more filler cases under the same entity roster. Pure volume, no new design decisions.
2. Add a second reporting quarter's worth of filler cases for the existing scheme (still Meridian Alpha Opportunities Fund I), which is what `BUILD_SPEC_v1.md`'s own ranked cut list gestures at when it names "a second document type in the eval corpus" as the first thing to cut under time pressure; scaling up means doing more of exactly what is already being cut down to, not inventing a new axis.
3. A second scheme under the same FME (Meridian Alpha Capital IFSC Private Limited running a second fund). This is a genuine scope increase, since it requires a new scheme name that does not currently exist in `CANON.md`. See "Open founder decisions" below before building this one.

This order matches `BUILD_SPEC_v1.md`'s own ranked cut list in reverse: the last thing that document says to cut under time pressure ("the second document type in the eval corpus") is the first thing worth restoring if time is available, and a second scheme is explicitly the most expensive, most CANON-touching option, so it sits last.

---

## 7. CSV column specifications

Five CSV artifacts. Column headers use the same camelCase property names as the JSON Schemas in `BUILD_SPEC_v1.md` section 3, so a row loads directly into the matching object shape with no rename step.

### 7.1 `documents/CASE-2026-Q1-MER001/D2_subscription_register.csv` (the D2 source document itself)

| Column | Type | Notes |
|---|---|---|
| `lpId` | string | `LP-01`, `LP-02`, ... |
| `lpName` | string | Synthetic placeholder name, e.g. "Investor One (synthetic)" |
| `commitmentAmountUsd` | integer | Whole USD |
| `subscriptionAgreementStatus` | string, enum: `Countersigned`, `Signed - Not Counter-Executed` | LP-04 in the canon case is the latter |
| `subscriptionDate` | date (`YYYY-MM-DD`) | |
| `counterExecutionDate` | date (`YYYY-MM-DD`) or empty | Empty exactly when status is "Signed - Not Counter-Executed" |

Filler register-style documents reuse this exact column set.

### 7.2 `csv/documents_index.csv`

| Column | Type | Notes |
|---|---|---|
| `sourceDocId` | string | e.g. `DOC-D1V2-8f2a`, matching `BUILD_SPEC_v1.md` section 3's own id-style example |
| `caseId` | string | |
| `docCode` | string | `D1`-`D4` |
| `version` | integer | 1 or 2 for D1, 1 for D2-D4 |
| `supersedesDocId` | string or empty | Set only on D1 v2 |
| `docFormat` | string, enum: `PDF_TEXT`, `CSV`, `XLSX_TEXT` | |
| `issuer` | string | |
| `title` | string | |
| `cutoffAt` | ISO 8601 datetime with offset | |
| `issuedAt` | ISO 8601 datetime with offset | |
| `filePath` | string | Relative to `fixtures/` |
| `pageOrTabCount` | integer | Pages for `PDF_TEXT`, tabs for `XLSX_TEXT`, 1 for `CSV` |
| `sha256` | string, 64 hex chars | |
| `syntheticLabel` | string, constant `SYNTHETIC` | Present on every row, no exceptions |

### 7.3 `csv/fields.csv`

| Column | Type | Notes |
|---|---|---|
| `fieldId` | string | Pattern `FIELD-<CASEID>-F<n>`, matching `BUILD_SPEC_v1.md` section 3.2 |
| `caseId` | string | |
| `fieldCode` | string | `F1`-`F4` for canon; free string for filler |
| `label` | string | |
| `unit` | string, enum: `USD`, `COUNT` | |
| `groundTruthState` | string, enum: `SUPPORTED`, `CONFLICTED`, `UNSUPPORTED` | |
| `groundTruthValue` | number or empty | Empty exactly when `groundTruthState` is `UNSUPPORTED` |
| `conflictId` | string or empty | e.g. `CONF-F1`; empty for `SUPPORTED`/`UNSUPPORTED` |
| `conflictCause` | string, enum: `TIMING`, `CORRECTION`, `VERSION`, or empty | Empty for `SUPPORTED`/`UNSUPPORTED`; never `MISSING` here, see Section 4's note |

### 7.4 `csv/bindings.csv`

| Column | Type | Notes |
|---|---|---|
| `bindingId` | string | e.g. `BIND-F2-D3-91c`, matching `BUILD_SPEC_v1.md` section 3's example |
| `fieldId` | string | |
| `caseId` | string | |
| `sourceDocId` | string | |
| `candidateValue` | number | |
| `asOf` | ISO 8601 datetime with offset | Copied from the owning document's `cutoffAt` |
| `sourceRegionPage` | integer | |
| `sourceRegionCharStart` | integer | |
| `sourceRegionCharEnd` | integer | |
| `snippetText` | string | Literal substring, for display and hash verification |

### 7.5 `csv/eval_labels.csv` (the eval label file, full spec in Section 8)

| Column | Type | Notes |
|---|---|---|
| `itemId` | string | |
| `caseId` | string | |
| `fieldCode` | string | |
| `expectedFieldState` | string, enum: `SUPPORTED`, `CONFLICTED`, `UNSUPPORTED` | |
| `expectedValue` | number or empty | Empty exactly when `expectedFieldState` is `UNSUPPORTED` |
| `expectedSourceDocId` | string or empty | Non-empty only when `expectedFieldState` is `SUPPORTED` |
| `conflictingDocIds` | string or empty | Semicolon-separated, e.g. `D1;D3`; populated only when `expectedFieldState` is `CONFLICTED` |
| `shouldAbstain` | boolean | `TRUE` when `expectedFieldState` is `CONFLICTED` or `UNSUPPORTED`, `FALSE` when `SUPPORTED` |
| `reasonCategory` | string, enum: `CLEAN`, `DISTRACTOR`, `VERSION_CONFLICT`, `TIMING_CONFLICT`, `CORRECTION_CONFLICT`, `MISSING_FIELD` | |
| `difficultyTier` | string, enum: `EASY`, `MEDIUM`, `HARD` | |
| `note` | string | Free text |

This CSV seeds only the ground-truth half of `BUILD_SPEC_v1.md`'s `EvalItem` schema (the `expected*` fields). The model-scored half (`modelPredicted*`, `isExtractionCorrect`, `isAbstentionCorrect`, `scoredAt`) is written later, by the eval harness itself, when `GET /eval/run` actually executes against a live or replayed model. The generator does not and should not populate those columns.

---

## 8. The eval label format

**Scope.** 50 to 100 labelled items (sourced, `04_CLEAN_START_BUILD_KIT.md` section 5 and `BUILD_SPEC_v1.md` section 6). This document's plan lands at approximately 64 (Section 6).

**Per-item spec**, mapped onto the columns in Section 7.5:

| Task's field | CSV column(s) | What it is |
|---|---|---|
| Item id | `itemId` | Unique across the whole eval set |
| Document id | `expectedSourceDocId` (`SUPPORTED` items) or `conflictingDocIds` (`CONFLICTED` items) | A `CONFLICTED` item has no single correct document, so it carries a list instead of one id; an `UNSUPPORTED` item carries neither |
| Field id | `fieldCode` | |
| True value | `expectedValue` | The correct answer, including for `CONFLICTED` items, since `CANON.md` section 5 itself names a correct answer even where the model must abstain ("A human who knows..."). Abstaining does not mean there is no truth, it means the model is not the one who gets to pick it |
| Should-abstain boolean | `shouldAbstain` | The single most important column, see below |
| Reason category | `reasonCategory` | |
| Difficulty tier | `difficultyTier` | |
| Free-text note | `note` | |

**The scoring consequence of each field**, tied to `BUILD_SPEC_v1.md` section 7's seven metrics: `expectedFieldState` plus `shouldAbstain` sort every item into the denominator of field recall, coverage, abstention rate, or conflict-detection recall. `expectedValue` plus `expectedSourceDocId` are what field precision and evidence-localisation success get checked against, but only for items where `expectedFieldState` is `SUPPORTED`. `reasonCategory` lets the results table break accuracy down by cause after the run (was the model actually worse on CORRECTION-type conflicts than TIMING-type, for instance), which is a stronger, more falsifiable claim than one blended accuracy number. `difficultyTier` supports the same kind of breakdown and also flags which items a juror-facing walkthrough should and should not cherry-pick.

**Abstention correctness is a first-class scored outcome, not a tiebreaker.** Stated exactly as `CANON.md` section 6 and `BUILD_SPEC_v1.md` section 7 both already establish, and repeated here because it governs every row where `shouldAbstain` is `TRUE`: abstaining on a planted conflict is CORRECT. Silently picking a value on a planted conflict is a FAILURE, even when the picked value happens to match the true value in `expectedValue`. A model that gets CONF-F2 "right" by guessing 19,300,000 without showing both candidates and their cut-off timestamps has still failed the item, because the product's entire claim is refusing to decide silently, not guessing well. `isExtractionCorrect` and `isAbstentionCorrect` (`BUILD_SPEC_v1.md` section 3.10) are never both scored on the same item precisely so this distinction cannot be blurred into one "was it right" boolean.

**Worked table, 12 example rows.** Rows 1 to 4 are the canon case, exact CANON numbers, no hypothesis tag needed. Rows 5 to 12 are illustrative filler, values marked hypothesis.

| itemId | caseId | fieldCode | Document id | True value | shouldAbstain | reasonCategory | difficultyTier | note |
|---|---|---|---|---|---|---|---|---|
| EVAL-0001 | CASE-2026-Q1-MER001 | F1 | conflicting: D2 vs D1/D3 | 42,500,000 | TRUE | VERSION_CONFLICT | HARD | LP-04 signed but not counter-executed; correct behaviour shows both 42,500,000 and 45,000,000 |
| EVAL-0002 | CASE-2026-Q1-MER001 | F2 | conflicting: D1/D4 vs D3 | 19,300,000 | TRUE | TIMING_CONFLICT | HARD | Call landed 17:42 IST, after the 16:00 IST cut-off; both 17,800,000 and 19,300,000 are correct as of their own cut-off |
| EVAL-0003 | CASE-2026-Q1-MER001 | F3 | conflicting: D1 v2 vs D3 | 21,940,500 | TRUE | CORRECTION_CONFLICT | HARD | Administrator restated 8 Jul; D3 predates the restatement and shows no version marker at all |
| EVAL-0004 | CASE-2026-Q1-MER001 | F4 | none | (no value) | TRUE | MISSING_FIELD | MEDIUM | No source document carries this field; correct behaviour is zero candidates, never a default of zero |
| EVAL-0005 | CASE-EVAL-0001 | F1 | D1-style statement only | 40,000,000 (hypothesis) | FALSE | CLEAN | EASY | Single clean source, no trap planted; a prior, smaller quarter for the same fund |
| EVAL-0006 | CASE-EVAL-0001 | F3 | D1-style statement only | 20,100,000 (hypothesis) | FALSE | CLEAN | EASY | Single clean source |
| EVAL-0007 | CASE-EVAL-0002 | F2 | D1-style statement only | 15,000,000 (hypothesis) | FALSE | DISTRACTOR | MEDIUM | Same line also prints an "Undrawn Commitment" figure of 25,000,000 (hypothesis) directly beside it; correct extraction must pick the labelled Drawn figure, not its neighbour |
| EVAL-0008 | CASE-EVAL-0003 | F1 | conflicting: D2-style vs D1-style | 46,000,000 (hypothesis) | TRUE | VERSION_CONFLICT | HARD | A second, independently generated VERSION-cause example, so the harness is not scoring on one memorised case |
| EVAL-0009 | CASE-EVAL-0004 | F2 | conflicting: D1-style vs D3-style | 12,400,000 (hypothesis) | TRUE | TIMING_CONFLICT | HARD | A second, independently generated TIMING-cause example |
| EVAL-0010 | CASE-EVAL-0005 | F3 | conflicting: D1-style vs D3-style | 18,225,000 (hypothesis) | TRUE | CORRECTION_CONFLICT | HARD | A second, independently generated CORRECTION-cause example |
| EVAL-0011 | CASE-EVAL-0006 | F5-EVAL (eval-only field code, never appears in the canon demo or on stage: "side letters executed during the quarter") | none | (no value) | TRUE | MISSING_FIELD | MEDIUM | A second, differently-worded MISSING example, so the harness is not just re-testing "complaints closed" |
| EVAL-0012 | CASE-EVAL-0007 | F2 | D1-style statement only | 9,750,000 (hypothesis) | FALSE | CLEAN | HARD | Single source, but heavy thousands-separator and currency-symbol noise; tests formatting robustness, not abstention |

**Composition target for the full approx. 64-item set**, a hypothesis / design choice consistent with the sourced 50-100 band: 28 `SUPPORTED` clean, 12 `SUPPORTED` distractor (40 `SUPPORTED` total), 15 `CONFLICTED` (roughly five per cause), 9 `UNSUPPORTED`. That puts `CONFLICTED` plus `UNSUPPORTED` at roughly 24 of 64 items, about 38%, enough to make conflict-detection recall and abstention rate statistically meaningful without making the corpus mostly traps, which would not resemble a real quarterly return either.

---

## 9. JSON Schema for the fixture manifest

This is the build-time corpus index, `fixtures/manifest.json`, written once per generator run. It is a different object from `BUILD_SPEC_v1.md` section 3.8's `ManifestEntry` (that one is a runtime, per-case, hash-chained ledger the product itself builds as a case moves through the state machine, sealed on demand). This one is the generator's own receipt: what did Hour 0 actually produce.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kriseva.ai/attest/schema/fixture-manifest.json",
  "title": "FixtureManifest",
  "type": "object",
  "required": ["generatorVersion", "seed", "generatedAt", "syntheticLabel", "counts", "cases", "documents"],
  "properties": {
    "generatorVersion": {
      "type": "string",
      "description": "Free-text tag or commit id of the generator script that produced this run."
    },
    "seed": {
      "type": ["integer", "string"],
      "description": "The fixed deterministic seed used for this run. Identical seed plus identical generatorVersion must reproduce byte-identical output."
    },
    "generatedAt": { "type": "string", "format": "date-time" },
    "syntheticLabel": {
      "const": "SYNTHETIC",
      "description": "Present so any consumer of this file can assert, without reading further, that everything it indexes is fictional."
    },
    "counts": {
      "type": "object",
      "required": ["cases", "documents", "fields", "bindings", "conflicts", "evalItems"],
      "properties": {
        "cases": { "type": "integer", "minimum": 1 },
        "documents": { "type": "integer", "minimum": 1 },
        "fields": { "type": "integer", "minimum": 1 },
        "bindings": { "type": "integer", "minimum": 1 },
        "conflicts": { "type": "integer", "minimum": 0 },
        "evalItems": {
          "type": "integer",
          "minimum": 50,
          "maximum": 100,
          "description": "Total labelled eval items. Must land in the 50-100 band from 04_CLEAN_START_BUILD_KIT.md section 5 and BUILD_SPEC_v1.md section 6."
        }
      },
      "additionalProperties": false
    },
    "cases": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["caseId", "isCanonCase", "fieldCodes"],
        "properties": {
          "caseId": { "type": "string" },
          "isCanonCase": {
            "type": "boolean",
            "description": "True only for CASE-2026-Q1-MER001. Exactly one case in the array may be true."
          },
          "fieldCodes": { "type": "array", "items": { "type": "string" }, "minItems": 1 }
        },
        "additionalProperties": false
      },
      "minItems": 1
    },
    "documents": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["sourceDocId", "caseId", "docCode", "docFormat", "filePath", "sha256"],
        "properties": {
          "sourceDocId": { "type": "string" },
          "caseId": { "type": "string" },
          "docCode": { "type": "string" },
          "version": { "type": "integer", "minimum": 1 },
          "supersedesDocId": { "type": ["string", "null"] },
          "docFormat": { "type": "string", "enum": ["PDF_TEXT", "CSV", "XLSX_TEXT"] },
          "filePath": { "type": "string" },
          "sha256": { "type": "string", "pattern": "^[a-f0-9]{64}$" }
        },
        "additionalProperties": false
      },
      "minItems": 1
    },
    "csvArtifacts": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "filePath", "rowCount", "sha256"],
        "properties": {
          "name": { "type": "string" },
          "filePath": { "type": "string" },
          "rowCount": { "type": "integer", "minimum": 0 },
          "sha256": { "type": "string", "pattern": "^[a-f0-9]{64}$" }
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```

---

## 10. Acceptance checks for Hour 0

Run before committing the fixture pack. All must be true.

1. `fixtures/manifest.json` exists and validates against the JSON Schema in Section 9.
2. `manifest.json`'s `counts.evalItems` is between 50 and 100 inclusive.
3. The canon case folder `fixtures/documents/CASE-2026-Q1-MER001/` contains exactly five files: D1 v1 (superseded), D1 v2, D2, D3, D4. Not four; five, per Section 3's file-count note.
4. Every one of D1's, D2's, D3's and D4's canon field values matches `CANON.md` section 5 exactly: F1 is 42,500,000 (D1 v2, D3) and 45,000,000 (D2); F2 is 17,800,000 (D1 v2, D4) and 19,300,000 (D3); F3 is 21,940,500 (D1 v2) and 22,415,000 (D3); F4 appears nowhere.
5. All four planted conflicts are present and independently detectable from the raw document text alone, without consulting this spec: CONF-F1 via LP-04's status column in D2, CONF-F2 via the 17:42 IST timestamp in D3 against the 16:00 IST cut-off on D1/D4, CONF-F3 via D1's version-2 stamp and D3's total absence of a version stamp, ABSENCE-F4 via checking all four documents and finding nothing.
6. The four conflicts render as four visibly different detection paths (a status field, a timestamp comparison, a version-stamp comparison, an absence), not the same mechanism relabelled.
7. Every generated document file and every generated CSV file contains the literal word "SYNTHETIC" (or the exact phrase used in this document's example blocks) somewhere in its header or footer.
8. Re-running the generator with the same seed produces byte-identical output to the prior run (diff the `fixtures/` tree, or compare every file's `sha256` in `manifest.json`; there must be zero differences).
9. `csv/eval_labels.csv` row count matches `manifest.json`'s `counts.evalItems`, and its `reasonCategory` distribution is within a reasonable band of the Section 8 composition target (roughly 60-65% `SUPPORTED`, roughly 20-25% `CONFLICTED`, roughly 12-16% `UNSUPPORTED`).
10. Every `CONFLICTED` row in `eval_labels.csv` has `shouldAbstain = TRUE` and a non-empty `conflictingDocIds`; every `UNSUPPORTED` row has `shouldAbstain = TRUE` and an empty `expectedValue`; every `SUPPORTED` row has `shouldAbstain = FALSE` and a non-empty `expectedSourceDocId`. No row violates the pairing in any direction.
11. No banned word (see `FACT_CARD.md` section 9) and no em dash appears anywhere in any generated document text.
12. No real company, fund, administrator, custodian or person's name appears anywhere in the corpus. Grep the entire `fixtures/` tree for the founders' own names and for any real IFSCA-registered entity name known to the team; zero matches.
13. `csv/documents_index.csv`, `csv/fields.csv` and `csv/bindings.csv` row counts match `manifest.json`'s `counts.documents`, `counts.fields` and `counts.bindings` respectively.
14. Total elapsed wall-clock time from generator start to this checklist passing is under 45 minutes, timed and written down for the milestone-map log.
15. `git status` inside the fresh sprint repo shows the entire `fixtures/` tree as new, untracked or newly added files, generated after 14:00 Friday, matching the commit-history-audit requirement in `04_CLEAN_START_BUILD_KIT.md` section 1.

---

## Open founder decisions

**OD1: does the scale-up path (Section 6, option 3) get built at all, and if so, what is the second scheme called?** `CANON.md` is marked STABLE and locked, owned by the founder, with an explicit rule that any change propagates to every other factory artifact and must be re-verified. A second scheme under the existing FME (Meridian Alpha Capital IFSC Private Limited running a second fund alongside Meridian Alpha Opportunities Fund I) is the only scale-up option in this document that requires inventing an entity not currently in `CANON.md`. Every other volume increase in Section 6 stays entirely inside the existing roster. Exact question for the founder: if there is spare time on Friday, is a second scheme in scope, and if yes, what is it named (this document does not propose a name, since naming it is the kind of canon-propagating decision `CANON.md` itself reserves for the founder)? Default if unanswered: do not build it. Stop at option 2 (a second reporting quarter for the existing scheme), which needs no new entity and no founder sign-off.

---

## 11. The clean case (added by Fable, 2026-08-19, and it is not optional)

**Why this exists.** Every scenario specified above is an exception. If a juror says "show me a normal one, where nothing is wrong" and we cannot, the honest read is that we built four exception screens rather than a working product. `QUALITY_BAR.md` ranks this as the cheapest scenario to cover and `USE_CASE_MATRIX.md` lists it in the Q&A bank. It is one generator run with different parameters, not new engineering.

**Adjudication of open decision OD1.** Do not invent a second scheme, and do not invent a second entity. CANON is locked and a new fund adds nothing a juror wants to see. Build a second **case** instead: the same entity, the same scheme, the **prior** quarter. That answers the question, costs one parameter set, and adds a second thing worth more than either case alone, which is continuity between quarters.

### 11.1 Case definition

| Property | Value |
|---|---|
| Case id | `CASE-2025-Q4-MER001` |
| Entity and scheme | Meridian Alpha Capital IFSC Private Limited, Meridian Alpha Opportunities Fund I (unchanged) |
| Reporting period | Quarter ended 31 March 2026 (Q4 FY2025-26) |
| Return due | 21 April 2026 |
| Designed outcome | All four fields `SUPPORTED`. Zero conflicts. Zero abstentions. Case reaches `SEALED` with no human conflict decision required |

### 11.2 The four fields, all agreeing

| Field | Value, all sources agreeing | Why there is no conflict in this quarter |
|---|---|---|
| F1 Committed capital | USD 42,500,000 | LP-04's subscription is dated 22 June 2026, which is inside the next quarter. In this quarter the register and the administrator statement carry the same four-investor total |
| F2 Drawn capital | USD 14,400,000 | No capital call lands near a cut-off in this quarter. Administrator, ledger and custodian all agree |
| F3 Closing NAV | USD 20,512,000 | The administrator issues one statement and never restates it. There is no version 2 |
| F4 Complaints closed | 2 | A compliance register extract exists for this quarter and carries the figure. This is the field's `SUPPORTED` state, and it exists so the contrast with the next quarter is visible |

### 11.3 The continuity that makes this worth more than a happy path

The two cases chain, and the arithmetic is checkable by anyone in the room who knows funds:

- Closing NAV of this quarter, USD 20,512,000, is the opening NAV on the Q1 internal ledger (`D3`, section 3). Same number, two documents, two quarters.
- Closing drawn capital of this quarter, USD 14,400,000, plus the 14 May capital call of USD 3,400,000 already on the Q1 ledger, gives USD 17,800,000, which is exactly what the Q1 administrator statement reports at its 16:00 cut-off.
- Add the USD 1,500,000 call that lands at 17:42 on 30 June, after that cut-off, and you get USD 19,300,000, which is exactly what the Q1 ledger reports.

That chain is the demo's strongest technical moment if a juror asks for it. The timing conflict in Q1 is not an arbitrary planted disagreement. It is the arithmetic consequence of one payment arriving one hour and forty-two minutes after somebody drew a line. Walk the numbers and the conflict explains itself.

### 11.4 The teaching contrast on F4

In this quarter the complaints figure has a source and the system produces a value with a binding. In the next quarter nobody produced a compliance register, so the same field has no source and the system refuses. Same field, same product, two different outcomes, and the only thing that changed is whether the evidence existed.

That is the cleanest available answer to the objection "your conflicts are planted, of course it catches them". The system is not detecting planted conflicts. It is reporting the state of the evidence.

### 11.5 Documents to generate

Same four templates as sections 3.1 to 3.4, regenerated with this quarter's parameters, plus one addition:

| Doc id | Document | Notes |
|---|---|---|
| `D1-Q4` | Administrator statement, version 1 only | No `supersedesDocId`, no version 2. This is what a normal quarter looks like |
| `D2-Q4` | Subscription register extract | Three counter-executed investors, no pending row |
| `D3-Q4` | Internal ledger export | Closing NAV 20,512,000, closing drawn 14,400,000 |
| `D4-Q4` | Custodian confirmation | Cash position consistent with drawn capital |
| `D5-Q4` | Compliance register extract | New template. Carries the complaints-closed figure of 2, with the quarter's complaint log summarised. Two columns: complaint reference, date closed. This is the only new document shape in the clean case |

### 11.6 Generation and eval

- Same deterministic seed discipline as section 5. Use seed offset `+1` from the Q1 seed so both cases regenerate reproducibly and independently.
- Add 12 to 16 eval items for this case to the label set, all with `shouldAbstain = FALSE`. This matters for the eval numbers: without any clean items, abstention rate is meaningless because the system has never been given a chance to answer. A harness that only measures refusals on cases designed to require refusal is not measuring anything.
- Target composition after this addition: roughly 76 to 80 items total, still inside the 50 to 100 band.

### 11.7 Build cost and cut rule

Estimated 20 to 30 minutes at M1, almost all of it verification rather than authoring, because the generator already exists by then and this is a parameter set (hypothesis, to be confirmed at rehearsal build 1).

Cut rule: if M1 runs long, generate the clean case with the four existing document templates and drop `D5-Q4`, accepting that F4 abstains in both quarters. That loses the teaching contrast in 11.4 but keeps the "show me a normal one" answer, which is the part that matters.
