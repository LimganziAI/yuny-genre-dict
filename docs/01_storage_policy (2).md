# YUNY Suno OS — Storage Policy

## Purpose

This document defines where each type of project material should live inside the repository.

## Repository layers

### 1. Runtime guide
Location: `instructions/`

Keep this layer short. It should contain the rules that control routing, output format, GitHub lookup order, review flow, and update flow.

Do not place long dictionaries, case archives, artist notes, or old migration files here.

### 2. Stable knowledge
Location: `knowledge-static/current-20/`

This layer stores the stable reference set used by the GPT package: Suno engine behavior, lyric cue grammar, lyric craft, prosody, production design, diagnostics, arrangement direction, and genre routing.

### 3. Growing knowledge
Location: `knowledge-evolving/`

This layer stores material that will keep changing: genre dictionary entries, K-pop and artist DNA, reference cards, prompt patterns, lyric cue recipes, engineering notes, and trend notes.

### 4. Cases and private notes
Locations: `cases/`, `vault/`

This layer stores practical experience: what worked, what failed, what was observed, and what should be reused later.

## Promotion ladder

```text
observation
→ case
→ repeated pattern
→ knowledge patch
→ runtime guide patch
```

One good or bad result is stored as a case. Repeated cases become a pattern. A verified pattern becomes a knowledge patch. A rule that changes the whole workflow becomes a runtime guide patch.

## Duplication rule

Do not copy the same long text into multiple layers.

- `instructions/` holds the operating rule.
- `knowledge-static/` holds stable reference content.
- `knowledge-evolving/` holds expandable dictionaries and cards.
- `cases/` holds concrete experience.
- `archive/` keeps migration originals.

## Archive rule

Migration originals stay in `archive/`. They are kept for traceability, not for direct routing. Current routing names should follow the active GPT file map.
