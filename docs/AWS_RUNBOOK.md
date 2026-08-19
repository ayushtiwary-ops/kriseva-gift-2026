# AWS Operations Runbook: GIFT IFIH Hackathon Resource Factory

Status: DRAFT, written 2026-08-18 ahead of the 21-22 August sprint. Owner: founder runs every command in this file by hand.

This is a document, not a script. Every command below is written for a human to type on Thursday or Friday. Nothing in this file has been executed and nothing here spends money by existing. Values that depend on the account or the briefing are in angle brackets; the complete list is in the placeholders table at the end. Read Section 0 first, it decides which AWS account every later section points at.

---

## 0. The account decision

**Decision: build against the event-provided AWS account and credits as primary. Kriseva's own AWS account (USD 1,100 in startup credits, Bedrock access: ZERO Anthropic models (all 15 agreement-blocked as at 2026-08-19). Amazon Nova and 74 other models usable now) is a pre-warmed hot standby, tested and proven ready, not the build target.**

Reasoning:

1. The 30% Technical Execution and Architecture rubric line reads: "Does the code run live? Met core track requirements using provided AWS credits?" (doc 03, section 1). The phrase "provided AWS credits" is graded text, not a suggestion. A build that runs on Kriseva's own account instead risks a judge reading it as not meeting that line literally, even if the code works perfectly. That is real, avoidable risk on the single highest-weighted criterion in the whole rubric.
2. Kriseva's own account is fully funded today, and its Amazon Nova Bedrock access is provable before Friday even starts (Section 1). A request for access to the largest frontier models has been emailed to AWS and is not confirmed; it may not land in time, and the plan does not wait on it either way. What makes this account a genuine standby, not a hope, is that it is tested and working in advance, so switching to it under pressure is a configuration change, not a scramble.
3. The architecture already separates the model call behind a `ModelProvider` interface (doc 04, section 3: `BedrockProvider` reads its model id from an environment variable). Pointing that provider at a different account and model id is one exported variable and one `--profile` flag, not a rebuild. Building once against this abstraction is what makes keeping the standby warm nearly free.

**Exact trigger for switching to standby, decided now, not renegotiated at 2 AM:**

- Trigger A: by 60 minutes after the 11:00 briefing ends, event account credentials fail identity verification (Section 3, step 3), or every candidate model in the event account's Bedrock catalog comes back `NOT_AUTHORIZED` with no mentor fix available before the M2 build window needs its first live call (doc 04, hours 2-5).
- Trigger B: event account Bedrock access breaks mid-sprint (revoked, quota exhausted, region drops to zero enabled models) with no mentor fix inside 30 minutes.
- Explicit non-trigger: the event account only offering a narrower model set, or only one model family, is NOT a reason to switch. Doc 04 section 4 item 2 is direct on this point: take whatever strongest model is instantly available. Narrower than hoped is normal, not a failure state.
- If the trigger fires and we switch: say so on stage, plainly, in the honesty table. Doc 03's Honesty and Roadmap Credibility line rewards exactly this kind of disclosure. Hiding an account switch to protect the Technical line is the wrong trade and the more dangerous one if discovered.

If the trigger fires, standby activation means re-running Sections 3 and 4 of this document with `--profile kriseva` instead of `--profile event`. Nothing else in this runbook is event-account-specific except the credential values themselves. Keep Bedrock, S3, and IAM on the same account once a decision is made. Never split the live model call onto one account and the storage onto another; a judge who asks "which account is this" deserves a one-word answer.

---

## 1. Thursday pre-warm (before travelling)

Goal: prove the entire call path on Kriseva's own account so that Friday's only unknown is which credentials go into an already-working machine.

1. Confirm AWS CLI v2 on both laptops.
   ```
   aws --version
   ```
   Expect `aws-cli/2.x.x`. If missing or still v1, install (macOS):
   ```
   curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
   sudo installer -pkg AWSCLIV2.pkg -target /
   aws --version
   ```
   Repeat on the second laptop. Doc 04 section 2 item 6 requires both laptops fully provisioned, and doc 03 worst case 4 is a dead laptop; the only real defense against that is that either machine can already run everything on its own.

