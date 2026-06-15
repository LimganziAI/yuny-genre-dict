# 14. PROSODY AND PHONETICS — MULTILINGUAL ALIGNMENT REFERENCE
# Version: 3.6 (YUNY v2.11 — Suno-tested Syllable Rules + 27-Item Gate)
# Scope: Prosody and phonetic gates for Korean, English, Japanese,
#        Spanish lyric writing; cross-linguistic prosody comparison;
#        Stable/Unstable framework; Suno engine realization gates;
#        27-item pre-output gate checklist (v2.11 expansion).
# Use: Final validation pass for lyrics before output. Run *every
#      output* through SECTION 7 (or its subset).
# Working language: Korean dialogue, multilingual technical content.

---

## VERSION 3.5 — WHAT CHANGED AND WHY

v3.0 was a solid prosody reference with Korean / English / Japanese /
Spanish coverage. The 2026-05-22 session diagnosis identified two
critical gaps that v3.0 couldn't reach:

1. **No Stable/Unstable framework.** Pat Pattison's Stable/Unstable
   tool is the universal lens through which all craft decisions
   make sense. v3.0 referenced it but never codified it as a *gate*.
2. **16-item gate insufficient.** Operator's session-level diagnoses
   surfaced 6 additional failure modes (translationese after Style
   Box, verb wattage, AID gaps, cliché surge, persona drift, melody
   marriage). v3.0 caught some, missed others. Gate expanded to 22.

v3.5 adds:
- **§5.5 Cross-linguistic Stable/Unstable Map** — how each language
  realizes the spectrum
- **§7 22-item Gate** (was 16) — covers all session-level failure
  modes
- **§8.5 Konglish Prosody Negotiation** — when English hook + Korean
  verse syllable density collide

Preserved: §1-4 prosody by language, §4bis Spanish, §6 Suno
realization, §9 specificity, §10 example.

---

## SECTION 0. PURPOSE

This file is the **final phonetic and prosodic validation pass**
before lyric output. Every lyric that ships through YUNY runs
through the 27-item gate in §7 (v3.6 / v2.11 expansion).

The file does not generate lyrics. It validates them. Generation
happens upstream in 07 (Korean), 08 (English), 17 (Scene Dossier),
and the Suno templates (10, 12). This file catches what slipped.

Failure modes this file catches:
1. Syllable / mora / beat misalignment
2. Translationese surface
3. Forced rhyme / cliché rhyme
4. Tongue twisters Suno can't sing
5. Tense / persona / POV drift
6. Vowel-consonant cluster problems
7. Phrase-end mismatches with melody
8. Verb wattage too low
9. AID gaps in verses
10. Stable/Unstable arc broken

---

## SECTION 1. THE THREE-LAYER ALIGNMENT MODEL

A lyric line works when three layers align:

1. **Phonetic Layer** — How the words *sound* (syllable structure,
   vowel/consonant balance, singability)
2. **Prosodic Layer** — How the words *fit the rhythm* (stress
   patterns, beat alignment, phrase length)
3. **Semantic Layer** — How the words *mean what they should*
   (precision, persona match, scene continuity)

When all three align: prosody (in Pattison's sense — appropriate
relationship between elements).

When one breaks:
- Phonetic off → Suno mumbles, slurs, mispronounces
- Prosodic off → vocal feels rushed or dragged, lines don't sit
- Semantic off → message doesn't land

The 27-item gate (§7, v3.6) checks all three layers.

---

## SECTION 2. KOREAN PROSODY GATES

### 2.1 Korean = syllable-timed

Each syllable takes roughly the same time. Stress does *not* change
meaning. Implications:
- Stress-based rhythm rules from English do not transfer
- Syllable count vs BPM is the primary alignment tool
- 받침 (final consonants) shape singability heavily

### 2.2 Syllable count × BPM table

| BPM range | Syllables / line | Notes |
|---|---|---|
| 60-80 | 6-9 | Ballad, ample breath |
| 80-100 | 7-10 | Midtempo |
| 100-120 | 7-11 | Mid-up / R&B |
| 120-140 | 6-10 | Dance pop / K-Pop main |
| 140-160 | 5-9 | Uptempo dance, hyperpop |
| 160-180 | 4-8 | Punk, drill |
| 180+ | 3-7 | Extreme tempos |

Lines exceeding upper limit → Suno rushes, lyrics blur.
Lines below lower limit → Suno stretches notes, creates artificial
melisma.

### 2.3 받침 (final consonant) load

Final consonants close syllables:
- 받침 없는 음절 (open syllable, vowel ending): soft, can sustain
  long notes (사랑 → 사 sustains)
- 받침 있는 음절 (closed syllable, consonant ending): hard,
  short notes (꿈 → cannot sustain naturally)

#### 받침 ratio by tempo
- ≥130 BPM: ≤50% syllables with 받침
- 100-130 BPM: ≤60% 받침
- ≤100 BPM: ≤70% 받침

#### 받침 cluster danger
3+ consecutive 받침 syllables = Suno breakdown:
- "값 있는 빛깔" (3 closed syllables) — *fails*
- Spread closed syllables across line, alternate with open

### 2.4 Vowel harmony (모음조화)

Korean vowels group:
- 양성 (bright/light): ㅏ ㅗ ㅑ ㅛ
- 음성 (dark/heavy): ㅓ ㅜ ㅕ ㅠ
- 중성 (neutral): ㅣ ㅡ ㅔ ㅐ

Onomatopoeia / mimetic words follow strict harmony:
- 반짝반짝 (bright) vs 번쩍번쩍 (dark) — both work, different feel
- 쿵쾅쿵쾅 (bright cousin) vs 쿵쾅쿵쾅 (mixed — common in K-Pop)

#### Gate
- Mimetic words must follow vowel harmony
- Mixed harmony in non-mimetic OK but watch for accidental
  uncomfortable mixes

### 2.5 Translationese gate (referenced from 07 §5)

After Style Box (English), before Korean lyric write, *conscious
mode shift*:
- "~의 ~" — max 1 per line, 2 per chorus
- Inanimate subject (물주구문) — ban
- Subject over-specification ("나는 / 너를") — minimize
- Passive direct translation ("~게 되었다") — ban
- Relative clause direct translation ("~하는 사람의") — minimize
- Tense over-specification ("~았었다") — ban
- Abstract noun reliance ("~의 것이다") — minimize

### 2.5.5 Korean natural-phrasing audit (v2.11 NEW — from Case 41)

