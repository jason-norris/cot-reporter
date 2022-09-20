#!/usr/bin/env python3
import re
import urllib.request
from bs4 import BeautifulSoup
from datetime import date
from main import install_dir
from pathlib import Path

def get_report_links():

    cwd = Path(install_dir / "cot-reporter")
    data_dir = Path(cwd / "data")
    htmlfile = f"{data_dir}/index.html"
    urlfile = f"{data_dir}/urls.txt"

    # Assigning opener agent to not look like a bot
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-Agent", "Mozilla/5.0")]
    urllib.request.install_opener(opener)

    # Retrieving website html
    urllib.request.urlretrieve("http://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm", htmlfile)

    # Parsing html
    with open(htmlfile) as fp:
        soup = BeautifulSoup(fp, "html.parser")

    # Defining regex function for desired reports
    def targetlink(href):
        return href and re.compile(r"(fut_disagg_txt|fut_fin_txt)").search(href)

    # Required to conduct full historic load and then incremental loads week-over-week
    # If nothing in archived location, grab all urls; else...
    # if file in archive, then only url with current year

    arcpath = Path(data_dir / "archive")
    arclist = list(arcpath.glob("*.zip"))
    current_year = str(date.today().year)

    if len(arclist) == 0:
        # Passing in a function to filter and return links
        # Writing links for historical files (initial download)
        with open(urlfile, "w") as file:
            for link in soup.find_all(href=targetlink):
                if "_hist_" not in str(link): # For fut_disagg_text, do not get 2006 - 2016 file
                    file.write("https://www.cftc.gov" + str(link.get("href") + "\n"))
    else:
        # Writing links for non-historical files (weekly refresh)
        with open(urlfile, "w") as file:
            for link in soup.find_all(href=targetlink):
                if "_hist_" not in str(link) and str(link).rsplit("_txt_", 1)[1].rsplit(".", 1)[0] == current_year:
                    file.write("https://www.cftc.gov" + str(link.get("href") + "\n"))