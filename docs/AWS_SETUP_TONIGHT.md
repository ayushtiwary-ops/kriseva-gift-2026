# AWS SETUP TONIGHT: 30 minutes, start to finish

Written 2026-08-19 01:20 IST. This is the do-it-now version of `AWS_RUNBOOK.md`, cut down to only what has to be true before you sleep.

**Verified on your machine just now:** Node v25.9.0, npm 11.12.1, Python 3.11.15, git 2.53.0 all present. Homebrew present. **AWS CLI is NOT installed.** That is the blocker, and finding it tonight instead of at 11:00 Friday is worth the whole exercise.

**What you are setting up:** Kriseva's own AWS account, as the pre-warmed standby. Friday's build still runs on the event-provided account and credits, because the rubric says "using provided AWS credits" in the sentence that carries 30% of the score. Tonight's job is to make sure that if the event credits are late or Bedrock access is refused, you are running again in ten minutes instead of dead.

**Steps 2 and 3 need you personally.** I do not handle access keys, passwords or console logins, and you should not paste them into any chat. Everything else I can run or verify for you.


---

## REVISION, 2026-08-19 04:20 IST: steps 4 and 5 are settled, here is what actually applies

You ran the inventory. Account `082706806837`, IAM user `attest`, region `us-east-1`. Full report saved at `factory/AWS_MODEL_INVENTORY_2026-08-19.md`.

**The finding: 0 of 15 Anthropic models are usable. All are agreement-blocked.** Not just the frontier ones. Claude 3 Haiku is blocked too. So is Sonnet 4, 4.5 and 5. My earlier assumption that Sonnet-class was granted was wrong, and this section replaces it.

**75 of 122 model entries are usable now, and the one we want is on the list.**

### The decision: Amazon Nova Pro is the demo model

`amazon.nova-pro-v1:0`. Active, on-demand, no agreement needed, multimodal, and AWS-native.

Three reasons, in order of weight:

1. **It works today.** No email, no waiting, no dependency on a sales conversation resolving before Friday.
2. **On an AWS-judged rubric, Amazon's own model is the better story, not the consolation prize.** Doc 04 section 4 already told us to confirm access for "Claude family and Nova, take whatever strongest is instantly available". Nova is instantly available. A juror from AWS watching a build on AWS credits using AWS's own model is not thinking about what we could not get.
3. **The model is swappable by design.** The provider reads its id from an environment variable. If the event account has Anthropic enabled on Friday, we change one variable and the demo gets better. If it does not, nothing changes. This is exactly why the `ModelProvider` abstraction exists.

**Ladder, in order. Take the first that answers:**

| Order | Model | Model id | Note |
|---|---|---|---|
| 1 | Amazon Nova Pro | `amazon.nova-pro-v1:0` | Primary. On-demand and inference-profile both available |
| 2 | Amazon Nova 2 Lite | `us.amazon.nova-2-lite-v1:0` | Faster and cheaper. **Inference-profile only, so it needs the `us.` prefix** |
| 3 | Mistral Large 3 | `mistral.mistral-large-3-675b-instruct` | Strong text extraction, on-demand |
| 4 | Llama 4 Maverick | `us.meta.llama4-maverick-17b-instruct-v1:0` | Inference-profile, needs the `us.` prefix |

**The `us.` prefix rule, because this is the failure that wastes twenty minutes:** a model whose inference type is `INFERENCE_PROFILE` only will reject the bare id with a `ValidationException`. Prefix it with `us.` and it works. A model listing `ON_DEMAND` takes the bare id. Nova Pro lists both, so the bare id is fine.

### The corrected step 5 test call

```bash
cat > /tmp/converse-test.json <<'JSON'
{
  "modelId": "amazon.nova-pro-v1:0",
  "messages": [
    { "role": "user",
      "content": [ { "text": "A document says: Drawn capital as at 30 June 2026 (16:00 IST): USD 17,800,000. Reply with only the numeric value you find, no commentary." } ] }
  ],
  "inferenceConfig": { "maxTokens": 64, "temperature": 0 }
}
JSON
```

```bash
aws bedrock-runtime converse --profile kriseva --region us-east-1 --cli-input-json file:///tmp/converse-test.json
```

A response containing `17,800,000` means the model plane works. Screenshot it.

