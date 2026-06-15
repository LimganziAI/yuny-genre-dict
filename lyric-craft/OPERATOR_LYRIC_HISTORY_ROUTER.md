# OPERATOR LYRIC HISTORY ROUTER — private taste overlay

This file contains no private lyric text. It routes the private vault materials.

## Trigger
Use only when the operator says:
- 내 결
- 내 작업 히스토리
- 내가 예전에 쓴 것들
- 유튜브 작업
- all_videos
- a named recurring character from the operator palette
- continue this character/project

Do not apply to unrelated brand-new songs unless the user asks.

## Fetch route
1. `vault/operator-private/LYRIC_HISTORY_PRIVATE_PROFILE_FROM_ALL_VIDEOS.md`
2. `vault/operator-private/CHARACTER_TONE_PRIORS_FROM_ALL_VIDEOS.csv` when a named character appears
3. `vault/operator-private/LYRIC_HISTORY_EXPRESSION_LEDGER_FROM_ALL_VIDEOS.csv` only for row-level history; never quote raw lyrics because none are stored here

## Use rule
Extract:
- preferred speech tactics
- object families
- motion/temperature/light motifs
- character tendency
- structural habit
- anti-patterns

Never extract:
- old hook lines
- exact titles as new titles
- raw lyric lines
- private story details into public cases
- character lore as fixed canon unless the user asks

## Integration with v4.2.1
This overlay is downstream of the universal lyric SOP:
- It cannot override Korean Lyric Sovereignty.
- It cannot skip syllable grid, Python verification, or infill repair.
- It cannot force old style into a new song.
- It only colors speaker/register/object-bank choices.

## Output phrase
“이건 네 작업 히스토리 쪽 결이라, 원문은 복제하지 않고 speech tactic / object family / character tone만 가져왔어.”
