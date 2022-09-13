import os
import urllib.request
from datetime import date

# Assign opener agent to help us not look like a bot
opener = urllib.request.build_opener()
opener.addheaders = [("User-Agent", "Mozilla/5.0")]
urllib.request.install_opener(opener)

# Assign directory to check before downloading
downloads_dir = os.path.abspath("data/downloaded")

# For the list of urls...
for url in open("data/urls.txt"):

    # Parse source file name from list
    # Remove new line characters
    src_file = url.rsplit("/", 1)[-1].replace('\n','')

    # Create current year string for source file comparison
    current_year = str(date.today().year)

    # Combine the name and the downloads directory to create destination path
    dst_path = os.path.join(downloads_dir, src_file)

    # Download the file if it does not exist or if it is from the current year
    # Split source file date stamp and compare to current year
    # (Consider removing this line with changes made to geturls.py if/else for urls)
    if not os.path.isfile(dst_path) or src_file.rsplit("_", 1)[1].rsplit(".", 1)[0] == current_year:
        urllib.request.urlretrieve(url, dst_path)