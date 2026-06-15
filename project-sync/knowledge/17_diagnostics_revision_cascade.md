# CURRENT ADDENDUM — Where To Start After User Says Fix It

## Where To Start After User Says Fix It
Use render_stage + revision_entrypoint:
- pre-render complaint: run self-test and internal production council.
- CREATE-render complaint: source diagnosis first. Repair CREATE bone/vocal/topline/cue before COVER.
- COVER-render complaint: final-record diagnosis. Lock liked lyric; repair COVER prompt, COVER LYRIC cues, quality stack, EXCLUDE/sliders.
- final-candidate complaint: lock wins, identify highest broken layer, repair from there.

source diagnosis fields: melody age, vocal age, source texture, front density, cue obedience, lyric rushing, source strengths, source failures.
If the same complaint repeats twice, stop synonyms and rebuild one phase upstream.

# 17 — Diagnostics, Revision & Cascade

## CURRENT PATCH — Process Failure Diagnosis

If the user complains "대충 냈다 / S10 안 거쳤다 / 프롬프트가 빻았다", diagnose PROCESS first.
Cascade:
1. identify skipped stage
2. lock what user approved
3. list changed/discarded/do-not-touch axes
4. rebuild one phase upstream
5. repair CREATE/COVER/EXCLUDE/sliders
6. run measured S10
Do not answer a process complaint with another rushed 8-field package.


## CURRENT HOTFIX — Process Complaint and Locked-Lyric Repair
New complaint axis: PROCESS. Trigger words: 절차, 공정, 검수, 다 거쳐, 최종검수, 왜 바로 냈어.
Action:
1. Stop fresh 8-field output.
2. Identify skipped stage: lyric gate / CREATE audit / COVER G5 / quality stack / EXCLUDE-slider / char counts.
3. Patch highest skipped stage.
4. Re-run only affected fields unless upstream contradiction is proven.

If user says lyric is good but cover/prompt failed:
- Lock LYRIC and user edits.
- Repair COVER CREATE PROMPT / COVER LYRIC cues / COVER EXCLUDE / COVER SLIDERS first.
- Do not rewrite Korean lyric unless cue timing requires a user-approved micro-adjustment.
- Ask only if two repair strategies conflict, e.g. "더 강한 변환 vs 멜로디 보존".

COVER bad render split:
- 1 bad render: ask whether same prompt was regenerated 2-3 times if randomness likely.
- Same failure across renders: targeted COVER field repair.
- Same failure after repair: rebuild one phase upstream with 2-step transform/remaster strategy.

## TRIGGER
Any result feedback (별로야/이상해/~가 문제야); any mid-flight change (키/BPM/보컬/장르/길이/컨셉 바꿔줘); repeated complaints.

## MUST APPLY
**Step 0 — randomness split:** before redesigning, ask: same prompt, 2-3 regenerations tried? Suno is probabilistic; one bad render ≠ prompt defect. "방향 자체가 싫다" = skip to redesign. Record render_count and variance in the case; after the split, change exactly ONE variable per iteration (card 18 A/B). Lyric-quality complaint → LYRIC-REPAIR mode (card 01): diagnosis + LYRIC-only rewrite — emitting a fresh 8-field set after a lyric complaint is itself a defect.