### What to say on stage about this

Do not hide it and do not apologise for it. The honest version is stronger:

> "The extraction runs on Amazon Nova Pro, on Bedrock, on the credits this event provided. The model sits behind a provider interface, so it is one environment variable to swap. That mattered to us because the product's claim is that the model is the replaceable part and the accountability record is the durable part. This build demonstrates that literally."

That answer turns a constraint into evidence for the architecture. Do not say a word about which models you could not get. Nobody asked.

### Still to do on AWS

Steps 6, 7 and 8 below are unchanged and still outstanding: the S3 bucket with versioning, the budget alarm, and exporting `BEDROCK_MODEL_ID=amazon.nova-pro-v1:0` into your shell.

---
---

## Step 1: Install the AWS CLI (2 minutes, no password needed)

```bash
brew install awscli
```

Then confirm:

```bash
aws --version
```

You want `aws-cli/2.x`. If Homebrew gives you v1, use the official installer instead, which will ask for your Mac password:

```bash
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "/tmp/AWSCLIV2.pkg" && sudo installer -pkg /tmp/AWSCLIV2.pkg -target /
```

---

## Step 2: Get an access key (you do this in the browser, 5 minutes)

Sign in to the AWS console with the Kriseva account. Then:

1. Go to IAM, Users, and create a user named `kriseva-attest-dev`. Do not enable console access for it.
2. Attach these two AWS managed policies for now: `AmazonBedrockFullAccess` and `AmazonS3FullAccess`. We tighten this on Friday for the event account; tonight speed matters more than least privilege on an account only you use.
3. Open the user, go to Security credentials, and create an access key. Choose "Command Line Interface" as the use case.
4. Copy the Access key ID and the Secret access key. The secret is shown once.

**Do not paste those anywhere except the terminal prompt in step 3.** Not into chat, not into a file, not into the repo.

---

## Step 3: Configure the profile (2 minutes, you type the keys)

```bash
aws configure --profile kriseva
```

It asks four things:

- AWS Access Key ID: paste it
- AWS Secret Access Key: paste it
- Default region name: `us-east-1`
- Default output format: `json`

**Why us-east-1:** it has the widest Bedrock model availability, which matters because we are not in a position to be choosy about which model we get. If your credits or account are pinned to a different region, use that instead and tell me which.

Confirm it worked:

```bash
aws sts get-caller-identity --profile kriseva
```

You should see an account number and the `kriseva-attest-dev` user ARN. If you see an error, the keys are wrong or not yet active; wait 30 seconds and retry once.

---

## Step 4: Find out which models you actually have (3 minutes)

List everything on offer in the region:

```bash
aws bedrock list-foundation-models --profile kriseva --region us-east-1 --query "modelSummaries[?providerName=='Anthropic'].modelId" --output table
```

Then check what you are actually allowed to invoke. Access being listed is not the same as access being granted:

```bash
aws bedrock list-foundation-models --profile kriseva --region us-east-1 --query "modelSummaries[?providerName=='Anthropic'].[modelId,modelLifecycle.status]" --output table
```

**Write down every model id that comes back.** As at 2026-08-19 every Anthropic model on your account is agreement-blocked. That is fine and changes nothing, because Amazon Nova Pro is usable now and is the better story on an AWS-judged rubric anyway. The demo is designed to be excellent on Amazon Nova Pro. If the bigger models land, the demo gets better. If they never land, nothing about Friday changes.

If nothing comes back at all, open the Bedrock console, go to Model access, and request access to the Anthropic family. Approval for Sonnet-class is usually quick.

---

## Step 5: Prove one real model call (5 minutes)

This is the step that matters. Everything before it is plumbing.

Write the request body:

```bash
cat > /tmp/converse-test.json <<'EOF'
{
  "modelId": "MODEL_ID_FROM_STEP_4",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "A document says: Drawn capital as at 30 June 2026 (16:00 IST): USD 17,800,000. Reply with only the numeric value you find, no commentary."
        }
      ]
    }
  ],
  "inferenceConfig": { "maxTokens": 64, "temperature": 0 }
}
EOF
```

Replace `MODEL_ID_FROM_STEP_4` with a real id, then call it:

```bash
aws bedrock-runtime converse --profile kriseva --region us-east-1 --cli-input-json file:///tmp/converse-test.json
```

