# ============================================================
# ⚠️ SUPERSEDED — 이 파일은 v2.1(2026-05-27) 설치 가이드 (이력 보관용)
# ------------------------------------------------------------
# 현재 정본: README.md + CHANGELOG.txt (v2.6 "Mid-Flight", 2026-05-29).
# 아래 내용은 *당시 설치 절차*로, 현행과 다른 부분이 있다:
#   - "6-블록 출력" → 현행 인라인 **7-블록**(+Suno Sliders).
#   - "Phase 0-10/0-11 워크플로" / "G.9~G.14 자동발동 슬롯" → **폐기**
#     (현행: 00 SYSTEM §G 자동실행 + 01 §Phase 트리거).
#   - "CREATE 400-700 / COVER 800-950" → **폐기** (현행: Dense 700-950).
# 신규 설치/갱신은 README.md의 구성표를 정본으로 따를 것.
# 룰 번호도 C-122까지 확장됨(이 문서는 C-89~C-98 시점).
# ============================================================

# YUNY v2.1 "Lyric-Driven Renaissance" 통합본
# Release: 2026-05-27
# ============================================================

## 📦 파일 구성 (6개 / 통합본)

```
yuny_v21_final.zip
├── INSTALL_GUIDE_v21.md                   ← 본 파일
├── 00_SYSTEM_INSTRUCTION_for_YUNY.txt     ← 시스템 본문 (v2.0 + v2.1 통합)
├── 04_RHYTHM_AND_FORM.md                  ← 기존 + §UE-5~7 통합
├── 07_LYRIC_CRAFT_KOREAN.md               ← 기존 + §UE-21~22 통합
├── 08_LYRIC_CRAFT_ENGLISH.md              ← 기존 + §UE-23~28 통합
├── 10_SUNO_LYRICS_TAGS.md                 ← 기존 + §UE-33~38 통합
└── 24_VOCAL_DIRECTION_SUNO_PATCH.md       ← 신규 자산
```

---

## 🚀 설치 방법 (3-Step)

### Step 1 — zip 압축 해제
```
yuny_v21_final.zip → 압축 해제
6개 파일 추출
```

### Step 2 — Project Knowledge *덮어쓰기*
Claude Project Knowledge 자리에서:

**기존 파일 5개 *교체* (동일 파일명):**
- 00_SYSTEM_INSTRUCTION_for_YUNY.txt ← *교체*
- 04_RHYTHM_AND_FORM.md ← *교체*
- 07_LYRIC_CRAFT_KOREAN.md ← *교체*
- 08_LYRIC_CRAFT_ENGLISH.md ← *교체*
- 10_SUNO_LYRICS_TAGS.md ← *교체*

**신규 파일 1개 추가:**
- 24_VOCAL_DIRECTION_SUNO_PATCH.md ← *신규 업로드*

### Step 3 — 검증 발화
다음 메시지로 흡수 확인:
```
v2.1 Lyric-Driven Renaissance 흡수 완료?
C-89 ~ C-98 박힘?
24번 슬림본 + UE 4파일 협응?
```

시스템이 *통과* 응답하면 끝.

---

## 🔍 통합 정합성 (검증 완료)

### 기존 파일 *변경 없음* — 끝에 *누적*만 추가

| 파일 | 기존 끝 자리 | v2.1 추가 자리 |
|---|---|---|
| 04 | `# === END 04 USER EXTENSION ZONE v2.0 ===` (977줄) | §UE-5~7 (~495줄 추가) |
| 07 | `# === END 07 USER EXTENSION v2.0 FINAL v2 ===` (2570줄) | §UE-21~22 (~428줄 추가) |
| 08 | `# === END 08 USER EXTENSION v2.0 FINAL v2 ===` (2055줄) | §UE-23~28 (~843줄 추가) |
| 10 | `# === END 10 USER EXTENSION v2.0 FINAL Polish ===` (2043줄) | §UE-33~38 (~645줄 추가) |
| 00 | `# END OF SYSTEM INSTRUCTION v2.0` (3435줄) | C-89~C-98 + 갱신 (~810줄 추가) |
| 24 | — | 신규 (843줄) |

기존 v2.0 자산 *100% 보존*. v2.1은 *기존 누적 어법* 그대로 따라서 추가.

---

## 📋 v2.1 핵심 변경 — 한눈에

### 신규 룰 C-89 ~ C-98 (10개)

