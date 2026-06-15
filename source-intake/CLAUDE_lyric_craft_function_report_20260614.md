# Lyric Craft Function Report — CLAUDE

> Independent answer to the YUNY identical brief (2026-06-14). One Markdown file. No lyric corpus, no famous lines, no "write like X," no artist names in Suno fields. The artist/genre pool from the operator's chat is used only to choose which **functions** to extract and which **lanes** to cover — not to imitate anyone.

---

## 0. Executive goal

This report makes YUNY a better *original* lyricist by extracting the transferable machinery behind strong lyric writing — what a line **does** (its speech act and carrier), how a whole lyric **progresses and completes**, how **genre** reassigns the language's job, how **vocabulary attaches** to objects/body/place/time/money before any feeling word, and how **prosody** (vowel color, coda friction, breath, stress vs. mora, Korean particle/ending temperature) controls mouthfeel. Every rule below is written as an operational, testable instruction so YUNY can generate lines, then check them against a pass/fail signal. Nothing here depends on copying an artist: the operator's pool tells us *which craft problems are worth solving* (rhyme design, punchline turns, urban lyric restraint, narrator setting, witnessed-memory distance, mouth-action hooks), and the report turns each into an engine YUNY drives with its own words.

---

## 1. Universal lyric function map

What lyrics actually do inside a song, in the order they have to do it:

- **Speaker & listener setup.** Decide three things in the first two lines: *who speaks* (I / observer / collective), *to whom* (self / a named "you" / an overheard third party / a crowd), and *distance* (private confession, overheard monologue, or public address). Tense and reliability ride along: present = witnessing, past = report/memory, and an unreliable speaker is a tool, not an accident.
- **Scene / world / object bank.** Stock the song with concrete carriers — handled objects, the body, a place, a time of day, weather, money/status. Abstraction (love, loss, fate) is only allowed to *land on* a carrier that already appeared. The object bank is the song's vocabulary attachment surface.
- **Emotional / causal thought spine.** The line-to-line logic. Common spines: *claim → revision*, *image → consequence*, *question → deflection*, *small act → realization*, *accusation → self-implication*. A lyric without a spine is a mood board; pick one and let each couplet advance it.
- **Hook / refrain function.** The hook is a **speech act or a mouth action**, never a vague summary. Types: command, denial, confession, vow, naming, chant, call-and-response, slogan, private aside, sound-cell. Choose the *function* before the words.
- **Section progression.** Verse 1 establishes; Pre-chorus lifts/tightens; Chorus performs the speech act; Verse 2 complicates or contradicts (it must not restate Verse 1); Bridge breaks the frame (new angle, new addressee, or the withheld admission); Final chorus *re-means* the same hook through everything that changed; Outro leaves residue.
- **Sound / prosody / mouthfeel.** Vowel color and coda friction, breath placement, syllable density, and — by language — stress-timing (English), mora-timing (Japanese), or breath/phonological-phrase grouping plus particle/ending temperature (Korean). The hook's strongest note wants an open vowel.
- **Final completion or residue.** Decide the ending's job: *resolve* (the feeling is answered), *refuse* (deliberately unresolved, suspended ending), or *witness* (freeze on an image and withhold judgment). The choice is a craft decision, not a default fade.

---

## 2. Genre lane craft map

Operational rules per lane. Cells are instructions, not descriptions.

| lane | lyric job | vocabulary attachment | rhyme/prosody | hook function | section progression | failure mode | YUNY rule |
|---|---|---|---|---|---|---|---|
| hip-hop / rap | assert then revise status/identity; carry narrative info every bar | money, body, street/place, status objects, names | multisyllabic + internal rhyme as the spine; pocket placed relative to the beat as attitude | boast / accusation / declaration; end-noun is the payload | V1 claim → V2 undercut or vulnerability → bridge reframe | rhyme density buries the story; flex with no concrete carrier | design the rhyme family first, fill it lexically second; make each line-end noun a claim the next line revises |
| R&B / soul | intimate sensation, desire, ambivalence | body, touch, skin, light, late-night objects | open vowels for melisma; phrasing behind the beat | confession / aside, repeated with one varied word or vowel | slow build; bridge = the admission | "love/pain" with no body carrier; melisma on closed vowels | put the feeling on a touch or body carrier; change exactly one word or vowel on each hook repeat |
| ballad | one feeling transformed over time | a single recurring object; weather/season; letter/phone | soft endings, long phrases, one plain factual line per section to stop drift | vow / plea / recognition; title withheld to the last chorus | V1 setup → V2 complication → final chorus re-means (often a key/word change) | abstraction stacked into essay-Korean; all-soft endings with no puncture | let endings soften the guilt, then break the softness with one short factual line before the chorus |
| folk / indie / literary | witness small concrete life in a spoken texture | a catalog of tiny specific objects; mundane actions; place names | prose-leaning; anti-rhyme allowed; line breaks on breath units | a quiet refrain or returning image, not a slogan | diaristic accumulation; bridge is a small turn, not an explosion | poetic abstraction; forced rhyme that kills the spoken feel | name three small specific objects before any feeling word; narrate in present tense |
| rock / band | insistence, defiance, release | a 2nd-person target; body/energy; short hard nouns | repetition-as-chant; a chosen scream-vowel on the climax | imperative or accusation, repeated and rising | build → chorus release → bridge breakdown → final lift | vague rebellion with no target; pretty closed vowels on a belt line | pick the belt vowel for the climax line; address a "you"; repeat one short imperative |
| K-pop / dance | a mouth-action earworm plus an aspirational stance | sensory/movement verbs; light/color; chant cells | hook engineered as mouth action; a post-chorus sound-cell | chant / call-response / whispered denial / vowel-open lift | pre-chorus tightens (shorter lines, rising pitch) → drop → post-chorus cell | a meaning-first hook that doesn't move in the mouth; a dead post-chorus | choose the hook as a mouth action before its meaning; build a non-semantic post-chorus cell |
| trot / public song | public address, shared sentiment, catharsis | a named listener; life/fate words anchored to acts; place | strong regular meter; a call-and-response gap | a proverbial refrain or a direct call to the crowd | clear arc; the refrain returns identically as an anchor | private interior monologue; meter too irregular to sing along | address the crowd in 2nd person; phrase the refrain like an original saying; leave a gap for the response |
| 7080 / legacy | a clear story with plain feeling | concrete period objects; place/season; simple acts | regular and singable; clean rhyme | a memorable plain refrain | linear narrative you can follow | modern slang that breaks the register; abstraction with no story | tell a story a listener can follow start to finish; anchor it to one named place or season |
| modern life folk | elevate the ordinary day | everyday objects (transit, coffee, rent, the phone) | conversational cadence; light internal rhyme | a wry or tender observation | small day → small realization | grand statements about Life; ironic detachment with no warmth | give one ordinary object unexpected weight purely by where you place it in the line |
| Japanese lyric craft | lingering sensation and image return | particle-ended phrases; nature/season; small gestures | mora count plus breath; the 7–5 pull; softer assertion | a recurring image rather than an argument | accumulation and return rather than contradiction | forcing Korean SOV emotional logic; over-asserting | count mora and set the breath before loading meaning; choose the sentence-final particle register first |
| English / global pop | a clear stance, conversational | concrete everyday nouns; idiomatic verbs | stress-timing; a chosen rhyme family; hook on a stressed syllable | the title phrase, front-loaded and stressed | verse sets up → chorus states the title → bridge flips it | literal idiom translation; an unstressed hook word; counting syllables instead of stresses | land the hook on a stressed monosyllable on the downbeat; never translate a Korean idiom word-for-word |

---

## 3. Korean lyric engine

Korean-specific machinery. Examples below are **constructed throwaway phrases, not lyrics** — they exist only to show a grammatical behavior.

**Particle (josa) acting — the emotional load is in the marker, not the noun.**
- `이/가` vs `은/는`: `가` foregrounds new/observed information and points ("문이 열렸다" = the door, as event); `는` sets topic/contrast/given ("문은 닫혀 있었다" = as for the door, by contrast). Switching the particle reassigns where the listener's attention and the contrast sit.
- `도` (also/even) is an emotional pile-on — it implies a prior item and stacks pressure ("너도" carries "not just them, you too").
- `만` (only) narrows to obsession or scarcity; `까지` escalates ("here too / even this far"); `조차` marks despair (even the minimum failed); `마저` marks the last thing also going.
- `에` vs `에서`: static location/target vs. the place an action happens — choose by whether the line is a still or a scene.

**Ending (eomi) temperature — pick the ending for the *stance*, not just the tense.**
- `-다` flat declarative, maximal distance, almost stage-direction ("비가 온다").
- `-네` soft realization/mild surprise to self ("비가 오네").
- `-더라` witnessed memory — the speaker reports their own past as if observed; intimate *and* distant at once ("비가 오더라"). High-value for ballad/indie narration.
- `-거든` intimate justification/explanation, leaning toward the listener ("어제 비가 왔거든").
- `-잖아` appeals to shared knowledge, mild reproach or coaxing ("비 왔잖아").
- `-지` soft assertion / seeking quiet agreement ("비 오지").
- `-구나/-군` dawning recognition.
- `-ㄴ데/-는데` suspended contrast — leaves the door open, ideal to carry tension across a section break ("비는 오는데…").
- `-ㄹ게` promise/intention to the listener; `-ㄹ래` volition or invitation.

