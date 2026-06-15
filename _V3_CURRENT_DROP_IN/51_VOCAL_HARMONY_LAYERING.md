# 51. VOCAL HARMONY & LAYERING — 보컬 하모니·레이어링 (화음 아키텍처)
# VERSION: v1.0 (2026-06-15) — 이력 CHANGELOG.txt
# 근거: §6(보컬 디렉션)·39(보컬편곡 doubling/octave/adlib/chop)·§7(컨투어)·02/03(화성)·47(훅) + 현행 보컬 하모니/백킹 편곡 web 검증(2026-06)
# 위상: §6([Singing:] 7요소)·39(doubling≠harmony·옥타브·adlib)를 *전제*하고, 그 위에 **하모니 인터벌 시스템 + 콜앤리스폰스 + 장르 하모니 접근 + 레이어 목적 규율**을 더함. 39 반복 X.
# 발동: "화음 넣어/백보컬/코러스 두껍게/콜앤리스폰스/가스펠 화음/스택"·보컬 풍성함 설계.
# ★핵심: 대부분 곡은 한 목소리가 아니다. **하모니 = 색(새 음) / 더블링 = 두께(같은 음).** 둘 다 쓴다. 리드는 앞, 레이어는 뒤.

## §0. 원리 — 색과 두께는 다른 도구
하모니는 *새 음*으로 멜로디를 보완(코드·움직임 생성). 더블링은 *같은 파트*를 겹쳐 두께·안정. 빌리 아일리시=속삭임 더블 /
퀸=조밀 하모니 스택 — 프로 믹스는 *둘 다*. 39가 doubling/octave/adlib 기본이면, 51은 *하모니 인터벌·콜앤리스폰스·장르 접근*.

## §1. 레이어 택소노미 (각 → Suno 큐)
```
레이어            정체/효과                        Suno 큐
──────────────────────────────────────────────────────────
Lead             주 초점                          (기본)
Harmony          새 음, 3rd/5th/7th 색·깊이         [Harmony +3rd] / "3rd and 5th harmony stack"
Double           같은 음 겹침, 두께·안정(pan L/R)    [Doubled] / "doubled lead, panned"
Octave           음역 확장(위/아래 옥타브)           [Octave double] / "octave double on the hook"
Whisper layer    공기·친밀(리드 밑)                 "whisper layer beneath the lead"
Background(BGV)  코러스 감정 리프트                  (BGV) / "background vocals lifting the chorus"
Ad-lib           즉흥 짧은 구절(프로덕션 가치)        줄 끝 인라인 (adlib) (§8 — 독립 줄 X)
Counter-melody   리드와 *다른* 보완 멜로디 라인       "counter-melody weaving under the lead"
Pad/Sustain      지속음 화성 베드                    "sustained vocal pad underneath"
Vocal chop       리듬 퍼커시브(리듬섹션과 lock)       "rhythmic vocal chops" (40 그루브 연동)
```

## §2. 하모니 인터벌 시스템 (화음 쌓기)
- **기본:** 평행 3rd + 5th(60s~현재 라디오 클래식 사운드, 토닉 코드 모방).
- **확장:** 7th·옥타브 추가 = 합창 느낌 / 카운터멜로디 = 더 코러스적.
- **★3D(upper+lower):** 리드 *위* 3rd/5th + *아래* 3rd/5th → 입체 풀 사운드.
- **★코드 진행 따라 이동(R&B 핵심):** 하모니가 *코드 톤 위를 움직임*(고정 평행 X) — 각 코드의 코드톤에 화음, 부드러운 컴프·리버브로 녹임. 02/03 화성 연동.
- 큐: "3rd and 5th harmony stack on the chorus, harmonies moving with the chord progression".

## §3. 콜앤리스폰스 & 대화 (백킹이 리드와 대화)
- **콜앤리스폰스:** 백보컬이 리드에 *답*(모방 아닌 대화). 가스펠·소울·R&B 핵심. "call-and-response backing answering the lead".
- **지속 백킹:** 메인 라인 뒤 sustained 하모니 = 깊이·친밀. "sustained background harmonies behind the main line".
- **위빙(weaving):** R&B는 하모니가 리드 사이로 *드나듦*(in and out) — 대화 질감. (H.E.R./Jazmine Sullivan 결.)

