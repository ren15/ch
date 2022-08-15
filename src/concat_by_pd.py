# read data in data

import glob
import pandas as pd
import time
import os


file_list = glob.glob("./data/*.parquet")

print("before reading")
os.system("free -h")

cnt = 70

df_list = []
for i in range(cnt):
    df = pd.read_parquet(file_list[0])
    df_list.append(df)

print("After reading")

os.system("free -h")

time.sleep(5)

df = pd.concat(df_list)

print("After concat")
os.system("free -h")

time.sleep(2)

print(f"concat {cnt} parquet files")
print(df.shape)