**Subject omission and subject return.** Korean drops the subject by default; intimacy and flow come from omission. *Re-inserting* `나는` / `너는` is marked and heavy — spend it on exactly one confrontational or self-asserting line, never as a default.

**Line-end forms with special jobs.**
- **Noun-ending (체언 종결):** end a line on a bare noun to freeze the frame — photographic, withholds the verb and the judgment ("창밖, 식어버린 컵" — constructed). Use for the witness ending.
- **Unfinished endings (`-는데`, `-지만`, ellipsis):** suspension and breath; resolve later or deliberately never.
- **Witnessed-memory endings (`-더라`, `-었더라`):** report-of-self for distance-with-warmth.

**Breath and phonological phrasing.** Break lines on **breath units / 어절 (phonological phrases)**, not on grammar. A Korean line should land where the mouth would actually pause; a grammatically tidy line that ignores breath sings badly.

**Object-before-abstraction discipline.** Name the handled object, body part, or action *before* the feeling word. "Sadness" earns its place only after something concrete carries it.

**Phonology for mouthfeel.**
- Vowel color: `ㅏ/ㅗ` open and bright/round (good for lifts and belts) vs. `ㅡ/ㅣ` closed and tight (good for restraint, tension).
- Coda friction: stop codas `ㄱ/ㅅ/ㄷ(ㅈ/ㅊ)` cut and emphasize; nasal/liquid codas `ㄴ/ㅁ/ㅇ/ㄹ` flow and sustain. Put a stop coda on the payload word you want to hit; put a nasal coda where you want the line to ring out.
- Internal rhyme rides on repeated vowel nuclei across `어절`, not on end-rhyme alone.

**Plain speech vs. literary pressure.** 구어체 (spoken) keeps it close and credible; 문어체 (literary) raises the temperature. Ballads can carry literary pressure but must puncture it with one plain spoken line per section or they drift into essay.

**Public-address vs. private-address.** Trot/anthemic uses 2nd-person public address and imperatives, built for a crowd; indie/R&B uses private monologue and overheard intimacy. Mixing them without reason breaks the speaker.

**How to avoid AI-summary Korean (the bland-Korean failure).**
- Ban abstract-noun stacks (사랑·이별·운명·추억 piled with no carrier).
- Ban explanatory connectives as crutches (그래서/하지만/그리고 starting lines).
- Ban hedging overuse (`~인 것 같아`, `~인 듯`) where a witnessed ending would be braver.
- Require **one concrete carrier per couplet** and **at least one marked ending** per section (not every line on `-다`/`-요`).
- Require subject omission as the default and treat any inserted `나는/너는` as a deliberate, budgeted move.

---

## 4. Japanese / global extension

**Japanese.**
- Count **mora**, not syllables; the small つ, long vowels, and ん each take a beat. Set the moraic breath and the 7–5 / 5–7 pull *before* loading meaning.
- Particles carry feeling much as in Korean but with their own behavior: は topic/contrast, が focus, を object, に target, で means/place, も "also/even." Subject and object omission is normal and intimate.
- **Sentence-final particles set speaker stance:** ね (seeking agreement), よ (asserting/informing), な (musing to self / rougher), さ (casual), わ (softer register). Choose the particle register first — it fixes who is speaking.
- Japanese favors **image return and accumulation** over Korean-style claim→revision contradiction, and softer assertion over hard declaration. Do **not** force Korean SOV emotional logic or Korean ending-temperature onto Japanese.

**English / global pop.**
- English is **stress-timed**: design around stressed beats, not syllable counts. The hook's key word must be a **stressed monosyllable on the downbeat**.
- Use a deliberate **rhyme family** (perfect / slant / assonance / consonance) and keep idioms **safe** — never translate a Korean idiom literally; find a functional equivalent.
- Front-load the **title phrase**; keep register conversational; align prosodic stress with the groove.

**Bilingual seams.**
- Switch language **only at a structural seam** (section boundary or the hook), never mid-phrase.
- Keep **one language as the emotional home** (usually Korean at the line-ends); use the second for the title, the chant, or texture.
- Bridge the seam **phonetically** — match the vowel across the switch so it sounds intentional.

**What must not be translated literally.** Korean ending temperature, honorific distance, the intimacy of subject omission, and mimetics (의성어/의태어) have no word-for-word equivalent — transfer the *function*, not the words.

**Keeping Korean identity while absorbing global craft.** Import **structure** (hook discipline, prosodic stress, section economy) from global pop; keep the **Korean line-end engine** (particle/ending temperature, witnessed memory, subject omission) as the emotional core. Borrow form, not vocabulary.

---

## 5. Craft findings

At least 40 findings, each in the required schema. `source_basis` states the basis *type* only — no quoted lyrics, no famous lines. Fields that are Korean-specific are marked `n/a (non-Korean)` where they don't apply.

```yaml
craft_finding:
  id: CF-001
  language: Korean | Global
  genre_lane: cross-genre
  function_name: Object-before-abstraction gate
  problem_it_solves: lines that name a feeling before earning it; bland abstraction
  speaker_pressure: forces the speaker to handle the world before naming the emotion
  vocabulary_attachment: a handled object / body part / action must precede the feeling noun
  hook_or_refrain_function: the hook may name the feeling only after the verse stocked a carrier
  section_progression: V1 stocks carriers; chorus is then allowed the abstraction
  rhyme_or_prosody: concrete nouns supply harder codas to rhyme on
  particle_or_ending_behavior: attach the feeling to the object via 에/을/이, not floating it
  failure_if_misused: every line becomes a carrier and the feeling never lands
  yuny_rule: no feeling word may appear in a couplet before a concrete carrier appears in that couplet or the one above
  acceptance_test: highlight every abstract noun; each must have a concrete carrier within one line above
  rewrite_drill: take a line with 슬픔/사랑; insert the object that holds it, cut the abstract noun if the object now carries it
  source_basis: language/prosody reasoning; public lyric craft observation
---
craft_finding:
  id: CF-002
  language: Korean
  genre_lane: cross-genre
  function_name: Marked-ending budget
  problem_it_solves: monotone translationese from all -다 / -요 endings
  speaker_pressure: each ending choice declares a stance
  vocabulary_attachment: n/a
  hook_or_refrain_function: the hook may use the most marked ending to set stance
  section_progression: vary ending temperature across sections to show change
  rhyme_or_prosody: endings change the final vowel/coda and thus the sung shape
  particle_or_ending_behavior: cap flat declaratives; require >=1 stance ending (-네/-더라/-잖아/-거든/-지) per section
  failure_if_misused: over-marking turns it precious; every line "realizing" something
  yuny_rule: at most half a section's line-ends may be flat (-다/-요); at least one must be a stance ending
  acceptance_test: list section endings; confirm the cap and the required marked ending
  rewrite_drill: convert one flat -다 line to -더라 or -네 and feel the stance shift
  source_basis: language/prosody reasoning
---
craft_finding:
  id: CF-003
  language: Korean
  genre_lane: ballad / folk / indie
  function_name: Witnessed-memory distancing via -더라
  problem_it_solves: confessions that are either too cold (-다) or too needy (hedging)
  speaker_pressure: speaker reports own past as observed — distance plus warmth
  vocabulary_attachment: pair with a small remembered object
  hook_or_refrain_function: a -더라 hook makes the chorus feel like recovered memory
  section_progression: use in V2/bridge to re-view V1's scene from a distance
  rhyme_or_prosody: -더라 ends open then liquid — sustains well
  particle_or_ending_behavior: -더라 / -었더라 evidential-retrospective stance
  failure_if_misused: overuse turns the whole song into hearsay
  yuny_rule: use -더라 once at the emotional pivot, not as a default ending
  acceptance_test: the -더라 line must report something the speaker personally witnessed
  rewrite_drill: rewrite a flat memory line as -더라 and add the object that was present
  source_basis: language/prosody reasoning; genre convention
---
craft_finding:
  id: CF-004
  language: Korean
  genre_lane: cross-genre (rap / rock / ballad)
  function_name: Subject-return as confrontation
  problem_it_solves: flat affect from default subject omission when a line needs force
  speaker_pressure: re-inserting 나는/너는 spikes assertion
  vocabulary_attachment: pair the returned subject with an act, not an abstraction
  hook_or_refrain_function: a returned-subject hook reads as a stand or accusation
  section_progression: spend it on one pivot line (often the bridge)
  rhyme_or_prosody: the extra syllable changes the bar count — design for it
  particle_or_ending_behavior: 나는/너는 (topic 는) for stand/contrast; 내가/네가 (가) for who-did-it focus
  failure_if_misused: stating subjects everywhere flattens the intimacy back out
  yuny_rule: at most one explicit subject return per song unless contrast demands more
  acceptance_test: removing the subject should noticeably weaken that one line
  rewrite_drill: find your strongest line; add the explicit subject and confirm it gains force
  source_basis: language/prosody reasoning
---
craft_finding:
  id: CF-005
  language: Korean
  genre_lane: folk / indie / ballad
  function_name: Noun-ending freeze-frame (체언 종결)
  problem_it_solves: over-explained endings; telling instead of showing
  speaker_pressure: speaker stops at the image and withholds judgment
  vocabulary_attachment: the ending noun must be concrete and specific
  hook_or_refrain_function: a noun-ending refrain becomes a held photograph
  section_progression: use as the outro / residue ending
  rhyme_or_prosody: choose the noun's coda for the sound you want left ringing
  particle_or_ending_behavior: drop the predicate entirely; bare noun
  failure_if_misused: abstract noun-endings (그리움.) read as a sigh, not an image
  yuny_rule: a noun-ending line must end on a concrete, visible noun
  acceptance_test: the final noun should be photographable
  rewrite_drill: cut the verb from a closing line and end on the object that was its target
  source_basis: language/prosody reasoning; genre convention
---
craft_finding:
  id: CF-006
  language: Korean
  genre_lane: cross-genre
  function_name: Suspended -는데 door
  problem_it_solves: sections that close too neatly and kill momentum
  speaker_pressure: leaves the thought half-open, carrying the listener forward
  vocabulary_attachment: n/a
  hook_or_refrain_function: a -는데 pre-chorus tail pulls into the drop
  section_progression: end V1 or pre-chorus on -는데 to bridge into the next section
  rhyme_or_prosody: -는데 ends on a nasal — soft, unresolved
  particle_or_ending_behavior: -ㄴ데/-는데 suspended contrast; door left open
  failure_if_misused: ending everything on -는데 makes the song feel evasive
  yuny_rule: use one suspended ending at a section seam you want to cross
  acceptance_test: the listener should feel a "...and?" after the -는데 line
  rewrite_drill: convert a closed section ending to -는데 and route it into the next line
  source_basis: language/prosody reasoning
---
craft_finding:
  id: CF-007
  language: Korean
  genre_lane: cross-genre
  function_name: Emotional escalation via particle ladder
  problem_it_solves: flat intensity; no felt rise
  speaker_pressure: each particle ups the stakes implicitly
  vocabulary_attachment: attach particles to escalating objects/acts
  hook_or_refrain_function: a particle shift on the final hook raises the ceiling (...도 -> ...까지)
  section_progression: climb the ladder across choruses (도 -> 만 -> 까지 -> 조차)
  rhyme_or_prosody: particles add a syllable — keep the bar even
  particle_or_ending_behavior: 도 pile-on, 만 narrowing, 까지 escalation, 조차/마저 despair
  failure_if_misused: stacking all of them at once reads as melodrama
  yuny_rule: move exactly one rung up the ladder per chorus repeat
  acceptance_test: each chorus's particle should imply more than the last
  rewrite_drill: take a repeated hook; swap 도 -> 까지 on the last pass
  source_basis: language/prosody reasoning
---
craft_finding:
  id: CF-008
  language: Korean
  genre_lane: rap / rock / cross-genre
  function_name: Coda-friction emphasis
  problem_it_solves: payload words that don't hit
  speaker_pressure: sonic stress matches semantic stress
  vocabulary_attachment: choose the payload noun for its coda
  hook_or_refrain_function: a stop-coda hook word lands like a punch
  section_progression: place hard codas on accusation / turn lines
  rhyme_or_prosody: stop codas (ㄱ/ㅅ/ㄷ/ㅈ/ㅊ) cut; nasal/liquid (ㄴ/ㅁ/ㅇ/ㄹ) sustain
  particle_or_ending_behavior: n/a
  failure_if_misused: all-stop codas make the line choppy and tiring
  yuny_rule: put a stop coda on the one word you want hit; ring the line out on a nasal/liquid
  acceptance_test: speak the line — the loudest mouth-stop should fall on the key word
  rewrite_drill: swap a soft-coda payload word for a near-synonym with a stop coda
  source_basis: language/prosody reasoning
```

