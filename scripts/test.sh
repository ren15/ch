set -e

sudo clickhouse start

eval "$(${HOME}/miniconda3/bin/conda shell.bash hook)"

set -x

python --version
which python
pip --version

pip install \
    pandas pyarrow \
    clickhouse_driver[lz4,zstd,numpy] \
    matplotlib \
    psutil

# ----------------------------------------------------

echo "import sql/insert_trips.sql"

# bash scripts/free_loop.sh > /tmp/free_output.txt & 
python src/monitor.py &

clickhouse-client < sql/trips_schema.sql
clickhouse-client < sql/insert_trips.sql

clickhouse-client --database=default --query='SHOW tables'

clickhouse-client --database=default --query='SELECT * FROM trips LIMIT 3'

mkdir data

export query="
SELECT pickup_datetime,store_and_fwd_flag,rate_code_id 
FROM trips FORMAT Parquet
"
clickhouse-client --query="${query}" > data/trips.parquet

ls data/
du -d1 -h data

python src/create_dump.py 20

ls data/
du -d1 -h data

python src/concat_by_pd.py

python src/concat_by_ch.py MergeTree


kill $(ps -elf | grep 'python src/monitor.py' | head -1 | cut -d' ' -f7)
