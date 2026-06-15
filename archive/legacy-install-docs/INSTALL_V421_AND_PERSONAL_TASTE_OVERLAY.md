# INSTALL — v4.2.1 + all_videos private taste overlay

## Part 1 — v4.2.1 KR Lyric Sovereignty Patch

Install `yuny_suno_os_v4_2_1_korean_lyric_sovereignty_patch.zip`.

Use it as a replacement for the earlier v4.2 package. Do not install both.

Steps:
1. GPT Builder Instructions: replace with `00_GPT_BUILDER/00_INSTRUCTIONS_UNDER_8000_FULL_REPLACE.txt` from v4.2.1 package.
2. Knowledge: replace only `05_lyric_dossier_and_5000_script_engine.md` and `06_korean_lyric_prosody_hook.md`.
3. GitHub: overlay-add the 14 files under `02_GITHUB_SUPPORT/` to matching repo paths.
4. Do not delete existing GitHub files.
5. Do not touch `genre-dictionary/`, `vault/`, or raw corpora.

## Part 2 — all_videos private taste overlay

This package is optional and private.

Recommended GitHub paths:
- `vault/operator-private/LYRIC_HISTORY_PRIVATE_PROFILE_FROM_ALL_VIDEOS.md`
- `vault/operator-private/LYRIC_HISTORY_EXPRESSION_LEDGER_FROM_ALL_VIDEOS.csv`
- `vault/operator-private/CHARACTER_TONE_PRIORS_FROM_ALL_VIDEOS.csv`
- `vault/operator-private/ALL_VIDEOS_PRIVATE_ANALYSIS_STATS.json`
- `lyric-craft/OPERATOR_LYRIC_HISTORY_ROUTER.md`
- `tests/acceptance/AT-OPERATOR-LYRIC-HISTORY-PRIVATE-ROUTE-v1.md`

## Important
- Do not upload raw `all_videos.csv` to GPT Knowledge.
- Do not upload this private profile to Knowledge.
- If the GitHub repo is public or shared, do not commit the `vault/operator-private/` files there.
- If the repo is private and only the operator uses it, committing distilled profile files is acceptable.
- Raw lyrics remain outside the system. This overlay stores distilled tendencies only.

## When to use
- Invoke with “내 결”, “내 작업 히스토리”, character names, or direct request.
- Do not auto-apply to unrelated new songs.

## Smoke
1. “새 곡 만들어줘” → private taste not invoked.
2. “내 결로 가사부터” → private profile invoked, no raw line copying.
3. “네르로 새 곡” → character prior used as taste seed only.
