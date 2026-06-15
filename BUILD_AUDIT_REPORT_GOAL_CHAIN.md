# CURRENT GOAL-CHAIN PATCH — BUILD AUDIT REPORT

Status: CURRENT INSTALL CANDIDATE / not live-applied.

## Purpose
Patch the package around the actual goal:
Suno integrated production OS, not a lyric-only bot and not an 8-field formatter.
The runtime must drive:
Universal Korean lyric quality → CREATE source design → CREATE source simulation/repair → COVER final-record staging → render-stage repair.

## Changes made
- Added `UNIVERSAL LYRIC QUALITY LAW` to Project Instructions.
- Added universal Korean lyric gate to cards 05 and 06.
- Added goal-chain behavioral acceptance to card 20.
- Added `lyric-craft/UNIVERSAL_KOREAN_LYRIC_QUALITY_GATE.md`.
- Added `tests/acceptance/AT_CURRENT_GOAL_CHAIN_BEHAVIOR.md`.
- Added `tests/test_goal_chain_behavior.py`.
- Preserved the V4.7 full-base GitHub material; this is not patch-only.
- Removed generated cache directories from the deliverable tree.

## Integrity
- Project Instructions: 7981 chars (<8000)
- Knowledge files: 20
- GitHub upload files: 844
- Root folders: 1_PROJECT_INSTRUCTIONS / 2_KNOWLEDGE_FILES / 3_GITHUB_UPLOAD_STRUCTURE

## Executable test result
`python -m pytest -q -p no:cacheprovider`
Result: 10 passed

Script checks:
- test_current_full_package.py PASS
- test_goal_chain_behavior.py PASS
- test_install_candidate.py PASS
- test_register_standard_guard.py PASS

## Remaining reality gate
This package can test the production chain structurally. Actual Suno audio still decides final sonic success.
