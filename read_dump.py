import pandas as pd

df = pd.read_parquet("trips.parquet")

print(df.shape)

df_list = []

for i in range(10):
    df_list.append(df)

df_10 = pd.concat(df_list)

for i in range(10):
    df_10.to_parquet(f"data/trips{i}.parquet")
