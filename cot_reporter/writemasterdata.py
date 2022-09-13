import pandas as pd
from pathlib import Path

stagepath = Path.cwd() / "data/stage/"
targetpath = Path.cwd() / "data/workbooks/master"
futfls = list(stagepath.glob("fut_fin_*.txt"))
futdls = list(stagepath.glob("fut_disagg_*.txt"))

# Need to rewrite this section to use single for loop (iterate over list of lists)
# !! Need to rewrite to read both existing data and new data, concatenate, and dedupe !!
# Create master data file for first report
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