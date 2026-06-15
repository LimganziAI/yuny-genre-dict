# Correction — Rounds 1-3 Require CREATE ↔ COVER Re-Link

Date: 2026-06-13
Applies to prior interview rounds:
- Round 1: [ラン・サルラ・ラン] マリー - '濡れた靴で踊ろう' [JA]
- Round 2: [デルビル P.I.D.] マルティナ - '夏が笑うほど' [JA]
- Round 3: [Derville Pen is dead!] 미첼 x 마르티나 - '바람, 풀내음 그리고' [KO]

## User correction

User states that the already-interviewed songs also went through COVER, so each should have an original CREATE/source output even if the current workbook's top matched row is gen/create.

## Current workbook state observed

The raw workbook's FINAL_LINKS top match currently shows:
- 濡れた靴で踊ろう: matched_task_type = gen, lyric_similarity = 100%
- 夏が笑うほど: matched_task_type = gen, lyric_similarity = 100%
- 바람, 풀내음 그리고: matched_task_type = gen, lyric_similarity = 100%

No child covers for those exact matched create IDs were found inside the currently supplied metadata export.

## Interpretation

Do not treat the workbook's gen top match as proof that the YouTube final audio was create-only.

Possible explanations:
1. The true final COVER metadata is missing from the supplied export set.
2. The true final COVER exists but did not surface as top lyric match due to title/lyric/metadata divergence.
3. The workbook matched the source/create lyrics perfectly, while the actual final audio was a cover render using the same lyrics.
4. Suno export lineage may be incomplete for these tracks.

## Revised rule

For every previously interviewed song, run a second-pass lineage search:
- YouTube final title/lyrics
- top lyric-matched gen/create
- all candidate covers around the same date/time
- parent_id / cover_clip_id / edited_clip_id
- any missing parent ids
- user memory of actual cover render

Final analysis must preserve:
- user_memory_final_from_cover: true
- workbook_top_match_task_type
- confirmed_or_missing_cover_id
- confirmed_or_missing_parent_create_id
- nearest_available_create_family_candidate
- confidence and conflict note

## Status

Rounds 1-3 remain valid as user interview notes for character assignment, lyric origin, and selection reason.
They are not final lineage analysis until CREATE↔COVER linkage is reconstructed.
