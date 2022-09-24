$appConfigFile = [IO.Path]::Combine($currentDirectory, '.\pwshConfigFile.xml')
[xml]$appConfig = Get-Content $appConfigFile
$filePath = $appConfig.SelectSingleNode('//add[@key="workbookDir"]').Value
$excelObj = New-Object -ComObject Excel.Application
$excelObj.Visible = $true
$workBook = $excelObj.Workbooks.Open($filePath)
$workSheet = $workBook.Sheets.Item("BleesPivot")
$workSheet.Select()
$workBook.RefreshAll()
$workBook.Save()
# Uncomment this line if you want Excel to close on its own
#$excelObj.Quit()2

# Thank you to BeardOfCrimson: https://stackoverflow.com/a/23597066