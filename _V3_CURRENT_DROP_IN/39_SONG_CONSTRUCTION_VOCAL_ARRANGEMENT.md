# 39. SONG CONSTRUCTION & VOCAL ARRANGEMENT — 곡 구성·보컬 편곡 지식 (전부 Suno 큐 매핑)
# VERSION: v1.0 (2026-06-15) — 이력 CHANGELOG.txt
# 근거: 04(리듬·구조)·06(보컬)·§7(컨투어)·§8(큐) + 현행 작곡/편곡/보컬 프로덕션 web 검증(2026-06)
# 위상: 04(구조 이론)·06(보컬 정체성)를 *작곡 구성 + 보컬 편곡 레이어* 차원으로 심화. 전부 Suno 렌더 큐로 번역.
# 발동: 곡 구조 설계 / "섹션 어떻게"·"전환 밋밋"·"후렴 더 크게"·"보컬 얇다·풍성하게"·"화음 넣어"·포스트코러스·애드립.
# 핵심: ①섹션 = *라벨이 아니라 기능* ②에너지 = *섹션 교체가 아니라 레이어 가감* ③보컬 = doubling(두께) ≠ harmony(색).

## §0. 두 원리
1. **섹션은 기능이다.** intro=낮은 에너지로 mood 확립 / verse=이야기 전진 / pre-chorus=*램프*(긴장 빌드, 훅 가리킴) /
   chorus=페이오프 / post-chorus=훅 태그(바이럴 자리) / bridge=귀 리프레시(최종 후렴이 가장 세게 떨어지게) / outro=마지막 인상.
2. **현대 에너지 = 레이어 가감.** 섹션을 바꾸지 말고 *레이어를 더하고 빼라* — 화음 스택 추가, 옥타브 추가, 드럼 드롭,
   필터 오픈. "목적지의 나열이 아니라 여정"으로. Suno는 레이어 이벤트를 큐로 받는다.

## §1. 섹션 기능 맵 (각 섹션의 JOB + Suno 큐)
```
섹션          JOB(기능)                              Suno 큐 / 주의
──────────────────────────────────────────────────────────────────
Intro        mood·tempo·key 확립, *낮은 에너지*,      [Short Instrumental Intro: 2 bars] / EDM=드럼+베이스만
             과하지 않게. EDM은 더 비움.              V5 자동확장 주의 → bar 명시 or [Verse 1 8] 직접
Verse        이야기 전진, *낮은 에너지*(대비 여지),    V2는 V1을 *전복/증폭*(§9.5) — 같은 가사 X
             각 verse 새 가사
Pre-Chorus   ★램프 — 긴장 빌드 + 훅 가리킴.            [Building] + 리듬/화성/멜로디 ramp.
             verse나 chorus 코드 조각 재사용(친숙)     bridge와 혼동 금지(pre=훅 앞 / bridge=후렴 뒤 반전)
Chorus       페이오프, 훅 front-load, *최고 에너지*    훅 라인 앞 2-4줄 응집(§8) / [Belted]
Post-Chorus  ★훅 태그·확장 = *바이럴/TikTok 자리*.     [Post-Chorus] catchy instrumental hook or vocal chant.
             bridge 없을 때 특히 유용                  후렴 직후 짧은 훅 모먼트(가사 적거나 vocal chop)
Bridge       귀 리프레시 → 최종 후렴 최대 임팩트.       ★분류: breakdown(스트립다운) [Band drops out]/[Drums cut]
             *같은 곡 안의* 반전                        vs lyrical-twist(새 의미). 2개면 각자 다른 기능
Outro        마지막 인상 — 전략적(태그/포스트코러스/    [Outro]/[End] 필수. 페이드는 스트리밍 시대 *절제*
             페이드 절제)
```
**무브릿지(VCVC) OK:** bridge 생략 시 대비를 *편곡 변화·post-chorus·outro 태그*로 보강(§2).

