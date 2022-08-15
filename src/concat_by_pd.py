# read data in data

import glob
import pandas as pd
import time
import os


file_list = glob.glob("./data/*.parquet")

print("before reading")
os.system("free -h")

cnt = 70

start_t = time.time()

df_list = []
for i in range(cnt):
    df = pd.read_parquet(file_list[0])
    df_list.append(df)

print("After reading")
os.system("free -h")

df = pd.concat(df_list)

end_t = time.time()

print("After concat")
os.system("free -h")


print(f"concat {cnt} parquet files")
print(df.shape)
print(f"Cost time: {end_t - start_t}")