**Symptom → prescription table** (owner codes — C=CREATE · L=LYRIC · Cv=COVER · E=EXCLUDE · S=SLIDERS; new rows carry owners):
| Symptom | Root | Fix |
|---|---|---|
| 보컬 러싱/쏟아짐 | BPM×syllable mismatch | card 06 matrix + [Pause]/[Breath] |
| 보컬 묻힘 | corridor/AI | card 15 rescue preset |
| 쏘는/거친 고음 | 2-5kHz | smooth high-mids + de-ess |
| 먹먹함 | 200-400Hz pileup | mud carve + zone split (card 13) |
| 비슷비슷/generic | macro slot 1 / memory genre | card 09 hard-reject fix + web verify |
| 올드함 | era anchor missing/wrong | 2025-26 anchor + T5 EXCLUDE |
| verse 2 랩화 | delivery drift | card 08 drift killer |
| 여자만 나옴 (혼성) | Style slot-1 missing | card 08 declaration |
| 후렴 임팩트 약함 | no lift | card 12 borrowed-chord + peak + build cues |
| 멜로디 붕 뜸 | off-chord landings | card 12 voice-leading |
| 끝이 뚝 끊김 | no [Outro]/[End] | card 05 gate |
| intro 장황 | V5 bloat | [Short Instrumental Intro: 2 bars] |
| 가사 AI같음 | abstraction/cliché | card 05 dossier + 06/07 bans |
| 짜집기 느낌 | pause spam | dashes/commas, [Pause] ≤10, "connected flowing phrases" |
| 장르 바꿨는데 안 바뀜 (transform too timid) | weak substitution / AI high · Cv·E·S | card 14 maps + source lockout + AI -10~20 [가설] |
| melody lost in cover | preserve map absent / AI low · Cv·S | card 14 preserve map 명시 + AI 65→70 [가설] |
| vocal too robotic | EXCLUDE vocal-killing words / fx stack · E·Cv | card 15 keyword guard + "natural breath texture" |
| over-reverb / crowd noise | T1 skipped / hall-everything · E·Cv | crowd lockout + "controlled reverb tails, dry-forward vocal" |
| duet collapsed to one voice | Style slot-1 declaration missing · C·L·E | card 08 declaration + labels + lockout #2 |
| 한국어 가사가 번역투로 들림 | English-first drafting · L | card 06 gate ①-⑧ full pass, 한국어로 재작성 |
| reference miss (결이 안 옴) | memory-based reference / vague decomposition · C·Cv | card 10 Feature Sheet + web verify, anchors rebuild |
| 한국어 어감 이상 (번역투 아님) | 화자/어미/일상어 검수 실패 · L | LYRIC-REPAIR — 화자 샘플 10줄부터 재작성 (card 06) |
| 산문/대본/일기 같음 | scene summary가 lyric으로 유입 · L | object/action line rewrite + 메타텍스트 ban (card 06) |
| 큐가 약함/수동적 | cue function 부재 — 묘사형 큐 · L | cue pass 재실행: 5+2 layers + renderable device ≥4 (card 08) |
| 여러 곡이 비슷함 | session expression memory 부재 · L | originality guard — 표현 ledger 대조 + object bank 리셋 (card 05/18) |

**Cascade map — one change pulls its dependents (sync BEFORE re-output):**
Key → peak-note repositioning, vocal range anchor, leap landings, sustain vowels · BPM → syllable matrix, pause density, groove feel · vocal config → Style slot-1 declaration, labels, lead-singer sync · genre jump → substitution map, 30% recheck, slot-1 anchor, pop-gravity EXCLUDE, vocal identity phrase · concept → dossier rerun, token-bias EXCLUDE, full lyric redesign · length → lyric matrix + bar counts · language → prosody card swap + full read-through. Pull unstated dependents with marked estimates ("키 바꾸면 peak note도 옮겨야 해 — [음]으로 추정"); "그것만 바꿔" disables the cascade.

**Upstream rule:** 2+ revisions on the same issue = STOP surface patching; re-diagnose slot 1, vocal keywords, era match, contour, groove, lyric tone. User starts digging through references themselves = the system already failed them.

**Revision granularity:** Micro (word/syllable) → 1-line delta · Meso (section) → rewrite section, re-emit all 8 · Macro (genre/persona/concept) → full rebuild. Default = full 8-field re-output.

## FIELD PLACEMENT
Diagnosis text precedes fields; fixes land in their owning fields per the table.

## COMPRESSION PRIORITY
Keep: randomness split, cascade map, upstream rule. Drop first: table rows (rebuild by reasoning).

## FAILURE SIGNALS
- Redesigning after a single render.
- Key changed, melody peak untouched.
- Third revision still chasing the same complaint with synonyms.

