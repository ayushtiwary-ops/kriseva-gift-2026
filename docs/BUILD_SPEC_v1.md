# BUILD_SPEC v1: the engineering specification for KRISEVA ATTEST

> **Read `UI_LANGUAGE_AND_VISUALS_SPEC.md` before building any screen.** This file specifies the engine, the data and the API. It does not specify what the screens say, and building from this file alone reproduces an interface that reads in machine vocabulary: a juror sees "Committed capital, CONFLICTED" and disengages. The language mapping, the glossary, every visual algorithm, the filing history model and five defects that were invisible from the code all live in that file.

Status: DRAFT v1, written 2026-08-19. Owner: founder approves, this document is what the Friday build agent implements from.

Ground truth order: `CANON.md` is the fictional world, the state model and the seven screens, and wins on any conflict. `FACT_CARD.md` is every number allowed on stage. `AWS_RUNBOOK.md` is the exact AWS commands. `UX_PSYCHOLOGY_SPEC.md` is the visual, typographic, motion and copy specification for the same seven screens described functionally here. `SCHEMA_PACK.md` and `DEMO_STORYBOARD.md` are named as companion documents throughout this file; as of this writing they do not yet exist in `factory/`, so every section that would defer to them also carries a self-contained summary sufficient to build from. See "Open founder decisions" at the end.

This document contains no application source code. JSON Schema blocks, CLI commands and API payload examples are specifications and configuration, not code, per the hackathon's own pre-build allowance (doc 04 section 1). Every behaviour is stated in English or as a schema.

---

## 0. Build order and milestone map

Read this first. It maps the 22-hour sprint (doc 04 section 6, Friday 14:00 to Saturday 12:00) to the sections below, so the build agent knows what to open when. Milestone names and hour windows are doc 04's; nothing here changes them.

| Milestone | Hours | Doc 04 deliverable | Build FROM these sections | Also consult |
|---|---|---|---|---|
| M1 | 0-2 | Repo init, NOTICE + docs commit, scaffold, synthetic generator running, fixture pack v1 | Section 2 (glossary), Section 3 (Case, Field, SourceDoc, Binding schemas), Section 6 (data generation rules and the conflict matrix) | `REPO_FIRST_COMMIT_PACK.md` for the exact NOTICE.md and README text; `SCHEMA_PACK.md` (not yet written) for the full field-by-field generation spec |
| M2 | 2-5 | Bedrock provider live, first real extraction with source pins, run recording working | Section 3 (RunRecord, Binding), Section 4 (`POST /extract`, `GET /replay/:id`), Section 9 (AWS: IAM app identity, Bedrock verification) | `AWS_RUNBOOK.md` sections 3 and 4 for exact CLI |
| M3 | 5-10 | The spine closed: conflict detection, abstain, decision UI with named reviewer and reason, maker-checker, manifest chain and tamper check | Section 3 (Conflict, Decision, Signoff, ManifestEntry), Section 4 (`POST /decide`, `POST /signoff`, `GET /manifest/:id`), Section 5 (S1, S2, S3, S6, S7), Section 8 (hash spec) | `UX_PSYCHOLOGY_SPEC.md` section 13 ranks S1 and S3 as the first two screens to build fully in this window, before S4 or S5 |
| M4 | 10-15 | Eval harness run on 50+ labelled items, risk board, results table | Section 3 (EvalItem), Section 4 (`GET /eval/run`), Section 5 (S5), Section 7 (eval protocol), Section 11 (the five invariant tests) | none new |
| M5 | 15-19 | AWS hosting, replay panel, failure-mode demo, polish | Section 9 (hosting, ranked, abandon points), Section 5 (S4 polish) | `AWS_RUNBOOK.md` section 6 |
| M6 | 19-21 | Pitch integration: honesty table, architecture slide, demo rehearsed 3x, screen-recording backup captured | Section 10 (demo script mapping), Section 12 (never-cut list) | `DEMO_STORYBOARD.md` (not yet written); `REPO_FIRST_COMMIT_PACK.md` section 3 for the honesty table skeleton |
| 21-22 | freeze | Freeze, push, tag, verify history, README final | Section 12 (verify the never-cut list survived) | `REPO_FIRST_COMMIT_PACK.md` section 5, the audit read-back commands |

Note on the human-lead names in doc 04's table: doc 04 section 6 names "Ayush" and "Sony." `CANON.md` section 12, decision C1, records that the newest documents use "Mahek" and flags the name as an open reconciliation item. This document follows CANON's stated default (Mahek) wherever a second founder is named, and takes no further position; it is not a new decision, only an application of the existing one.

---

## 1. Product, one paragraph

KRISEVA ATTEST is a research-stage evidence and accountability layer for the quarterly regulatory return an IFSCA-registered Fund Management Entity in GIFT City must file. It is built for the two named individuals whose personal signatures that filing requires: the Compliance Officer and the Principal Officer. Where source documents agree, a model proposes a value for a reported field and pins it to the exact text it read it from. Where documents disagree, or where no document supports a required field, the model abstains and a named human decides, with a mandatory recorded reason, before a second named human confirms under a maker-checker rule the system enforces, not policy. Every artifact and every state change is chained into a SHA-256 sealed manifest that breaks visibly if altered after the fact. ATTEST sits upstream of DRR, the regulator's own submission pipeline: it governs how the entity assembles and stands behind its own numbers before anything is filed anywhere, and it never integrates with, connects to, or files to DRR or any other IFSCA system. This build makes no accuracy claim, no pilot claim, no production claim. It is a demonstration of a protocol, on synthetic data, at the research stage.

---

## 2. Glossary

Plain English, one line each. Every term a coding agent or a juror needs.

| Term | Meaning |
|---|---|
| FME (Fund Management Entity) | An entity registered with IFSCA to manage investment funds in GIFT City. Meridian Alpha Capital IFSC Private Limited, our synthetic buyer, is a Registered FME, Non-Retail. |
| Principal Officer | The senior individual an FME designates to IFSCA as accountable for the fund's operations. The checker in our maker-checker flow (Rajiv Menon). Must be based in the IFSC; the signature is personal. |
| Compliance Officer | The individual responsible for the FME's regulatory filings and record-keeping. The maker in our flow (Priya Ramanathan). Must be based in the IFSC. |
| Administrator | An independent firm the fund hires to compute NAV and produce periodic statements. Northwind Fund Services (IFSC) Private Limited in our canon. Does not itself decide what the FME reports. |
| Custodian | An independent firm that holds and confirms the fund's cash and securities. Sentinel Custody Services, IFSC Branch, in our canon. |
| NAV (Net Asset Value) | The fund's assets minus its liabilities, at a point in time. "Closing NAV" is the NAV as at the end of the reporting quarter. |
| Committed capital | The total amount investors have contractually agreed to invest, whether or not it has been paid in yet. |
| Drawn capital | The portion of committed capital that has actually been called and paid in by investors so far. |
| Capital call | A formal demand from the fund to its investors to pay in some or all of their remaining committed, undrawn capital. |
| Quarterly return | The periodic regulatory filing an FME must submit to IFSCA, due 21 calendar days after each quarter end. |
| DRR | IFSCA's own Data Receipt and Repository system: web-based report collection, taxonomy management, validation, dashboards, API integrations, security. ATTEST sits upstream of it and never integrates with, connects to, or files to it. |
| Propose | What the model does to a field: suggests a value and pins it to the source text it read the value from. Never final. |
| Abstain | What the model does instead of guessing, when it finds two or more disagreeing candidates (CONFLICTED) or none (UNSUPPORTED). A designed, correct outcome, not an error. |
| Decide | What a named human does to move a CONFLICTED or UNSUPPORTED field to DECIDED, by choosing a value, or by formally confirming none exists, and recording a mandatory, non-empty reason. |
| Maker-checker | The rule that the human who decided a field's value (the maker) cannot be the human who signs off the case (the checker). Enforced by the engine, not left to policy. |
| Manifest | The ordered, hash-chained record of every artifact and state transition in a case, sealed with SHA-256, that lets anyone independently verify nothing was altered after the fact. |
| Binding | The data record that pins one candidate value to the exact region of the exact source document it was read from. The mechanism behind "every proposed value is pinned to evidence." |
| Source region | The specific location inside a source document, in this build a page plus a character-offset span, that a Binding points to as the origin of a candidate value. |
| Replay | Re-serving a previously recorded model call's exact response, deterministically, without contacting the live model provider again. Used for offline demo insurance and the judge-facing replay panel. |
| Eval harness | The rig that runs extraction over a labelled synthetic dataset and scores it, separately, on whether it extracted correctly and on whether it abstained correctly. |

---

## 3. Data model, as JSON Schema

Ten objects. Each schema below is complete and implementable as written: required properties, types, and enums matching `CANON.md` section 7 exactly. The case-state and field-state enums appear on `Case.state` and `Field.state` respectively (3.1 and 3.2); they are not repeated as separate schemas because CANON does not treat them as separate objects.

