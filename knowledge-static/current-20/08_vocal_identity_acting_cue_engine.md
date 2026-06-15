# CURRENT ADDENDUM — Cue/PROMPT Co-Design Loop

## Cue/PROMPT Co-Design Loop
cue-prompt sync is mandatory. A cue that names an arrangement event must be supported by the prompt's instrument/texture map; a prompt layer that must appear at a moment needs a lyric-field cue.

## Render reliability
[ ] = non-sung arrangement/section instruction. ( ) = audible ad-lib/breath/chant. [Whispered] works only after silence/drop and on short phrases. [Held] works only on open-vowel endings, 1-2 times. *asterisk* and **bold** are marginal and must not carry performance alone. Pair them with Tier-S devices: [Sudden drop], [One-bar rest], [Band drops out], [Drums cut], [Kick-only break], [Instrumental: ...], [Harmony enters], [Vocal doubles only on final phrase].

# 08 — Vocal Identity & Acting Cue Engine

## CURRENT PATCH — Vocal/Topline Firewall + Range Anchors

- Vocal tone can change without changing melody. Always separate MELODY LOCK from VOCAL TONE ONLY.
- Use range anchors when they stabilize Suno: light lyric soprano, soprano-to-high-mezzo, mezzo-soprano, low mezzo/alto, tenor, etc.
- Combine technical range with natural acting: "low-effort but centered", "tossed aside, still pitched", "keeps the room quiet", "cool deadpan without flattening melody".
- Dangerous words like spoken-like, monotone, whisper, under-sung must be paired with melody protection or moved to EXCLUDE if they cause drift.
- Cues for voice: [One-beat rest], [Two-beat rest: piano only], [Band softens], [Harmony enters only on final phrase], [brief narrow-radio aside] when justified.


## CURRENT HOTFIX — COVER Cue Render Protection
When COVER feedback says cue events did not render, rebuild cue pass after the COVER prompt, not before it.
Use few, loud events:
- [One-bar rest] before a critical shout
- [Sudden drop] before hook return
- [Band drops out] for bridge reset
- [Harmony enters] only where harmony must appear
- [Vocal doubles only on final phrase] for final line emphasis
For stereo/group response, write cues as lead/backing function: center lead, wide gang response, hook doubles L/R. Do not spam more than the song can parse.

## TRIGGER
Every song; any 보컬/창법/듀엣/혼성/목소리/딜리버리 utterance; 가사큐 부실 feedback.

## MUST APPLY
**5-element vocal anchor — first line of every LYRIC field:**
① gender+range ② core tone 1-2 words ③ section behavior (verse vs chorus role contrast — NOT technique change) ④ genre inflection ⑤ special technique/negation. Mirror ①②④ into CREATE prompt slots 1-3 (Style↔Lyrics sync).

**[Singing:] cue — every section, 7 elements, one bracket, ≤120 chars, English:** voice placement · dynamic · mic distance · phrasing · expression · mood · backing arrangement. Density scale: Intro·Outro 1-4 / Verse 3-5 / Pre-Chorus 4-6 / Chorus 5-7 / Bridge 4-6 / Final Chorus = Chorus + evolution cue ≥1 (key lift, stacked harmony, or ad-lib layer — exactly ONE new lift, no pile-up). 12+ bar sections get a 2nd cue mid-way. Cue purpose per section (no cross-section copy-paste): Intro = 곡의 온도+motif 제시 · Verse 1 = 화자 거리감·말투 고정 · Pre = pressure · Chorus = hook 가창성+size+backing · Post = motif 회수 · Verse 2 = 새 정보, 같은 말투 · Bridge = 말하지 않는 전환 · Instrumental = 가사 대신 감정 처리 · Final = 단 하나의 진화 · Outro = 마지막 이미지 고정.

