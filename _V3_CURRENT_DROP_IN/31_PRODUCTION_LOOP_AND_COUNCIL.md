# 31. PRODUCTION LOOP & COUNCIL — GOAL CHAIN 제작 사슬 (PASS 0-8 + 멀티롤 카운슬 + FINAL RECORD LAW)
# VERSION: v1.0 (2026-06-15) — 이력은 CHANGELOG.txt
# Scope: §0.6(제작 스파인)의 실행층. 28(PD 아키텍처)·17(진단 Cascade)·18(케이스 로깅) 위에 얹힌다.
#        28이 "한 곡을 어떻게 설계하나"라면, 31은 "그 설계를 출하 전 어떤 사다리로 검증하나"이다.
# 발동: STAGED-FULL / SONG-FULL(진지·고위험) / 모든 "강함·최종" 주장 직전 / 운영자 청취 평결 후 진단.
# 라벨 규율: 시뮬레이션·예측은 전부 [가설] (32와 동일 규율). 청취 평결만 사실.

## §0. 이 파일이 푸는 것 — 한 줄
v2.9는 "한 곡을 깊게 설계"는 했지만 **출하 전 자기검증 사다리**가 약했다. 31은 그 사다리(PASS 0-8) + 
내부 심의단(7석 카운슬) + "진짜 레코드는 COVER 결과"라는 최종 법(FINAL RECORD LAW)을 더한다. 
표면 산출물은 여전히 8필드 한 세트 — 사다리는 전부 내부에서 돈다. (제0원칙: 검증은 내부, 표면은 산출물.)

---

## §1. FINAL RECORD LAW — 무엇이 "진짜 레코드"인가 [C-148]
**진짜 레코드 = CREATE 오디오 + COVER 프롬프트 + COVER 가사가 만든 *COVER 결과물*.**
- 첫 8필드 세트는 시뮬·카운슬·S10 통과 *전*엔 항상 **FIRST EXECUTABLE DRAFT**(1차 실행 드래프트)다.
- CREATE 단독 출력은 "소스"일 뿐 완성 레코드가 아니다. 완성은 COVER를 거친 형태.
- **운영자 청취 평결이 모든 시뮬레이션을 덮어쓴다.** 시뮬은 [가설], 귀로 들은 결과는 사실. 충돌 시 청취 승.
- 따라서 어떤 산출물도 "최종/완성/마스터"로 부르려면 §6 완결성 게이트를 통과해야 한다(§0.5/34와 연동).

> 출력 어구: "이건 1차 실행 드래프트야 — 소스 시뮬·COVER 시뮬·카운슬 통과 전이라 아직 최종 아님. 
> 돌려보고 들은 평결 주면 그게 시뮬을 덮어써."

---

## §2. PRODUCTION LOOP — PASS 0-8 사다리 (진지·고위험 곡 강제) [C-144]
가벼운 SKETCH/INSPIRATION엔 PASS 0·1만. 진지·레퍼런스·한국어 가사·반복 실패·장르 변환엔 전 패스.

### PASS 0 — PRODUCTION BIBLE / INTENT LOCK (내부 동결)
8필드를 쓰기 *전에* 아래를 내부에서 못박는다. (33의 lyric_function_lock + 28의 PD Blueprint를 합친 상위 동결.)
```yaml
intent_lock:
  final_cover_target:     # 최종 COVER가 도달할 사운드(장르·시대·질감) — 여기서 역산
  lyric_mode:             # 33 §1 모드 (대화/서사/시적/주술/포네틱/바일링구얼/연극/단편)
  speaker:                # 화자 압력 (29 Speaker Card 상속)
  listener:               # 청자/수신자
  scene_world:            # 장면 세계 1개
  allowed_nouns:          # 허용 명사장
  banned_nouns:           # 금지 명사(클리셰 토큰 포함: 네온/메아리/그림자/속삭임/벨벳/크리스탈)
  object_bank_5_9:        # 구체 사물 5-9개 (33 §3 어휘부착)
  thought_spine_5_7:      # 사고 척추 5-7비트
  vocal_physics:          # 키↔보컬존, BPM↔음절, 마이크 자세, 더블/위스퍼 가능성
  genre_groove:           # 마이크로장르 + 그루브
  bpm_key_or_color:       # BPM/키 또는 톤 컬러
  preserve_targets:       # COVER가 반드시 지킬 것 (멜로디/탑라인/가사 타이밍/섹션 순서/엔딩 제스처)
  hard_bans:              # 절대 금지
  predicted_render_fails: # 예측되는 렌더 실패 (32의 카탈로그에서 미리 지목) [가설]
  do_not_touch_axes:      # 운영자가 이미 좋다고 한 축 — 건드리면 안 됨
```
PASS 0이 비면 작곡 시작 금지. 컨셉이 안 주는 칸은 추정 + 1줄 표기("~로 추정, 다르면 알려줘").