A design decision that touches several schemas at once, stated here so it is not repeated ten times: `CANON.md`'s "planted-conflict matrix" (section 6) names four causes, TIMING, CORRECTION, VERSION and MISSING, but only the first three are genuine disagreements between two or more candidate values. MISSING (field F4 in the canon case) has zero candidates, not two conflicting ones; `UX_PSYCHOLOGY_SPEC.md` section 3.4 independently confirms this by giving MISSING a different hue, a different border style and the label "categorically different state, not just a different cause within CONFLICTED." This build therefore models TIMING, CORRECTION and VERSION as `Conflict` records (3.5), and models MISSING as a `Field` that reaches state `UNSUPPORTED` with zero `Binding` records and no `Conflict` record at all. A coding agent should not try to force a fourth `Conflict.cause` value for MISSING.

A second decision that touches the model: source regions are addressed as page plus character-offset span into the canonical extracted text of a document, not as PDF bounding boxes. This is the buildable choice inside a 22-hour, no-build-step, static-HTML sprint (doc 04 section 3); document fixtures are generated as structured text per Section 6, not scanned images, so there is nothing for a bounding box to be measured against.

### 3.1 Case

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kriseva.ai/attest/schema/case.json",
  "title": "Case",
  "type": "object",
  "required": ["caseId", "fmeId", "schemeId", "reportingPeriodEnd", "returnDueDate", "state", "fieldIds", "syntheticLabel", "createdAt", "updatedAt"],
  "properties": {
    "caseId": { "type": "string", "pattern": "^CASE-[0-9]{4}-Q[1-4]-[A-Z0-9]{4,10}$", "description": "One case per quarterly return. Canon example: CASE-2026-Q1-MER001." },
    "fmeId": { "type": "string", "description": "Canon example: FME-MERIDIAN-ALPHA." },
    "schemeId": { "type": "string", "description": "Canon example: SCHEME-MAOF-I." },
    "reportingPeriodEnd": { "type": "string", "format": "date", "description": "Canon value: 2026-06-30." },
    "returnDueDate": { "type": "string", "format": "date", "description": "Canon value: 2026-07-21, 21 calendar days after period end." },
    "state": { "type": "string", "enum": ["INGESTED", "EXTRACTED", "UNDER_REVIEW", "SIGNED", "SEALED"] },
    "fieldIds": { "type": "array", "items": { "type": "string" }, "minItems": 1 },
    "sourceDocIds": { "type": "array", "items": { "type": "string" } },
    "makerUserId": { "type": ["string", "null"], "description": "Set once the first Decision is recorded on this case." },
    "checkerUserId": { "type": ["string", "null"], "description": "Set once Signoff is recorded." },
    "manifestId": { "type": ["string", "null"] },
    "syntheticLabel": { "type": "string", "const": "SYNTHETIC" },
    "createdAt": { "type": "string", "format": "date-time" },
    "updatedAt": { "type": "string", "format": "date-time" }
  },
  "additionalProperties": false
}
```

**Invariant that matters most:** `state` only ever moves forward through the five listed values, one step at a time, and the move to `SIGNED` is rejected unless every `fieldId` on the case resolves to `Field.state` of `DECIDED` or `CONFIRMED` (CANON hard rule 3: a case cannot reach SIGNED while any field is CONFLICTED or UNSUPPORTED). No code path may set `state` directly; it is always a side effect of an API call in Section 4.

### 3.2 Field

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kriseva.ai/attest/schema/field.json",
  "title": "Field",
  "type": "object",
  "required": ["fieldId", "caseId", "fieldCode", "label", "unit", "state", "candidateCount"],
  "properties": {
    "fieldId": { "type": "string", "pattern": "^FIELD-[A-Z0-9-]+-F[0-9]+$" },
    "caseId": { "type": "string" },
    "fieldCode": { "type": "string", "description": "Free string so the eval corpus (Section 6) can generate fields beyond the canon four. The canon demo case uses exactly F1, F2, F3, F4 per CANON section 3.", "examples": ["F1", "F2", "F3", "F4"] },
    "label": { "type": "string", "examples": ["Committed capital", "Drawn capital", "Closing NAV", "Complaints closed during the quarter"] },
    "unit": { "type": "string", "enum": ["USD", "COUNT"] },
    "state": { "type": "string", "enum": ["SUPPORTED", "CONFLICTED", "UNSUPPORTED", "DECIDED", "CONFIRMED"] },
    "candidateCount": { "type": "integer", "minimum": 0, "description": "0 for UNSUPPORTED, 1 for SUPPORTED, 2+ for CONFLICTED. Carried forward unchanged once DECIDED or CONFIRMED." },
    "conflictId": { "type": ["string", "null"], "description": "Set only when state is or was CONFLICTED. Null for UNSUPPORTED; see the note at the top of Section 3." },
    "decisionId": { "type": ["string", "null"] },
    "decidedValue": { "type": ["number", "string", "null"] },
    "createdAt": { "type": "string", "format": "date-time" },
    "updatedAt": { "type": "string", "format": "date-time" }
  },
  "additionalProperties": false
}
```

**Invariant that matters most:** `state` can never be set to `DECIDED` or `CONFIRMED` by anything other than, respectively, a `Decision` record and a `Signoff` record that names a human. A model-produced extraction can only ever leave a `Field` in `SUPPORTED`, `CONFLICTED` or `UNSUPPORTED` (CANON hard rule 1: a model may propose, never decide).

### 3.3 SourceDoc

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kriseva.ai/attest/schema/source-doc.json",
  "title": "SourceDoc",
  "type": "object",
  "required": ["sourceDocId", "caseId", "docCode", "issuer", "version", "cutoffAt", "issuedAt", "storageUri", "contentHash", "syntheticLabel"],
  "properties": {
    "sourceDocId": { "type": "string" },
    "caseId": { "type": "string" },
    "docCode": { "type": "string", "description": "Free string. Canon demo uses D1 to D4 (CANON section 4).", "examples": ["D1", "D2", "D3", "D4"] },
    "documentType": { "type": "string", "enum": ["ADMINISTRATOR_STATEMENT", "SUBSCRIPTION_REGISTER", "INTERNAL_LEDGER", "CUSTODIAN_CONFIRMATION"] },
    "issuer": { "type": "string", "examples": ["Northwind Fund Services (IFSC) Private Limited", "Sentinel Custody Services, IFSC Branch"] },
    "version": { "type": "integer", "minimum": 1 },
    "supersedesDocId": { "type": ["string", "null"], "description": "Points at the prior version's sourceDocId. Never null-then-filled by editing the same row; a new version is always a new SourceDoc record." },
    "cutoffAt": { "type": "string", "format": "date-time", "description": "The 'as at' timestamp the document itself claims, with explicit UTC offset, e.g. 2026-06-30T16:00:00+05:30." },
    "issuedAt": { "type": "string", "format": "date-time", "description": "When the document was produced or reissued." },
    "storageUri": { "type": "string", "description": "e.g. s3://<BUCKET_NAME>/<caseId>/<sourceDocId>.txt" },
    "extractedText": { "type": "string", "description": "Canonical plain-text extraction. Binding.sourceRegion offsets are measured against this exact string." },
    "contentHash": { "type": "string", "pattern": "^[a-f0-9]{64}$", "description": "SHA-256 hex of extractedText, computed at ingest. See Section 8." },
    "mimeType": { "type": "string", "enum": ["text/plain", "application/pdf"] },
    "syntheticLabel": { "type": "string", "const": "SYNTHETIC" },
    "createdAt": { "type": "string", "format": "date-time" }
  },
  "additionalProperties": false
}
```

**Invariant that matters most:** a `SourceDoc` is never mutated after creation; the store is append-only. Reissuing a document (CANON's D1 version 1 to version 2 trap) always creates a new `SourceDoc` row with `version` incremented and `supersedesDocId` set; it never overwrites `extractedText`, `cutoffAt` or `contentHash` on the existing row. This is what lets the conflict between an old and a new version surface naturally instead of being silently hidden.

### 3.4 Binding

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kriseva.ai/attest/schema/binding.json",
  "title": "Binding",
  "type": "object",
  "required": ["bindingId", "fieldId", "caseId", "sourceDocId", "candidateValue", "sourceRegion", "asOf", "createdAt"],
  "properties": {
    "bindingId": { "type": "string" },
    "fieldId": { "type": "string" },
    "caseId": { "type": "string" },
    "sourceDocId": { "type": "string" },
    "candidateValue": { "type": ["number", "string"] },
    "sourceRegion": {
      "type": "object",
      "required": ["page", "charStart", "charEnd", "snippetText"],
      "properties": {
        "page": { "type": "integer", "minimum": 1, "default": 1 },
        "charStart": { "type": "integer", "minimum": 0 },
        "charEnd": { "type": "integer", "minimum": 0 },
        "snippetText": { "type": "string", "description": "Literal substring of the SourceDoc.extractedText between charStart and charEnd, stored redundantly for display and hash verification." }
      },
      "additionalProperties": false
    },
    "asOf": { "type": "string", "format": "date-time", "description": "Copied from the owning SourceDoc.cutoffAt at binding time. This is what lets S3 show both candidates with their own cut-off timestamps." },
    "extractedByRunId": { "type": ["string", "null"], "description": "Null only for seed/ground-truth bindings written by the generator, never for a binding shown as a live model proposal." },
    "confidence": { "type": ["number", "null"], "minimum": 0, "maximum": 1 },
    "createdAt": { "type": "string", "format": "date-time" }
  },
  "additionalProperties": false
}
```

