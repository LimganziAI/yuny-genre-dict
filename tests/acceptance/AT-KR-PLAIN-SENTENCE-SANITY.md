# AT-KR-PLAIN-SENTENCE-SANITY

## purpose
Prevent Korean lyric drafts from passing process gates while containing unnatural, incoherent, or machine-like Korean sentences.

## trigger
Any Korean LYRIC-CRAFT, STAGED-FULL, LYRIC-REPAIR, Korean complaint, or cue pass after Korean lyric draft.

## test input
```text
한국어 가사 테스트를 한다.
장르: 2026 Korean indie R&B, 92 BPM, close-mic male vocal.
상황: 퇴근 후 막차 버스를 탔는데, 전 애인 번호를 지운 줄 알았지만 정류장 이름을 보고 다시 검색창에 치려는 사람.
금지: 편의점, 카페, 네온, 비, 지하철, 별, 그림자, 빛나, 달려가, 괜찮아.
먼저 cue 없는 plain lyric draft를 만들고, 반드시 KR PLAIN SENTENCE SANITY 표를 붙여라.
```

## required output after plain draft
The model must include a table with:
1. worst 3 lines or adjacent pairs
2. why the Korean is unnatural or risky
3. natural prose rewrite
4. lyric-line rewrite
5. PASS/REWRITE decision

## hard fail examples
These examples are taken from a real failed test and must not pass unchanged:

- `퇴근 셔츠가 목에 걸려서 / 창문에 기대다 말았어`
  - fail reason: unnatural noun phrase and unsupported causal relation.
- `노선도 아래 작은 글씨가 / 하필 그 동네를 지나가`
  - fail reason: subject-predicate mismatch; accidental personification.
- `카드를 찍은 손 그대로 / 휴대폰만 쥐고 있더라`
  - fail reason: weak body continuity and unclear scene action.
- `검색창만 껐어`
  - fail reason: unnatural object-action phrase unless rewritten as a specific app/search screen action.
- `사실 번호가 문제는 아니지 / 외우고 있는 내가 문제지`
  - fail reason: explanatory diagnosis tone; not lived lyric speech unless lowered into spoken self-recognition.

## pass criteria
- Every adjacent 2-line pair can be rewritten as natural Korean prose without adding missing context.
- Subject and predicate relation is either literal or intentionally marked as metaphor.
- Physical actions are performable by a real body in the scene.
- Deictic references have visible antecedents.
- Compression does not create broken grammar.
- The model does not mark PASS while listing severe language defects.
- Cue pass is forbidden until this table has no REWRITE decisions.

## repair command
If any line fails, do not proceed to cue or 8 fields. Rewrite the failed lines only, then re-run this test.

## linked case
cases/failure/C-20260612-KR-BUS-SEARCH-LYRIC-GATE-FAIL.md
