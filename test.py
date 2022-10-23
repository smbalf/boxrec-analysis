import pandas as pd
import numpy as np
import os

os.system('cls')


df = pd.DataFrame({'A': ['bat', 'foo', 'bait'],
                   'B': ['abc', 'bar', 'xyz']})

print(df)

df.replace(to_replace=r'^ba.$', value='new', regex=True, inplace=True)
print(df)