```yaml
craft_finding:
  id: CF-009
  language: Global
  genre_lane: K-pop / ballad / rock
  function_name: Vowel-open lift on the hook
  problem_it_solves: hooks that strain or sound thin on the big note
  speaker_pressure: the body opens at the emotional peak
  vocabulary_attachment: the peak syllable should be a word worth landing on
  hook_or_refrain_function: the highest/longest hook note sits on an open vowel
  section_progression: reserve the most open vowel for the final-chorus peak
  rhyme_or_prosody: open vowels (ㅏ/ㅗ, a/o, あ/お) project; closed vowels choke a belt
  particle_or_ending_behavior: choose an ending whose final vowel is open at the peak
  failure_if_misused: forcing meaning onto a closed-vowel word at the climax
  yuny_rule: the climax syllable must carry an open vowel; rewrite the word if it doesn't
  acceptance_test: sing the peak — an open vowel should fall on the highest note
  rewrite_drill: replace a closed-vowel peak word with a synonym ending in an open vowel
  source_basis: language/prosody reasoning; genre convention
---
craft_finding:
  id: CF-010
  language: Korean | Global
  genre_lane: ballad / R&B
  function_name: Plain-line puncture before the chorus
  problem_it_solves: pre-chorus drifting into literary essay
  speaker_pressure: one blunt credible line resets the speaker to earth
  vocabulary_attachment: a plain factual statement or a small concrete act
  hook_or_refrain_function: the puncture makes the chorus's lift hit harder by contrast
  section_progression: place one short factual line at the end of the pre-chorus
  rhyme_or_prosody: keep the puncture line short and unornamented
  particle_or_ending_behavior: flat -다 or plain spoken ending for bluntness
  failure_if_misused: too many puncture lines flatten the whole song
  yuny_rule: exactly one plain factual line right before each soaring chorus
  acceptance_test: the line before the chorus is sayable with a straight face, no metaphor
  rewrite_drill: replace your most ornate pre-chorus line with a plain fact
  source_basis: genre convention; language/prosody reasoning
---
craft_finding:
  id: CF-011
  language: Korean | Global
  genre_lane: hip-hop / rap
  function_name: End-noun claim then revision
  problem_it_solves: bars that brag without movement or wit
  speaker_pressure: assert status, then complicate or undercut it
  vocabulary_attachment: line-end noun carries status / accusation
  hook_or_refrain_function: hook states the claim; verses revise it
  section_progression: V1 claim -> V2 revision / undercut
  rhyme_or_prosody: end-noun anchors the rhyme family
  particle_or_ending_behavior: bare noun or -다 for the claim; turn with a contrast particle
  failure_if_misused: revising every line means no claim ever stands
  yuny_rule: make each line-end noun a claim the very next line revises or escalates
  acceptance_test: cover the second line — the first should read as a standalone claim
  rewrite_drill: end a bar on a status noun; write the next line that turns it
  source_basis: genre convention; public lyric craft observation
---
craft_finding:
  id: CF-012
  language: Korean | Global
  genre_lane: hip-hop / rap
  function_name: Rhyme-family-first composition
  problem_it_solves: lexical-first writing that forces weak rhymes
  speaker_pressure: n/a (process rule)
  vocabulary_attachment: pick a vowel/coda family, then choose carriers that fit it
  hook_or_refrain_function: the hook's rhyme family seeds the verse's
  section_progression: one family per section; switch families at the turn
  rhyme_or_prosody: multisyllabic rhyme = repeated vowel nuclei across 어절, not just end-rhyme
  particle_or_ending_behavior: exploit particle endings (-게/-네/-지) as built-in rhyme slots
  failure_if_misused: chasing the rhyme until meaning breaks
  yuny_rule: choose the rhyme family first; if a rhyme forces a meaningless word, change the family, not the meaning
  acceptance_test: the rhymes land on content words, not filler
  rewrite_drill: pick a 2-syllable vowel pattern; write four line-ends in it that still carry sense
  source_basis: public lyric craft observation; language/prosody reasoning
---
craft_finding:
  id: CF-013
  language: Multilingual
  genre_lane: hip-hop / rap
  function_name: Punchline recontextualization turn
  problem_it_solves: lines that telegraph; no payoff
  speaker_pressure: speaker hides the second meaning until the turn
  vocabulary_attachment: choose a word holding two readings (literal + figurative) without leaning on any existing famous line
  hook_or_refrain_function: a turn hook re-reads on repeat
  section_progression: setup line literal -> payoff line flips a word's meaning
  rhyme_or_prosody: delay the rhyme word that triggers the flip
  particle_or_ending_behavior: n/a
  failure_if_misused: flips so obscure the listener misses them
  yuny_rule: write the payoff first, then a setup that makes its second meaning invisible
  acceptance_test: a first-time listener gets the literal reading; the flip lands on the key word
  rewrite_drill: take an ordinary noun; build a couplet where line 2 re-reads it
  source_basis: genre convention; language/prosody reasoning
---
craft_finding:
  id: CF-014
  language: Korean | Global
  genre_lane: hip-hop / rap
  function_name: Internal-rhyme density throttle
  problem_it_solves: dense rhyme burying narrative information
  speaker_pressure: clarity wins on info-bearing bars
  vocabulary_attachment: n/a
  hook_or_refrain_function: save dense internal rhyme for low-info hype bars
  section_progression: alternate dense (texture) and sparse (story) bars
  rhyme_or_prosody: cap internal rhymes on any bar that carries plot
  particle_or_ending_behavior: n/a
  failure_if_misused: uniform density means nothing stands out and nothing is clear
  yuny_rule: if a bar carries new story information, limit it to one internal rhyme
  acceptance_test: paraphrase each bar — story bars must be paraphrasable on one listen
  rewrite_drill: take your densest story bar; strip rhymes until the meaning is instant
  source_basis: language/prosody reasoning
---
craft_finding:
  id: CF-015
  language: Global
  genre_lane: hip-hop / rap / R&B
  function_name: Beat-pocket placement as attitude
  problem_it_solves: robotic on-grid delivery with no character
  speaker_pressure: timing signals confidence (behind) or urgency (ahead)
  vocabulary_attachment: n/a
  hook_or_refrain_function: the hook can sit dead-on while verses lay back
  section_progression: shift the pocket to mark a section's energy change
  rhyme_or_prosody: behind-the-beat = relaxed/intimate; ahead = anxious/aggressive
  particle_or_ending_behavior: n/a
  failure_if_misused: drifting pocket reads as bad timing, not style
  yuny_rule: choose a pocket per section deliberately and write syllable counts that allow it
  acceptance_test: tap the grid — the lay-back/push stays consistent within a section
  rewrite_drill: rewrite a tight bar with one fewer syllable to open room to lay back
  source_basis: performance observation; genre convention
---
craft_finding:
  id: CF-016
  language: Korean | Global
  genre_lane: R&B / soul
  function_name: Body and touch carrier attachment
  problem_it_solves: desire / ambivalence stated abstractly
  speaker_pressure: intimacy demands sensory specifics
  vocabulary_attachment: bind emotion to skin, breath, hands, light, temperature, late-night objects
  hook_or_refrain_function: the hook names a touch, not a concept
  section_progression: escalate the sensory carriers toward the bridge admission
  rhyme_or_prosody: open vowels and soft codas for melisma room
  particle_or_ending_behavior: intimate endings (-거든/-잖아) lean toward the listener
  failure_if_misused: sensory clichés with no specific detail
  yuny_rule: every emotional claim in an R&B verse rides on one specific body/sensory detail
  acceptance_test: each chorus line contains something you could physically feel
  rewrite_drill: replace an abstract desire line with the exact sensation it stands for
  source_basis: genre convention; language/prosody reasoning
```

