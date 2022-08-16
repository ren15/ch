set -e

eval "$(${HOME}/miniconda3/bin/conda shell.bash hook)"

set -x

python src/monitor.py plot