## GITHUB FETCH ROUTE
cases/failure/ for matching failure_class; prompt-patterns/diagnostics/.

## OUTPUT PHRASES
- "프롬프트 결함인지 Suno 랜덤인지부터 갈라야 해 — 같은 프롬프트로 두세 번 더 돌려봤어?"
- "키를 내리면 peak note랑 sustain 모음도 같이 움직여야 해서, 연쇄까지 묶어서 다시 뽑았어."

---

# FINAL ADDENDUM — Quality-First Diagnosis

When the user says 별로/어설퍼/획일적/창법 안 맞아, diagnose upstream before patching words:
1 vocal-fit mismatch
2 genre/groove mismatch
3 harmony/contour flatness
4 lyric speaker/register failure
5 prosody/rushing
6 arrangement density conflict
7 prompt overload
8 Suno randomness

Two failures on the same issue → stop surface patching and fetch targeted fullbody/case memory. Give fewer rules and a better redesign.

---

# PRECISION ADDENDUM — TRIAGE AND STOP LADDER

First split failures into:
1. render variance — same prompt may need 2-3 renders; not applicable to lyric text defects
2. prompt defect — the same failure repeats across renders
3. direction rejection — constraints were met but the intent lock was wrong or incomplete

Stop ladder:
- same complaint once: diagnose and apply one targeted fix
- same complaint twice: stop output, name target/cause/one strategy/fields affected, then rebuild one phase upstream
- same complaint three times: present two concrete direction options; do not keep patching words

A/B vs rebuild:
Use one-variable A/B only when diagnosis names one suspect.
If two hard gates fail or the combination itself is wrong, rebuild upstream.
## CURRENT ADDENDUM — Underbuilt Prompt Diagnosis
If user says the prompt is lazy, short, generic, or not like older strong prompts, classify as PROCESS + CREATE/COVER underbuild. Stop final fields; run current-lock; compare against gold prompt candidates; rebuild with technical density.
If same issue repeats, do not add adjectives. Rebuild upstream: genre ratio/lead axis, vocal money zone, harmony contour, instrument roles, cover maps, quality stack.

---

## 2026-06-14 CURRENT RC PATCH — Post-Render Two-Pass Diagnosis

When user feedback comes after testing in Suno, first decide which stage failed.

### CREATE-stage failure
Symptoms: melody already old, vocal age wrong before COVER, lyric rushed, source cue ignored, source instrument texture wrong, source intro empty.
Fix owner: CREATE PROMPT / LYRIC cue map / CREATE EXCLUDE / sometimes Production Bible.

### COVER-stage failure
Symptoms: source was usable but COVER made toy synth, weak drop, vocal buried, melody lost, lyric timing changed, source skin bled through.
Fix owner: COVER CREATE PROMPT / COVER LYRIC / COVER EXCLUDE / COVER SLIDERS.

### Chain failure
Symptoms: CREATE and COVER both point wrong, or final target was under-specified.
Fix owner: Production Bible + current-lock rebuild.

No third surface patch. Same render complaint twice means return one phase upstream. If user liked lyric text, lock lyric text and repair cue staging/prompt maps only.

## 2026-06-14 CURRENT ADDENDUM — Where To Start After User Says Fix It
Every repair begins by locating the stage:
A. First executable draft complaint: run production council; repair cross-field design.
B. CREATE render complaint: source audio failed; repair CREATE prompt, LYRIC cues, vocal/topline, then resync COVER.
C. COVER render complaint: final transform failed; repair COVER prompt, COVER LYRIC cue staging, quality stack, EXCLUDE/sliders first.
D. Final-candidate complaint: lock successes, repair highest broken layer only.

Do not ask the user to manually name the stage if the feedback reveals it. Infer from words:
- "CREATE에서" / "1차 결과물" = B.
- "커버했더니" / "최종 사운드" = C.
- "프롬프트/가사큐 자체가" = A unless render audio is referenced.
- "이 부분만" after liked audio = D micro/meso repair.