Operator discovery (Case 41 v2.10 session):
> *"한글로 지랄해도 어차피 안 감겨서 차라리 쪼개는 게 나음"*

Korean lyrics that "don't stick" / "don't catch" have three diagnosable
causes. Run *before* output, alongside §2.5 translationese gate.

**Diagnostic A: Run-on syllable cluster**
- ❌ "어차피내일도same old song" (no spacing, mixed romaji+English)
- ✅ "어차피 내일도 same old song" (natural 어절 spacing)
- Suno parses 어절 as breath unit. No spacing = forced compression.

**Diagnostic B: Romanization leak**
- ❌ "ileul ttwieo" / "il-dan ttwi-eo" (romaja in lyrics field)
- ✅ "일단 뛰어" (Hangul direct)
- External research (HookGenius Korean guide 2026): *Always use Hangul.
  Suno processes Hangul much better than romaja.*

**Diagnostic C: 받침 cluster + tempo mismatch (§2.3 connection)**
- 145+ BPM + 받침 ratio >50% = mumbled output
- 65+ BPM + 받침 ratio <20% = airy/weightless output
- Match tempo to consonant load (§2.2 table).

### 2.6 Concept ↔ Lyric ↔ Vocal Anchor consistency (v2.11 NEW)

Three layers must agree. Mismatch = "concept doesn't land" / "vocal
feels off" / "section transition jarring" diagnoses.

**Layer 1: Concept (Brief Lock §7.3)** — what the song is *about*
**Layer 2: Lyric content** — words on the page
**Layer 3: Vocal Anchor (C-29 5-element)** — how it's sung

**Consistency gate (per section):**

| Section | Concept signal | Lyric signal | Vocal Anchor signal |
|---|---|---|---|
| Verse 1 | introduction / mood-setting | concrete imagery, AID | conversational, behind-beat |
| Pre-Chorus | tension build | rising semantic field | glissando, doubled entry |
| Chorus | core statement | hook line FIRST | belt, harmony stack |
| Bridge | shift / breakdown | new POV or memory | stripped, intimate |
| Final Chorus | resolution / amplification | hook + ad-libs | maximum belt, stacked |

**Failure detection:**
- *Verse uses chorus-level imagery* → re-rank section function
- *Vocal Anchor says "intimate" but chorus says "explosive"* → conflict
- *Bridge has same Persona as Verse 1* → bridge missing its shift

**Fix workflow:**
1. Map each section's Concept signal (1 line)
2. Map each section's Vocal Anchor signal (1 line)
3. Re-read lyric — does the section's *signal* match?
4. If no, revise *lyric*, not concept (concept is locked).

### 2.7 Syllable-beat alignment — Suno-tested (v2.11 NEW)

External research synthesis (HookGenius, Suno v5.5 docs, Reddit
r/SunoAI compiled studies):

#### 2.7.1 Suno-safe line lengths (per language)

| Language | Reliable zone | Past this → rushing/smear |
|---|---|---|
| English | 6-12 syllables | 15+ |
| Korean | **6-10 음절** (denser per character) | 12+ |
| Japanese | 6-12 mora | 15+ |
| Spanish | 6-12 syllables (with sinalefa) | 15+ |

Rule: If a line is loaded, *break it*. Two 8-syllable lines always
out-sing one 16-syllable line. The model breathes in the gap.

#### 2.7.2 Stress-kick alignment (English / Spanish)

Suno places vocal stress on the strong beat. Write so:
- Stressed syllable of each line lands on **beat 1 or 3** (strong)
- Unstressed on **beat 2 or 4** (weak)

✅ "DANcin' in the MOONlight" (trochaic, kick on 1 & 3)
❌ "the DANcing of the MOON in the sky" (iambic + run-on)

Write *against* the stress → Suno fights you (rushing, mumbling, or
syllable-shifting to force the match).

#### 2.7.3 Korean: 어절 strong-position rule

Korean = syllable-timed. *Each 어절's first syllable* gets natural
emphasis. Place these on strong beats.

✅ "**일**단 **뛰**어" (1st syllable each = strong beat)
✅ "**카**드값 **또** 뛰어" (lexical heads on beats)

#### 2.7.4 Section first-line hook landing

Suno gives **maximum melodic weight** to the FIRST LINE of each
tagged section. Implications:
- Chorus: hook line goes FIRST (not buried at line 3)
- Verse: most-singable line opens
- Bridge: tonal shift line opens

Choruses work best at 2-4 lines total. Above 4 lines, Suno may
*re-weight* and bury the original hook.



### 2.8 Korean sentence-ending palette

| 어미 | Register | Effect |
|---|---|---|
| ~야 / ~지 / ~네 | Informal | Friendly, peer |
| ~어 / ~지 / ~데 | Informal-soft | Intimate |
| ~다 / ~어! / ~지! | Declarative | Punchy, declarative |
| ~요 / ~어요 | Polite | Respectful, distant |
| ~ㅂ니다 / ~ㅂ니까 | Formal | Ceremonial, news |
| (생략) | Poetic | Modern, lyrical |
| Noun ending | Poetic | Cinematic still-frame |

Gate: persona-aligned ending palette per song. Mixing within a
section = drift.

### 2.9 Korean pre-output phonetic gate (9 items, v2.11 +1)

1. [ ] Syllable count per line ∈ BPM range (6-10 음절 safe — §2.7.1)
2. [ ] 받침 ratio ≤ tempo limit
3. [ ] No 3+ consecutive 받침 clusters
4. [ ] Vowel harmony respected in mimetic words
5. [ ] Translationese 7 patterns clear
6. [ ] 어미 palette persona-consistent
7. [ ] No untranslatable cultural terms unexplained
8. [ ] **Hangul direct, NO romaja** (v2.11 strengthened — Suno
       processes 한글 much better than romanization)
9. [ ] **자연 어절 spacing applied** (v2.11 NEW — §2.5.5 / no
       run-on, each 어절 = breath unit)

---

## SECTION 3. ENGLISH PROSODY GATES

### 3.1 English = stress-timed

Stress positions are fixed in words; misplacing them on melody
creates "greedy spots" (Pattison) — listeners feel the line as
rushed or unnatural.

### 3.2 Stress-syllable alignment

Word stress examples:
- One syllable: free placement
- Two syllables: TR-O-ched (BRIDE-groom) or i-AM-bic (re-LATE)
- Three syllables: PRE-fer-red, of-FEN-sive, in-VI-ted

Place stressed syllables on:
- Beat 1 (strongest in 4/4)
- Beat 3 (second strongest)
- Match strong-weak words to strong-weak musical positions

