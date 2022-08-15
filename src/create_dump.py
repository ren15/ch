import pandas as pd
import shutil

df = pd.read_parquet("data/trips.parquet")

print(df.shape)

df.to_parquet("data/trips.parquet")

for i in range(70):
    shutil.copy("data/trips.parquet", f"data/trips{i}.parquet")
