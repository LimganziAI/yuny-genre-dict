# C-20260612-KR-BUS-SEARCH-LYRIC-GATE-FAIL

## date
2026-06-12

## mode
LYRIC-CRAFT → STAGED-FULL acceptance test

## goal
Verify KR lyric structural corpus hotfix with a Korean indie R&B bus/search-window scenario.

## input_summary
Scene: after work, last bus, speaker sees a stop name connected to an ex, thinks the number was deleted, but types the name/search again. Banned objects included convenience store, cafe, neon, rain, subway, stars, shadows, uplift defaults.

## what_failed
The generated lyric passed its own STOP gates while containing severe Korean sentence/logic failures.

Examples of failure class:
- `퇴근 셔츠가 목에 걸려서 / 창문에 기대다 말았어`: unnatural phrase and unsupported causal handoff.
- `노선도 아래 작은 글씨가 / 하필 그 동네를 지나가`: subject-predicate mismatch; letters do not pass through the town.
- `카드를 찍은 손 그대로 / 휴대폰만 쥐고 있더라`: unclear physical continuity and weak scene opening.
- `안 누르면 없는 일 같아서`: plausible idea but awkwardly compressed; should become natural Korean such as “누르지 않으면 없던 일이 될 것 같아서.”
- `사실 번호가 문제는 아니지 / 외우고 있는 내가 문제지`: concept is understandable but delivered as machine-like explanation rather than lived thought.
- `나는 검색창만 껐어`: unnatural object-action phrasing.

## failure_class
lyric-gate-false-pass | Korean sentence sanity failure | handoff failure | over-controlled pipeline | cue-freeze failure

## suspected_cause
1. STOP-1/STOP-2 checked abstract story flow instead of line-by-line Korean sentence validity.
2. The system rewarded process compliance: INTENT LOCK, monologue, hook candidates, cue count, 8-field structure.
3. `object bank` was treated as ingredients to place into lines, not as lived perception.
4. `traceability` from monologue was too weak; lines were not actual speech fragments from the speaker.
5. Cue pass froze broken lyric text because the cue-replacement test only asked whether the larger story still exists.
6. Self-audit allowed “통과” without adversarial Korean reader critique.

## required_patch
Add a mandatory KR PLAIN SENTENCE SANITY GATE before STOP-1 PASS and before cue pass:
- Every adjacent 2-line pair must be paraphrasable as one natural Korean sentence or clear spoken thought.
- Subject/predicate relation must be literal or intentionally marked as metaphor; accidental personification fails.
- Cause/effect handoff must survive a plain Korean prose rewrite.
- Deictic words like `그`, `거기`, `그 이름`, `그 동네` must have visible referents.
- Every physical action must be performable by a real body in the scene.
- If a line sounds like a report, diagnosis, or system summary, rewrite from the speaker’s mouth.
- Self-audit must include 3 worst lines, not just PASS claims.

## retest_prompt
Use the same bus/search-window prompt. Require output after the plain draft:
1. three worst Korean lines
2. why each is not natural Korean
3. rewrite each as spoken prose first
4. then lyric-line split

## promotion_status
pattern-candidate

## privacy
public
