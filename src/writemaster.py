#!/usr/bin/env python
import pandas as pd
from main import install_dir
from pathlib import Path

def write_master_data():

    cwd = Path(install_dir / "cot-reporter")

    data_dir = Path(cwd / "data")
    arcpath = Path(data_dir / "archive")
    stagepath = Path(data_dir / "stage")
    targetpath = Path(data_dir / "master")
    arclist = list(arcpath.glob("*.zip"))
    reports = ["fut_fin","fut_disagg"]

    # Reading multiple files into single master data file initially, then appending net new records after that
    for r in reports:

        rst = r[0:5]
        stagelist = list(stagepath.glob(f"{rst}*.txt"))

        if len(arclist) == 0: # No files previously archived

            dfs = []
            for file in stagelist:
                # Setting data type to string to not trim leading zeroes on codes
                # Setting header to "None" to avoid header misalignment on report date column
                # Adding header for indices, which will be ignored when writing out file below
                df = pd.read_csv(file, dtype=str, header=None, skipinitialspace=True).drop_duplicates().reset_index(drop=True)
                dfs.append(df)

            df_master = pd.concat(dfs, axis=0)
            masterfile = (f"{targetpath}/master_data_{rst}.csv")
            df_master.to_csv(masterfile, mode="a", index=False, header=False) # Using append mode and ignoring header of indices

        else:
            for file in stagelist:
                new_data = pd.read_csv(file, dtype=str, header=None, skiprows=1, skipinitialspace=True) # Skipping header after historical load

            masterfile = (f"{targetpath}/master_data_{rst}.csv")
            existing_data = pd.read_csv(masterfile, dtype=str, header=None)

            # Dropping duplicates recurring in new file and the known duplicates in existing file
            df_master = pd.concat([existing_data, new_data], axis=0).drop_duplicates().reset_index(drop=True) # Ordering concat matters to not lose header
            df_master.to_csv(masterfile, index=False, header=False)