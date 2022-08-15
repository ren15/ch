import glob
import pandas as pd
import time
import os


file_list = glob.glob("./data/*.parquet")

cnt = 2
print(cnt)

print("before reading")
os.system("free -h")

df_list = []
for i in file_list[:1]:
    df = pd.read_parquet(i)
    df_list.append(df)
    print(df)
    print(df.shape)
    print(df.dtypes)
