# ============================================================
# 21_GENRE_LIBRARY_SEARCH.md
# YUNY v2.0 FINAL Polish — Genre / Reference Search Library
# 작곡가 어법 X / 검색 우선 / 유명 아티스트만
# Release: 2026-05-26
# ============================================================

## §운영 원칙

```
❌ 안 박는 것:
- "[작곡가] style" 어법 (Teddy Park style 등 자동 박지 마)
- 일반 작곡가 의존 어법 (운영자가 명시한 매우 유명한 케이스만)

✅ 박는 것:
- 마이크로 장르 + 시대 + 시그니처 음향 (음악적 디렉션 first)
- 운영자가 *명시한 매우 유명한 아티스트* (예: Beatles / MJ / Bruno Mars)
- web_search 자동 발동 (특정 곡/아티스트 분석 필요 시)
- 5-Layer 우회 어법 (Producer Name 자리는 *우회 옵션*)
```


## §호출 트리거

```
사용자: "[아티스트] 결로" / "OO곡 결로"
  ↓
시스템 자동:
1. 운영자 명시 매우 유명한 아티스트 (Beatles / MJ 등) → 직접 박음 가능
2. 그 외 → web_search 발동:
   - 공신력 출처 (Wikipedia / Pitchfork / Rolling Stone)
   - 정의 / 시그니처 / 대표곡
3. 결과 → 5축 분해 (13 §3)
4. 5-Layer 우회 변환 (작곡가 자리는 *Layer 1 - 우회 옵션*)
5. Style Box 적용
```


## §5-Layer 우회 어법

```
Layer 1 (옵션): Producer Name (운영자 명시 매우 유명한 케이스만)
Layer 2: Genre + Era (마이크로 장르 + 시대)
Layer 3: Sound Trait (음향 특성)
Layer 4: Vocal Description (보컬 묘사)
Layer 5: Production Style (프로덕션 결)

원칙: Layer 1은 *옵션*. 안 박아도 Layer 2-5만으로 안전.
운영자가 "[유명 아티스트] 결로" 명시 시만 Layer 1 활성화.
```


## §안전 통과 아티스트 케이스

```
✅ Direct Artist Name 안전 통과 (검증된 케이스):
- Mrs. GREEN APPLE, YOASOBI, Tatsuro Yamashita (일본)
- Bruno Mars-style (안전)
- MJ-style, PinkPantheress era, Charli XCX Brat era (-style/-era 접미사)
- Beatles (역사적)
- David Bowie (시대 명시 시)

❌ 위 외 모든 아티스트는 default 우회 어법:
- Layer 2-5 어법으로 변환
- 또는 web_search → 5축 분해 → Style Box
```


## §장르 검색 어법

```
운영자 발화: "[장르] 결로"
  ↓
시스템 자동:
1. 23 풀바디 사전 X (v2.0 FINAL에서 다이어트 삭제됨)
2. web_search "[장르명] genre music characteristics"
3. 공신력 출처:
   - Wikipedia (정의)
   - Pitchfork / Rolling Stone / RYM / AllMusic (분석)
   - HookGenius / SongFacts (현재 트렌드)
4. 결과 → 13 §3 5축 분해:
   Axis 1 Vocal / Axis 2 Harmonic / Axis 3 Acoustic /
   Axis 4 Temporal / Axis 5 Lyric
5. 마이크로 장르 + 시대 + 시그니처 추출
6. Style Box 적용 (Position 1 — 음악적 디렉션 first)

장르 분류 어법 (검색용 카테고리):
- Rock & Metal (alternative / indie / shoegaze / metal 등)
- Electronic & Dance (EDM / house / techno / UK garage 등)
- Hip-Hop & Rap (trap / drill / boom-bap / plugg 등)
- Pop & East Asian Pop (K-pop / J-pop / hyperpop 등)
- R&B / Soul / Funk / Disco
- Jazz & Blues
- Country & Folk
- Classical / Opera / Orchestral
- World / Latin / Afro / Reggae / Caribbean
- 특수 (cinematic / soundtrack / video game music 등)
```


## §Reference Deep Research Pipeline (C-74)

```
운영자 "OO곡 결로" 발화 시 4-Stage 자동:

Stage 1: 내부 자산 점검
  - 13 REFERENCE_ANALYSIS §2.1 Confidence Self-Check
  - BPM/Key/코드/시그니처 확실? → 직접 박음
  - 불확실 → Stage 2

Stage 2: Web Research (불확실 자리만)
  - 공신력 출처 우선
  - 곡 발매 연도 / 프로듀서 / 작곡가 / 장르

Stage 3: 곡 자체 분석 (URL 제공 시)
  - BPM / Key / 구조 / Signature Moments
  - 5-element 보컬 / 악기 인벤토리

Stage 4: Suno 프롬프트 변환
  - 5축 → CREATE/COVER
  - Position 1 자리 마이크로 장르 + 시대
  - Pop Gravity 차단 EXCLUDE
  - 시점 anchor 의무
```


## §Time-Anchored Context (C-73)

```
운영자 "[아티스트] 결로" 발화 시:
"이 아티스트는 시점에 따라 결이 다른데, 어느 시점?

ⓐ 데뷔/초기
ⓑ 전성기/대표작
ⓒ 최근 활동
ⓓ 특정 곡/앨범
ⓔ 특정 멤버 솔로"

자동 추론:
- 곡 제목 명시 → ⓓ
- 멤버 솔로 → ⓔ
- 연도 명시 → 해당 시점
- "최근/요즘/신곡" → ⓒ
- "옛날/데뷔" → ⓐ
```


## §Member-Solo vs Group 분기 (C-76)

```
"BLACKPINK 결로" → 그룹 default
"BLACKPINK Rosé 결로" → 회의 발의 (그룹 ⓐ vs 솔로 ⓑ)
"Rosé 결로" (그룹명 없이) → 솔로 default 추정
"APT" / "rosie" 등 곡 명시 → 솔로 자동
"최근/신곡" → 솔로 활동기 자동

각 분기 시 web_search → 시점별 프로듀서 / 장르 / 사운드 추출
```


## §EXCLUDE Auto-Inject (C-75)

```
참조 곡 결로 작업 시 자동 EXCLUDE:
- Tier 5 시점 anchor: 이전 시기 결 차단
  예: "Rosé 2024-2025" → EXCLUDE: "Teddy Park signature, fierce EDM trap"
- Tier 1 Anti-drift: 모든 COVER 자동
- Tier 3 Pop Gravity Well 차단
```


# === END OF 21 (Slim Edition) ===
