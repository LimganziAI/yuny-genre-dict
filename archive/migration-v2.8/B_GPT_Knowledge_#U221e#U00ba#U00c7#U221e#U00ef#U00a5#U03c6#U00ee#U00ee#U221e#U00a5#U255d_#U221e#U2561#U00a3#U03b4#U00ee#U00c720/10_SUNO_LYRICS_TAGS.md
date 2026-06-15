10. SUNO LYRICS TAGS — Complete Bracket Tag Library
Version: 1.0 Last Updated: 2026-04-30 Engine Target: Suno v5 / v5.5 Load Trigger: Whenever lyrics are being formatted for Suno Custom Mode, or when diagnosing structure/vocal direction issues. Companion Files: 09_SUNO_ENGINE.md, 12_PROMPT_TEMPLATES.md, 06_VOCAL_PRODUCTION.md

SECTION 0. PURPOSE & USAGE RULES
This file is the verified bracket-tag reference for the Suno Lyrics field. Every tag listed here has been community-tested or appears in Suno-curated documentation.

0.1 Where Tags Belong
Style of Music box (Style Box): NO bracket tags. Tags here are illegal and cause parsing failures. Use commas, plain language only. (See 09_SUNO_ENGINE.md § 1.4.)
Lyrics field: Bracket tags belong here exclusively.
0.2 Bracket Forms
Suno accepts two bracket forms inside the Lyrics field:

Square brackets [ ] — for structural and direction commands. The engine reads these as instructions and does not vocalize them.
Parentheses ( ) — for performance hints inside lyric flow (whispered asides, ad-libs to be sung, harmony notes). Parentheses can sometimes be vocalized softly; use when you want a sung/spoken interjection.
Rule of thumb: structural and engineering instructions go in [ ]. Sung interjections and asides go in ( ).

0.3 Tag Reliability Tiers
Tags are tiered by how reliably Suno v5/v5.5 obeys them:

Tier S (always works): Section structure tags. Highly reliable.
Tier A (usually works): Vocal direction tags, ad-lib tags, common instrument cues.
Tier B (often works, context-dependent): Mood tags, atmosphere tags, mix tags.
Tier C (unreliable, use with backup): Specific technical tags (BPM changes mid-song, exact instrumentation swaps).
Tier F (avoid): Tags that cause parser confusion or are silently ignored.
Each tag in this file is marked with its tier.

0.4 Tag Density Rule
Do not over-tag. One vocal direction tag per section is the optimum. Over-tagging dilutes the signal and Suno starts ignoring tags. Aim for: one section tag, optionally one delivery cue, plus inline ad-libs/harmony where they occur — nothing more.

0.5 Bar-Count Tagging
For consistent section length, append the bar count after the section name:

[Verse 1 8] — Verse 1, 8 bars long
[Chorus 8] — Chorus, 8 bars
[Bridge 4] — Bridge, 4 bars
This is highly recommended. Without it, Suno improvises section length and frequently produces unbalanced takes.

SECTION 1. STRUCTURAL TAGS (TIER S)
These are the backbone of any Suno lyric. Always present, always obeyed.

1.1 Core Section Tags
Tag	Function	Typical Bar Count
[Intro]	Opening section, often instrumental	4-8
[Verse] or [Verse 1], [Verse 2]	Narrative section	8 (pop), 16 (hip-hop)
[Pre-Chorus]	Tension lift before chorus	4-8
[Chorus]	Main hook section	8
[Post-Chorus]	Tail after chorus, often hooky vamp	4-8
[Bridge]	Contrast section	4-8
[Outro]	Closing section	4-8
[Ending]	Hard stop, final tag	1-4
1.2 Genre-Specific Section Tags
Tag	Genre	Function
[Drop]	EDM, trap, dubstep	The energy peak — usually instrumental release
[Build-Up]	EDM, dance	Risers leading into Drop
[Breakdown]	EDM, dance, prog	Sparse section before re-entry
[Dance Break]	K-pop, dance-pop	Instrumental break for choreography
[Hook]	Hip-hop, R&B	Equivalent to chorus in rap context
[Refrain]	Folk, traditional	Recurring lyric line outside chorus
[Vamp]	Gospel, soul, jazz	Repeated chord cycle for ad-libs
[Tag]	Gospel, soul	Final repeated phrase for emphasis
[Riff Section]	Rock, metal	Instrumental riff feature
[Solo]	Any	Instrumental solo (specify instrument: [Guitar Solo])
[Instrumental Break]	Any	Generic instrumental section
[Interlude]	Any	Transitional section, often atmospheric
1.3 Section Modifiers (Append to Section Tag)
Modifier	Effect
[Verse 1 8]	8 bars
[Chorus, big]	Indicates fuller production
[Chorus, stripped]	Indicates sparser production
[Final Chorus]	Last chorus — often modulated or extended
[Half-time Chorus]	Tempo feel halves
[Double-time Bridge]	Tempo feel doubles
[Acapella]	Vocals only, no instruments
[A capella Intro]	Vocal-only opening
SECTION 2. VOCAL DIRECTION TAGS (TIER A)
Place immediately under the section tag, before the first lyric line. One per section is optimal.

2.1 Delivery Style
Tag	Effect
[Singing: breathy, intimate]	Soft, close-mic feel
[Singing: belted]	Powerful, projected
[Singing: whispered]	Very soft, ASMR-style
[Singing: half-sung]	Between speech and song
[Singing: melismatic]	Heavy ornamentation
[Singing: deadpan]	Flat, emotionless
[Singing: passionate]	High emotional intensity
[Singing: conversational]	Natural speech-like delivery
[Spoken]	Spoken word, no melody
[Spoken, soft]	Quiet spoken delivery
[Rapped]	Rap delivery
[Sung-rap]	Melodic rap, hip-hop hybrid
[Falsetto]	Head voice, light register
[Mixed Voice]	Blend of chest and head
[Chest Voice]	Full lower register
[Whisper to Belt]	Dynamic build within the section
2.2 Emotion / Attitude Tags
Use sparingly — Tier B reliability for these alone, but they reinforce delivery tags.

