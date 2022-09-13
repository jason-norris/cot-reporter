import pandas as pd
from pathlib import Path

arcpath = Path("data/archived/")
stagepath = Path("data/stage/")
targetpath = Path("data/workbooks/master") # !!Removed .cwd
dmasterfile = (f"{targetpath}/master_data_futd.csv")
fmasterfile = (f"{targetpath}/master_data_futf.csv")
arcls = list(arcpath.glob("*.zip"))
futfls = list(stagepath.glob("fut_fin_*.txt"))
futdls = list(stagepath.glob("fut_disagg_*.txt"))
targetls = list(targetpath.glob("master*.csv"))

# Need to rewrite this section to use single for loop (iterate over list of lists)
# !! Need to rewrite to read both existing data and new data, concatenate, and dedupe !!
# Create master data file for first report

if len(arcls) == 0:

    dfsf = []
    for file in futfls:
        # Set data type to string to not trim leading zeroes on codes
        # To avoid header misalignment on report date column, set header to "None":
        # This will add a header for indices, which will be ignored when writing out file below
        df = pd.read_csv(file, dtype=str, header=None, skipinitialspace=True)
        dfsf.append(df)

    dff_master = pd.concat(dfsf, axis=0)
    filename = (f"{targetpath}/master_data_futf.csv") # Will write out file if does not exist
    dff_master.to_csv(filename, mode="a", index=False, header=False) # Append mode and ignore header of indices

    # Create master data file for second report
    dfsd = []
    for file in futdls:
        df = pd.read_csv(file, dtype=str, header=None, skipinitialspace=True)
        dfsd.append(df)

    dfd_master = pd.concat(dfsd, axis=0)
    filename = (f"{targetpath}/master_data_futd.csv") # Will write out file if does not exist
    dfd_master.to_csv(filename, mode="a", index=False, header=False) # Append mode and ignore header of indices

else:

    for file in futfls:
        new_data = pd.read_csv(file, dtype=str, header=None, skipinitialspace=True)

    for file in targetls:
        existing_data = pd.read_csv(file, dtype=str, header=None, skipinitialspace=True)

    # Drop duplicates recurring in new file and known duplicates in existing file
    dff_master = pd.concat([new_data, existing_data], ignore_index=True).drop_duplicates().reset_index(drop=True)
    dff_master.to_csv(fmasterfile, index=False, header=False)