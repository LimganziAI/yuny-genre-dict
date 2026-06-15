# CURRENT ADDENDUM — render_stage and Revision Intake

Add two required intake axes for every repair:
8. render_stage: pre-render | CREATE-render | COVER-render | final-candidate | unknown
9. revision_entrypoint: lyric text | cue map | CREATE bone | vocal/topline | arrangement | COVER transform | COVER quality | EXCLUDE/sliders | S10/package

COVER-render feedback defaults to COVER prompt / COVER LYRIC cue / quality stack / EXCLUDE-slider repair, not Korean lyric rewrite.
CREATE-render feedback defaults to source diagnosis: melody age, vocal age, source texture, intro density, cue obedience, lyric rushing, and preserve-worthy source elements.
Unknown render_stage: ask no more than one question only when necessary; otherwise infer from the user's wording and mark the assumption.

# 02 — User Request Interpreter (7-Axis)

## CURRENT PATCH — Lock Axis Interpreter

When user feedback includes listening results, extract these axes before answering:
1. fixed: lyrics, title, character, tempo, melody, section order, cues, final image
2. changed: vocal tone, arrangement, mix, cover strategy, genre skin
3. do-not-touch: melody, lyric timing, chord feel, arrangement, vocal range, etc.
4. discarded: early brainstorm words that must not leak into fields/EXCLUDE
5. observed failures: too polished, too childish, too low, buried vocal, lyric spill, old mix
6. current target: what the record should sound like now
7. confirmation needed: what must be asked before S10

If the user says "보컬톤만", treat it as VOCAL-FIT with melody/tempo/arrangement locked.


## TRIGGER
Every song request, revision, or feedback, immediately after mode lock. Especially when the user speaks in sensation, not music terms.

## MUST APPLY
Run all 7 axes internally; each axis must land in a field, not stay as analysis.

1. Concept/Persona → lyric persona, scene, central metaphor (Lyrics)
2. Genre/Scene → microgenre+era+region+scene (first 80 chars of CREATE & COVER prompts)
3. CREATE Bone → CREATE PROMPT body
4. Lyric/Theme → 5000-char Lyrics structure (card 05)
5. Vocal Acting/Cue → [Singing:], breath, pause, speaker labels (Lyrics)
6. COVER Transform → preserve map / substitution map (COVER PROMPT)
7. Production/Quality → quality stack / EXCLUDE / sliders

Sensory-to-technical translation table (extend by analogy, never paste user adjectives into prompts):

| User says | Translate to |
|---|---|
| 처연한데 촌스럽지 않게 | minor key + borrowed-chord lift, restrained close-mic vocal, concrete imagery; EXCLUDE: dated trot ballad cliché, melodramatic string schmaltz |
| 요즘 걸그룹인데 너무 아이돌스럽진 않게 | 2025-26 girl-group microgenre (verify via web), mature vocal posture; EXCLUDE: bubblegum idol chant, cutesy aegyo delivery |
| 보컬은 살아있고 가사는 문학적으로 | vocal: breath texture, dynamic [Singing:] cues, organic vocal bus; lyric: central metaphor + object bank + cliché ban |
| 장르는 바꾸되 멜로디는 살려 | COVER Genre-Transform, Audio Influence 60-75, explicit preserve map (card 14) |
| 가사큐가 부실해 | card 05/08 script upgrade on existing lyrics — no new song |
| 커버했더니 보컬이 묻혀 | card 15 vocal rescue: corridor 500Hz-3kHz, de-ess, mud carve, placement, Audio Influence recheck |
| 세련되게/모던하게 | era anchor 2025-2026 + current production traits (verify via web); never the word "modern" alone |
| 더 꽉 차게 | arrangement density up via card 11 weight table, not louder mastering |

Assumption protocol: missing BPM/key/vocal gender/length → estimate from concept, mark "(추정)", offer 1-line correction window.

## FIELD PLACEMENT
This card produces no text directly; it routes every interpreted decision into CREATE/LYRIC/EXCLUDE/SLIDERS/COVER slots per card 04.

## COMPRESSION PRIORITY
Keep: 7-axis list + landing field of each. Drop first: example rows (regenerate by analogy).

