# read data in data

import glob
import pandas as pd


file_list = glob.glob("./data/*.parquet")

print(file_list)

df_list = []
for i in file_list:
    df = pd.read_parquet(i)
    df_list.append(df)
    print(df.shape)

df = pd.concat(df_list)
print(df.shape)