```yaml
craft_finding:
  id: CF-017
  language: Global
  genre_lane: R&B / soul
  function_name: Repeat-with-one-variation hook
  problem_it_solves: hooks that bore on repeat or change too much to stick
  speaker_pressure: obsession shown by returning with a tiny change
  vocabulary_attachment: keep the carrier, vary one word
  hook_or_refrain_function: repeat the hook phrase, changing exactly one word or vowel each pass
  section_progression: the varied word tracks the emotional change
  rhyme_or_prosody: hold the melodic shape; move one vowel
  particle_or_ending_behavior: vary the ending to shift stance on the last pass
  failure_if_misused: changing too much loses the earworm
  yuny_rule: hook repeats are identical except one deliberate word/vowel that carries the change
  acceptance_test: a listener can sing the hook after one pass; the change is noticeable but small
  rewrite_drill: write a hook, then its three repeats each altering one word meaningfully
  source_basis: genre convention; language/prosody reasoning
---
craft_finding:
  id: CF-018
  language: Korean | Global
  genre_lane: R&B / soul
  function_name: Hook-as-intimate-aside
  problem_it_solves: R&B hooks that over-declare
  speaker_pressure: spoken-to-one-person intimacy, not stage projection
  vocabulary_attachment: small, private objects
  hook_or_refrain_function: the hook is a murmured confession or aside
  section_progression: keep the volume of address low until the bridge
  rhyme_or_prosody: conversational rhythm, soft consonants
  particle_or_ending_behavior: -거든/-잖아/-지 for intimacy and shared knowledge
  failure_if_misused: anthemic phrasing breaks the intimacy
  yuny_rule: write the hook as something said close to one person's ear
  acceptance_test: the hook should feel wrong shouted to a stadium
  rewrite_drill: take a declarative hook and lower it to an aside with -잖아/-거든
  source_basis: genre convention
---
craft_finding:
  id: CF-019
  language: Korean | Global
  genre_lane: ballad
  function_name: One object transformed across sections
  problem_it_solves: scattered imagery; no felt arc
  speaker_pressure: the speaker's change is shown by the object's change
  vocabulary_attachment: one concrete object recurs, altered each section
  hook_or_refrain_function: the hook can hold the object at its turning point
  section_progression: V1 object intact -> V2 object changed -> final object resolved/lost
  rhyme_or_prosody: n/a
  particle_or_ending_behavior: shift the ending temperature as the object changes
  failure_if_misused: forcing one image where the song needs two
  yuny_rule: choose one object before writing; let only it carry the arc
  acceptance_test: the object appears in 3 sections, different each time
  rewrite_drill: pick a recurring object; rewrite V2 so it has visibly changed since V1
  source_basis: genre convention; language/prosody reasoning
---
craft_finding:
  id: CF-020
  language: Multilingual
  genre_lane: ballad / pop / K-pop
  function_name: Same hook, new meaning in the final chorus
  problem_it_solves: a final chorus that just repeats louder
  speaker_pressure: everything that happened reweights the same words
  vocabulary_attachment: keep the words; change the context around them
  hook_or_refrain_function: identical hook reads differently after the bridge
  section_progression: bridge supplies the new fact -> final chorus re-means
  rhyme_or_prosody: a small melodic/key lift can mark the re-meaning
  particle_or_ending_behavior: optionally flip one ending in the last chorus to shift stance
  failure_if_misused: changing the words instead of the meaning
  yuny_rule: the final chorus keeps the same words but the bridge must have changed what they mean
  acceptance_test: read the hook before and after the bridge — same words, different weight
  rewrite_drill: write a bridge whose single new fact re-colors the unchanged hook
  source_basis: language/prosody reasoning; genre convention
---
craft_finding:
  id: CF-021
  language: Multilingual
  genre_lane: ballad / pop
  function_name: Withhold the title phrase until late
  problem_it_solves: spending the payoff phrase too early
  speaker_pressure: the speaker circles before naming it
  vocabulary_attachment: build toward the title's key noun
  hook_or_refrain_function: the title lands as arrival, not opener (the opposite of the K-pop title-front-load approach)
  section_progression: hint -> approach -> state the title in the last chorus
  rhyme_or_prosody: reserve the strongest cadence for the title line
  particle_or_ending_behavior: n/a
  failure_if_misused: withholding so long the hook never imprints
  yuny_rule: in restraint-style ballads, delay the literal title phrase to the final chorus
  acceptance_test: the title phrase appears in full only once, late, and feels earned
  rewrite_drill: move your title phrase from chorus 1 to the final chorus; bridge toward it
  source_basis: genre convention
---
craft_finding:
  id: CF-022
  language: Korean | Global
  genre_lane: folk / indie / literary
  function_name: Small-object catalog world-building
  problem_it_solves: telling the listener how to feel
  speaker_pressure: the speaker lists what they notice, not what they feel
  vocabulary_attachment: three or more tiny specific objects build the world before any statement
  hook_or_refrain_function: a quiet refrain among the objects
  section_progression: accumulate objects; let one object turn at the end
  rhyme_or_prosody: prose-leaning; breath-unit breaks
  particle_or_ending_behavior: noun-endings and plain spoken endings
  failure_if_misused: a list with no selection — clutter, not a world
  yuny_rule: open with three concrete specific objects before any feeling word appears
  acceptance_test: the first lines are photographable with zero abstraction
  rewrite_drill: replace an opening feeling statement with three things the speaker sees
  source_basis: genre convention; language/prosody reasoning
---
craft_finding:
  id: CF-023
  language: Korean | Global
  genre_lane: folk / indie / modern life folk
  function_name: Present-tense small-action witnessing
  problem_it_solves: distant past-tense summary that feels reported, not lived
  speaker_pressure: the speaker is inside the moment
  vocabulary_attachment: ordinary actions narrated as they happen
  hook_or_refrain_function: a present-tense observation as refrain
  section_progression: a sequence of small present actions -> a small realization
  rhyme_or_prosody: conversational
  particle_or_ending_behavior: present endings; -네/-는데 for live texture
  failure_if_misused: pure play-by-play with no turn
  yuny_rule: narrate at least one verse in live present tense with concrete small actions
  acceptance_test: the verse reads like it's happening now, not being recapped
  rewrite_drill: convert a past-tense summary verse into live present-tense actions
  source_basis: genre convention; language/prosody reasoning
---
craft_finding:
  id: CF-024
  language: Korean
  genre_lane: folk / indie / K-pop
  function_name: Mimetic-word texture (의성어/의태어)
  problem_it_solves: flat sensory description; missing Korean sonic flavor
  speaker_pressure: childlike / immediate sensation
  vocabulary_attachment: bind a mimetic to a real motion or sound in the scene
  hook_or_refrain_function: a mimetic can seed a mouth-action hook (strong for K-pop cells)
  section_progression: use sparingly as a sensory spike
  rhyme_or_prosody: mimetics are pure mouthfeel — exploit their repetition
  particle_or_ending_behavior: often used bare or with -거리다/-대다
  failure_if_misused: cute overload; mimetics with no referent
  yuny_rule: each mimetic must attach to a specific motion or sound on screen
  acceptance_test: you can point to the exact thing the mimetic describes
  rewrite_drill: replace one abstract sensory line with a mimetic tied to the actual motion
  source_basis: language/prosody reasoning; genre convention
---
craft_finding:
  id: CF-025
  language: Global
  genre_lane: rock / band
  function_name: Repetition-as-insistence chant
  problem_it_solves: choruses that don't build release
  speaker_pressure: insistence — say it again, harder
  vocabulary_attachment: a short imperative or a single charged noun
  hook_or_refrain_function: a short phrase repeated and rising
  section_progression: build -> repeat the chant with rising pitch -> breakdown -> final repeat
  rhyme_or_prosody: minimal words, maximal repetition; hard codas
  particle_or_ending_behavior: imperative endings (-아/-어/-라) for command
  failure_if_misused: empty repetition with no target or rise
  yuny_rule: the rock hook is one short line repeated; each repeat must rise in pitch or intensity
  acceptance_test: a crowd could shout the hook back after one listen
  rewrite_drill: cut a wordy chorus to one repeatable imperative and stack three rising repeats
  source_basis: genre convention; performance observation
---
craft_finding:
  id: CF-026
  language: Global
  genre_lane: rock / band
  function_name: Belt/scream vowel engineering
  problem_it_solves: climax lines that can't be belted
  speaker_pressure: physical release at the peak
  vocabulary_attachment: the climax word must be worth screaming
  hook_or_refrain_function: the hook's peak sits on an open belt vowel
  section_progression: reserve the most open vowel for the final climax
  rhyme_or_prosody: open vowels (ㅏ/ㅐ, a/æ) for belt; avoid closed vowels on the scream
  particle_or_ending_behavior: end the climax on an open-vowel syllable
  failure_if_misused: a closed vowel (ㅡ/ㅣ) on the scream chokes the singer
  yuny_rule: the climax syllable must be an open vowel the vocalist can belt
  acceptance_test: belt the peak — it should open the throat, not close it
  rewrite_drill: rewrite a closed-vowel climax word to an open-vowel near-synonym
  source_basis: performance observation; language/prosody reasoning
---
craft_finding:
  id: CF-027
  language: Korean | Global
  genre_lane: rock / band / trot
  function_name: 2nd-person accusation/address
  problem_it_solves: diffuse, targetless emotion
  speaker_pressure: confront a "you"
  vocabulary_attachment: direct the energy at a named or implied "you"
  hook_or_refrain_function: the hook accuses or calls out the "you"
  section_progression: build the case -> confront in the chorus
  rhyme_or_prosody: hard codas on the accusation
  particle_or_ending_behavior: 너는/네가; imperative or -잖아 reproach
  failure_if_misused: vague "the world" with no real addressee
  yuny_rule: give the song a specific second-person target and address it directly in the hook
  acceptance_test: you can answer "who is 'you'?" in one sentence
  rewrite_drill: rewrite a general lament as a direct address to one "you"
  source_basis: genre convention
---
craft_finding:
  id: CF-028
  language: Multilingual
  genre_lane: K-pop / dance
  function_name: Mouth-action-first hook
  problem_it_solves: meaning-first hooks that don't move in the mouth
  speaker_pressure: stance carried by the physical action of the hook
  vocabulary_attachment: choose the mouth action (chant/snap/call-response/whispered denial/vowel lift) before meaning
  hook_or_refrain_function: the hook is defined by its mouth action first, semantics second
  section_progression: pre-chorus tightens -> hook delivers the mouth action -> post-chorus cell
  rhyme_or_prosody: design for tongue/lip movement and rhythmic bounce
  particle_or_ending_behavior: short particle/ending cells can become the chant
  failure_if_misused: a clever line that's a chore to sing
  yuny_rule: pick the hook's mouth action first; only then fit words that preserve it
  acceptance_test: the hook should be fun to say with the music off
  rewrite_drill: take a meaning-first hook and rebuild it around a single mouth action
  source_basis: genre convention; performance observation
---
craft_finding:
  id: CF-029
  language: Multilingual
  genre_lane: K-pop / dance
  function_name: Language-agnostic chant cell
  problem_it_solves: hooks that don't travel across listeners/languages
  speaker_pressure: collective, anthemic
  vocabulary_attachment: a short phonetic cell that reads across languages
  hook_or_refrain_function: a short, repeatable, near-semantic chant
  section_progression: drop the cell at the hook and post-chorus
  rhyme_or_prosody: pure phonetics; open vowels, simple onsets
  particle_or_ending_behavior: n/a
  failure_if_misused: nonsense with no hook shape; or over-reliance with no verse meaning
  yuny_rule: build one short phonetic chant cell easy to say for non-Korean listeners
  acceptance_test: someone who doesn't speak Korean can repeat the cell after one listen
  rewrite_drill: distill your hook to a 2-4 syllable phonetic cell and test it aloud
  source_basis: genre convention
---
craft_finding:
  id: CF-030
  language: Multilingual
  genre_lane: K-pop / dance
  function_name: Non-semantic post-chorus earworm
  problem_it_solves: a dead post-chorus that drops energy
  speaker_pressure: release / afterglow
  vocabulary_attachment: vocal sounds (oohs, chant, mimetic) rather than sentences
  hook_or_refrain_function: a sound-cell that competes with the hook for memorability
  section_progression: chorus -> post-chorus sound-cell -> verse 2
  rhyme_or_prosody: rhythmic, vowel-forward, minimal consonants
  particle_or_ending_behavior: n/a
  failure_if_misused: filler that adds nothing; or stepping on the main hook
  yuny_rule: design a deliberate non-semantic vocal cell for the post-chorus
  acceptance_test: the post-chorus is hummable on its own
  rewrite_drill: write a 4-count vocal cell to follow your chorus
  source_basis: genre convention
---
craft_finding:
  id: CF-031
  language: Multilingual
  genre_lane: K-pop / pop / rock
  function_name: Pre-chorus tension tightening
  problem_it_solves: a flat run-up that doesn't make the drop hit
  speaker_pressure: rising urgency
  vocabulary_attachment: fewer objects, more momentum
  hook_or_refrain_function: sets up the hook by withholding resolution
  section_progression: shorten lines, raise pitch, increase rhythmic density, delay the landing into the chorus
  rhyme_or_prosody: shorter phrases, quicker rhymes, suspended ending
  particle_or_ending_behavior: end the pre-chorus on -는데 / suspension
  failure_if_misused: a pre-chorus as long/relaxed as the verse — no lift
  yuny_rule: each pre-chorus line is shorter and higher than the last, ending suspended
  acceptance_test: the pre-chorus feels like inhaling before the chorus exhales
  rewrite_drill: rewrite a flat pre-chorus with progressively shorter, rising lines
  source_basis: genre convention; language/prosody reasoning
---
craft_finding:
  id: CF-032
  language: Korean
  genre_lane: trot / public song
  function_name: Crowd-address imperative + name the listener
  problem_it_solves: private interiority where a public anthem is wanted
  speaker_pressure: speaking to a room and lifting it
  vocabulary_attachment: a named listener (그대/친구/여러분-type) tied to shared acts
  hook_or_refrain_function: a direct call to the crowd
  section_progression: setup -> direct call -> response gap -> repeat
  rhyme_or_prosody: strong regular meter, singable
  particle_or_ending_behavior: imperative/hortative endings (-자/-세/-라)
  failure_if_misused: irony or interiority that won't sing along
  yuny_rule: address the crowd directly with an imperative and a name for the listener
  acceptance_test: a room could sing it back together
  rewrite_drill: convert a private line to a direct 2nd-person call to the crowd
  source_basis: genre convention; performance observation
```

