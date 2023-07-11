# read data in data

import glob
import time
import os

import pandas as pd
from arcticdb import Arctic


file_list = glob.glob("./data/*.parquet")

print("before reading")
os.system("free -h")


ac = Arctic("lmdb://ac_data")
ac.create_library("trip_concat")
lib = ac["trip_concat"]

df_list = []
for i in file_list:
    df = pd.read_parquet(i)
    lib.write("trip_concat", df)

print("After reading")
os.system("free -h")

start_t = time.time()

df = lib.read("trip_concat").data
print(df)

end_t = time.time()

print("After concat")
os.system("free -h")


print(f"concat {len(file_list)} parquet files")
print(df.shape)
print(f"Cost time: {end_t - start_t}")
