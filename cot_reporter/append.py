# importing the required modules
import glob
import pandas as pd
 
# specifying the path to csv files
path = "stage/"
 
# csv files in the path
file_list = glob.glob(f"{path}/*.xlsx")
 
# list of excel files we want to merge.
# pd.read_excel(file_path) reads the 
# excel data into pandas dataframe.
excl_list = []
 
for file in file_list:
    excl_list.append(pd.read_excel(file))
 
# concatenate all DataFrames in the list
# into a single DataFrame, returns new
# DataFrame.
excl_merged = pd.concat(excl_list, ignore_index=True)
 
# exports the dataframe into excel file
# with specified name.
excl_merged.to_excel("merge/CoT_wb.xlsx", index=False)