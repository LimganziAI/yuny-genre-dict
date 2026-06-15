# 05_NEW_CHAT_VALIDATION_SOP

Purpose: Validate that the updated GPT Instructions, 20 Knowledge files, and GitHub OS repository work together correctly in a fresh chat.

Use this SOP after updating GPT Builder Instructions and Knowledge.

---

## 0. Setup check

In the new chat, do not upload any files first. The goal is to verify whether the GPT package itself can route correctly.

Expected installed package:

- Instructions: `00_COPY_TO_GPT_INSTRUCTIONS_FINAL.txt` under 8000 characters
- Knowledge: exactly 20 md files, `01_` through `20_`
- GitHub repo connected: `playwithlawkr/yuny-suno-os`
- No optional bridge files in GPT Knowledge

Pass condition:

- The GPT understands that GitHub bridge logic is already inside the 20 md files.
- It does not ask for extra bridge md files.
- It does not claim it checked GitHub unless it actually uses the GitHub connector.

---

## 1. Identity and output-format test

Prompt:

```text
지금 네 역할과 기본 출력 형식이 뭐야? 노래 만들라는 건 아니고 설치 검수야.
```

Expected answer:

- Korean default.
- Says it is a Suno music director / lyricist / arrangement-production director / prompt engineer.
- Says normal serious deliverable is 8 fields:
  CREATE PROMPT / LYRIC / EXCLUDE / SLIDERS / COVER PROMPT / LYRIC / EXCLUDE / SLIDERS.
- Says system/package/review/diagnosis questions are audit first, not song fields.
- Does not output a song.

Fail signs:

- Outputs legacy 7-block by default.
- Starts writing a song.
- Says it needs an optional bridge md.

---

## 2. GitHub OS routing test

Prompt:

```text
GitHub는 이 GPT에서 무슨 역할이야? GPT 지식 20개랑 어떻게 분리돼?
```

Expected answer:

- Instructions = highest runtime rules.
- 20 Knowledge md = stable craft/routing knowledge.
- GitHub = growing layer: genre dictionary, K-pop/artist DNA, reference cards, prompt patterns, cases, 99 memory, archive.
- GitHub is fetched only when useful, index first, then 1-3 targeted entries/cards/cases.
- The GPT should not browse/fetch GitHub for every simple task.

Fail signs:

- Says GitHub replaces Knowledge.
- Says all GitHub files are loaded every time.
- Says optional bridge is required.

---

## 3. Genre dictionary fetch test

Prompt:

```text
장르 테스트야. Tech Para / テクパラ 스타일로 CREATE/COVER 만들려면 어떤 라우팅을 타야 해? 아직 곡 만들지는 말고 라우팅만 설명해.
```

Expected answer:

- Routes to `07_genre_library_github_index.md`.
- Uses GitHub genre dictionary index first.
- Search order: exact slug -> adjacent slug -> fallback DNA.
- If exact Tech Para entry is missing, preserve requested term and use adjacent Eurobeat + Hyper Techno + Trance + J-pop + ParaPara DNA.
- No song output yet.

Fail signs:

- Treats Tech Para as broad EDM only.
- Does not mention exact/adjacent/fallback route.
- Claims an exact GitHub entry exists without checking.

---

## 4. Lyric cue grammar test

Prompt:

```text
가사큐 검수. 듀엣 가사에서 (Female Vocal 1) 이렇게 쓰면 돼? 아니면 어떻게 해야 해?
```

Expected answer:

- Says speaker labels and non-sung instructions use square brackets.
- Correct: `[Female Vocal 1]`, `[Female Vocal 2]`, `[Duet]`.
- Parentheses are only audible ad-libs such as `(yeah)`, `(ha-ah)`.
- Should preserve useful cues like `[Breath]`, `[Held note]`, `[End]`.

Fail signs:

- Accepts `(Female Vocal 1)` as speaker label.
- Removes all cue markup.

---

## 5. COVER quality routing test

Prompt:

```text
커버 결과가 보컬이 묻히고 하이가 아프고 저역이 퍼지고 기계음 같아. 바로 문장만 바꾸면 돼? 진단 루트만 말해봐.
```

Expected answer:

- Says this is production-aware COVER failure, not surface wording failure.
- Route: 19 diagnosis -> 02 COVER mode -> 05 preserve/substitution map -> 06 full quality stack -> 03 cue/section preservation -> sliders.
- Must preserve hook, topline, lyric phrasing, section order, singer roles, signature motif before changing sound.
- Mentions full quality stack, not a shallow line.

Fail signs:

- Only says “add clearer vocals, less mud.”
- Rewrites lyric first.
- Ignores Audio Influence.

---

## 6. CREATE/COVER role separation test

Prompt:

```text
CREATE랑 COVER가 각각 무슨 역할이야? 둘을 섞으면 왜 안 돼?
```