**Invariant that matters most:** a `Binding` is immutable once written; a re-extraction creates a new `Binding`, never an overwrite. Bindings are direct inputs to the manifest hash chain (Section 8), so mutating one in place would silently invalidate a seal that has not yet been computed over it.

### 3.5 Conflict

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kriseva.ai/attest/schema/conflict.json",
  "title": "Conflict",
  "type": "object",
  "required": ["conflictId", "caseId", "fieldId", "cause", "candidateBindingIds", "status", "detectedAt"],
  "properties": {
    "conflictId": { "type": "string" },
    "caseId": { "type": "string" },
    "fieldId": { "type": "string" },
    "cause": { "type": "string", "enum": ["TIMING", "CORRECTION", "VERSION"], "description": "MISSING is not a Conflict cause. See the Section 3 note: a field with zero candidates goes straight to UNSUPPORTED with no Conflict record." },
    "candidateBindingIds": { "type": "array", "items": { "type": "string" }, "minItems": 2, "description": "Must reference Bindings from at least two different sourceDocIds with different candidateValue for the same fieldId." },
    "narrativeHint": { "type": "string", "description": "Short human-readable cause description, for S3. Canon example for F2/TIMING: 'Administrator cut off at 16:00, the call landed at 17:42.'" },
    "detectedByRunId": { "type": ["string", "null"] },
    "detectedAt": { "type": "string", "format": "date-time" },
    "status": { "type": "string", "enum": ["OPEN", "RESOLVED"] }
  },
  "additionalProperties": false
}
```

**Invariant that matters most:** a `Conflict` can never move to `status: RESOLVED` except as a side effect of a `Decision` record being created for the same `fieldId`. No automated process may resolve a conflict; that would be the system deciding, which CANON hard rule 1 forbids outright.

### 3.6 Decision

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kriseva.ai/attest/schema/decision.json",
  "title": "Decision",
  "type": "object",
  "required": ["decisionId", "caseId", "fieldId", "decisionType", "reason", "decidedByUserId", "decidedAt"],
  "properties": {
    "decisionId": { "type": "string" },
    "caseId": { "type": "string" },
    "fieldId": { "type": "string" },
    "conflictId": { "type": ["string", "null"], "description": "Set when resolving a CONFLICTED field. Null when confirming an UNSUPPORTED field, since MISSING fields carry no Conflict record." },
    "decisionType": { "type": "string", "enum": ["SELECT_CANDIDATE", "MANUAL_OVERRIDE", "CONFIRM_UNSUPPORTED"] },
    "selectedBindingId": { "type": ["string", "null"], "description": "Required when decisionType is SELECT_CANDIDATE, else null." },
    "decidedValue": { "type": ["number", "string", "null"], "description": "Null when decisionType is CONFIRM_UNSUPPORTED." },
    "reason": { "type": "string", "minLength": 1, "description": "CANON hard rule 2: non-empty, mandatory, always." },
    "decidedByUserId": { "type": "string", "description": "Must resolve to a registered human identity, e.g. priya.ramanathan. Never a runId or 'system'." },
    "decidedAt": { "type": "string", "format": "date-time" }
  },
  "additionalProperties": false
}
```

**Invariant that matters most:** `reason` is non-empty (server-side, not just client-side) and `decidedByUserId` must resolve to a human user record; the API in Section 4 rejects any request where either check fails, before anything is written.

### 3.7 Signoff

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kriseva.ai/attest/schema/signoff.json",
  "title": "Signoff",
  "type": "object",
  "required": ["signoffId", "caseId", "makerUserId", "checkerUserId", "decisionIdsConfirmed", "signoffStatement", "signoffAt"],
  "properties": {
    "signoffId": { "type": "string" },
    "caseId": { "type": "string" },
    "makerUserId": { "type": "string", "description": "The single decidedByUserId common to every Decision on this case. If more than one maker decided different fields, see Section 4 POST /signoff error responses." },
    "checkerUserId": { "type": "string" },
    "decisionIdsConfirmed": { "type": "array", "items": { "type": "string" }, "minItems": 1 },
    "signoffStatement": { "type": "string", "minLength": 1 },
    "signoffAt": { "type": "string", "format": "date-time" },
    "resultingCaseState": { "type": "string", "const": "SIGNED" }
  },
  "additionalProperties": false
}
```

**Invariant that matters most:** `checkerUserId` must not equal `makerUserId`, and must not equal any `decidedByUserId` recorded on any `Decision` referenced in `decisionIdsConfirmed` (CANON hard rule 4). This is enforced by the engine at write time, not by a UI hint; a request that violates it is rejected, not merely discouraged.

### 3.8 ManifestEntry

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kriseva.ai/attest/schema/manifest-entry.json",
  "title": "ManifestEntry",
  "type": "object",
  "required": ["caseId", "sequenceIndex", "entryType", "refId", "payloadHash", "previousEntryHash", "entryHash", "recordedAt"],
  "properties": {
    "caseId": { "type": "string" },
    "sequenceIndex": { "type": "integer", "minimum": 0, "description": "Strictly increasing per caseId, starting at 0. Never re-sorted." },
    "entryType": { "type": "string", "enum": ["SOURCE_DOC_INGESTED", "BINDING_CREATED", "CONFLICT_DETECTED", "DECISION_RECORDED", "SIGNOFF_RECORDED", "CASE_SEALED"] },
    "refId": { "type": "string", "description": "Id of the referenced object: sourceDocId, bindingId, conflictId, decisionId, signoffId, or caseId, matching entryType." },
    "payloadHash": { "type": "string", "pattern": "^[a-f0-9]{64}$", "description": "SHA-256 hex of the canonical JSON of the referenced object. See Section 8 for canonicalisation rules." },
    "previousEntryHash": { "type": "string", "pattern": "^[a-f0-9]{64}$", "description": "entryHash of sequenceIndex - 1, or 64 zero characters for sequenceIndex 0." },
    "entryHash": { "type": "string", "pattern": "^[a-f0-9]{64}$", "description": "SHA-256 hex of previousEntryHash + payloadHash + sequenceIndex + entryType + refId, concatenated in that exact order. See Section 8." },
    "recordedAt": { "type": "string", "format": "date-time" }
  },
  "additionalProperties": false
}
```

**Invariant that matters most:** `entryHash` must be recomputable at any time from `previousEntryHash`, `payloadHash`, `sequenceIndex`, `entryType` and `refId`, and doing so must reproduce the stored value exactly. A mismatch at any `sequenceIndex` means every entry from that point forward is unverifiable, by construction, not by a separate flag.

### 3.9 RunRecord

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kriseva.ai/attest/schema/run-record.json",
  "title": "RunRecord",
  "type": "object",
  "required": ["runId", "provider", "modelId", "mode", "promptHash", "latencyMs", "startedAt", "completedAt"],
  "properties": {
    "runId": { "type": "string" },
    "caseId": { "type": ["string", "null"] },
    "provider": { "type": "string", "enum": ["BEDROCK", "REPLAY"] },
    "modelId": { "type": "string", "description": "Read from environment at call time; confirmed live at the 11:00 Friday AWS briefing. Do not hardcode a specific id in the build; treat it as configuration.", "examples": ["<BEDROCK_MODEL_ID from env, confirmed at the 11:00 briefing>"] },
    "mode": { "type": "string", "enum": ["LIVE", "RECORDED"] },
    "promptHash": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
    "promptRef": { "type": ["string", "null"], "description": "Storage pointer to the full prompt text, e.g. runs/<runId>.prompt.txt." },
    "responseRef": { "type": ["string", "null"], "description": "Storage pointer to the raw response, e.g. runs/<runId>.response.txt." },
    "requestParams": { "type": "object", "properties": { "temperature": { "type": "number" }, "maxTokens": { "type": "integer" } }, "additionalProperties": true },
    "extractedBindingIds": { "type": "array", "items": { "type": "string" } },
    "latencyMs": { "type": "integer", "minimum": 0 },
    "startedAt": { "type": "string", "format": "date-time" },
    "completedAt": { "type": "string", "format": "date-time" },
    "replayOfRunId": { "type": ["string", "null"], "description": "Required when mode is RECORDED: the original LIVE runId this fixture re-serves verbatim." }
  },
  "additionalProperties": false
}
```

**Invariant that matters most:** `mode: "LIVE"` requires `provider: "BEDROCK"`, and `mode: "RECORDED"` requires `provider: "REPLAY"` plus a non-null `replayOfRunId`. No `RunRecord` may claim `LIVE` while actually served from `REPLAY`; this is the structural guarantee behind the honesty table's LIVE/RECORDED row and behind `UX_PSYCHOLOGY_SPEC.md` section 10's "no third, silent, unmarked default state" rule.

### 3.10 EvalItem

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kriseva.ai/attest/schema/eval-item.json",
  "title": "EvalItem",
  "type": "object",
  "required": ["evalItemId", "evalRunId", "caseId", "fieldCode", "expectedFieldState"],
  "properties": {
    "evalItemId": { "type": "string" },
    "evalRunId": { "type": "string", "description": "Groups all rows produced by one GET /eval/run execution." },
    "caseId": { "type": "string", "description": "One of the many generated synthetic cases in the eval corpus (Section 6), not only the canon Meridian Alpha case." },
    "fieldCode": { "type": "string" },
    "expectedFieldState": { "type": "string", "enum": ["SUPPORTED", "CONFLICTED", "UNSUPPORTED"], "description": "Ground truth, planted by the generator. DECIDED/CONFIRMED are excluded: those require a human and are not something the model is scored on producing." },
    "expectedValue": { "type": ["number", "string", "null"], "description": "Null when expectedFieldState is UNSUPPORTED." },
    "expectedSourceDocId": { "type": ["string", "null"] },
    "expectedSourceRegion": { "type": ["object", "null"] },
    "modelPredictedFieldState": { "type": ["string", "null"], "enum": ["SUPPORTED", "CONFLICTED", "UNSUPPORTED", null] },
    "modelPredictedValue": { "type": ["number", "string", "null"] },
    "modelPredictedBindingId": { "type": ["string", "null"] },
    "isExtractionCorrect": { "type": ["boolean", "null"], "description": "Applies when expectedFieldState is SUPPORTED. See Section 7." },
    "isAbstentionCorrect": { "type": ["boolean", "null"], "description": "Applies when expectedFieldState is CONFLICTED or UNSUPPORTED. See Section 7." },
    "isEvidenceLocalized": { "type": ["boolean", "null"] },
    "scoredAt": { "type": ["string", "null"], "format": "date-time" }
  },
  "additionalProperties": false
}
```

