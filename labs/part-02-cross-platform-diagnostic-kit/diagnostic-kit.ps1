[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$KitArguments
)

$ErrorActionPreference = 'Stop'
$scriptPath = Join-Path $PSScriptRoot 'diagnostic_kit.py'
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    throw 'Python is required and was not found on PATH.'
}

& $python.Source $scriptPath @KitArguments
exit $LASTEXITCODE
