import pandas as pd
from pathlib import Path

arcpath = Path("data/archived/")
stagepath = Path("data/stage/")
targetpath = Path("data/workbooks/master")

arclist = list(arcpath.glob("*.zip"))
stagelist = list(stagepath.glob("fut_*.txt"))
targetlist = list(targetpath.glob("master_data.csv"))

masterfile = f"{targetpath}/master_data.csv"

# Reading multiple files into single master data file initially, then appending net new records after that
# For this project, two required reports contain same number of columns
if len(arclist) == 0: # No files previously archived

    dfs = []
    for file in stagelist:
        # Setting data type to string to not trim leading zeroes on codes
        # Setting header to "None" to avoid header misalignment on report date column
        # Adding header for indices, which will be ignored when writing out file below
        df = pd.read_csv(file, dtype=str, header=None, skipinitialspace=True)
        dfs.append(df)

    df_master = pd.concat(dfs, axis=0).drop_duplicates().reset_index(drop=True) # !! Testing deduping at this step
    filename = (f"{targetpath}/master_data.csv") # Writing out file if does not exist
    df_master.to_csv(filename, mode="a", index=False, header=False) # Using append mode and ignoring header of indices

else:
    for file in stagelist:
        new_data = pd.read_csv(file, dtype=str, header=None, skipinitialspace=True)

    for file in targetlist:
        existing_data = pd.read_csv(file, dtype=str, header=None, skipinitialspace=True)

    # Dropping duplicates recurring in new file and the known duplicates in existing file
    df_master = pd.concat([new_data, existing_data], ignore_index=True).drop_duplicates().reset_index(drop=True)
    df_master.to_csv(masterfile, index=False, header=False)