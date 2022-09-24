# Commitment of Traders (COT) Reporter

COT Reporter is a Python application for scraping weekly reports posted by the Commodity Futures Trading Commission ([CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm)) website and preparing them for presentation in Excel via PowerQuery and Power Pivot. To demonstrate how reports of interest can be automatically extracted, loaded, and transformed for analysis in pivot tables and charts, two reports were targeted in this pilot project - the [Disaggregated Futures](https://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm) and [Traders in Financial Futures](https://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm) - and a model with certain measures was created to present the [Blees Sentiment Rating](https://bit.ly/3S76uMm) for given markets week-over-week.

## Tech Choices
Python was selected for its convenient libraries in handling HTML or XML ([Beautiful Soup](https://pypi.org/project/beautifulsoup4/)) and various data structures ([pandas](https://pandas.pydata.org/)), while Excel was chosen for its accessibility as a BI tool. PowerQuery offers the necessary ETL functionality to manage the underlying CSVs created by the app, while PowerPivot acts as a suitable, if not robust, endpoint for the expected consumers of this data.

## Challenges and Future Plans
The primary challenge was in maintaining modularity for additional reports to be pulled and pushed to the model workbook. Attention was given to portability and dynamic paths overall.

Future updates will likely include:

- Logging and error handling
- Rewrites to leverage classes
- Console with progress bars
- Interactive installation

## Installation

Use the compressed folder to install COT Reporter.