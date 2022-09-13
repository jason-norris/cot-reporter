import os
import zipfile
from datetime import datetime
from pathlib import Path

cwd = Path(__file__).parent
src_dir = (f"{cwd.parent}\data\downloaded")
dst_dir = (f"{cwd.parent}\data\stage")

# Extract downloaded files to staging folder and ensure file name uniqueness
for filename in os.listdir(src_dir):
    arcpath = os.path.join(src_dir, filename) # Get archive file path
    if arcpath.endswith(".zip"): # Check extension
        zip_obj = zipfile.ZipFile(arcpath)
        zip_obj.extractall(f"{dst_dir}") # Extract archive to destination directory
        zip_obj.close()
    unarc = os.path.join((f"{dst_dir}\\f_year.txt")) # Get unarchived file path (Need to variabalize for new FinFutYY report
    dts = datetime.now().strftime("%Y%m%d%H%M%S%f") # Create timestamp for uniqueness
    renfile = (f"f_year.{dts}.txt") # Create new file name
    unarc = os.rename(unarc, os.path.join((f"{dst_dir}\\{renfile}"))) # Set unarchived file to new file name