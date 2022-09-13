import zipfile
from pathlib import Path

src = Path.cwd() / "data/downloaded"
dst = Path.cwd() / "data/stage"

for f in src.glob('**/*.zip'):
    z = str(Path(src).joinpath(f))
    z_name = str(Path(z).stem)
    if z.endswith(".zip"):
        zip_obj = zipfile.ZipFile(z)
        zip_obj.extractall(str(dst))
        zip_obj.close()
    zl = zipfile.ZipFile.namelist(zip_obj) # Use namelist to get file name in archive
    uz = ''.join(map(str, zl)) # Use map function to convert list (of one in this case) to string
    new_name = "{}_{}".format(z_name, uz) # Use format to try new way of creating file name
    Path(dst / uz).rename((f"{dst}//{new_name}")) # Use pathlib exclusively to see if I can do without os