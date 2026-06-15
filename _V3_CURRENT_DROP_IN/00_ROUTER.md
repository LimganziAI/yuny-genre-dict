# ============================================================
# ★v3.0 GOAL CHAIN: 본 파일은 v2.7 유래 — 정본 동작은 00_SYSTEM_INSTRUCTION(v3.0)이며 충돌 시 그쪽 우선. 출력=8-필드. 신규 레이어 31~36(제작사슬·캐릭터·출력계약) 추가됨. 라우팅은 00 지침 D 인덱스 기준.
# 00_ROUTER.md — System Entry Router (파일 라우팅 맵)
# YUNY v2.7 — 버전·실행룰 정본은 00_SYSTEM_INSTRUCTION + CHANGELOG
# (본 파일은 '어느 파일을 여나' 맵 전용. Phase 번호 스킴 폐기 → 지침 §G + 01 §Phase)
# ★v2.7: 설명 최소화·산출물 최대화 — 검증/게이트 전부 내부, 표면=8-필드+0-2줄.
# ============================================================

사용자 발화 → 시스템이 *어느 파일·룰·SOP*를 발동할지 결정하는
1차 라우터. C-55 (17-type response template) 및 C-54 (11-카테고리
diagnostic)와 통합 운영.


## §1. Always-Load 파일 (모든 응답 시작 전 로드)

```
00_SYSTEM_INSTRUCTION_for_YUNY.txt  ← 상위 오버라이드 (System Instruction)
00_ROUTER.md                         ← 이 파일
01_OPERATING_RULES.md                ← SCP / Brief Lock
```
(※ 23a_GENRE_INDEX_MASTER는 v2.7에서 On-Demand로 강등 — §2.3 참조)

**Always-Load 사이즈(실측):** 00_SYSTEM_INSTRUCTION ~16K + 00_ROUTER ~2K + 01 ~7.5K
≈ **~25K tokens.** (v2.7: 23a ~25K를 On-Demand로 강등 — 장르 안 부르는 세션에서 절반 절약.
장르 발화 시에만 23a 인덱스 → 해당 장르 web_fetch(외부 GitHub). 깊은 장르 데이터는 per-genre 외부 fetch라 품질 손해 0.)


## §2. On-Demand 로드 (호출 트리거 발동 시만)

### §2.1 음악 본문 (16개) — 작업 흐름 따라 view

```
02 HARMONY_FOUNDATIONS    ← 코드/스케일 발화
03 HARMONY_ADVANCED       ← 비다이어토닉 / 리하모
04 RHYTHM_AND_FORM        ← 박/구조 발화
05 GENRE_LIBRARY          ← 장르 발화
06 VOCAL_PRODUCTION       ← 보컬 발화
07 LYRIC_CRAFT_KOREAN     ← 한국어 가사
08 LYRIC_CRAFT_ENGLISH    ← 영어 가사
26 LYRIC_CRAFT_JAPANESE   ← 일본어 가사 (전용 풀바디, §9 LAW)
27 LYRIC_CRAFT_SPANISH    ← 스페인어/라틴 가사 (전용 풀바디, §9 LAW)
09 SUNO_ENGINE            ← Suno 어법 / Style Box
10 SUNO_LYRICS_TAGS       ← Suno 태그
11 PRODUCTION_DESIGN      ← 사운드 디자인
12 PROMPT_TEMPLATES       ← 템플릿 풀
13 REFERENCE_ANALYSIS     ← 레퍼런스 결 분석
14 PROSODY_AND_PHONETICS  ← 운율 / 발음
15 NATURAL_LANGUAGE       ← 자연어 디렉션
16 INSTRUMENT_ARTICULATION← 악기 / 이펙터
17 THEMATIC_CULTURAL      ← 테마 / 캐릭터
```

### §2.2 v2.0 신규 4개 — 라우팅 시 view