## §2. 편곡 레이어링 = 에너지 엔진 (★현대 핵심 — 섹션 교체 대신 레이어)
좋은 편곡은 섹션을 갈아끼우지 않고 *레이어를 쌓고 벗긴다*. 이게 모던 사운드의 핵심 — 에너지 곡선을 레이어로 그린다.
```
에너지 무브            Suno 큐 (Lyrics box, [Singing:] 안 또는 섹션 큐)
─────────────────────────────────────────────────────────────
빌드(쌓기)            "layers build underneath" / "second guitar enters on bar 5" /
                     "add harmony stack on the chorus" / "strings swell +6dB underneath"
드롭(벗기)            "drums cut to half-time" / "band drops out leaving only vocal" /
                     "strip to vocal and one instrument" / "everything drops but the sub"
재진입(폭발)          "full band re-enters" / "drums slam back in" / "the whole mix opens up"
필터/공간            "filter opens up into the chorus" / "reverb tail blooms then snaps dry"
```
- 원칙: 후렴이 verse보다 *큰* 이유는 새 멜로디만이 아니라 *레이어가 더해져서*다. 매 곡 에너지 아크(§5 강약)를 레이어 이벤트로 구현.
- 최종 후렴 = 레이어 최대(옥타브 보컬 + 화음 스택 + 풀 밴드). Outro = 레이어 점감.

## §3. 트랜지션 어휘 (섹션 *사이* 구체 장치 — 밋밋한 전환 차단)
전환이 밋밋하면 곡이 "목적지 나열"처럼 들린다. 섹션 경계에 장치를 박아라.
```
장치             효과                    Suno 큐
──────────────────────────────────────────────────────────
riser/uplifter   상승 긴장 → 드롭         "riser into the chorus" / "white-noise rise"
downlifter       하강·전환               "downlifter into the verse"
drum fill        섹션 연결               "drum fill into the chorus"
impact/boom      타격 강조               "impact hit on the downbeat of the chorus"
reverse cymbal   흡입감                  "reverse cymbal swell before the drop"
filter sweep     개방/폐쇄              "filter sweep up into the final chorus"
tape stop        급정지 멋             "tape stop before the bridge"
silence→hit      극적 진입              [One-bar rest] 직후 [Belted] (§8 휴지 설계)
beat drop        EDM/댄스 정점          "beat drop on the chorus downbeat"
```

## §4. ★보컬 편곡 — DOUBLING vs HARMONY (핵심 구분 — 둘은 다른 일을 한다)
가장 흔한 혼동: 더블링 ≠ 화음. **더블링=두께(같은 음 다시), 화음=색(새 음).** 프로 믹스는 *둘 다* 쓴다.
```
기법              무엇                            Suno 큐
──────────────────────────────────────────────────────────────
Doubling(유니즌)  같은 음 다시 = 두께·존재감       [Doubled] / [Unison double] / "lead vocal doubled"
                  (새 음 X). ADT 계열              "vocal doubles only on the final phrase"(절제)
Octave double     옥타브 위=시머/에테리얼          [Octave double higher] (밝음·천상)
                  옥타브 아래=무게/그라운드        [Octave double lower] (무게·박력)
Harmony(화음)     새 음 = 색·움직임.               [Harmony +3rd] / [+5th] / [+7th] / [Octave harmony]
                  3rd/5th/7th/옥타브               "stacked harmonies on the chorus"
보색키 화음       보색 key 화음 = 신스/보코더 질감  "vocoder-like stacked harmony" / "synthetic choir stack"
Ad-lib            *한 번만* 녹음(스택 X) = 필/응답  (ad-lib) 줄 끝 인라인 / 힙합 콜앤리스폰스
                  ·에너지(힙합 특히)               독립 줄 금지(§8)
Vocal chop        단어/구 잘라 리듬 재배치          [chopped vocal stutter] / "vocal chop hook"
Call-response     리드 + 응답                      [V1] 리드 ... [V2] answers / "call and response"
Counter-melody    스택에 대선율 = 합창 느낌         "counter-melody in the backing stack"
```
- 적용: 후렴/브릿지/최종에 *moment*를 만들려면 화음 스택. 리드를 두껍게는 더블. 둘을 섞어 입체.
- ★절제: 레이어 과다 = 머드(38 §3). "quality over quantity" — 잘 둔 몇 레이어 > 난잡한 다수.