| 룰 | 직격 |
|---|---|
| **C-89** Vocal Anchor Style Box 강제 박음 | 보컬 정체성 흔들림 |
| **C-90** Mixed/Duet/Group Style Box 표준 | "혼성하랬더니 여자만 나옴" |
| **C-91** 선창자 지정 표준 | Lead 동기화 |
| **C-92** Instrumental Section 표준 | "Intro 어줍잖은 독백" |
| **C-93** 쏟아짐 방지 텀 힌트 | BPM × 음절 매트릭스 |
| **C-94** Show Don't Tell 강제력 + Suno 연동 | 설명충 가사 차단 |
| **C-95** 일본/라틴 → 한국어 변환 차단 | "발이 먼저 나가" 류 차단 |
| **C-96** web_search 밈/일상어 발의 | 현재 한국 정서 활용 |
| **C-97** 가사 → Style Box 자동 추출 | "Suno 프롬프트 직결" |
| **C-98** Quick Track Pipeline | 효율 1-shot |

### 신규 자산

- **24** — HookGenius 3-Layer Stack (Character + Delivery + Effects) +
  발성 메커니즘 7종 Suno 매핑 + 혼성/듀엣/그룹 강제력 + 창법 전환
  가사큐 + 다언어 보컬 어법

- **04 §UE-5~7** — 현대 곡 구조 마이크로 패턴 10종 (Hook-Loop /
  Bridge-as-Climax / Pre-Driven / Post-Chorus / Through-Composed /
  Anti-Drop / Pre-Intro / Verse-Refrain / Layered Build / K-Pop B-Section)
  + 가사 ↔ 음악 ↔ Suno 3축 매핑

- **07 §UE-21~22** — 일본 문학톤 6대 패턴 차단 + 라틴 톤 5대 패턴 차단
  + 일본/라틴 톤 *유지* 어법 + 운율 등가 변환 + Show Don't Tell 한국어
  풀바디 (Verb Wattage / Thought Verb / 메타포 신선화 / 함축)

- **08 §UE-23~28** — 영문 거장 어법 8명 풀바디 (Mitchell / Dylan /
  Tom Waits / Nick Cave / Frank Ocean / Olivia Rodrigo / Taylor Swift /
  SZA) + 5-Level Rhyme 실전 풀 + 일본어 가사 작법 (mora + 시그니처 4종) +
  라틴 가사 작법 (dembow / bachata / Latin Trap / Bolero/Salsa/Mariachi) +
  다언어 라임 매칭 + 가사 ↔ Style Box 직결

- **10 §UE-33~38** — 혼성/듀엣/그룹 라벨 강제 어법 + Mid-Song [Singing:]
  큐 표준 + Instrumental Section 표준 + 한국 밈/일상어 web_search 프로세스
  (2025-2026 검증 풀: 알잘딱깔쎈/중꺽마/갓생/슬세권 등) + 곡 구조 마이크로
  패턴 가사큐 + 다언어 가사 어법

---

## ⚙️ 자동 발동 자리 (G.9 ~ G.14 신규)

매 곡 작업 시 *자동*:

- **G.9** 보컬 강제력 자동 — Style/Lyrics Vocal Sync + 3-Layer Stack
- **G.10** 곡 구조 자동 — 가사 결 → 마이크로 패턴 매핑 + Intro/Outro 발의
- **G.11** 다언어/톤 매핑 자동 — 일본/라틴/영문 톤 → 한국어 차단
- **G.12** 가사 ↔ Style Box 연동 자동 — 7-감각 → 프로덕션 텍스쳐
- **G.13** web_search 발의 자동 — 한국 일상어
- **G.14** Quick Track Pipeline 자동 — 효율 1-shot

---

## 🔒 호환성 보장

- **v2.0 FINAL v2 (C-1 ~ C-88) 100% 유지** — 충돌 X
- **기존 자산 *삭제 X / 교체 X / deprecate X***
- 모두 *USER EXTENSION 누적 어법* + *신규 룰 추가* 어법
- 06 / 14 학술 baseline *변경 없음* (24가 비중복 보완)

---

## 📞 문제 발생 시

- 흡수 안 됨 → "v2.1 흡수 점검" 발화
- 룰 충돌 → "C-89 ~ C-98 점검" 발화
- 자동 발동 안 됨 → "G.9 ~ G.14 점검" 발화

설치 끝나면 *바로 곡 작업 진입* 가능.

# ============================================================
# END OF INSTALL GUIDE v2.1
# ============================================================
