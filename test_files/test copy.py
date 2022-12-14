import pandas as pd
import numpy as np
import os
from pathlib import Path
import csv

os.system('cls')

tables_test_path = "C:/Users/smbal/Desktop/Data Science MSc/General/Web Scraping/analysis/boxrec-analysis/tables_test.csv"
bout_data_path = "C:/Users/smbal/Desktop/Data Science MSc/General/Web Scraping/analysis/boxrec-analysis/bout_data_test.csv"

tables_test = pd.read_csv(Path(tables_test_path),index_col=[0,1]).rename_axis(['name', 'bout'])
bout_data = pd.read_csv(Path(bout_data_path))

tt_df = pd.DataFrame(tables_test)
bd_df = pd.DataFrame(bout_data)


# unstack the tt_df dataframe to create a new dataframe with one row per combination of name, bout, outcome, and opp_name
unstacked_tt_df = tt_df.unstack(1)
print(unstacked_tt_df)

# merge the unstacked_tt_df dataframe with the bd_df dataframe on the name column
merged_df = bd_df.merge(unstacked_tt_df, on='name')

print(merged_df)

merged_df.to_csv('testbout.csv')