**Invariant that matters most:** `isExtractionCorrect` and `isAbstentionCorrect` are never both non-null for the same item. A ground-truth `SUPPORTED` item is scored only on extraction; a ground-truth `CONFLICTED` or `UNSUPPORTED` item is scored only on abstention. Conflating them into one "was it right" boolean is exactly the mistake Section 7 exists to prevent.

---

## 4. API surface

All eight endpoints from `CANON.md` section 9. Examples use canon numbers (`CANON.md` section 5) and stay short; a full response lists every field, not just the ones shown here.

### 4.1 `POST /ingest`

**Purpose:** register one or more `SourceDoc` records against a case, creating the case if it does not yet exist, moving case state to `INGESTED`.

Request:
```json
{
  "caseId": "CASE-2026-Q1-MER001",
  "fmeId": "FME-MERIDIAN-ALPHA",
  "schemeId": "SCHEME-MAOF-I",
  "reportingPeriodEnd": "2026-06-30",
  "sourceDocs": [
    {
      "docCode": "D1",
      "documentType": "ADMINISTRATOR_STATEMENT",
      "issuer": "Northwind Fund Services (IFSC) Private Limited",
      "version": 2,
      "cutoffAt": "2026-06-30T16:00:00+05:30",
      "issuedAt": "2026-07-08T00:00:00+05:30",
      "extractedText": "..."
    }
  ]
}
```

Success response, `201`:
```json
{
  "caseId": "CASE-2026-Q1-MER001",
  "state": "INGESTED",
  "sourceDocIds": ["DOC-D1V2-8f2a"],
  "syntheticLabel": "SYNTHETIC"
}
```

Error responses: `400` a source doc is missing a required field; `409` `caseId` already exists under a different `fmeId` or `schemeId` (cases are never silently merged).

**Invariant enforced:** ingest is append-only. Re-ingesting the same `docCode` and `version` is idempotent (returns the existing record). A new `version` (D1 v1 to v2) always creates a new `SourceDoc` row with `supersedesDocId` set; it never overwrites the prior row (Section 3.3).

### 4.2 `POST /extract`

**Purpose:** run the model provider over a case's ingested documents to propose field values, creating `Binding` and `Conflict` records, moving case state `INGESTED` to `EXTRACTED`.

Request:
```json
{ "caseId": "CASE-2026-Q1-MER001", "provider": "BEDROCK", "fieldCodes": ["F1", "F2", "F3", "F4"] }
```

Success response, `200`:
```json
{
  "caseId": "CASE-2026-Q1-MER001",
  "state": "EXTRACTED",
  "runId": "RUN-8841",
  "mode": "LIVE",
  "fields": [
    { "fieldCode": "F2", "state": "CONFLICTED", "candidateCount": 2 },
    { "fieldCode": "F4", "state": "UNSUPPORTED", "candidateCount": 0 }
  ]
}
```

Error responses: `404` case not found or not in `INGESTED` state; `422` a referenced source document has no extractable text; `502` the model provider call failed and no `ReplayProvider` fallback is configured.

**Invariant enforced:** extraction only ever writes `Binding` and `Conflict` records and moves a `Field` to `SUPPORTED`, `CONFLICTED` or `UNSUPPORTED`. There is no code path from `/extract` to a `Decision` write (CANON hard rule 1, enforced structurally, not by convention).

### 4.3 `GET /case/:id`

**Purpose:** read full case, field, binding and conflict state, to render S1 through S7.

Success response, `200` (trimmed):
```json
{
  "caseId": "CASE-2026-Q1-MER001",
  "state": "UNDER_REVIEW",
  "fields": [
    { "fieldCode": "F1", "state": "DECIDED", "decidedValue": 42500000 },
    { "fieldCode": "F2", "state": "CONFLICTED", "candidateCount": 2 }
  ]
}
```

Error responses: `404` case not found.

**Invariant enforced:** this call has no side effects. It may be polled repeatedly, including during a live pitch, without changing anything it returns.

### 4.4 `POST /decide`

**Purpose:** record one named human's decision on one field.

Request:
```json
{
  "caseId": "CASE-2026-Q1-MER001",
  "fieldCode": "F2",
  "decisionType": "SELECT_CANDIDATE",
  "selectedBindingId": "BIND-F2-D3-91c",
  "reason": "Ledger candidate reflects the capital call that landed at 17:42 IST, after the administrator's 16:00 cut-off. Confirmed against the call notice.",
  "decidedByUserId": "priya.ramanathan"
}
```

Success response, `200`:
```json
{ "fieldCode": "F2", "state": "DECIDED", "decisionId": "DEC-4471", "decidedValue": 19300000 }
```

Error responses: `400` empty or whitespace-only `reason`; `404` field or `selectedBindingId` not found; `409` field already `DECIDED` or `CONFIRMED`, or `decidedByUserId` does not resolve to a registered human identity.

**Invariant enforced:** `reason` is mandatory and non-empty; the decider must be a named human, never a `runId` or `"system"` (CANON hard rules 1 and 2).

### 4.5 `POST /signoff`

**Purpose:** a second named human confirms every decided field; case moves `UNDER_REVIEW` to `SIGNED`.

Request:
```json
{
  "caseId": "CASE-2026-Q1-MER001",
  "checkerUserId": "rajiv.menon",
  "signoffStatement": "I confirm the above decisions as Principal Officer for Meridian Alpha Capital IFSC Private Limited."
}
```

Success response, `200`:
```json
{ "caseId": "CASE-2026-Q1-MER001", "state": "SIGNED", "signoffId": "SGN-1120", "fieldsConfirmed": 4 }
```

Error responses: `409` `checkerUserId` equals any `decidedByUserId` already recorded on this case (maker-checker violation); `409` at least one field is still `CONFLICTED` or `UNSUPPORTED`; `404` case not found.

**Invariant enforced:** checker never equals maker, on any field, and every field must be `DECIDED` first (CANON hard rules 3 and 4).

### 4.6 `GET /manifest/:id`

**Purpose:** retrieve the ordered `ManifestEntry` chain for a case and the computed receipt. Readable at any point after the case exists, not only after sealing; is closed to further appends once a `CASE_SEALED` entry is written.

Success response, `200` (trimmed):
```json
{
  "caseId": "CASE-2026-Q1-MER001",
  "entries": [
    { "sequenceIndex": 0, "entryType": "SOURCE_DOC_INGESTED", "entryHash": "3f1a...c9" },
    { "sequenceIndex": 1, "entryType": "BINDING_CREATED", "entryHash": "7b02...4e" }
  ],
  "latestEntryHash": "7b02...4e",
  "verified": true,
  "hashAlgorithm": "SHA-256"
}
```

Error responses: `404` case or manifest not found.

**Invariant enforced:** `verified` is computed fresh on every read by recomputing the chain from `sequenceIndex` 0 forward (Section 8); it is never a stored flag that could go stale.

### 4.7 `GET /replay/:id`

**Purpose:** re-serve a previously recorded model call deterministically, given a `runId`. Never re-invokes the live provider, even if live credentials are present.

Success response, `200` (trimmed):
```json
{ "runId": "RUN-8841", "mode": "RECORDED", "modelId": "<recorded model id>", "promptHash": "a41c...02", "latencyMs": 1180, "replayed": true }
```

