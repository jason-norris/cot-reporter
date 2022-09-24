#!/usr/bin/env python3
import urllib.request
from datetime import date
from main import install_dir
from pathlib import Path

def download_reports():
    
    cwd = Path(install_dir / "cot-reporter")

    # Assigning opener agent to help us not look like a bot
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-Agent", "Mozilla/5.0")]
    urllib.request.install_opener(opener)

    # Assigning directory to check before downloading
    downloads_dir = Path(cwd / "data/download")

    # For the list of urls...
    data_dir = Path(cwd / "data")
    urlfile = f"{data_dir}/urls.txt"
    for url in open(urlfile):

        # Parsing source file names from list
        # Removing new line characters
        src_file = url.rsplit("/", 1)[-1].replace('\n','')

        # Creating current year string for source file comparison
        current_year = str(date.today().year)

        # Combining the name and the downloads directory to create destination path
        dst_path = Path(downloads_dir / src_file)

        # Downloading the file if it does not exist or if it is from the current year
        # Splitting source file date stamp and comparing to current year
        if not Path.is_file(dst_path) or src_file.rsplit("_", 1)[1].rsplit(".", 1)[0] == current_year:
            urllib.request.urlretrieve(url, dst_path)