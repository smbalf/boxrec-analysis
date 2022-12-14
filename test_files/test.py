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

df1 = pd.read_csv(boxrec_tables_path)



# Group the rows by the "name" column and combine the "bout", "outcome", and "opp name" columns into a single column
df1 = df1.groupby("name")

df1 = df1.pivot_table(index="bout", values=["outcome", "opp name"])
# Merge the dataframes using the "name" column to match rows
# Keep the rows from the first dataframe and discard any duplicates from the second dataframe
df = pd.merge(df1,bt_df , on="name", how="left")

# Save the resulting dataframe to a new CSV file
df.to_csv("merged_file.csv", index=False)




"""
Sam
I have a CSV file in this format: name,bout,outcome,opp name
Sam,3,win,Roy Jones
Sam,2,win,Floyd Mayweather
Sam,1,win,Bernard Hopkins
James,3,win,James Bond
James,2,win,Michael O'Terry
James,1,win,Donald Trump
Jonny,3,win,Oscar De la Hoya
Jonny,2,win,Roberto Duran
Jonny,1,loss,Manny Pacquiao
Dyaus,3,win,Thierry Henry
Dyaus,2,win,David Beckham
Dyaus,1,loss,Gabriel Jesus



the first column "name" has name values for a boxer, the second column has the bout ID, the third column has the outcome of the bout, and the last column has the name of the opponent in the bout, do you understand?

yes there is, but first take a look at this second CSV file:

name,country,colour,wins,losses
Sam,England,red,10,0
Jonny,China,blue,9,3
Dyaus,Italy,white,3,8
James,France,green,12,6

here the first column represents the boxer's name, the second their country of birth, the third column their favourite colour, the fourth column the number of wins that they have, and the fifth column the number of losses. 

take note that both CSV files have the same boxer's having their data recorded. do you understand?


I want to use python to merge the two CSV files into a single CSV file. I would like to incorporate the data from the first CSV file into the second CSV file, however I would not like to repeat rows with the "name" value. 

I would like it in a format such as the below for example:

name,country,colour,wins,losses,bout,outcome,opp name
Sam,England,red,10,0,3,win,Roy Jones
                        2,win,Floyd Mayweather
                        1,win,Bernard Hopkins
Jonny,China,blue,9,3,3,win,Oscar De la Hoya
                        2,win,Roberto Duran
                        1,loss,Manny Pacquiao
Dyaus,Italy,white,3,8,3,win,Thierry Henry
                        2,win,David Beckham
                        1,loss,Gabriel Jesus
James,France,green,12,6,3,win,James Bond
                        2,win,Michael O'Terry
                        1,win,Donald Trump

How could I go about this?

"""











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