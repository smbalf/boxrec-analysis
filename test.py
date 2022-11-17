import pandas as pd
import numpy as np
import os

os.system('cls')

bout_data = pd.read_csv('bout_data.csv',index_col=[0,1])
print(bout_data)

second_df = pd.DataFrame(bout_data)