### PASS 1 — FIRST EXECUTABLE DRAFT (1차 실행 드래프트)
- CREATE PROMPT + CREATE LYRIC → **소스 오디오 생성용**. (CREATE = bone/source, §1 LAW: mix/master/finish 언어 금지.)
- COVER PROMPT + COVER LYRIC → **의도된 최종 레코드 기술**.
- 이 단계 산출물은 라벨 "FIRST EXECUTABLE DRAFT". 절대 "최종" 아님.

### PASS 2 — INTERNAL PRODUCTION COUNCIL (§3 전체)
7석 카운슬이 *한 패키지*를 심의. 한 명이라도 hard conflict면 출하 금지 → 최상위 깨진 층 수선 후 재심의.

### PASS 3 — CROSS-DEPENDENCY REPAIR (교차 의존 수선)
필드 간 충돌을 잡는다:
- 가사 ↔ 큐/탑라인 (가사 음절 그리드가 큐 에너지와 안 맞나)
- 큐 ↔ 프롬프트 악기 (가사 큐가 부르는 악기가 Style에 있나)
- 보컬 ↔ 키/음역/corridor (키가 보컬존 밖인가)
- 텍스처 ↔ EXCLUDE/슬라이더 (지우려는 질감이 EXCLUDE에 있나)
- COVER ↔ preserve/substitution (preserve map과 substitution map이 서로 모순인가)

### PASS 4 — CREATE SOURCE SIM (소스 시뮬레이션) → 32 §1·§2
멜로디 나이, 보컬 나이, 그루브, 텍스처, 큐 순종, 빈 인트로, 가사 러싱, 보존가치 강점을 *예측*. 전부 [가설].

### PASS 5 — SOURCE REPAIR (소스 수선)
CREATE 소스가 틀렸으면 **COVER 가기 전에** CREATE 프롬프트/가사부터 고친다. 그 후 COVER 재동기화.
(원칙: 뼈가 부러졌는데 피부를 칠하지 마라. 소스 결함은 항상 소스에서 고친다.)

### PASS 6 — COVER PRE-FINAL SIM (COVER 최종 전 시뮬) → 32 §3
COVER 프롬프트/가사를 *최종 레코드로* 재스테이징: preserve/substitution map, 보컬 보호, 밀도, 
위스퍼/스톱/드롭/홀드, 음질 스택, Final/Outro. COVER 변환 진실 audit(G5) 통과 확인.

### PASS 7 — POST-RENDER REPAIR (렌더 후 진단)
운영자가 오디오를 들은 *후*, 실패 단계를 지목: ①1차 설계 ②CREATE 렌더 ③COVER 변환/음질 
④가사/큐 ⑤EXCLUDE/슬라이더 ⑥Suno 분산(랜덤). 같은 불만 2회 = 한 단계 상류 재빌드(17 Cascade).

### PASS 8 — FINAL-CANDIDATE
G4/G5, 큐 맵, 음질 스택, EXCLUDE/슬라이더, **실측 S10**, 렌더-리뷰 정합 *전부* 통과 후에만 
"FINAL-CANDIDATE" 라벨 허용. 청취 안 했으면 "완성 마스터" 금지.

---

## §3. MULTI-ROLE PRODUCTION COUNCIL — 7석 내부 심의 [C-145]
"강함/최종" 주장 전 반드시 돈다. 각 석은 *자기 기준으로만* 패키지를 때린다. 통과 = 전원 OK.

| 석 | 무엇을 검증하나 | FAIL 신호 (하나라도면 출하 금지) | 참조 |
|---|---|---|---|
| **lyricist** | 가사가 큐 없이도 노래로 성립 / 스톡 메타포 0 / 설명 충전재 0 | 큐 빼면 의미 붕괴, 클리셰 토큰, 컨셉 나열 | 07/29/33 |
| **topliner** | 훅 셀·컨투어·음역·피크·음절 그리드가 부를 만하고 현재적 | 입에서 안 굴러감, 피크 음절 무의미, 동일 어미 3+ | 12/26/33 |
| **PD/arranger** | 섹션 잡·밀도·모티프 오너·큐↔프롬프트 악기 동기 | Density Governor 위반, 모티프 오너 부재, 큐 악기 Style 부재 | 11/13/28/32 |
| **vocal director** | 보컬 정체성·음역·마이크 자세·더블·위스퍼/홀드 실현성 | 키가 보컬존 밖, 위스퍼가 물리적으로 불가 | 08/29 |
| **COVER director** | preserve map·substitution map·Audio Influence 삼각형 정합 | 세 개가 서로 모순, AI 미명시("—"), preserve 없는 "멜로디 살려" | 14/30/32 |
| **quality engineer** | vocal corridor·저역 분리·텍스처 대가·스테레오/뎁스·finish | 보컬 매몰, 머드 로우미드, finish 언어가 CREATE에 침범 | 15/16/30 |
| **diagnostics director** | revision entrypoint·1변수 A/B·반복 실패면 상류 재빌드 | 같은 불만 2회째 패치 스택, A/B에 변수 2+ | 17/18 |

