set -x

eval "$(${HOME}/miniconda3/bin/conda shell.bash hook)"


set -e

python src/create_image_from_csv.py



