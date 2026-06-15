# 19 — K-pop Artist DNA & Operator Memory Router

## CURRENT PATCH — Tatoo Alias + Multi-Mode Router

- Tatoo = Sis Tatoo = 시스타투 = 타투. Tatoo is female. Do not infer male from low/noir sing-rap wording.
- Tatoo is multi-mode, chosen per song:
  A. female low/noir rhythmic close-mic branch
  B. female sharp dry soprano-to-high-mezzo / chic deadpan branch
  C. female fragile light dry upper-mezzo/soprano branch
- Use soprano/mezzo/alto anchors when they stabilize Suno.
- Character name is a routing key. In Suno fields, write selected vocal physics unless user explicitly wants the name.
- If the render fits a different character after listening, relock concept and rebuild fields from current locks.


## TRIGGER
"[아티스트] 결로 / 느낌으로"; "Rosé 보컬 톤"; "[앨범] 사운드"; "[프로듀서] production"; K-pop group/member/era named as direction; operator invokes 임간지/Limganzi, "내 결", a case number, or a named character (Una/Sally/봉남이 etc.).

## MUST APPLY
**Artist DNA is direction, never replication.** An artist name in the user request is a routing key, NOT a prompt token. Artist names are FORBIDDEN inside Suno fields (the engine ignores or distorts them; descriptors render better). Resolve via 5-Layer decomposition: ① producer techniques ② era/scene anchor ③ instrumentation ④ vocal posture/texture ⑤ production traits — then write those as descriptors.

**Fetch route (kpop-artist-dna/):** fetch the artist-DNA index/section, extract per-member vocal detail + per-album sound keywords + producer signatures, combine with 5-Layer bypass. Quote nothing verbatim into fields — translate into functional language.

**Group vs member solo:** group request → blend/ensemble identity, section trade-offs, duet/unison labels in Lyrics. Member-solo request → single vocal identity card (5 elements: gender/age-band, weight, texture, register behavior, attitude) + that member's known stylistic axis. Never stack two members' descriptors into one voice.

**Korean-language anchor:** when K-pop direction drives an English-described prompt, anchor language explicitly — "Korean-language vocal topline", "Korean lyrics, [era] K-pop vocal production" — or Suno drifts to English phonetics.

**Era→producer mapping:** translate "2nd gen / 3rd gen / 요즘 4세대" into era + production traits (e.g., late-2000s brass-stab dance-pop with shouted gang hooks vs 2020s minimal trap-pop with whisper-to-belt dynamics). Resolve era from DNA file when named artist exists; otherwise from genre-dictionary K-pop section.

**Trend duty:** 요즘/트렌디/최신/2025-26 direction → web-verify BEFORE writing; memory-based trends forbidden; verified findings enter fields ONLY as era + producer-trait + signature descriptors — never as artist names.

**Operator memory (vault/):** ON-DEMAND only — never auto-load. Tokens that invoke it: operator name, "내 결/내 스타일로", named characters, case references. Vault content (호칭, character personas, personal preferences) NEVER appears in Suno fields or public cases; it shapes dialogue and creative defaults only. Default behavior without invocation: neutral, no honorifics, no character overlays.

## FIELD PLACEMENT
- 5-Layer decomposition → CREATE PROMPT (era/scene + production traits + vocal identity), Position 1-2 zone
- Member vocal detail → CREATE PROMPT vocal identity 5 elements + Lyrics [Singing:] cues
- Producer signature → COVER PROMPT production stack flavor (e.g., Teddy-style: hard-quantized 808 + sparse drop + chant hook → written as those descriptors)
- Album-era keywords → CREATE PROMPT instrumentation slots
- Duet/group structure → Lyrics speaker labels [Female Vocal 1/2], [Duet], [All]
- Vault preferences → dialogue tone + default choices, NEVER into fields

## COMPRESSION PRIORITY
Keep: era anchor, trend duty, vocal identity 5 elements, 1-2 producer-trait descriptors, language anchor. Cut first: album trivia, member biography, multi-era blends (pick ONE era), redundant genre macro-words.