Error responses: `404` no such `runId`; `500` recorded fixture missing or corrupt.

**Invariant enforced:** the replayed response is byte-identical to what was originally recorded for that `runId`. This is what makes offline demo insurance and the judge-facing replay panel trustworthy rather than merely convenient.

### 4.8 `GET /eval/run`

**Purpose:** execute the eval harness over the labelled synthetic set and return the scoring table (Section 7).

Request: `GET /eval/run?setId=EVAL-SET-2026-08-18&provider=REPLAY`

Success response, `200` (trimmed, see Section 7 for the full table shape):
```json
{
  "evalRunId": "EVALRUN-0091",
  "itemCount": 64,
  "metrics": {
    "fieldPrecision": { "numerator": null, "denominator": null, "value": null },
    "abstentionRate": { "numerator": null, "denominator": null, "value": null }
  }
}
```

Error responses: `400` unknown `setId`; `503` a harness run is already in progress.

**Invariant enforced:** every metric ships with its numerator and denominator, never a bare percentage (Section 7). The corpus is small enough (50 to 100 items) that this call runs synchronously; it does not need a job-polling pattern in a 22-hour build.

---

## 5. The seven screens

Functional acceptance checks only: data correctness and enforced behaviour. Visual layout, colour, motion and copy are `UX_PSYCHOLOGY_SPEC.md` section 12's job for the same seven screens; each entry below points to its matching subsection there rather than repeating it. Rubric weights are `FACT_CARD.md` H3: Technical Execution & Architecture 30, Founder & Venture Assessment 30, Problem Depth & Regulatory Realism 20, Honesty & Roadmap Credibility 20.

A sequencing note that governs S1 and the live demo together, derived from combining `CANON.md` sections 8 and 10 with the pitch timing in doc 03 section 2: the live demo (under 70 seconds) walks exactly one field through the full spine, ingest to sealed tamper-check, end to end. `CANON.md`'s F2 (drawn capital, TIMING cause) is the field CANON itself calls out as "the field that proves the whole thesis," and is the recommended choice for that single live pass. The other three canon fields (F1, F3, F4) should already sit in varied states before the dashboard is first shown on stage, so that S1's own claim, "four fields, four different states, at a glance," is true at first sight rather than only after several minutes of live resolution. Build the case-seeding path (via the generator, Section 6, not a special API) so a rehearsal can start from a dashboard already showing a mix of `CONFLICTED`, `UNSUPPORTED`, `DECIDED` and `CONFIRMED`, with `F2` held back in `CONFLICTED` for the live resolution.

### S1: Case dashboard

**Purpose:** four fields, four different states, at a glance. Status is the product.
**On it:** case identity, reporting period, a case-state stepper (`Ingested -> Extracted -> Under review -> Signed -> Sealed`), one row of four field cards.
**States rendered:** all five `Field.state` values are possible across the four cards simultaneously; the case-state stepper reflects `Case.state`.
**The one thing a juror must see:** at a glance, without reading body text, which fields are resolved and which still need a human.
**Rubric:** primary, Technical Execution & Architecture (the product runs, live). Secondary, Founder & Venture Assessment (this screen is the whole defensible claim in one view).
**See also:** `UX_PSYCHOLOGY_SPEC.md` section 12, S1, for layout, the von Restorff isolation treatment on CONFLICTED/UNSUPPORTED cards, and its own three visual acceptance checks.

Acceptance checks:
1. The dashboard renders exactly the four fields on the case: committed capital, drawn capital, closing NAV, complaints closed during the quarter.
2. Each card shows its `fieldCode`, label, and `state`, with `CONFLICTED` cards additionally showing their `cause` (TIMING, CORRECTION or VERSION) and `UNSUPPORTED` cards showing MISSING, per Section 3's note that MISSING is a distinct state, not a fourth conflict cause.
3. Before any live resolution, the four cards do not all share one state; at least three distinct `Field.state` values are visible at once.
4. The case-level state is shown once, separate from the four per-field states, never merged into the same visual element.
5. The word "synthetic" is visible on this screen without scrolling.
6. No card ever shows "0," a blank cell or a dash as a stand-in value for `UNSUPPORTED`; it shows the explicit no-value state with its reason.

### S2: Evidence workspace

**Purpose:** every proposed value is pinned to the exact source region it came from.
**On it:** breadcrumb (case, field), candidate list (source doc id, version, value, cut-off timestamp), source document viewer with the region highlighted.
**States rendered:** `SUPPORTED` shows one candidate; `CONFLICTED` shows two or more, selectable; `UNSUPPORTED` shows an explicit empty-evidence state, never a blank pane.
**The one thing a juror must see:** a number on screen that traces, by a visible click, to the literal text it came from.
**Rubric:** primary, Technical Execution & Architecture (real extraction, real binding). Secondary, Problem Depth & Regulatory Realism (evidence-grade traceability is what a compliance officer actually needs).
**See also:** `UX_PSYCHOLOGY_SPEC.md` section 12, S2.

Acceptance checks:
1. Every candidate value shown carries its `sourceDocId`, `version`, and the exact `sourceRegion` (page plus character span) it was read from.
2. Clicking a candidate moves the highlighted region in the document viewer to that candidate's `sourceRegion`.
3. For F4 (`UNSUPPORTED`), the screen states explicitly that no source document contains the field, and names which documents were checked, rather than rendering an empty or blank value.
4. No numeric value appears anywhere on this screen without a visible link to at least one `SourceDoc`, except the explicit zero-candidate `UNSUPPORTED` state.
5. Each candidate shows the `asOf` cut-off timestamp of the document it came from, so a reviewer can see why two numbers differ without leaving the screen.

### S3: Conflict decision

