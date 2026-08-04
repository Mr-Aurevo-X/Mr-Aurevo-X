$ErrorActionPreference = 'Continue'
$names = @(
  'profile-preview-12-phosphor-dense',
  'profile-preview-13-ice-cyan',
  'profile-preview-14-amber-warn',
  'profile-preview-15-magenta-crt',
  'profile-preview-16-red-alert',
  'profile-preview-17-matrix-deep',
  'profile-preview-18-dual-split',
  'profile-preview-19-mono-brutal',
  'profile-preview-20-gold-champagne',
  'profile-preview-21-soft-mint',
  'profile-preview-22-void-abyss',
  'profile-preview-23-deep-space',
  'profile-preview-24-noir-ink',
  'profile-preview-25-shadow-forge',
  'profile-preview-26-eclipse',
  'profile-preview-27-smoke-glass',
  'profile-preview-28-blood-moon',
  'profile-preview-29-obsidian',
  'profile-preview-30-midnight-atelier',
  'profile-preview-31-hollow'
)
$ok = 0
$fail = 0
foreach ($n in $names) {
  Write-Host "DELETE $n ..."
  gh repo delete "Mr-Aurevo-X/$n" --yes 2>&1 | Tee-Object -Variable out | Out-Null
  if ($LASTEXITCODE -eq 0) { $ok++; Write-Host "  OK" } else { $fail++; Write-Host "  FAIL $out" }
}
Write-Host "DONE ok=$ok fail=$fail"
$root = 'C:\Users\aurel\Documents\Dev Central Tree'
foreach ($d in @('profile-preview-batch-12-21','profile-preview-batch-22-31','_profile-previews')) {
  $p = Join-Path $root $d
  if (Test-Path $p) {
    Remove-Item $p -Recurse -Force
    Write-Host "removed local $d"
  }
}
Write-Host 'Remaining profile-preview repos:'
gh repo list Mr-Aurevo-X --limit 200 --json name -q '.[].name' | Select-String 'profile-preview'