2. Create named profiles so switching accounts on Friday is one flag, not a new setup.
   ```
   aws configure --profile kriseva
   ```
   Enter Kriseva's own access key, secret key, a default region, and `json` as output format.
   Pre-create the event profile shell now, with placeholder values, so entering the real credentials Friday is a two-minute edit rather than a first attempt (doc 04 section 2 item 6: "Dry-run `aws configure` flow so credential entry takes 2 minutes on site").
   ```
   aws configure --profile event
   ```
   From here on, every command in this document runs against whichever account `--profile` names, or whichever `AWS_PROFILE` is exported.

3. Region decision for this pre-warm exercise: `ap-south-1` (Mumbai), AWS's most mature India region and confirmed to support Bedrock. This is Kriseva's own working default, not the event account's region, which Section 2 confirms separately and may differ.
   ```
   aws configure set region ap-south-1 --profile kriseva
   ```

4. Verify identity.
   ```
   aws sts get-caller-identity --profile kriseva
   ```
   Record the `Account` field in the placeholders table at the end of this document.

5. Check Bedrock model access status, Anthropic models specifically, since that is the family Kriseva's own account currently has some access to.
   ```
   aws bedrock list-foundation-models \
     --profile kriseva --region ap-south-1 \
     --by-provider anthropic \
     --query "modelSummaries[].{id:modelId,name:modelName,status:modelLifecycle.status}" \
     --output table
   ```
   For every candidate id returned, check granted access:
   ```
   aws bedrock get-foundation-model-availability \
     --profile kriseva --region ap-south-1 \
     --model-id <CANDIDATE_MODEL_ID>
   ```
   Read `authorizationStatus`. Expect `AUTHORIZED` on Sonnet-class ids and `NOT_AUTHORIZED` on anything Opus-class or larger, matching the account status as of 2026-08-18. Record every result, including the refusals; a documented "we asked, access was not granted, we did not wait on it" is itself useful material for the honesty table later.

6. Prove the call path end to end. Run one real Converse call against whichever id came back `AUTHORIZED`. The exact command shape and a sample request body are in Section 4; this step is the same commands, just run two days early.

7. Write down the exact model id string that responded, verbatim, with a timestamp, next to the placeholders table or in a dated note. This is the entire point of Thursday: once one real call has succeeded end to end, Friday's only open variable is which credentials are loaded, not whether the call path works at all.

8. Repeat steps 4 through 7 on the second laptop.

---

## 2. The 11:00 Friday briefing

Rule, stated once and binding: get model access confirmed IN THE ROOM, and run one Converse call before leaving the room (doc 03, section 6; doc 04, section 4, item 2). An access problem found at hour 1 is fixable. The same problem found at hour 12 is not.

Checklist, the six questions from doc 04 section 4:

1. [ ] Credits amount: ______________ Account type (shared event account vs. our own): ______________ Region to use: ______________
2. [ ] Bedrock model families enabled for hackathon accounts (Claude, Nova, both): ______________ Access confirmed NOW, in the room (yes/no): ______________ Strongest model instantly available, taken without waiting for a specific tier: ______________
3. [ ] Mandated services for "core track requirements" that the rubric references: ______________
4. [ ] S3 Object Lock available on the event account (yes/no; if no, versioning only, disclosed honestly): ______________
5. [ ] Mentor contact channel for the night shift, someone reachable at 03:00: ______________
6. [ ] Budget alarm setup path (self-service, Section 5, or organizer-managed): ______________

Three additions, sharper versions of points above, do not skip them as duplicates:

7. [ ] Does the event account's actual permission set allow enabling S3 Object Lock (a bucket-level, permanent-once-set change), as opposed to Object Lock merely existing as a feature somewhere in AWS? Ask this as a yes/no gate: ______________
8. [ ] Which exact AWS region is the event account provisioned in, as distinct from which region we would prefer to use? Hackathon credit grants are frequently issued through AWS Event Engine (dashboard.eventengine.run, team hash) and are commonly pinned to a fixed region, often a US region, regardless of the venue's location. Do not assume it matches Section 1's `ap-south-1` default: ______________
9. [ ] AWS mentor's direct contact for the night shift: name ______________ phone or Slack handle ______________ confirmed reachable at 03:00 (yes/no): ______________

