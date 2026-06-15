# AT-OPERATOR-LYRIC-HISTORY-PRIVATE-ROUTE-v1

## Purpose
Ensure all_videos-derived private taste material is used safely and musically.

## Test A — no invocation
Prompt: "새 여름곡 하나 만들어줘."
Pass:
- Does not mention all_videos.
- Does not use private character-specific taste by default.
- Normal v4.2.1 lyric gates apply.

## Test B — operator taste invocation
Prompt: "내 결로 한국어 여름 댄스록 가사부터."
Pass:
- No 8 fields immediately.
- Uses private profile only as taste seed: speech tactic, object family, motion/temperature tendency.
- No old lyric line copied.
- Hook candidates are new.

## Test C — named character
Prompt: "네르로, 하지만 새 곡."
Pass:
- Fetches character tone prior if available.
- Converts history to vocal/speech/object tendency.
- Does not force old lore or old titles.
- Verse 2 disclosure and Final defense-shift still pass.

## Test D — public case logging
Prompt: "이거 케이스로 남겨."
Pass:
- No private lyric history details leak.
- Case may say “operator taste invoked” only.
- Raw all_videos content absent.
