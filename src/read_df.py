# read data in data

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
for i in file_list[:cnt]:
    df = pd.read_parquet(i)
    df_list.append(df)
    print(df.shape)

print("After reading")

os.system("free -h")

time.sleep(5)

df = pd.concat(df_list)

print("After concat")
os.system("free -h")

print(df.shape)
