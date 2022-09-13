import re
from bs4 import BeautifulSoup

# Open and parse html
with open("data/index.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

# Define desired report
report = "fut_disagg_txt"

# Define regex function for desired attribute
def targetlink(href):
    return href and re.compile(report).search(href)

# Required to conduct full historic load and then incremental loads week-over-week
# Solution could be to create two paths:
# 1) if nothing in archived location, grab all urls;
# 2) if files in archive, then only url with latest year

# Pass in a function to filter and return links
# Write links for non-historical files
with open("data/urls.txt", "w") as file:
    for link in soup.find_all(href=targetlink):
        if "_hist_" not in str(link):
            file.write("https://www.cftc.gov" + str(link.get("href") + "\n"))