# KR Web Expression Comparison Protocol

## date
2026-06-12

## purpose
Add web-based Korean expression comparison to prevent narrow, awkward, or translated Korean lyric lines.

This protocol is for line repair and expression calibration, not for copying web sentences or lyrics.

## source classes
Use sources in this order:

1. User/team lyric corpus and current project premise
2. NIKL/local Korean corpora already uploaded to runtime
3. Official Korean language resources
   - Urimalsaem / Standard Korean dictionary family for lexical sense, tone, derivative words
   - NIKL language information and corpus portals for corpus-oriented context
   - Korean Basic Dictionary when learner-oriented example sentences help
4. General Korean web search for expression comparison
5. K-pop corpus only for lyric structure, repetition, hook, and section compression

## when to invoke web comparison
Use when a Korean lyric draft has:

- awkward particles
- unclear subject-predicate relation
- suspicious verb-object pairing
- translated phrasing
- body/action handoff that feels impossible
- noun pile without action
- line pair that cannot be restored as plain Korean
- metaphor that feels decorative rather than scene-born
- chorus phrase that feels like a summary, not a singable Korean expression

## comparison loop
For a questionable line or pair:

```text
ORIGINAL LINE/PAIR:
INTENDED MEANING:
PROSE REPAIR CANDIDATES:
SEARCH QUERIES:
- exact phrase
- natural prose candidate
- verb-object pair
- noun + common predicate
- scene-specific Korean phrase
WEB/CORPUS OBSERVATION:
REWRITE DECISION:
LYRIC LINE:
```

## what to compare
Do not only ask whether a phrase exists. Compare:

1. particle pattern
   - 이/가 vs 은/는
   - 을/를 vs 에/에서/으로
   - 에 걸리다 / 목에 걸리다 / 마음에 걸리다 style differences

2. verb-object fit
   - press, hold, stop, remain, turn, lean, pass, check, avoid, fold, open, close
   - the object must be something the verb can naturally act on

3. subject-predicate fit
   - a map cannot literally pass a town unless the wording makes the route or bus pass
   - a hand can remain, hover, stop, hesitate, or miss timing; choose the verb by action

4. spoken register
   - whether the speaker would actually say it in the given emotional distance
   - whether the line is too formal, translated, explanatory, or poetically inflated

5. lyric usability
   - whether the natural prose candidate can be cut into singable lines without breaking Korean

## web comparison rules
- Do not paste long web text or copyrighted lyric lines.
- Do not copy source phrasing into the lyric.
- Use web results as collocation and register evidence only.
- If web evidence is weak, prefer natural Korean prose and user/team corpus style.
- Exact search with no result is not automatic failure, but it is a warning for fixed expressions.
- Corpus/common expression evidence does not outrank the song's voice when the line is intentionally idiosyncratic and understandable.

## line repair example pattern
Bad compressed line:
```text
손은 한참 그대로였어
```

Intended meaning:
The speaker did not press, but the hand stayed delayed over the phone.

Repair direction:
```text
손은 그 위에 한참 머물렀어
손은 아직 화면 위에 남아 있었어
누르진 않았는데 손이 늦게 돌아왔어
```

Decision rule:
Choose by section rhythm and speaker voice, then test adjacent prose.

## acceptance requirement
Any Korean lyric marked PASS after a complaint about unnatural language must show either:

- internal corpus/team-corpus reasoning, or
- web/corpus comparison for the worst 1-3 lines, or
- a clear reason why the line is intentionally idiosyncratic and still understandable.

## status
Protocol created after user request. Needs promotion into cards 05 and 06.