**Cue = function, not description (5+2 layers):** every section cue designs ① voice placement ② dynamic ③ mic distance ④ phrasing/breath/pause ⑤ arrangement event. High-stakes sections (Chorus/Bridge/Final) add ⑥ emotional action as a VERB (삼킨다/버틴다/내려놓는다 — not mood adjectives) ⑦ ≥1 renderable device.

**Renderable devices (commands BETWEEN lyric lines — describing is not directing):** [Breath] · [Held] · [Whispered] (only after silence) · [Sudden drop] · [Band drops out] · [Drums cut] · [One-bar rest] · [Harmony enters] · [Vocal doubles only on final phrase]. Minimum 4 per song, placed at real positions between lines. A cue that only describes and never commands = defect.

**Anti-쏟아짐 (breath architecture):** every section gets ≥1 explicit vocal rest BETWEEN lines ([Breath]/[One-bar rest]/[Held]) — default spots: end of Pre, the bar before Chorus, right after Bridge. 8+ consecutive lyric lines with no rest device = defect.

**Let the band speak:** Bridge/Instrumental never explain the emotion in words — the arrangement carries it ([Band drops out] / [bell motif alone]). Instrumental sections take [Instrumental: ...] cues, never [Singing:].

**Cue-lyric interaction check:** what a cue commands (breath/stop/harmony/drop) must fit the exact line it touches — length·어미·vowel. Don't throw [Whispered] at a 10-syllable run; put [Held] on an open-vowel ending.

**Mic distance 5-step:** inside(ASMR) / close(intimate, breath) / mid(balanced) / mid-back(roomy) / hall(cinematic). Vary by section — one distance全곡 = flat. Placement: chest-forward / head / mixed-belt.

**Backing cues mandatory in Chorus/Bridge/Final** inside [Singing:]: "strings swell underneath", "band drops out leaving only vocal", "drums cut to half-time".

**Multi-voice grammar:** speaker labels [Female Vocal 1] / [Female Vocal 2] / [Male Vocal] / [Duet] / [V1+V2] — brackets only, never "V1:" prefixes, never parentheses. Style prompt slot 1 MUST declare it: mixed = "Mixed male and female vocals throughout, [lead] opening verses, alternating duet chorus"; duet = "Female duet, vocal 1 [range] and vocal 2 [range] trading lines, unison on chorus"; group = "[gender] group vocals, distinct timbral identity per member, both vocals prominent throughout". Lead-singer choice synced: Style line + anchor + section labels.

**Delivery consistency (verse-2 rap drift killer):** section behavior = role contrast, not technique swap. Sung song → every verse sung: (a) anchor carries "sung throughout, melodic delivery in every verse" (b) verse 2 [Singing:] repeats a sung descriptor (c) rap-gravity genres add EXCLUDE "rapping, spoken-word delivery, rap verse". Rap appears only when intended → [Rapping] tag explicitly.

**What Suno actually renders (write to this):** RENDERS: ALL-CAPS word/line (1-2×/song), vowel stretch (lo-o-ove / Loooove), [bracket] cues ([Whispered][Belted][Held][Airy][Raspy]), (BGV) inline ad-libs, pipe stacks [Chorus|Anthemic|Stacked]. MARGINAL (never alone — pair with a RENDERS device): *asterisk* emphasis, exact stress placement, **bold**, quotes. (whisper:) only directly after [Sudden Absolute Silence: 1 bar]. [Pause] total ≤10 per song; connect lines with dashes/commas, not pause spam.

## FIELD PLACEMENT
Anchor+cues+labels → LYRIC. Vocal identity ①②④ → CREATE prompt. Identity preservation phrase → COVER prompt. Anti-drift → EXCLUDE.

## COMPRESSION PRIORITY
Keep: anchor 5, [Singing:] 7, density scale + section purpose, 5+2 layers, renderable-device minimum + anti-쏟아짐, label grammar, drift killer, RENDERS list. Drop first: mic poetry.

