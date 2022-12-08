import pandas as pd
import numpy as np
import os
from pathlib import Path

os.system('cls')

boxrec_tables_path = "C:/Users/smbal/Desktop/Data Science MSc/General/Web Scraping/analysis/boxrec-analysis/tables_test.csv"
bout_data_path = "C:/Users/smbal/Desktop/Data Science MSc/General/Web Scraping/analysis/boxrec-analysis/bout_data_test.csv"

boxrec_tables = pd.read_csv(Path(boxrec_tables_path),index_col=[0,1]).rename_axis(['name', 'bout number'])
bout_data = pd.read_csv(Path(bout_data_path))

bt_df = pd.DataFrame(boxrec_tables)
bd_df = pd.DataFrame(bout_data)

























"""
df = (bd_df.join(bt_df.set_index('outcome', drop=False)).set_index('name',append=True))
print(df)

main_df = (bt_df.assign(g = bt_df.groupby(level=0).cumcount())
                .reset_index()
                .merge(bd_df[::-1].reset_index(drop=True), 
                       left_on='g',
                       right_index=True, 
                       how='left', 
                       suffixes=('_',''))
                .set_index(['name_', 'bout number'])
                )
print(main_df)
"""