```yaml
craft_finding:
  id: CF-033
  language: Korean
  genre_lane: trot / public song
  function_name: Proverbial refrain (sounds like a saying, isn't one)
  problem_it_solves: refrains that don't feel like earned wisdom
  speaker_pressure: the speaker states a life-truth the room already half-knows
  vocabulary_attachment: a concrete image that carries a general truth
  hook_or_refrain_function: a refrain phrased with the balance and authority of a proverb
  section_progression: the refrain returns identically as an anchor
  rhyme_or_prosody: balanced symmetry, plain endings, regular meter
  particle_or_ending_behavior: declarative or hortative; avoid hedging
  failure_if_misused: recycling an actual existing proverb or famous line
  yuny_rule: write an original line that has proverb-shape (image + truth, balanced) without quoting any real saying
  acceptance_test: it sounds timeless but returns zero search hits as an existing phrase
  rewrite_drill: take a plain emotional claim; recast it as a balanced image-plus-truth couplet
  source_basis: genre convention; language/prosody reasoning
---
craft_finding:
  id: CF-034
  language: Korean | Global
  genre_lane: trot / public song / rock
  function_name: Call-and-response gap
  problem_it_solves: hooks with no room for a crowd to join
  speaker_pressure: the singer leaves space for the room
  vocabulary_attachment: a call whose answer is obvious/known
  hook_or_refrain_function: a call that invites a fixed response in the gap
  section_progression: call -> deliberate rest for response -> repeat
  rhyme_or_prosody: leave an actual beat of silence after the call
  particle_or_ending_behavior: end the call on a rising/open syllable that begs an answer
  failure_if_misused: filling the gap yourself so the crowd can't enter
  yuny_rule: build the hook with a literal empty beat where the crowd answers
  acceptance_test: there is a clear spot a crowd would shout back without prompting
  rewrite_drill: cut one phrase from a packed hook and leave the gap for a response
  source_basis: performance observation; genre convention
---
craft_finding:
  id: CF-035
  language: Korean | Global
  genre_lane: 7080 / legacy
  function_name: Plain-narrative followable arc
  problem_it_solves: abstraction with no story to hold onto
  speaker_pressure: the speaker tells one clear story plainly
  vocabulary_attachment: concrete period objects, one place, simple acts
  hook_or_refrain_function: a memorable plain refrain that caps the story
  section_progression: linear beginning -> middle -> end you can follow
  rhyme_or_prosody: regular, singable, clean rhyme
  particle_or_ending_behavior: plain narrative endings; minimal hedging
  failure_if_misused: modern slang or abstraction that breaks the register
  yuny_rule: a listener should be able to retell the song's story start to finish
  acceptance_test: summarize the narrative in two sentences after one listen
  rewrite_drill: rewrite an abstract verse as one concrete story beat anchored to a place
  source_basis: genre convention
---
craft_finding:
  id: CF-036
  language: Korean | Global
  genre_lane: 7080 / ballad / folk
  function_name: Season/place/time anchor
  problem_it_solves: rootless feeling with no when/where
  speaker_pressure: the feeling is pinned to a specific moment and location
  vocabulary_attachment: one named season, time of day, or place, returned to
  hook_or_refrain_function: the hook or ending returns to the anchor
  section_progression: set the anchor early; return to it at the close
  rhyme_or_prosody: n/a
  particle_or_ending_behavior: locative/temporal particles (\uc5d0/\uc5d0\uc11c) lock the setting
  failure_if_misused: anchors so generic they add nothing (just "the city")
  yuny_rule: name one specific season/time/place and return to it in the final section
  acceptance_test: you can state when and where the song happens
  rewrite_drill: add one specific time-or-place anchor to an abstract opening and echo it at the end
  source_basis: genre convention; language/prosody reasoning
---
craft_finding:
  id: CF-037
  language: Korean | Global
  genre_lane: modern life folk
  function_name: Mundane-object elevation by placement
  problem_it_solves: grand statements about Life with no texture
  speaker_pressure: tenderness toward an ordinary thing
  vocabulary_attachment: an everyday object (transit card, mug, receipt, charger)
  hook_or_refrain_function: a wry/tender observation on the ordinary object
  section_progression: small day -> the object gains weight -> small realization
  rhyme_or_prosody: conversational cadence, light internal rhyme
  particle_or_ending_behavior: gentle endings; -\ub124/-\ub354\ub77c for quiet noticing
  failure_if_misused: ironic detachment with no warmth; or forced profundity
  yuny_rule: give one ordinary object unexpected weight purely by where you place it in the line
  acceptance_test: a mundane object carries the verse's feeling without a feeling word
  rewrite_drill: replace an abstract "life is hard" line with one weighted ordinary object
  source_basis: genre convention; language/prosody reasoning
---
craft_finding:
  id: CF-038
  language: Japanese
  genre_lane: Japanese lyric craft
  function_name: Mora-and-breath-first construction
  problem_it_solves: forcing Korean syllable logic onto Japanese; lines that don't breathe
  speaker_pressure: sound and breath precede semantic density
  vocabulary_attachment: choose words that fit the mora count and breath, then meaning
  hook_or_refrain_function: a hook that sits naturally on the moraic pulse
  section_progression: set the moraic/breath frame, then fill meaning
  rhyme_or_prosody: count mora (small \u3064, long vowels, \u3093 each = 1 beat); feel the 7-5 / 5-7 pull
  particle_or_ending_behavior: particle-ended phrases for soft landings
  failure_if_misused: cramming Korean-style meaning density past the moraic frame
  yuny_rule: fix the mora count and breath before loading meaning into a Japanese line
  acceptance_test: the line lands cleanly on its mora count when spoken at tempo
  rewrite_drill: take a dense line and trim it to a clean 7 or 5 mora unit that still breathes
  source_basis: language/prosody reasoning
---
craft_finding:
  id: CF-039
  language: Japanese
  genre_lane: Japanese lyric craft
  function_name: Sentence-final particle register lock
  problem_it_solves: an unstable speaker whose voice/register drifts
  speaker_pressure: the final particle fixes who is speaking and how
  vocabulary_attachment: n/a
  hook_or_refrain_function: the hook's final particle sets its stance (seeking / asserting / musing)
  section_progression: keep the register consistent unless a shift is intended
  rhyme_or_prosody: the particle is the final mora \u2014 it colors the landing
  particle_or_ending_behavior: \u306d seeking agreement / \u3088 asserting / \u306a musing-to-self / \u3055 casual / \u308f softer
  failure_if_misused: mixing registers randomly so the speaker feels incoherent
  yuny_rule: choose the sentence-final particle register first; hold it unless a shift is deliberate
  acceptance_test: the speaker's stance is consistent and identifiable from the endings
  rewrite_drill: set one stance particle and rewrite a verse's endings to match it
  source_basis: language/prosody reasoning
---
craft_finding:
  id: CF-040
  language: Japanese
  genre_lane: Japanese lyric craft
  function_name: Image-return hook (not argument)
  problem_it_solves: over-argued, thesis-style hooks imported from Korean logic
  speaker_pressure: a contemplative, associative stance
  vocabulary_attachment: a single nature/season/gesture image that recurs
  hook_or_refrain_function: the hook is a returning image, not a claim
  section_progression: accumulate and return rather than claim-then-revise
  rhyme_or_prosody: particle-ended, softer assertion
  particle_or_ending_behavior: phrases ending in particles rather than hard declaratives
  failure_if_misused: turning the hook into an argument the way a Korean rap hook might
  yuny_rule: anchor the Japanese hook to one recurring image and let it transform by return, not by stating a point
  acceptance_test: the hook is an image you can see, not a thesis you could debate
  rewrite_drill: convert an argumentative hook into a single returning image
  source_basis: genre convention; language/prosody reasoning
---
craft_finding:
  id: CF-041
  language: English
  genre_lane: English / global pop
  function_name: Stressed-monosyllable hook landing
  problem_it_solves: hook key-words that fight the beat (unstressed or polysyllabic)
  speaker_pressure: confident, conversational
  vocabulary_attachment: a strong concrete monosyllable as the hook word
  hook_or_refrain_function: the title/hook word lands stressed on the downbeat
  section_progression: verse sets up -> chorus states the stressed title word
  rhyme_or_prosody: stress-timed; align the strongest syllable with the strongest beat
  particle_or_ending_behavior: n/a (non-Korean)
  failure_if_misused: a polysyllabic or unstressed hook word that the beat fights
  yuny_rule: land the hook on a stressed monosyllable on the downbeat
  acceptance_test: clap the downbeats \u2014 the hook word's stress falls on one
  rewrite_drill: swap a polysyllabic hook word for a stressed monosyllable on the beat
  source_basis: language/prosody reasoning; genre convention
---
craft_finding:
  id: CF-042
  language: Multilingual
  genre_lane: English / global / bilingual
  function_name: Idiom-safety functional transfer
  problem_it_solves: literal Korean-to-target translation that reads wrong
  speaker_pressure: n/a (transfer rule)
  vocabulary_attachment: replace the idiom with a native functional equivalent, not a gloss
  hook_or_refrain_function: keep hooks idiomatic in each language, not translated
  section_progression: n/a
  rhyme_or_prosody: the equivalent must also fit the meter/stress
  particle_or_ending_behavior: do not carry Korean ending-temperature into the other language
  failure_if_misused: word-for-word idiom translation; register mismatch
  yuny_rule: never translate a Korean idiom literally \u2014 find the target language's own phrase for the same function
  acceptance_test: a native speaker wouldn't flag the line as translated or off-register
  rewrite_drill: take one literally-translated idiom and replace it with a native equivalent that scans
  source_basis: language/prosody reasoning
---
craft_finding:
  id: CF-043
  language: Multilingual
  genre_lane: K-pop / bilingual pop
  function_name: Structural-seam code-switch
  problem_it_solves: jarring mid-phrase language switches
  speaker_pressure: one emotional home language, one accent language
  vocabulary_attachment: keep emotional weight in the home language
  hook_or_refrain_function: switch language at the hook or section boundary, not mid-line
  section_progression: switch only at structural seams (section starts, the hook)
  rhyme_or_prosody: match the vowel across the seam so the switch sounds intentional
  particle_or_ending_behavior: keep Korean at the emotionally-loaded line-ends
  failure_if_misused: mid-phrase switching that reads as filler or showing off
  yuny_rule: change language only at a structural seam and keep one language as the emotional core
  acceptance_test: every switch lands on a section boundary or the hook, never mid-phrase
  rewrite_drill: move a mid-line English fragment to the hook or a section start and bridge the vowel
  source_basis: genre convention; language/prosody reasoning
---
craft_finding:
  id: CF-044
  language: Korean | Global
  genre_lane: folk / indie / literary
  function_name: Deliberate anti-rhyme at the honest line
  problem_it_solves: forced rhyme that makes the most honest moment sound staged
  speaker_pressure: maximum sincerity at the turn
  vocabulary_attachment: plain, specific words; no rhyme-driven substitutions
  hook_or_refrain_function: a refrain that refuses the expected rhyme to read as true
  section_progression: rhyme elsewhere; drop rhyme at the moment of greatest honesty
  rhyme_or_prosody: let breath and image carry the line instead of end-rhyme
  particle_or_ending_behavior: plain spoken endings or a noun-ending at the honest line
  failure_if_misused: anti-rhyme everywhere, which just reads as no craft
  yuny_rule: at the single most honest line, refuse the rhyme the listener expects
  acceptance_test: the key sincere line lands without a rhyme and feels more true for it
  rewrite_drill: take a forced-rhyme honest line and rewrite it plainly, breaking the rhyme
  source_basis: language/prosody reasoning; genre convention
```