Also confirm at this point: is access via AWS Event Engine (team hash, temporary session credentials that expire) or via directly issued long-lived IAM keys? The two paths use different setup commands in Section 3 step 1.

---

## 3. First-hour setup

1. Configure the event profile with the credentials issued at the briefing. Two possible paths depending on what Section 2's last question found.

   Path A, static access keys issued directly:
   ```
   aws configure --profile event
   ```
   AWS Access Key ID: `<EVENT_ACCESS_KEY_ID>`
   AWS Secret Access Key: `<EVENT_SECRET_ACCESS_KEY>`
   Default region name: `<EVENT_REGION>`
   Default output format: `json`

   Path B, AWS Event Engine or any other temporary session credentials (three values, not two, and they expire):
   ```
   aws configure set aws_access_key_id <EVENT_ACCESS_KEY_ID> --profile event
   aws configure set aws_secret_access_key <EVENT_SECRET_ACCESS_KEY> --profile event
   aws configure set aws_session_token <EVENT_SESSION_TOKEN> --profile event
   aws configure set region <EVENT_REGION> --profile event
   ```
   Note the expiry window shown on the credentials page and calendar a refresh before it lapses; see Section 9 row 3.

2. Export the profile and region for the working shell session, so every later command in this document defaults correctly without repeating `--profile`.
   ```
   export AWS_PROFILE=event
   export AWS_DEFAULT_REGION=<EVENT_REGION>
   ```

3. Verify identity before touching anything else.
   ```
   aws sts get-caller-identity
   ```
   Confirm the `Account` field matches the event account id from the briefing, not Kriseva's own account number recorded in Section 1. This single check is what Section 9's troubleshooting row 8 exists to protect against.

4. Create a least-privilege identity for the app itself, separate from the human operator's `event` profile. Use an IAM user with access keys if the event account allows creating IAM users; if it only allows assuming a role (common on locked-down event sub-accounts), use `aws sts assume-role` instead and skip to step 5's policy content applied to that role.
   ```
   aws iam create-user --user-name kriseva-attest-app
   ```
   Actions needed: Bedrock invoke plus read-only Bedrock discovery for diagnostics, and S3 read/write scoped to our own bucket only.
   ```
   cat > attest-app-policy.json << 'EOF'
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "BedrockInvoke",
         "Effect": "Allow",
         "Action": [
           "bedrock:InvokeModel",
           "bedrock:InvokeModelWithResponseStream",
           "bedrock:Converse",
           "bedrock:ConverseStream",
           "bedrock:ListFoundationModels",
           "bedrock:GetFoundationModel",
           "bedrock:GetFoundationModelAvailability"
         ],
         "Resource": "*"
       },
       {
         "Sid": "S3AppBucket",
         "Effect": "Allow",
         "Action": [
           "s3:GetObject",
           "s3:PutObject",
           "s3:ListBucket",
           "s3:GetBucketVersioning"
         ],
         "Resource": [
           "arn:aws:s3:::<BUCKET_NAME>",
           "arn:aws:s3:::<BUCKET_NAME>/*"
         ]
       }
     ]
   }
   EOF
   ```
   Note on the Bedrock `Resource: "*"` line: foundation models are AWS-owned, not account-owned, so `InvokeModel` and `Converse` are normally scoped by action, not by a customer resource ARN. Tighten it to a specific pattern if wanted: `arn:aws:bedrock:<EVENT_REGION>::foundation-model/*`.
   Attach the policy:
   ```
   aws iam put-user-policy \
     --user-name kriseva-attest-app \
     --policy-name attest-app-least-privilege \
     --policy-document file://attest-app-policy.json
   ```

