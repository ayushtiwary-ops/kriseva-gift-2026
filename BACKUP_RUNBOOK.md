# BACKUP RUNBOOK: what to open when something fails

One page. Keep it on your phone. Every link below works with no laptop, no server,
no local build and no network beyond the venue wifi.

---

## The links, in the order you would reach for them

| # | If this fails | Open this |
|---|---|---|
| 1 | Nothing has failed. Normal demo | Your laptop, `http://localhost:4000` |
| 2 | Laptop, port, server, or the local build | **`https://kriseva-gift-backup-2026.s3.us-east-1.amazonaws.com/prototype/index.html`** |
| 3 | You need the whole submission, not just the product | `https://kriseva-gift-backup-2026.s3.us-east-1.amazonaws.com/index.html` |
| 4 | AWS itself is unreachable | `https://ayushtiwary-ops.github.io/kriseva-gift-2026/` |
| 5 | All networks are down | The video, offline on your phone, and the deck as a PDF |

**Say it plainly when you switch.** "The laptop is not cooperating, so I am opening
the deployed build. Same product, same numbers, all synthetic." A calm switch reads
as preparation. An apology reads as a failure.

---

## What the backup prototype is, exactly

It is the real product with the real application code, embedded unmodified. Only the
network layer is replaced by responses captured from the running server by driving it.
Nothing is reimplemented to make the demo work. Every screen says **recorded walkthrough**
across the top, so nobody can say you implied it was live.

**All 26 cases are in it.** The entity switcher works. Every screen works.
Verified across 182 screens on the deployed build.

**The write actions follow the walkthrough order.** Decide, then attest, then sign off,
then tamper. Click them in that order and you get the real sequence. Click out of order
and it says so plainly rather than pretending.

---

## The one thing that can go wrong with the backup

**A stale browser cache.** If you loaded the link earlier in the week, the browser may
serve that older copy.

Fix, in order:
1. Add `?v=` and today's date to the end of the link.
2. Hard reload: **Cmd + Shift + R**.
3. Open it in a private window.

**Before you travel, open the link in the browser you will use on stage, confirm it
loads, then leave that tab open.** A tab that is already open cannot fail to load.

---

## If a juror asks to see it themselves

Give them the hub link, not the prototype link. The hub explains what they are looking
at before they click into it, and it carries the data statement, so a screenshot of the
product can never be mistaken for a real record.

`https://kriseva-gift-backup-2026.s3.us-east-1.amazonaws.com/index.html`

---

## Redeploying during or after the sprint

From the hub repository:

```bash
bash scripts/deploy.sh --prototype ~/path/to/attest
```

It rebuilds the document pages, uploads the hub, builds and uploads the prototype, and
then checks six URLs and prints `DEPLOYED` or `NOT DEPLOYED`. It writes the prototype to
a **timestamped path as well as the stable one**, so on stage you can use a link that no
cache has ever seen.

Requires the `kriseva` AWS profile. Costs a few cents of S3 storage and nothing else.

---

## What is where

| | |
|---|---|
| Public hub repository | `github.com/ayushtiwary-ops/kriseva-gift-2026` |
| Private rehearsal source | `github.com/ayushtiwary-ops/kriseva-attest-rehearsal`, **public after 14:00 Friday** |
| Everything deployed | S3 bucket `kriseva-gift-backup-2026`, our own AWS account |