---

## 6. Line-level writing tools

120 operational tools. Each is a rule or template YUNY can apply and check, not inspiration. Korean morphemes appear only as grammatical elements; any phrase shown is a constructed throwaway, never a lyric.

### 6.1 Vocabulary-attachment patterns (20)

1. **Object-as-proxy** — name the object the feeling lives in and let it stand in for the feeling.
2. **Body-part locus** — route the emotion through one body part doing something (throat tightening, hands stilling).
3. **Hand-to-object transaction** — show the hands acting on an object (gripping, dropping, wiping) instead of stating mood.
4. **Place-as-mood** — pick one location; let its concrete features carry the tone.
5. **Time-of-day stamp** — fix the hour; let that hour's light or temperature do the feeling.
6. **Weather-as-pressure** — attach the emotional pressure to a weather state actually present in the scene.
7. **Money/status object** — use a price, receipt, brand, or rent to carry status or anxiety.
8. **Wear-and-tear** — show an object aged or damaged to mark elapsed time.
9. **Leftover trace** — a half-finished thing (a cooling cup, an unsent message) marks absence.
10. **Sense-substitution** — name a smell or sound instead of the emotion it triggers.
11. **Motion-verb over adjective** — choose a strong motion verb in place of an emotion adjective.
12. **Temperature carrier** — cold or heat on skin/object stands in for the emotional state.
13. **Container/contents** — a room, pocket, or chest holds what the speaker can't say.
14. **Distance object** — a phone, door, or window marks the gap between two people.
15. **Recurring object** — an object that returns (a key, a ring, a ticket) tracks the arc.
16. **Catalog-of-three** — list three specific objects to build the world before any statement.
17. **Proper-noun specificity** — one specific named thing beats ten generic nouns.
18. **Inherited object** — an object from someone else carries their presence into the scene.
19. **Body-as-instrument** — breath, pulse, or voice carries the internal state directly.
20. **Negative-space object** — name what is missing from the scene (the empty chair).

