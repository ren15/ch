set -e

eval "$(${HOME}/miniconda3/bin/conda shell.bash hook)"

set -x

python src/create_image_from_csv.py


