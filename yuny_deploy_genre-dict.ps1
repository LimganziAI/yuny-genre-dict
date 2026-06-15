# ============================================================
# YUNY v3.0 deploy : local C:\uploadc  ->  GitHub main
# Repo  : LimganziAI/yuny-genre-dict
# Mode  : ADDITIVE by default (장르사전 277개 보존하고 OS 구조만 얹음)
#         $WipeExisting=$true 로 바꾸면 .git 빼고 전체 삭제 후 덮어쓰기(파괴적)
# 실행  : 우클릭 > PowerShell로 실행  또는  powershell -ExecutionPolicy Bypass -File deploy.ps1
#         바로 때리려면:  .\deploy.ps1 -Force   (확인 프롬프트 생략)
# ============================================================
param([switch]$Force)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

# ---- 설정 ----------------------------------------------------
$RepoUrl      = "https://github.com/LimganziAI/yuny-genre-dict.git"
$Branch       = "main"
$UploadDir    = "C:\uploadc"
$WorkDir      = "C:\_yuny_genre_dict_push"
$CommitMsg    = "Deploy YUNY v3.0 goal-chain structure (54 layers, knowledge 02-53)"
$WipeExisting = $false   # ★ $false=ADD(장르사전 보존) / $true=전체삭제후덮어쓰기(파괴적)
# -------------------------------------------------------------

Write-Host "`n[YUNY] Preflight..." -ForegroundColor Cyan
if (!(Get-Command git -ErrorAction SilentlyContinue)) {
    throw "git이 설치되어 있지 않음. Git for Windows 설치 후 다시 실행."
}
if (!(Test-Path $UploadDir)) {
    throw "업로드 폴더가 없음: $UploadDir"
}
$uploadItems = Get-ChildItem -LiteralPath $UploadDir -Force
if ($uploadItems.Count -eq 0) {
    throw "$UploadDir 폴더가 비어 있음."
}

# 흔한 실수 방지: C:\uploadc 안에 압축해제 폴더 하나만 있는 경우
$dirs  = $uploadItems | Where-Object { $_.PSIsContainer }
$files = $uploadItems | Where-Object { -not $_.PSIsContainer }
if ($dirs.Count -eq 1 -and $files.Count -eq 0) {
    Write-Host "`n[경고] $UploadDir 안에 폴더 하나만 있음: $($dirs[0].Name)" -ForegroundColor Yellow
    Write-Host "원하는 구조가 $UploadDir\README.md 처럼 바로 나와야 함." -ForegroundColor Yellow
    Write-Host "현재가 $UploadDir\$($dirs[0].Name)\... 라면 안쪽 내용물을 $UploadDir 바로 아래로 옮긴 뒤 다시 실행." -ForegroundColor Yellow
    throw "중첩 폴더 감지로 중단."
}

# ---- 안전 확인 ----------------------------------------------
$modeLabel = if ($WipeExisting) { "전체 삭제 후 덮어쓰기 (DESTRUCTIVE)" } else { "ADD (기존 파일 보존, 같은 경로만 갱신)" }
Write-Host "`n[YUNY] 대상 repo : $RepoUrl" -ForegroundColor White
Write-Host "[YUNY] 브랜치    : $Branch" -ForegroundColor White
Write-Host "[YUNY] 업로드원  : $UploadDir" -ForegroundColor White
Write-Host "[YUNY] 모드      : $modeLabel" -ForegroundColor $(if ($WipeExisting) { "Red" } else { "Green" })

if ($WipeExisting) {
    Write-Host "`n[!!! 경고 !!!] WipeExisting=TRUE — 이 repo의 .git 외 모든 파일을 삭제합니다." -ForegroundColor Red
    Write-Host "yuny-genre-dict 에 277개 장르사전(23_GENRE_FULLBODY/...)이 있으면 전부 사라지고" -ForegroundColor Red
    Write-Host "YUNY 런타임 장르 조회가 깨집니다. 장르사전을 옮겼거나 백업했을 때만 진행하세요." -ForegroundColor Red
}

if (-not $Force) {
    $ans = Read-Host "`n진행하려면 YES 입력 (취소는 엔터)"
    if ($ans -ne "YES") { Write-Host "[YUNY] 취소됨." -ForegroundColor Yellow; exit 0 }
}

# ---- 작업 ----------------------------------------------------
if (Test-Path $WorkDir) {
    Write-Host "[YUNY] 기존 작업폴더 삭제: $WorkDir" -ForegroundColor DarkGray
    Remove-Item -LiteralPath $WorkDir -Recurse -Force
}

Write-Host "[YUNY] Clone repo..." -ForegroundColor Cyan
git clone --branch $Branch $RepoUrl $WorkDir
Set-Location $WorkDir

if ($WipeExisting) {
    Write-Host "[YUNY] 기존 repo 파일 제거(.git 유지)..." -ForegroundColor Red
    Get-ChildItem -LiteralPath $WorkDir -Force |
        Where-Object { $_.Name -ne ".git" } |
        Remove-Item -Recurse -Force
} else {
    Write-Host "[YUNY] ADD 모드 — 기존 파일 보존, C:\uploadc 내용을 위에 덮어 병합..." -ForegroundColor Green
}

Write-Host "[YUNY] $UploadDir 내용 복사..." -ForegroundColor Cyan
Get-ChildItem -LiteralPath $UploadDir -Force | ForEach-Object {
    Copy-Item -LiteralPath $_.FullName -Destination $WorkDir -Recurse -Force
}

Write-Host "[YUNY] Git 상태 확인..." -ForegroundColor Cyan
git status --short
git add -A
$changes = git status --porcelain
if ([string]::IsNullOrWhiteSpace($changes)) {
    Write-Host "`n[YUNY] 변경사항 없음. push 생략." -ForegroundColor Yellow
    exit 0
}

Write-Host "`n[YUNY] Commit..." -ForegroundColor Cyan
git commit -m $CommitMsg

Write-Host "`n[YUNY] Push to $Branch..." -ForegroundColor Cyan
git push origin $Branch

Write-Host "`n[YUNY] 완료: $UploadDir 내용이 $RepoUrl ($Branch)에 반영됨." -ForegroundColor Green
if (-not $WipeExisting) {
    Write-Host "[YUNY] (ADD 모드 — 기존 장르사전 등은 그대로 유지됨)" -ForegroundColor Green
}
