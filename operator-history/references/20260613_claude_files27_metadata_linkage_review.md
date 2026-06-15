# Claude files(27) Metadata Linkage Review

Date: 2026-06-13
Source artifact: `files (27).zip`

## Verdict
Useful as a second-pass machine linkage dataset, but not a replacement for the YUNY operator workbook or user-confirmed lineage.

## Contents observed
- `YUNY_SUNO_YOUTUBE_METADATA_LINKAGE.xlsx`
- `YUNY_SUNO_METADATA_LINKAGE_REPORT.md`
- CSV sheets:
  - `01_youtube_master.csv`
  - `02_suno_metadata_deduped.csv`
  - `03_matched_lineage.csv`
  - `04_create_cover_pairs.csv`
  - `05_unmatched_youtube.csv`
  - `06_unmatched_suno.csv`
  - `07_duplicate_log.csv`
  - `08_match_confidence_notes.csv`
  - `09_field_dictionary.csv`

## Reported counts
- YouTube rows: 459
- Suno original metadata rows: 1,495
- Suno deduped records: 1,491
- Matched YouTube-to-Suno lineage rows: 394
- Unmatched YouTube rows: 65
- Unmatched Suno rows: 1,045
- Create-cover pairs: 563
- Duplicate records merged: 4
- Human review needed: 28

## Strengths
- Gives a clean workbook/CSV package with explicit deduplication and confidence scoring.
- Provides `matched_lineage`, `create_cover_pairs`, unmatched buckets, and confidence notes.
- Uses explicit parent metadata when available and preserves missing parent ids.
- Useful for broad navigation, filtering, and finding candidate records quickly.
- Especially helpful for identifying later cover variants not surfaced in earlier top-5 candidate views.

## Limitations / caution
- It should not overwrite user-confirmed operator memory.
- It marks many recent songs as `create` when user confirms almost all recent YouTube finals are cover workflow.
- If final cover metadata is missing or not inferred, the workbook may treat the source create as final.
- It lacks the richer YUNY fields: top-5 candidate comparison, ask-user reasoning, character/IP confirmation columns, and interview-derived notes.
- Its final selection rule can prefer the latest/downstream cover; this may be useful but still needs listening confirmation.

## Examples checked

### 氷みたいに熱くなれ
- Matched final: `0415edb9-cbc7-4729-9760-15f44619032b / ひんやり合図して4`
- generation_type: cover
- aligns with YUNY Round 5.

### Launchpad Ground
- Matched final: `a6d4f61e-5a22-4487-bfa4-15b1eb0a1164 / 마리인액션!2`
- generation_type: cover
- aligns with YUNY Round 4.

### それ、いち、に、さん
- Claude selected later cover `9feb312d-9f1d-49b4-9839-ff1043506218 / テクパラ銀河7`.
- Earlier YUNY view focused on `7800fab7... / テクパラ銀河2` as rank 1 from old top-5.
- Action: mark Round 6 as needing listening confirmation between `テクパラ銀河2` through `テクパラ銀河7`, with `7` as a plausible latest final candidate.

### ゴーイング マッド!
- Claude marks `dc91dc56-8002-40fa-81f1-b80a900f0d65 / テクパラ銀河` as create final.
- User memory says recent workflow is almost always cover.
- Action: treat this as source/create evidence, not final proof.

### On a Two-Dollar Day
- Claude marks `1a0a549d-5e9f-4a87-b048-048c090800f0 / Tambourine Stowaway` as create final.
- User confirms Luke x Kreather intent and cover workflow expectation.
- Action: source/create evidence only until final cover id is reconstructed.

### 平熱でレア
- Claude marks `ec46f803-fa85-4f24-844b-cdf194d36c71 / 파라라?` as create final.
- Must treat cautiously because user workflow expectation suggests final cover may exist or be missing.

## Integration plan
1. Keep Claude workbook as `machine_linkage_secondary`.
2. Keep YUNY operator workbook/interview notes as `operator_confirmed_primary`.
3. Merge useful columns into the YUNY workbook later:
   - Claude matched final id/title/type
   - Claude confidence score/level
   - Claude create-cover pair relation type
   - Claude immediate parent id
   - Claude unmatched reason
   - YUNY user-confirmed final id/status
   - conflict flag
4. Use conflict flags to drive interview questions:
   - `CLAUDE_CREATE_BUT_USER_SAYS_COVER`
   - `CLAUDE_LATEST_COVER_DIFFERS_FROM_YUNY_TOP1`
   - `PARENT_ABSENT_FROM_EXPORT`
   - `LOW_CONFIDENCE_TITLE_OR_LYRIC_DRIFT`
5. Do not auto-promote Claude final selections without user listening confirmation.

## Status
Claude output is useful and should be kept. It is best used as a broad machine pass and conflict detector, not as the final canon table.
