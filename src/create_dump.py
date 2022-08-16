import pandas as pd
import shutil
import sys

df = pd.read_parquet("data/trips.parquet")

print(df.shape)

df.to_parquet("data/trips.parquet")

cnt = int(sys.argv[1])

for i in range(cnt):
    shutil.copy("data/trips.parquet", f"data/trips{i}.parquet")
