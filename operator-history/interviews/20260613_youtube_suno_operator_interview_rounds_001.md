# YouTube ↔ Suno Operator Interview Log — Rounds 1-3

Date: 2026-06-13
Runtime: YUNY / TEAM LEMOT SUNO PROJECT
Purpose: Preserve user-confirmed interpretation notes for YouTube-final songs matched to Suno metadata, before building compressed character/IP/vocal-palette profiles.

## Global method lock

Canonical final anchor:
- YouTube title is canonical song title.
- YouTube description lyrics are treated as final/public lyric anchor when present.
- Suno auto-generated title is metadata-only and should not be used as canonical title.
- Image matching is discarded. YouTube image and Suno auto-image are unrelated/noisy.

Matching principle:
- Primary key: YouTube description lyrics ↔ Suno metadata lyrics similarity, after cue/noise cleanup.
- If a matched Suno output is COVER, the parent/source CREATE must be shown with it.
- Analysis unit is a triangle: YouTube FINAL ↔ Suno CREATE ↔ Suno COVER.
- COVER is never analyzed alone; it is a re-render of a CREATE/source output.

Interview storage policy:
- Metadata-inferred values and user-memory values are both preserved when they differ.
- User confirmation overrides automatic character/profile promotion.
- Character names are voice/palette seeds and archive labels, not fixed Suno prompt tokens.
- Do not promote a one-off successful track into character canon unless repeated/user-confirmed.

Required per-song fields going forward:
- youtube_title
- canonical_song_title
- confirmed_ip
- confirmed_character
- character_assignment_type
- lyric_edit_level
- selection_reason_primary
- profile_promotion_level
- youtube_final_summary
- suno_create: id/title/task/model/date/prompt/lyrics_similarity/reverse_8axis
- suno_cover: id/title/task/model/date/parent_create_id/cover_prompt/lyrics_similarity/reverse_8axis
- link_judgment
- user_confirmed_notes
- reusable_system_notes

Reverse 8-axis template:
CREATE reverse 8-axis:
1. concept/persona inferred
2. genre/scene
3. vocal identity
4. lyric/theme/source
5. melody/topline/harmony
6. arrangement/instruments
7. model/version/date/metadata
8. system judgment: what this create was trying to be

COVER reverse 8-axis:
1. target transform direction
2. preserve map: melody/lyrics/vocal/structure
3. substitution map: drums/bass/lead/texture/vocal treatment
4. cover vocal behavior
5. cover arrangement events
6. quality/finish intent
7. Audio Influence / parent linkage / model/date
8. system judgment: why this cover may have become final

---

## Round 1

YouTube title:
- [ラン・サルラ・ラン] マリー - '濡れた靴で踊ろう' [JA]

Canonical song title:
- 濡れた靴で踊ろう

Matched Suno title:
- 雨樋のスニーカー

Suno title status:
- Ignore for canon; metadata-only.

Confirmed IP / character:
- IP: Run Sarura Run
- Character: Marie

User confirmation:
- This was not originally strongly fixed as Marie.
- User assigned it to Marie after hearing/reading because the lyric atmosphere felt more Marie.
- Could have gone to Nerh if lyric/content fit Nerh better.
- Vocal color/sound was also near Marie/Nerh boundary.

Lyric origin/edit level:
- Japanese AI lyric used almost as-is.
- User does not directly write Japanese lyrics; usually works from Korean concept/AI process and accepts if Japanese seems natural and the song works.
- User thought Korean interpretation may be somewhat scattered, but expressions felt pretty; accepted after AI/naturalness check.

Selection reason:
- Primary: sound/melody/overall audio feel.
- Secondary: pretty expressions, usable character assignment.

Prompt/genre note:
- Prompt genre such as samba-cancao sophisti-pop x soft yacht-soul was not a fixed Marie target.
- It worked by chance and should not be promoted as Marie core.
- Old v4-era vocal prompt fragments may have produced useful texture, but lacked precise modern tone/technique control.

Marie/Nerh voice seed note:
- Marie: Japanese rock-leaning female vocal seed; bright, powerful, husky/slightly raspy, raw heartfelt emotion, frustration, passionate/desperate chorus, regret/longing, clumsy painful love rock-anthem energy.
- Nerh: more Western rock-leaning female vocal posture, straighter attack, forward drive.
- These are not fixed presets; they are starting points that change by genre/language/song.

Profile promotion:
- one_off_case
- Do not lock Marie to this exact genre, imagery, or lyric tone.

Reusable system notes:
- Character in YouTube title may be post-hoc assignment, not generation intent.
- Suno auto-title is not reliable.
- Foreign-language lyric acceptance may depend on sound + external naturalness check + translated impression.

