# 44. VOCAL EMOTION MICRO-DIRECTION — 보컬 감정 미세연출 (감정의 물리적 소리 → Suno 큐)
# VERSION: v1.0 (2026-06-15) — 이력 CHANGELOG.txt
# 근거: 06(보컬)·24(보컬패치)·25(사운드엔진)·§6([Singing:])·§8(큐) + 현행 보컬 감정표현 교습 web 검증(2026-06)
# 위상: 06(보컬 정체성)·§6([Singing:] 7요소)에 *감정의 물리적 소리(브레스·브레이크·프라이·퀴버)*를 더함. 전부 Suno 렌더 큐로.
# 발동: 보컬 감정 연출("더 절절하게/감정 살려/울먹이게/그렁하게/담담하게")·섹션 감정 정점·캐릭터 감정 디폴트.
# ★핵심: 감정은 *음정이 아니라 물리적 소리*에 산다 — 숨, 갈라짐, 떨림, 프라이. 의도적 불완전 = 감정의 '양념'(완벽 기술만으론 안 움직임).

## §0. 원리 — 감정은 몸의 소리다
조이는 톤 vs 브레시 톤, 갈라짐, 떨림, 프라이 — 이게 감정을 나른다. 완벽하게 깨끗한 노래는 차갑다. *의도적 미세
불완전*(살짝 갈라짐·숨 걸림·안 깨끗한 음)이 진정성을 만든다(38 organic-imperfect 연동). 감정 → 물리적 소리 → Suno 큐로 번역.

## §1. 감정-소리 어휘 (물리적 발성 기법 → Suno 큐)
```
기법             무엇/감정                           Suno 큐 (discrete + [Singing:] 서술)
──────────────────────────────────────────────────────────────────
Cry(크라이)      브레스 브레이크 + 크랙, 밝음, 취약함.  [voice cracks slightly] / "cry-break on the high notes,
                 후렴 정점(아델식)                    controlled breath breaks and crackle"
Sob(소브)        떨림/퀴버, 가볍고 에어리하나 깨짐.     "quivering trembling delivery, the voice shakes and
                 (샘 스미스 — 울며 노래)               breaks while staying light and airy" / [trembling]
Vocal fry        저역 그렁그렁 거칠고 까칠.            [vocal fry] / "gravelly vocal fry on the low phrase ends,
                 (브리트니 'oh baby' / 마일리)         raspy gritty lower register"
Breathy          숨 섞인 톤(친밀) ↔ 풀 톤(힘).         [breathy] / "audible breath, breathy intimate tone with
                 둘 섞으면 복합 감정                   space, mixing resonant and breathy"
Quiver/shake     지속음에 떨림 — 강렬한 감정.          "a shake in the sustained notes, the held note wavers"
Vowel 연장       열린 모음 길게(감정 임팩트).          "extended open vowels, lingering on the vowel before the
                 ('time'→'tah-ahm')                  consonant" + 가사 늘림(lo-o-ove, §8)
Belt+strain      파워 + 거친 엣지(절규 직전).          "belted with a raw strained edge, on the verge of breaking"
Whisper-sing     반속삭임(고백·취약).                  [whispered] (Silence 직후만, §8) / "half-whispered intimate"
Deadpan/flat     무감정·체념(평탄 톤).                 "flat deadpan delivery, minimal vibrato, conversational numb"
Yodel/break flip 흉성↔두성 급전환(감정 폭).           "a voice-break flip into falsetto on the peak"
```

## §2. 감정 → 물리적 발성 맵 (어떤 감정에 어떤 소리)
```
감정              물리적 발성 처방 (섹션 정점에 집중)
──────────────────────────────────────────────────────
비통·상심          cry-break + 퀴버 + 숨 걸림 + 고음에서 목소리 얇아짐
그리움·갈망        브레시 + 모음 연장 + 부드러운 다이내믹 스웰
분노·저항          belt+strain + 단단한 자음 + fry에서 파워로
취약·고백          whisper-sing + 들리는 숨 + near-cry(살짝 갈라짐)
환희·해방          밝은 열린 톤 + 다이내믹 상승 + 민첩한 run
무감각·체념        flat deadpan + 미니멀 비브라토 + 브레시
절박·애원          strained belt + cry-break + 점증 강도
관능·친밀          breathy + close-mic + 느린 프레이징 + 낮은 다이내믹
```
→ 감정어 받으면(41 §3) → 화자(29) → *이 표로 물리적 소리 처방* → 섹션 [Singing:]에 박음.

## §3. 다이내믹 미세연출 (스웰·휴지·대비 = 드라마)
- **크레셴도 into 훅** / **급강하 to whisper**(대비) / **핵심 줄 직전 휴지**(긴장) / **swell-and-pull**(밀고 당김) /
  **테라스드 다이내믹**(계단식 강화). 한 곡에 다이내믹 *대비* ≥1(평탄 = 무감정).
