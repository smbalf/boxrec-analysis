# FOCUS ON MARKING CRITERIA FIRST
import pandas as pd
import numpy as np
import os

"""
To do:
- create per division mean value of:
    - rounds
    - age
    - bouts
    - age
    - losses
    - draws
    - height
    - reach
        - reach relative to height
    - time since debut >> == (current date - debut)

- for values missing in:
    - age:
        - no data = average age of division 
    - reach:
        - reach == (height + reach relative to height for division)
    - height:
        ???
    - stance:
        ???


for column in df:
    total_rows = len(df[column])
    if len(df[df[column]=='NODATA']) != 0:
        missing = len(df[df[column]=="NODATA"])
        pct_missing = round(((missing/total_rows)*100), 2)
        print(f'{column} - missing = {missing}/{total_rows} - pct missing = {pct_missing}%')

age - missing = 19/793 - pct missing = 2.4%
stance - missing = 82/793 - pct missing = 10.34%    
height - missing = 98/793 - pct missing = 12.36%    
reach - missing = 380/793 - pct missing = 47.92%    
birth place - missing = 79/793 - pct missing = 9.96%
"""

os.system('cls')

def view_top_20(dataframe):
    print(dataframe[['name', 'division','bouts', 'rounds', 'KOs']].head(20))

boxrec_data = pd.read_csv('boxrec_tables.csv')
df = pd.DataFrame(boxrec_data)
df.replace(to_replace=r'^NODAT.$', value=np.nan, regex=True, inplace=True)
df.insert(3, 'div index', '')

div_list = ['heavy', 'cruiser', 'lightheavy', 'supermiddle', 'middle', 'superwelter', 'welter', 'superlight', 'light', 'feather', 'superbantam', 'bantam', 'superfly', 'fly', 'lightfly', 'minimum']

x = 0
for value in df['division']:
    # print(f'{value} - {div_list.index(value)}')
    df.at[x, 'div index'] = div_list.index(value)
    x += 1

ds = df.sort_values(by=['div index', 'division rating'], ascending=True)
rounds = df.sort_values(by=['rounds'], ascending = False)

print(df.dtypes)