import glob
import os
import time


import pandas as pd
from clickhouse_driver import Client


def delete_table():
    client = Client('localhost', settings={'use_numpy': True})

    client.execute('DROP TABLE IF EXISTS trip_concat')


def create_table():
    client = Client('localhost', settings={
                    'use_numpy': True}, compression='zstd')

    a = client.execute(
        """
    CREATE TABLE trip_concat
    (
        `pickup_datetime` DateTime,
        `store_and_fwd_flag` UInt8,
        `rate_code_id` UInt8
    )
    ENGINE = MergeTree()
    ORDER BY pickup_datetime
        """
    )
    print(a)


def insert_table(file_list):
    client = Client('localhost', settings={
                    'use_numpy': True}, compression='zstd')
    print("Before ch insert")
    os.system("free -h")

    for i in file_list:
        df = pd.read_parquet(i)
        client.insert_dataframe('INSERT INTO trip_concat VALUES', df)
        # print(a)


def query_table():
    client = Client('localhost', settings={
                    'use_numpy': True}, compression='zstd')
    print("Before ch query")
    os.system("free -h")

    start_t = time.time()

    df = client.query_dataframe(
        'SELECT pickup_datetime,store_and_fwd_flag,rate_code_id '
        'FROM trip_concat'
    )

    end_t = time.time()
    print(df.shape)
    print(f"Cost time {end_t - start_t}")

    print("After ch query")
    os.system("free -h")


if __name__ == '__main__':
    file_list = glob.glob("./data/*.parquet")
    print("before reading")
    os.system("free -h")

    delete_table()
    create_table()
    insert_table(file_list)
    query_table()