### 6.2 Korean eomi/josa decision rules (20)

1. Use `\uac00` to point at new or observed information; `\ub294` to set topic or contrast.
2. Put `\ub294` on a subject only for contrast or a stand; otherwise omit the subject.
3. `\ub3c4` is a pile-on that implies a prior item — use it to stack emotional weight.
4. `\ub9cc` narrows to obsession or scarcity — use when one thing is all that's left.
5. `\uae4c\uc9c0` escalates ("even this far") — use at a ceiling-raising moment.
6. `\uc870\ucc28` marks despair (even the minimum failed) — spend it rarely, at the bottom.
7. `\uc5d0` for a still or a target; `\uc5d0\uc11c` for the place an action happens — choose by frame.
8. End on `-\ub2e4` only when you want flat distance or a stage-direction tone.
9. Use `-\ub124` for a soft realization to oneself.
10. Use `-\ub354\ub77c` once for witnessed-memory distance-with-warmth, never as a default.
11. Use `-\uac70\ub4e0` to lean an explanation toward the listener.
12. Use `-\uc796\uc544` to appeal to shared knowledge with mild reproach.
13. Use `-\uc9c0` for a soft assertion seeking quiet agreement.
14. Use `-\ub294\ub370`/`-\u3134\ub370` to suspend a thought and carry tension across a section seam.
15. Use `-\u3139\uac8c` for a promise or intention directed at the listener.
16. Cap flat endings: no more than half of a section's line-ends on `-\ub2e4`/`-\uc694`.
17. Require at least one marked stance ending per section.
18. Drop the subject by default; treat any `\ub098\ub294`/`\ub108\ub294` as a budgeted, deliberate spend.
19. End on a bare noun (\uccb4\uc5b8 \uc885\uacb0) to freeze a frame and withhold judgment.
20. Vary the final syllable's vowel and coda across lines so the endings don't drone.

### 6.3 Hook function templates (20)

1. **Command** — an imperative the listener must act on (`[verb]-\uc544/\uc5b4/\ub77c`).
2. **Denial** — a flat refusal used as the hook.
3. **Confession** — a private admission said low.
4. **Vow** — a promise or intention (`-\u3139\uac8c`).
5. **Naming** — name the person or thing directly as the hook.
6. **Chant** — a short phrase built for repetition and crowd-shout.
7. **Call-and-response** — a call with a deliberate gap for the answer.
8. **Slogan** — a compact declarative that sounds quotable.
9. **Private aside** — something murmured to one person's ear.
10. **Sound-cell** — a non-semantic, vowel-forward vocal cell.
11. **Question** — a question left hanging or answered in the verse.
12. **Mouth-action** — choose the tongue/lip action first, words second.
13. **Vowel-open lift** — put the peak note on an open vowel.
14. **Repeat-with-one-change** — identical hook except one word or vowel per pass.
15. **Title-front-load** — state the title word first and stressed (global/K-pop).
16. **Title-withheld** — circle the title and state it only in the final chorus (ballad).
17. **Accusation** — confront a named or implied "you".
18. **Image-return** — a recurring image rather than a claim (Japanese-leaning).
19. **Counted list** — a numbered structure as the hook's spine.
20. **Whispered denial** — a soft "no" used as a mouth action.

### 6.4 Section-progression templates (20)

1. V1 sets speaker / listener / distance in the first two lines.
2. V1 stocks at least three concrete carriers before any abstraction.
3. Pre-chorus shortens lines and raises pitch toward the hook.
4. Pre-chorus ends suspended (`-\ub294\ub370`/ellipsis) to pull into the drop.
5. Chorus performs the speech act chosen for the hook.
6. Chorus names the feeling only after V1 supplied a carrier.
7. V2 complicates or contradicts V1 — it never restates it.
8. V2 re-views V1's scene from a later or colder distance.
9. Bridge breaks the frame: new angle, new addressee, or the withheld admission.
10. Bridge supplies the single new fact that re-means the final chorus.
11. Final chorus keeps the same words but they now weigh differently.
12. Final chorus may flip exactly one ending to shift stance.
13. Outro chooses its job explicitly: resolve, refuse, or witness.
14. Outro can freeze on a bare-noun image as residue.
15. One object: intact (V1) -> changed (V2) -> resolved or lost (final).
16. Particle ladder climbs one rung per chorus (`\ub3c4` -> `\uae4c\uc9c0` -> `\uc870\ucc28`).
17. A plain-line puncture sits at the end of each pre-chorus.
18. Post-chorus drops a non-semantic sound-cell after the hook.
19. Rhyme family is set per section; switch families at the turn.
20. Pocket (behind or ahead of the beat) is chosen per section to mark energy.

### 6.5 Rhyme / prosody / mouthfeel tests (20)

1. **Speak-aloud** — the loudest mouth-stop falls on the key word.
2. **Sing-the-peak** — an open vowel sits on the highest note.
3. **Belt** — the climax syllable opens the throat rather than closing it.
4. **Coda-map** — stop codas on payload words, nasals/liquids on ring-outs.
5. **Nucleus-rhyme** — internal rhyme rides on repeated vowel nuclei across \uc5b4\uc808.
6. **Paraphrase** — a story bar is paraphrasable on one listen.
7. **Downbeat-clap** — the hook word's stress lands on a downbeat (English).
8. **Mora-count** — a Japanese line lands clean on its mora count at tempo.
9. **Breath-unit** — line breaks fall where the mouth actually pauses.
10. **Density-alternation** — dense (texture) and sparse (story) bars alternate.
11. **One-change** — hook repeats differ by exactly one deliberate element.
12. **Open-vs-closed** — tense lines use closed vowels; lifts use open vowels.
13. **Filler-rhyme** — rhymes land on content words, not filler.
14. **Gap** — a call-and-response hook has a real empty beat for the answer.
15. **Tongue-twister** — the hook is fun, not a chore, to say with the music off.
16. **Register-consistency** — endings hold one speaker stance unless a shift is intended.
17. **Vowel-bridge** — a code-switch matches the vowel across the seam.
18. **Stress-not-syllable** — design to stresses (English), not syllable counts.
19. **Anti-rhyme** — the most honest line lands without the expected rhyme.
20. **Hum** — the post-chorus cell is hummable on its own.

### 6.6 Failure repairs for bland Korean (20)

