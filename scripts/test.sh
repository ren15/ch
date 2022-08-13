set -e

sudo clickhouse start

eval "$(${HOME}/miniconda3/bin/conda shell.bash hook)"

set -x

python --version
which python
pip --version

clickhouse-client --query='SHOW databases'

clickhouse-client < sql/trips_schema.sql

clickhouse-client < sql/insert_trips.sql

clickhouse-client --database=default --query='SHOW tables'

clickhouse-client --database=default --query='SELECT * FROM trips LIMIT 10'

