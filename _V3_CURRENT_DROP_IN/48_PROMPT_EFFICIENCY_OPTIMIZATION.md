# 48. PROMPT EFFICIENCY & OPTIMIZATION — 프롬프트 효율 최적화 (신호/char 극대화)
# VERSION: v1.0 (2026-06-15) — 이력 CHANGELOG.txt
# 근거: §3(Style 작법)·§5(글자수)·37(현대편곡 §7-PRE 구절효율)·§10(평균회귀) + 현행 Suno 프롬프트 가중·구조 web 검증(2026-06)
# 위상: §3(프롬프트 *쓰기*)·§5(글자수 *한도*)에 *드래프트를 받아 신호/char를 극대화하는 최적화 패스*를 더함 — 알고리즘 레이어.
# 발동: 프롬프트 드래프트 완성 후 출력 직전(내부 1패스)·"왜 generic/muddy"·char 초과·효율 요청.
# ★핵심: 길이 ≠ 품질. 적재적소 specificity + 프론트로딩 + 중복 제거 = 효율. 같은 말 두 번 = 낭비. 토크나이저는 *앞*을 무겁게 읽는다.

## §0. 원리 — 더 길게가 아니라 더 정확히, 앞에
descriptor를 더 쌓으면(12단어+) Suno가 방향 혼란 → muddy. 4개 정밀 단어가 12개 일반 단어를 이긴다. 효율 = (a)정보
가중 높은 걸 (b)앞에 두고 (c)중복·filler를 쳐내는 것. 이 파일은 드래프트에 *최적화 패스*를 거는 알고리즘(§3 쓰기와 별개).

## §1. descriptor 정보-가중 랭킹 (load-bearing / reinforcing / filler)
```
등급            정체                              처리
──────────────────────────────────────────────────────
LOAD-BEARING    장르/마이크로장르+시대, 보컬 캐릭터  Position 1 + 첫 200자 필수(나머지 해석 좌우)
(뼈대)          (보컬곡), BPM/Key — 숫자 앵커       
REINFORCING     무드(2-3), 구체 악기, 프로덕션 결    중간 배치(뼈대 보강, 단독으론 약함)
(보강)          
FILLER (컷)     vague adj(cool/nice/good/amazing/    *삭제* — 토크나이저에서 0 가중, 자리만 낭비
                modern/full band)·동의어 중복·문장형  
```
→ 최적화 = LOAD-BEARING 앞으로, REINFORCING 뒤로, FILLER 제거.

## §2. 프론트로딩 / Position 가중 활용 (★토크나이저는 앞을 무겁게)
- 토크나이저가 *앞을 무겁게* 처리 → Position 1 = *이 곡의 가장 load-bearing 요소*. 장르주도곡=장르 / 보컬주도곡(발라드·R&B·인디·듀엣)=보컬 먼저(§3).
- 시대 앵커 > 장르 라벨("indie rock" < "early 2000s garage rock revival raw production"). 시간 참조에 더 정밀 반응.
- Position 5→1 이동만으로 정확도 상승(검증). 묻히면 약해진다.
- **★Truncation-safe(중요):** Suno v5.5 style 필드 *유효 처리 구간이 짧을 수 있음*(보고상 ~200자 효과적, 초과분 silently ignored 가능성). → **load-bearing을 첫 200자에 전부 몰아** truncation돼도 핵심은 박히게. 그 뒤 detail은 *보강 보너스*. (§8 Dense 화해.)

## §3. 중복 제거 (★효율의 핵심 동작)
- *두 descriptor가 같은 말*이면 하나 컷("dark"+"moody"+"melancholic" → 1개). 동의어 스택 = 낭비.
- 무드 겹침·반복 개념·Style↔Lyrics 중복(§3 ④) 탐지 → 압축.
- 모든 단어가 *distinct dimension* 추가해야(장르/템포/무드/악기/보컬/시대/시그니처 각 1). 안 그러면 컷.

