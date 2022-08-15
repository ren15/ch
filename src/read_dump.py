from datetime import datetime
import pandas as pd

df = pd.read_parquet("data/trips.parquet")

print(df.shape)

df_list = []

concat_num = 20

print("Start concating at ", datetime.now().strftime("%H:%M:%S"))

for i in range(concat_num):
    df_list.append(df)

df_10 = pd.concat(df_list)

print("Finish concating at ", datetime.now().strftime("%H:%M:%S"))

for i in range(concat_num):
    df_10.to_parquet(f"data/trips{i}.parquet")

print("Finish to_parquet at ", datetime.now().strftime("%H:%M:%S"))
