# FOCUS ON MARKING CRITERIA FIRST
import pandas as pd
import os

os.system('cls')

boxrec_data = pd.read_csv('boxrec_tables.csv')

df = pd.DataFrame(boxrec_data)

div_list = ['heavy', 'cruiser', 'lightheavy', 'supermiddle', 'middle', 'superwelter', 'welter', 'superlight', 'light', 'feather', 'superbantam', 'bantam', 'superfly', 'fly', 'lightfly', 'minimum']

df.insert(3, 'div index', '')

x = 0

def view_top_20(dataframe):
    print(dataframe[['name', 'division','bouts', 'rounds', 'KOs']].head(20))

for value in df['division']:
    # print(f'{value} - {div_list.index(value)}')
    df.at[x, 'div index'] = div_list.index(value)
    x += 1

ds = df.sort_values(by=['div index', 'division rating'], ascending=True)
# view_top_20(ds)


rounds = df.sort_values(by=['rounds'], ascending = False)
view_top_20(rounds)