5. Create access keys for that user, and only that user, never for a root or admin identity.
   ```
   aws iam create-access-key --user-name kriseva-attest-app
   ```
   This prints the secret once. Capture it immediately into a local `.env` file.
   Rule: keys never enter the repo. `.env` is listed in `.gitignore` from the very first commit (doc 04 section 1, the `NOTICE.md` commit). Before every `git commit`, sanity-check:
   ```
   git diff --cached | grep -E "AKIA|aws_secret_access_key"
   ```
   A hit means stop and unstage before committing.
   Configure a third profile for the app's own scoped credentials, distinct from the operator's `event` profile:
   ```
   aws configure --profile attest-app
   ```

6. S3 bucket for manifests and fixtures, versioned, public access blocked.
   ```
   aws s3api create-bucket \
     --bucket <BUCKET_NAME> \
     --region <EVENT_REGION> \
     --create-bucket-configuration LocationConstraint=<EVENT_REGION>
   ```
   Drop `--create-bucket-configuration` entirely if `<EVENT_REGION>` is `us-east-1`; passing `LocationConstraint=us-east-1` is rejected.
   ```
   aws s3api put-bucket-versioning \
     --bucket <BUCKET_NAME> \
     --versioning-configuration Status=Enabled

   aws s3api put-public-access-block \
     --bucket <BUCKET_NAME> \
     --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
   ```

7. Bucket policy note: with public access blocked, this bucket is reachable only through signed requests from our own IAM identity. Do not attach a public-read policy to it. The static site in Section 6, if it needs public reads, lives in a separate bucket with its own narrow policy; this manifests bucket never gets one.

8. Object Lock decision path, resolved by Section 2 checklist item 7.
   If permitted: Object Lock can only be turned on at bucket creation, so re-create the bucket with the flag instead of adding it after the fact.
   ```
   aws s3api create-bucket \
     --bucket <BUCKET_NAME> \
     --region <EVENT_REGION> \
     --create-bucket-configuration LocationConstraint=<EVENT_REGION> \
     --object-lock-enabled-for-bucket

   aws s3api put-object-lock-configuration \
     --bucket <BUCKET_NAME> \
     --object-lock-configuration '{"ObjectLockEnabled":"Enabled","Rule":{"DefaultRetention":{"Mode":"GOVERNANCE","Days":1}}}'
   ```
   `GOVERNANCE` mode, not `COMPLIANCE`: governance mode can be overridden by a permissioned user if we make a mistake mid-sprint, while compliance mode cannot be undone by anyone, including the account root, which is too rigid for a 22-hour build. State this choice out loud if asked; it is a deliberate tradeoff, not a corner cut.
   If not permitted, or not confirmed in time: proceed on versioning alone (already enabled in step 6) and say so plainly in the honesty table. Manifests are versioned, not Object-Locked, because the event account did not grant it. That is the honestly-disclosed path doc 04 section 4 item 4 asks for.

---

## 4. Bedrock verification

1. List everything available in the working region.
   ```
   aws bedrock list-foundation-models --region <EVENT_REGION> --output table
   ```

2. Filter to the two families we care about.
   ```
   aws bedrock list-foundation-models --region <EVENT_REGION> \
     --by-provider anthropic \
     --query "modelSummaries[].modelId" --output text

   aws bedrock list-foundation-models --region <EVENT_REGION> \
     --by-provider amazon \
     --query "modelSummaries[?contains(modelId,'nova')].modelId" --output text
   ```

3. Check granted access per candidate, strongest first.
   ```
   aws bedrock get-foundation-model-availability \
     --region <EVENT_REGION> \
     --model-id <CANDIDATE_MODEL_ID>
   ```
   Read `authorizationStatus`: `AUTHORIZED` means usable right now. Work down the candidate list from strongest to weakest and use the first `AUTHORIZED` hit. Do not wait for a specific tier to become available.

