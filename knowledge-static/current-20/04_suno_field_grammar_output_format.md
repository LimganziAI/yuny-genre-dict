# CURRENT ADDENDUM — Status and Self-Test in 8-Field Delivery

Every 8-field output has an internal status:
FIRST EXECUTABLE DRAFT / STAGED REPAIR / FINAL-CANDIDATE.
Only FINAL-CANDIDATE requires measured counts plus production-loop self-test.

Before FINAL-CANDIDATE:
- CREATE PROMPT <1000, COVER CREATE PROMPT <1000
- LYRIC+CUES <5000, COVER LYRIC+CUES <5000
- COVER LYRIC is not a blind copy unless preserving exact timing is intentional
- section cues are renderable devices, not story explanations
- [Outro] and [End] present when full song format requires closure

# 04 — Suno Field Grammar & Output Format

## CURRENT PATCH — S10 Field Integrity Audit

Before final 8 fields:
- Reconfirm fields match the current lock, not old discussion.
- Measure CREATE/COVER prompt length and use the budget for execution value.
- Check LYRIC+cues under 5000 and cues are renderable, not explanatory.
- Ensure COVER LYRIC preserves text unless cue repair is intentional.
- Ensure EXCLUDE contains actual failure classes only.
- SLIDERS only: Weirdness / Style Influence / Audio Influence. CREATE Audio Influence = —; COVER Audio Influence numeric.
- If any field is generic, stale, contradictory, or thin, stop at staged artifact and repair.


## CURRENT HOTFIX — Field Validity and S10 Counts
- S10 is the only point where final 8 fields may ship.
- SLIDERS field must contain only:
  Weirdness: N
  Style Influence: N
  Audio Influence: — for CREATE, numeric for COVER
  No invented sliders such as Vocal Clarity, Tempo Target, Mix Quality, Loudness, Stereo Width.
- If BPM/tempo is important, put it in CREATE/COVER prompt; never put it in SLIDERS.
- Field names must be exactly:
  CREATE PROMPT / LYRIC / EXCLUDE / SLIDERS / COVER CREATE PROMPT / COVER LYRIC / COVER EXCLUDE / COVER SLIDERS.
- Final answer must include measured char counts internally before shipping. If counts are not checked, the output is staged, not final.
- If user asks for "부분부분 절차" show stage artifact, not 8-field final, until S10 passes.

## TRIGGER
Every 8-field emission; any question about format, char limits, tags, or why a field looks the way it does.

## MUST APPLY
**8-field skeleton (exact order, each in its own copyable code block, measured chars shown):**
```
1 CREATE PROMPT   (style, ≤1000; serious 700-950 / sketch 250-350)
2 LYRIC           (≤5000; performance script, card 05)
3 EXCLUDE         (card 16)
4 SLIDERS         (Weirdness / Style Influence / Audio Influence)
5 COVER PROMPT    (≤1000; serious 700-950)
6 LYRIC           (usually identical text; cue deltas only if COVER changes delivery)
7 EXCLUDE
8 SLIDERS         (Audio Influence MANDATORY)
```
**Prompt-field grammar:** English only. Comma-separated tag list, never sentences ("This song should..." banned). Period = concept boundary; comma = optional element; and/with = required pair. Position weight: slot 1 ≈ 50% influence, slot 2 ≈ 25%, slot 3 ≈ 12% — front-load identity. No [brackets] in prompt fields (Lyrics-only syntax). No imperatives (Create/Make). 1 word = 1 sound-world: "neo-soul" already implies Rhodes+jazz+late-night; don't restate.

**Lyrics-field grammar:** [ ] = non-sung instructions, section tags, speaker labels. ( ) = audible ad-libs/chant/breath ONLY — never a singer label. Section tags carry bar counts: [Verse 1 8], [Chorus 8], [Bridge 4]. Bar counts are approximate but control intro/outro well. V5 intro bloat fix: [Short Instrumental Intro: 2 bars] or open directly on [Verse 1 8]. Song always ends [Outro]→[End]. Multilingual: one section = one language; non-target sections cue "all lyrics in [lang]".

**Measurement duty:** count chars with the code tool per field and print them (e.g., `CREATE 928 / LYRIC 4,412`). Never estimate. ±5% over a limit → one auto-compress pass (card 05 order for lyrics; cut slot-4+ texture first for prompts).

## FIELD PLACEMENT
This card IS the placement law. Anything musical → prompt fields. Anything performed → Lyrics. Anything banned → EXCLUDE. Anything probabilistic → Sliders.

## COMPRESSION PRIORITY
Keep: 8-field order, ( ) vs [ ] rule, measurement duty, position weighting. Drop first: bar-count nuance.

## FAILURE SIGNALS
- Sentence-form prompt; bracket inside a prompt field.
- "(Female Vocal 1)" as a label.
- Char counts absent or suspiciously round.
- Song text ends mid-air without [Outro]/[End].

## GITHUB FETCH ROUTE
prompt-patterns/response-templates/ for non-standard deliveries (instrumental, album batch).

## OUTPUT PHRASES
- "필드별 글자수는 실측이야: CREATE 931 / LYRIC 4,387."
- "라벨은 괄호 말고 대괄호 — ( )는 실제로 소리나는 애드립 전용이야."
---

## 2026-06-14 CURRENT RC PATCH — Draft vs Final Label

8 fields may have three statuses:
1. **FIRST EXECUTABLE DRAFT** — ready to test in Suno, not final.
2. **POST-RENDER REPAIR** — based on CREATE/COVER listening feedback.
3. **FINAL-CANDIDATE** — measured S10 plus two-pass CREATE→COVER logic passed.

Before saying final:
- count all 8 fields
- confirm CREATE prompt builds source audio only
- confirm LYRIC is source-performance script
- confirm COVER prompt transforms the existing CREATE audio
- confirm COVER LYRIC is final-record staging script
- confirm COVER quality stack exists
- confirm EXCLUDE contains observed/predicted failure classes only

If the user is still in test/listen/feedback loop, label the output FIRST EXECUTABLE DRAFT or POST-RENDER REPAIR, not final.
