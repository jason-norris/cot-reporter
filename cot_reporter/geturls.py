import re
import urllib.request
from bs4 import BeautifulSoup
from datetime import date
from pathlib import Path

# Assign opener agent to not look like a bot
opener = urllib.request.build_opener()
opener.addheaders = [("User-Agent", "Mozilla/5.0")]
urllib.request.install_opener(opener)

# Retrieve website html
urllib.request.urlretrieve("http://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm", "data/index.html")

# Open and parse html
with open("data/index.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

# Define regex function for desired attribute
def targetlink(href):
    # return href and re.compile(report).search(href)
    return href and re.compile(r"(fut_disagg_txt|fut_fin_txt)").search(href)

# Required to conduct full historic load and then incremental loads week-over-week
# 1) if nothing in archived location, grab all urls;
# 2) if file in archive, then only url with current year

arcpath = Path("data/archived/")
arclist = list(arcpath.glob("*.txt"))
current_year = str(date.today().year)

if len(arclist) == 0:
    # Pass in a function to filter and return links
    # Write links for non-historical files
    with open("data/urls.txt", "w") as file:
        for link in soup.find_all(href=targetlink):
            if "_hist_" not in str(link): # For fut_disagg_text, do not get 2006 - 2016 file
                file.write("https://www.cftc.gov" + str(link.get("href") + "\n"))
else:
    with open("data/urls.txt", "w") as file:
        for link in soup.find_all(href=targetlink):
            if "_hist_" not in str(link) and str(link).rsplit("_txt_", 1)[1].rsplit(".", 1)[0] == current_year:
                file.write("https://www.cftc.gov" + str(link.get("href") + "\n"))