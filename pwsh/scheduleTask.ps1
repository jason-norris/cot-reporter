$appConfigFile = [IO.Path]::Combine($currentDirectory, '.\pwshConfigFile.xml')
[xml]$appConfig = Get-Content $appConfigFile
$filepath = $appConfig.SelectSingleNode('//add[@key="appDir"]').Value
$crTrigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Friday -At "15:35"
$crSettings = New-ScheduledTaskSettingsSet
$crAction = New-ScheduledTaskAction -Execute 'powershell.exe' -WorkingDirectory $filepath -Argument '-NonInteractive -NoLogo -NoProfile -Command ".\cotreporter.exe"'
$crTask = New-ScheduledTask -Action $crAction -Trigger $crTrigger -Settings $crSettings
Register-ScheduledTask -TaskName 'Reporter Weekly Run' -InputObject $crTask

# CFTC reports are currently published Fridays at 15:30 (adjust schedule accordingly)