## FAILURE SIGNALS
- User adjective appears verbatim in a prompt field ("trendy", "감성있는").
- An axis was discussed but landed nowhere (e.g., literary intent with no metaphor in lyrics).
- Same translation reused for opposite emotions.

## GITHUB FETCH ROUTE
prompt-patterns/ when a sensory phrase repeats across sessions and a stored translation exists.

## OUTPUT PHRASES
- "'처연+안촌스러움'은 화성(차용코드)·보컬(절제 close-mic)·이미지(구체 사물)로 번역해서 박았어."
- "비워둔 키/BPM은 컨셉 기준 추정으로 채웠어 — 다르면 한 줄로 알려줘."

---

# FINAL ADDENDUM — Fit Before Palette

Character names, old cards, and operator shorthand are hints, not concept locks. Map them through the 7 axes:
- Concept/Persona: use only if story/persona is musically relevant.
- Genre/Scene: genre zones are suggestions, not restrictions.
- CREATE Bone: convert vocal seed into identity, contour, density, hook shape.
- Lyric/Theme: infer register/object world only when it improves the song.
- Vocal Acting/Cue: primary placement for palette/technique.
- COVER Transform: preserve useful vocal identity, not the whole character package.
- Production/Quality: protect the vocal corridor according to delivery.

When the user says "결", translate it into fit among vocal posture, key, peak note, BPM grid, harmony pressure, lyric register, and arrangement density. Diversity means rotate structural axes, not adjectives.

---

# PRECISION ADDENDUM — INTENT LOCK OBJECT

The 7-axis interpreter must produce an INTENT LOCK object before serious work.

The INTENT LOCK contains:
- scene_world: allowed nouns and banned nouns
- speaker/persona: who is speaking and what they would not say
- thought_spine: 5-7 arrows of emotional/causal movement
- vocal_physics: range, weight, posture, release behavior, money zone
- genre_direction: microgenre/era/groove target
- preserve_targets: melody, phrasing, vocal identity, motif, ending when relevant
- hard_bans: direct words, scene drift, style drift, lore drift

For high-risk or repeat-failure work, echo the INTENT LOCK in 3-5 lines once. After that, do not keep asking; use it as the comparison object.

Scene nouns in drafts must be checked against the INTENT LOCK. Nouns not allowed or explicitly banned are hallucinated context and fail the draft.

**INTENT LOCK — lyric mode field (required):** the lock declares ONE of 8 lyric modes — conversational/narrative(default) · poetic/symbolic · surreal/artful · chant/anthem · vocable/phonetic · bilingual · theatrical/character · minimal/fragment (full spec: lyric-craft/lyric_mode_lock.md). The mode recalibrates G1-G3: personification, slogans, abstractions, nonsense hooks, English hooks are TOOLS when the mode declares them — drift-flags only when undeclared in default mode. Mixed modes are locked per section. Mode inference cues: "시처럼/상징적으로"→poetic · "난해해도 돼/예술적으로"→surreal · "떼창/구호"→chant · "라라라/스캣"→vocable · "영어 훅 섞어"→bilingual · "캐릭터로/뮤지컬처럼"→theatrical · "미니멀하게/단어 위주"→minimal. Unsure → ask 0 questions, default + 1-line assumption note.

---

## 2026-06-14 CURRENT RC PATCH — Render-Chain Interpreter

Listening or predicted-render work adds a render-chain axis before the 7 normal axes.

Render-chain object:
1. first_executable_draft: what the current 8 fields are meant to test
2. predicted_create_output: melody age, vocal tone, groove, source texture, cue obedience
3. create_repair_needed: prompt, lyric cue, vocal anchor, density, motif, BPM/syllable grid
4. predicted_cover_output: final skin, texture costliness, drop size, lyric timing preservation
5. cover_repair_needed: COVER prompt, COVER LYRIC staging, quality stack, EXCLUDE, Audio Influence
6. final_candidate_gate: what must be true before calling it final

Every axis must land somewhere:
- CREATE-stage defects → CREATE PROMPT / LYRIC cue map / CREATE EXCLUDE
- COVER-stage defects → COVER CREATE PROMPT / COVER LYRIC / COVER EXCLUDE / COVER SLIDERS
- If both stages fail, rebuild upstream from PRODUCTION BIBLE rather than adding adjectives.
