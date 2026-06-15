# YUNY Suno OS — System Rearchitecture Blueprint

## 0. Goal

The system exists for one result: consistently better Suno prompts, lyrics, cueing, CREATE/COVER pairing, and final production quality.

The repository should not become a storage dump. It should be a living operating system where each layer has a clear job.

---

## 1. Core design principle

```text
Instructions decide.
Stable knowledge judges.
GitHub evolving knowledge expands.
Cases teach.
Tests prevent regression.
```

The system should use fewer global rules, stronger routing, better case memory, and clearer promotion paths.

---

## 2. What belongs where

### 2.1 GPT Instructions

Purpose: the shortest possible command layer that controls behavior.

Belongs here:
- user-facing language and tone defaults;
- normal output format;
- CREATE/COVER doctrine;
- GitHub lookup triggers;
- high-level route order;
- promotion ladder;
- hard bans and must-keep rules;
- final answer discipline.

Does not belong here:
- full genre entries;
- long lyric craft chapters;
- full case logs;
- long artist dictionaries;
- old migration files;
- every discovered trick.

Instruction text should answer: **What must the GPT do every time?**

### 2.2 GPT Knowledge

Purpose: stable craft reference that the GPT should use frequently.

Belongs here:
- Suno engine facts and CREATE/COVER mechanics;
- cue grammar and lyric tags;
- lyric craft by language;
- prosody and phonetics;
- arrangement director / PD layer;
- production quality stack;
- diagnostics cascade;
- genre routing index;
- GitHub bridge / knowledge map.

Does not belong here:
- all 278 genre fullbody files;
- every success/failure case;
- volatile trends;
- personal raw notes;
- full migration archive.

Knowledge files should answer: **How does the GPT make the musical decision?**

### 2.3 GitHub evolving knowledge

Purpose: large, changing, expandable memory.

Belongs here:
- full genre dictionary;
- new genre additions;
- K-pop / artist / producer DNA;
- reference cards;
- prompt patterns;
- engineering discoveries;
- lyric cue recipes;
- successful and failed cases;
- operator-specific SOP and experience;
- migration overflow.

GitHub files should answer: **What extra material should the GPT pull only when useful?**

### 2.4 Cases

Purpose: convert experience into reusable improvement.

Belongs here:
- what worked;
- what failed;
- why it failed;
- what was preserved;
- what was changed;
- what pattern should be reused.

A case should never be a diary. It should preserve the lesson.

### 2.5 Tests and gates

Purpose: prevent the system from forgetting its own standards.

Belongs here:
- pre-output quality gate;
- CREATE/COVER separation test;
- lyric cue grammar test;
- COVER quality stack test;
- genre routing test;
- case promotion test.

Tests should answer: **What must not regress?**

---

## 3. Final target architecture

```text
instructions/
  YUNY_MASTER_ROUTER.txt
  YUNY_GPT_INSTRUCTIONS_GITHUB_OS.txt
  patches/

knowledge-static/current-20/
  00_knowledge_routing_map.md
  01_core_system_router_operating_rules.md
  ...
  20_kpop_operator_vault_session_learning.md
  21_github_bridge_operating_layer.md
  patches/

knowledge-evolving/
  genre-dictionary/
    index/
    23_GENRE_FULLBODY/
    additions/
  kpop-artist-dna/
  reference-dna/
  prompt-patterns/
    create-cover/
    lyric-cues/
    excludes/
    sliders/
  production-engineering/
  lyric-craft-updates/

cases/
  success/
  failure/
  neutral-observations/
  index/

tests/
  gates/
  regression/

schemas/
vault/operator-private/
archive/
changelog/
```

---

## 4. Route-first workflow

Every serious request follows this internal sequence:

```text
1. classify task
2. lock user goal
3. choose route
4. use stable knowledge
5. fetch GitHub only when useful
6. build music brief
7. generate or diagnose
8. run pre-output quality gate
9. output usable result
10. record case if the result teaches something
```

---

## 5. Task routes

### 5.1 New serious song

```text
02 Suno engine
→ 05 Arrangement Director / PD
→ 07 genre index or GitHub genre entry if needed
→ language lyric craft + 16 prosody + 17 theme/culture
→ 03 cue grammar
→ 06 production for COVER
→ 04 output template
→ pre-output gate
```

### 5.2 Genre-transform COVER

```text
07 genre / GitHub genre dictionary
→ 05 PD preserve/substitution map
→ 02 COVER mode
→ 06 production quality stack
→ 03 cue preservation
→ cases if similar failures exist
```

### 5.3 Lyric cue or 가사큐 failure

```text
19 diagnosis
→ 03 cue grammar
→ 16 prosody/phonetics
→ target language lyric craft
→ prompt-patterns/lyric-cues
→ failure cases
```

### 5.4 Weak lyric / generic lyric

```text
target language lyric craft
→ 16 prosody
→ 17 theme/culture
→ reference-dna if style anchor exists
→ cases/success if similar theme worked
```

### 5.5 COVER quality failure

```text
19 diagnosis
→ 02 CREATE/COVER doctrine
→ 05 PD layer
→ 06 full production quality stack
→ prompt-patterns/create-cover
→ similar cases/failure
```

### 5.6 Genre or artist request

```text
07 genre routing
→ GitHub genre index
→ 1-3 exact or adjacent entries
→ K-pop/artist DNA if relevant
→ reference analysis if named track/artist is central
```

### 5.7 System/package update

```text
01 core/router
→ 19 diagnostics
→ 21 GitHub bridge
→ docs/update workflow
→ decide placement: instructions, stable knowledge, evolving knowledge, case, test, archive
```

---

## 6. Character budgets and placement

### 6.1 Suno field limits

- Style of Music: hard ceiling 1,000 visible characters.
- Lyrics: hard ceiling 5,000 visible characters.
- Exclude: short control surface, usually around 200 characters but may expand when needed.

### 6.2 YUNY target budgets

- Serious CREATE prompt: dense 700-950 visible characters.
- Serious COVER prompt: dense 700-950 visible characters.
- Sketch CREATE: 250-350 visible characters only when the user asks for quick exploration.
- Lyrics: usually 3,500-4,800 characters for full songs.
- Exclude: active control surface, not an afterthought.

### 6.3 Budget doctrine

CREATE and COVER may both be dense. The difference is not length. The difference is role.

CREATE spends characters on:
- melody identity;
- lyric phrasing;
- vocal identity;
- harmony/rhythm DNA;
- structure;
- signature motif;
- core arrangement bone.

COVER spends characters on:
- target genre micro-anchor;
- preserve map;
- substitution map;
- instrument articulation;
- vocal corridor;
- production stack;
- stereo/frequency/depth;
- final polish and ending preservation.

---

## 7. Case promotion policy

```text
raw note → case → repeated pattern → knowledge patch → instruction patch
```

Promotion should be evidence-based.

Do not turn a single good accident into a global rule.
Do not leave repeated failures as scattered chat memory.

---

## 8. Quality outcome definition

A high-quality YUNY output has:

- specific microgenre/era/scene anchor;
- correct CREATE/COVER role split;
- strong vocal 5-element identity;
- lyric theme with scene, metaphor, progression, and final closure;
- bar-counted section cues;
- square-bracket cue grammar;
- useful EXCLUDE surface;
- COVER Audio Influence guidance;
- production-aware final quality stack;
- no generic macro-genre average;
- no hidden workflow explanation in normal song output.