## §4. 장르 하모니 접근 (장르마다 다름)
```
장르          하모니 접근
──────────────────────────────────────────────
팝            ★단순 — 2-3 보이스가 리드 프레이징 *완벽 추종* > 조밀 스택(Taylor Swift). 깔끔.
R&B/소울       풍부·유동 — 거의 풀 코드(3rd/6th/7th), 코드 진행 따라 이동, 위빙·콜앤리스폰스(Boyz II Men/H.E.R.)
가스펠         대형 콜앤리스폰스 합창, 위·아래 풀 스택
록            하모니 스택(Queen), 떼창 코러스, 옥타브 파워
포크/컨트리     평행 3rd 듀엣(close harmony), 따뜻 단순
EDM/팝        보컬 chop·스택 + 옥타브, 후렴 wall
시티팝/재즈     세련 확장 화성(7th/9th), 부드러운 백킹
```
→ 장르 맞춰 *접근 선택* — 팝에 R&B 풀 스택 남발 X, R&B에 평행 3rd만 X.

## §5. 명료성 규율 (오버레이어링 차단)
- **리드 앞, 레이어 뒤.** 각 레이어 *명확한 목적*(곡 서사에 기여). 목적 없는 레이어 = 클러터.
- **보이싱·스페이싱:** 잘못 배치된 화음 = 머디·디소넌트. 주파수 스펙트럼에서 각 파트 자리(7-zone, D).
- **less is more vs wall:** 때론 2-3 보이스가 벽보다 강함. 곡이 정한다 — 후렴 wall / verse 성김(또는 없음).
- 섹션별: Verse 보통 리드만(또는 가벼운 더블) / Pre 빌드 / Chorus 풀 하모니·BGV / Bridge 가변 / Final 최대 스택(47 훅·50 아크 연동).

## §6. Suno 실현 (큐 통합)
- **Lyrics:** [Harmony +3rd]/[Doubled]/[Stacked]/[Octave double]/(BGV) + 콜앤리스폰스 마커 + ad-lib 인라인(§8). 릴리즈 코러스에 [Stacked].
- **[Singing:] 백킹(39/§6):** "lush 3rd and 5th harmony stack on the chorus" / "call-and-response gospel backing" / "sustained vocal pad underneath" / "octave double on the hook only".
- **CREATE Style:** 보컬 편곡 1줄("doubled lead with 3rd/5th harmony stacks on choruses, R&B-style harmonies moving with the chords"). 혼성/듀엣은 §6 강제어법 + 51 하모니.
- **배치 규율:** 섹션 역할 비례(§5) — verse 성김→chorus 풀. 47 훅(보컬 챈트/스택)·50 아크(에너지)·44(감정)와 동기화.

## §7. 출력 직전 하모니 체크 (내부, §6/39와 함께)
```
□ 하모니(색) vs 더블(두께) 구분해 썼나? (둘 다 가능)
□ 인터벌 명시(3rd/5th/7th·upper+lower·코드 따라 이동)?
□ 콜앤리스폰스/위빙 필요한 장르면 반영(R&B/가스펠)?
□ 장르 하모니 접근 맞나? (팝 단순 vs R&B 풀 코드)
□ 명료성 — 리드 앞·레이어 뒤·각 목적? 오버레이어링 X?
□ 섹션 비례(verse 성김→chorus 풀 스택)?
□ Suno 큐로 박았나([Harmony +3rd]/[Stacked]/[Singing:] 백킹)?
□ 47 훅·50 아크·44 감정·§6 혼성과 동기화?
```
하나라도 빠지면 보강 후 출력(표면 보고 X). ★하모니=색, 더블=두께 — 장르 맞게 쌓되 리드는 앞, 목적 없는 레이어는 컷.