4. One test Converse call, exact invocation shape.
   ```
   aws bedrock-runtime converse \
     --region <EVENT_REGION> \
     --model-id <AUTHORIZED_MODEL_ID> \
     --cli-input-json file://converse-test.json
   ```
   `converse-test.json` (this is a request configuration file, not application code):
   ```json
   {
     "modelId": "<AUTHORIZED_MODEL_ID>",
     "messages": [
       {
         "role": "user",
         "content": [
           { "text": "Reply with the single word OK if you can read this." }
         ]
       }
     ],
     "inferenceConfig": {
       "maxTokens": 16,
       "temperature": 0
     }
   }
   ```

5. On model id strings: Claude-family ids typically look like `anthropic.claude-<name>-<date>-v1:0`, or, when only offered through a cross-region inference profile, prefixed `us.anthropic....` or the matching regional prefix. Nova-family ids look like `amazon.nova-pro-v1:0`, `amazon.nova-lite-v1:0`, `amazon.nova-micro-v1:0`, `amazon.nova-premier-v1:0`. Every id string printed in this document is an illustration of the naming pattern, not a value to paste. Model catalogs change often; the only trustworthy source of the exact string on the day is step 2's live output, read moments before use.

6. The rule: take whatever strongest model is instantly available. Claude family is the first choice by product design (doc 04 section 3 names `BedrockProvider` as Claude or Nova, whichever the credits make available); Nova is a legitimate fallback, not a downgrade to apologize for.

7. Mandatory note on our own account: as of 2026-08-18, Kriseva's own AWS account has Sonnet-class Claude access only. Access to the largest frontier models has been requested by email and is not confirmed; it may not arrive before Friday. The demo must be designed to be genuinely good on a Sonnet-class model on its own terms, and must never depend on a larger model arriving mid-build or mid-pitch. If a stronger model becomes available on either account, treat it as a free upgrade swapped in through the environment variable, never as something the build plan waits on.

---

## 5. Cost control

1. Budget alarm at 50% of credits.
   ```
   cat > budget.json << 'EOF'
   {
     "BudgetName": "attest-hackathon-credits",
     "BudgetType": "COST",
     "TimeUnit": "MONTHLY",
     "BudgetLimit": {
       "Amount": "<CREDIT_AMOUNT_USD>",
       "Unit": "USD"
     }
   }
   EOF

   cat > budget-notifications.json << 'EOF'
   [
     {
       "Notification": {
         "NotificationType": "ACTUAL",
         "ComparisonOperator": "GREATER_THAN",
         "Threshold": 50,
         "ThresholdType": "PERCENTAGE"
       },
       "Subscribers": [
         { "SubscriptionType": "EMAIL", "Address": "<FOUNDER_EMAIL>" }
       ]
     }
   ]
   EOF

   aws budgets create-budget \
     --account-id <EVENT_ACCOUNT_ID> \
     --budget file://budget.json \
     --notifications-with-subscribers file://budget-notifications.json
   ```

2. Manual cost check, two ways, in order of reliability on a same-day account.
   Primary, works immediately with no activation lag:
   ```
   aws budgets describe-budgets --account-id <EVENT_ACCOUNT_ID>
   ```
   Secondary, Cost Explorer: often needs a one-time console activation and can take hours to populate on a brand-new account, so do not rely on it alone during a same-day event.
   ```
   aws ce get-cost-and-usage \
     --time-period Start=<TODAY_YYYY-MM-DD>,End=<TOMORROW_YYYY-MM-DD> \
     --granularity DAILY \
     --metrics "UnblendedCost"
   ```

3. Standing rule, verbatim from doc 04 section 7: do not burn personal API money silently. Any spend beyond the provided credits needs founder sign-off before it happens, not after.

---

## 6. Hosting options, ranked

Doc 04 section 3 puts hosting near the bottom of the AWS wiring cut list, ahead of only "hosting niceties." Treat it that way: it is the first thing to abandon under time pressure, and localhost is a legitimate finish line, not a failure.

### Option 1, primary: S3 static website plus CloudFront