## FAILURE SIGNALS
- Artist/member/producer name appears inside any Suno field → strip, re-decompose
- Output sounds generically "K-pop" with no era → era anchor missing from Position 1-2
- English-phonetic vocal on Korean lyrics → language anchor missing
- Two members' textures merged into one mushy voice → re-route to single identity or proper duet labels
- Vault persona leaked into lyrics/prompt or a public case → privacy violation, remove + flag

## GITHUB FETCH ROUTE
`knowledge-evolving/kpop-artist-dna/` → artist section (members/albums/producers). Era only, no artist → `knowledge-evolving/genre-dictionary/` K-pop entries. Operator invocation → `vault/operator-private/99_OPERATOR_VAULT.md` (on-demand, never cached into cases). Fetch index first, then 1 targeted section.

## OUTPUT PHRASES
- "아티스트 이름은 프롬프트에 못 들어가니까 5-Layer로 풀었어: [era] + [production traits] + [vocal posture]."
- "멤버 솔로 결이라 보컬 아이덴티티 5요소를 그 멤버 축으로 잡았어."
- "한국어 가사 앵커 박았어 — 'Korean-language vocal topline' 없으면 영어 발성으로 새."
- "이건 네 개인 결 설정이라 vault에서만 쓰고 케이스에는 안 남겨."

---

# FINAL ADDENDUM — Vocal Palette & Operator Material

Operator memory is taste material, not default style. It is invoked only by "내 결", "내 경험", case number, named character, or explicit vault reference. Extract reusable craft method, vocal tendency, genre tendency, anti-pattern, arrangement/lyric mechanism. Never extract literal hooks, titles, private personal content, or exact narratives.

## Vocal palette is separate from private vault
The character/vocal palette lives at `knowledge-evolving/vocal-palette/` and is a musical shorthand library:
Luke, Marie, Nerh, Rebecca, Ryeong, Chenny, Laini, Serica, Sally, Tepi, Kashas, Oleg, Walcott, Crader, Bongnam, Jensen, Hyeonam, Mitchell, Tatoo, Una, Martina, Tarahan, Welling.

Use names to choose vocal color and likely genre zones. Ignore role/lore labels unless asked. Convert names into English vocal descriptors. If repeated, preserve the core useful vocal identity and rotate other axes for diversity.

---

# PRECISION ADDENDUM — VOICE/LORE SEGREGATION

Vocal palette names load voice physics only by default.

Each character/vocal palette should be treated as two conceptual blocks:
[VOICE] range, weight, posture, tone, release behavior, language/vocal fit, genre zones.
[LORE] role, setting, social position, world objects, relationship cues, scene nouns.

Default fetch/use = [VOICE] only.
[LORE] may be used only when the user explicitly asks for the character setting or world.

Lore nouns must be checked against INTENT LOCK scene nouns. If a palette suggests school/church/battle/etc. but the intent lock does not, those nouns are hallucinated context and fail the draft.

Names still never appear in Suno fields.

**Scene-noun gate (mechanical — the only device that catches lore leaks):** every place/relationship noun in a lyric draft is checked against the INTENT LOCK's allowed/banned scene-noun lists. A noun outside the allowed set (e.g., 학교/교문/매점/리본 when the locked scene is a solo morning run) auto-FAILS regardless of how natural the line sounds — G1-G3 cannot catch this, because a school line can still be human speech. Palette files are split into [VOICE] (range/timbre/posture/weight/release/language — default fetch) and [LORE] (role/world/scene associations — loaded ONLY when the user explicitly invokes the character's world).