## §4. 정밀 앵커 — 숫자 > 모호 (Suno는 숫자에 강함)
- "120 BPM" > "medium tempo" / "3:30 track" > "standard length" / "Rhodes+upright bass" > "full band" / "B minor" > "minor key".
- 숫자·구체명이 모호성을 줄여 정확도↑. 모호어는 가중 0(§1 filler).

## §5. 무드/장르 캡 (dials, not switches)
- **무드 2-3개**(Suno가 하나의 감정 평균으로 블렌딩). 모순 무드("dark"+"euphoric"="moody" — 안 시킨 출력) 금지. 일관 스택만(brooding+slow+introspective).
- **장르 1-2개**(지배 먼저), 마이크로장르 > 거시(§10). 3개+ 모순 → 섹션 분리/융합(45).

## §6. ★최적화 패스 알고리즘 (드래프트 → 최적화, 내부 1패스)
```
1. 스캔: 각 descriptor를 load-bearing/reinforcing/filler로 점수
2. 컷: filler(vague adj·문장형) + 중복 동의어 제거
3. 재정렬: load-bearing → Position 1 + 첫 200자 / reinforcing → 뒤
4. 코어 확인: distinct 차원 4-7개가 앞에 확실히(detail은 그 뒤 보강=Dense)
5. 정밀화: 모호어 → 숫자/구체명(BPM·Key·악기명)
6. 필드 규율: Style=음향만 / Lyrics=가사+메타태그 / 부정어=EXCLUDE(§4) 분리 확인
7. 캡: 무드 2-3·장르 1-2·악기 3-4(초과 시 약한 것 컷, §3)
```
→ 결과: 같은 정보가 *더 적은 고가중 char*에. (§5 글자수·37 §7-PRE 구절효율과 연동.)

## §7. 가사 효율 (Lyrics 필드)
- **각 섹션 첫 줄 = 가장 강한 줄**(Suno가 오프닝 줄에 최대 멜로딕 가중). 강한 줄 먼저.
- verse 4-8줄(짧을수록 타이트 멜로디) / chorus 2-4줄(짧을수록 catchy 훅, 47 연동) / 후렴 반복 ≤3회(초과=패딩 느낌).
- 다양한 줄 길이(리듬 흥미). BPM×음절(§5) 준수.

## §8. ★Dense(700-950)와 화해 — "프론트로딩된 Dense"
- 우리 시스템 Dense Style Box(700-950, §5)는 *정교/검증결 재현*용. 효율 최적화는 *대체가 아니라 정렬*:
  → load-bearing 4-7 코어를 *첫 200자 고가중 구간*에 truncation-safe로 박고, 그 뒤 detail(악기 디스크립터·프로덕션·throughout)을 보강으로.
  → 즉 Dense여도 *앞이 자급자족*(첫 200자만 읽혀도 핵심 곡 성립) + 중복/filler 0.
- Tight(250-350, §3)는 그 자체로 고효율 — sketch/다양성 시. Dense는 정밀 재현 시(앞 정렬 필수).
- 어느 쪽이든 §6 패스 적용 — filler·중복은 길이 무관 제거.

## §9. 출력 직전 효율 체크 (내부, §3/§5와 함께)
```
□ filler(vague adj·문장형·full band) 0? (토크나이저 가중 0 = 낭비)
□ 중복 동의어 컷? (같은 말 두 descriptor X)
□ load-bearing(장르+시대·보컬·BPM/Key) 첫 200자에? (truncation-safe)
□ Position 1 = 이 곡 최강 load-bearing(장르 또는 보컬)?
□ 모호어 → 숫자/구체명? (120 BPM·Rhodes·B minor)
□ 무드 2-3·장르 1-2(지배 먼저)·악기 3-4? (초과 컷)
□ 필드 분리(Style 음향/Lyrics 가사메타/EXCLUDE 부정)?
□ Dense면 앞이 자급자족? 각 섹션 가사 첫 줄 최강?
```
하나라도 걸리면 최적화 후 출력(표면 보고 X). ★효율 = 고가중을 앞에, 중복·filler는 컷 — 같은 비전을 더 적은 char로 정확히.