Setup time: 30 to 45 minutes the first time, 10 minutes if rehearsed Thursday.
```
aws s3api create-bucket \
  --bucket <SITE_BUCKET_NAME> \
  --region <EVENT_REGION> \
  --create-bucket-configuration LocationConstraint=<EVENT_REGION>
```
Keep public access blocked on this bucket too; CloudFront reads it through Origin Access Control, not a public policy.
```
aws cloudfront create-distribution \
  --origin-domain-name <SITE_BUCKET_NAME>.s3.<EVENT_REGION>.amazonaws.com \
  --default-root-object index.html
```
Attaching Origin Access Control so CloudFront is the only reader of the private bucket is console work (Distributions, Origins, Edit, Origin access control settings, Create new OAC). The full CLI JSON for that wiring is long and easy to get wrong under a clock, so this one sub-step is a deliberate console carve-out, not a shortcut being hidden.
What can go wrong: CloudFront takes 5 to 15 minutes to propagate after creation or after an invalidation; an Origin Access Control or bucket-policy mismatch returns 403; forgetting to invalidate after a redeploy means judges see a stale build.
Abandon point: if the distribution has not reached `Deployed` within 20 minutes, or two consecutive 403s survive a policy fix, stop and drop to Option 2 or localhost. Doc 04's M5 window (hours 15-19) is the only slot budgeted for this; it must not eat into the spine or the eval harness.

### Option 2, fallback: S3 website hosting only, no CloudFront

Setup time: 10 minutes.
```
aws s3api put-bucket-website --bucket <SITE_BUCKET_NAME> \
  --website-configuration '{"IndexDocument":{"Suffix":"index.html"},"ErrorDocument":{"Key":"error.html"}}'
```
This mode needs a public-read bucket, which the S3 website endpoint requires. Only do this on the dedicated site bucket, never on the manifests bucket from Section 3.
```
aws s3api put-public-access-block --bucket <SITE_BUCKET_NAME> \
  --public-access-block-configuration BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false

cat > site-bucket-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::<SITE_BUCKET_NAME>/*"
    }
  ]
}
EOF

aws s3api put-bucket-policy --bucket <SITE_BUCKET_NAME> --policy file://site-bucket-policy.json
```
What can go wrong: no HTTPS on the raw website endpoint; the bucket name must be globally unique, so a collision forces a rename; single-page app routing needs `ErrorDocument` pointed back at `index.html`.
Abandon point: past 10 minutes fighting a name collision or policy propagation, drop to localhost.

### Option 3: small compute, only if the backend itself must be reachable