Tag	Effect
[Yearning]	Longing, melancholic
[Defiant]	Confrontational
[Triumphant]	Victorious, anthemic
[Vulnerable]	Exposed, raw
[Playful]	Light, teasing
[Menacing]	Dark, threatening
[Nostalgic]	Wistful, looking back
[Confident]	Assertive
[Resigned]	Accepting, weary
[Joyful]	Upbeat, celebratory
2.3 Vocal Identity (when not using Persona)
Tag	Effect
[Female lead]	Locks female voice for that section
[Male lead]	Locks male voice
[Duet]	Alternating male and female
[Group vocals]	Multiple voices in unison
[Children's choir]	Young voice texture
[Choir]	Full choir backing
[Gospel choir]	Gospel-style backing vocals
2.4 Layering Tags
Tag	Effect
[Doubled]	Lead vocal doubled
[Triple-tracked]	Lead vocal tripled
[Harmony +3rd]	Add a third above
[Harmony +5th]	Add a fifth above
[Harmony, octave up]	Octave doubling above
[Harmony, octave down]	Octave doubling below
[Stacked vocals]	Multiple harmony layers
[Choir backing]	Choir behind lead
[Counter-melody]	Secondary vocal line in counterpoint
[Call and response]	Lead-then-backing alternation
[Round / canon]	Layered staggered entries
SECTION 3. AD-LIB & INTERJECTION TAGS (TIER A)
Ad-libs are sung interjections layered around or between main lines. Place them inline within the lyric block where they should occur, or as a section-wide directive.

3.1 Ad-Lib Section Tag
Tag	Effect
[Ad-libs]	Engine adds spontaneous interjections throughout the section
[Ad-lib: yeah, mmm, oh]	Specific ad-libs requested
[Background ad-libs]	Ad-libs in background only
[Trap ad-libs]	Hip-hop style "yuh, skrrt, ay" interjections
[Gospel ad-libs]	"Lord, oh, yes" gospel style
[R&B ad-libs]	"Mmm, yeah, oh baby" smooth style
3.2 Inline Sung Interjections (use parentheses)
Place these directly inside the lyric line where they should be sung:

I'm running through the night (yeah)
Calling out your name (oh, baby)
Common inline interjections:

Interjection	Style
(yeah)	Universal
(oh)	Universal
(woo)	R&B, soul, pop
(uh)	Hip-hop, trap
(mmm)	R&B, neo-soul
(ay)	Hip-hop, Latin
(let's go)	Hip-hop, EDM
(come on)	Soul, rock
(baby)	R&B, pop
(no, no)	Pop, R&B
(la la la)	Pop, indie
(ooh ooh)	Universal
(skrrt)	Trap
(ha)	Pop, dance
3.3 Echo and Repeat Tags
Tag	Effect
[Echo]	Last phrase repeats with delay
[Echo: <phrase>]	Specific phrase echoes
[Repeat: <phrase>]	Phrase repeats deliberately
[Repeat 2x]	Whole section repeats twice
[Stutter]	Word stuttered for effect
SECTION 4. INSTRUMENT & ARRANGEMENT TAGS (TIER A-B)
Use to indicate instrumental moments inside a lyric block.

4.1 Solo Tags
Tag	Effect
[Guitar Solo]	Electric guitar solo
[Acoustic Guitar Solo]	Acoustic feature
[Piano Solo]	Piano feature
[Saxophone Solo]	Sax feature
[Trumpet Solo]	Trumpet feature
[Violin Solo]	Violin feature
[Synth Solo]	Synth lead feature
[Bass Solo]	Bass feature
[Drum Solo]	Drum feature
[Vocal Solo]	A cappella vocal moment
4.2 Instrument Cues (mid-section)
Tag	Effect
[Strings enter]	Strings join the arrangement
[Horns enter]	Brass section joins
[Drums drop]	Drums begin
[Drums cut]	Drums stop
[Bass drops]	Bass enters powerfully
[Synth pad rises]	Pad swells in
[Beat switch]	Rhythmic change
[Tempo lift]	Tempo increases
[Half-time]	Drums shift to half-time feel
[Double-time]	Drums shift to double-time feel
4.3 Texture Tags
Tag	Effect
[Stripped back]	Sparse arrangement
[Full band]	All instruments active
[Acoustic]	Acoustic-only arrangement
[Electronic]	Electronic-only arrangement
[Orchestral]	Full orchestra
[Lo-fi]	Lo-fi production character
[Vintage]	Vintage production character
[Cinematic]	Film-score character
SECTION 5. SOUND EFFECT & ATMOSPHERE TAGS (TIER B)
Use sparingly. These are atmospheric cues, not guaranteed to render exactly but often shape mood successfully.

5.1 Environmental SFX
Tag	Effect
[Rain]	Rain ambience
[Thunder]	Thunder hit
[Wind]	Wind atmosphere
[Ocean waves]	Ocean ambience
[Crowd noise]	Crowd/stadium sound
[Applause]	Applause
[Crowd cheering]	Cheering crowd
[Footsteps]	Footstep sounds
[Heartbeat]	Heartbeat pulse
[Phone ringing]	Phone ring
[Static]	Radio/TV static
[Vinyl crackle]	Vinyl record texture
5.2 Production FX
Tag	Effect
[Riser]	Pitch-rising sweep
[Sweep]	White-noise sweep
[Impact]	Cinematic boom
[Reverse cymbal]	Reverse cymbal swell
[Tape stop]	Tape-stop effect
[Vinyl scratch]	DJ scratch sound
[Glitch]	Glitch effect
[Drop out]	Sudden silence
[Cut]	Hard cut
[Fade out]	Gradual fade
[Fade in]	Gradual entry
SECTION 6. PRONUNCIATION & EMPHASIS TAGS (TIER A)
6.1 Pronunciation Override
When Suno mispronounces a word, force phonetics with bracket annotation immediately after the word:

Tomorrow [tuh-MAH-roh]
Coffee [KAW-fee]
Either [EE-thur]
Use uppercase for stressed syllables, hyphens between syllables. Useful for:

Foreign words
Names
Regional pronunciations
Words Suno consistently mispronounces
6.2 Emphasis
Form	Effect
*word*	Emphasis on that word
WORD (all caps)	Stronger emphasis, almost shouted
**word**	Strongest emphasis
Use very sparingly — overuse desensitizes the engine to emphasis.

6.3 Held / Sustained Notes
Tag	Effect
[Sustain]	Hold the next note long
[Held note]	Same — hold the note
wooooooo (vowel extension)	Hold the vowel sound
[Long note]	Sustained final note of phrase
SECTION 7. LANGUAGE & ACCENT TAGS (TIER A-B)
7.1 Language Lock
Tag	Effect
[Korean lyrics]	Force Korean pronunciation
[English lyrics]	Force English pronunciation
[Japanese lyrics]	Force Japanese pronunciation
[Spanish lyrics]	Force Spanish
[Bilingual]	Mix of two languages
7.2 Code-Switching Cues
For multilingual sections, mark transitions:

[Korean lyrics]
밤이 깊어지면 너는 어디에
(English) wherever you go, I'll find you
7.3 Accent Tags
Tag	Effect
[Southern US accent]	Country-style accent
[British accent]	UK accent
[Jamaican accent]	Reggae/dancehall
[Korean accent]	K-pop English pronunciation style
[French accent]	French-tinted English
SECTION 8. MIX & PRODUCTION TAGS INSIDE LYRICS (TIER B)
These tags affect how the section is mixed/processed. Less reliable than vocal direction tags but useful as reinforcement.

Tag	Effect
[Reverb heavy]	More reverb on this section
[Dry vocal]	Minimal reverb
[Auto-tuned]	Apply autotune
[Vocoder]	Vocoder effect on vocal
[Distorted]	Distorted vocal
[Telephone effect]	Lo-fi phone-quality vocal
[Megaphone]	Megaphone effect
[Underwater]	Filtered, muffled
[Wide stereo]	Wide stereo image
[Mono]	Centered, mono feel
SECTION 9. DYNAMIC & ENERGY TAGS (TIER B)
Tag	Effect
[Building intensity]	Section grows in energy
[Building tension]	Tension rises
[Climax]	Peak energy moment
[Release]	Tension resolves
[Sudden quiet]	Drop to soft dynamics
[Big sound]	Maximum production
[Stripped down]	Minimum production
[Crescendo]	Gradual volume rise
[Decrescendo]	Gradual volume fall
[Key change]	Modulation up
[Modulation]	Same — key change
SECTION 10. RISKY / UNRELIABLE TAGS (TIER C-F — USE WITH CAUTION OR AVOID)
10.1 Unreliable but sometimes work (Tier C)
These work occasionally; have a backup plan.

[BPM 130] — Suno often ignores BPM mid-song.
[Tempo change] — Sometimes works, often ignored.
[Time signature: 7/8] — Specific meter requests fail more than half the time.
[Modulate to D minor] — Specific key changes are unreliable.
[Fade to silence over 8 bars] — Specific bar-count fades are imprecise.
10.2 Avoid (Tier F — these cause problems)
Multiple vocal direction tags in one section ([Whispered] [Belted] [Shouted] simultaneously) — Suno picks one, ignores others, may pick the wrong one.
Negation tags inside Lyrics field ([No drums], [Without bass]) — frequently parsed as inclusion. Use Exclude Styles instead.
Direct artist references ([in the style of <Artist>]) — flagged or blocked.
Markdown formatting (# headers, - bullets) inside Lyrics field — Suno tries to vocalize these.
Long descriptive paragraphs inside [ ] — engine truncates at first comma or period.
Emoji inside tags — unreliable, often re-tokenized poorly.
SECTION 11. STANDARD LYRIC FILE TEMPLATE
Below is the canonical structure every Lyrics field should follow.

[Intro 4]
(instrumental atmosphere)

[Verse 1 8]
[Singing: breathy, intimate]
Lyric line one
Lyric line two (yeah)
Lyric line three
Lyric line four

[Pre-Chorus 4]
[Singing: rising intensity]
Tension line one
Tension line two
Tension line three
Tension line four

[Chorus 8]
[Singing: belted, passionate]
[Doubled]
Hook line one
Hook line two (oh)
Hook line three
Hook line four
Hook line five
Hook line six (yeah)
Hook line seven
Hook line eight — title placement

[Verse 2 8]
[Singing: breathy, intimate]
...

[Pre-Chorus 4]
...

[Chorus 8]
[Singing: belted, passionate]
[Doubled]
[Harmony +3rd]
...

[Bridge 4]
[Singing: vulnerable, half-sung]
[Stripped back]
Departure line one
Departure line two
Departure line three
Departure line four

[Final Chorus 8]
[Singing: belted, triumphant]
[Doubled]
[Harmony +3rd, +5th]
[Ad-libs]
...

[Outro 4]
[Singing: breathy, fading]
Closing line one
Closing line two
(la la la)
[Fade out]
SECTION 12. GENRE-SPECIFIC TAG TEMPLATES
12.1 Pop / K-Pop Template
[Intro 4]
[Verse 1 8] [Singing: conversational, light]
[Pre-Chorus 4] [Singing: building intensity]
[Chorus 8] [Singing: belted, bright] [Doubled] [Harmony +3rd]
[Verse 2 8]
[Pre-Chorus 4]
[Chorus 8]
[Dance Break 8] (instrumental)
[Bridge 4] [Singing: stripped, vulnerable]
[Final Chorus 8] [Key change] [Ad-libs]
[Outro 4]
12.2 Hip-Hop / Trap Template
[Intro 4]
[Verse 1 16] [Rapped] [Trap ad-libs]
[Hook 8] [Sung-rap] [Doubled]
[Verse 2 16] [Rapped]
[Hook 8]
[Bridge 8] [Singing: melodic]
[Hook 8] [Ad-libs]
[Outro 4]
12.3 R&B / Neo-Soul Template
[Intro 4] [Stripped back]
[Verse 1 8] [Singing: breathy, intimate, melismatic]
[Pre-Chorus 4] [Singing: rising]
[Chorus 8] [Singing: passionate, melismatic] [Harmony +3rd] [Ad-libs]
[Verse 2 8]
[Pre-Chorus 4]
[Chorus 8] [Stacked vocals]
[Bridge 4] [Vamp] [Ad-libs] [Spoken: soft]
[Final Chorus 8] [Gospel choir] [Ad-libs]
[Outro 4] [Fade out]
12.4 Indie / Alt Template
[Intro 4] [Acoustic]
[Verse 1 8] [Singing: conversational, vulnerable]
[Chorus 8] [Singing: half-sung, layered]
[Verse 2 8]
[Chorus 8] [Doubled]
[Bridge 8] [Stripped back] [Spoken, soft]
[Final Chorus 8] [Full band] [Building intensity]
[Outro 4] [Fade out]
12.5 EDM / Dance Template
[Intro 8] [Build-Up]
[Verse 1 8] [Singing: airy]
[Pre-Chorus 4] [Build-Up]
[Drop 8] (instrumental)
[Verse 2 8]
[Pre-Chorus 4] [Build-Up]
[Drop 8] (instrumental)
[Breakdown 8] [Stripped back]
[Drop 8] (instrumental)
[Outro 4] [Fade out]
12.6 Rock / Anthem Template
[Intro 4] [Guitar Riff]
[Verse 1 8] [Singing: conversational]
[Pre-Chorus 4] [Building intensity]
[Chorus 8] [Singing: belted] [Big sound]
[Verse 2 8]
[Pre-Chorus 4]
[Chorus 8]
[Guitar Solo 8]
[Bridge 4] [Stripped back] [Singing: vulnerable]
[Final Chorus 8] [Singing: triumphant] [Doubled]
[Outro 4]
12.7 Ballad Template
[Intro 4] [Piano only]
[Verse 1 8] [Singing: intimate, vulnerable]
[Pre-Chorus 4] [Strings enter]
[Chorus 8] [Singing: passionate] [Doubled]
[Verse 2 8]
[Pre-Chorus 4]
[Chorus 8] [Harmony +3rd]
[Bridge 4] [Stripped back] [Singing: half-spoken]
[Final Chorus 8] [Key change] [Singing: belted] [Ad-libs]
[Outro 4] [Fade out]
SECTION 13. TAG PLACEMENT RULES (CRITICAL)
Rule 1 — Section Tag Always First
Every section begins with its structural tag on its own line. Lyric content never precedes the section tag.

Rule 2 — Vocal Direction Tag Second
Place vocal direction tag(s) immediately under the section tag, before any lyric line. Limit to one or two per section.

Rule 3 — Inline Cues Stay Inline
Ad-libs in parentheses, pronunciation overrides in brackets, emphasis markers — all stay within the lyric line where they occur.

Rule 4 — Layering Tags Apply Globally to the Section
Tags like [Doubled], [Harmony +3rd], [Stacked vocals] apply to the whole section they appear in. Place them immediately under the section tag and vocal direction tag.

Rule 5 — Atmosphere/Mix Tags at Section Start
Tags like [Stripped back], [Big sound], [Reverb heavy] apply to the whole section. Place at section opening.

Rule 6 — Transition Cues at Section End or Start
[Fade out], [Build-Up], [Drop], [Beat switch] go at the boundary between sections, on their own line.

Rule 7 — Empty Lines Separate Sections
Always leave one blank line between sections. Suno uses blank lines as breath/section separators.

Rule 8 — Don't Stack Conflicting Tags
[Whispered] and [Belted] in the same section cause Suno to pick one or produce a confused middle. If you want a dynamic shift within a section, use [Whisper to Belt] or split into two sub-sections.

SECTION 14. DIAGNOSTIC: WHEN TAGS GET IGNORED
If your tags aren't working, run these checks in order:

Are tags in the right field? Tags only work in the Lyrics field, never in Style Box.
Are tags in the right bracket form? Structural = [ ], vocalized interjections = ( ).
Is there a section tag above the direction tag? Direction tags need a section tag to scope to.
Are there too many tags in the section? Reduce to one or two key tags.
Are there conflicting tags? Remove conflicts.
Is the lyric field over 4,800 characters? Truncation may have cut tags.
Are tags using approved syntax? Refer to this file's tag list — non-standard tags are silently ignored.
Is the Style Box overpowering the tag? If Style Box says "aggressive belted vocal" and Lyrics tag says [Whispered], the Style Box usually wins. Soften the Style Box vocal directive.
SECTION 15. REFERENCES
Suno-curated:

suno.com/style/with-instrumental-breaks-featuring-guitar-solos
suno.com/style/vocal-layering
Suno community blog tutorials (Ad Libs & Interjections by RUA)
Community-tested guides:

HookGenius — Suno Style Tags List (300+ tested tags)
TagASong — square brackets and structure tag library
JackRighteous — meta tags guide, layered harmonies guide
musci.io — complete Suno tags reference
sunometatagcreator.com — meta tags guide
r/SunoAI — tag-properly threads, meta tag verification
Verification documents:

Suno AI Meta Tags Verification and Usage Guide (Scribd archive)
v5.5 Master Prompt Reddit threads
SECTION 16. RELATED FILES
09_SUNO_ENGINE.md — engine rules, character limits, mode selection.
12_PROMPT_TEMPLATES.md — complete CREATE/COVER and One-Shot templates that consume these tags.
06_VOCAL_PRODUCTION.md — full vocal directive system (this file's vocal tags are compact forms of that system).
04_RHYTHM_AND_FORM.md — song form theory backing the section tag library.
01_OPERATING_RULES.md — pre-generation gate that validates tag use.


---

## SECTION 17. v2.6 보강 — v5/v5.5 메타태그 갱신 (2026-05-20)

2026-05-19 외부 리서치 검증 반영. 기존 §1-16은 그대로 유효,
본 섹션은 v5/v5.5 현행 동작 기반 갱신·신규 태그 추가.

### §17.1 Suno 인식 섹션 태그 — v5 확정 목록

v5에서 안정적으로 인식되는 섹션 태그 (각 태그는 줄 시작 한 줄):

```
[Intro]        [Verse]        [Verse 1]      [Verse 2]
[Pre-Chorus]   [Chorus]       [Hook]         [Post-Chorus]
[Bridge]       [Instrumental] [Instrumental Break]
[Break]        [Interlude]    [Drop]         [Build-Up]
[Breakdown]    [Outro]        [End]          [Fade Out]
```

운영 노트:
- 곡 끝에 [Outro] 또는 [End] 없으면 Suno가 어색하게 컷·페이드.
  반드시 명시.
- [Drop] / [Build-Up] / [Breakdown]은 EDM·하이브리드용. 발라드
  계열에는 [Bridge] / [Interlude]가 자연스러움.
- [Hook]은 [Chorus]와 사실상 동일 처리되나, R&B·힙합 곡에서
  의도적으로 짧고 캐치한 단위를 명시하고 싶을 때 사용.

### §17.2 [Callback] 메타태그 신규 (v5 Studio Timeline)

v5에서 Extend / Replace Section 작업 시 새로 등장한 태그.
이전 섹션의 느낌·요소를 *명시적으로* 참조하라는 메타 지시.

**사용법** (가사 박스 안):
```
[Callback: continue with same vibe as Chorus 1]
[Callback: reference verse melody but darker]
[Callback: same groove as bridge, lower energy]
```

**용도**:
- Extend 시 곡 일관성 유지 (Suno 디폴트는 새 섹션을 다른
  무드로 끌고 가려 함)
- Replace Section 시 교체 섹션이 곡의 다른 부분과 맞물리게
- 곡 후반부 드리프트 방지의 새 무기 (기존 C-5 throughout
  키워드와 보완 작동)

**한계**: [Callback]은 Studio 편집 모드 (Extend/Replace) 작업
시에만 발동. 일반 Generate에서는 인식 약함. v5 Studio 구독자
한정 기능.

### §17.3 인라인 보컬 큐 정리 — v5 검증 어법

가사 줄 사이·줄 끝에 박는 보컬 디렉션. v5에서 안정적으로
인식되는 큐만 추림:

**다이내믹·딜리버리**:
- [Whispered] / [Hushed] — 속삭이듯
- [Soft] — 여리게 (단, 06번 §11.16 함정 주의 — warm
  계열로 끌릴 수 있음)
- [Belted] / [Powerful] — 가창력 폭발
- [Building] — 텐션 상승 중
- [Held] / [Sustained] — 길게 끄는 음

**음색**:
- [Raspy] / [Gritty] — 거친 톤
- [Airy] / [Breathy] — 공기감 섞인
- [Clear] / [Bright] — 또렷·맑은

**감정**:
- [Tender] / [Intimate] — 부드럽고 친밀
- [Urgent] / [Desperate] — 절박
- [Playful] — 가볍고 신난

**배치 룰**:
- 섹션 헤더 다음 줄에 박으면 섹션 전체 적용:
  `[Verse 1]`
  `[Singing: hushed, intimate, audible breath]`
- 라인 끝에 박으면 그 라인만 적용:
  `네 이름을 부르려다 만 손 [Held]`

### §17.4 EXCLUDE 위치 — Style Box 맨 끝 룰

기존 §10번대에 정합. 외부 리서치 확정:
- Suno는 긍정형 태그를 먼저 처리하고 그 다음 exclusion을 적용
- 따라서 EXCLUDE 표기는 **Style Box 맨 끝**에 두는 게 효과 최대
- 형식 (인라인 EXCLUDE):
  `[Style: neo city pop 2020s ... vibraphone solo mid section,
   no synthwave bell pluck, no DX7 FM bell, no key change]`
- Custom Mode의 별도 Exclude 필드 사용 시 위치 무관 (오히려
  별도 필드가 더 신뢰성 높음, 외부 검증)

### §17.5 v5/v5.5 현황 요약 — 가사·태그 영향

- v5 (2025-09 출시): 부정 프롬프트 정식 지원, Studio 편집, 스템
  분리, 섹션 편집 도입. 가사 5000자 / 스타일 박스 1000자.
- v5.5 (2026-03-26 출시): v5 위 개인화 레이어. Voices / Custom
  Models / My Taste. **가사·태그 문법은 v5과 100% 동일.**
- v5 이전 (v4 등): 스타일 박스 200자, 부정 프롬프트 미지원.
  우리 SOP는 v5 기준이므로 무관.

운영 시점 (2026-05) — 모든 사용자가 v5 디폴트 생성. 우리 가사
태그 SOP는 그대로 유효.

---



---

## SECTION 18. GRENAR'S DIRTY TRICKS — FULL BODY (NEW v2.7)

External research source: Reddit Grenar Days 1-10 syntactic patterns,
verified by community testing.

### §18.0 Why this section exists

Field guide synthesis showed 10 distinctive Suno lyric/tag syntactic
patterns operator's prior SOP did not document fully. v2.7 absorbs
them as Tier A/B (community-verified) reference.

### §18.1 Live Concert Mode

```
[Intro: Live Crowd]
*crowd cheering* *applause* *whistles*
[Verse 1 8]
```

Effect: Adds crowd ambience to verse / chorus. Useful for *anthemic*
or *stadium* deliveries. Caution: overuse triggers stadium reverb
which can muddy mix. Tier B.

Inline placement:
```
[Final Chorus 16]
We're standing on the edge *crowd: WHOA-OH-OH!*
We're never coming back *crowd cheering*
```

### §18.2 Phonetic Respelling (Pronunciation Override)

Suno mispronounces by *phonetic pattern matching*, not understanding.
Override via respell:

| Trap word | Respell |
|---|---|
| `read` (past tense) | `red` |
| `read` (present) | `reed` |
| `live` (verb) | `lyve` |
| `live` (adjective) | `liev` |
| `tear` (rip) | `tair` |
| `tear` (cry) | `teer` |
| `wind` (noun) | `wynd` |
| `wind` (verb) | `whined` |
| `lead` (verb) | `leed` |
| `lead` (metal) | `led` |
| `tomorrow` | `tuh-MAH-roh` |

For numbers / acronyms: spell out.
- `2026` → `twenty twenty six`
- `NASA` → `naa-saa`

Keep operator-readable copy separate; Suno gets phonetic version.
Tier S.

### §18.3 Homophone Filter Bypass

If certain words trigger content filter:
- Distance from sensitive vocabulary
- Use homophone or near-rhyme
- Pass through punk / metal / hip-hop genre Style Box (less strict)

Examples (operator-tested):
- Sensitive word → euphemistic homophone
- Brand name → consonant-substituted version
- Real person name → kana-bracketed Korean version (`NMIXX(엔믹스)`)

Tier B — case-by-case verification needed.

### §18.4 Rap Cadence Control (Hyphen-Runs)

Force *fast rap delivery*:
```
[Verse 1 8 | Rap delivery | Fast cadence]
i-hit-the-street-with-my-shoes-on-fire
you-ain't-never-seen-a-flow-like-this-one
```

- Hyphens between words: forces fast 16th-note delivery
- Periods: hard stops within a line
- Commas: subtle pauses, breath points
- Ellipsis (`...`): drawn-out drift

Combined:
```
i-hit-the-street, then i stopped... and walked away.
```

Tier A.

### §18.5 ALL CAPS Emotional Spike

```
[Chorus 16]
I see you in the morning light
You make me feel ALIVE
WHY DON'T YOU TELL ME?!
```

Effect: ALL CAPS lines = louder delivery, *emotional peak*.

Rules:
- Use sparingly (1-2 per song)
- *Contrast* matters — surround with lowercase
- Pair with `!` or `?!` for vocal intensity
- Avoid full verses in ALL CAPS (loses contrast effect)

Tier S.

### §18.6 Stretching / Stuttering

#### Stretching (sustain a syllable)
```
lo-o-o-ove me
ne-e-ever let go
B-A-B-Y
```
- Dashes between repeated letters = sustained vowel
- Suno holds the note longer on stretched parts
- Works for both vowels and consonants

#### Stuttering (rapid repetition)
```
B-b-baby tell me what to do
Sh-sh-shake it off
```
- Letter + dash + same letter = stutter
- Suno articulates as rapid attack
- Pop / R&B / hyperpop staple

#### L-O-V-E spelling
```
L-O-V-E that's what you give to me
```
- Each letter pronounced separately
- Adds *playful* / *youthful* texture
- K-pop / bubblegum frequent use

Tier S.

### §18.7 Parentheses Background Vocals

```
[Verse 1 8]
I'm walking down the street tonight (walking alone)
Looking for a friend to find (yeah, yeah)
But all I see is empty rooms (empty rooms)
```

- `( )` = background / harmony / ad-lib vocals
- Place at line end (operator C-3 rule)
- Common contents:
  - Echo of preceding word: `(walking alone)` after "street tonight"
  - Ad-lib affirmation: `(yeah!)` `(uh!)` `(oh!)`
  - Harmony cue: `(harmony +3rd)` — inline harmony

Tier S.

### §18.8 Pipe Tag Stacking (Multi-Modifier Sections)

Full body covered in 09 §29.3.

Stack syntax:
```
[Section | Mod 1 | Mod 2 | Mod 3 | Mod 4 ...]
```

- Max 7 elements (after that Suno parser drops trailing)
- First element = section type (Verse, Chorus, etc.)
- Second onward = modifiers in priority order (left = strongest)

Operator-verified stacks:
```
[Chorus 16 | Anthemic | Stacked harmonies +3rd +5th | Brass | Drop]
[Verse 1 8 | Sparse | Single vocal | Acoustic guitar only |
 Behind the beat]
[Bridge 8 | Stripped down | Closer mic | Intimate | Half-time]
[Final Chorus 16 | Key up half-step | Layered vocals | Full band |
 Belted]
[Drop 8 | Heavy 808 | Sidechained synth | Vocal chops | EDM-style]
```

Tier S.

### §18.9 Inline Ad-libs (Right-Aligned Only)

Operator C-3 rule (already mandatory):
```
✓ I'm on top [yeah!] of the world [uh!]
✓ Walking down the street (whoa)
✗ Walking down the street
  (whoa)                  ← INDEPENDENT LINE FORBIDDEN
```

Reason: independent `(adlib)` lines confuse Suno parser — interpreted
as full lyric line, not ad-lib decoration. Always *inline at line end*.

Operator-verified ad-lib palette:
- Affirmation: `(yeah)` `(uh)` `(oh)` `(mmm)` `(ah)`
- Excitement: `(woo!)` `(yeah!)` `(let's go!)`
- Soft: `(oh baby)` `(mmhm)` `(yeah baby)`
- K-pop: `(yeah-yeah)` `(우우)` (uu-uu) `(yo!)`
- Hip-hop: `(uh-huh)` `(skrrt)` `(yeah-yeah)` `(let's get it)`

Tier S.

### §18.10 Broadway Clarity Hack

Style Box keyword:
```
Broadway musical clarity, theatrical vocal projection
```

Effect (counterintuitive): Style Box says "Broadway" but output is
*not Broadway-style*. Instead, Suno applies *enunciation clarity*
across whatever genre is set.

Use cases:
- Korean lyrics mispronouncing → add "Broadway musical clarity"
- Hip-hop verses mumbled → add for clearer rap diction
- Heavily mixed productions where vocals get buried

Combined with genre:
```
Modern K-pop with female vocals and 128 BPM, synth-pop production.
Broadway musical clarity on lead vocals, theatrical projection.
```

Tier B — works ~60% of generations per community testing.

---

## SECTION 19. DUET LABELS-PER-LINE (NEW v2.7)

### §19.1 Why this section exists

Operator's persistent failure mode in duet projects (Serica × Cheny):
which vocal sings which line. Operator's prior approach (`vocal 1:`
prefix or section markers) was unreliable.

External research + operator verification: **bracket label per line**
is the verified method.

### §19.2 Verified syntax

```
[V1] 6시 옥상 위에 콘크리트가 녹아
[V2] 에어컨이 죽었다, 너에게 보낸 톡
[V1+V2] 답장은 오지 않고 햇빛이 차오르네
[V2] 공룡들도 이런 날에 안녕했을까
```

Rules:
- `[V1]` `[V2]` `[V3]` = vocal index labels at line start
- `[V1+V2]` = both vocals together (unison or harmony)
- `[V1 → V2]` = handoff mid-line (rare, use sparingly)
- Each lyric line MUST have a label (no unlabeled lines)

### §19.3 Combination with Vocal Anchor

09 §25 Vocal Anchor at lyrics top:
```
[Vocal 1 (Serica): female soprano C4-E5, clear calm polite.]
[Vocal 2 (Cheny): female high soprano E4-G5, child-like punk-rap,
sweet light airy.]

[Verse 1 16]
[V1] 햇빛이 너무 환해
[V1] 옥상에 올라왔어
[V2] 어머나 진짜 더워!
[V2] 콘크리트가 녹아!
[V1+V2] 우리 같이 외쳐볼까
```

Anchor declares character voice. Line labels assign performance.

### §19.4 Anti-Patterns (Forbidden)

```
✗ vocal 1: 햇빛이 너무 환해     ← prefix syntax fails
✗ V1 - 햇빛이 너무 환해        ← dash separator fails
✗ Serica: 햇빛이 너무 환해     ← character name not recognized
✗ 햇빛이 너무 환해 [V1]        ← label must be line start
✗ [V1]햇빛이 너무 환해          ← need space after bracket
```

### §19.5 Three-vocal handling

```
[Vocal 1 (V1): ...]
[Vocal 2 (V2): ...]
[Vocal 3 (V3): ...]

[V1] first vocal line
[V2] second vocal line
[V3] third vocal line
[V1+V2+V3] all three together
[V1+V3] one and three (skip middle)
```

### §19.6 Operator-confirmed character ↔ vocal label mapping

For operator's recurring characters:

| Character | Label | Voice baseline |
|---|---|---|
| Serica | V1 | female soprano C4-E5, refined |
| Cheny | V2 | female high soprano E4-G5, punk-rap |
| 테피 | V1 or V3 | (per case file 99_OPERATOR_VAULT Part B (캐릭터 베이스라인)) |
| 우나 | V2 | (per case file) |
| 크래더 | V1 | (per case file) |
| 봉남이 | V2 | (per case file) |

Character names go in **Vocal Anchor only**, **never in Style Box**.

---

## SECTION 20. LYRIC BLEED COUNTERMEASURES (NEW v2.7)

### §20.1 Problem definition

Suno reads *anything singable-looking* as lyric input. Style Box
content can leak into vocal output.

Full diagnosis: 09 §31.

### §20.2 Tag-level countermeasures

Inside Lyrics field, place these at top to *block* bleed:

```
[STYLE BOX ENDS HERE]
///*****///

[Vocal Anchor: ...]
[Verse 1 8]
...
```

The `///*****///` separator + explicit "STYLE BOX ENDS HERE" tag
signals Suno that lyric content begins now.

Tier B — partial effectiveness, varies by generation.

### §20.3 Empty-Lyrics-Box bleed

If Lyrics field is empty:
- Suno auto-generates lyrics from Style Box
- Style Box content (descriptions, technical terms) gets sung

Prevention:
- ALWAYS fill Lyrics Box, even with single line
- Minimum: `[Intro 8] [Instrumental]`
- For instrumental track: `[Intro 4] [Verse 1 8 Instrumental] ...`

---


## SECTION 21. v2.11 EXPANSIONS — SUNO MASTERY INTEGRATION

External research consolidation (HookGenius, Blake Crosley, AJ Suno
Mastery, AnimalMonk Knowledge Base, songaifarm.com, jackrighteous.com,
TikTok community, Reddit r/SunoAI, Suno official docs v5.5).

This section adds 7 sub-sections that bring Suno mastery on par with
the best external guides — *plus* operator-specific discoveries from
Case 41 v2.10 session.

### §21.1 Hangul direct-input rule (v2.11 NEW)

External verification (HookGenius Korean prompts 2026):
> *"Always use Hangul (한글) characters, never romanized Korean.
> Suno processes Hangul much better for pronunciation and natural
> phrasing. Keep lines relatively short — Korean syllables pack more
> meaning per character."*

**Rule (CRITICAL v2.11):**
- ❌ `il-dan ttwi-eo` / `ileul ttwieo` / `Annyeong` — romaja in lyrics
- ✅ `일단 뛰어` / `안녕` — Hangul direct
- Romaja allowed ONLY for Style Box context cues (e.g.
  "Korean-language vocal topline with crisp diction") — never in
  Lyrics field.

**Konglish handling:**
- Korean root + English word: write English in Latin alphabet
  ("일단 뛰어 *also* 뛰어")
- English-borrowed Korean concept: Hangul (e.g. "*케이크*" not "*cake*"
  if Korean-spoken in song)

**Natural spacing rule:**
- Each 어절 gets a space — Suno parses 어절 as a breath unit
- ❌ "어차피내일도same old song"
- ✅ "어차피 내일도 same old song"
- Run-on Korean = compressed/mumbled Suno output

### §21.2 Suno-safe line syllable rule (v2.11 NEW)

External verification (HookGenius lyrics 2026):
> *"Suno v5/v5.5 handle 6-12 syllables per line most reliably. Past
> 15 the model rushes or smears the consonants together. If a line
> is loaded, break it. Two 8-syllable lines always out-sing one
> 16-syllable line."*

**Per-language Suno-safe zones:**

| Language | Reliable zone | Past this → degradation |
|---|---|---|
| English | 6-12 syllables | 15+ |
| Korean | **6-10 음절** (denser per character) | 12+ |
| Japanese | 6-12 mora | 15+ |
| Spanish | 6-12 syllables (with sinalefa) | 15+ |

**Implementation:**
- Count syllables (한국어 음절) per line before output
- If a verse line exceeds zone, *break it* into two shorter lines
- Choruses: 4-8 syllable hooks land HARDEST

**Cross-reference:** 14 §2.7.1 / §7 Gate item 23.

### §21.3 Stress-kick alignment (trochaic landing) (v2.11 NEW)

External verification (HookGenius lyrics 2026):
> *"Suno places vocal stress on the strong beat of the bar. Write
> lyrics where the stressed syllable of each line lands where the
> kick lands. Write against the stress and the model fights you —
> rushing, mumbling, or shifting the syllable."*

**English / Spanish:**
- ✅ "**DAN**cin' in the **MOON**light" (trochaic, beat 1 & 3)
- ❌ "the dan**CING** of the **MOON** in the sky" (iambic + run-on)

**Korean (어절 strong-position):**
- ✅ "**일**단 **뛰**어" (1st syllable of each 어절 = beat)
- ❌ "이르단 뛰이어" (artificial stress)

**Cross-reference:** 14 §2.7.2 / 14 §7 Gate item 24.

### §21.4 First-line hook landing (v2.11 NEW)

External verification (HookGenius lyrics 2026):
> *"Suno gives the most melodic weight to the first line of each
> tagged section. Choruses work best at 2 to 4 lines."*

**Rule:**
- Put the hook line as the FIRST line of [Chorus]
- Don't bury the hook at line 3 of a 6-line chorus
- 2-4 line choruses get full melodic emphasis
- 5+ line choruses → Suno may re-weight, burying the hook

**Example:**

```
✅ Good
[Chorus]
일단 뛰어 (hook FIRST)
출근 또 뛰어
GOAT 아닌데 오늘 밤만은

❌ Buried
[Chorus]
출근 또 뛰어
영어학원 뛰어
일단 뛰어 (hook hidden at line 3)
GOAT 아닌데
```

**Cross-reference:** 14 §2.7.4 / 14 §7 Gate item 25.

### §21.5 Vocal direction library — Suno-tested (v2.11 NEW)

External verification (AJ Suno Mastery, jackwellshop.gumroad,
songaifarm.com) — Suno-tested high-signal vocal direction tags.

**Tier 1 — High-signal (always reliable):**

| Tag | Effect |
|---|---|
| `[Whispered]` | Pure whisper delivery, intimate |
| `[Belted]` | Full-throat power, chorus peak |
| `[Spoken Word]` | Speech-singing, no melody |
| `[Falsetto]` | Head-voice register |
| `[Vocal fry]` | Creaky low register, edge |
| `[Doubled]` | Same vocal stacked tight |
| `[Stacked vocals]` | Multi-voice harmony |
| `[Harmony +3rd +5th]` | Specific interval stacking |
| `[Hushed conversational]` | Soft talky |
| `[Crowd-shoutable]` | Anthemic chorus |

**Tier 2 — Style descriptors (Style Box):**

| Tag | Effect |
|---|---|
| `airy female vocals` | Light, breathy |
| `powerful male vocals` | Chest-voice belt |
| `raspy vocals` | Texture/edge |
| `breathy vocals` | Intimate, ASMR-like |
| `crooner vocals` | 1950s sustained smooth |
| `gospel vocals` | Melisma-heavy |
| `auto-tuned vocals` | T-Pain era pitch correction |
| `pitched-up vocals` | Hyperpop crystalline |
| `nasal vocals` | Sassy / character |
| `chest voice` | Full body resonance |

**Tier 3 — Negative (EXCLUDE field):**

| Tag | When to use |
|---|---|
| `no autotune` | Force raw vocal |
| `no reverb wash` | Dry mix |
| `no falsetto` | Force chest belt |
| `no choir` | Block backing layer |
| `no oohs` | Block ad-lib backing |
| `no melisma` | Force straight notes |

**Cross-reference:** 06 §11 5-element Vocal Anchor / 09 §25 / C-29.

### §21.6 Persona Stacking framework (v2.11 NEW)

External verification (arkiii Suno Personas 2026):
> *"Persona Stacking — singers as characters, not prompts. Most
> Personas drift or feel ignored — design problem, not prompt
> problem."*

**Workflow (Pro/Premier tier):**

1. **Design layer**: 99_OPERATOR_VAULT Part B (캐릭터 베이스라인) character baseline (24 characters)
2. **Sample layer**: 8-16바 vocal sample per character, multiple
   tempos/keys, both soft + power delivery
3. **Persona creation**: Upload samples → Suno trains Persona
4. **Persona application**: Future songs call Persona ID
5. **Stack with prompt**: Persona + detailed Vocal Anchor + Style
   Box — three layers stack for max coherence

**Operator catalog opportunity:**
- 24 character baselines → 24 Personas potentially
- Series continuity solved (same character = same Persona)

**Cross-reference:** 09 §33 / 06 §14.

### §21.7 Section markers v5/v5.5 reference list (v2.11 NEW)

External verification (Blake Crosley v5.5 reference, Suno official):

**Structure markers (lyrics field, own line):**
- `[Intro]` / `[Intro: 8 bars]`
- `[Verse 1]` / `[Verse 1: 16]`
- `[Pre-Chorus]` / `[Pre-Chorus: 8]`
- `[Chorus]` / `[Chorus: 16]`
- `[Post-Chorus]`
- `[Bridge]` / `[Bridge: 8]`
- `[Breakdown]` / `[Drop]`
- `[Outro]` / `[Outro: 8 bars Fade]`
- `[Instrumental]` / `[Interlude]`
- `[Solo: guitar]` / `[Solo: saxophone]`

**Energy / mood modifiers (stacked with `|`):**
- `[Chorus | Anthemic | Stacked | Brass]`
- `[Bridge | Intimate | Solo piano | Whispered]`
- `[Drop | Hardstyle | Reverse bass | Distorted kick]`

**Inline delivery tags (within lyrics, parentheses or brackets):**
- `(yeah)` / `(oh)` — ad-lib
- `[Doubled]` — vocal layer
- `[Whispered]` — delivery mode
- `[F5 belt spike]` — specific peak note
- `[Held note: 2 bars]` — sustain
- `[Pause half bar]` — explicit silence

**Suno v5.5 confirmed working (Blake Crosley):**
- Time signature tags (`[6/8]`) — *editing surface only*, not generation
- BPM tags (`[155 BPM]`) — *reliably respected in v5.5*
- Era tags (`[2025-2026]`) — *aggressively bias production style*

**Cross-reference:** 09 §29 / §30 / C-30.

---

## SECTION 22. EXCLUDE FIELD MASTERY (v2.11 NEW)

External verification + operator discovery (Case 41 v2.10 session
+ this v2.11 session).

### §22.1 The "200-character limit" is a guideline, not a hard cap

Operator discovery (v2.11 session):
> *"EXCLUDE는 200자도 넘게 할 수 있는데 잘 깎으면 그만 아님?"*

External verification (HookGenius character limits 2026):
> *"You can use multiple negative prompts, but keep the total style
> prompt under 200 characters. Prioritize your 2-3 most important
> exclusions for best results."*

**Reconciliation (v2.11 rule):**
- 200 chars = recommended sweet spot
- Past 200 chars: still works, *priority-based pruning* applied
- Hard cap: not documented officially. Cut from low-priority tier
  if exceeded.

### §22.2 Priority tier system (v2.11 NEW)

**Tier 1 — Always-keep (high-signal negative):**
- `no autotune`
- `no reverb wash`
- `no choir`
- `no oohs`
- `no falsetto`
- `no melisma`

External verification (songaifarm.com 2026): *"no autotune and no reverb
wash are two of the highest-signal negative tags. They consistently push
the model toward a rawer, more organic result."*

**Tier 2 — Anti-drift (C-6 default):**
- `stadium reverb live audience crowd cheering`
- `muddy lo-fi mix compression artifacts`
- `autotune robotic vocal`

**Tier 3 — Pop Gravity Well defense (when needed):**
- `pop modern radio polish`
- `generic festival EDM filler`

**Tier 4 — Concept protection (per song):**
- `slow ballad emo melancholic` (when concept = dance)
- `bright cheerful` (when concept = dark)
- `2010s K-pop average production` (when era anchor critical)

**Tier 5 — Weak negatives (drop first when over 200 chars):**
- Vague descriptors that overlap with positive Style Box content
- Negatives already implied by genre tag

### §22.3 Style Box "no X" syntax — UNRELIABLE

External verification (Blake Crosley v5.5 reference 2026):
> *"'No drums' in the Style field is unreliable. Use the official
> Exclude field under Advanced Options for unwanted instruments and
> elements."*

**Rule (v2.11):**
- ❌ Style Box: `"warm acoustic guitar, no drums, no autotune"`
- ✅ Style Box: `"warm acoustic guitar with intimate male vocal"`
  Exclude field: `"drums, autotune, percussion"`

Negatives ALWAYS go in Exclude field. Style Box stays positive-only.

### §22.4 EXCLUDE writing workflow (v2.11)

```
Step 1: Identify Tier 1 high-signal negatives needed (1-2)
Step 2: Add Tier 2 anti-drift (C-6 default — 2-3)
Step 3: Add Tier 3 Pop Gravity Well IF genre at risk (0-1)
Step 4: Add Tier 4 concept protection IF needed (0-2)
Step 5: Count characters
  - Under 200: ship
  - 200-250: review Tier 5 candidates, prune if any
  - Over 250: prune Tier 5, then weakest Tier 4
Step 6: Verify NO negatives leaked into Style Box (§22.3)
```

**Default count: 3-4 items** (operator practical range)
**Maximum recommended: 5-6 items** (arrangement instability risk past 6)
**Hard ceiling: ~7 items** (external research consensus)

### §22.5 Cross-reference

- 00 C-16.2 / C-46 — EXCLUDE redesign rules
- 09 §26 — Pop Gravity Well defense
- 99_OPERATOR_VAULT Part F (검증 키워드) — High-Signal Negative tag library (v2.11 expansion)

---

## SECTION 23. POSITION-BASED WEIGHTING (v2.11 NEW)

External verification (AnimalMonk Knowledge Base, Suno Database
compilation):

> *"Tag Weighting: Position 1 = ~50% influence, Position 2 = ~25%,
> Position 3 = ~12.5%, Position 4+ = diminishing. Always frontload
> the most important sonic element."*

### §23.1 The math

| Position | Influence weight |
|---|---|
| 1 | ~50% |
| 2 | ~25% |
| 3 | ~12.5% |
| 4 | ~6% |
| 5+ | <5% (diminishing) |

**Implication:** Whatever is in Position 1 = 50% of how Suno hears
the entire prompt. Everything after Position 4 = decoration.

### §23.2 Application — Style Box position planning

**Tight Mode (250-350 chars):**
- Position 1 (50%): Strongest microgenre word
- Position 2 (25%): Era anchor / dominant mood
- Position 3 (12.5%): Vocal identity OR signature instrument
- Position 4-5: Tempo + key
- Position 6+: Detail (drop if over budget)

**Dense Mode (700-950 chars):**
- Position 1 (50%): Same — microgenre 1-word
- Position 2 (25%): Era + style lineage
- Position 3 (12.5%): Vocal directive 5-element open
- Position 4+ (decoration): Instruments, production, mix, throughout

### §23.3 Position 1 — what to put there

✅ Strong microgenres (50% weight rewards specificity):
- `Festival mainstage hardstyle anthem`
- `Modern UK garage 2-step`
- `2026 hyperpop crystal`
- `Vintage 70s funk soul`
- `Brazilian bossa nova jazz fusion`

❌ Weak Position 1 candidates:
- `K-pop` (industry category — C-40)
- `Pop` (Pop Gravity Well — too broad)
- `Electronic` (genre cloud — vague)
- `Beautiful` (mood word — wastes 50%)

### §23.4 Common Position 1 mistakes

**Mistake 1: Industry category leak**
- ❌ `"K-pop hardstyle anthem"` → Position 1 = "K-pop" → 50%
   regression to average K-pop
- ✅ `"Festival hardstyle anthem with Korean topline"` → Position 1
   = "Festival hardstyle" → 50% to hardstyle

**Mistake 2: Compound microgenre dilution**
- ❌ `"Pop-rock indie-folk crossover"` → Position 1 has 3 weak
   genres splitting 50%
- ✅ `"Indie folk-rock with pop polish"` → Position 1 = "Indie folk-rock"
   one clear unit

**Mistake 3: Mood-first**
- ❌ `"Beautiful emotional ballad"` → 50% wasted on "Beautiful"
- ✅ `"Cinematic piano ballad, beautiful and emotional"` → 50% on
   actionable "Cinematic piano ballad"

### §23.5 Cross-reference

- 00 C-28.1 ② — Position 1 macrogenre prohibition (v2.11 +
  quantified)
- 00 C-40 — Industry category banishment
- 00 C-45 — Position-Based Weighting rule (this section is the
  technical detail)
- 09 §38 — Style Box position planning workflow

---

## SECTION 24. CREATIVE SLIDERS — WEIRDNESS / STYLE INFLUENCE / AUDIO INFLUENCE (v2.11 NEW)

External verification (Suno v5.5 docs, Hollyland 2026, openmusicprompt
2026).

### §24.1 Three sliders explained

**Weirdness (0-100, default 50):**
- Low (0-30): Safe, average, follows training distribution
- Medium (40-60): Balanced — default sweet spot
- High (70-100): Glitch, dark, experimental, unexpected harmonies

**Style Influence (0-100, default 50):**
- Low (0-30): Genre tag weakly applied — more freedom
- Medium (40-60): Genre tag applied at typical strength
- High (70-100): Genre tag aggressively applied — every detail
  conforms

**Audio Influence (0-100, UI default 25 — COVER는 25에서 올림: lead 60-75 / texture 20-40):**
- Only active when reference audio uploaded
- Low (0-40): Reference is a vibe suggestion
- Medium (50-70): Reference shapes production
- High (80-100): Reference strongly constrains output

### §24.2 Application guide

**For sketches / exploration:**
- Weirdness 50-60 / Style Influence 40-50 — let Suno surprise

**For polished production:**
- Weirdness 40-50 / Style Influence 70-80 — tight control

**For experimental tracks (Case 32 microtonal era):**
- Weirdness 70-85 / Style Influence 40-50 — embrace glitch

**For reference-based tracks:**
- Weirdness 30-40 / Audio Influence 70-80 — mirror reference

### §24.3 Cross-reference

- 11 §17 — production design weirdness/influence summary
- 00 C-47 — Tight/Dense mode (slider settings tie to mode choice)

---

## SECTION 25. STUDIO / ITERATIVE WORKFLOW (v2.11 NEW)

External verification (Blake Crosley v5.5 reference 2026):
> *"Effective Suno usage follows an iterative workflow, not a
> single-prompt approach. Generate in Suno until the arrangement
> and vibe are right → stem edit → section replace."*

### §25.1 Studio mode features (Pro/Premier)

1. **Stem export**: Separate vocals from instrumental, or 12-track
   breakdown (vocals, drums, bass, harmony, melody, etc.)
2. **Section Replace**: Regenerate just one section (Verse 2 only,
   Bridge only) without redoing the whole song
3. **Warp Markers**: Micro-adjust timing of notes/phrases with
   quantize snap-to-grid
4. **Alt Takes**: Generate and audition alternative sections inline
5. **Remove FX**: Strip AI-applied reverb/delay to get dry stems

### §25.2 Iterative workflow

```
1. First generation (full Style + Lyrics)
2. Listen — identify which sections work, which don't
3. Section Replace on weak sections (not whole-song regen)
4. Once arrangement satisfies → export stems
5. DAW work: EQ, additional mix, replace stems if needed
```

**Cross-reference:** 00 C-48 / 09 §39.

---

## SECTION 26. REFERENCE TRACK UPLOAD (v2.11 NEW)

External verification (Suno v5.5 docs, Suno API docs).

### §26.1 Capabilities

- **Free tier**: Upload up to 60 seconds, generates ~30 seconds based on
- **Pro tier**: Upload up to 2 minutes (some sources cite 8 min for
  V4_5PLUS / V5 models)
- **Premier tier**: Reference Track Upload feature — locks audio
  characteristics as persistent influence

### §26.2 Best practices

- Clean reference audio (no background noise, no other voices)
- Match desired output style (don't upload heavy metal if you want
  ballad)
- Set Audio Influence slider 60-80% for shape-mirroring
- Use operator's own previous best work as reference for
  catalog consistency

### §26.3 Operator catalog application

**Workflow:**
1. Identify operator's "best" track in a given style (e.g. Case 24b
   modern UK garage)
2. Upload that track as Reference
3. New songs in similar style → upload reference + new prompt
4. Result: Suno learns operator's specific catalog sound

**Cross-reference:** 00 C-49 / 09 §35.

---

## SECTION 27. UNOFFICIAL HACKS (v2.11 NEW — OPERATOR-OPT-IN ONLY)

⚠️ **Operator-explicit-request only.** Default workflow uses
official 5-Layer artist workaround (00 C-1.2). Unofficial hacks
have policy risk and commercial release risk.

External sources: TikTok community, Facebook Suno Lovers group,
Reddit r/SunoAI compilation, aitooltips.com bypass guides.

### §27.1 Number-letter obfuscation

**Method:** Replace letters with phonetically similar numbers/symbols.
**Example:**
- `Taylor Swift` → `T4yl0r 5w1ft` / `Tayl0r Swyft`
- `Beyoncé` → `Bey on say` / `Bey-Yon-Say`
- `BLACKPINK` → `BL4CKP1NK` (untested — high detection risk)

**Reliability:** Hit-or-miss. Sometimes passes filter, sometimes
flagged. Test with small generation first.

### §27.2 Language transliteration

**Method:** Write artist name in different script (Korean/Japanese/
phonetic English).
**Example:**
- `BTS` → `비티에스` (Korean phonetic) / `B.T.S` (dot separation)
- `Michael Jackson` → `마이클 잭슨` (Korean — sometimes passes)

**Reliability:** Higher than §27.1 for some artists (Korean/Japanese
acts via Korean/Japanese transliteration). Western artists less
reliable.

### §27.3 Era + work + style combination

**Method:** Bypass artist name with their era's signature.
**Example:**
- `Michael Jackson` → `"King of Pop 80s era + Thriller-era pop-funk"`
- `Madonna` → `"Like a Virgin era pop"`
- `Prince` → `"Minneapolis sound era + Purple Rain era"`

**Reliability:** High. Officially "fair" since these are eras/works,
not direct artist references.

### §27.4 Producer/disciple lineage

**Method:** Use producer name (which is allowed) or "disciple-of" framing.
**Example:**
- `Michael Jackson` → `"Quincy Jones-trained dance pop"` / `"MJ-trained
  production lineage"`
- `Aretha Franklin` → `"Atlantic Records soul-era production"`

**Reliability:** Very high. Producer names are not artist names.

### §27.5 Risk acknowledgment

System usage of unofficial hacks:
- Display 1-line warning: `⚠️ 비공식 어법 — 정책 변동 / 상업 배포
  리스크 운영자 책임`
- Document use in 99c case Lock if song is built on hack
- Recommend §27.4 (producer lineage) as safest of the four

**Cross-reference:** 00 C-1.4 / C-50.

---

# END OF 10_SUNO_LYRICS_TAGS v2.11


## § USER EXTENSION ZONE v2.0 (2026-05-24)

bitwize structure-tags + voice-tags + instrumental-tags 풀바디.


### §UE-1. Structure Tags Reference

```
[Intro] — 'notoriously unreliable', 대체:
  [Short Instrumental Intro]
  [Intro - Spoken]

[Verse] / [Verse 1] / [Verse 2] / [Catchy Verse]
[Chorus] / [Catchy Hook]
[Bridge] / [Pre-Chorus]
[Break] / [Interlude]
[Instrumental] / [Instrumental Break]
[Guitar Solo] / [Piano Solo] / [Drum Solo] / [Bass Solo] /
[Synth Solo] / [Saxophone Solo] / [Violin Solo]
[Melodic Interlude] / [Guitar Solo Interlude]
[Dance Break]
[End] / [Outro] / [Final Chorus]
```


### §UE-2. Voice Tags Reference (06 USER EXTENSION 통합)

19 vocal style tags + V5 Voice Gender Selector.


### §UE-3. Instrumental Tags Reference

```
사용:
- Custom Mode 진입
- Instrumental: On 또는 lyrics blank
- Style prompt에 장르/스타일 명시

Section tags 활용:
[Instrumental]
[Instrumental Break]
[Guitar Solo]
[Piano Solo]
[Drum Solo]
[Bass Solo]
[Synth Solo]
[Saxophone Solo]
[Violin Solo]
[Melodic Interlude]
```


### §UE-4. Sound Effects Brackets (C-68)

```
[laughter] / [whisper] / [screaming] / [echo] / 
[crowd] / [applause] / [footsteps] / [breath]

Note: mid-line 박음 best, standalone 금지
```


### §UE-5. Atmospheric Effects (C-68)

```
Lyrics Box + Style Box 양쪽 박음:

Lyrics:
[Verse]
Rain falling on the window
Thunder in the distance

Style:
"lofi effects rain, ambient thunder"

Atmospheres:
- rain + "lofi effects rain"
- wind + "ambient wind textures"
- fire + "crackling fire ambience"
- ocean + "ocean waves background"
```


### §UE-6. Bar Count Targeting (C-65)

```
[INTRO 4] [VERSE 1 8] [PRE 4] [CHORUS 8] [BRIDGE 8] [OUTRO 4]
```


# === END 10 USER EXTENSION ZONE v2.0 ===





# ============================================================
# § USER EXTENSION v2.0 FINAL Polish (2026-05-26)
# Suno V5 / V5.5 Metatag 풀바디 보강 (HookGenius 300+ / 외부 정설)
# ============================================================


## §UE-30. Metatag 핵심 원칙 (HookGenius 외부 검증)

```
원칙:
- Metatag = 대괄호 [] 안 명령어
- Suno V5는 *structural control*로 metatag 활용
- 가사 필드 안에 박음 (Style Box 아님)
- Case-insensitive: [Verse] = [VERSE] = [verse]
- 새 라인에 박음 (섹션 시작 자리)
- Stack 가능: [Chorus] [Belted] = chorus + 강한 보컬

배치 룰:
- 가장 중요한 tag → 첫 20-30 단어 안
- 1-2 genre tags / 2-3 instrument tags / 1-2 mood tags 권장
- 8+ tags → V5 prompt fatigue 위험
```


## §UE-31. Structure Metatags 풀바디

### §UE-31.1 기본 구조 태그

```
[Intro]           — 곡 시작 (V5는 자동 확장 경향 — Short Instrumental 권장)
[Verse 1]         — 첫 절
[Verse 2]         — 둘째 절
[Pre-Chorus]      — 빌드업
[Chorus]          — 후렴 (가장 강한 자리)
[Bridge]          — 대비/반전
[Post-Chorus]     — 후렴 후 hook
[Outro]           — 마무리
[Drop]            — EDM 자리
[Refrain]         — 짧은 후렴
[Hook]            — 메모러블 자리
```

### §UE-31.2 Bar Count Targeting (C-65 외부 정설)

```
[INTRO 4]         — Intro 4바
[VERSE 1 16]      — Verse 1 16바
[PRE 8]           — Pre-chorus 8바
[CHORUS 16]       — Chorus 16바
[BRIDGE 8]        — Bridge 8바
[OUTRO 4]         — Outro 4바

Notes (외부 정설):
- 결과는 approximate (Suno는 target으로 처리, 절대치 X)
- 명시 섹션 태그와 *조합* 사용 best
- intro/outro 길이 제어에 특히 효과적
- 우리 어법 [Verse 1: 16]도 작동 — 두 어법 다 OK
```

### §UE-31.3 섹션 변형 태그

```
[Verse 1 - Building]      — 빌드업 결
[Verse 2 - Reflective]    — 회상 결
[Chorus - Anthemic]       — 송가 결
[Chorus - Stripped]       — 미니멀 결
[Bridge - Climax]         — 정점
[Bridge - Contrast]       — 대비
[Final Chorus - Belted]   — 폭발 결
[Final Chorus - Doubled]  — 더블 보컬
```


## §UE-32. Voice Style Metatags 풀바디 (19종)

### §UE-32.1 보컬 딜리버리 태그 (HookGenius)

```
[Whispered]       — 속삭임 (조용한 자리만)
[Hushed]          — 낮춘 톤
[Spoken]          — 말하듯이
[Conversational]  — 대화 톤
[Belted]          — 강하게 부름 (Chorus 자리)
[Powerful]        — 강력한
[Soft]            — 부드럽게
[Gentle]          — 온화한
[Breathy]         — 숨 섞인
[Raspy]           — 거친 결
[Smooth]          — 매끈한
[Bright]          — 밝은 결
[Dark]            — 어두운 결
[Yelping]         — 짧게 외침
[Growling]        — 으르렁
[Falsetto]        — 가성
[Head Voice]      — 두성
[Chest Voice]     — 흉성
[Mixed Voice]     — 믹스 보이스
```

### §UE-32.2 보컬 테크닉 태그

```
[Vibrato-heavy]   — 비브라토 강
[Monotone]        — 평탄한 결
[Melismatic]      — 멜리스마틱 (한 음절 여러 음)
[Syncopated]      — 싱코페이션
[Operatic]        — 오페라
[Chanting]        — 차임
[Spoken-word]     — 시 낭독
[Rapping]         — 랩
[Scatting]        — 스캣
[Humming]         — 허밍
[Falsetto runs]   — 가성 런
[Yodeling]        — 요들
```

### §UE-32.3 보컬 감정 태그

```
[Emotional]       — 감정적
[Tender]          — 부드러운
[Aching]          — 아련한
[Longing]         — 그리움
[Defiant]         — 도전적
[Triumphant]      — 승리
[Vulnerable]      — 취약한
[Confident]       — 자신감
[Intimate]        — 친밀한
[Detached]        — 무심한
[Pleading]        — 호소하는
```


## §UE-33. Dynamic / Performance Metatags

### §UE-33.1 다이내믹 태그

```
[Building]        — 빌드업
[Climax]          — 정점
[Drop]            — 드롭
[Breakdown]       — 브레이크다운
[Buildup]         — 빌드업
[Crescendo]       — 점점 강하게
[Decrescendo]     — 점점 약하게
[Sudden Stop]     — 갑작스러운 멈춤
[Slow Burn]       — 천천히 타오름
[Release]         — 풀어짐
```

### §UE-33.2 Pause / Silence 태그

```
[Pause]           — 짧은 멈춤
[Pause half bar]  — 0.5바 멈춤
[Pause 1 bar]     — 1바 멈춤
[Sudden Absolute Silence: 1 bar]   — 완전 정적 1바
[Sudden Absolute Silence: 0.5s]    — 0.5초 정적
[Held note]       — 길게 끄는 음
[Breath]          — 호흡
```

### §UE-33.3 레이어링 태그

```
[Doubled]         — 더블 보컬
[Tripled]         — 트리플 보컬
[Stacked vocals]  — 쌓인 보컬
[Harmony +3rd]    — 3도 화음
[Harmony +5th]    — 5도 화음
[Harmony +octave] — 옥타브 위
[Group chant]     — 그룹 차임
[Background vocals] — 백 보컬
[Adlibs]          — 애드립
```


## §UE-34. Sound Effects Metatags (C-68)

```
원칙 (외부 정설):
- Sound effect는 *mid-line* 박는 게 best
- Standalone line으로 박지 마
- 대괄호 안 박음

[laughter]        — 자연 웃음
[screaming]       — 보컬 스크림
[whisper]         — 속삭임
[echo]            — 에코/리버브
[crowd]           — 군중 소음
[applause]        — 박수
[footsteps]       — 발걸음
[door slam]       — 문 닫는 소리
[phone ring]      — 전화벨
[siren]           — 사이렌

Atmospheric (Lyrics + Style Box 양쪽 박음):
- rain / wind / fire / ocean / thunder
- 반복 = AI 인식 강화
```


## §UE-35. Stretching / Phonetic Metatags

### §UE-35.1 Vowel Stretching (외부 정설)

```
어법: 모음 반복으로 sustain 자리 명시

✅ Sustained notes:
- "Loooove" — 모음 늘림
- "Ohhhh" — 감탄 늘림
- "Yeeeah" — 감정 늘림
- "lo-ove" — 하이픈으로 늘림
- "sooo-long" — 강조 늘림

✅ ALL CAPS 외침:
- "NEVER AGAIN"
- "I LOVE YOU"
- (chorus / climax 자리)
```

### §UE-35.2 Phonetic Respelling

```
어법: 발음 직접 표기

영어 단어 발음 락:
- "read" → 어떻게? past tense [red] vs present [reed]
- 처방: "read" → "reed" 또는 "red" 명시

K-pop hook 영어 자리:
- "love" → "luv" (간단)
- "honestly" → "honest-ly" (음절 명시)
```

### §UE-35.3 Stuttering

```
어법: 반복 자음으로 stutter 표현

예시:
- "B-b-baby" — 떨림
- "lo-o-ove" — 더듬
- "I-I-I" — 망설임

자리: Bridge 감정 정점 / Intimate verse 자리
```


## §UE-36. K-pop / Multilingual Metatags

### §UE-36.1 K-pop 직격 태그

```
[Mixed group vocals]  — K-pop multi-member 시뮬
[Layered harmonies]   — 화음 쌓기
[Gang vocals]         — 그룹 차임
[Member A] / [Member B] — 멤버 구분 (가능 시)
[All]                 — 전체 한꺼번에
[Group chant]         — 차임
```

### §UE-36.2 Multilingual Track Isolation (C-67)

```
[Verse - Korean]      — 한국어 섹션
[Chorus - English]    — 영어 섹션
[Bridge - Spanish]    — 스페인어 섹션

원칙:
- 섹션 안 언어 혼용 금지 (발음 무너짐)
- 한 섹션 = 한 언어
- 비영어 섹션 → all lyrics in [language], no English 박음
```


## §UE-37. Suno V5 / V5.5 신규 기능 (외부 정설)

### §UE-37.1 Voice Cloning (Pro/Premier)

```
- 15초-4분 acapella 또는 직접 녹음 업로드
- Voice + Persona = redundant (하나만 픽)
- Style Box에서 gender/register descriptor 제거
  (Voice가 그 정보 caury)
- 4 credits per creation (beta)
- 18+ age-gated
```

### §UE-37.2 Personas (Pro/Premier)

```
- 생성된 곡의 vocal/style/vibe "essence" 저장
- 시리즈/앨범 consistency에 최적
- 200 free songs per billing cycle
- 그 후 10 credits per song
- December 2025 update: Personas more dominant in mix
  (Style 충돌 시 Persona 이김)

운영자 카탈로그 (24+ 한국 곡) → Persona 24개 만들기 가능
```

### §UE-37.3 Custom Models (Pro/Premier)

```
- 최소 6 original tracks 업로드
- Suno fine-tunes V5.5 on 운영자 catalog
- Build time 2-5분
- Up to 3 models per account
- Style Box에서 generic production language 제거
  (glossy / modern pop production / polished mix)
```

### §UE-37.4 Studio (Stem Separation)

```
- 곡을 12개 stem으로 분리:
  Vocals / Drums / Bass / Guitar / Keys / Synths /
  Strings / Brass / Woodwinds / Percussion / Effects / Other
- DAW로 옮겨 mix / EQ / replace 가능
- Section Replace / Extend / Remake 어법 활용
```


## §UE-38. 글자수 정밀 강제 (Suno 입력 자리)

### §UE-38.1 Suno 한도

```
- Style Box: 1,000자 hard (Suno 공식)
- Lyrics Box: 5,000자 hard (Suno V5.5)
- EXCLUDE: 200자 권장 (절대 X)

운영 권장:
- Style Box: Tight Mode 250-350 / Dense Mode 700-950
- Lyrics: C-3.1 매트릭스 (3,000-3,800 default)
- EXCLUDE: 5-7개 / 200-300자

V5 prompt fatigue 경고:
- 8+ tags → 약화
- Sweet spot: 4-7 descriptors
```

### §UE-38.2 자동 측정 의무 (C-79)

```
시스템 자동 (모든 곡 출력 직전):
1. Style Box wc -c → Tight/Dense 적정?
2. Lyrics wc -c → C-3.1 매트릭스 ±5%?
3. EXCLUDE 개수 → 3-4개 default?
4. 결과 표기:
   📏 Style: 850자 (Dense) ✅
   📏 Lyrics: 3,247자 (3:00-3:30 default 범위) ✅
   📏 EXCLUDE: 4개 / 195자 ✅
```


## §UE-39. v2.0 USER EXTENSION 통합 운영

```
원칙:
- §UE-1 ~ §UE-29 (v2.0 기존 metatag 자료)
- §UE-30 ~ §UE-39 (v2.0 FINAL Polish — HookGenius / V5.5 외부 정설)
- 본문 §1-17 (v1.8 정합 유지)

호출:
- 운영자 "Suno 가사 큐" / "metatag" 발화 → 본 파일 view
- 가사 출력 시 자동 metatag 활용
- 정밀 측정 자동 (C-79 연동)
```


# === END 10 USER EXTENSION v2.0 FINAL Polish ===
# ============================================================
# § USER EXTENSION v2.1 PATCH (2026-05-27)
# 10_SUNO_LYRICS_TAGS.md 끝에 *추가* 자리 — 기존 §UE-1~39 유지
# 혼성/듀엣 라벨 강제 어법 + Mid-song [Singing:] 큐 표준 +
# 한국 밈/일상어 web_search 프로세스 + 곡 구조 마이크로 패턴 큐
#
# § Integrity Patch (v2.1.1, 2026-05-27):
# 원본 v2.1 패치가 §UE-33~38 박았으나 *v2.0 §UE-33~38 자리와 중복*.
# 재배정: §UE-33~38 → §UE-40~45.
# ============================================================


## §UE-40. 혼성 / 듀엣 / 그룹 라벨 강제 어법 (C-90/C-91 직격)

운영자 신고 직격:
> *"혼성하랬더니 여자만 나왔거든. 가사큐에만 위쪽에 박아놨더라고."*

### §UE-40.1 작동 검증된 라벨 어법

**섹션 시작 큐:**
```
✅ [Verse 1 8 - V1 (Male) leads]
✅ [Verse 2 8 - V2 (Female) leads]
✅ [Chorus 8 - V1+V2 with V1 leading hook]
✅ [Bridge 8 - V2 (Female) solo]
✅ [Final Chorus 8 - V1+V2 unison]
```

**라인 라벨:**
```
✅ [V1] line by vocal 1
✅ [V2] line by vocal 2
✅ [V1+V2] both together
✅ [All] / [Group] 그룹 chant
✅ [Male] / [Female] / [Male+Female] gender label
```

**금지 라벨:**
```
❌ vocal 1: line (prefix 어법 인식 약함)
❌ V1: line (prefix)
❌ Serica: line (캐릭터 이름 prefix)
❌ [Serica] line (Vocal 1 anchor 없이 단독)
```

### §UE-40.2 강제력 풀바디 예시

**예시 1 — Male verse / Female chorus 듀엣:**

```
[Vocal 1 (Tatoo): male baritone A2-E4, low monotone sexy
 trip-hop delivery, dry close-mic with subtle tape saturation]
[Vocal 2 (Sis Tattoo): female soprano D4-F#5, bright clean
 sassy modern pop diction with crisp consonants, contemporary
 club pop inflection]

[Instrumental Intro: 4 bars]
[Synth arpeggiator + drum machine]

[Verse 1 8 - V1 (Tatoo) leads]
[Singing (V1): low monotone trip-hop conversational]
[V1] First line by male trip-hop vocal
[V1] Second line continuing male verse
[V1] Third line
[V1] Fourth line

[Pre-Chorus 4 - V2 entering]
[Singing (V2): bright sassy modern pop, building from intimate
 to forward]
[V2] First pre-chorus line by female
[V2] Second pre-chorus line

[Chorus 8 - V1+V2 with V2 (Sis Tattoo) leading hook]
[Singing: V2 forward sassy hook delivery, V1 low backing texture]
[V2] Female hook line one
[V2] Female hook line two
[V1+V2] Unison line three
[V2] Female hook line four

[Verse 2 8 - V1 (Tatoo) leads]
[Singing (V1): low monotone trip-hop conversational]
[V1] First line of verse 2
[V1] Second line
[V1] Third line
[V1] Fourth line

[Bridge 8 - V2 (Sis Tattoo) solo]
[Singing (V2): stripped down close-mic intimate, building to
 controlled belt]
[V2] Bridge line one solo
[V2] Bridge line two
[V2] Bridge line three building
[V2] Bridge line four climax

[Final Chorus 8 - V1+V2 with V2 hook lead]
[V1+V2] All unison opening line
[V2] Female hook line two
[V1+V2] Unison line three
[V2] Female hook line four
[V1+V2] Final unison line

[Outro 4]
[Instrumental fade]
```

**예시 2 — 동등 듀엣 (남녀 trading lines):**

```
[Vocal 1 (Welling): male tenor C3-A4, standard pop-rock]
[Vocal 2 (Tarahan): female soprano C4-E5, sweet K-indie]

[Verse 1 8 - alternating V1/V2 trading lines]
[V1] First line by male
[V2] Second line by female responding
[V1] Third line by male
[V2] Fourth line by female
[V1] Fifth line
[V2] Sixth line
[V1+V2] Seventh line together
[V1+V2] Eighth line together

[Chorus 8 - V1+V2 unison]
[V1+V2] All unison chorus throughout
```

### §UE-40.3 그룹 보컬 라벨 어법

```
[Vocal: K-pop multi-member group — Member 1 (Lead) soprano,
 Member 2 (Sub) mezzo airy, Member 3 (Rapper) speech-tone,
 Member 4 (Sub2) mezzo powerful belt]

[Verse 1 8 - Member 1 leads]
[Singing (Member 1): clean clear K-pop mix voice]
[M1] First line by Member 1
[M1] Second line
[M2] (Member 2 responds) Third line — airy breathy
[M1] Fourth line
[M2] Fifth line
[M1+M2] Sixth line together
[M1] Seventh line
[M1] Eighth line

[Pre-Chorus 4 - Member 4 leads]
[Singing (Member 4): powerful belt building]
[M4] Pre-chorus line one
[M4] Pre-chorus line two
[All] Pre-chorus line three group
[All] Pre-chorus line four group

[Chorus 8 - All members with M1 leading hook]
[All] Unison chorus opening
[M1] Lead hook line
[All] Group response
[M1] Lead hook line two
[All] Group response

[Rap Verse 8 - Member 3]
[Singing (Member 3): speech-tone cutting precision rap]
[M3] Rap line one
[M3] Rap line two
[M3] Rap line three
[M3] Rap line four
[M3] Rap line five
[M3] Rap line six
[M3] Rap line seven
[M3] Rap line eight

[Bridge 8 - Member 1 and Member 4 duet]
[Singing (M1+M4): trading lines between lead vocalists]
[M1] Bridge line one (clean)
[M4] Bridge line two (powerful)
[M1] Bridge line three
[M4] Bridge line four building
[M1+M4] Bridge line five together
[M1+M4] Bridge line six together
[All] Bridge line seven (group joining)
[All] Bridge line eight climax

[Final Chorus 8 - All with key change up]
[Singing: maximum belt with all members, key change up]
[All] Final chorus throughout
```


## §UE-41. Mid-Song [Singing:] 큐 표준 (창법 전환)

기존 §2.1이 *Tier A delivery style 풀*. §UE-41는 *섹션 안 전환 자리 표준*.

### §UE-41.1 섹션 시작 큐 (Section Start)

```
모든 섹션은 [섹션 태그] 직후 [Singing:] 큐 박음:

[Verse 1 8]
[Singing: hushed conversational close-mic]
가사 첫 줄
...

[Chorus 8]
[Singing: anthemic chest belt with controlled vibrato]
가사 첫 줄
...
```

### §UE-41.2 라인 전환 큐 (Mid-Section Transition)

12바+ 섹션 / 결 변환 자리:

```
[Verse 1 16]
[Singing: hushed conversational]
첫 줄
둘째 줄
셋째 줄
넷째 줄

[Singing: shifting to declarative half-spoken]
다섯째 줄 (큐 직후 라인이 결 변환)
여섯째 줄

[Singing: building to belt]
일곱째 줄
여덟째 줄
```

**룰:**
- 4-라인 이상 같은 결 → 결 단조 위험
- 12바+ 섹션 *최소 2개* 큐
- 짧은 섹션 (4-8바) *1개* 충분

### §UE-41.3 감정 정점 큐 (Climax Cue)

```
[Bridge 8]
[Singing: vulnerable stripped down close-mic intimate]
모든 게 변했지만
[Singing: emotional cry break with controlled rasp]
너만은 그대로 있어줘
```

```
[Final Chorus 8]
[Singing: explosive belt with stacked +3rd +5th harmonies and
 melismatic ad-libs]
지나갈 줄 알았는데 (yeah)
너는 그대로야 (forever)
```

### §UE-41.4 호흡 / 정지 / 텀 힌트 (C-93 통합)

```
[Pause half bar]              — 반 마디 호흡
[Pause 1 bar]                 — 한 마디 호흡
[Pause 2 bars]                — 두 마디 호흡
[Breath]                      — 자연 호흡
[Held note]                   — sustained
[Held 2 bars]                 — 2마디 held

[Mute 1 bar]                  — 1마디 mute
[Sudden Silence 1 bar]        — 갑작스러운 정적
[Sudden Absolute Silence: 1 bar] — 완전 정적
[Instrumental Break 4 bars]   — 4마디 인스트루멘탈
```

**자동 텀 힌트 (130+ BPM + 8 음절/바 초과 시):**

```
[Chorus 16]
[Singing: anthemic chest belt with controlled vibrato]
지나갈 줄 알았는데 너는 그대로야
[Breath]
하루가 또 길어지고 새벽은 또 깊어지고
[Pause half bar]
이제는 정말 못 견디겠어
[Held note]
가-지 마-아
[Pause 1 bar]
한 번만 더
```


## §UE-42. Instrumental Section 표준 (C-92 통합)

운영자 신고:
> *"인트로 아웃트로에서 어줍잖은 독백 넣어서 빡치게 만들더니, 이제는
>  아예 없애는 경우도 많은데 필요에 따라서는 instrumental 이런 거로
>  지정한다든가 간주라든가."*

### §UE-42.1 Intro 어법

```
검증 옵션:

옵션 A — Short Instrumental Intro 명시:
[Short Instrumental Intro: 2 bars]
[Acoustic guitar alone]

옵션 B — 풀바디 Instrumental Intro:
[Instrumental Intro: 4 bars]
[Acoustic guitar finger-picking with sparse atmospheric pad]

옵션 C — Verse 직접 시작:
[Verse 1 8]
[Singing: hushed conversational]
첫 줄

옵션 D — Spoken Intro (의도적 자리):
[Intro - Spoken: 2 bars]
[Single spoken phrase preceding band entry]
"...첫 번째 단어..."
```

### §UE-42.2 Outro 어법

```
옵션 A — Instrumental Fade:
[Instrumental Outro: 8 bars]
[Vocal fades, instruments sustain with fade]

옵션 B — Vamp Outro:
[Outro - Instrumental Fade: 8 bars]
[Acoustic guitar vamp with chord progression repeating]

옵션 C — Sustained Note:
[Outro: 4 bars]
[Held sustained vocal note with band decay]

옵션 D — Abrupt Cut:
[Outro: 1 bar]
[Sudden end on downbeat]
```

### §UE-42.3 Mid-Song Instrumental Break (간주)

```
옵션 A — 짧은 간주:
[Instrumental Break: 4 bars]
[Saxophone solo over chord progression]

옵션 B — 풀바디 간주:
[Instrumental Break: 8 bars between Verse 2 and Final Chorus]
[Guitar solo with band continuing]

옵션 C — Dance Break (K-pop):
[Dance Break: 8 bars]
[Instrumental with drums + bass + lead synth, no vocals]

옵션 D — Bridge Solo:
[Bridge - Instrumental Solo: 4 bars]
[Lead synth or guitar solo replacing vocal bridge]
```

### §UE-42.4 V5 Intro Control (C-61 통합)

V5는 *intro 자동 확장* 경향 → 어줍잖은 독백 위험

**해결:**
1. `[Short Instrumental Intro: 2 bars]` 명시
2. `[Verse 1 8]` 직접 시작
3. `[Intro - Spoken: 2 bars]` 의도적 자리만


## §UE-43. 한국 밈 / 일상어 web_search 프로세스 (C-96)

운영자 핵심 통찰:
> *"의외로 웹서핑해서 일상적인 용어 밈들을 활용해서 운율을 맞춰 넣는다든가
>  그 의미를 네가 짓는 게 아니라 웹서핑으로 현재 분위기 사용 그런 것들
>  메타 분석도 필요해."*

### §UE-43.1 web_search 발의 자리

**시스템 자동 (가사 작업 진입 시):**

```
1. 컨셉 분석
2. 한국어 가사 작업이면 → web_search 발의:
   "한국어 가사 자리에 현재 살아있는 일상어 / 밈 추가할까?"

3. 운영자 명시 발화 시 즉시 발동:
   "요즘 어법으로" / "요즘 말로" / "지금 한국 정서로" /
   "MZ 세대 결로" / "Z세대 결로"

4. 검색 어법:
   web_search ["2026 한국 신조어", "[해당 정서] 한국 일상어",
              "MZ세대 [감정] 표현 2025-2026", "한국 밈 [컨셉]"]

5. 결과 → 가사 자리 후보:
   - Hook 자리 (강조)
   - Pre-Chorus 자리 (즉각 공감)
   - Verse 디테일 자리 (일상감)
```

### §UE-43.2 검증된 2025-2026 한국 일상어 풀 (참조용)

**MZ세대 / Z세대 어법:**
```
- 알잘딱깔쎈 (알아서 잘 딱 깔끔하고 센스있게)
- 중꺽마 (중요한 건 꺾이지 않는 마음)
- 이왜진 (이게 왜 진짜)
- 홀리몰리 (놀람)
- 힘숨찐 (힘 숨긴 찐따 — 숨겨진 능력자)
- 감다살 (감사가 다 살았다)
- GMG (가면 가)
- 밥플릭스 (밥 + 넷플릭스)
- 슬세권 (슬리퍼 신을 정도로 가까운 주거)
- 섹시푸드 (비주얼 + 맛 좋은 음식)
- 미코노미 (나를 위한 소비)
- 미닝아웃 (신념 소비)
- 테토남/녀 (테스토스테론 성향)
- 에겐남/녀 (에스트로겐 성향)
- 전업자녀 (부모 의존 자녀)
```

**일상어 / 감정 표현:**
```
- 갓생 (good 인생)
- 영끌 (영혼 끌어 모으다)
- 빚투 (빚내서 투자)
- 갭모이 (간극이 모이다)
- 정중동/동중정 (정지 + 움직임)
- 찐 / 찐친 (진짜 / 진짜 친구)
- 핵 / 핵존맛 (강조)
- 인생곡 / 인생영화 (인생 최고)
- 떡밥 (호기심 자극)
```

### §UE-43.3 밈 / 일상어 가사 활용 어법

**원칙:**
- 의미 시스템이 짓지 마 / *현재 살아있는 어법* 활용
- 밈 그대로 박지 마 / *결만 가져옴*
- 한국어 자연 어법 유지

**예시 — "외로움" 컨셉:**

```
❌ 시스템 임의: "혼자라는 게 외로워"

✅ 일상어 활용:
"새벽 두 시 밥플릭스 / 또 혼자"
"슬세권 한 바퀴 / 너 없는 자리"
"오늘도 갓생 실패 / 영혼 끌어 너 생각"
```

**예시 — "결단 / 자신감" 컨셉:**

```
❌ 시스템 임의: "이제 강해질 거야"

✅ 일상어 활용:
"중꺽마 / 이번엔 진짜로"
"알잘딱깔쎈 / 내 결대로"
"미닝아웃 / 너 없이도"
```

### §UE-43.4 자동 점검 (C-96)

**시스템 자동 (가사 작성 시):**

```
1. 컨셉 분석 → 한국 일상어 적합 자리?
2. web_search → 현재 살아있는 어법 후보
3. 후보 중 *컨셉 정합* 어법 추출
4. 가사 자리에 활용 (Hook / Pre / Verse 디테일)
5. 표기:
   "🔍 한국 일상어 활용: [어법 N개] (web_search 2026 결)"
```

**자동 발동 회피:**
- 운영자 "전통적인 가사로" / "시적인 가사로" 명시 시
- 영문 가사 메인일 때
- 컨셉이 *고전적 / 클래식 / 문학적* 일 때


## §UE-44. 곡 구조 마이크로 패턴 가사큐 (04 §UE-5 통합)

04 §UE-5 곡 구조 풀바디를 가사 자리에서 어떻게 박는지:

### §UE-44.1 Hook-Loop 어법 (04 §UE-5.1)

```
[Vocal: Male tenor with melodic-rap flow]

[Intro 4 - Hook variation]
[Singing: behind-the-beat conversational]
Hook 변형 line 1
Hook 변형 line 2

[Verse 1 16]
[Singing: storytelling melodic rap]
16 bars verse with internal rhyme density

[Hook 8 - Main hook]
[Singing: catchy melodic delivery]
Main hook line 1
Main hook line 2
(repeat with variation)

[Verse 2 16]
...

[Hook 8 - Main hook with ad-libs]
...

[Outro - Hook fade]
[Hook variation fading]
```

### §UE-44.2 Bridge-as-Climax 어법 (04 §UE-5.2)

```
[Bridge 16]
[Singing: stripped down then building to maximum belt with
 controlled vibrato and rasp on peaks]
Bridge new perspective line 1
Bridge new perspective line 2
[Held note]
Bridge climax line 3
[Pause half bar]
Bridge climax line 4 with key change up

[Final Chorus 8 - echo, not climax]
[Singing: anthemic but slightly softer than bridge]
Same chorus lyrics
```

### §UE-44.3 Post-Chorus 어법 (04 §UE-5.4)

```
[Chorus 8]
[Singing: main hook with belt]
Chorus lines

[Post-Chorus 4]
[Singing: vocable repetition with hook word]
(oh-oh-oh) (yeah yeah)
Hook word ah ah ah
(oh-oh-oh)
Hook word ah ah ah
```

### §UE-44.4 Anti-Drop 어법 (04 §UE-5.6)

```
[Build-up 8]
[Singing: ascending intensity with rising synths]
Build line 1
[Pause half bar]
Build line 2 building
[Held note]
Final tension build

[Anti-Drop 8]
[Sudden Absolute Silence: 1 bar]
[Singing: hushed whisper]
(whisper:) ...silence...
[Singing: building back from whisper]
Subtle line returning

[Drop 16]
[Singing: full energy return]
Full drop with maximum energy
```

### §UE-44.5 Pre-Intro 어법 (04 §UE-5.7)

```
[Pre-Intro: 2 bars at 0:00]
[Singing: instant hook teaser]
Quick hook word with reverb tail
[Sudden Silence half bar]

[Intro 8]
[Instrumental band entry building]

[Verse 1 8]
[Singing: storytelling]
Verse begins
```


## §UE-45. 다언어 가사 어법 (C-67 통합)

기존 §2.5에서 일부 다룸. §UE-45은 풀바디.

### §UE-45.1 섹션 격리 (default)

```
[Verse 1 - Korean]
[Singing: intimate Korean diction]
한국어 가사 line 1
한국어 가사 line 2

[Pre-Chorus - English]
[Singing: building English delivery]
English pre-chorus line 1
English pre-chorus line 2

[Chorus - English]
[Singing: anthemic English belt]
English chorus throughout

[Verse 2 - Korean]
[Singing: intimate Korean diction]
한국어 가사 line 1
한국어 가사 line 2

[Bridge - Mixed]
[Singing: code-switching mid-line, transition from Korean
 verse to English chorus mood]
Korean line transitioning
English line continuing
```

### §UE-45.2 Hook 자리 Single Foreign Word

```
[Chorus]
[Singing: Korean chorus with English hook word]
지나갈 줄 알았는데 (forever)
너는 그대로야 (always)
시간이 지나도 (forever)
변하지 않는 너 (always)
```

### §UE-45.3 위험 자리 회피

```
❌ 라인 안 혼용:
[Verse]
사랑해 baby 너만이 my one love

❌ 매 라인 언어 전환:
[Verse]
Line 1 in Korean
Line 2 in English
Line 3 in Korean
Line 4 in English
(pronunciation drift 위험)

✅ 안전 어법:
- 섹션 단위 언어 격리
- Hook 자리 single word
- Bridge 자리 완전 전환
```


# === END 10 USER EXTENSION v2.1 PATCH ===

# ============================================================
# § USER EXTENSION v2.2 PATCH (2026-05-28)
# Lyric Cue Precision — 옆동네 프로 어법 정합
# C-99 ~ C-103 시스템 룰 풀바디 자산
# ============================================================


## §UE-46. [Singing:] 7-요소 매트릭스 풀바디

### §UE-46.1 7-요소 정의 + 어법 풀

**1. Voice Type / Placement** (음역 + 발성 자리)

```
음역 (06 §2 베이스):
- soprano / mezzo-soprano / alto / tenor / baritone / bass
- light soprano / dramatic alto / lyric tenor / heroic baritone

발성 자리:
- chest voice forward (흉성, 무게감)
- head voice forward (두성, 가벼움)
- mixed voice (흉두성 mix)
- chest dominant mix (흉성 위주, R&B 자리)
- floating head voice (두성 floating)
- forward placement (마스크 앞, 밝음)
- back placement (인후 뒤, 어두움)
- belted from diaphragm (횡경막 belt)

조합 예:
"full classical tenor with chest voice forward"
"light alto, mixed voice with chest dominance"
"floating head voice soprano, forward placement"
```

**2. Dynamic** (음량 / 강도)

```
정적 다이내믹 (절대값):
- pianissimo (pp) — 매우 약하게
- piano (p) — 약하게
- mezzo-piano (mp) — 약간 약하게
- mezzo-forte (mf) — 약간 강하게
- forte (f) — 강하게
- fortissimo (ff) — 매우 강하게

변화 다이내믹:
- crescendo into [자리] — 점점 강하게
- decrescendo into [자리] — 점점 약하게
- subito forte — 갑자기 강하게
- subito piano — 갑자기 약하게
- swell on [단어/노트] — 부풀리기
- pull back on [단어/노트] — 약화

조합 예:
"mezzo-piano in verse, crescendo into chorus, forte on hook"
"pianissimo opening, subito forte on the word *fire*"
```

**3. Mic Distance** (마이크 거리 = 공간감)

→ §UE-47 풀바디 참조

**4. Phrasing** (구절 흐름 / 결)

```
시간 처리:
- legato (이어지게)
- staccato (끊어서)
- slight rubato on phrase-ends (구절 끝 자유 시간)
- accelerando (점점 빠르게)
- ritardando (점점 느리게)
- in tempo strict (정확한 박자)
- behind the beat (박자 뒤로)
- ahead of the beat (박자 앞으로)

호흡 처리:
- breath between phrases (구절 사이 호흡)
- breath audible (호흡 들리게)
- breath silent (호흡 안 들리게)
- sustained vowels (모음 sustain)
- clipped consonants (자음 짧게)

조합 예:
"warm legato phrasing, slight rubato on phrase-ends"
"staccato attack on verse, legato sustain on chorus"
"behind-the-beat conversational phrasing"
```

**5. Expression** (표현 디테일)

```
비브라토:
- no vibrato (없음)
- subtle vibrato on sustained notes (subtle)
- expressive vibrato blooming on sustained vowels (풍부)
- wide vibrato (넓음)
- fast vibrato (빠름)
- slow vibrato (느림)
- vibrato entering on final syllable (마지막 음절에만)
- vibrato widening through phrase (점점 넓게)

호흡 / 텍스처:
- breath audible between phrases
- slight cry on belt notes (belt 자리 cry 결)
- raspy edge on belted notes (raspy edge)
- airy tail on phrase-ends (끝 airy)
- glottal stop attack (성문 attack)
- subtle vocal fry on lower register (낮은 영역 fry)

조합 예:
"expressive vibrato blooming on sustained vowels, breath audible between phrases"
"no vibrato on opening, vibrato entering on final syllable"
"raspy edge on belted notes, airy tail on phrase-ends"
```

**6. Mood** (감정 결)

```
긍정:
- tender / warm / nostalgic / triumphant / confident /
  blissful / playful / sassy / cheeky / defiant

부정:
- aching / longing / vulnerable / detached / bitter /
  resigned / haunted / melancholic / restless

복합:
- tender nostalgic mood (애틋한 회상)
- sassy bratty edge (sassy + bratty)
- vulnerable yet determined (취약하지만 결연)
- detached cool with subtle bitterness (무심한 cool + 약간 쓴맛)
- triumphant with raw edge (승리 + raw)
```

**7. Backing Arrangement Cue** (백킹 변화)

→ §UE-48 풀바디 참조

### §UE-46.2 섹션별 7-요소 풀바디 박힘 예

```
[Intro]
[Singing: hushed alto, pianissimo, close mic intimate, breath-on-capsule]

[Verse 1]
[Singing: warm chest voice, mezzo-piano, close mic intimate,
conversational phrasing with slight behind-the-beat feel,
breath audible between phrases, tender nostalgic mood]

[Pre-Chorus]
[Singing: lifting to mixed voice, crescendo to mezzo-forte,
moving to mid-distance mic, urgency entering phrasing,
vibrato widening through phrase, anticipation building]

[Chorus]
[Singing: full belt to F#5, forte, mid-back mic for room presence,
sustained vowels with wide vibrato blooming, triumphant defiant mood,
strings swell underneath +6dB, gang vocal handclap layered]

[Verse 2]
[Singing: pulled back to chest voice, mezzo-piano, close mic,
conversational with slight bitter edge, breath audible,
detached cool mood with subtle restlessness]

[Bridge]
[Singing: stripped to head voice pianissimo, close mic intimate,
no vibrato on opening, vibrato entering on final syllable,
vulnerable yet determined, band drops out leaving only nylon guitar and piano]

[Final Chorus]
[Singing: belt at peak, fortissimo, mid-back mic + hall ambience,
wide vibrato blooming, ritardando into final cadence,
triumphant with raw edge, full band crescendo with horn countermelody +6dB]

[Outro]
[Singing: voice trails off, decrescendo to piano, close mic,
breath release tail, nostalgic resigned mood]
```

### §UE-46.3 7-요소 압축 어법 (한 큐 120자 이내)

```
풀바디 (180자):
[Singing: full classical tenor with chest voice forward, mezzo-forte,
mid-distance mic, warm legato phrasing with slight rubato on phrase-ends,
expressive vibrato blooming on sustained vowels, tender nostalgic mood,
piano arpeggio carrying chords underneath]

압축 (110자):
[Singing: chest tenor, mf, mid-mic, warm legato, vibrato blooming,
nostalgic, piano arpeggio under]

압축 룰:
- Voice type: full classical tenor → chest tenor
- Dynamic: mezzo-forte → mf
- Mic: mid-distance mic → mid-mic
- Phrasing: warm legato phrasing → warm legato
- Expression: expressive vibrato blooming on sustained vowels → vibrato blooming
- Mood: tender nostalgic mood → nostalgic
- Backing: piano arpeggio carrying chords underneath → piano arpeggio under
```


## §UE-47. Mic Distance / Vocal Placement 풀바디

### §UE-47.1 Mic Distance 5단계 풀

```
Lavalier / Inside (~ 0-3cm):
- "inside-mic, breath-on-capsule"
- "lavalier proximity, ASMR detail"
- "tongue and lip detail forward"
효과: 극도 친밀, ASMR 결
자리: Whispered intro / 속삭임 자리

Close mic (~ 5-10cm):
- "close mic intimate"
- "close mic, breath audible"
- "close mic with lip detail"
- "close mic, proximity effect"
효과: 친밀, 디테일
자리: Verse / Bridge / 인티밋

Mid mic (~ 20-50cm):
- "mid-distance mic, balanced presence"
- "mid mic with slight air"
- "studio standard mic distance"
효과: 표준, 균형
자리: 일반 Verse / Pre-Chorus

Mid-back mic (~ 80cm-1.5m):
- "mid-back mic for room presence"
- "mid-back mic with slight air, room reflection"
- "back mic for natural ambience"
효과: 공간감, 풍성함
자리: Chorus / 풍성

Hall / Far (~ 3m+):
- "hall mic for natural reverb"
- "distant theatrical mic"
- "concert hall mic, full reverb tail"
효과: 콘서트홀, 극장
자리: Outro / 시네마틱
```

### §UE-47.2 Vocal Placement 풀바디

```
Chest forward — 흉성, 무게감
  자리: Verse / 발라드 / R&B verse
  
Head forward — 두성, 가벼움
  자리: Pre-Chorus build / 가벼운 자리

Mixed voice — 흉두성 mix
  자리: K-pop belt / Chorus / 정점 자리

Chest dominant mix — 흉성 위주 mix
  자리: 모던 R&B / Soul

Floating head voice — 두성 floating
  자리: Bridge stripped / 인티밋 자리

Forward placement — 마스크 앞, 밝음
  자리: 밝은 곡 / Pop / 청량

Back placement — 인후 뒤, 어두움
  자리: 어두운 곡 / Indie / Alt R&B

Belted from diaphragm — 횡경막 belt
  자리: 정점 belt / Power ballad
```

### §UE-47.3 섹션별 Mic + Placement 매핑

```
[Intro hushed] → close mic + chest piano
[Verse intimate] → close mic + chest forward + conversational
[Verse driving] → mid mic + chest forward + propulsive
[Pre-Chorus build] → mid mic + lifting to mixed voice
[Chorus belt] → mid-back mic + mixed voice belt + room air
[Chorus floating] → mid mic + floating head voice + airy
[Bridge stripped] → close mic + head voice pianissimo
[Bridge defiant] → mid mic + chest voice forte
[Final Chorus peak] → mid-back mic + full belt + hall ambience
[Outro fade] → close mic + breath tail
[Outro sustained] → hall mic + held note + reverb tail
```


## §UE-48. Backing Arrangement Cue 풀바디 (진짜 빠진 자산)

### §UE-48.1 악기 In/Out 어법 풀

```
악기 enters:
- "piano enters on bar 5"
- "strings enter on the downbeat"
- "synth lead enters with countermelody"
- "horns enter +6dB on chorus"
- "sub-bass enters on the and of 4"

악기 drops out:
- "accordion drops out leaving only nylon guitar and cello"
- "drums drop out for the verse"
- "bass drops out for 2 bars"
- "band drops out leaving only vocal"
- "all instruments out except piano"

악기 swells:
- "strings swell underneath +6dB"
- "synth pad swells +3dB into chorus"
- "horn section swells through final chorus"
- "full band swell to crescendo"

악기 cuts to:
- "drums cut to half-time"
- "drums cut to double-time on 2nd half"
- "guitars cut to staccato chord stabs"
- "bass cuts to walking pattern"

악기 takes over:
- "synth lead takes over from guitar"
- "strings take over melody on bar 16"
- "accordion takes over harmonization"
```

### §UE-48.2 다이내믹 변화 어법 풀

```
악기 다이내믹:
- "strings swell +6dB"
- "brass stab on the 2-and"
- "sub drop on the downbeat"
- "kick drop on bar 8"
- "snare crack on 2 and 4"
- "horn stab punctuating phrase-ends"

다이내믹 전환:
- "half-time switch with kick prominent"
- "double-time switch on the 2nd half"
- "full band drop to half-time on bridge"
- "sudden cut to acoustic-only"
- "build to full band climax"
```

### §UE-48.3 시간 명시 어법 풀

```
- "on bar [N]"
- "on the [beat number]"
- "on the and of [beat]"
- "into final cadence"
- "between phrases"
- "under the final note"
- "on phrase-ends"
- "into chorus drop"
- "out of bridge into final chorus"
- "through the outro"
```

### §UE-48.4 섹션별 Backing Cue 권장 박힘

```
[Verse]
backing: piano arpeggio carrying chords, bass entering on bar 5

[Pre-Chorus]
backing: drums building tension, strings entering underneath +3dB,
kick drop on bar 8

[Chorus]
backing: full band swell, gang vocal layered, strings sustaining
underneath +6dB, brass stabs on the 2-and

[Bridge]
backing: band drops out leaving only nylon guitar and piano,
breath audible, subtle string pad +1dB

[Final Chorus]
backing: full band crescendo, horns entering with countermelody +6dB,
ritardando into final cadence, full band held note

[Outro]
backing: synth pad fade, plucky synth tail, room reverb +2dB
```

### §UE-48.5 [Singing:] 큐 안 Backing 통합 예

```
풀 통합 예 1 (Verse):
[Singing: warm chest voice, mezzo-piano, close mic, conversational
phrasing, breath audible, piano arpeggio carrying chords underneath,
bass entering on bar 5]

풀 통합 예 2 (Chorus):
[Singing: full belt to F#5, forte, mid-back mic, sustained vowels,
wide vibrato blooming, triumphant, strings swell underneath +6dB,
gang vocal handclap layered, brass stab on the 2-and]

풀 통합 예 3 (Bridge):
[Singing: stripped to head voice pianissimo, close mic, no vibrato
on opening, vibrato entering on final syllable, vulnerable,
band drops out leaving only nylon guitar and piano, breath audible]

풀 통합 예 4 (Final Chorus):
[Singing: belt at peak, fortissimo, mid-back mic + hall ambience,
ritardando into final cadence, triumphant raw edge,
full band crescendo with horn countermelody +6dB, held note tail]
```


## §UE-49. 강세 / 호흡 / 애드리브 / 늘림 어법 풀바디

### §UE-49.1 강세 5단계 풀

```
word — 일반 발음 (모든 자리)
*word* — 펀치인 강세 (보통)
  자리: Verse 2-4개/section
  예: "I *don't* even read the *room*, I just own this *town*"

**word** — 최강 강세
  자리: Hook 핵심 단어 1-2개/Chorus
  예: "Hell-fire **cherry** on a summer high"

Word — 첫글자 capital (subtle 강조)
  자리: 일반 노래 시작 자리

WORD — ALL CAPS (외침 / 큰소리)
  자리: Bridge climax / Hook peak 1자리
  예: "I'm *NOT* waiting for September"
```

### §UE-49.2 자리별 강세 권장량

```
[Intro] — 강세 0-1개 (가벼움)
[Verse 1] — *word* 2-4개 (펀치인)
[Pre-Chorus] — *word* 1-2개 (긴장)
[Chorus] — **word** 1-2개 (Hook) + *word* 1-3개
[Verse 2] — *word* 2-4개 (Verse 1과 다른 단어)
[Pre-Chorus 2] — 변형
[Chorus 2] — Chorus 1과 동일 강세 + 1개 변형
[Bridge] — WORD 1자리 (climax) + *word* 2-3개
[Final Chorus] — **word** 2-3개 (최대치)
[Outro] — 강세 0-1개 (페이드)
```

### §UE-49.3 호흡 / 정지 / 텀 큐 풀

```
[Breath] — 들숨 들리게
  자리: 격렬 라인 사이 / 130+ BPM 자리

[Pause half bar] — 반박자 정지
  자리: 라인 사이 / 강조 직전

[Pause 1 bar] — 1바 정지
  자리: Pre-Chorus 끝 / Hook 진입 직전

[Pause 2 bars] — 2바 정지
  자리: Bridge 끝 / 극적 자리

[Sudden Absolute Silence: 1 bar] — 절대 정지
  자리: (whisper:) 직전만 (C-21 룰)

[Held note] — 마지막 노트 길게
  자리: 라인 끝 강조

[Mute 1 bar] — 1바 백킹 음소거
  자리: 보컬 솔로 자리

박힘 룰:
- 130+ BPM + 8 음절/바 초과 → 자동 [Breath]
- Pre-Chorus 끝 → [Pause half bar] 권장
- Bridge → Final Chorus 사이 → [Pause 1 bar]
- Final Chorus 마지막 줄 → [Held note]
```

### §UE-49.4 애드리브 어법 풀

```
(word) — 백킹 보컬 / 애드리브 (줄 끝 인라인)
(yeah) (oh baby) (uh-huh) — 짧은 애드리브
  자리: Hook 자리
(echo: word) — 에코 효과
  자리: Hook 끝 / Outro
(whisper: word) — 속삭임
  자리: [Sudden Silence] 직후만 (C-21)

박힘 룰:
- 줄 끝 인라인 박음 (`*dance* (yeah)`)
- 독립 줄 X (단독 줄은 발화 안 됨)
- Hook 자리 1-3개 권장 (남발 X)
- Chorus 자리 2-4개 권장

예시:
"I'm a heat wave walking, ninety-eight today (heat wave, heat wave)"
"Hell-fire cherry, melt me, baby (melt me, baby)"
"Cherry on my tongue, sun in my hair (echo: in my hair)"
```

### §UE-49.5 늘림 / 더듬 / 강조 풀

```
lo-o-o-ve — 모음 sustain (가벼움)
Loooove — 더 강한 sustain (Belt)
Ohhhh — 감탄 sustain
B-b-baby — 더듬 (Charli XCX 결)
na-na-na — 반복 hook (Post-Chorus)
la-la-la — 가벼운 반복 (Bridge / Outro)

박힘 룰:
- Hook 끝 자리 1-2회 권장
- Belt 자리 강한 sustain
- 시그니처 자리 의도적 박음
- Post-Chorus / Outro 반복 활용
- 남발 X (3-5회 이상 단조)

예시:
"Hellfire **cherry**, melt meee, baby"
"Never *gonna* let you go-o-o"
"I-I-I won't back down"
```

### §UE-49.6 통합 운영 — Lyrics Box 안 풀바디 예

```
[Verse 1 - UK garage shuffle, sub-bass enters on bar 5]
[Singing: warm chest voice, mezzo-piano, close mic intimate, conversational
phrasing with slight behind-the-beat feel, breath audible between phrases,
sassy detached mood, piano arpeggio carrying chords]

Roof's on *fire*, no it's just *July*
Concrete kissing back, hot enough to fry
Boy on the *corner* thinks he's got a chance
[Breath]
I'm not even looking, baby, watch me *dance* (yeah)

[Chorus - half-time, belt to F#5, full band swell]
[Singing: full belt to F#5, forte, mid-back mic for room presence,
sustained vowels with wide vibrato blooming, triumphant defiant mood,
strings swell underneath +6dB, gang vocal handclap layered, brass stab on the 2-and]

Hell-fire **cherry** on a summer high
I'ma let it *drip*, let it drip dry
[Pause half bar]
Tell the *sky* to move, move outta my way
I'm a *heat wave* walking, ninety-eight today
(heat wave, heat wave)
Hellfire cherry, melt meee, baby [Held note]
```


## §UE-50. 멜로디 컨투어 정식 태그 (C-113 / 04 §UE-8 연동) [v2.4]

**출처/주체**: 컨투어×하모니×연출 본체는 **04 §UE-8**. 본 §은 그 중
*Suno 정식 태그(Layer A)*만 모은 빠른 참조 카드. 04 §UE-8 + C-113과 한 몸.

### §UE-50.1 컨투어 정식 태그 (Lyrics box 섹션 첫 줄)

검증된 Suno 컨투어 태그. 섹션 첫 줄 = 멜로디 가중치 최대 자리.

```
[Ascending melody]    상승 — 텐션·에너지·고양 (Pre→Chorus build)
[Descending melody]   하강 — 해결·이완·체념·코웃음 (release 자리)
[Emotional climax]    정점 — 가장 강한 가사 + 가장 큰 음악적 lift (Chorus)
[Flattened tone]      ♭3/♭6/♭7 색채 — 블루지·다크·도도 (Verse 담담)
[Falling tension]     긴장 해제 — 단순화·약화·협화 (Bridge 후반)
[Ascending progression] 피치·키·화성 lift 전진 동력
```

### §UE-50.2 섹션별 박힘 (04 §UE-8.4 통합 요약)

```
[Verse]        [Flattened tone]    static/conjunct, 담담 깔림
[Pre-Chorus]   [Ascending melody]  stepwise build
[Chorus]       [Emotional climax]  도약+상승, bIII/IV lift 착지
[Bridge]       [Falling tension]   narrow/대비
[Final Chorus] [Emotional climax]  peak note 1회 + 반음 위
```

### §UE-50.3 화성 연동 (Layer B — CREATE Style box)

태그만으로 부족. *도약 착지점=코드톤*을 CREATE에 명시 (04 §UE-8.2).
```
"hook leaps to the 5th of [chord], ascending then steps down"
"verse melody lands on chord tones of [chord], conjunct deadpan"
```

### §UE-50.4 연출 연동 (Layer C — 연출=컨투어 실현)

컨투어를 보컬 다이내믹으로 실현 (C-113.3 / C-99~102).
```
상승 → (building intensity) + crescendo + belt
하강 → (stripped back) + decrescendo
정체 → deadpan, conversational, even
도약 → (belted) + peak note 강박
```

### §UE-50.5 금지

```
❌ 컨투어를 度단위 산문으로 길게 (04 §UE-8.8) → 정식 태그로
❌ 태그만 박고 화성 연동 누락 → 도약 착지=코드톤 명시
❌ 연출 따로 → 컨투어 실현으로 물림
```

> 풀바디(이론·3층 표기·섹션 템플릿·자동점검)는 **04 §UE-8** 참조.

# === END 10 USER EXTENSION v2.2 PATCH ===