- Suno 큐: "swells into the chorus then pulls back" / "drops to a near-whisper on the bridge" / "a held breath before the final line"(§8 휴지 설계 연동).
- 배치: Verse 낮게 → Pre 빌드 → Chorus 정점 → Bridge 급변(드롭 또는 폭발) → Final 최대 → Outro 여운(§5 강약·39 레이어링).

## §4. 프레이징·호흡 = 감정 (어디서 숨 쉬나 = 어디서 느끼나)
- **핵심 단어 직전 호흡** = 기대·머뭇 / **몰아치는 프레이징** = 패닉·격정 / **늘어지는 서스펜션** = 긴장·여운 /
  **비트 뒤 프레이징(behind-beat)** = 피로·체념 / **앞선 프레이징(ahead)** = 다급함.
- Suno 큐: "[Breath] before the key word" / "rushed breathless phrasing" / "behind-the-beat weary delivery" / "lets the note hang".

## §5. 의도적 불완전 — 감정의 '양념' (★완벽 ≠ 감동)
- 살짝 갈라짐·숨 걸림·안 깨끗한 음 = 진정성. 단 *맛깔나게·배치해서*(매 줄 X — 정점 한두 곳).
- Suno 큐: "a slight catch in the voice on the key line" / "voice cracks on the highest note" / "imperfect raw human delivery"(38 §2 organic 연동).
- 캐릭터 시그니처 가능: 그렁한 끝(fry tail)·울먹 후렴(cry chorus)·숨 많은 verse(breathy verse) = 페르소나 식별자(35/§6).

## §6. 리프·런·멜리스마 (보컬 민첩성 = 감정)
- **멜리스마**(한 음절 여러 음) = 갈망·가스펠·R&B·소울 / **절제**(직선) = 인디·포크·담백.
- 배치: 프레이즈 끝·클라이맥스(남발 X). Suno 큐: "melismatic runs at phrase ends" / "a soulful run into the final chorus" / "restrained straight delivery, no runs".
- 장르 매칭: 가스펠/R&B=run 풍부 / 시티팝=깔끔 / 트랩=오토튠 멜로디 / 발라드=클라이맥스 1회.

## §7. Suno 큐 통합 (어떻게 [Singing:]·brackets에 박히나)
- **discrete 태그**(렌더 강): [voice cracks][breathy][trembling][vocal fry][whispered][belted][Held] — 라인 *사이* 실위치.
- **[Singing:] 서술**: "cry-break and audible breath, voice thins at the top, vulnerable" 등 감정 물리음 명시(7요소 안, §6).
- **가사 늘림/CAPS**: 모음 연장 lo-o-ove·외침 CAPS(25 실현 — `*` 단독 X).
- 25(사운드엔진 실현 판정)·§8(큐 device)·06(보컬)와 연동. 큐=기능(묘사 X, §8): "[voice cracks] on '가지마'"처럼 *닿는 줄* 지정.

## §8. 장르·캐릭터 감정-보컬 경향
```
장르/맥락       감정-보컬 디폴트
──────────────────────────────────────────────
소울/가스펠      cry-break·멜리스마·belt strain·풍부한 다이내믹
인디/포크        breathy·deadpan 허용·절제·의도적 미세 불완전
R&B             breathy·run·관능 프레이징·near-whisper
발라드          cry 정점·모음 연장·다이내믹 대비 큼·클라이맥스 belt
록/얼트          belt strain·fry·거친 엣지·raw
트랩/이모랩      오토튠 멜로디·fry·취약 톤·deadpan↔cry 교차
시티팝/팝        깔끔·밝은 톤·민첩·과한 cry 절제
```
→ 캐릭터(35)마다 감정-보컬 시그니처 1-2개 고정(구별화 — fry tail / cry chorus / breathy verse 등).

## §9. 출력 직전 감정연출 체크 (내부, §6/25와 함께)
```
□ 섹션 정점에 감정 물리음(cry/sob/fry/breath/quiver) ≥1 배치?
□ 감정 → 물리 발성 맵(§2) 적용? (감정어 직접 진술 X — 소리로)
□ 다이내믹 대비 ≥1? (평탄 = 무감정 — 스웰/드롭/휴지)
□ 호흡 배치가 감정과 일치? (핵심어 직전 [Breath] 등)
□ 의도적 불완전 1-2곳(정점)? 매 줄 남발 X?
□ 멜리스마/run이 장르 맞나? (가스펠 풍부 / 포크 절제)
□ discrete 태그로 *닿는 줄* 지정(큐=기능)? [Singing:] 감정 물리음 명시?
□ 캐릭터(35)면 감정-보컬 시그니처 일관?
```
하나라도 빠지면 보강 후 출력(표면 보고 X). ★감정은 소리로 — "슬프게"가 아니라 [voice cracks]+[Breath]+모음 연장으로.
