# Runtime Patch Proposal — Hibiscus / Sis Tatoo Concept Relock

Date: 2026-06-13
Case: `cases/failure/C-20260613-HIBISCUS-TATOO-CONCEPT-RELOCK.md`
Status: patch proposal logged; direct full-instruction replacement was not applied in this step.

## Problem

The Hibiscus session exposed a repeatable failure class:

- old fields were patched after the song concept changed
- vocal-tone instructions leaked into melody/topline behavior
- a vocal-only repair changed tempo/arrangement feel
- COVER was treated as a copy/refine afterthought instead of the final record
- EXCLUDE carried abandoned conversation ideas instead of actual render failure classes
- transcript requests were answered with summaries

## Patch summary

### Concept Relock Law
When vocal character, genre, tempo, lyric density, arrangement role, cover goal, or final listening judgment changes, stop patch-stacking. Rebuild from that point as the new brief: current locks, discarded assumptions, do-not-touch scope, producer lock, lyric grid, vocal/topline firewall, CREATE/COVER preserve map, EXCLUDE/sliders, then S10. A fixed item must be reinterpreted inside the new concept, not copied blindly.

### Scope Firewall Law
If the user says vocal-only, lyric-only, cover-only, prompt-only, or sound-only, lock all other axes unless the user approves upstream rebuild. Vocal-only repair may change timbre, range color, mic distance, diction, attack/release, fry/breath/noise, vocal EXCLUDE, and COVER vocal preservation. It must not change tempo, chords, melody contour, section order, lyric timing, arrangement skeleton, or genre skin.

### Vocal / Melody Firewall
Vocal identity is timbre and acting, not melody. When changing vocal character, separately protect melody map, hook lift, phrase lengths, chorus shape, peak note, and lyric timing. Use explicit language: preserve the topline; change vocal color only. Character names are routing keys; Suno fields use descriptors. If an emergent render character sounds better and the user approves, promote it as the new vocal lock and rebuild all fields.

### COVER Final-Record Law
COVER is not a style afterthought. If the final render problem is vocal, quality, stereo, finish, or source-skin drift, lock approved lyrics and rebuild COVER CREATE/COVER LYRIC cues/COVER EXCLUDE/COVER SLIDERS from the current concept. Include preserve map, substitution/refine map, vocal identity, timing/rest protection, quality stack, and final/outro preservation.

### EXCLUDE Actual-Failure Rule
EXCLUDE should name the actual failed render class. Do not carry discarded meeting ideas into EXCLUDE just because they appeared earlier in the discussion.

### Transcript Request Rule
When the user asks for 전문/원문/txt/full transcript, provide raw available text first. If part of the session is unavailable as raw text, label it as unavailable rather than reconstructing it as if verbatim.

## Acceptance test

Add and run `AT-20260613-HIBISCUS-TATOO-RELOCK` before Builder replacement. See:

- `operator-history/simulations/20260613_hibiscus_tatoo_relock_simulation.md`
- `builder-runtime/knowledge/current/20_installation_tests_update_policy.md` once updated

## Builder note

This patch is in GitHub mirror only until the Builder instruction file is successfully replaced and applied by the user.