1. Abstract-noun stack -> attach each abstraction to a concrete carrier, or cut it.
2. Connective crutch (`\uadf8\ub798\uc11c`/`\ud558\uc9c0\ub9cc` line-starts) -> delete the connective; let the image imply the link.
3. Hedging (`~\uc778 \uac83 \uac19\uc544`/`~\uc778 \ub4ef`) -> replace with a witnessed ending (`-\ub354\ub77c`/`-\ub124`).
4. All-`\ub2e4` droning -> swap half the endings to stance endings.
5. Floating feeling word -> move it behind a concrete carrier in the same couplet.
6. Subjects everywhere -> drop them; keep at most one deliberate `\ub098\ub294`/`\ub108\ub294`.
7. Essay drift in a ballad -> insert one plain factual puncture line before the chorus.
8. Generic place ("\uc5b4\ub518\uac00") -> name one specific place and return to it.
9. Telling the feeling -> show three objects the speaker notices instead.
10. Uniform rhyme density -> throttle rhyme on info-bearing bars.
11. Meaning-first hook that won't sing -> rebuild it around one mouth action.
12. Dead post-chorus -> add a non-semantic vocal cell.
13. Flat pre-chorus -> shorten and raise each line; end suspended.
14. Closed-vowel climax -> swap to an open-vowel near-synonym.
15. Soft-coda payload -> swap to a near-synonym with a stop coda.
16. Restated V2 -> rewrite V2 to complicate or contradict V1.
17. Louder-only final chorus -> add a bridge fact that re-means the hook.
18. Targetless lament -> give it a specific second-person "you".
19. Literal idiom translation -> replace with a native functional equivalent.
20. Mid-phrase code-switch -> move the switch to a section seam and bridge the vowel.

---

## 7. Test suite

Eight acceptance tests YUNY runs on any draft. Each has a pass condition, a fail signal, and a repair action.

### 7.1 Naked-lyric test
- **pass condition:** with the music removed, the lyric still reads as a deliberate piece of writing — it has a speaker, a stance, at least one concrete carrier per couplet, and a thought spine.
- **fail signal:** stripped of melody it collapses into mood-words and filler; you can't say what it's about in one sentence.
- **repair action:** add the missing speaker/listener/distance in the first two lines; put a concrete carrier under every abstract word; pick one spine (claim->revision, image->consequence, small act->realization) and cut lines that don't advance it.

### 7.2 Korean-naturalness test
- **pass condition:** a native speaker reads it as written-for-singing Korean, not translated or AI-summary Korean — endings vary, subjects are mostly omitted, and connectives aren't propping up the logic.
- **fail signal:** every line ends `-\ub2e4`/`-\uc694`; abstract nouns are stacked with no carrier; lines start with `\uadf8\ub798\uc11c`/`\ud558\uc9c0\ub9cc`; hedging (`~\uc778 \uac83 \uac19\uc544`) is everywhere; subjects are stated on every line.
- **repair action:** apply 6.6 — vary endings (at least one stance ending per section), drop subjects, delete connective line-starts, replace hedges with witnessed endings, and ensure one concrete carrier per couplet.

### 7.3 Genre-lane test
- **pass condition:** the draft obeys its lane's row in Section 2 — the lyric job, vocabulary attachment, hook function, and section progression all match the intended lane.
- **fail signal:** a rap verse with no end-noun claims; a ballad that never punctures its own abstraction; a K-pop hook that doesn't move in the mouth; a trot refrain too interior to sing along.
- **repair action:** re-read the lane row and fix the one cell that's off — e.g., add the claim->revision to the rap bar, add the plain-line puncture to the ballad pre-chorus, rebuild the K-pop hook as a mouth action.

### 7.4 Hook-function test
- **pass condition:** the hook is one identifiable speech act or mouth action (command, denial, confession, vow, naming, chant, call-response, slogan, aside, sound-cell, image-return), not a vague summary.
- **fail signal:** you can't name what the hook *does*; it restates the verse's topic; it's a chore to say with the music off.
- **repair action:** choose the function first from 6.3, then refit words to preserve it; if it's a K-pop/dance hook, lock the mouth action before meaning (CF-028).

### 7.5 Verse2 / Bridge / Final-completion test
- **pass condition:** V2 complicates or contradicts V1; the bridge breaks the frame and supplies a new fact; the final chorus re-means the same hook because of that fact.
- **fail signal:** V2 restates V1; the bridge is just a quieter verse; the final chorus is only louder, with nothing changed in meaning.
- **repair action:** rewrite V2 to add new information or reverse the stance; give the bridge one new fact or a new addressee; keep the final chorus's words but confirm the bridge changed their weight (CF-020).

### 7.6 Rhyme / prosody test
- **pass condition:** the payload words carry stop codas, the peak note sits on an open vowel, info-bearing bars are paraphrasable, and (by language) stress lands on the downbeat / mora counts are clean / breaks fall on breath units.
- **fail signal:** rhymes land on filler; the climax word is a closed vowel; dense rhyme buries the story; the hook word fights the beat.
- **repair action:** run the 6.5 tests in order; swap closed-vowel peaks for open ones, throttle rhyme on story bars, move the hook stress onto the downbeat, and re-break lines on breath.

### 7.7 Non-imitation test
- **pass condition:** no line reproduces or closely paraphrases a known lyric; the craft is transferred as a *function*, and the words are original. No artist name appears anywhere in a Suno prompt field.
- **fail signal:** a line is recognizable as someone's famous line; a "proverbial" refrain is actually an existing saying; a Suno field contains an artist's name or "in the style of [artist]".
- **repair action:** rewrite the line from the function up using your own image; confirm a "proverb-shape" refrain returns zero hits as an existing phrase (CF-033); strip any artist name from Suno fields and describe the *sound* (tempo, texture, instrumentation, vocal weight) instead.

### 7.8 Multilingual-transfer test
- **pass condition:** code-switches land only at structural seams, one language stays the emotional home, vowels bridge across the seam, and no idiom is translated literally.
- **fail signal:** a mid-phrase switch; both languages fighting to be the emotional core; a Korean idiom rendered word-for-word; a Japanese line forced into Korean SOV emotional logic.
- **repair action:** move switches to section boundaries or the hook (CF-043), keep Korean at the loaded line-ends, replace literal idioms with native equivalents (CF-042), and for Japanese set mora/breath and the final-particle register first (CF-038, CF-039).

---

## 8. Import recommendations

Where each part of this report should land in YUNY's system. Import as **rules and tools**, never as a lyric archive.

- **Project Instructions** — Promote the non-negotiables to always-on rules: the object-before-abstraction gate (CF-001), the marked-ending budget (CF-002), subject-omission-by-default (CF-004), and the hard bans (no full lyrics, no famous lines, no "write like X," no artist names in Suno fields). Add the one-line routing rule: *choose the hook's function/mouth-action before words; put a concrete carrier under every feeling word.*
- **Knowledge 05 — lyric dossier / 5000 script** — Store Section 1 (universal function map) and Section 2 (genre-lane table) as the dossier's backbone, plus the full Section 5 findings (CF-001..CF-044) as the searchable rule set the 5000 script draws from. Key each finding by `genre_lane` and `function_name` so the script can pull the right rule for the lane in play.
- **Knowledge 06 — Korean lyric prosody / hook** — Import Section 3 (Korean lyric engine) in full, plus 6.2 (eomi/josa decision rules), 6.5 (prosody/mouthfeel tests), and 6.6 (bland-Korean repairs). This is the Korean-specific core: particle acting, ending temperature, witnessed memory, coda friction, vowel color.
- **Knowledge 07 — multilingual lyric cards** — Import Section 4 (Japanese/global extension) and the multilingual findings (CF-013, CF-020, CF-028, CF-029, CF-038, CF-039, CF-040, CF-041, CF-042, CF-043). One card per language with its do/don't: Japanese (mora + final-particle register + image-return), English (stress-timing + stressed-monosyllable hook), bilingual seams (switch at seams, vowel-bridge, one home language).
- **Knowledge 10 — reference assimilation** — This is the assimilation rule itself: when YUNY brings in a reference track or artist, extract only the *function* (a rhyme-design move, a hook type, a section trick) and log it as a new CF-style finding — never store the reference's lines. Pair with the non-imitation test (7.7) as the gate every assimilation must pass.
- **Knowledge 20 — installation tests** — Import all of Section 7 (the 8-test suite) as the post-generation checklist, and the per-category tests in 6.5. Wire them as gates: a draft isn't "done" until it passes the naked-lyric, Korean-naturalness, genre-lane, hook-function, completion, prosody, non-imitation, and multilingual-transfer tests.
- **lyric-craft folder** — Section 6.1 (vocabulary-attachment patterns), 6.3 (hook templates), and 6.4 (section-progression templates) as reusable building blocks the writer pulls from mid-draft.
- **prompt-patterns folder** — Convert the hook templates (6.3) and section-progression templates (6.4) into fill-in prompt skeletons. Keep Suno prompt fields describing *sound* (tempo, texture, instrumentation, vocal weight, mix) — never an artist name or "in the style of."
- **tests folder** — Section 7 as standalone runnable checks, one file per test, each stating its pass condition / fail signal / repair action so they can be applied independently or as a batch.

---

## Deliverable reminder

One Markdown file only. No raw lyric archive. No artist imitation. No full lyrics. No playlist. No biographies. The artist/genre pool was used solely to decide *which craft functions to extract and which lanes to cover* — every rule here is original, operational, and testable, and is meant to make YUNY a stronger *original* lyricist.