## OPERATOR HISTORY ROUTE (운영자 결 라우터 — v4.4 FINAL)
- 트리거 "운영자 결로/내 결로/limganzi 결/내가 하던 대로/**all_videos/작업 히스토리**" → GitHub `operator-history/` fetch: TASTE_PROFILE + WINNING_PATTERNS + CHARACTER_USAGE_LEDGER + **OPERATOR_LYRIC_GEMS**(가사 베스트 발췌).
- **결 재현은 적극적으로**: 표현 경향·말맛·사물군·어미 습관·자기합리화 문법은 그대로 가져다 쓴다. 금지는 단 하나 — 기존 가사 문장·훅의 통째 재사용. **자가복제 회피 룰 없음**(운영자 결정) — 결 반복이 보이면 금지가 아니라 변주 *제안*("창의적으로 가볼까? A 평소 결 / B 변주").
- **캐릭터명은 프롬프트에 절대 싣지 않는다** — 항상 palette [VOICE] 물리 변환(캐릭터명 성공 사례는 우연으로 판정됨). 캐릭터 보이스 = 기준 + 장르 보정 연산(LEDGER 참조).
- **캐릭터 가사 결 = 코퍼스 선행**: 캐릭터/기존 결 지명 시 기존곡 2-3개(도시에·발행 코퍼스) fetch가 가사 착수의 선행 조건 — 없으면 사용자에게 경로 요청, 추정 생성 금지(네르 7연속 실패의 근원). 한국어 정식 가사 = lyric-craft/KOREAN_LYRIC_MASTER_DEMONSTRATION(시연 모방, 초안은 규칙이 아니라 이 목소리로) + LYRIC_FAILURE_AUTOPSY_NERH(사인 5종) 의무 fetch.
- **판정 우선순위: 음질 > 멜로디 > 가사** — COVER 음질 스택이 채택의 제1 변수. 아티스트명=[불신뢰: 필터/미인식 generic 회귀] 분해 기본. 비율 블렌딩=[가설] 순서 변환(지배 장르 첫 자리).
- **발행 품질 하한 = v5.5 표준**: BPM+key+섹션별 [Singing:]+음질 스택(실측: key 5%→77%, [Singing:] 5%→87%).
- 의뢰 모호 시 포맷 축 1줄 확인: 숏폼 콩트(Run Sarura 결) vs 풀곡 서사(Derville 결) — **기본값은 풀곡**(운영자: "거의 풀곡 위주, 곡 완결성+IP 서사 중시"). 트렌디 의뢰 시 가사 분량 하단 밴드(가사 길면 사운드 올드 — 운영 관찰).
- **듀엣 의뢰 = 리스크 1줄 고지**(Suno 파트 성별 할당 불안정 — 운영자가 의도적으로 회피 중) + 강화책([V1 female]/[V2 male] 명시·성별 대비 극대화 서술·섹션 분리) + 실패 시 솔로 재구성 제안.
- 시작은 회의-스케치: 운영자는 자유 발화로 시작한다("신나게, 여름, 가볍게") — RUNBOOK 의식 없음. 발화에서 8값 추정 → 2-3안 맞춤 제안 → 확정 후 풀 공정.

## v4.5 라우팅 추가
- 모든 SONG-FULL/STAGED-FULL은 8필드 前 **PRODUCTION BIBLE**(≤25행, lyric-craft/PRODUCTION_BIBLE_PROTOCOL.md) 내부 작성 — 8필드는 전부 Bible에서 파생, 필드 간 모순 = Bible 위반으로 검출('짜집기' 차단). Pre-production 확인 = Bible 정수 3-5줄 1회.
- 불만 수신 = REVISION AXIS 선판정(품질/분량/방향/형식) 후 해당 축만 수리. 품질 불만에 분량 처방 금지.
- 어미/文末 단조 신고("어미 신경 써/단조로워") = 어미 분포 게이트 재가동(카드 06), 새 8필드 금지.
## CURRENT ADDENDUM — Operator Data and Prompt Banks
Operator-history data may be used proactively when the user asks for 작업 히스토리, files(27), prompt banks, 캐릭터 결, or "내가 하던 대로". Fetch/consult: machine-mined character seeds, prompt bundle candidates, style-ratio/MJ notes, and v5.5 gold candidates.
Use these as material: prompt vocabulary, vocal routing, genre zones, EXCLUDE failures, cover maps, lyric linecraft. Do not promote machine matches over user-confirmed memory. Character names still convert to voice descriptors; lore stays off unless requested.
