$ErrorActionPreference = "Stop"

$stateRoot = Join-Path ([System.IO.Path]::GetTempPath()) "copilot-primer-test-gate"

function Get-StateFilePath([string]$sessionId) {
    if (-not (Test-Path $stateRoot)) {
        New-Item -ItemType Directory -Path $stateRoot -Force | Out-Null
    }

    $safeSessionId = ($sessionId -replace "[^a-zA-Z0-9_-]", "_")
    return Join-Path $stateRoot ("{0}.json" -f $safeSessionId)
}

function Save-ApprovalState([string]$sessionId, [string]$decision) {
    $stateFilePath = Get-StateFilePath $sessionId
    @{ decision = $decision } | ConvertTo-Json -Compress | Set-Content -Path $stateFilePath -Encoding ascii
}

function Read-ApprovalState([string]$sessionId) {
    $stateFilePath = Get-StateFilePath $sessionId
    if (-not (Test-Path $stateFilePath)) {
        return $null
    }

    try {
        return Get-Content -Path $stateFilePath -Raw | ConvertFrom-Json -ErrorAction Stop
    } catch {
        return $null
    }
}

function Clear-ApprovalState([string]$sessionId) {
    $stateFilePath = Get-StateFilePath $sessionId
    if (Test-Path $stateFilePath) {
        Remove-Item -Path $stateFilePath -Force
    }
}

function Get-StringValues($value) {
    if ($null -eq $value) {
        return @()
    }

    if ($value -is [string]) {
        return @($value)
    }

    if ($value -is [System.Collections.IDictionary]) {
        $strings = @()
        foreach ($entry in $value.GetEnumerator()) {
            $strings += Get-StringValues $entry.Value
        }
        return $strings
    }

    if ($value -is [System.Collections.IEnumerable] -and -not ($value -is [string])) {
        $strings = @()
        foreach ($item in $value) {
            $strings += Get-StringValues $item
        }
        return $strings
    }

    return @([string]$value)
}

$hookInput = if ($MyInvocation.ExpectingInput) {
    ($input | Out-String)
} else {
    [Console]::In.ReadToEnd()
}

$payload = $null

try {
    $payload = $hookInput | ConvertFrom-Json -ErrorAction Stop
} catch {
}

$eventName = if ($payload -and $payload.hookEventName) { [string]$payload.hookEventName } else { "" }
$sessionId = if ($payload -and $payload.sessionId) { [string]$payload.sessionId } else { "default-session" }

if ($eventName -eq "UserPromptSubmit") {
    $promptText = if ($payload -and $payload.prompt -is [string]) { [string]$payload.prompt } else { $hookInput }

    if ($promptText.Contains("PROCEED")) {
        Save-ApprovalState $sessionId "PROCEED"
    } elseif ($promptText.Contains("MODIFY") -or $promptText.Contains("SKIP")) {
        Save-ApprovalState $sessionId "HOLD"
    } else {
        Clear-ApprovalState $sessionId
    }

    exit 0
}

if ($eventName -ne "PreToolUse") {
    exit 0
}

$toolName = if ($payload -and $payload.tool_name) { [string]$payload.tool_name } else { "" }
$toolInputStrings = if ($payload) { Get-StringValues $payload.tool_input } else { @() }
$normalizedInput = ($toolInputStrings + @($toolName)) -join "`n"
$normalizedInput = $normalizedInput.ToLowerInvariant()

$isFileEditTool =
    $toolName.ToLowerInvariant().Contains("edit") -or
    $toolName.ToLowerInvariant().Contains("create") -or
    $toolName.ToLowerInvariant().Contains("write") -or
    $toolName.ToLowerInvariant().Contains("replace")

$targetsTestGeneration =
    $isFileEditTool -and (
        $normalizedInput.Contains("python-app/tests/test_api.py") -or
        $normalizedInput.Contains("python-app/tests/") -or
        $normalizedInput.Contains("test_api.py")
    )

if (-not $targetsTestGeneration) {
    exit 0
}

$state = Read-ApprovalState $sessionId
if ($state -and $state.decision -eq "PROCEED") {
    Clear-ApprovalState $sessionId
    exit 0
}

$response = @{
    hookSpecificOutput = @{
        hookEventName = "PreToolUse"
        permissionDecision = "deny"
        permissionDecisionReason = "Before editing tests, first summarize the planned test changes and wait for the user to reply with PROCEED, MODIFY, or SKIP."
        additionalContext = "Test-file edits are gated. Summarize the intended test changes first. Only edit tests after the user replies with PROCEED in a follow-up prompt."
    }
} | ConvertTo-Json -Compress

Write-Output $response
exit 0