Misalignments:
- "come BACK" set as "COME back" → wrong stress → unnatural
- "tomorrow" set as "TO-morrow" → wrong stress → robot delivery

### 3.3 Syllable count guide (English)

Same as Korean §2.2, slightly different sweet spot:
- 6-12 syllables per line (most pop)
- Hip-hop / rap can go higher (12-20+ for dense flow)
- EDM hooks tighter (4-8)

### 3.4 Pronunciation traps for Suno

Suno mispronounces by pattern, not understanding. Common traps:

| Pattern | Example | Fix |
|---|---|---|
| Homographs | "read" (present vs past) | Phonetic spell: "reed" / "red" |
| Silent letters | "knight" | Often OK in v5, but "rite" or context fix |
| Acronyms | "NASA" | Spell out or "naa-saa" |
| Numbers | "2026" | "twenty twenty six" |
| Names | "Caoimhe" | "Kee-va" |
| Loanwords | "rendezvous" | "rond-ay-voo" |

### 3.5 Vowel quality for sustained notes

Suno sustains best on:
- Long open vowels: ah, oh, ee, oo, ay
- Diphthongs: ay (way), oh (go), eye (high)

Suno struggles to sustain:
- Short vowels: i (bit), u (cup), a (cat) — pinched on long notes
- Schwa (uh): always weak, never put on a strong note

Gate: held notes (whole/half) get long vowels.

### 3.6 Consonant cluster gate

Suno chokes on:
- 3+ consonants in a row across word boundary
  ("just stretch" → s-t-s-t-r → mush)
- Word-final cluster on quick syllable ("strength" sustained)
- Plosive on whisper section ("p, t, k" + soft vocal = pops)

### 3.7 English pre-output phonetic gate (8 items)

1. [ ] Stressed syllables on stressed beats
2. [ ] Syllable count in BPM range
3. [ ] No mispronunciation traps (or phonetic-spelled)
4. [ ] Long vowels on sustained notes
5. [ ] No 3+ consonant clusters at boundaries
6. [ ] Plosives matched to vocal dynamic
7. [ ] Hook 6-12 syllables (pop)
8. [ ] AI lyric anti-patterns clear (08 §6)

---

## SECTION 4. JAPANESE PROSODY GATES

### 4.1 Japanese = mora-timed

A *mora* is a phonological unit ≈ time slot. Each kana = 1 mora.

Crucial difference from English/Korean:
- "Tokyo" = 2 syllables, but **4 morae** (To-ki-yo-o)
- "Nippon" = 2 syllables, but **4 morae** (Ni-p-po-n)
- Final ん (n) = its own mora
- っ (small tsu, doubled consonant) = its own mora
- Long vowels = 2 morae

Implication: Japanese lyric line length should be counted in
*morae*, not syllables.

### 4.2 Japanese rhyme constraints

Only 5 vowels (a, i, u, e, o) → end rhyme severely constrained.
Most sentences end in predictable verb forms:
- ~る (ru)
- ~ます (masu)
- ~た (ta)
- ~だ (da) / ~です (desu)

End rhyme exists but is *weak* and *expected*. Japanese songwriters
compensate with:

#### A. Parallelism (対句)
Same structure, different meaning — Japanese tradition prizes this.

#### B. Moraic Assonance (Kawahara 2002, hip-hop)
Final 2 morae of phrase match in vowel sequence:
- "sa-tsu-ta-ba" and "so-ko-ji-ka-ra" → last 2 morae (ka-ra / ba)
- Common in J-rap

#### C. Internal repetition / alliteration
Strong device given end-rhyme weakness.

#### D. Kanji compression
Visual / semantic density per character — fits more meaning per
mora.

#### E. Pitch accent
Japanese has pitch accent. Mismatching can change meaning. In pop
singing, pitch accent often overridden — but listeners notice when
it's *very* off.

### 4.3 Japanese mora × BPM table

| BPM | Morae / line |
|---|---|
| 60-80 | 8-12 |
| 80-100 | 10-15 |
| 100-120 | 10-16 |
| 120-140 | 8-14 |
| 140-160 | 7-12 |
| 160+ | 6-10 |

Japanese fits *more morae per line* than Korean syllables — note
the difference.

### 4.4 Japanese pre-output gate

1. [ ] Mora count per line ∈ BPM range
2. [ ] Moraic assonance attempted in hip-hop / rap
3. [ ] Parallel structure used as primary device
4. [ ] Pitch accent not violently misaligned (key words)
5. [ ] Loanwords / kanji choice fits register
6. [ ] Suno gets Japanese text in *kana / kanji* (not romaji)
7. [ ] "Singing in Japanese" cue present in style box

### 4.5 The 6-step J-pop hook protocol (Case 27)

When working on J-pop:
1. **First-line lock** — establish persona / scene in line 1
2. **Three-clue rule** — 3 specific objects per verse
3. **One-fall rule** — exactly one emotional fall per song
4. **Hook restraint** — avoid 5+ repetitions of same hook word
5. **Mora discipline** — count morae, not syllables
6. **End rhyme freedom** — don't force when language resists

---

## SECTION 4bis. SPANISH PROSODY GATES

### 4bis.1 Spanish = syllable-timed (like Korean)

Each syllable roughly equal duration. Stress matters for meaning
(unlike Korean) but is more predictable than English (default
penultimate stress).

### 4bis.2 Spanish rhyme tradition

Spanish distinguishes:
- **Asonancia (assonance)**: vowel rhyme only — *standard* in
  Spanish poetry
- **Consonancia (consonance / perfect rhyme)**: vowel + consonant
  match — *stronger*

Both have *long literary tradition*. Spanish lyric tradition values
strict syllable count (octosyllabic, hendecasyllabic, etc.).

### 4bis.3 Stress placement

Spanish word stress:
- Penultimate (default): paLAbra, escribir, montaña
- Última (last) — marked with accent: papá, café, corazón
- Antepenúltima (third from last) — marked: música, lágrima

Match stressed syllables to musical stress positions.

### 4bis.4 Syllable count by tempo (Spanish)

Similar to English, slightly tighter due to syllable-timed nature:
- Slow: 7-9
- Mid: 7-10
- Fast: 5-8

### 4bis.5 Sinalefa (vowel elision)

When word ends in vowel and next begins with vowel, Spanish often
*elides* them into one syllable:
- "la amiga" → "lamiga" (2 syllables, not 3)
- Affects syllable count

Gate: count sinalefas correctly.

### 4bis.6 Spanish pre-output gate

