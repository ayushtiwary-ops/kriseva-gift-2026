#!/usr/bin/env bash
# Redeploys the hub and, if a build is present, the prototype.
#
#   bash scripts/deploy.sh            hub only
#   bash scripts/deploy.sh --prototype /path/to/attest    hub plus prototype
#
# Everything goes to one S3 bucket on our own AWS account. No CloudFront: this
# IAM user has no CloudFront permission, so the HTTPS REST endpoint is the link.
set -euo pipefail
export AWS_PROFILE="${AWS_PROFILE:-kriseva}"
export AWS_REGION="${AWS_REGION:-us-east-1}"
BUCKET="${ATTEST_BUCKET:-kriseva-gift-backup-2026}"
BASE="https://$BUCKET.s3.us-east-1.amazonaws.com"
HERE="$(cd "$(dirname "$0")/.." && pwd)"
STAMP="$(date +%Y%m%d-%H%M)"

cd "$HERE"

echo "1. Rendering document pages"
for pair in "RESIDENCY_ASK:residency-ask:What we need from the residency" \
            "MEASURED_RESULTS:measured-results:Measured results" \
            "AGENT_CONTRACT_PACK:agent-contracts:Agent contracts" \
            "RUNNING_COST_AND_LIMITS:cost-and-limits:What it costs to run" \
            "DEFECT_LEDGER_2026-08-19:defect-ledger:Defect ledger" \
            "CANON:canon:The fictional world" \
            "SCENARIO_DESIGN:scenario-design:Scenario design"; do
  src="${pair%%:*}"; rest="${pair#*:}"; out="${rest%%:*}"; title="${rest#*:}"
  [ -f "docs/$src.md" ] && timeout 30 python3 scripts/md2html.py "docs/$src.md" "docs/$out.html" "$title" >/dev/null
done
echo "   ok"

echo "2. Uploading the hub"
aws s3 cp index.html "s3://$BUCKET/index.html" --content-type "text/html; charset=utf-8" --cache-control "public,max-age=120" >/dev/null
aws s3 cp deck/index.html "s3://$BUCKET/deck/index.html" --content-type "text/html; charset=utf-8" --cache-control "public,max-age=120" >/dev/null
aws s3 cp styles/hub.css "s3://$BUCKET/styles/hub.css" --content-type "text/css; charset=utf-8" --cache-control "public,max-age=120" >/dev/null
aws s3 cp README.md "s3://$BUCKET/README.md" --content-type "text/plain; charset=utf-8" >/dev/null
for f in docs/*.html; do
  aws s3 cp "$f" "s3://$BUCKET/$f" --content-type "text/html; charset=utf-8" --cache-control "public,max-age=120" >/dev/null
done
for f in docs/*.md; do
  [ -e "$f" ] && aws s3 cp "$f" "s3://$BUCKET/$f" --content-type "text/plain; charset=utf-8" >/dev/null
done
echo "   ok"

if [ "${1:-}" = "--prototype" ]; then
  APP="${2:?pass the path to the attest build}"
  echo "3. Building and uploading the prototype from $APP"
  ( cd "$APP" && node scripts/build-static.js >/dev/null 2>&1 )
  gzip -9 -c "$APP/attest-walkthrough.html" > /tmp/proto-$STAMP.html.gz
  # Versioned copy first, so a stale browser cache can never serve an old build
  # at the venue. The stable path is updated after it, and the versioned link is
  # the one to use on stage.
  aws s3 cp "/tmp/proto-$STAMP.html.gz" "s3://$BUCKET/prototype/$STAMP/index.html" \
    --content-type "text/html; charset=utf-8" --content-encoding gzip --cache-control "public,max-age=31536000" >/dev/null
  aws s3 cp "/tmp/proto-$STAMP.html.gz" "s3://$BUCKET/prototype/index.html" \
    --content-type "text/html; charset=utf-8" --content-encoding gzip --cache-control "public,max-age=60" >/dev/null
  echo "   versioned: $BASE/prototype/$STAMP/index.html"
fi

echo
echo "4. Verifying"
fail=0
for p in "index.html" "deck/index.html" "styles/hub.css" "docs/residency-ask.html" "docs/measured-results.html" "prototype/index.html"; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "$BASE/$p")
  printf "   %-34s %s\n" "$p" "$code"
  [ "$code" = "200" ] || fail=1
done
echo
if [ "$fail" = "0" ]; then echo "DEPLOYED. $BASE/index.html"; else echo "NOT DEPLOYED. A path above did not return 200."; exit 1; fi
