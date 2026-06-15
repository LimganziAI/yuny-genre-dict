# reference_feature_sheet.schema.md — 레퍼런스 1건당 기능 분해 시트
경로 후보: `knowledge-evolving/reference-dna/reference_feature_sheet.schema.md`
채우는 것: **기능**. 금지: 가사·멜로디 채보·고유 어레인지 시퀀스 복제, 아티스트명의 Suno 필드 유입.

```yaml
release_year_era:        # 연도 + era grain (예: 2003 / early-2000s glossy R&B)
production_context:      # 프로듀서·씬 맥락 — 이름은 여기까지만, 필드에는 5-layer 분해로만
bpm_groove_feel:         # 수치 + swing/straight/halftime 등
key_tonal_color:         # 키 또는 밝기/모드 색
drum_role:               # 그루브 내 드럼의 기능 (예: 타이트 백비트, 공간 채움 아님)
bass_role:               # (예: 멜로딕 무빙 vs 페달)
harmonic_bed:            # 화성 바닥 (예: 7th 보이싱 키즈 패드)
vocal_posture:           # 자세·거리·강도 — 음색 모사 아님
section_density:         # 섹션별 레이어 증감 곡선
hook_function:           # 훅이 곡에서 하는 일 (예: 콜&리스폰스 해소)
signature_moment:        # 기능으로 서술 (예: post-chorus vocal-chop drop)
ending_behavior:         # 페이드/컷/모티프 회귀
do_not_copy:             # 이 레퍼런스에서 복제 금지인 식별 요소 명시
safe_functional_translation:  # 위 항목들의 프롬프트행 번역 — 장르어·기능어만
```

규칙: 시트 작성 전 필드 한 줄도 쓰지 않는다(card 10) · 사용자 고지 의무: "레퍼런스에서 기능만 가져왔어" · 완성 시트는 reference-dna/에 케이스처럼 저장해 재사용.