```
18 RESPONSE_TEMPLATES     ← 17-type 발화 라우팅
19 DIAGNOSTIC_CHECKLISTS  ← 11-카테고리 진단
20 PRODUCTION_AWARE       ← 7-zone / LUFS / 마스터링
21 GENRE_LIBRARY_SEARCH   ← 검색 어법 + 5-Layer 우회 (작곡가 X)
```

### §2.3 풀바디 사전 (K-pop + 277 장르 · v2.7 외부화)

```
22 KPOP_ARTIST_DEEP_DIVES        ← K-pop 27명 풀바디 (4,363줄)
                                   호출: "[K-pop 아티스트] 결로"

23 사전 (v2.7 외부화 — 프로젝트엔 23a 인덱스만, 본문 277개는 외부 public GitHub):
23a GENRE_INDEX_MASTER  ← 프로젝트 상주 슬림 인덱스. 장르 발화 시 *첫* view → 해당 장르 raw URL 확보 → web_fetch.
본문 277개 (per-genre, 외부 GitHub, 카테고리 폴더별 web_fetch):
  rock-metal       ← Rock/Metal 호출 시
  electronic-dance ← EDM/Electronic 호출 시
  hiphop-rap       ← Hip-Hop/Rap 호출 시
  pop-eastasian    ← Pop/East Asian 호출 시
  rnb-soul-funk    ← R&B/Soul/Funk 호출 시
  jazz-blues       ← Jazz/Blues 호출 시
  country-folk     ← Country/Folk 호출 시
  classical        ← Classical 호출 시
  world            ← World/Latin/Afro 호출 시
  other-specialty  ← 특수/희귀 ★★★★+ 호출 시
```

**Note (v2.7)**: 23 본문(277 per-genre)은 *사전식 슬림본* — Genre Overview / Suno Prompt Keywords / 핵심 Characteristics / Reference Tracks 자리. 외부 public GitHub 상주, 장르별 web_fetch(23a 인덱스의 raw URL). 학술 풀바디 원본은 운영자 zip 백업.

### §2.4 운영자 자산 (🔒 ON-DEMAND ONLY)

```
99_OPERATOR_VAULT.md       ← Limganzi 개인 자산 (호출 시만!)
                              호출 트리거:
                              - "내 결로" / "Limganzi" / "임간지 결로"
                              - "[캐릭터명]" (Una/Sally/봉남이/세리카/체니/마리)
                              - "[Case번호]처럼"
                              - "[패턴명]" (Polarity Fusion / Show Don't Tell / 메타포 엔진)

99z_SESSION_LOG.md         ← 미래 누적 자리 (세션 종료 시 자동 출력)
```

**중요**: 99_OPERATOR_VAULT는 *자동 로드 X*. 사용자 명시 호출 시만 발동.
동료 / 다른 사용자 사용 시 *적용 X*. 동료 본인 자산은 99z에 누적.


### §2.5 v2.1 신규 — 보컬 강제력 (NEW)

```
24 VOCAL_DIRECTION_SUNO_PATCH   ← HookGenius 3-Layer Stack 검증
                                   호출 트리거:
                                   - 혼성/듀엣/그룹 곡 작업 (C-90/C-91)
                                   - "보컬 톤" / "창법" 명시 발화
                                   - 다언어 보컬 컨셉
                                   - 발성 메커니즘 (twang/cry/fry 등)
                                   - Style Box ↔ Lyrics Box 동기화 (C-89)
                                  06_VOCAL_PRODUCTION.md *비중복 보완* (의도적 슬림)
```

### §2.6 v2.6 신규 — 가사 사운드 (NEW)

```
25 LYRIC_SOUND_ENGINE   ← 가사가 '소리로' 들리게: Suno 실현 판정표 +
                          영어 연음 엔진 + 강세·딕션·flow 정본.
                          호출 트리거:
                          - "가사 흐름/연음/발음/강세/세련된 표현"
                          - 번역 후 가사 (음절경계 깨짐 → 연음 재점검)
                          - 수정단계 사운드 (지침 §18 연동)
                         06/07/08/10/14 *통합·라우팅* (중복 X)
```


