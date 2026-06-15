# CURRENT ADDENDUM — Stage-Specific EXCLUDE/Slider Repair

Stage-Specific EXCLUDE/Slider Repair:
- CREATE-render failure: block source failures such as old melody, retro idol belting, cheap source synth, lyric rushing, empty intro only if observed or highly likely.
- COVER-render failure: block final failures such as toy synth, beep-boop lead, ringtone melody, thin first 8 bars, weak drop, melody loss, lyric timing drift, buried Korean lead, mono collapse.
- Do not move abandoned brainstorm genres into EXCLUDE unless they leaked.
Change one variable per A/B: prompt OR EXCLUDE OR Audio Influence, unless rebuilding upstream.

# 16 — EXCLUDE & Slider Strategy

## CURRENT PATCH — EXCLUDE Purity + Slider Fit

- EXCLUDE is not a meeting-history trashcan. Do not include genres or instruments abandoned during discussion unless they leaked in renders.
- Wrong-gender exclusions are useful only when drift is likely/observed.
- For vocal-tone repairs, prioritize actual failures: melody flattening, pitch collapse, too-low weight, too-glossy sweetness, whisper-only, breath-noise wash, rushed timing, buried Korean lead.
- For COVER repairs: changed melody, changed lyric timing, source-skin bleed, old karaoke mix, mono collapse, harsh sibilance, muddy low-mids.
- Sliders must match the job: high preserve/refine COVER uses higher Audio Influence; stronger skin replacement lowers it.


## CURRENT HOTFIX — EXCLUDE and Slider A/B for COVER Failures
If COVER quality failed, EXCLUDE must include the actual failed render class, not generic negatives.
Useful failure classes:
- old kids TV theme, retro educational song, dated radio rock, cheap MIDI guitars, thin karaoke backing
- mono vocal collapse, buried Korean lead, masked hook shouts, weak gang chant
- muddy low-mid wash, harsh cymbal fizz, smeared low end, loose drums
- fresh-song rewrite, melody loss, lyric timing drift, source skin bleeding through

Slider rules:
- CREATE Audio Influence = —
- COVER Audio Influence:
  70-75 = melody/topline very protected; risk source skin preservation.
  62-68 = preserve melody but allow transform.
  55-61 = balanced transform after skin/oldness failure.
  45-54 = stronger skin replacement; monitor melody drift.
Change one variable per A/B. Do not change prompt, EXCLUDE, and Audio Influence at the same time unless rebuilding upstream.

## TRIGGER
Every build (auto-inject pass); any no/never/avoid found in a prompt draft; drift feedback; slider questions.

## MUST APPLY
**EXCLUDE is an active control surface, not a passive fence.** Every negative the user or the concept implies moves OUT of prompt fields INTO EXCLUDE — the dedicated Exclude field is parsed more consistently than inline negation (inline "no X" may partially work on newer models [커뮤/中]); freeing prompt budget for positive design is the trade that wins. ~200 chars is comfortable; 300-400+ is legitimate when control demands it (high-signal entries only, no noise spam).

**Priority order = drift-lockout taxonomy (trim bottom-up, never the top):**
1 language-drift lockout — non-target language drift, stray foreign-language lines, random multilingual inserts; never NAME an unrelated language unless it actually leaked
2 vocal/gender-drift lockout — wrong gender lead, single-voice collapse on duets [공식: Exclude는 악기·스타일·보컬스타일 지원 — Lyrics "[female vocals]" × Exclude "male vocals" 페어링]
3 source-genre drag + generic-pop pull lockout
4 crowd/live lockout — live audience crowd cheering, stadium reverb, arena crowd noise
5 mix-defect lockout — guarded wording per card 15
6 delivery-drift lockout — rapping, spoken-word delivery, rap verse (sung songs in rap-gravity genres)
7 abrupt-ending lockout — unfinished/abrupt ending
8 robotic-vocal lockout — robotic autotune vocal (unless vocoder is the concept)