---

## Round 2

YouTube title:
- [デルビル P.I.D.] マルティナ - '夏が笑うほど' [JA]

Canonical song title:
- 夏が笑うほど

Confirmed IP / character:
- IP: Derville P.I.D.
- Character: Martina

User confirmation:
- Not initially intended as Martina.
- Theme/mood came first; user assigned to Martina because it fit after hearing.
- Martina is originally that IP's character.
- Martina usually has Latin-side music: Latin jazz / funk / dance-adjacent zones.
- Vocal was lighter than usual Martina, but acceptable because the genre/sound was light.

Lyric origin/edit level:
- Korean concept/original direction given; Japanese AI lyric generated.
- Japanese AI lyrics used almost as-is.
- User remembers concept roughly: upbeat but slightly sad melody at create stage, cover toward para-para / techpara line.
- User judged title/expressions pretty; overall unity may be loose due to foreign-language distance.

Selection reason:
- Primary: sound matched requested concept very well.
- Secondary: prompt instruction seemed followed; overall song worked.

Lyric/title analysis note:
- Title 夏が笑うほど is strong because it sets up bright-summer vs crying-heart contrast.
- Likely strength: title/hook contrast and pretty summer imagery.
- Caution: more sensory collage than tight character-specific narrative.

Martina voice seed:
- Mature, slightly lower, elegant.
- Often Latin/Latin-jazz/funk, but can do rock/pop depending on song.
- Usually user prefers upbeat songs; sad songs exist but are less common.

Profile promotion:
- pattern_candidate_for_martina_light_branch, not fixed canon.
- Do not lock Martina to this exact light vocal or genre.

Reusable system notes:
- Character assignment type must be tracked separately from generation intent.
- Metadata prompt and user-remembered intent can diverge; preserve both.

---

## Round 3

YouTube title:
- [Derville Pen is dead!] 미첼 x 마르티나 - '바람, 풀내음 그리고' [KO]

Canonical song title:
- 바람, 풀내음 그리고

Confirmed IP / character:
- IP: Derville Pen is dead!
- Character label: Mitchell x Martina

User confirmation:
- Originally intended as a Mitchell song.
- After hearing chorus/vocal behavior, user felt Martina should be layered/archived with it.
- Song was assigned to the pair after generation.
- Suno may not reliably render true duet even when prompted; user may archive/label as pair/relationship even if audio is one-vocal.
- This is not a highly precise character-fit song; more of AI test / quick usable result.

Duet reality:
- User hears it as mostly one-vocal feeling.
- If prompt had Female Vocal 1 / Female Vocal 2, it may have been intended, but output likely did not clearly separate.

Lyric origin/edit level:
- AI test lyric / thrown to AI, likely lightly touched or used as-is.
- User often discusses or drafts with AI first; older songs may include more direct user writing, but this one was not high-touch.

Selection reason:
- Usable song + genre variety / overall enough to upload.
- Not because lyric quality or character fit was especially strong.

Vocal mismatch note:
- Metadata/intent seemed Mitchell-leaning airy/light vocal.
- Rendered chorus felt too powerful for Mitchell.
- Martina was added because chorus strength made her useful as support label, but tone was still lighter than typical Martina.
- Mitchell should not be too power-vocal.

Pairing note:
- Mitchell x Martina later has stronger evidence in a song called 'Signal'.
- This song is weak early/archive evidence, not pair-core evidence.

Profile promotion:
- do_not_promote_as_core
- Useful mismatch case for vocal-fit and posthoc character assignment.

Reusable system notes:
- Title with x does not prove actual duet render.
- character x character may mean actual vocal structure, relationship/archive label, or posthoc assignment.
- Intended character and final-assigned character must be separate fields.
- Vocal-render deviation is valuable: e.g. "too powerful for Mitchell" becomes a future protection rule.

---

## Open correction from user

Assistant correction accepted:
- Previous analysis incorrectly looked only at matched Suno output.
- Going forward, every YouTube song must show projected/linked Suno CREATE and COVER values when cover exists.
- For cover cases, parent/source CREATE exists even if missing from current workbook export.
- Parent missing means not found in current export, not nonexistent.

Upcoming priority examples mentioned by user:
- [ラン・サルラ・ラン] マリー x ネル - '氷みたいに熱くなれ' [JA]
- [ラン・サルラ・ラン] レベッカ x ルーク - 'それ、いち、に、さん' [JA]
- [Derville Pen is dead!] Park Bongnam - 'Launchpad Ground' [EN]

Status:
- This file is an interview log, not final compressed profile.
- It should later feed workbook v3 columns and GitHub operator-history / character-ip-profile / vocal-palette summaries.
