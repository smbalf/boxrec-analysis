import os
import pandas as pd
import numpy as np

os.system('cls')

def view_top_20(dataframe):
    print(dataframe[['name', 'division','bouts', 'rounds', 'KOs']].head(20))

boxrec_data = pd.read_csv('boxrec_tables.csv')
df = pd.DataFrame(boxrec_data)

df.replace(to_replace='None', value=np.nan, regex=True, inplace=True)

df.insert(3, 'div index', '')

div_list = ['heavy', 'cruiser', 'lightheavy', 'supermiddle', 'middle', 'superwelter', 'welter', 'superlight', 'light', 'feather', 'superbantam', 'bantam', 'superfly', 'fly', 'lightfly', 'minimum']

# Sort for heaviest weight to lightest weight (heavy > minimum)
# Sorting by 'division' won't work as values are strings
x = 0
for value in df['division']:
    df.at[x, 'div index'] = div_list.index(value)
    x += 1

ds = df.sort_values(by=['div index', 'division rating'], ascending=True)
rounds = df.sort_values(by=['rounds'], ascending = False)

cols_to_convert = ['age', 'height', 'reach']

for col in cols_to_convert:
    ds[col] = ds[col].astype(float)

average_by_division = ds.groupby(['division']).mean(numeric_only=True)

average_everything_numeric = ds.mean(numeric_only=True)

def replace_with_mean(column):
    pass

print(average_by_division['age'])


