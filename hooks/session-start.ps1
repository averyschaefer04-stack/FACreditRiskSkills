# DRIVER Session Start Hook (PowerShell)
# Injects the using-driver skill at the start of every session

$SkillPath = Join-Path $env:CLAUDE_PLUGIN_ROOT "skills\using-driver\SKILL.md"

if (Test-Path $SkillPath) {
    Write-Output "<EXTREMELY-IMPORTANT>"
    Get-Content $SkillPath -Raw
    Write-Output "</EXTREMELY-IMPORTANT>"
}
