

# https://clickhouse.com/docs/en/tutorial


```bash
clickhouse-client --password --query="SELECT pickup_datetime,store_and_fwd_flag,rate_code_id FROM trips FORMAT Parquet" > trips.parquet
```