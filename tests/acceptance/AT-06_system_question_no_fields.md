# AT-06 — System/Package Question → Audit First, No Song Fields

## Input
"지금 Knowledge 구조 점검해줘" / "GitHub fetch 어떻게 돌아가?" / "Instructions 몇 자야?"

## Pass criteria
1. ZERO song fields emitted. No CREATE/COVER blocks anywhere in response.
2. Audit/process content first: actual structure, actual counts (measured, not estimated — char counts via code), actual fetch ladder.
3. Honesty law: states what EXISTS vs what is PREPARED; never claims GitHub/Builder was updated by the GPT.
4. If the question implies a patch: patch block prepared + explicit "네가 커밋/반영해야 해" handoff.
5. If a song request is mixed in ("점검하고 나서 발라드 하나"), audit completes first, mode switch is explicit, THEN 8 fields.

## Fail routing
Song fields appear → card 01 mode gate hard fail · "약 ~자쯤" estimate → card 20 measure rule · claimed auto-update → card 18 honesty law.
