# Commitment of Traders (COT) Reporter

COT Reporter is a Python application which scrapes weekly reports posted by the Commodity Futures Trading Commission ([CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm)) and prepares them for presentation in Excel via PowerQuery and Power Pivot. To demonstrate how reports of interest can be automatically extracted, loaded, and transformed for analysis in pivot tables and charts, two reports were targeted in this pilot project - the [Disaggregated Futures](https://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm) and [Traders in Financial Futures](https://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm). A data model with certain measures was then created to present the [Blees Sentiment Rating](https://bit.ly/3S76uMm) for given markets.

## Tech Choices
Python was selected for its convenient libraries to handle HTML or XML ([Beautiful Soup](https://pypi.org/project/beautifulsoup4/)) and various data structures ([pandas](https://pandas.pydata.org/)), while Excel was chosen for its accessibility as a BI tool. PowerQuery offers the necessary ETL functionality to manage the underlying CSVs created by the app, while PowerPivot acts as a suitable endpoint for the expected consumers of this data.

## Challenges and Future Plans
The primary challenge was in maintaining modularity for additional reports to be pulled and pushed to the model workbook. Attention was given to portability and dynamic paths overall.

Future updates will likely include:

- Logging and error handling
- Rewrites to leverage classes
- Console with progress bars
- Interactive installation

## Installation

Use the archive to install COT Reporter in your preferred directory. Once extracted, complete the following steps to obtain reports and populate workbook.

1. Update [**config.ini**](/src/config.ini) with the installation path. Example:

![config_ini](https://user-images.githubusercontent.com/8696078/192114851-a6f95e7a-b4f7-4ec6-9713-b9732421ba1f.png)


2. Update the workbook sheet *edit_paths* with the same install path. Example:

![wb_edit_paths](https://user-images.githubusercontent.com/8696078/192114117-0b79624b-ca31-4abb-b13b-93b2c0ab92cb.png)

3. **Optional**: Update [**pswhConfigFile.xml**](/pwsh/pwshConfigFile.xml) in text editor if you plan to run PowerShell

![pwshConfigFile](https://user-images.githubusercontent.com/8696078/192114203-10366b3e-0872-473f-8d95-37cf5eea0080.png)

## Usage
### Populating workbook
* There are a couple of ways to run and create consolidated master files for the workbook:
    * Run **cotreporter.exe** (silently). Reports will create two files in [/data/master](/data/master).
    * Use bundled PowerShell script in [/pwsh](/pwsh) to schedule the task

* Open Excel and click *Refresh All* on *Data* tab to import and query master files

![wb_refresh_1](https://user-images.githubusercontent.com/8696078/192114676-0cb650ae-4039-45e9-a129-1aeea4da70ed.png)

The app will download all historical reports when first executed, but it will only append the report for the current year on each subsequent run. Note that these files are not datestamped, but a week number is appended to the file name when compressed and saved in [/data/archive](/data/archive).

Excel (without a VBA or macro-based solution) may require multiple clicks to completely refresh. However, there is another [PowerShell script](/pwsh/refreshExcel.ps1) included that will refresh the workbook in one go.

### Other Notes & Tips

* Do not enable content for workbook until paths to master files set (avoids warnings)
* Once template is set up, save as .xlsx (and update PowerShell config file if used)
* Native Excel add-ons may require enablement if prompted

## Disclaimer

If you choose to run this app automatically, please scrape responsibly and schedule it to run once per week when new reports are posted. Likewise, if you modify this code for any other related purpose, please read up on [ethical web scraping](https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/) before you do.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache 2.0](http://www.apache.org/licenses/)