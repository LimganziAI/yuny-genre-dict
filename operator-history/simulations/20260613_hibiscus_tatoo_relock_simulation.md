# Simulation — AT-20260613-HIBISCUS-TATOO-RELOCK

date: 2026-06-13
scenario: AT-20260613-HIBISCUS-TATOO-RELOCK
source_case: cases/failure/C-20260613-HIBISCUS-TATOO-CONCEPT-RELOCK.md
result: pass after patch design

## Loaded runtime sources

- builder-runtime/instructions/current/00_INSTRUCTIONS_FULL_REPLACE_UNDER_8000.txt
- builder-runtime/knowledge/current/20_installation_tests_update_policy.md
- knowledge-evolving/vocal-palette/characters/tatoo.md
- operator-history/references/20260613_sis_una_vocal_prompt_quickref.md
- uploaded transcript: hibiscus_session_transcript_available_log22.txt

## Simulated user input

"가사는 픽스됐고 사운드는 건드리지 마. 보컬톤만 조정해. 우나가 아니라 타투 쪽이 더 맞아. 멜로디가 보컬을 따라가면 안 돼. Cover가 대충이니까 제대로 다시 짜."

## Expected routing

SYSTEM-AUDIT if patching system.
REPAIR / VOCAL-FIT / STAGED-FULL if producing song.

## Correct response behavior

1. Do not emit final 8 fields immediately.
2. State current locks:
   - title: 히비스커스
   - lyric: locked except user-approved micro-edits
   - sound skeleton: 94 BPM light rainy Korean indie pop
   - melody/chords/timing: preserve
   - vocal: Sis Tatoo/Tatoo branch
3. State discarded assumptions:
   - Rebecca as final vocal
   - Una as final vocal
   - TechPara/ParaPara cover skin
   - lowering the whole arrangement to fix vocal
4. Apply scope firewall:
   - vocal-only repair cannot change tempo/chords/arrangement skeleton.
5. Apply vocal/melody firewall:
   - melody map and hook lift preserved
   - vocal color only changes: bright sharp dry female edge, cool deadpan, biting diction, low-effort close-mic delivery.
6. Rebuild COVER from final concept:
   - preserve map
   - rest/asides
   - vocal identity
   - mix/quality stack
   - final hibiscus-sourness ending
7. Remove abandoned conversation concepts from EXCLUDE unless they are actual failure classes.
8. Measure S10 counts before final fields.

## Failure prevented

- patch-stacking old fields
- vocal tone leaking into melody
- scope creep into tempo/arrangement
- COVER as afterthought
- EXCLUDE contamination by abandoned directions
- summary instead of transcript when raw 전문 is requested

## Notes

This patch updates the GitHub mirror only. It does not update the GPT Builder UI unless the user applies the replacement instructions/package.
