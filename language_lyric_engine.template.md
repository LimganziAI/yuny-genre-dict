# language_lyric_engine.template.md — 신규 언어 온보딩 템플릿
경로 후보: `knowledge-evolving/lyric-expression-banks/language_lyric_engine.template.md`
새 언어 가사 작업은 이 템플릿이 채워지기 전 출하 금지 (카드 07).

```yaml
language:
core_prosody_unit:        # 음절/모라/강세 — 셈의 단위
register_map:             # 화자 레지스터 선택지 + 곡당 1개 규칙
common_lyric_idioms:      # 그 언어 가사에서 실제로 부르는 관용 표현 (검증된 것만)
forbidden_translationese: # 영어→해당 언어 직역 패턴 블랙리스트
rhyme_assonance_system:   # 그 문화권의 라임/유사음 체계와 위계
hook_vowel_strategy:      # 지속음에 강한 모음 / 피해야 할 음
cultural_cliche_guard:    # 그 문화권 AI-클리셰 금지 목록
research_requirement:     # 무엇을 반드시 웹으로 검증하는가 (현행 구어/세대 어법)
acceptance_tests:         # 이 언어 전용 AT 1-2개
```

작성 예 (EN 축약): core=stress-syllable / register=conversational vs literary 선결 / idioms=실사용 검증만 / translationese=한국어식 조사 직역 영문 금지 / rhyme=perfect<family<assonance 위계 / hook=long open vowels / cliché=fire-desire·rain-pain 류 / research=세대 슬랭 웹 검증 / AT=stress-on-strong-beats 검사.
