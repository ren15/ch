set -xe

sudo clickhouse start

eval "$(${HOME}/miniconda3/bin/conda shell.bash hook)"

python --version
which python
pip --version