Expected answer:

- CREATE = bone: melody identity, lyric phrasing, vocal identity, harmony/rhythm DNA, structure, signature motif.
- COVER = final body: texture, arrangement, genre transformation, production quality while preserving declared bone.
- COVER needs Audio Influence.
- CREATE should not be overloaded with final mastering details.

Fail signs:

- Says CREATE and COVER are basically the same.
- Omits Audio Influence.

---

## 7. 99 memory / operator vault test

Prompt:

```text
99_OPERATOR_VAULT는 항상 자동 적용되는 거야? 내 결이라고 할 때랑 일반 유저일 때 차이를 설명해.
```

Expected answer:

- 99 memory is on-demand only.
- Use when user invokes Limganzi, 내 결, a case number, named character, or operator pattern.
- Do not auto-apply personal vault to neutral users.
- Use it for system migration audits or explicitly invoked operator workflow.

Fail signs:

- Applies Limganzi style by default to every user.
- Ignores 99 memory entirely.

---

## 8. Failure/case loop test

Prompt:

```text
결과가 실패했을 때 성공/실패 사례는 어떻게 기록하고 언제 지식이나 지침으로 승격해?
```

Expected answer:

- observation -> case -> repeated pattern -> knowledge patch -> instruction patch.
- One success/failure is not a global rule.
- Preserve what worked, classify failure, search similar cases if useful, fix upstream, then record/propose case.

Fail signs:

- Treats one result as a global rule.
- Does not mention cases or promotion ladder.

---

## 9. Full one-shot music output test

Prompt:

```text
이제 실제 출력 테스트. 한국어 여성 솔로, 2000s Y2K R&B-pop + UK garage bounce, BPM 132, 밤비 내리는 지하철역에서 이별 직전의 담담한 고백. Suno CREATE/COVER 8필드로 줘.
```

Expected answer:

- Exactly 8 fields.
- Prompts/excludes/cues in English; lyrics in Korean.
- CREATE focuses on bone, vocal identity, groove, structure, signature motif.
- COVER includes production-aware quality stack and Audio Influence.
- EXCLUDE contains negatives; PROMPT fields stay positive.
- Lyric has clear section cues and natural Korean prosody.
- No long explanation about GitHub.

Fail signs:

- Missing COVER Audio Influence.
- Prompt field contains many negative commands.
- Lyrics become multilingual without reason.
- Uses parenthesis as speaker labels.
- Gives broad genre only, e.g. “R&B pop”.

---

## 10. GitHub live-check test

Use this only if the new GPT has GitHub connector enabled.

Prompt:

```text
GitHub 연결 검수. playwithlawkr/yuny-suno-os에서 genre index와 99 vault 첫 부분을 실제로 확인하고, 확인한 파일 경로만 말해줘. 내용 요약은 짧게.
```

Expected answer:

- Must use GitHub connector before claiming checked.
- Should check paths similar to:
  - `knowledge-evolving/genre-dictionary/index/GENRE_INDEX.md`
  - `vault/operator-private/99_OPERATOR_VAULT.md`
- Should state if it cannot access GitHub.

Fail signs:

- Claims checked without tool use.
- Invents file paths.
- Says repo is not connected when it is connected.

---

## 11. Pass/fail scoring

Score 1 point for each section 1-10.

- 9-10: install is coherent.
- 7-8: mostly coherent; inspect failed route files.
- 5-6: routing conflict likely; check Instructions and 01/07/19/20 md.
- 0-4: package install likely wrong; replace Instructions and all 20 md again.

Critical fail conditions:

- Legacy 7-block output by default.
- No 8-field serious output.
- COVER omits Audio Influence.
- GitHub optional bridge requested despite 20-file package.
- Parentheses used as singer labels.
- 99 memory auto-applied to neutral users.
- False claim of GitHub checking.

---

## 12. Repair map

If identity/output fails:
- Check Instructions txt and `04_prompt_templates_response_blocks.md`.

If GitHub routing fails:
- Check `01_core_system_router_operating_rules.md`.

If genre route fails:
- Check `07_genre_library_github_index.md` and GitHub genre index.

If 가사큐 fails:
- Check `03_suno_lyrics_tags_cues_vocal_patch.md` and `16_prosody_phonetics_sound_engine.md`.

If COVER quality fails:
- Check `19_diagnostics_revision_cascade.md`, `02_suno_engine_create_cover.md`, `05_arrangement_director_pd_layer.md`, and `06_production_design_cover_quality_full.md`.

If K-pop or 99 memory fails:
- Check `20_kpop_operator_vault_session_learning.md` and GitHub `vault/operator-private/`.

If the GPT asks for extra bridge md:
- The package installed is wrong or old. Correct package is exactly 1 txt + 20 md; bridge logic is embedded inside the 20 md files.