## FAILURE SIGNALS
- Mixed-vocal song outputs one singer (Style slot-1 declaration missing).
- Verse 2 came out rapped on a ballad.
- *asterisks* doing all emphasis work.
- Same [Singing:] copy-pasted across sections.
- Final Chorus stacked with 2+ new lifts (over-stuffed) or zero evolution.
- A section cue that describes mood but commands no event (zero renderable devices where required).
- [Singing:] cue on an instrumental section.
- 8+ consecutive lines with no rest device — 가사 쏟아짐.

## GITHUB FETCH ROUTE
prompt-patterns/lyric-cues/ for cue stacks; archive/fullbody-legacy/12_vocal_production_direction.md.

## OUTPUT PHRASES
- "혼성인데 여자만 나온 건 Style 1번 자리에 'Mixed vocals throughout' 선언이 빠져서야 — 박았어."
- "verse 2 랩화는 Suno 표류 버그라, sung 명시 + EXCLUDE rapping 이중으로 잠갔어."

---

# FINAL ADDENDUM — Vocal Fit & Palette Integration

## Vocal Fit Pass
Before CREATE/COVER, infer:
1 posture: chest/mix/head/falsetto/speech/belt/whisper/rasp/nasal/airy
2 weight: thin / thin-to-medium / medium / thick
3 comfort range and peak zone
4 release behavior: held belt, falsetto flip, breath tail, vibrato, straight tone, run
5 matching key/mode and chord-tone peak
6 BPM syllable density + rest needs
7 arrangement density and corridor risk
8 lyric register the voice can carry.

Vocal change cascades: technique → key/range → peak note → BPM syllable density → lyric register → arrangement density → EXCLUDE → COVER quality.

## Vocal Palette Route
When a recurring character/vocal name appears, fetch `knowledge-evolving/vocal-palette/INDEX.md` and one targeted character file. Treat the name as a vocal palette seed, not fixed lore. Convert to Suno descriptors; never put character names in fields. If the song needs another posture, adapt the palette. Repeated same palette → rotate genre, groove, arrangement, lyric register, or section role.

---

# PRECISION ADDENDUM — CUE SUBORDINATION

Cues are subordinate to the lyric. They cannot rescue a dead lyric.

Cue-replacement test:
Before output, mentally remove all [Singing:] and renderable device cues. If the lyric no longer works as a song or the emotion only exists in the cues, return to lyric repair.

Cue narrative ban:
Cues describe HOW the vocal/arrangement performs: placement, dynamic, mic distance, breath, pause, device, backing event.
Cues may not carry the WHAT of the story. Do not put plot, metaphor, or missing emotion into cues.

Device quota is a minimum, not a target. Avoid cue spam. Renderable devices must sit between the exact lines they affect, not be dumped at section ends.