**Purpose:** both candidates stay visible. No default winner. Reason is mandatory.
**On it:** shared context line (the two cut-offs or versions in conflict), two (or more) equal-weight candidate cards, a mandatory reason field, decider identity, submit control. Per `UX_PSYCHOLOGY_SPEC.md` section 5.3, this is a full-width in-place panel entered by a "Review" action from a `CONFLICTED` or `UNSUPPORTED` card on S1 or S2, not a separate nav destination.
**States rendered:** field state moves from `CONFLICTED` or `UNSUPPORTED` to `DECIDED` on submit.
**The one thing a juror must see:** two real, disagreeing numbers, neither one pre-picked, with a name attached to whichever one gets chosen.
**Rubric:** primary, Problem Depth & Regulatory Realism (this is the realism thesis, made interactive). Secondary, Honesty & Roadmap Credibility (no fabricated confidence score substitutes for a human's reason).
**See also:** `UX_PSYCHOLOGY_SPEC.md` section 12, S3, and section 2.2 on why nothing is pre-selected.

Acceptance checks:
1. For a `CONFLICTED` field, all candidates render with equal visual weight; none is pre-selected, checked, or listed with implied precedence (candidates order by `sourceDocId`, a neutral rule, never by recency or by which value is larger).
2. The reason field is required; submitting with an empty or whitespace-only reason is rejected both client-side and server-side, and no `Decision` record is written.
3. Each candidate is labelled with its `sourceDocId` and `asOf` cut-off, so the reviewer can see the cause without leaving the screen.
4. Submitting requires selecting a named, logged-in human identity; there is no path that records a decision as made by a model, a `runId`, or "system."
5. After submit, the field visibly moves to `DECIDED`, and the chosen candidate plus the full reason text remain permanently visible on this screen, not only in a database.
6. No numeric confidence score is ever shown as a basis for picking a candidate; if a confidence value is shown at all, it is informational only and cannot substitute for the reason field.

### S4: Agent trace

**Purpose:** the model call is real and inspectable: model id, prompt hash, latency, LIVE or RECORDED badge.
**On it:** a LIVE/RECORDED summary band, then a reverse-chronological log of `RunRecord`s, each with model id, prompt hash, latency, mode.
**States rendered:** every row is either `LIVE` or `RECORDED`; a `RECORDED` row states which original `LIVE` run it replays.
**The one thing a juror must see:** a badge that says whether this specific call actually happened just now, and proof it isn't decorative.
**Rubric:** primary, Technical Execution & Architecture (proves real AWS Bedrock usage, not a canned demo). Secondary, Honesty & Roadmap Credibility (the LIVE/RECORDED distinction, disclosed on screen rather than only asserted on stage).
**See also:** `UX_PSYCHOLOGY_SPEC.md` section 12, S4, and section 10 on the LIVE/RECORDED indicator.

Acceptance checks:
1. Every run shown displays `modelId`, `promptHash`, `latencyMs`, and a `LIVE` or `RECORDED` badge; there is no third, unmarked default.
2. The badge value is read from `RunRecord.mode`, never inferred from context or hardcoded in the UI.
3. Clicking a run reveals the full prompt and response, or a working link to both (`promptRef` / `responseRef`).
4. A `RECORDED` row shows its `replayOfRunId`, so a juror can trace a fixture back to the real call it came from.
5. No run can display `mode: LIVE` with `provider: REPLAY`, or the reverse (Section 3.9's invariant, made visible here).

### S5: Risk and anomaly board

**Purpose:** deterministic indicators, each closed only by a named disposition.
**On it:** a table of indicators (rule name, description, severity, disposition, assigned reviewer); open rows sort first.
**States rendered:** each row is `OPEN` or `CLOSED`; `CLOSED` requires a named reviewer and a note.
**The one thing a juror must see:** an anomaly that cannot be dismissed by anyone unnamed.
**Rubric:** primary, Problem Depth & Regulatory Realism (named disposition mirrors how a real risk function actually operates).
**See also:** `UX_PSYCHOLOGY_SPEC.md` section 12, S5. Per doc 04's cut list (Section 12 below), this screen's depth is the second thing to cut under time pressure; keep the table, cut per-row inline expansion first if squeezed.

Acceptance checks:
1. Every indicator names the deterministic rule that produced it, not only a free-text model explanation.
2. Closing an indicator requires a named human reviewer and a non-empty note; there is no bulk "dismiss all" or auto-close action anywhere in the API or the UI.
3. Open and closed rows are visually distinguishable without relying on colour alone (icon and label, per `UX_PSYCHOLOGY_SPEC.md` section 3.4's redundant-encoding rule).
4. Each closed row shows who closed it and when, visible on this screen or one click away.

### S6: Sign-off

**Purpose:** two different named humans, enforced separation.
**On it:** case summary (fund, period, the fields in their final `DECIDED` state), a maker block (read-only once complete) and a checker block (active input).
**States rendered:** case moves `UNDER_REVIEW` to `SIGNED`.
**The one thing a juror must see:** the system physically refusing to let one person play both roles.
**Rubric:** primary, Problem Depth & Regulatory Realism (mirrors `FACT_CARD.md` B1: both officers mandated by IFSCA, the signature is personal). Secondary, Founder & Venture Assessment (accountability is the sellable wedge).
**See also:** `UX_PSYCHOLOGY_SPEC.md` section 12, S6.

Acceptance checks:
1. The screen requires two different identities: the maker(s) already recorded on the case's `Decision`s, and a separate checker for signoff itself.
2. Attempting to sign off with a checker identity matching any decider identity on the case is rejected with a specific, visible message (the copy bank's maker-checker line), never a silent no-op.
3. Sign-off is blocked, with the specific blocking field named, while any field on the case is still `CONFLICTED` or `UNSUPPORTED`.
4. Once signed, both named humans and the signoff timestamp are simultaneously visible, permanently, on this screen.
5. Signoff is one deliberate, un-mistakable control, not a state that can change as a side effect of any other action.

### S7: Receipt and manifest

**Purpose:** portable, hash-sealed, and it breaks visibly when tampered with.
**On it:** the manifest table (artifact, hash, linked transition), the hash-chain visualisation, a "Verify chain" action, export actions, the full-form synthetic disclosure line.
**States rendered:** sealed (every link verified) to tamper-checked-and-broken.
**The one thing a juror must see:** a single altered byte breaking the chain, visibly, at the exact point of the alteration.
**Rubric:** primary, Technical Execution & Architecture (real SHA-256 chain engineering). Secondary, Honesty & Roadmap Credibility (the tamper-evidence claim is proven on screen, not asserted in the pitch).
**See also:** `UX_PSYCHOLOGY_SPEC.md` section 12, S7, and section 2.7 on why this screen is built as the demo's peak and its end.

Acceptance checks:
1. The receipt shows a single latest chain hash, copyable, plus the full ordered `ManifestEntry` list beneath it.
2. An exportable version of the receipt exists and carries enough information (every entry hash, in order) to re-verify the chain independently, outside the app.
3. Running "Verify chain" against an unmodified, sealed case returns `verified: true`.
4. Editing even one character of one already-sealed artifact and re-running "Verify chain" returns `verified: false` and names the first `sequenceIndex` where the chain breaks, not just a generic "invalid."
5. "SHA-256" is stated visibly on the screen itself, not only in code.
6. The synthetic disclosure sentence and the `caseId` both appear on the exported receipt file itself, not only in the surrounding app.

---

## 6. Synthetic data generation rules

Full field-by-field generation spec, document templates and CSV column layout belong in `SCHEMA_PACK.md`, named as the detailed source in doc 04 section 5. It does not yet exist in `factory/` as of this writing; this section is self-contained until it lands. Doc 04 section 2 item 2 sets the target: schemas as documents this week, generator written live Friday, under 45 minutes with the playbook.

**The canon case.** One case, `CASE-2026-Q1-MER001`, generated with the exact entities, documents and numbers fixed in `CANON.md` sections 1 through 5: FME Meridian Alpha Capital IFSC Private Limited, scheme Meridian Alpha Opportunities Fund I, administrator Northwind, custodian Sentinel, four source documents D1 to D4, four fields F1 to F4. This case is never randomised; its numbers are memorised for the pitch (`FACT_CARD.md` and `CANON.md` section 5) and must come out of the generator byte-identical every run.

**The eval corpus.** `GET /eval/run` needs 50 to 100 labelled items (doc 04 section 3). One case yields only four. The generator must additionally produce roughly 15 to 25 further synthetic fixture cases, each with a handful of fields, spanning ground-truth `SUPPORTED` (clean, single source, no trap), `CONFLICTED` (one of the three planted causes below, picked at random per field), and `UNSUPPORTED` (no source carries it). Every generated field gets its ground-truth `EvalItem` row written alongside the documents, at generation time, not inferred afterward, since the generator is the thing planting the conflict and therefore already knows the answer.

**Determinism.** A single fixed random seed, checked into the generator's config, must reproduce the entire fixture set (canon case plus eval corpus) byte-for-bit identical on every run. This is what lets Thursday's rehearsal, Friday's live build, and the `ReplayProvider` fixtures all agree with each other.

**Format.** Monetary fields are whole USD integers, no cents; every canon number in `CANON.md` section 5 is already a round figure. Timestamps are ISO 8601 with an explicit offset (`+05:30` for IST, matching CANON's own "17:42 IST" style). Documents are generated as structured plain text (per Section 3's source-region decision), not scanned images or rendered PDFs, so no OCR or bounding-box layer is needed anywhere in the build.

### The planted-conflict matrix

Reproduced from `CANON.md` section 6 because the build depends on it directly. Four distinct causes, on purpose; the build must make all four look visibly different, not one state relabelled four times (`UX_PSYCHOLOGY_SPEC.md` section 3.4 gives the exact icon and border treatment per cause).

| Cause | Field | The two stories | What a silent AI does | What ATTEST does | The line to say on stage |
|---|---|---|---|---|---|
| TIMING | F2 | Administrator cut off at 16:00, the call landed at 17:42 | Picks one, usually the administrator, because it looks authoritative | Abstains, shows both with their cut-off timestamps, makes the human choose | "Both documents are correct. That is the point. There is no algorithm that resolves this, only a person who knows what happened that afternoon." |
| CORRECTION | F3 | Administrator restated on 8 July, the ledger predates the restatement | Picks the higher or the more recent file, with no idea a restatement occurred | Abstains, surfaces that D1 is version 2 and D3 derives from version 1 | "The machine cannot know there was a correction. It can only know the two numbers disagree, and say so." |
| VERSION | F1 | Register counts a subscription that is signed but not counter-executed | Averages, or takes the register because it is the primary record | Abstains, shows both with exact source regions | "The register is not wrong. It is answering a different question." |
| MISSING | F4 | No document contains the field at all | Produces a plausible number, most commonly zero | Produces nothing, marks UNSUPPORTED, blocks sign-off until a human resolves it | "Zero is the most dangerous answer in regulatory reporting, because it looks like an answer." |

For the eval corpus beyond the canon case, the generator assigns one of TIMING, CORRECTION or VERSION to each planted `CONFLICTED` field (never a fifth invented cause), and reuses the same MISSING pattern for planted `UNSUPPORTED` fields: an eval item whose field genuinely has zero source candidates.

---

## 7. Eval protocol and scoring

Measures extraction correctness and abstention correctness separately, per doc 04 section 3. A model that silently picks one of two disagreeing values is a failure on this product's own terms even if the picked value happens to be correct, because the design goal is refusing to decide silently, not guessing well.

**The rule:** no headline accuracy number is ever reported without its denominator visible next to it, on the same table, at the same time. This applies to every metric below, to the pitch slide, and to any verbal claim on stage (`FACT_CARD.md`'s own banned list: "any accuracy percentage for ATTEST that is not on the eval slide with its denominator visible").

**Seven metrics, each with what it measures and its denominator:**

| Metric | What it measures | Denominator |
|---|---|---|
| Field precision | Of fields the model resolved to a single confident `SUPPORTED` value (did not abstain), the fraction whose value exactly matches ground truth | Count of items where `modelPredictedFieldState = SUPPORTED` |
| Field recall | Of fields whose ground truth is genuinely `SUPPORTED`, the fraction the model correctly proposed (right value, right state), rather than mis-abstaining or mis-extracting | Count of items where `expectedFieldState = SUPPORTED` |
| Evidence-localisation success | Of fields where the model produced any candidate, the fraction whose `Binding.sourceRegion` overlaps the ground-truth region in the correct document | Count of items where the model produced at least one candidate |
| Coverage | Of all eval items, the fraction the model produced any state for at all, versus erroring out or timing out | Total eval items in the run |
| Abstention rate | Of all eval items, the fraction the model did not resolve to a single confident `SUPPORTED` value (ended `CONFLICTED` or `UNSUPPORTED`) | Total eval items scored |
| Conflict-detection recall | Of fields whose ground truth is genuinely `CONFLICTED` or `UNSUPPORTED` (should be abstained), the fraction the model correctly abstained on, rather than silently emitting one confident value | Count of items where `expectedFieldState` is `CONFLICTED` or `UNSUPPORTED` |
| Human-override rate | Of fields that reached `DECIDED`, the fraction where the human's `decisionType` was `MANUAL_OVERRIDE` rather than `SELECT_CANDIDATE`, i.e. the human's answer was not one of the model's own candidates | Count of `Decision` records on the case |

A note on abstention rate specifically, since it reads counter-intuitively: a high abstention rate is not automatically good or bad by itself. It only means something when read against conflict-detection recall. High abstention with high conflict-detection recall is the product working as designed. High abstention with low conflict-detection recall means the model is abstaining on fields it should be confident about, which is its own kind of failure (poor field recall), just a safer one than a silent wrong answer.

**The exact output table the pitch shows**, produced by `GET /eval/run` and rendered on one slide:

| Metric | Numerator | Denominator | Value |
|---|---|---|---|
| Field precision | n | N | n/N |
| Field recall | n | N | n/N |
| Evidence-localisation success | n | N | n/N |
| Coverage | n | N | n/N |
| Abstention rate | n | N | n/N |
| Conflict-detection recall | n | N | n/N |
| Human-override rate | n | N | n/N |

The `n` and `N` columns are placeholders in this document on purpose. They are filled in only after the M4 harness run (doc 04 section 6) actually executes against the real fixture corpus; nothing in this document invents a plausible-looking number ahead of that run, consistent with `FACT_CARD.md` K3's own caution about a check-count claim that was said before it was verified.

---

## 8. Manifest and hash spec

Algorithm: **SHA-256** throughout, hex-encoded, lower case.

**What gets hashed.** Every `SourceDoc`, `Binding`, `Conflict`, `Decision` and `Signoff` object, plus the `CASE_SEALED` event itself, in its canonical JSON form (below). One `ManifestEntry` is appended per object, at the moment that object is created, not batched at the end.

**Canonical JSON, so the same object always hashes the same way:**
1. UTF-8 encoding.
2. Object keys sorted lexicographically at every nesting level.
3. No insignificant whitespace.
4. Numbers serialised as plain decimal (monetary values are whole-dollar integers per Section 6; no floating-point ambiguity to resolve).
5. Date-times as ISO 8601 strings with an explicit offset, never a bare `Z`-less local time.

**Canonical order.** Strict chronological append order, by `sequenceIndex`, per `caseId`. Never re-sorted by artifact type, never re-sorted alphabetically, never re-sorted for display. The chain's integrity depends on this order being the literal order things happened.

**How the chain links.** For entry at `sequenceIndex = i`:
1. `payloadHash` = SHA-256 of the canonical JSON of the referenced object.
2. `previousEntryHash` = the `entryHash` of `sequenceIndex = i - 1`, or 64 zero characters (`"0"` repeated 64 times) when `i = 0` (the genesis entry).
3. `entryHash` = SHA-256 of the concatenation, in this exact order: `previousEntryHash`, `payloadHash`, `sequenceIndex` (as a plain decimal string), `entryType`, `refId`.

**What the receipt contains** (`GET /manifest/:id`, S7 export): `caseId`, the latest `entryHash` (the "root hash" shown large on S7), the full ordered `entries` array, `sealedAt`, `syntheticLabel: "SYNTHETIC"`, and `hashAlgorithm: "SHA-256"` stated explicitly, not just implied by the hex length.

**How the tamper check works.** On `GET /manifest/:id` or S7's "Verify chain" action: recompute `payloadHash` for every referenced artifact from its currently stored state, then recompute `entryHash` for every entry from `sequenceIndex = 0` forward using step 3 above, comparing each recomputed value against the stored one.

**What breaks, and how it is visible.** The first `sequenceIndex` whose recomputed `payloadHash` or `entryHash` no longer matches the stored value is the tamper point. `verified` flips to `false`, and the response names that exact `sequenceIndex`, its `entryType` and its `refId`, not a generic "invalid" flag. Every entry after that index also fails verification in the same pass, because each one's `previousEntryHash` depends on the one before it: this is the real, structural behaviour of a hash chain, not a stylised approximation of one, and matches `UX_PSYCHOLOGY_SPEC.md` section 6.2's requirement that "every link after the break also flags unverifiable in the same motion pass, because that is how a hash chain actually behaves."

**Algorithm-agility note.** The receipt states its algorithm explicitly (`hashAlgorithm: "SHA-256"`) precisely so a future version could move to a different digest without changing the chain's structure. This build hashes with SHA-256 today; nothing here is a cryptographic claim beyond that, and no stronger claim ("tamper-proof," "immutable") is made anywhere in the product, per `FACT_CARD.md`'s banned list.

---

## 9. AWS deployment steps

Full command-by-command runbook: `AWS_RUNBOOK.md` (34KB, exists in `factory/`). This section summarises the decision, the priority-ordered service list, and the Bedrock fallback; use the runbook itself for exact CLI, the IAM policy JSON, the troubleshooting table and the placeholder list.

**The account decision** (`AWS_RUNBOOK.md` section 0). Build against the event-provided AWS account and credits as primary, because the Technical Execution rubric line reads "met core track requirements using provided AWS credits" and that phrase is graded text. Kriseva's own AWS account (USD 1,100 in startup credits, Bedrock access: ZERO Anthropic models (all 15 agreement-blocked as at 2026-08-19). Amazon Nova and 74 other models usable now) is a pre-warmed, Thursday-tested hot standby, not the build target. Switch to standby only on an explicit trigger: event credentials fail identity verification within 60 minutes of the 11:00 briefing, or Bedrock access breaks mid-sprint with no mentor fix inside 30 minutes. The event account only offering Sonnet-class or one model family is explicitly **not** a trigger to switch; take the strongest `AUTHORIZED` model available and move on. If the trigger fires, say so on stage, in the honesty table; hiding an account switch is the wrong trade.

**Service list, priority order** (synthesising doc 04 section 3's cut-from-the-bottom list with `AWS_RUNBOOK.md`'s actual build sequence):

1. **Least-privilege IAM app identity** (`kriseva-attest-app`, or an assumed role if the event account blocks IAM user creation), scoped to Bedrock invoke/discovery actions and read/write on the app's own S3 bucket only. Must exist before the app touches AWS as itself, separate from the human operator's own credentials.
2. **S3 bucket for manifests and fixtures**, versioning enabled, public access fully blocked (reachable only through signed requests from the app's own IAM identity). Object Lock only if the 11:00 briefing confirms the event account's permission set actually grants it (a bucket-level, set-once-at-creation choice); `GOVERNANCE` retention mode, not `COMPLIANCE`, since compliance mode cannot be undone by anyone including root, which is too rigid for a 22-hour build. If Object Lock is not confirmed in time, proceed on versioning alone and disclose that honestly in the honesty table.
3. **Bedrock model access verification and one real Converse call**: list foundation models in the working region, check `authorizationStatus` per candidate strongest-first, and run one Converse call before anyone leaves the briefing room. Claude family is first choice by product design; Nova is a legitimate fallback, not a downgrade to apologise for.
4. **Cost control**: a budget alarm at 50 percent of credits, notifying the founder by email. No spend beyond provided credits without founder sign-off, before it happens, not after.
5. **Static hosting**, ranked and each with an abandon point (`AWS_RUNBOOK.md` section 6): S3 plus CloudFront primary (abandon if not `Deployed` within 20 minutes, or two consecutive 403s survive a policy fix); S3 website hosting alone as fallback (abandon past 10 minutes fighting a name collision); small compute (App Runner or EC2) only if the backend itself must be reachable, abandoned if not verified reachable by hour 19. Localhost is an acceptable floor: the rubric asks whether AWS credits met core requirements, not whether the address bar shows an AWS domain, and hosting is the lowest-priority AWS line item by design.
6. **CloudTrail**, left on, filtered to Bedrock and S3 events during the sprint window, as an audit-trail talking point that mirrors the product's own pitch: proof of who did what, when.

**The fallback if Bedrock access does not land** (`AWS_RUNBOOK.md` section 8, doc 03 worst case 2). Every live call, including Thursday's own pre-warm success on Kriseva's account, is already recorded to `runs/*.jsonl`. If live Bedrock access disappears at any point, `ReplayProvider` re-serves those recorded fixtures deterministically: one environment variable flip, not new engineering under pressure, because the `ModelProvider` abstraction (doc 04 section 3) was built this way from hour 0 regardless of how the Bedrock story goes. On stage, say plainly: "This run is replayed from a recorded Bedrock call we made earlier on our own AWS account. We are showing you the identical prompt, response and latency we captured live," and show the `RECORDED` badge, never bury it. Even in total Bedrock failure, the versioned S3 bucket with the manifest chain actually stored in it, plus the least-privilege IAM identity actually used to read and write it, plus the budget alarm and CloudTrail if reached, are genuine, inspectable AWS usage under "provided credits," not a consolation prize.

`AWS_RUNBOOK.md` carries its own two open founder decisions (overspend sign-off mechanism during the overnight window; comfort building on a possibly shared event account) in its final section; they are not repeated here to avoid the two copies drifting apart.

---

## 10. Demo script mapping

Shot-by-shot detail (narration lines, per-step failure fallback) belongs in `DEMO_STORYBOARD.md`, named as the detailed source in the war room prep prompt. It does not yet exist in `factory/` as of this writing. This table is the load-bearing summary until it lands: every beat, which screen it runs on, the specific pitch claim it proves, and the rubric line it scores, built from `CANON.md` section 10's demo spine (never cut) and doc 03 section 2's pitch skeleton.

| Demo beat | Screen | Pitch claim it proves | Rubric criterion |
|---|---|---|---|
| Cold open: the wound | none, spoken | "The committed-capital number exists in three documents, and they disagree. An AI tool picks one silently." | Problem Depth & Regulatory Realism |
| Ingest two conflicting documents | S1, then S2 | The system reads real, structured source documents, not a hardcoded answer | Technical Execution & Architecture |
| Model proposes with source pins | S2, S4 | Live Bedrock extraction in the demo, not canned; every value traces to evidence | Technical Execution & Architecture |
| Hits the conflict, abstains | S3 | CANON's TIMING line: "Both documents are correct. That is the point. There is no algorithm that resolves this, only a person who knows what happened that afternoon." | Problem Depth & Regulatory Realism (primary), Honesty & Roadmap Credibility (secondary) |
| Named human decides, with reason | S3 | "A named human owns every judgement" | Founder & Venture Assessment |
| Maker-checker signs | S6 | The whole trail is sealed under enforced two-person accountability, mirroring `FACT_CARD.md` B1 | Problem Depth & Regulatory Realism (primary), Founder & Venture Assessment (secondary) |
| Seal | S7 | A real, hash-sealed receipt, not a decorative badge | Technical Execution & Architecture |
| Tamper attempt breaks the seal, visibly | S7 | Tamper-evidence proven on screen, not asserted in the pitch | Honesty & Roadmap Credibility (primary), Technical Execution & Architecture (secondary) |
| Why us, why now | none, pitch slide | Registered company, prior public prototype, built clean in 22 hours on AWS; market and why-now figures as stated, with confidence hedges, in `FACT_CARD.md` sections 1 to 2 | Founder & Venture Assessment |
| Business, honesty and the ask | honesty table, README plus pitch slide | The SYNTHETIC/MOCKED/LIVE table (`REPO_FIRST_COMMIT_PACK.md` section 3), buyer persona, pricing stated as hypothesis, residency ask | Honesty & Roadmap Credibility (primary), Founder & Venture Assessment (secondary) |

---

## 11. Test plan

**Invariants worth testing.** Every one of these is already named as "the invariant that matters most" for some schema in Section 3; this is the consolidated list:

1. A model- or system-authored `Decision` is impossible: `decidedByUserId` must resolve to a registered human, never a `runId` or `"system"`.
2. `Decision.reason` is non-empty; empty or whitespace-only is rejected server-side, not just in the UI.
3. `POST /signoff` is rejected while any field on the case is still `CONFLICTED` or `UNSUPPORTED`.
4. `POST /signoff` is rejected when `checkerUserId` equals any `decidedByUserId` already recorded on the case.
5. Mutating one byte of one already-sealed artifact and re-running the tamper check flips `verified` from `true` to `false` and identifies the first broken `sequenceIndex`.
6. A `RunRecord` can never have `mode: LIVE` with `provider: REPLAY`, or the reverse.
7. A `Conflict` requires at least two `candidateBindingIds` from different `sourceDocId`s with differing `candidateValue` for the same `fieldId`.

**The five tests that must exist even if everything else is cut.** These map one to one onto `CANON.md` section 7's own five hard rules, which is a deliberate choice: CANON already names these as "the hard rules the engine enforces and the demo shows," so the minimum test suite is exactly a machine-checked version of that list, nothing added, nothing left out.

1. Test: a decision attempt where the decider identity is a `runId` or `"system"` is rejected. (Hard rule 1: a model may propose, never decide.)
2. Test: a decision attempt with an empty `reason` is rejected and no `Decision` record is written. (Hard rule 2.)
3. Test: a signoff attempt while a field is still `CONFLICTED` or `UNSUPPORTED` is rejected. (Hard rule 3.)
4. Test: a signoff attempt where the checker matches the maker is rejected. (Hard rule 4.)
5. Test: tampering with one sealed artifact is detected, and the first broken entry is correctly identified. (Hard rule 5.)

**One happy-path browser test.** Script the canon case's F2 field through the full spine: S1 loads showing the seeded mixed-state dashboard; open F2 (`CONFLICTED`); S3 shows both candidates with neither pre-selected; submit a decision as Priya with a non-empty reason; attempt signoff as Priya and confirm it is blocked; sign off as Rajiv and confirm it succeeds; S7 shows `verified: true`; tamper one artifact; confirm S7 now shows `verified: false` with the broken entry named. This is the same sequence as the live demo (Section 10), so the test doubles as demo insurance, not just coverage.

**Tests are not gold-plated in a 22-hour sprint.** No coverage target, no snapshot test of every screen, no exhaustive edge-case matrix, no test-framework debate. The five invariant tests plus the one browser test are the floor and, unless M4 finishes early, also the ceiling. If time is short, the browser test is the first thing to drop, not the invariant tests: rehearsal (doc 04 section 6, M6, three run-throughs) already covers demo insurance, while the five invariant tests are cheap, headless, and are exactly what defends the product's central claim under adversarial Q&A (doc 03 section 3, question 2: "the product is not extraction, it is the refusal protocol").

---

## 12. Ranked cut list

**Cut order**, pre-decided in doc 04 section 5 and doc 03 section 7 row 9, unchanged here:

1. Public API polish (error message quality, response shape niceties beyond what Section 4 specifies).
2. Risk-board (S5) depth: keep the flat table and named disposition; cut per-row inline expansion first (`UX_PSYCHOLOGY_SPEC.md` section 13 makes the identical call independently, for the same screen).
3. The second document type in the eval corpus (keep the four canon documents and enough synthetic variety to hit 50 to 100 eval items; cut further document-type variety beyond that).
4. Hosting niceties: CloudFront, then even S3 website hosting, in favour of localhost (`AWS_RUNBOOK.md` section 6, "the localhost floor").

**Never cut, made unambiguous:**

1. **The live model call.** At least one real Bedrock `Converse` call happens during the build and is shown on S4, even if the rest of the demo runs on `ReplayProvider`.
2. **The conflict-abstain-decide-seal loop.** `CANON.md` section 10's eight-step spine, end to end, uninterrupted, for at least one field (F2 is the recommended choice, Section 5).
3. **Manifest integrity.** The SHA-256 chain and the tamper check (Section 8), demonstrated in both directions: `verified: true` before tampering, `verified: false` with the break named after.
4. **The honesty table.** SYNTHETIC/MOCKED/LIVE, present in the README from the first relevant commit (`REPO_FIRST_COMMIT_PACK.md` section 1, commit 4) and on a pitch slide, updated as the build lands, never written at the end.
5. **The demo path.** A working, rehearsed, end-to-end script that runs in under 90 seconds (doc 03 section 1's Technical Execution actions).

**Related operational fallbacks** (doc 03 section 7, "worst cases"), stated as build requirements rather than repeated as prose: `ReplayProvider` must work with zero network calls, since it is also the wifi-failure fallback (worst case 1), not only the Bedrock-failure fallback; a full screen recording of the rehearsed demo must exist by the end of M6 (doc 04 hour 19 to 21) so a live failure on stage can switch to it within five seconds, announced as a recording (worst case 5); and either laptop must be able to run the full demo alone (worst case 4), which is a consequence of the fixture corpus and `runs/*.jsonl` living in the repo and in S3, not only on one machine.

---

## Open founder decisions

| # | Question |
|---|---|
| 1 | `SCHEMA_PACK.md` and `DEMO_STORYBOARD.md` are named throughout doc 04 section 5's own contract, and cross-referenced by name in Sections 6 and 10 of this document, as the detailed sources this spec summarises. As of this writing neither exists in `factory/` (confirmed immediately before finishing this document; `AWS_RUNBOOK.md` and `UX_PSYCHOLOGY_SPEC.md`, requested the same way, now do exist and were read in full and folded in above). Who owns writing `SCHEMA_PACK.md` and `DEMO_STORYBOARD.md`, and by when relative to M1 (which assumes a schema pack exists for the generator) and M6 (which assumes a storyboard exists for the final rehearsal)? |
