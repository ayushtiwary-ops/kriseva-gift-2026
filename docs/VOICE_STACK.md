# THE VOICE STACK: what we use, what we rejected, and why

Status: STABLE. Written 2026-08-20. Star counts read from the GitHub API on the day.

**Decision: Kokoro-82M, voice `bm_lewis`, running locally on the founder's Mac. No API, no credits,
no per-character cost.** ElevenLabs is kept as a one-variable swap if a key
appears, and macOS `say` remains as a floor that always works.

---

## 1. The candidates, with real numbers

| Repository | Stars | Licence | Last push | Verdict |
|---|---|---|---|---|
| microsoft/VibeVoice | 52,929 | MIT | 2026-07-24 | Most starred. Built for long-form multi-speaker dialogue. Overkill for a single narrator reading 290 words |
| coqui-ai/TTS | 45,918 | MPL-2.0 | **2024-08-16** | **Rejected.** Unmaintained since the company wound down, and the XTTS-v2 weights are non-commercial |
| suno-ai/bark | 39,238 | MIT | **2024-08-19** | **Rejected.** Stale, slow, and unreliable prosody on numbers |
| myshell-ai/OpenVoice | 37,159 | MIT | 2025-04-19 | Voice cloning rather than narration. Not what we need |
| fishaudio/fish-speech | 32,273 | no SPDX licence declared | 2026-08-03 | Strong, but an undeclared licence is a bad fit for a company submission |
| resemble-ai/chatterbox | 26,066 | **MIT** | 2026-07-21 | **The serious runner-up.** See below |
| index-tts/index-tts | 23,211 | no SPDX licence declared | 2026-08-18 | Very active, same licence caution |
| nari-labs/dia | 19,369 | Apache-2.0 | 2025-11-19 | Dialogue-focused |
| SWivid/F5-TTS | 15,136 | MIT repo | 2026-07-23 | **Careful:** the repo is MIT but the released weights are CC-BY-NC. Non-commercial |
| rhasspy/piper | 11,280 | MIT | 2025-08-26 | **Archived.** Fast but the quality gap is audible |
| **hexgrad/kokoro** | **8,479** | **Apache-2.0** | 2025-08-06 | **Chosen.** See below |
| boson-ai/higgs-audio | 8,320 | Apache-2.0 | 2026-06-05 | Capable, much heavier for no gain here |
| canopyai/Orpheus-TTS | 6,298 | Apache-2.0 | 2025-12-05 | Good, needs more setup |

**Most stars is not the same as best for the job.** Two of the top three are
effectively unmaintained, and three otherwise strong options carry licences that
are wrong for a company pitch.

---

## 2. Why Kokoro, on 8,479 stars rather than 52,929

Four reasons, in the order they mattered.

1. **Apache 2.0 on the code and the weights.** No non-commercial clause to
   explain to anybody. Several higher-starred options fail this alone.
2. **It is 82 million parameters.** Measured on the founder's M5: a 12 second
   clip generates in about 2 seconds, roughly six times faster than real time,
   on CPU, with no GPU and no network.
3. **Fixed named voices, which is what narration actually needs.** The video is
   29 separate clips. A cloning model re-infers the voice each time and can drift
   in timbre between clips. Kokoro's voices are deterministic, so clip 1 and clip
   29 match.
4. **It is free and unmetered.** Retaking the script twenty times costs nothing,
   which matters more than the last five percent of quality when the script is
   still moving.

**Chatterbox is the better model and we still did not pick it.** It is MIT,
actively maintained, and Resemble's own blind study reports 65.3 percent of
listeners preferring it over ElevenLabs. It is the right choice the moment we
want a *specific* cloned voice, and it is the first thing to try if the founder
does not like any Kokoro voice. For reading a fixed script in a consistent
register it buys us little and costs setup time we do not have.

---

## 3. How it is wired

`tts.py` picks an engine in this order, and every engine returns the measured
duration of the clip it produced:

```text
TTS_ENGINE set explicitly?          use that
ELEVENLABS_API_KEY starts with sk_? elevenlabs
~/kriseva-tts exists?               kokoro
otherwise                           macOS say
```

Because captions are timed from the **measured duration of each clip**, changing
engine re-times every caption automatically. Sync cannot drift, whichever engine
is used.

Kokoro runs in its own interpreter at `~/kriseva-tts` and is held open as a
worker process, so the model loads once for all 29 lines instead of once per
line.

### Rebuilding the video

```bash
cd <video dir>
KOKORO_VOICE=bm_lewis KOKORO_SPEED=1.24 python3 render.py && bash build2.sh
```

`KOKORO_VOICE` accepts any Kokoro voice; the film uses `bm_lewis`, chosen by the
founder from the comparison page. `KOKORO_SPEED` sets the pace; 1.24 puts the
current script at 156 words per minute and the finished film at 1:56, inside the
two minute limit.

The build ends with an EBU R128 loudness pass at -16 LUFS. Kokoro voices differ
in level by up to a third between them, so without it a quieter voice does not
carry in a room.

---

## 4. Two install traps, recorded so they are not hit twice

1. **macOS blocks native extensions loaded from `/private/tmp`.** A virtualenv
   there fails with *"library load disallowed by system policy"* on `_cffi_backend`.
   Install under the home directory.
2. **A uv-managed interpreter hit the same signature check.** Building the venv
   from the existing pyenv Python with `--system-site-packages` worked first time.

---

## 5. What we are not claiming

The voice is synthesised and we say so on the video page. We are not claiming a
human recorded it, and we are not claiming Kokoro matches ElevenLabs. It is
markedly better than the macOS voice it replaces, it is free, and it runs offline
on a laptop at a venue with no network.