**CUE DEVICE HIERARCHY (실사용 기준 — 전체 라이브러리: suno-render-behavior/cue_device_library.md):**
- **Tier-S 구조 이벤트(가장 신뢰)**: [Instrumental: …] · [Band drops out] · [Sudden drop] · [One-bar rest] · [Harmony enters] · [Vocal doubles only on final phrase] · 섹션 태그 — 편곡 레벨 지시는 렌더가 잘 받는다. 섹션 전환·에너지 설계는 여기서 한다.
- **Tier-A 보컬 연출(조건부 강함)**: 섹션별 [Singing:](≤120자, 영어) · [Breath](훅 직전/긴 런 직후) · **[Whispered]는 드랍/휴지 직후의 짧은 행에서만 작동** — 고에너지 한복판·긴 행에선 깨진다 · **[Held]는 행 끝 열린 모음(ㅏ/ㅗ/ah/oh)에서만, 곡당 1-2회** — 받침 파열음·행 중간에선 깨진다.
- **Tier-B 채색(메인 제어 금지)**: ALL CAPS(1-2 단어 외침) · 모음 늘임 표기(사라져어—/lo-o-ove — 지속 힌트로 실효) · 인라인 (BGV)/애드립 괄호(독립 행 금지) · ***asterisk*는 장식적·미약** — 단독 과신 금지, CAPS나 늘임과 페어링.
- **수량과 과감함**: device ≥4 그리고 ≤행수÷3, 닿는 행 *사이* 실배치(섹션 끝 더미 금지), 큐 텍스트에 서사 0(HOW만). 단 설계된 2-3 순간엔 과감하게 스택([Sudden drop]+[Whispered]+[Held]는 정당한 설계 이벤트다).
**CALL-RESPONSE 배치 (호응 기준 — 큐는 가사 이벤트에 대한 응답이다):** 큐 위치는 임의가 아니라 가사 이벤트가 부른 자리다 — 고백 직전=[Band drops out](직후 행이 최강 행일 때만) / 훅 진입=[Breath] 또는 [Sudden drop] 중 1 / Final 변이 행=[Held]+옥타브 점프 또는 [Harmony enters] / 브릿지 항복=스택 합법 / 엔딩 잔향=드랍 직후 [Whispered] 짧은 행 / 콩트 오프닝=인트로 보컬 첫 줄 식별 애드립. 전체표: suno-render-behavior/cue_call_response_grid.md.
**행 끝 어미와 호흡:** 견인 행(-고/-서/-는데 끝) 뒤 [Breath] 금지 — 흐름 절단. 호흡은 완결 어미 행(-어/-야/-지/!) 뒤에만. ? 반문 뒤 = 침묵 또는 [Pause half bar], 즉답 큐 금지. 섹션 큐 수 ≤ 그 섹션의 가사 이벤트 수.
**듀엣 파트 할당 [운영 관찰]:** Suno는 성별 파트 배정이 불안정(여 파트를 남이 부름) — 듀엣 의뢰 시 리스크 1줄 고지 + [V1 female]/[V2 male] 명시 + 성별 대비 극대화 보컬 서술 + 섹션 단위 분리, 실패 시 솔로 재구성 제안.
- **비작동 확정형**: 인라인 (whisper:) 무효 — [Whispered] 디바이스로. 카메라 지시·감정 형용사만 있는 큐 = 노이즈.
## CURRENT ADDENDUM — Performance Marking and Radio/Emphasis Devices
Use renderable cues before weak typography. Asterisks may add tiny emphasis but cannot carry performance. For spoken/quoted fragments, prefer a structural setup: silence/drop/rest first, then a short [Whispered] or narrow-radio line if the phrase is brief and singable.
Radio/narrow color is a vocal treatment for a specific tossed phrase, not a whole-section default. It must not steal pitch or lyric intelligibility.
After a lyric is locked, create a cue map: rests, drops, held vowels, harmony entry, final-line double, instrumental handoff. Cue density follows lyric events, not decoration quotas.

---

## 2026-06-14 CURRENT RC PATCH — Two-Pass Cue Map

Cue design now has two maps.

### CREATE cue map
Purpose: make the source audio sing correctly.
Controls:
- vocal posture and mic distance
- talk-sing vs sung vs chant
- breath grid and anti-rushing
- source hook timing
- one peak note runway
- motif/instrumental handoff
- section length and final source gesture

### COVER cue map
Purpose: make the final record hit correctly.
Controls:
- cold-open or no-empty-intro density
- whisper pickups before drops
- hard stops and one-beat cuts
- kick/bass-only breaks
- drop-cell isolation
- vocal chop material
- final chorus doubles
- final held/cut gesture

If COVER feedback says cue events did not render, rebuild cue pass **after** the COVER prompt, not before it. COVER LYRIC may repeat fewer words with stronger devices. Asterisks and bold are marginal; [Sudden drop], [One-bar rest], [Band drops out], [Whispered], [Held], [Vocal doubles only on final phrase] carry the real control.
