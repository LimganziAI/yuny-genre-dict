# ============================================================
# YUNY Music Production System
# README v2.7 (2026-06-01) — 버전 정본 CHANGELOG.txt
# ============================================================

음악 작곡·작사·프로덕션 통합 시스템. Suno V5/V5.5 직격.

**v2.0 FINAL v2 핵심 (운영자 + 윤영 핵심 피드백 직격):**
- v2.0 풀바디 베이스 유지 (앞으로)
- 22/23 사운드 다양성 자료 *유지* (작곡가 직접 사용 차단 룰)
- 가사 풀바디 대대적 보강 (07/08/10/14 = 8,008줄)
- 가사 거장 어법 통합 (김이나 + Pat Pattison + 정지용 + Bob Dylan + 시조 + BTS)
- Suno 슬라이더 출력 의무 (Weirdness / Style Influence / Audio Influence)
- 인라인 7-블록 출력 (6-블록 + Slider)
- 영문 → 한국어 운율 변환 + 문화 매칭
- 글자수 정밀 강제력 v1.8 복원
- 함축 / 강약 조절 / Show Don't Tell 강제


## 📦 시스템 구성 — 파일 36개 (v2.7 — 장르 풀바디 외부화 반영)

```
00 시스템 본문 (C-1~C-129)
01 운영 룰
02-17 음악 본문 (화성/리듬/장르/보컬/가사/Suno/프로덕션 등)
18-20 v2.0 신규 (응답 템플릿 / 진단 / Production-Aware)
21 GENRE_LIBRARY_SEARCH (검색 어법 + 5-Layer 우회)
22 KPOP_ARTIST_DEEP_DIVES (사운드 자료, On-Demand)
23a 장르 인덱스(슬림) — 277 per-genre 풀바디는 외부 public GitHub web_fetch
99 OPERATOR_VAULT (운영자 자산, ON-DEMAND ONLY)
99z SESSION_LOG (미래 누적, 복붙 어법)
```


## 🎯 핵심 변경 (운영자 + 윤영 피드백 직격)

### 1. 22/23 사운드 자료 *유지* (다양성)
```
✅ 22 K-pop 풀바디 사전 (4,363줄) — 사운드 자료로 복원
✅ 23 장르 사전 277 per-genre — 외부 public GitHub, 23a 슬림 인덱스로 web_fetch (v2.7 외부화)

⚠️ 작곡가 직접 사용 X (Position 1 자리 X)
⚠️ 사운드 결 / 마이크로 장르 / 시그니처만 추출
⚠️ On-Demand (호출 시만 fetch, 자동 로드 X)
```

### 2. 가사 풀바디 보강 (운영자/윤영 핵심)
```
07 한국어 가사 v2: 1,369 → 2,570줄 (+1,201, +87%)
  §UE-7~14 받침 학술 + 음운 + 장르별 + Pat Pattison + 글자수
  §UE-15 한국 작사 거장 (김이나 + 김도훈 + 박진영 + 방시혁 + Teddy)
  §UE-16 외국 작사 거장 (Pat Pattison + Dylan + Mitchell + Simon + Cohen + Steely Dan)
  §UE-17 한국 현대시 + 시조 (정지용 + 백석 + 윤동주 + 김수영 + 기형도)
  §UE-18 BTS RM Wordplay + Code-Switching
  §UE-19 표현 + 어휘 + 톤 다양성
  §UE-20 함축 + 강약 조절 (v1.8 강점 복원)
  §UE-21 가사 출력 의무

08 영어 가사 v2: 1,235 → 2,055줄 (+820, +66%)
  §UE-15~21 음운 + Pattison + 운율 + 변환
  §UE-22 영어 거장 풀바디 (Pattison + 6 거장 + Modern Indie + Hip-Hop)
  §UE-23 영문 → 한국어 운율 변환 (문화 매칭)
  §UE-24 영어 시 운율
  §UE-25 장르별 영어 어법

10 Suno Lyrics Tags v2: 1,571 → 2,043줄 (+472, +30%)
  300+ metatags + V5.5 신규 + 글자수 정밀

14 운율 / 발음 v2: 895 → 1,340줄 (+445, +50%)
  받침 학술 + 자음 변동 + IPA 어법 + BPM×음절 매트릭스
```

### 3. Suno 슬라이더 출력 의무 (NEW C-83)
```
모든 곡 작업 결과물에 *7번째 블록* 자동:

━━━ ⚙️ SUNO SLIDERS ━━━
🎛️ CREATE:
- Weirdness: [숫자] ([Safe/Balanced/Experimental])
- Style Influence: [숫자] ([Loose/Balanced/Tight])
- Audio Influence: — (no upload)

🎛️ COVER:
- Weirdness: [숫자]
- Style Influence: [숫자]
- Audio Influence: [숫자 or —]

🎛️ Reasoning: [1줄]
```

