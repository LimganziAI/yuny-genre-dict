# ============================================================
# 23a_GENRE_INDEX_MASTER.md  —  On-Demand 장르 인덱스 (외부 fetch 버전)
# YUNY v2.7  ·  풀바디 본문은 외부(public GitHub)에 위치, 본 인덱스만 프로젝트 상주
# ============================================================
#
# ▶ 조회 절차 (장르 발화 시):
#   1) 아래 표에서 장르명 또는 [slug] 매칭
#   2) 그 줄의 raw URL을 그대로 web_fetch → 그 장르 본문만 로드 (개당 ~4-16K)
#   ※ 각 줄에 전체 raw URL이 박혀 있음(조합 불필요). repo 이름 바꾸면 일괄 치환.
#   ※ 매칭 실패 시 인접 후보 1-2개 fetch 후 판단, 그래도 없으면 web_search → 5축
#   ※ web_fetch가 막히면(드묾) bash로 'curl -s <URL>' 또는 운영자가 URL 직접 투척
#
# 총 277개 장르 / 10개 카테고리.  형식:  표시명 [slug] → 경로
# ============================================================

## Classical / Opera / Orchestral  (23i · 2)  →  classical/
Classical [classical] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/classical/classical.md
Opera [opera] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/classical/opera.md

## Country / Folk / Acoustic  (23h · 13)  →  country-folk/
Americana [americana] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/americana.md
Bakersfield Sound [bakersfield-sound] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/bakersfield-sound.md
Bluegrass [bluegrass] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/bluegrass.md
Bro-Country [bro-country] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/bro-country.md
Celtic [celtic] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/celtic.md
Country [country] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/country.md
Folk [folk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/folk.md
Honky-Tonk [honky-tonk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/honky-tonk.md
Indie Folk [indie-folk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/indie-folk.md
Neotraditional Country [neotraditional-country] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/neotraditional-country.md
Outlaw Country [outlaw-country] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/outlaw-country.md
Singer-Songwriter [singer-songwriter] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/singer-songwriter.md
Western Swing [western-swing] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/country-folk/western-swing.md

## Electronic & Dance  (23c · 47)  →  electronic-dance/
2-Step Garage [2-step-garage] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/2-step-garage.md
Acid Jazz [acid-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/acid-jazz.md
Ambient [ambient] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/ambient.md
Balearic [balearic] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/balearic.md
Bass House [bass-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/bass-house.md
Bassline [bassline] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/bassline.md
Breakbeat [breakbeat] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/breakbeat.md
Breakcore [breakcore] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/breakcore.md
CHILLWAVE [chillwave] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/chillwave.md
Chiptune [chiptune] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/chiptune.md
Deep House [deep-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/deep-house.md
Drum and Bass [drum-and-bass] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/drum-and-bass.md
Dubstep [dubstep] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/dubstep.md
Electronic Dance Music (EDM) [edm] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/edm.md
Electro [electro] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/electro.md
Electronic [electronic] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/electronic.md
Eurodance [eurodance] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/eurodance.md
Folktronica [folktronica] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/folktronica.md
Footwork [footwork] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/footwork.md
Future Bass [future-bass] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/future-bass.md
Future Funk [future-funk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/future-funk.md
Glitch [glitch] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/glitch.md
Glitch Hop [glitch-hop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/glitch-hop.md
Grime [grime] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/grime.md
Hardstyle [hardstyle] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/hardstyle.md
House [house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/house.md
HYPERPOP [hyperpop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/hyperpop.md
IDM [idm] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/idm.md
Italo Disco [italo-disco] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/italo-disco.md
Jersey Club [jersey-club] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/jersey-club.md
Jungle [jungle] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/jungle.md
Minimal Techno [minimal-techno] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/minimal-techno.md
Moombahton [moombahton] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/moombahton.md
Neurofunk [neurofunk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/neurofunk.md
Nightcore [nightcore] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/nightcore.md
PHONK [phonk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/phonk.md
Progressive House [progressive-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/progressive-house.md
Reggaeton [reggaeton] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/reggaeton.md
Synthwave [synthwave] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/synthwave.md
Tech House [tech-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/tech-house.md
Techno [techno] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/techno.md
Trance [trance] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/trance.md
Trip-Hop [trip-hop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/trip-hop.md
Tropical House [tropical-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/tropical-house.md
UK Garage [uk-garage] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/uk-garage.md
Vaporwave [vaporwave] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/vaporwave.md
Witch House [witch-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/electronic-dance/witch-house.md

## Hip-Hop & Rap  (23d · 20)  →  hiphop-rap/
Abstract Hip-Hop [abstract-hip-hop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/abstract-hip-hop.md
Boom Bap [boom-bap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/boom-bap.md
Cloud Rap [cloud-rap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/cloud-rap.md
Country Rap [country-rap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/country-rap.md
Crunk [crunk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/crunk.md
Drill [drill] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/drill.md
East Coast Hip Hop [east-coast-hip-hop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/east-coast-hip-hop.md
Emo Rap [emo-rap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/emo-rap.md
G-Funk [g-funk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/g-funk.md
Gangsta Rap [gangsta-rap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/gangsta-rap.md
Grime [grime] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/grime.md
Hip-Hop [hip-hop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/hip-hop.md
Horrorcore [horrorcore] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/horrorcore.md
Jazz Rap [jazz-rap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/jazz-rap.md
Latin Trap [latin-trap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/latin-trap.md
Mumble Rap [mumble-rap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/mumble-rap.md
PHONK [phonk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/phonk.md
Southern Hip Hop [southern-hip-hop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/southern-hip-hop.md
Trap [trap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/trap.md
Underground Hip Hop [underground-hip-hop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/hiphop-rap/underground-hip-hop.md

## Jazz & Blues  (23g · 15)  →  jazz-blues/
Acid Jazz [acid-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/acid-jazz.md
Bebop [bebop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/bebop.md
Big Band [big-band] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/big-band.md
Blues [blues] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/blues.md
Bossa Nova [bossa-nova] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/bossa-nova.md
Cool Jazz [cool-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/cool-jazz.md
Delta Blues [delta-blues] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/delta-blues.md
Hard Bop [hard-bop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/hard-bop.md
Jazz [jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/jazz.md
Latin Jazz [latin-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/latin-jazz.md
Modal Jazz [modal-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/modal-jazz.md
Ragtime [ragtime] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/ragtime.md
Smooth Jazz [smooth-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/smooth-jazz.md
Swing / Neo-Swing [swing] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/swing.md
Vocal Jazz [vocal-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/jazz-blues/vocal-jazz.md

## Other / Children / Faith / Specialty  (23k · 52)  →  other-specialty/
A Cappella [a-cappella] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/a-cappella.md
Beatboxing [beatboxing] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/beatboxing.md
Blackgaze [blackgaze] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/blackgaze.md
Chopped and Screwed [chopped-and-screwed] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/chopped-and-screwed.md
Cinematic [cinematic] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/cinematic.md
Conscious Hip-Hop [conscious-hip-hop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/conscious-hip-hop.md
Contemporary Christian Music [contemporary-christian] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/contemporary-christian.md
Dark Ambient [dark-ambient] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/dark-ambient.md
Dark Jazz [dark-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/dark-jazz.md
Darksynth [darksynth] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/darksynth.md
Darkwave [darkwave] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/darkwave.md
Deathcore [deathcore] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/deathcore.md
Downtempo [downtempo] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/downtempo.md
Drone [drone] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/drone.md
Drone Metal [drone-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/drone-metal.md
Dungeon Synth [dungeon-synth] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/dungeon-synth.md
EBM [ebm] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/ebm.md
Electroswing [electroswing] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/electroswing.md
Enka [enka] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/enka.md
Ethio-Jazz [ethio-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/ethio-jazz.md
Future House [future-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/future-house.md
Glitch Pop [glitch-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/glitch-pop.md
Gypsy Jazz [gypsy-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/gypsy-jazz.md
Hair Metal [hair-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/hair-metal.md
Jazz Fusion [jazz-fusion] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/jazz-fusion.md
Kayokyoku [kayokyoku] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/kayokyoku.md
Lo-Fi [lo-fi] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/lo-fi.md
Lo-Fi House [lo-fi-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/lo-fi-house.md
Madchester [madchester] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/madchester.md
New Age [new-age] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/new-age.md
Noise Pop [noise-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/noise-pop.md
Nu Jazz [nu-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/nu-jazz.md
PC Music [pc-music] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/pc-music.md
Plugg [plugg] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/plugg.md
Pop Rap [pop-rap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/pop-rap.md
Post-Dubstep [post-dubstep] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/post-dubstep.md
Post-Metal [post-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/post-metal.md
Progressive Metal [progressive-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/progressive-metal.md
Psychedelic Trance [psychedelic-trance] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/psychedelic-trance.md
Riot Grrrl [riot-grrrl] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/riot-grrrl.md
Slowcore [slowcore] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/slowcore.md
Soul Jazz [soul-jazz] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/soul-jazz.md
Soundtrack [soundtrack] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/soundtrack.md
Space Disco [space-disco] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/space-disco.md
Spaghetti Western [spaghetti-western] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/spaghetti-western.md
Spoken Word [spoken-word] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/spoken-word.md
Trap Metal [trap-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/trap-metal.md
Trot [trot] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/trot.md
Twee Pop [twee-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/twee-pop.md
Video Game Music [video-game-music] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/video-game-music.md
Visual Kei [visual-kei] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/visual-kei.md
Worship [worship] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/other-specialty/worship.md

## Pop & East Asian Pop  (23e · 17)  →  pop-eastasian/
Anisong [anisong] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/anisong.md
Art Pop [art-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/art-pop.md
Baroque Pop [baroque-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/baroque-pop.md
Britpop [britpop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/britpop.md
Bubblegum Pop [bubblegum-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/bubblegum-pop.md
Cantopop [cantopop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/cantopop.md
Chamber Pop [chamber-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/chamber-pop.md
City Pop [city-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/city-pop.md
Electropop [electropop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/electropop.md
HYPERPOP [hyperpop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/hyperpop.md
J-Pop [j-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/j-pop.md
K-Pop [k-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/k-pop.md
Mandopop [mandopop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/mandopop.md
Pop [pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/pop.md
Sophisti-pop [sophisti-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/sophisti-pop.md
Synth-Pop [synth-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/synth-pop.md
Vocaloid [vocaloid] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/pop-eastasian/vocaloid.md

## R&B / Soul / Funk / Disco  (23f · 15)  →  rnb-soul-funk/
Alternative R&B [alternative-rnb] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/alternative-rnb.md
Boogie [boogie] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/boogie.md
Disco [disco] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/disco.md
Doo-Wop [doo-wop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/doo-wop.md
Funk [funk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/funk.md
Gospel [gospel] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/gospel.md
Motown [motown] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/motown.md
Neo-Soul [neo-soul] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/neo-soul.md
New Jack Swing [new-jack-swing] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/new-jack-swing.md
Nu Disco [nu-disco] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/nu-disco.md
P-Funk [p-funk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/p-funk.md
Post-Disco [post-disco] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/post-disco.md
Quiet Storm [quiet-storm] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/quiet-storm.md
R&B / Soul [rnb] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/rnb.md
Trap Soul [trap-soul] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rnb-soul-funk/trap-soul.md

## Rock & Metal  (23b · 49)  →  rock-metal/
Alternative Rock [alternative] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/alternative.md
Arena Rock [arena-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/arena-rock.md
Black Metal [black-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/black-metal.md
Death Metal [death-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/death-metal.md
Djent [djent] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/djent.md
Doom Metal [doom-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/doom-metal.md
Dream Pop [dream-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/dream-pop.md
Emo [emo] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/emo.md
Folk Metal [folk-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/folk-metal.md
Garage Rock [garage-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/garage-rock.md
Grindcore [grindcore] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/grindcore.md
Groove Metal [groove-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/groove-metal.md
Grunge [grunge] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/grunge.md
Hardcore Punk [hardcore-punk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/hardcore-punk.md
Indie Folk [indie-folk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/indie-folk.md
Indie Rock [indie-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/indie-rock.md
Industrial [industrial] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/industrial.md
Jam Band [jam-band] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/jam-band.md
Jangle Pop [jangle-pop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/jangle-pop.md
Krautrock [krautrock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/krautrock.md
Math Rock [math-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/math-rock.md
Melodic Death Metal [melodic-death-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/melodic-death-metal.md
Metal [metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/metal.md
Metalcore [metalcore] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/metalcore.md
Nerdcore [nerdcore] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/nerdcore.md
New Wave [new-wave] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/new-wave.md
Noise Rock [noise-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/noise-rock.md
Nu-Metal [nu-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/nu-metal.md
NWOBHM [nwobhm] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/nwobhm.md
Pop Punk [pop-punk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/pop-punk.md
Post-Punk [post-punk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/post-punk.md
Post-Punk Revival [post-punk-revival] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/post-punk-revival.md
Post-Rock [post-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/post-rock.md
Power Metal [power-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/power-metal.md
Progressive Rock [progressive-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/progressive-rock.md
Psychedelic Rock [psychedelic-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/psychedelic-rock.md
Punk [punk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/punk.md
Rockabilly [rockabilly] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/rockabilly.md
Screamo [screamo] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/screamo.md
Shoegaze [shoegaze] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/shoegaze.md
Ska Punk [ska-punk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/ska-punk.md
Sludge Metal [sludge-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/sludge-metal.md
Space Rock [space-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/space-rock.md
Speed Metal [speed-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/speed-metal.md
Stoner Rock [stoner-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/stoner-rock.md
Surf Rock [surf-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/surf-rock.md
Symphonic Metal [symphonic-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/symphonic-metal.md
Thrash Metal [thrash-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/thrash-metal.md
Viking Metal [viking-metal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/rock-metal/viking-metal.md

## World / Latin / Afro / Caribbean / Middle Eastern  (23j · 47)  →  world/
Afro-Cuban [afro-cuban] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/afro-cuban.md
Afro House [afro-house] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/afro-house.md
Afrobeats [afrobeats] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/afrobeats.md
Afropop [afropop] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/afropop.md
Afroswing [afroswing] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/afroswing.md
Amapiano [amapiano] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/amapiano.md
Axe [axe] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/axe.md
Bachata [bachata] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/bachata.md
Baile Funk [baile-funk] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/baile-funk.md
Banda [banda] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/banda.md
Bhangra [bhangra] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/bhangra.md
Bolero [bolero] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/bolero.md
Bollywood [bollywood] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/bollywood.md
Bongo Flava [bongo-flava] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/bongo-flava.md
Bossa Nova [bossa-nova] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/bossa-nova.md
Calypso [calypso] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/calypso.md
Chanson [chanson] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/chanson.md
Cumbia [cumbia] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/cumbia.md
Dancehall [dancehall] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/dancehall.md
Dub [dub] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/dub.md
Fado [fado] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/fado.md
Flamenco [flamenco] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/flamenco.md
Ghazal [ghazal] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/ghazal.md
Highlife [highlife] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/highlife.md
Indian Classical [indian-classical] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/indian-classical.md
Juju [juju] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/juju.md
Klezmer [klezmer] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/klezmer.md
Kuduro [kuduro] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/kuduro.md
Kwaito [kwaito] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/kwaito.md
Latin [latin] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/latin.md
Latin Trap [latin-trap] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/latin-trap.md
Lovers Rock [lovers-rock] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/lovers-rock.md
Mambo [mambo] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/mambo.md
Mbalax [mbalax] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/mbalax.md
Merengue [merengue] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/merengue.md
Qawwali [qawwali] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/qawwali.md
Reggae [reggae] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/reggae.md
Reggaeton [reggaeton] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/reggaeton.md
Rocksteady [rocksteady] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/rocksteady.md
Roots Reggae [roots-reggae] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/roots-reggae.md
Samba [samba] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/samba.md
Schlager [schlager] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/schlager.md
Ska [ska] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/ska.md
Soca [soca] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/soca.md
Soukous [soukous] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/soukous.md
Tango [tango] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/tango.md
Tropicalia [tropicalia] → https://raw.githubusercontent.com/LimganziAI/yuny-genre-dict/main/23_GENRE_FULLBODY/world/tropicalia.md

# ── 중복 slug (2개+ 카테고리에 존재 — 조회 시 카테고리로 구분) ──
#   acid-jazz: electronic-dance, jazz-blues
#   bossa-nova: jazz-blues, world
#   grime: electronic-dance, hiphop-rap
#   hyperpop: electronic-dance, pop-eastasian
#   indie-folk: rock-metal, country-folk
#   latin-trap: hiphop-rap, world
#   phonk: electronic-dance, hiphop-rap
#   reggaeton: electronic-dance, world