set -e

sudo clickhouse start

eval "$(${HOME}/miniconda3/bin/conda shell.bash hook)"

set -x

python --version
which python
pip --version

