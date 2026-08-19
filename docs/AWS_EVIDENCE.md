# AWS EVIDENCE: what we can prove, and the exact words for it

Captured 2026-08-19. Account `082706806837`, IAM user `attest`, region `us-east-1`. All of this is verified output, not description.

This document exists because the 30% technical criterion asks "does the code run live, using provided AWS credits". Evidence beats assertion, and these are the four pieces we hold.

---

## Evidence 1: a real Bedrock model call, live

```
aws bedrock-runtime converse --profile kriseva --region us-east-1 --cli-input-json file:///tmp/converse-test.json
```

Result: Amazon Nova Pro (`amazon.nova-pro-v1:0`) read a document line stating drawn capital of USD 17,800,000 and returned `17800000`. Latency **302 ms**. Tokens: 50 in, 10 out.

**Why 302 ms matters:** a live model call sits inside a 70-second demo. At 302 ms it is invisible to a viewer. This is the number that tells us the demo will not stall waiting on the model, and it is worth knowing before we are on stage rather than during.

**The line to say:** "The extraction runs live on Amazon Nova Pro through Bedrock. Three hundred milliseconds. You are watching a real model call, not a recording, and the badge on screen tells you which one you are getting."

---

## Evidence 2: the model inventory, meaning we chose rather than defaulted

A full availability sweep across the region returned **122 model entries, 75 usable now, 46 agreement-blocked**. Saved at `AWS_MODEL_INVENTORY_2026-08-19.md`.

**Why show this:** it converts "we used Nova" from a default into a decision. A technical juror who asks why Nova gets an answer with a survey behind it rather than a shrug.

**The line to say:** "We swept the account, 122 model entries, 75 available to us. Nova Pro won on latency and on being AWS-native for an AWS build. The model sits behind a provider interface, so it is one environment variable to change."

**Do not volunteer** which models were unavailable. If asked directly, answer plainly and move on. It is not interesting and it is not our point.

---

## Evidence 3: evidence custody in S3, demonstrated

Bucket `kriseva-attest-evidence-2026`. Versioning `Enabled`. All four public access blocks `true`.

A manifest was written, then overwritten. Both versions persist:

| Version | Content | IsLatest |
|---|---|---|
| `JaIt0piF7A2VDCAim95znF1Dwvh.65hI` | `{"caseId":"CASE-2026-Q1-MER001","synthetic":true,"v":2}` | true |
| `FzqdGxo3vRW5HYNmmLSbnxQXXzItFLeb` | `{"caseId":"CASE-2026-Q1-MER001","synthetic":true,"v":1}` | false |

The superseded version was then fetched by version id and returned its original content intact.

**This is the important part.** It is not a screenshot of a settings page saying versioning is on. It is an overwrite followed by a successful retrieval of what was overwritten. The claim and the demonstration are the same action.

**The line to say:** "Evidence objects are versioned. I overwrote one and then pulled the previous version back with its original content. An overwrite does not destroy the record."

**The honest second half, which is not optional:** "We did not enable Object Lock in this build. Versioning means the prior copy survives an overwrite. Object Lock would mean it cannot be deleted at all. That is a real difference and I am not going to blur it."

Volunteering that distinction is worth more on the honesty criterion than the versioning is worth on the technical one.

---

## Evidence 4: what we have not done

Stated here so it is never accidentally implied.

| Not done | Why it matters |
|---|---|
| Budget alarm | The `attest` IAM user has no `budgets:ViewBudget` permission, so it needs the console as account owner. Two minutes, still outstanding |
| CloudTrail | Same permission gap. Would be a good audit-trail talking point, not required |
| Object Lock | Deliberately not enabled. See the honest sentence above |
| Hosting on AWS | The demo runs from localhost. AWS is genuinely exercised for the model plane and evidence storage, which is what the rubric asks about |
| Anything on the event account | Friday's job. Roughly 10 minutes, because everything here has been done once already |

---

## The Friday repeat, in one line

Everything above gets redone on the event-provided account at the 11:00 briefing. It takes about ten minutes instead of an evening, because the only unknown left is credentials. That is the entire reason for doing it tonight.

---

## Screenshot checklist

| # | Screenshot | Held? |
|---|---|---|
| 1 | The Converse response showing `17800000` and `latencyMs: 302` | Yes |
| 2 | The `list-object-versions` table showing two versions | Yes |
| 3 | The inventory summary line: 122 found, 75 usable | Yes |
| 4 | Cost Explorer showing real Bedrock spend after Friday's build | Not yet, Friday |

One and three prove the model plane. Two proves the evidence plane. Four proves the calls were real rather than mocked, and it is the only one that has to wait.