## §3. Phase 0 — 발화 라우팅 (NEW v2.0)

사용자 발화 들어옴 → 시스템 즉시 분류:

### §3.1 Session Mode 8-toggle 인식 (C-51)

| Mode | 발화 신호 |
|---|---|
| ① Composition | "이 곡 만들자" / 곡명 + 컨셉 |
| ② Diagnostic | "왜 이래" / "안 돼" / "이상해" |
| ③ Inspiration | "트렌드" / "강의" / "요즘 핫한" |
| ④ Reference Analysis | "OO곡처럼" / 레퍼런스 입력 |
| ⑤ Revision | "바꾸자" / "다듬어줘" |
| ⑥ Critique | "어때" / "평가해" |
| ⑦ Brainstorm | "아이디어 줘" / 모호 발화 |
| ⑧ Teaching | "왜?" / "설명해줘" |

### §3.2 17-type Response Template 매칭 (C-55 → 18)

사용자 발화 → 18 RESPONSE_TEMPLATES §[해당 type] 라우팅.

### §3.3 11-카테고리 Diagnostic (C-54 → 19)

진단 발화 → 19 DIAGNOSTIC_CHECKLISTS §[해당 카테고리] 라우팅.

### §3.4 사용자 식별 (A.0)

```
운영자 호출 발화 검색:
- "내 결로" / "Limganzi" / "임간지" / 캐릭터명 / Case번호 / 패턴명

발견 → 99_OPERATOR_VAULT 발동
미발견 → 중립 default (운영자 자산 X)
```


## §4. Workflow (정본 위임)

워크플로 Phase 번호는 **01 §Phase 0-Quick/0-Deep + 지침 §G 트리거**가 정본.
본 파일은 번호 스킴 보유 X (구 0~10 폐기 — README 0~11과 충돌했음).
핵심 자동 발동만: §15 자료-우선 → 17 Scene → §2 CREATE Density → §10 평균회귀
→ 8-필드(§12) → 9-체크리스트 → 99z. 수정 발화는 지침 §18 Cascade.


## §5. Reference Deep Research 자동 발동 (NEW v2.0 FINAL)

사용자 "OO곡 결로" / "[아티스트] 결로" 발화 시 자동:

```
C-73 Time-Anchored Context Selector
  → 시점 진단 자동 발의 (ⓐ-ⓔ)

C-76 Member-Solo vs Group 분기
  → 멤버명 단독 → 솔로 추정
  → 그룹+멤버 → 회의 발의

C-77 시기별 프로듀서 추적
  → 22 view → 시기별 프로듀서 맵 추출

C-74 Deep Research Pipeline 4-Stage
  → Stage 1: 내부 자산 (22/23/21)
  → Stage 2: Web Search (불확실 자리)
  → Stage 3: 곡 자체 분석 (URL 제공 시)
  → Stage 4: 5축 → Suno 변환
```


## §6. Tone Toggle (A.1)

**2-모드** (v2.2~): ⓐ 친밀(운영자 default) / ⓑ 격식(동료·외부·공식).
자동 추론, 모호 시 격식 default. 명시 전환 즉시. (구 4-모드 폐기)


## §7. SCP (Session Continuity Protocol)

01 §7-9 참조. 5턴마다 Drift Check 자동.


## §8. EXCLUDE Auto-Inject (NEW v2.0 FINAL — C-75)

Style Box 출력 직전 자동 강제 박음:
- Tier 1: Anti-drift (절대 자동)
- Tier 2: 컨셉 보호 자동 발의
- Tier 3: Pop Gravity Well 차단
- Tier 4: V5 Token Bias 8단어 점검
- Tier 5: 시점 anchor 위반 차단


## §9. 세션 종료 자동 (C-23)

사용자 "로깅하자" / "끝" / "케이스 박자" 발화 시:
- 99z_SESSION_LOG.md §[자동 번호] 블록 출력
- 사용자가 99z 끝에 복사 붙여넣기


# ============================================================
# END OF 00_ROUTER.md (v2.7)
# ============================================================
