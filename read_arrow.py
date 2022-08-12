import pandas as pd
import pyarrow as pa

df = pd.read_parquet("trips.parquet")

print(df)



