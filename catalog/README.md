# YUNY 카탈로그 — 캐릭터 보컬 & 곡 프롬프트 복원본 (2026-06-11 데이터)

YouTube 메타(450) + Suno export(유니크 클립 1,491) 매칭. video 가사 ↔ Suno 클립 가사 4-gram Jaccard(≥0.42), 커버는 cover_clip_id로 CREATE 링크.

## 구조
- `00_MASTER_INDEX.md` — 캐릭터별 곡 표 (YT♥/key/bpm/model/CREATE·COVER 보유)
- `01_VOCAL_PROFILES.md` — 캐릭터별 보컬톤 (실사용 tags에서 추출 + 음역)
- `songs/{캐릭터}/{번호}_{곡}.md` — 곡별 실제 CREATE/COVER 풀 프롬프트(tags+가사+큐)+커버체인+메타
- `catalog.json` — 구조화 데이터
- `02_UNMATCHED.md` — 미매칭 + 메이킹필름

## 정직 고지
- COVER 프롬프트가 주로 복원됨 (다수 CREATE 원본은 export 미포함 → COVER에 풀 Style+보컬+음질 존재).
- 매칭 <0.55는 가사수정 추정 낮은신뢰 (각 곡파일에 Jaccard 표기).
- 미복원 곡 = 클립 매칭 실패(휴지통/유튜브단독/대량수정). YT 메타만.
- 보컬 프로파일은 솔로+듀엣 합산(듀엣은 상대 보컬 섞임), 가끔 비-보컬 구절 혼입.
- OST_기타 = 단일캐릭터 없는 ED/OST/인스트/MV (극소수 오분류 가능).