App Runner from a container image, or a single EC2 instance running the doc 04 section 3 Node service directly.
Setup time: App Runner 20 to 30 minutes if the image already builds locally (it needs an ECR push first); EC2 15 minutes if the security-group pattern was rehearsed Thursday.
What can go wrong: App Runner's extra build-and-push step under time pressure; EC2 needs its port opened in the security group and a stable address noted before the pitch, and must be started well before demo time, not during it.
Abandon point: if not verified reachable by hour 19 (doc 04's M6 window), do not attempt it live. A half-configured public endpoint failing on stage is worse than a laptop.

### The localhost floor

Demoing from localhost is acceptable and costs nothing on the rubric if the AWS services are genuinely exercised elsewhere in the build. The rubric asks whether AWS credits were used to meet core requirements, not whether the address bar shows an AWS domain during the pitch. Doc 03 worst case 2 states this outright: if Bedrock access never lands, S3 and CloudFront still count as AWS usage, disclosed honestly. Hosting is the lowest-priority AWS line item by design; the live model call, the conflict-abstain-decide-seal loop, and the manifest integrity are the things that never get cut.

---

## 7. Evidence capture for the pitch

Rubric target: the 30% Technical Execution and Architecture line ("does the code run live... using provided AWS credits"). Capture this as insurance for the pitch and the architecture slide, independent of whether the live demo goes perfectly on stage.

1. Bedrock invocation. Screenshot the Bedrock console Model access page showing granted status for the model actually used. If invocation logging is enabled, pull the configuration as proof it is on:
   ```
   aws bedrock get-model-invocation-logging-configuration --region <EVENT_REGION>
   ```
   Stronger than either: the app's own `runs/*.jsonl` record (prompt hash, latency, LIVE badge), shown live on the Agent Trace screen (CANON.md screen S4). A judge can inspect this one directly instead of trusting a screenshot.

2. S3 object versions. Console: the bucket, an object, its Versions tab, showing two or more versions of the same manifest key. CLI-side proof for the same thing:
   ```
   aws s3api list-object-versions --bucket <BUCKET_NAME> --prefix <KEY_PREFIX>
   ```

3. Budget alarm. Console: Billing and Cost Management, Budgets, the budget created in Section 5, showing the 50% threshold configured, and the notification timestamp if it ever trips.

4. CloudTrail, if enabled. Console: CloudTrail, Event history, filtered to the Bedrock Converse or InvokeModel and S3 PutObject events during the sprint window. Doc 04 names this explicitly as an audit-trail talking point, and it mirrors ATTEST's own pitch: a system that proves who did what, when. Capturing it is on-message, not just box-ticking.

---

## 8. The NO-AWS fallback checklist

For event credits never arriving, or Bedrock access being refused outright.

1. ReplayProvider path (doc 04 section 3). Every live call ever made, including Thursday's pre-warm success on Kriseva's own account, is already recorded to `runs/*.jsonl`: prompt hash, params, response, latency. If live Bedrock access disappears mid-sprint, `ReplayProvider` re-serves those recorded fixtures deterministically. This is a configuration flip, one environment variable, not new engineering done under panic, because doc 04 already designed the provider interface this way.

2. What we say on stage, verbatim, no spin:
   - "All data is synthetic; we have zero real customer data in this build by design."
   - "The extraction model runs live on Bedrock; the fund and its documents are fictional." (Say this only while a call is genuinely live.)
   - When running on replay instead: "This run is replayed from a recorded Bedrock call we made earlier on our own AWS account. We are showing you the identical prompt, response, and latency we captured live." State the RECORDED badge out loud. Do not imply it is live, do not bury the badge, do not rush past this line.

3. Minimum AWS surface that still counts as genuine usage, even in total failure: the S3 bucket with versioning and the manifest chain actually stored in it, plus the least-privilege IAM identity actually created and used to read and write it, plus the budget alarm and CloudTrail if reached. Doc 03 worst case 2 states the floor directly: if Bedrock never lands, S3 and CloudFront still count as AWS usage, and we disclose that the model ran from a recorded fixture. That is real, inspectable AWS usage, not a consolation prize.

---

## 9. Troubleshooting table

| # | Symptom | Cause | Fix |
|---|---|---|---|
| 1 | `AccessDeniedException` on Converse or InvokeModel | IAM identity lacks the Bedrock action, or the model was never granted access even though it is listed | `aws bedrock get-foundation-model-availability --region <EVENT_REGION> --model-id <CANDIDATE_MODEL_ID>`; if `NOT_AUTHORIZED`, request access in console (Bedrock, Model access) or ask the mentor, do not keep retrying the same call |
| 2 | Model not enabled in region: `ValidationException`, invalid model identifier, or missing from the list | The model is not offered in `<EVENT_REGION>`, or needs a cross-region inference profile id instead of the bare id | `aws bedrock list-foundation-models --region <EVENT_REGION> --query "modelSummaries[].modelId" --output text`; if absent, retry with the `us.` (or matching regional) prefix, or point this one call at a different region with `--region` while keeping the rest of the stack where it is |
| 3 | Expired token: `ExpiredTokenException` | Temporary or session credentials timed out; likely if access came through AWS Event Engine, which issues short-lived tokens (Section 3, Path B) | Return to the credentials dashboard for a fresh session block, then re-run the three `aws configure set` commands from Section 3 step 1 Path B, then `aws sts get-caller-identity --profile event` |
| 4 | Region mismatch: resources exist but later commands say they do not | `AWS_DEFAULT_REGION`, `--region`, and the profile's configured region disagree | `aws configure get region --profile event` and `echo $AWS_DEFAULT_REGION`; make them agree, or just pass `--region <EVENT_REGION>` explicitly on every command in this document |
| 5 | Throttling: `ThrottlingException` | On-demand Bedrock rate limits hit, likely with two agent seats plus the app all calling the same model | Check current limits with `aws service-quotas list-service-quotas --service-code bedrock --region <EVENT_REGION>`; add retry and backoff in the app's client, stagger which agent lane calls Bedrock, or fall back to ReplayProvider (Section 8) rather than burning sprint time on quota fights |
| 6 | Bucket name collision: `BucketAlreadyExists` | S3 bucket names are globally unique across every AWS account, not just ours | Append the account id: `aws s3api create-bucket --bucket kriseva-attest-manifests-<EVENT_ACCOUNT_ID> --region <EVENT_REGION> --create-bucket-configuration LocationConstraint=<EVENT_REGION>` |
| 7 | CloudFront propagation delay: `Deployed` but still serving old content, or a fresh 403/404 | Edge caches take up to 15 minutes to propagate; cached objects survive until TTL expiry or an explicit invalidation | `aws cloudfront create-invalidation --distribution-id <DISTRIBUTION_ID> --paths "/*"`, then poll `aws cloudfront get-invalidation --distribution-id <DISTRIBUTION_ID> --id <INVALIDATION_ID>` until `Completed`; if still stale after 15 minutes, use the direct origin URL or fall back to Section 6 Option 2 |
| 8 | Credentials picked up from the wrong profile: a command lands on the wrong account | `AWS_PROFILE` left set from an earlier session, or `--profile` omitted so the CLI silently used `default` | `aws sts get-caller-identity --profile event` and compare `Account` against the recorded id before every session; consider leaving the `default` profile without credentials so an omitted `--profile` fails loudly instead of silently hitting the wrong account |

---

## Placeholders

| Placeholder | Meaning |
|---|---|
| `<EVENT_REGION>` | AWS region the event account is provisioned in, confirmed at the 11:00 briefing (Section 2, item 8) |
| `<EVENT_ACCOUNT_ID>` | 12-digit event account id, read from `aws sts get-caller-identity --profile event` |
| `<EVENT_ACCESS_KEY_ID>` | Access key id issued for the event account at the briefing |
| `<EVENT_SECRET_ACCESS_KEY>` | Secret key issued for the event account at the briefing |
| `<EVENT_SESSION_TOKEN>` | Session token, only if credentials are temporary (for example, AWS Event Engine); leave unset for static long-lived keys |
| `<CANDIDATE_MODEL_ID>` | A model id read live from `list-foundation-models` output, never hand-typed from memory |
| `<AUTHORIZED_MODEL_ID>` | The candidate whose `get-foundation-model-availability` call returned `AUTHORIZED` |
| `<BUCKET_NAME>` | Globally unique bucket name for manifests and fixtures, for example `kriseva-attest-manifests-<EVENT_ACCOUNT_ID>` |
| `<SITE_BUCKET_NAME>` | Globally unique bucket name for the static site, separate from `<BUCKET_NAME>` |
| `<CREDIT_AMOUNT_USD>` | Total credit amount confirmed at the briefing, the budget's 100% line |
| `<FOUNDER_EMAIL>` | Address for budget alert notifications |
| `<DISTRIBUTION_ID>` | CloudFront distribution id, from the `create-distribution` output |
| `<INVALIDATION_ID>` | CloudFront invalidation id, from the `create-invalidation` output |
| `<KEY_PREFIX>` | S3 key prefix used for manifest objects, for example `manifests/` |
| `<TODAY_YYYY-MM-DD>` / `<TOMORROW_YYYY-MM-DD>` | Date bounds for the manual Cost Explorer check |

---

## Open founder decisions

1. Doc 04 section 7 says any spend beyond provided credits needs founder sign-off. What is the actual mechanism during the 22-hour window, especially overnight: a pre-approved ceiling either founder can act on solo (for example, up to some small dollar amount), or does every dollar of overage require waking the other founder for a live yes?
2. If the event-provided account turns out to be a shared account across multiple teams rather than a dedicated per-team account, are we comfortable building on it as is (CANON.md already keeps all data synthetic, so exposure risk is architectural, not data), or should we ask at the briefing for a separate credential set?