1. [ ] Syllable count with sinalefas counted
2. [ ] Word stress on strong beats
3. [ ] Rhyme choice (asonancia or consonancia) appropriate
4. [ ] Persona-appropriate register (tú vs usted vs vos)

---

## SECTION 5. MULTILINGUAL FRAMEWORK

### 5.1 Cross-linguistic prosody comparison

| Language | Rhythm | Stress | Rhyme tradition | Primary device |
|---|---|---|---|---|
| English | Stress-timed | Lexical, meaning-changing | Strong end rhyme + internal | Prosody / Verb |
| Korean | Syllable-timed | Not meaning-changing | Moderate (assonance base) | Syllable count / 모음조화 / 대구 |
| Japanese | Mora-timed | Pitch accent | Weak end rhyme | Parallelism / Mora / Assonance |
| Spanish | Syllable-timed | Lexical, meaning-changing | Strong (asonancia base) | Strict syllable count |
| Chinese (Mandarin) | Syllable-timed | Tonal | Tonal rhyme tradition | Tone matching / Syllable |
| French | Syllable-timed | Phrase-final | Strong | Syllable count / Vowel sounds |

### 5.2 Universal prosody principles (Pattison)

Apply across all languages:
- Lyric phrase ends when melody phrase ends
- Stressed musical positions get *important* words (regardless of
  language-specific stress mechanics)
- Repetition + variation is fundamental
- Show > Tell in all languages

### 5.3 Per-language adaptations

#### English in Korean melody (Konglish hook)
- Match Korean syllable count of melody
- Use 1-2 syllable English words preferentially
- Avoid Latinate multisyllabic words
- See 08 §13 for full protocol

#### Korean in English melody (rare, K-Pop overseas release)
- Korean has higher syllable density → may need to *cut* lyric
  content
- Often use Korean ad-libs over English structure

#### Japanese in J-Pop with English hook
- Match Japanese mora count of melody — English hook needs more
  morae often
- "I love you" (3 morae in English, 4 morae in Japanese pronunciation
  "ai-ra-bu-yu")

### 5.4 Cultural register transfer

When translating concepts across languages:
- Korean 한 (han) → no English equivalent, *don't* try "deep sorrow"
- Japanese 物の哀れ (mono no aware) → not "transience," keep concept
- English "freedom" → multiple Korean translations depending on context

Translation always *loses* — operator decides what to lose.

### 5.5 Cross-linguistic Stable/Unstable Map (NEW v3.5)

Pattison's Stable/Unstable framework realized differently per
language:

| Domain | English Stable | English Unstable | Korean Stable | Korean Unstable | Japanese Stable | Japanese Unstable |
|---|---|---|---|---|---|---|
| Rhythm | Iambic regular | Mixed feet | 음절수 일정 | 음절수 변동 | 모라수 일정 | 모라수 변동 |
| Rhyme | Perfect end rhyme | Assonance / X | 완전운 | 모음운 / 무라임 | Parallel structure | Free verse |
| Syntax | Complete sentence | Fragments | 완결문 | 도치·생략 | 完結文 | 倒置・省略 |
| Line ending | Same word class | Varied | 같은 어미 | 변동 어미 | 同じ語尾 | 変動語尾 |
| Tense | Consistent | Shifts | 일관 | 변동 | 一貫 | 変動 |
| POV | Locked | Shifts | 일관 | 변동 | 一貫 | 変動 |

Master principle: *every language realizes the spectrum, but the
specific devices differ*. Apply the lens consciously per language.

---

## SECTION 6. SUNO ENGINE REALIZATION GATES

### 6.1 What Suno actually does with lyrics

Suno doesn't *understand* lyrics — it pattern-matches phonetics to
melody. Implications:
- Mispronunciation = pattern failure, not "wrong reading"
- Held notes = need long vowels
- Fast notes = need fewer consonants per syllable
- Section markers ([Verse], [Chorus]) shape arrangement
- Tags inside lyrics ([whispered], etc.) shape delivery

### 6.2 Suno singability gates

For *every* line:
1. **Read aloud at song tempo** — if you can't say it, Suno can't
   sing it