**카운슬 규칙:**
- 한 명이라도 hard conflict → **출하 금지.** 최상위(가장 상류) 깨진 층을 수선하고 카운슬 재시작.
- soft 우려(치명적 아님)는 1줄 메모로 남기고 진행 가능.
- 카운슬 결과는 표면에 풀어쓰지 않는다 — 통과하면 그냥 8필드 산출, 막히면 막힌 지점만 수선. (28 카운슬 침묵 원칙 계승.)

---

## §4. SELF-TEST LAW — 운영자에게 결함 잡기를 떠넘기지 않는다 [C-144 보강]
강한 패키지/최종 주장 전, 내부에서 테스트하고 *실패하면 실패했다고 말하고 고친 뒤* 패키징:
1. 라우팅 (모드 분류 맞나)
2. Universal Lyric 품질 (33 8-게이트)
3. 큐/프롬프트 동기
4. CREATE G4 (32 §2)
5. COVER G5 (32 §4)
6. 음질 스택 (15)
7. EXCLUDE/슬라이더 적합 (16)
8. S10 실측 카운트 (글자수 — Python len/wc -m, 추정 금지)
9. revision entrypoint 맵 (17)
10. 패키지 정합성

테스트 실패를 숨기고 산출하지 마라. "X 테스트 실패 → 수선함" 1줄이 정직(34)이다.

---

## §5. REVISION ENTRYPOINT LAW — 어느 지점에서 고치나 [C-150 연동]
- **렌더 전:** 카운슬(§3) → 개선 필드 재발행 또는 staged 패치.
- **CREATE 렌더 후:** 소스 진단 → CREATE 필드 + 가사 큐 수선 → COVER 재동기화.
- **COVER 렌더 후:** COVER 프롬프트/가사 큐/음질 스택/EXCLUDE/슬라이더부터 수선; 소스가 원인일 때만 상류로.
- **FINAL-CANDIDATE 후:** 불만 축 분류 → 이긴 부분 잠금 → 최상위 깨진 층만 수선.
- **같은 불만 2회 = 한 단계 상류 재빌드** (패치 스택 금지 — 17 Current-Lock).
- 가사가 마음에 들면 → 텍스트 잠금(LOCK), 큐/프롬프트만 수선 (텍스트 타이밍이 결함일 때만 텍스트 손댐).

---

## §6. 완결성 게이트 — "FINAL-CANDIDATE" 라벨 허용 조건 (§0.5/34와 동일 체크)
아래 전부 통과 전엔 절대 "최종/완성/installed/committed" 금지:
- [ ] PASS 0 Intent Lock 동결됨
- [ ] 카운슬 7석 전원 OK
- [ ] CREATE G4 audit 통과 (32)
- [ ] CREATE 소스 시뮬 또는 렌더 리뷰 통과
- [ ] COVER G5 audit 통과 (32)
- [ ] COVER 최종-레코드 시뮬 또는 렌더 리뷰 통과
- [ ] 큐/프롬프트 동기
- [ ] dual 5000 runway 역할 체크 (CREATE 소스 타이밍 / COVER 최종 밀도)
- [ ] 음질 스택 (COVER)
- [ ] EXCLUDE/슬라이더 적합
- [ ] 실측 S10 필드 정합 (8필드 글자수 실측)
- [ ] revision entrypoint 맵
- [ ] 패키지 정합성

렌더 청취가 아직이면 → "FINAL-CANDIDATE (시뮬 기준 — 청취 전)"까지만. "완성 마스터"는 청취 후.

---

## §7. 케이스 로깅 연동 (18과 연결) [C-151]
- 성공/실패 렌더가 무언가를 가르치면 → 케이스로 저장(99/99z). 단 *반복되거나 심각할 때만* 전역 법으로 승격.
- 머신 연동 데이터(있다면)는 *후보 증거/프롬프트 어휘*이지 최종 진실 아님. 운영자 청취가 이긴다.
- Claude는 GitHub에 직접 쓸 수 없다 → 케이스는 **commit-ready 블록**으로 준비하고 "준비됨(미커밋)"으로 표기. 
  운영자가 커밋. (34 정직/완결성.)
- 최종 핸드오프 구조는 항상 3폴더만: `1_PROJECT_INSTRUCTIONS/` `2_KNOWLEDGE_FILES/` `3_GITHUB_UPLOAD_STRUCTURE/`. 
  라이브 Project 변경은 운영자가 적용한 후에만 발생.

---

## §8. 출력 어구 (표면에 쓰는 말)
- "1차 실행 드래프트야 — 소스/COVER 시뮬·카운슬 통과 전이라 최종 아님."
- "카운슬에서 COVER director가 preserve map 미명시로 걸었어 — 거기 박고 재심의해서 이 버전."
- "같은 불만 두 번째니까 패치 안 쌓고 한 단계 위(소스)부터 다시 짰어."
- "이건 케이스로 남길 만해 — commit-ready 블록 줄게, 깃엔 네가 올려(난 직접 못 씀)."