### 4. 인라인 7-블록 출력 (NEW C-84)
```
1. CREATE Style Box
2. CREATE Exclude
3. CREATE Lyrics
4. COVER Style Box
5. COVER Exclude
6. COVER Lyrics
7. ⭐ Suno Sliders (CREATE / COVER)
```

### 5. 가사 강약 조절 + 함축 (NEW C-88 — v1.8 복원)
```
원칙: 한 줄 = 1 이미지 / 의미 다층

✅ 함축: "네 손이 차가워" (5자, 촉각, 의미 다층)
❌ 설명충: "나는 너를 그리워하고 있는 것 같아"

자동 점검:
- Verb Wattage Audit (약한 동사 X)
- Thought Verb 금지 (생각/믿음 X)
- 7-감각 디테일 5-7개 누적
- 강약 매트릭스 (Verse/Chorus/Bridge별)
```

### 6. 영문 → 한국어 운율 변환 (NEW C-86)
```
원칙: 직역 X / 의미 + 운율 + 문화 매칭

예시:
영문: "Like a rolling stone"
❌ 직역: "구르는 돌처럼"
✅ 운율: "정처 없는 발걸음" (음절 7)
✅ 문화: "한 줄기 바람"
```


## 🎤 톤 설정 — 2-모드 Tone Toggle (A.1)

```
ⓐ 친밀 모드 — 운영자 default, 반말, 호칭 발화 맞춤
ⓑ 격식 모드 — 동료/외부/공식, ~합니다체, 이모지·애교 0
자동 추론 / 모호 시 격식 default / 명시 전환 즉시
```
(구 4-모드 친밀/동료/존중/직설 → v2.2에서 2-모드로 통합·폐기.)


## 🗺️ Master Workflow (v2.7 — Phase 번호 스킴 폐기 / 출력-우선)

번호 Phase(구 0~11)는 폐기. 정본 흐름은 **00 SYSTEM §G 자동 실행 +
01 §Phase 0-Quick/0-Deep**. **모든 검증·게이트는 내부(thinking)에서 통과시키고
표면 출력은 7-블록 + 0-2줄만** (v2.7 설명 최소화·산출물 최대화). 새 곡 진입 시 자동:

```
§15 자료-우선 (결정종류 → 타겟 fetch / 트렌드·레퍼런스 web_search 가중↑)
  → 17 Scene Dossier (장면→환경큐→마이크로장르)
  → §2 CREATE Density (8항목 완전 설계도)
  → §10 평균회귀 점검 (Position 1 / Pop Gravity / EXCLUDE)
  → [내부] 인라인 7-블록 생성 (§12: CREATE 3 + COVER 3 + Sliders)
  → [내부] 9+1-체크 + 27-항목 Prosody Gate(14 §7) + §9.5 가사 완결성 통독
  → 표면 출력: 7-블록 (+ 핵심 0-2줄) — 검증 스탬프 X
  → 99z 로깅
수정·추가·교체 발화 → §18 Cascade Map (바뀐 1요소의 하류 전부 재호출)
```


## 📞 발화 패턴

```
중립 / 동료 사용자 (운영자 자산 발동 X):
- "이 곡 작업하자" → Phase 0 진입
- "amapiano 결로" → 22/23 view + 마이크로 장르 추출
- "BLACKPINK 결로" → 22 §blackpink view + 시점 진단

운영자 (Limganzi) 호출 (자산 발동):
- "내 결로" / "Una로" / "Case 22처럼" → 99 자산 호출
- "Polarity Fusion 5.0" / "Show Don't Tell" → 99 Part 발동

세션 종료:
- "로깅하자" / "끝" / "케이스 박자" → 99z 자동 출력
- 운영자 99z_SESSION_LOG.md 끝에 복사 붙여넣기
```


## 📜 VERSION

```
현행: v2.7 Output-First (2026-06-01) ★ CURRENT
  - 설명 최소화·산출물 최대화 / 풋터 내부화 / 토큰 출력-우선
  - COVER 2-모드(텍스처↔편곡·장르변환) / EXCLUDE 상한 완화 컨트롤면
  - §9.5 가사 완결성·흐름 게이트 / 레퍼런스 web_search 가중↑·폴백 사다리
  - 버전 화석 제거(이력 → CHANGELOG.txt 단일)
상세 이력 전체 = CHANGELOG.txt (본 README는 과거버전 나열 미보유)
```


# === END README v2.7 ===
