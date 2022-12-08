import pandas as pd

# read the first CSV file into a dataframe called "df1"
df1 = pd.read_csv("bout_data.csv")

# read the second CSV file into a dataframe called "df2"
# specify that the first column has no header and should be named "name"
df2 = pd.read_csv("tables_test.csv", header=None, names=["name", "bout number", "outcome", "opp name"])

# merge the two dataframes based on the "name" column
df = pd.merge(df1, df2, on="name")

# create a multi-indexed dataframe by setting the "name" and "outcome" columns as the index
df.set_index(["name", "outcome"], inplace=True)

print(df)