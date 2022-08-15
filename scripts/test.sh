set -e

sudo clickhouse start

eval "$(${HOME}/miniconda3/bin/conda shell.bash hook)"

set -x

python --version
which python
pip --version
pip install pandas pyarrow

# ----------------------------------------------------

echo "import sql/insert_trips.sql"

# bash scripts/free_loop.sh > /tmp/free_output.txt & 

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

python src/read_dump.py

ls data/
du -d1 -h data

python src/concat_by_pd.py

python src/concat_by_ch.py

