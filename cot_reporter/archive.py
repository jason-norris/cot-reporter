from datetime import datetime
from pathlib import Path

# Assign working directory as script location
cwd = Path(__file__)

# Assign source path and set file timestamp
source = Path("data/f_year.txt")
dts = datetime.now().strftime("%Y%m%d%H%M%S")
rename = f"f_year.txt.{dts}"

# Move single file
target = source.replace(cwd.parent / "archive" / rename)