**Auto-inject tiers (silent, every serious build):**
T1 studio defaults (#4 + muddy lo-fi wash + robotic autotune) · T2 concept protection (dark concept → block "bright cheerful pop"; acoustic → block "stadium production") · T3 pop-gravity lockout for weak genres (emo/phonk/drill → "pop chorus, radio polish") · T4 token-bias: lyric contains Neon/Echo/Ghost/Silver/Shadow/Whisper/Crystal/Velvet → block their drift genres · T5 era anchor 2025+ → block "early 2010s production, 2nd-gen idol sound" · T6 delivery lock (#6).

**festival/anthem/live in any prompt → crowd block REQUIRED same build.**

**Sliders (state all three, both packages):**
- Weirdness: 40-50 stable record / 50-60 sketch / 70-85 experimental.
- Style Influence: 70-85 prompt-led (tight) / 40-50 lyric-led (loose).
- Audio Influence: CREATE "—" only when nothing uploaded; COVER ALWAYS a number — 60-75 preserve lead/topline · 45-55 balanced transform · 20-40 texture/refine. Melody wobble → 65-70; too timid → 30-40.
- Presets: stable W45/S75 · experimental W75/S45 · transform-preserve W50/S60/A65 · refine W45/S55/A30.

**Slider failure map [전부 가설 — 케이스 3회 전 수치 확정 금지]:** melody lost in cover → AI +5~10 · transform too timid → AI -10~20 or stronger source lockout · vocal buried → AI recheck + corridor reinforcement (card 15) · generic → Style Influence up + Position-1 rewrite · chaotic → Weirdness down + prompt density down · too safe/flat → Weirdness +10 or ONE signature-motif spike.
**Entry count:** ~5개 엔트리가 클린 처리 한계라는 커뮤 관찰 [커뮤/中] — 룰 변경은 보류(A/B 대상); 6+가 필요하면 high-signal만 남기고 묶음어로 압축.

## FIELD PLACEMENT
All negatives → EXCLUDE fields 3 & 7 (CREATE-side = bone/vocal/structure threats; COVER-side = sound/genre/source-lockout; same-family simple songs may share one list). Slider numbers → fields 4 & 8 with one-word purpose tags.

## COMPRESSION PRIORITY
Keep: lockout taxonomy, T1/T6, Audio Influence table, never-name-languages rule; the failure map keeps its [가설] label or drops whole. Drop first: preset shorthand.

## FAILURE SIGNALS
- "no autotune" sitting inside a prompt field.
- Duet collapsed to one voice and EXCLUDE has no #2 entry.
- Festival anthem with crowd roaring (T1 skipped).
- COVER sliders missing Audio Influence — instant defect.

## GITHUB FETCH ROUTE
prompt-patterns/diagnostics/ for drift-specific EXCLUDE sets that proved out in cases.

## OUTPUT PHRASES
- "부정어는 전부 EXCLUDE로 뺐어 — Suno는 인라인 'no'를 못 읽고, 프롬프트 예산은 설계에 써야 해."
- "COVER Audio Influence 65: '멜로디 보존' 의도값이야. 흔들리면 70까지 올려."
## CURRENT ADDENDUM — Ratio/MJ and EXCLUDE Discipline
Do not put abandoned ratio lanes or discarded genre experiments into EXCLUDE unless they actually leaked into renders. `MJ style 10%` as seasoning does not require excluding unrelated artist traits; only block failure classes that threaten the song.
When using technical mix prompts, EXCLUDE still stays high-signal: buried lead, mono collapse, harsh sibilance, muddy low-mid wash, melody loss, lyric timing drift, wrong vocal identity.

## 2026-06-14 CURRENT ADDENDUM — Stage-Specific EXCLUDE/Slider Repair
EXCLUDE and sliders follow render_stage:
- no-render: block known likely failures from intent and case memory.
- CREATE-render: block source failures only if they actually leaked; repair CREATE/COVER assumptions together.
- COVER-render: COVER EXCLUDE holds final render failures: toy synth, empty intro, old vocal, melody loss, lyric timing drift, buried Korean lead, source-skin bleed, weak drop.
- Audio Influence changes are single-variable A/B unless rebuilding upstream.
- If lowering Audio Influence fixes skin but loses melody, the next repair must strengthen preserve map before changing anything else.
