import zipfile
from datetime import datetime
from pathlib import Path

arcpath = Path.cwd() / "data/archive"
stagepath = Path.cwd() / "data/stage"
stagelist = list(stagepath.glob("fut_*"))
wkDTS = datetime.now().strftime("%V")

# Archiving week-stamped files, moving, and deleting from stage
for file in stagelist:
    rename = f"{file.stem}_{wkDTS}"
    # Open archive in "w" mode and write file to directory to not zip folder structure
    zipfile.ZipFile(f"{arcpath}/{rename}.zip", mode='w', compression=zipfile.ZIP_DEFLATED).write(file, arcname=rename)
    # Move file by replacing to archive
    file_to_rem = Path(file) # Delete file after writing to master data file
    file_to_rem.unlink()