## §5. 스택 패닝·공간 (Suno 렌더 가능)
- **리드 센터 / 더블 ~30% L·R / 화음 더 넓게 ~60%.** 전부 하드팬 금지(가운데 구멍·보컬 단절).
- Suno 큐: "lead vocal center, doubles panned wide left and right, harmonies wider" / "backing stack spread, lead dry and centered".
- 남녀 보컬 섞으면 깊이 ↑. 톤 변화(whispery/chesty/nasal)로 다성 효과(§6 캐릭터).

## §6. 장르별 보컬 레이어링 (장르마다 보컬 편곡이 다르다)
```
장르           보컬 레이어링 처방
──────────────────────────────────────────────────────────
Pop            폴리시 더블, 클로즈 하모니(3rd/5th), 와이드 패닝, 후렴 스택
Hip-Hop        ★미니멀 레이어 + 크리에이티브 애드립 + 콜앤리스폰스(스택 적게)
R&B/소울       스택 하모니 + 브리시 톤, 밀집 화음, 7th/9th 색
Indie/Electronic 앰비언트 텍스처, 리버스 레이어, 실험 FX, 보색키 보코더
Rock/밴드       더블 리드 + 갱 보컬 후렴(unison shout) + 옥타브
Gospel/합창     덴스 하모니 스택, 콜앤리스폰스, 화음 피라미드
Folk/어쿠스틱   성긴 더블 1겹, 자연스런 3rd 하모니, 과스택 금지(친밀 유지)
```

## §7. Suno 큐 치트시트 (이 파일의 렌더 가능 태그 모음)
구조: `[Short Instrumental Intro: N bars]` `[Post-Chorus]` `[Instrumental Break: N bars]` `[Outro]`/`[End]`
레이어: `[layers build underneath]` `[add harmony stack]` `[band drops out leaving only vocal]` `[drums cut to half-time]` `[full band re-enters]` `[strip to vocal and one instrument]`
전환: `[riser into the chorus]` `[drum fill]` `[reverse cymbal swell]` `[filter sweep up]` `[tape stop]` `[One-bar rest]` `[impact hit]`
보컬: `[Doubled]` `[Octave double higher/lower]` `[Harmony +3rd/+5th/+7th]` `[stacked harmonies]` `[vocoder-like stacked harmony]` `[chopped vocal stutter]` `[V2 answers]` `(ad-lib)`
패닝: "lead center, doubles panned wide, harmonies wider" (Style/큐 양쪽)

## §8. 출력 직전 구성·보컬편곡 체크 (내부, 36/37/38과 함께)
```
□ 각 섹션이 *기능*을 하나? (pre=램프 / post=훅태그 / bridge=리프레시·분류)
□ 에너지를 레이어로 그렸나? (후렴이 큰 이유 = 레이어 추가, 단순 새멜로디 X)
□ 섹션 전환에 장치 ≥1? (riser/fill/drop/rest — 밋밋한 컷 방지)
□ 보컬 풍성함 필요 자리(후렴/브릿지/최종): 더블(두께) + 화음(색) 구분 적용?
□ 옥타브/화음 인터벌 명시? 보색키 보코더 의도면 명시?
□ 애드립 = 한 번·인라인? 스택 과다 머드 아닌가(38 §3)?
□ 패닝: 리드 센터, 하드팬 전부 회피?
□ 장르별 보컬 레이어링(§6) 매칭? (힙합=애드립 / R&B=스택 / 록=갱)
```
하나라도 빠지면 보강 후 출력(표면 보고 X).