2. **Check vowel-consonant ratio** — vowels >40% for sustained
3. **Check cluster boundaries** — no 3+ consonants between syllables
4. **Check rhyme natural-vs-forced** — Suno emphasizes rhyme position
5. **Check capitalization** — ALL CAPS = louder delivery (Grenar
   Trick #8)
6. **Check punctuation** — . = hard stop, ... = drag, ! = emphasis

### 6.3 Section marker hygiene

10 SECTION 1 (Tag Taxonomy) covers full taxonomy. Prosody-relevant:
- [Verse] / [Chorus] / [Bridge] must be on their own line
- Modifiers stack: `[Chorus | anthemic | stacked harmonies]`
- Inline tags in lyrics shape delivery: `[whispered] I see you`
- Vocal anchor at *top* of lyrics: `[Vocal: female alto, intimate]`

### 6.4 Pronunciation override syntax (Grenar Trick #5)

When Suno mispronounces:
- Simple respell: "read" → "reed" (forces reed pronunciation)
- Syllable split: "extraordinary" → "ex-traor-din-ary"
- IPA last resort: `I'm out of /brɛθ/ again`

Keep operator-readable version saved separately; Suno gets the
phonetic version.

### 6.5 Suno phonetic gate (6 items)

1. [ ] Every line speakable at song tempo
2. [ ] Long vowels on long notes
3. [ ] No consonant cluster traps
4. [ ] Pronunciation overrides for traps (homographs, names,
       acronyms, numbers)
5. [ ] Section markers correct format (own line, brackets)
6. [ ] Vocal anchor present at lyrics top

---

## SECTION 7. THE 27-ITEM PROSODY GATE CHECKLIST (v3.6 — v2.11 expansion)

Run *every output* through this gate before submission. v2.11 expansion
adds **Gate F: Suno Natural-Singing Alignment (5 items)** from external
research (Suno v5/v5.5 syllable-stress-section landing studies).

### Gate A: Phonetic Alignment (6 items)
1. [ ] Syllable / mora count ∈ BPM range
2. [ ] 받침 ratio (Korean) or consonant cluster density tempo-fit
3. [ ] Long vowels on sustained notes
4. [ ] No 3+ consonant clusters at boundaries
5. [ ] Vowel harmony (Korean mimetic words)
6. [ ] Pronunciation overrides applied where Suno would fail

### Gate B: Prosodic Alignment (5 items)
7. [ ] Stressed syllables on stressed beats (English)
8. [ ] Word stress respected (Spanish, English)
9. [ ] Pitch accent not violently misaligned (Japanese key words)
10. [ ] Lyric phrase ends with melody phrase ends (all languages)
11. [ ] Stable/Unstable choices match section function

### Gate C: Semantic / Persona Alignment (5 items)
12. [ ] Persona consistent across sections
13. [ ] Tense consistent (or shift is intentional)
14. [ ] POV consistent (or shift is intentional)
15. [ ] One-metaphor rule (or deliberate switching)
16. [ ] Semantic field unified (5-6 fields, no random jumps)

### Gate D: Anti-Pattern Sweep (3 items)
17. [ ] No banned nouns (08 §6.2 / Field Guide)
18. [ ] No banned phrases / clichés (08 §6.3)
19. [ ] No banned rhyme pairs (08 §6.4)

### Gate E: Craft Quality (3 items, NEW v3.5)
20. [ ] Verb wattage audit — <30% weak verbs (0-10W)
21. [ ] AID applied to verses — Action / Imagery / Detail present
22. [ ] Show > Tell ratio — abstract emotion statements minimized

### Gate F: Suno Natural-Singing Alignment (5 items, NEW v3.6 / v2.11)

External research (HookGenius, Blake Crosley, Suno v5.5 docs):

23. [ ] **Line syllable count in Suno-safe zone** — 6-12 syllables
    English / **6-10 Korean** / 6-12 Japanese mora. 15+ = rushing/smear.
    Past 12 → break into two lines.
24. [ ] **Stress lands on kick** (trochaic kick alignment) — stressed
    syllable of each line lands on beat 1 or 3 (strong beats). Write
    *against* the stress and Suno fights you (rushing, smearing,
    syllable-shifting).
25. [ ] **Section first-line hook landing** — Suno gives the most
    melodic weight to the FIRST LINE of each tagged section. Choruses
    work best at 2-4 lines, with the hook line FIRST. Don't bury the
    hook on line 3.
26. [ ] **Korean spacing (한글 띄어쓰기)** — write Hangul with natural
    word-spacing. No run-on phrases. No romanization (Suno processes
    Hangul better than romaja). Each 어절 = natural breath unit for
    Suno's phrasing engine.
27. [ ] **Concept ↔ Lyric ↔ Vocal Anchor consistency** — chorus mood
    matches Vocal Anchor instructions; verse imagery matches Persona
    Brief Lock; bridge tonal shift matches structural intent. No
    "happy lyric in dark-vocal anchor" type mismatches.

### Gate output (v3.6 v2.11)

- **All 27 pass**: ship lyric → output `✅ Gate 27/27`
- **1-3 fail**: surface in operator review, recommend fix → output
  `❌ Gate X/27 — [items] auto-reinforced`
- **4+ fail**: do not ship — return to lyric craft files (07 / 08)

### Cross-reference to 00 SYSTEM

- C-13 / C-26.6 reference this gate for 1-line ✅/❌ output marking
- C-45 Position Weighting: items 25 (first-line hook) ties to Style
  Box position-1 50% weighting principle
- C-3.3 Vocal Rushing Diagnostic: items 23-24 trigger when operator
  reports "rushed" or "smeared" vocals

---

## SECTION 8. KOREAN-ENGLISH HYBRID HANDLING

### 8.1 Konglish vs translation

- **Konglish**: English words integrated into Korean rhythm /
  melody as natural syllable units. Common in K-Pop hooks.
- **Translation**: English content rendered in Korean (different
  rhythm needs).

These are *different* operations.

### 8.2 Konglish density per genre

| Genre | Konglish density |
|---|---|
| K-Pop main | High (hook in English, verse mixed) |
| K-Indie | Low (Korean dominant) |
| K-R&B | Moderate (ad-libs, hooks) |
| K-Hip-Hop | High (English vocab, code-switching) |
| K-Ballad | Low (Korean dominant) |
| OST | Low (Korean dominant) |
| Trot | Very low (Korean dominant) |

### 8.3 Konglish phonetic safety

- 1-2 syllable English words: safe (baby, love, free, mine)
- 3 syllable English: handle with care (forever, beautiful)
- 4+ syllable English: usually fails Konglish fluidity

### 8.4 Konglish rhythm matching

Korean syllables = roughly 1 mora-equivalent each. English borrowed
into Korean melody must match:
- "I love you" (3 English syllables) ≈ 3 Korean syllables
- Place on melody slots where 3 Korean syllables would fit

### 8.5 Konglish Prosody Negotiation (NEW v3.5)

When English hook + Korean verse syllable density collide:

**Problem**: Producer hands you melody with hook slot = 11 syllables.
English hook needs 11 English syllables. Korean verses need 11
Korean syllables. *Korean syllables carry more meaning*, so:

- Korean verse at 11 syllables = full sentence with subject + verb +
  modifier
- English hook at 11 syllables = filler-padded line ("baby tell me
  what you wanna do tonight" = 11 syllables)

Negotiation options:
1. **Shorter English hook + extended note** (3 syllables + sustained):
   "Tell me how" (3 sylls), hold "how" for remaining duration
2. **Repeat short English hook** ("baby baby, tell me what to do" —
   8 syllables, 1 word doubled)
3. **English hook in 2 phrases** ("I see you / I know you" — 6
   syllables total in melody slot of 11, with rests)
4. **Pure Korean melody** — drop English, use Korean verse rhythm in
   chorus too (less K-Pop-typical but viable)

Default: option 2 (repeated short hook) — K-Pop industry standard.

---

## SECTION 9. LYRIC SPECIFICITY VALIDATION

### 9.1 The specificity test

For *every line*, ask:
- Could this line appear in *any* song? → too generic
- Is there a *specific image / detail / verb*?
- If a listener heard only this line, would they remember it?

### 9.2 Specificity audit pass

After draft:
1. Highlight every line that contains a *concrete noun, specific
   verb, or sensory detail*
2. Lines without any specificity = candidates for revision
3. Goal: ≥70% of verse lines have specificity
4. Chorus may be more general, but central image still needed

### 9.3 Show vs Tell ratio

Count:
- Tell lines (state emotion / abstract concept directly)
- Show lines (image / action / sense / specific detail)

Target ratios:
- Verse: 80%+ Show
- Pre-Chorus: 60%+ Show
- Chorus: 40%+ Show (chorus may state)
- Bridge: 70%+ Show (bridge re-engages)

### 9.4 Verb wattage check (NEW v3.5)

Per 08 §5:
- Circle all verbs
- Rank by wattage (0-1000W)
- Calculate weak (0-10W) ratio
- Target: <30% weak verbs

If >30%: revise.

---

## SECTION 10. EXAMPLE — GATE IN ACTION

### Lyric (Korean, K-Pop, 128 BPM)

```
[Verse 1]
6시 옥상 위에 콘크리트가 녹아
에어컨이 죽었다, 너에게 보낸 톡
답장은 오지 않고 햇빛이 차오르네
공룡들도 이런 날에 안녕했을까

[Chorus]
태양아 안녕 잘 가렴
공룡도 빠이 했을걸
태양아 안녕 잘 가렴
이젠 우주야 너의 곁
```

### Gate run

**A. Phonetic (Korean):**
1. ✓ Syllable count: Verse 9-10, Chorus 7 — fits 128 BPM (6-10)
2. ✓ 받침 ratio ~ 40% — under 50% limit
3. ✓ Long vowels (옥, 콘, 안, 우) on sustained notes
4. ✓ No 3+ consonant clusters
5. N/A (no mimetic words)
6. ✓ No pronunciation traps

**B. Prosodic:**
7. N/A (Korean)
8. N/A
9. N/A
10. ✓ Phrases match 4-bar units
11. ✓ Verse = mid-stable / Chorus = strong-stable (assonance →
    family)

**C. Semantic:**
12. ✓ Persona = "shy romantic with cosmic humor" — consistent
13. ✓ Tense — present throughout
14. ✓ POV — first person
15. ✓ One metaphor = "summer rooftop + cosmic farewell"
16. ✓ Semantic fields: heat / rooftop / phone / sun / cosmos
    (5 fields, connected)

**D. Anti-Pattern:**
17. ✓ No banned nouns (no crown, throne, shadows, etc.)
18. ✓ No banned phrases
19. ✓ No banned rhyme pairs (~네 / ~걸, ~렴 / ~걸)

**E. Craft (NEW v3.5):**
20. ✓ Verbs: 녹다(200W), 죽다(200W), 차오르다(500W), 빠이하다
    (100W) — strong
21. ✓ AID present:
    - Action: 보내다, 차오르다, 빠이하다
    - Imagery: 콘크리트 녹아, 햇빛 차오르네
    - Detail: 6시, 옥상, 에어컨, 톡
22. ✓ Show > Tell — no abstract emotion direct statements

**Result: 22/22 pass — ship.**

---

## SECTION 11. RELATED FILES

- **07_LYRIC_CRAFT_KOREAN.md** — Korean lyric generation (upstream)
- **08_LYRIC_CRAFT_ENGLISH.md** — English lyric generation (upstream)
- **17_THEMATIC_CULTURAL_ENGINE.md** — Scene Dossier / Object
  Writing → raw material
- **10_SUNO_LYRICS_TAGS.md** — Suno tag syntax / Grenar tricks
- **04_RHYTHM_AND_FORM.md** — Song structure / BPM
- **99_OPERATOR_VAULT Part F (검증 키워드)** — Cliché dictionaries / persona vocabulary
- **99_OPERATOR_VAULT Part F (BPM × 음절 매트릭스)** — BPM × syllable canonical table

---

## USER EXTENSION ZONE

Operator-found prosody patterns, language-specific phonetic surprises,
and recurring failure modes documented here.

(Empty — populated by 99z_SESSION_LOG session-end logging.)


## § USER EXTENSION ZONE v2.0 (2026-05-24)

bitwize pronunciation-guide 19KB 풀바디 + SJY prosody-and-language
통합. **Pronunciation Notes Table 의무 활용 원칙.**


### §UE-1. Why This Matters (외부 검증)

*"Suno reads lyrics literally."* Context 무시. Homograph 함정.
V5에서 context 개선 but *never trust context for homographs*.


### §UE-2. High-Risk Homographs (bitwize 풀바디)

```
| Word | Pron A | Pron B | Example |
|------|--------|--------|---------|
| live | /lɪv/ LIV (performance) | /laɪv/ LYVE (alive) | "I LYVE here" |
| read | /riːd/ REED (present) | /rɛd/ RED (past) | "I RED it yesterday" |
| lead | /liːd/ LEED (guide) | /lɛd/ LED (metal) | "LED pipes" |
| wind | /wɪnd/ WIND (breeze) | /waɪnd/ WYND (coil) | "WYND the clock" |
| close | /kloʊs/ KLOHS (near) | /kloʊz/ KLOHZ (shut) | "KLOHZ the door" |
| tear | /tɪr/ TEER (crying) | /tɛr/ TAIR (rip) | "TAIR the page" |
| bow | /boʊ/ BOH (ribbon) | /baʊ/ BOW (bend) | "Take a BOW" |
| bass | /beɪs/ BAYSS (instrument) | /bæs/ BASS (fish) | Usually BAYSS |
| wound | /wuːnd/ WOOND (injury) | /waʊnd/ WOWND (coiled) | "WOWND around" |
| minute | /ˈmɪnɪt/ MIN-it (60s) | /maɪˈnjuːt/ my-NOOT (tiny) | "my-NOOT details" |
| resume | /rɪˈzuːm/ ri-ZOOM (continue) | /ˈrɛzjʊmeɪ/ REZ-oo-may (CV) | Usually ri-ZOOM |
| object | /ˈɒbdʒɪkt/ OB-jekt (thing) | /əbˈdʒɛkt/ ob-JEKT (protest) | "I ob-JEKT" |
| project | PROJ-ekt (plan) | pro-JEKT (throw voice) | "pro-JEKT your voice" |
| record | REK-ord (noun) | ri-KORD (verb) | "ri-KORD a song" |
| present | PREZ-ent (gift) | pri-ZENT (give) | "pri-ZENT the award" |
| content | KON-tent (stuff) | kon-TENT (satisfied) | "I'm kon-TENT" |
| desert | DEZ-ert (sand) | di-ZURT (abandon) | "di-ZURT the cause" |
| refuse | REF-yoos (garbage) | ri-FYOOZ (decline) | "I ri-FYOOZ" |
| row | ROH (line) | ROW (argument) | Usually ROH |
| sow | SOH (plant seeds) | SOW (female pig) | "SOH the seeds" |
```


### §UE-3. "live" 풀바디 처방

#### LYVE (rhymes with "five") — alive

```
| Intended | Risk | Fix |
|---|---|---|
| "live your life" | May say LIV | "lyve your life" or "living your life" |
| "live and breathe" | May say LIV | "lyve and breathe" or "alive and breathing" |
| "I live here" | May say LIV | "I lyve here" or "I'm living here" |
| "LiveJournal" | LIV-journal | "Life-journal" or "Lyve-journal" |
| "live wire" | LIV wire | "lyve wire" |
| "alive" | Usually OK | No fix |
```

#### LIV (rhymes with "give") — performance

```
| Intended | Risk | Fix |
|---|---|---|
| "live performance" | May say LYVE | "liv performance" or "performing live" |
| "live show" | May say LYVE | "liv show" or "concert" |
| "going live" | May say LYVE | "going liv" or "on air now" |
| "live stream" | May say LYVE | "liv stream" or "streaming now" |
```

**Decision Guide:** Rhymes with "five" or "give"?


### §UE-4. Tech Terms & Acronyms

```
| Term | Write As | Notes |
|---|---|---|
| GNU | guh-new | Hard G |
| Debian | Deb-Ian | Hyphen for 3 syllables |
| Linux | LIN-ucks | Not LINE-ucks |
| daemon | DEE-mon | Not DAY-mon |
| cache | "cash" | Not catch / cash-ay |
| router | ROW-ter (US) | Or ROOT-er (UK) |
| sudo | SOO-doo or SOO-doh | Not pseudo |
| regex | REJ-eks | Not REE-jeks |
| tuple | TUP-el or TOO-pel | Both |
| SQL | "sequel" or S-Q-L | sequel more common |
| GUI | "gooey" | Not G-U-I |
| API | A-P-I | Spell out |
| URL | U-R-L or "earl" | Spell out preferred |
| GIF | "jif" or "gif" | Contested, avoid |
| IEEE | "eye-triple-E" | Not I-E-E-E |
| BIOS | BY-ose | Not B-I-O-S |
| ASCII | ASK-ee | Not A-S-C-I-I |
| SCSI | "scuzzy" | Not S-C-S-I |
| WYSIWYG | WIZ-ee-wig | The what-you-see acronym |
| JPEG | JAY-peg | Not J-P-E-G |
| MIDI | MID-ee | Not M-I-D-I |
| WiFi | WY-fy | Not wiff-ee |
| SaaS | "sass" | Not S-A-A-S |
| LED | L-E-D | Spell out |
| RAM | "ram" | Like the animal |
| DOS | "doss" | Not D-O-S |
| LAN | "lan" | Rhymes with pan |
```

**Letter-by-letter (use periods):**
S.L.S. / L.K.M.L. / B.D.F.L. / D.F.S.G. / A.P.I.


### §UE-5. Numbers (외부 검증)

```
Spell out:
- "twenty-one" not "21"
- "nineteen eighty-four" not "1984"
- "three hundred" not "300"

Exception:
- '93 (year abbreviation) OK
```


### §UE-6. Multilingual (C-67)

```
원칙 (외부 검증):
"Use one language per section — mixing languages causes pronunciation drift"

룰:
1. 섹션별 언어 격리
2. 비영어 섹션에 "all lyrics in [language], no English" Style
3. Style: "bilingual, [lang1] verse, [lang2] chorus"

K-pop 어법:
- Hangul 직접 V5 작동
- 또는 hyphenated romanization: "Sa-rang-hae"
- [Clear Vocals] / [High Fidelity Vocals] when mixing
```


### §UE-7. German Pronunciation (bitwize)

```
Short vs Long Vowels:
- 단일 모음 → short English 해석
- Long forced → double vowel (juchhe → juchee)

Umlauts:
- ä → "ae"
- ö → "oe"
- ü → "ue"
- ß → "ss" (usually OK)
```


### §UE-8. Fix Priority (외부 검증)

```
1. Rewrite (preferred) — 다른 단어로
2. Phonetic Spelling — 음운 표기
3. Hyphenation — 음절 분리
4. Context Padding — 명확화
5. Accept — 문서화 후 진행
```


### §UE-9. Pronunciation Notes Table 의무 사용

```
Track 작업 시 의무 표:

| Word | Standard | Phonetic | Applied? |
|------|----------|----------|----------|
| Ramos | Ramos | Rah-mohs | ✓ All 4 occurrences |
| live | live | lyve | ✓ V1, V2, Chorus |
| FBI | FBI | F-B-I | ✓ Bridge |

원칙:
- 표 = source of truth
- Suno 가사 = phonetic 사용
- 스트리밍 가사 = 표준 영어
- 새 단어 추가 → 즉시 가사 적용
- 최종 단계 검증 (모든 occurrences)
```


### §UE-10. Accent Simulation (bitwize)

```
Technique:
1. 가사 phonetically rewrite (target accent)
2. Style box: "[X] accent"
3. ChatGPT 활용 가능

예:
Standard: "I'm going to the store"
Russian: "Ahm go-ink to da store"
Jamaican: "Mi ah go ah di store"
Southern US: "Ahm goin' to tha store"
```


# === END 14 USER EXTENSION ZONE v2.0 ===


# ============================================================
# § USER EXTENSION v2.0 FINAL Polish (2026-05-26)
# 운율 / 발음 풀바디 보강 — 받침 학술 + IPA 변환
# ============================================================


## §UE-40. 받침 (Batchim) 발음 정밀 (90daykorean 학술)

### §UE-40.1 받침 7-sound 분류

```
| Batchim | Sound | Sustain | Suno 자리 |
|---|---|---|---|
| ㄱ, ㅋ, ㄲ | k (unreleased) | X (stop) | Hook 자리 X |
| ㄴ | n | OK | 어디든 OK |
| ㄷ, ㅅ, ㅆ, ㅈ, ㅊ, ㅌ | t (unreleased) | X (stop) | Hook 자리 X |
| ㄹ | l (liquid) | BEST | Sustain 자리 |
| ㅁ | m | OK | 어디든 OK |
| ㅂ, ㅍ | p (unreleased) | X (stop) | Hook 자리 X |
| ㅇ | ng | OK | Sustain 자리 |

원칙:
- Hook / Final Chorus 자리 → ㄹ / ㅁ / ㄴ / ㅇ 받침 권장
- Verse 자리 → 다양 OK
- 빠른 BPM → 받침 ㄱ/ㄷ/ㅂ 회피
```

### §UE-40.2 Double Batchim (이중 받침)

```
11개 이중 받침 → 단일 sound로 압축:

ㄳ → [k]
ㄵ → [n]
ㄶ → [n]
ㄺ → [k] (예: 닭 [닥])
ㄻ → [m] (예: 삶 [삼])
ㄼ → [l]
ㄽ → [l]
ㄾ → [l]
ㄿ → [p]
ㅀ → [l]
ㅄ → [p]

Suno 함정:
- 이중 받침 단어 → 발음 무너지기 쉬움
- 처방: IPA-like 표기 + 다음 음절 ㅇ 만나는 자리 활용
```

### §UE-40.3 받침 연음 처방 (Liaison)

```
받침 + 다음 음절 ㅇ → 받침이 다음 음절로:

예시:
- "꽃이" [꼬치] — ㅊ 연음
- "옷을" [오슬] — ㅅ 연음
- "낮은" [나즌] — ㅈ 연음

Suno 처방 어법:
- 가사 한 줄에 연음 자리 3+개 → 발음 무너짐 위험
- 처방 metatag: [Vocal: clear diction, careful liaison]
- 또는 IPA-like 표기: "꽃이" → "ggo-chi"
```


## §UE-41. 자음 변동 풀바디 (Suno 함정)

### §UE-41.1 비음화 (Nasalization)

```
받침 ㄱ/ㄷ/ㅂ + ㄴ/ㅁ → 비음화:

ㄱ + ㄴ/ㅁ → [ㅇ]:
- "한국말" [한궁말]
- "국물" [궁물]
- "막내" [망내]

ㄷ + ㄴ/ㅁ → [ㄴ]:
- "닫는" [단는]
- "받는" [반는]

ㅂ + ㄴ/ㅁ → [ㅁ]:
- "감사합니다" [감사함니다]
- "밥먹다" [밤먹다]
- "잡는" [잠는]

Suno 처방:
- 자주 발생 자리 → IPA-like 표기 권장
- 또는 변동 적은 단어로 치환
```

### §UE-41.2 유음화 (Lateralization)

```
ㄴ + ㄹ → [ㄹㄹ]:
- "신라" [실라]
- "권력" [궐력]
- "관리" [괄리]
- "본래" [볼래]

ㄹ + ㄴ → [ㄹㄹ]:
- "물난리" [물랄리]
- "달나라" [달라라]

Suno 처방:
- 유음화는 자연스러움 — 활용 권장
- ㄹ 받침 + ㄴ 어울림 (sustain 자리)
```

### §UE-41.3 격음화 (Aspiration)

```
받침 ㄱ/ㄷ/ㅂ/ㅈ + ㅎ → 거센소리:

- "좋다" [조타]
- "많다" [만타]
- "닿는" [단는] (격음 → 비음화)
- "괜찮다" [괜찬타]

Suno 처방:
- 격음화 자리 발음 명확
- 노래에서 무리 없음
```

### §UE-41.4 경음화 (Tensification)

```
받침 + 평음 → 된소리:

- "학교" [학꾜]
- "독서" [독써]
- "악기" [악끼]
- "법정" [법쩡]

Suno 처방:
- 경음화 자리 자연스러움
- 노래 박을 때 발음 명확
```

### §UE-41.5 구개음화 (Palatalization)

```
받침 ㄷ/ㅌ + 이 → ㅈ/ㅊ:

- "같이" [가치]
- "굳이" [구지]
- "곧이" [고지]
- "맡이다" → "맡혀" [마쳐]

Suno 처방:
- 구개음화 자리 발음 자연스러움
- 단, "같이" → 가사로 박을 때 [가치]로 들림 — 의도된 자리만
```


## §UE-42. IPA-like 표기 어법 (Suno 발음 락)

### §UE-42.1 어법

```
Suno에서 발음 락 필요 시 IPA-like 표기:

[Vocal: pronounce "사랑해요" as "sa-rang-hae-yo"]
[Vocal: pronounce "꽃이" as "kkot-chi"]

원칙 (외부 정설):
- "Suno V5 handles Korean Hangul better than V4"
- "단, romanized Korean with hyphens remains more reliable
   for pronunciation control"
- "Format: Sa-rang-hae not Saranghae"

활용 자리:
- 발음 무너지기 쉬운 단어
- 이중 받침 단어
- 자음 변동 자리
- 한국 음악 용어 (kkeokgi / ppongki / nori 등)
```

### §UE-42.2 영어 단어 IPA-like 표기

```
영어 단어 발음 함정 자리:

자음 cluster:
- "strength" → [streng-th]
- "spring" → [s-pring]

장단모음:
- "ship" → [ship] (short)
- "sheep" → [shi-ip] (long)

Suno 처방:
- 한국어 화자 발음 함정 자리 → IPA-like 표기 권장
- 영어 hook 자리 [Vocal: native-like English pronunciation]
```


## §UE-43. BPM × 음절 매트릭스 (한국어 정밀)

### §UE-43.1 한국어 음절 매트릭스 풀바디

```
| BPM 구간 | 한국어 음절/바 | 영어 음절/바 | 받침 권장 |
|---|---|---|---|
| 60-70 (slow ballad) | 3-5 | 5-7 | 다양 OK |
| 70-90 (ballad/R&B) | 4-6 | 6-8 | 다양 OK |
| 90-110 (mid-tempo) | 6-8 | 8-10 | ㄹ/ㅁ/ㄴ/ㅇ 위주 |
| 110-130 (pop/dance) | 7-9 | 10-12 | ㄹ/ㅁ/ㄴ/ㅇ 위주 |
| 130-150 (EDM/dance) | 6-8 | 9-11 | 받침 최소 |
| 150-170 (hardstyle) | 5-7 | 8-10 | 받침 최소 |
| 170+ (psytrance) | 4-6 | 7-9 | 개음절 위주 |

원칙:
- 빠른 BPM → 받침 회피 (특히 stop 받침 ㄱ/ㄷ/ㅂ)
- 느린 BPM → 받침 다양 OK (감정 디테일)
- 32분음표 자리 → 음절 1개 (러싱 차단)
```

### §UE-43.2 보컬 러싱 진단 자동

```
시스템 자동 (가사 출력 직전):
1. BPM 추정
2. 음절/바 계산
3. 매트릭스 매칭
4. 미스매치 발견 시:
   - [Pause half bar] 자동 인서트 권유
   - 또는 받침 변경 권유 (stop → liquid)
   - 또는 음절 수 조정 권유

표기:
"🔍 보컬 러싱 진단:
 - BPM 138 / 음절/바 평균 9.2 (매트릭스 권장 7-9 — 미스매치)
 - Verse 2 라인 3 음절 압축 권유
 - 또는 [Pause half bar] 라인 사이 인서트"
```


# === END 14 USER EXTENSION v2.0 FINAL Polish ===
