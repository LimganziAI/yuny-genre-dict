# CURRENT PATCH — Japanese/English/Global Lyric Function Extension V2

## Transfer principle
Do not translate lines; transfer function. Preserve the song's role of each section, hook function, speaker pressure, and final residue while rebuilding prosody and register for the target language.

## Japanese
Choose register before wording: casual, literary, band, idol, anime-adjacent, city-pop, theatrical. Count mora, not syllables; long vowels, small っ, and ん consume time. Favor image return, omission, particle stance, and controlled residue over Korean-style explanation. A Japanese hook often works as recurring image or short decision, not argument. 체언종지/unfinished endings are powerful only when the register supports them.

## English/global
English is stress-timed. Put content words and hook/title payloads on strong beats. Choose rhyme family intentionally: perfect = closure, family/slant/assonance = openness or instability. Idiom safety is mandatory; never literal-translate Korean idioms or Korean ending temperature. Global hooks should be short, pronounceable, and immediately repeatable without becoming cliché.

## Bilingual seams
Switch language at section boundary or hook event, not random mid-line. One language remains the emotional home; the second may carry title, chant, texture, or global mouthfeel. Match vowels across the seam when possible. Section function outranks line-by-line meaning.

---

# 07 — English / Japanese / Spanish Lyric Cards

## TRIGGER
Lyric work in EN/JP/ES, or bilingual songs touching these languages.

## MUST APPLY — ENGLISH
- Accent is a decision: unspecified = neutral = flavorless. Specify in vocal anchor ("educated California English accent", "Pacific Northwest soft", "RP-adjacent"). Pronunciation override (IPA-like respelling) on ≥1 killing line per section when diction matters.
- Stress alignment: stressed syllables on strong beats; content words on peaks; connected-speech hazards (catenation/elision/flap-T) ≤3 per line — pile-ups smear diction.
- Rhyme hierarchy: perfect < family < additive/subtractive < assonance < consonance — choose for emotional stability (perfect = closure, assonance = unresolved). Lazy-rhyme pairs (fire/desire, heart/apart) banned.
- Verb wattage audit: replace is/get/go-class verbs where a strong verb lands. AID: verses max Action+Imagery+Detail; chorus leans Imagery.
- Stance models (function, not phrasing): Mitchell precision, Cohen gravity, Ocean fragment-collage, Rodrigo conversational spike, SZA run-on intimacy.
- Register decision FIRST: conversational vs literary diction (genre stance decides). Idiom safety: only idioms verified in real usage — no invented collocations. Cliché-rhyme blacklist beyond fire/desire: tonight/alright, rain/pain, cry/goodbye, love/above.

## MUST APPLY — JAPANESE
- Count mora, not syllables; long vowels/っ/ん each take a beat. Lines breathe at 5-7 groupings when the genre allows.
- Aesthetics through craft: mono no aware via concrete object + time mark; yugen via indirection (say the shadow, not the thing); taigen-dome (noun ending) for resonance; kireji-like cuts with — / … / unresolved line.
- Particles minimal on peaks AND on weak beats; implied subject default; no romaji ever in lyric body; katakana loanwords only when the persona would use them.
- Register map decision FIRST — one per song: casual male/female · literary · idol · band · anime · city-pop. Mixing registers mid-song = instant fake.
- Never echo a reference track's phrasing — original expression only.

## MUST APPLY — SPANISH
- Count with sinalefa (vowel elision across words) — written syllables ≠ sung syllables. Stress (agudas/llanas/esdrújulas) must land on strong beats; final agudas suit hook ends.
- Open-vowel hooks (a/o) stretch best. Register decision first: neutral Latin vs Iberian vs regional (voseo? slang?) — mixing registers = instant fake.
- Duende = directness: bodily, earthy verbs over abstractions; one image per line.

**New-language extension (when any other language arrives):** fill language_lyric_engine.template.md (GitHub) — core prosody unit · register map · common lyric idioms · forbidden translationese · rhyme/assonance system · hook vowel strategy · cultural cliché guard · research requirement · acceptance tests. No language ships without its template filled.

## MUST APPLY — BILINGUAL
One section = one language. Non-target sections cue "all lyrics in [lang], no [other]". Style prompt declares "bilingual, Korean verse, English chorus"-style map. Cross-language rhyme prep: bridge the seam with shared vowel color.

## FIELD PLACEMENT
All → LYRIC. Accent/diction → vocal anchor line (card 08) + Style prompt vocal slot. Language map → Style prompt + section cues.

## COMPRESSION PRIORITY
Keep: accent duty + register decision (EN), mora rule + register map (JP), sinalefa+register (ES), one-section-one-language. Drop first: stance models.

## FAILURE SIGNALS
- EN: no accent stated; fire/desire rhyme; 4 linked weak verbs.
- JP: syllable-counted lines; romaji; reference phrasing echoes.
- ES: stress off-beat; register salad.
- Bilingual: mid-section language flip (pronunciation drift).

## GITHUB FETCH ROUTE
lyric-expression-banks/ per language + language_lyric_engine.template.md (new-language onboarding); archive/fullbody-legacy/14_lyric_craft_english.md & 15_lyric_craft_japanese_spanish.md for deep dives.

## OUTPUT PHRASES
- "Accent 안 박으면 무국적 발음이 나와서 'educated California English'로 고정했어."
- "일본어는 음절이 아니라 모라로 셌고, 체언 종지로 여운 처리했어."

---

# FINAL ADDENDUM — Japanese Full Mode

Use Japanese Full Mode for Japanese lyrics, J-pop, anime-adjacent, Japanese city-pop topline, or when the user says Japanese quality matters.

Gates:
- Count mora, not syllables. Long vowels, っ, and ん each occupy time.
- Pick one register: casual feminine/masculine, literary, band, idol, anime, city-pop, vocaloid-adjacent.
- Balance kanji/hiragana/katakana for texture. No romaji in lyric body.
- Use image return, moraic assonance, parallelism, and omission more than English-style end rhyme.
- Avoid reference phrasing echoes.
- Use taigen-dome/kireji-like cuts only when the register supports them.
- Build mono no aware/yugen from object + time mark + absence, not abstract statements.

Fetch `knowledge-evolving/multilingual/JAPANESE_LYRIC_ENGINE.md` when Japanese is a primary quality axis.

**Conflict rule (all languages):** when a prosody instrument (stress/mora/sinalefa/rhyme) collides with speaker truth, speaker truth wins — find another phrase, re-split the line, or bend the melody. Never bend the speaker to fit the meter. New-language hard-gate order: register map → translationese blacklist → comprehension test in that language; prosody tables enter only after these three exist.

## v4.5 — 전 언어 공통법 (JA/EN/ES)
① **분량 역산 금지(LENGTH LAW)**: 글자수는 결과. 숫자를 채우려 행을 추가/삭제 = 결함(JP 실증: 3000자 맞추려 '少し軽く笑える' 패딩 후 'もう少し軽く笑える' 재패딩).
② **文末/어미 분포 게이트**: 동일 文末 3연속 금지 — 〜ないで/〜たい/〜いいな 연쇄가 실증 결함. 곡 전체 ≥5형.
③ **목소리 우선(WRITE-THEN-CHECK)**: 초안은 코퍼스·시연 모방으로, 언어 크래프트 카드는 검사용. 자기긍정 스톡 문구 연쇄(寂しさを責めないで/泣かない理由じゃなくて/明日へ歩いてみるよ 류) = G1 위반 — 화자의 구체물·장면·고유 화행으로 회귀. 추상 감정 진술 90행에 구체물 2개면 가사가 아니라 표어다.
