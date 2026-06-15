# CHARACTER VOCAL PALETTE — Usage Policy

This library is a musical palette, not lore.

## What it is
- Character names are shorthand for vocal color, delivery tendency, genre comfort zone, and failure-prevention hints.
- A character can move genres when the song needs it.
- Vocal fit outranks character default. If key, BPM, melody contour, lyric register, or arrangement density conflict with the named palette, redesign the palette for the song rather than forcing the song into the old character box.
- Roles, story ranks, party positions, and non-musical lore are ignored unless the operator explicitly asks for them.

## Runtime order
1. User request and song goal
2. Vocal fit: gender/range/body/placement/delivery/technique
3. Genre and arrangement compatibility
4. Lyric language and register
5. Character palette as shorthand
6. Suno field grammar and output gates

## Rules for use
- Do not put character names in Suno prompt fields by default.
- Convert the named palette into English vocal descriptors.
- Use genre zones as suggestions, not locks.
- When the operator says "이 톤은 누구다", update the relevant palette after the song result is observed.
- If a palette causes repetition across songs, deliberately shift one axis: genre, BPM, vocal placement, lyric register, groove, or instrumentation.

## Diversity protocol
For repeated use of one character:
- Version A: default zone
- Version B: adjacent genre
- Version C: opposite texture while preserving vocal identity
- Version D: duet/FX/section-only usage
- Version E: lyric-register inversion

## Protected-expression guard
Do not clone artist lyrics, melody, or arrangement. Artist-like descriptions in old notes must be converted to functional traits only.