A JSON response containing `17800000` or `17,800,000` means your model plane works end to end. **Screenshot that response.** It is evidence for the 30% technical criterion and it is the thing that proves, on Friday, that the only unknown is credentials.

If you get `AccessDeniedException`, the model is listed but not granted. Go back to step 4 and request access. If you get `ValidationException`, the model id is wrong or needs a regional inference-profile prefix such as `us.` in front of it; try that variant.

---

## Step 6: The S3 bucket (3 minutes)

Bucket names are globally unique, so pick something nobody else has:

```bash
aws s3api create-bucket --profile kriseva --region us-east-1 --bucket kriseva-attest-evidence-2026
```

Turn on versioning, which is what gives us an honest story about evidence custody:

```bash
aws s3api put-bucket-versioning --profile kriseva --bucket kriseva-attest-evidence-2026 --versioning-configuration Status=Enabled
```

Block all public access, because this holds evidence manifests:

```bash
aws s3api put-public-access-block --profile kriseva --bucket kriseva-attest-evidence-2026 --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
```

Confirm:

```bash
aws s3api get-bucket-versioning --profile kriseva --bucket kriseva-attest-evidence-2026
```

**On stage, the honest sentence is:** "Evidence objects are versioned in S3, so an overwrite leaves the prior version intact. We did not enable Object Lock in this build, and that is the difference between versioned and genuinely write-once." Say the second half. It costs nothing and it is exactly the kind of precision that scores on the honesty criterion.

---

## Step 7: The budget alarm (3 minutes)

You have USD 1,100 in credits. This stops a runaway loop eating them while you sleep.

```bash
cat > /tmp/budget.json <<'EOF'
{
  "BudgetName": "kriseva-attest-hackathon",
  "BudgetLimit": { "Amount": "50", "Unit": "USD" },
  "TimeUnit": "MONTHLY",
  "BudgetType": "COST"
}
EOF
```

```bash
aws budgets create-budget --profile kriseva --account-id YOUR_ACCOUNT_ID --budget file:///tmp/budget.json
```

Get `YOUR_ACCOUNT_ID` from the step 3 output. A 50 dollar monthly ceiling is deliberately far below your credit balance: it is a smoke alarm, not a spending plan. If it fires, something is wrong, not busy.

Check current spend any time:

```bash
aws ce get-cost-and-usage --profile kriseva --time-period Start=2026-08-01,End=2026-08-31 --granularity MONTHLY --metrics UnblendedCost
```

---

## Step 8: Wire it into the rehearsal build (2 minutes)

The build reads the model plane from environment variables and falls back to deterministic replay if any are missing, so it never breaks because AWS is absent.

```bash
export AWS_PROFILE=kriseva
export AWS_REGION=us-east-1
export BEDROCK_MODEL_ID=MODEL_ID_FROM_STEP_4
```

To make it permanent for your shell:

```bash
echo 'export AWS_PROFILE=kriseva' >> ~/.zshrc && echo 'export AWS_REGION=us-east-1' >> ~/.zshrc
```

Do NOT put `BEDROCK_MODEL_ID` in `.zshrc` permanently. It changes on Friday when you switch to the event account, and a stale value in a dotfile is exactly the kind of bug that costs an hour at 3am.

---

## What "done" looks like tonight

Tick all six and stop:

- [ ] `aws --version` shows 2.x
- [ ] `aws sts get-caller-identity --profile kriseva` returns your account
- [ ] At least one Anthropic model id is listed and granted, and you have written it down
- [ ] One `converse` call returned a real answer, and you screenshotted it
- [ ] The S3 bucket exists with versioning enabled
- [ ] The budget alarm exists

Ten minutes of it is waiting for AWS. The rest is typing.

---

## What this does NOT cover, on purpose

Hosting, CloudFront, IAM least-privilege policies and CloudTrail are all in `AWS_RUNBOOK.md` and none of them are needed tonight. Tonight is about one question: **can we make a real model call, and can we prove it.** Everything else is Friday's problem and Friday has a runbook.

## The one thing to remember on Friday

At the 11:00 briefing you will do this again on the event account. It will take ten minutes instead of thirty, because you will have done it once, in a calm room, with nobody watching. That is the entire reason for tonight.
