#!/usr/bin/env python3
import geturls
import download
import extract
import writemaster
import archive
from pathlib import Path
from configparser import ConfigParser

config = ConfigParser() 
configFilePath = Path(__file__).parent / "config.ini"
config.read(f"{configFilePath}")
install_dir = Path(config.get("SETUP", "install_dir")) # Converting path string to object

def main():

    geturls.get_report_links()
    download.download_reports()
    extract.extract_files()
    writemaster.write_master_data()
    archive.archive_files()

    print("Process complete!")

if __name__ == "__main__":
    main()