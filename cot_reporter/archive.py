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
    # Opening archive in "w" mode and writing file to directory to not zip folder structure
    zipfile.ZipFile(f"{arcpath}/{rename}.zip", mode='w', compression=zipfile.ZIP_DEFLATED).write(file, arcname=rename) # Not adding .txt
    file_to_rem = Path(file) # Removing after writing to master data file
    file_to_rem.unlink()