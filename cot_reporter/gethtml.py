import urllib.request

# Assign opener agent to not look like a bot and bypass website security
opener = urllib.request.build_opener()
opener.addheaders = [("User-Agent", "Mozilla/5.0")]
urllib.request.install_opener(opener)

# Retrieve website as txt
urllib.request.urlretrieve("http://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm", "index.html")