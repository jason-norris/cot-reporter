#!/usr/bin/env python3
import zipfile
from datetime import datetime
from main import install_dir
from pathlib import Path

def archive_files():

    cwd = Path(install_dir / "cot-reporter")
    data_dir = Path(cwd / "data")
    arcpath = Path(data_dir / "archive")
    stagepath = Path(data_dir / "stage")
    stagelist = list(stagepath.glob("fut_*"))
    wkDTS = datetime.now().strftime("%V") # Getting week number for file name

    # Archiving week-stamped files, moving, and deleting from stage
    for file in stagelist:
        rename = f"{file.stem}_{wkDTS}"
        # Opening archive in "w" mode and writing file to directory to not zip folder structure
        # Not adding .txt to filename to also prevent zipping folder structure
        zipfile.ZipFile(f"{arcpath}/{rename}.zip", mode='w', compression=zipfile.ZIP_DEFLATED).write(file, arcname=rename)
        file_to_rem = Path(file) # Removing after writing to master data file
        file_to_rem.unlink()