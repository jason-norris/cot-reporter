#!/usr/bin/env python3
from pathlib import Path
from configparser import ConfigParser

config = ConfigParser() 
configFilePath = Path(__file__).parent / "config.ini"
config.read(f"{configFilePath}")
install_dir = Path(config.get("SETUP", "install_dir"))

def main():

    # Moving import inside function to resolve circular import
    import geturls
    geturls.get_report_links()

    import download
    download.download_reports()

    import extract
    extract.extract_files()
    
    import writemaster
    writemaster.write_master_data()
    
    import archive
    archive.archive_files()

    print("Process complete!")

if __name__ == "__main__":
    main()