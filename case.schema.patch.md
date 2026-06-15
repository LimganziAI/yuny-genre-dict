# case.schema.patch.md — schemas/case.schema.md 패치 후보
적용 위치: yaml 블록의 `sliders:` 행 바로 아래에 4행 삽입. (아래는 후보이며, repo 반영은 운영자가 한다.)

```yaml
suno_feature_used: Create | Cover | Persona | Upload-Audio | Studio | Stem-Cover | Extend | Replace | Remaster
input_audio_ownership: original | licensed | unknown   # 업로드 소스 권리 — ToS 추적용
prompt_variable_changed:   # 직전 케이스 대비 바꾼 단일 변수 (card 18 A/B 추적)
render_count:              # 동일 프롬프트 렌더 횟수 (randomness 분리 증거, card 17 Step 0)
```

미채택(중복 방지): `confidence`·`promotion_threshold` — promotion_status 필드 + prompt-pattern.schema.md가 이미 커버. 카드 18의 인라인 축약 스키마는 변경하지 않는다(간결 유지) — "전체 필드는 schemas/case.schema.md 참조" 1줄만 카드에 반영됨.
