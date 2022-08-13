set -xe

docker build -t dev_container scripts

docker run -it --rm \
    --user $(id -u):$(id -g) \
    -v /etc/passwd:/etc/passwd:ro \
    -v /etc/group:/etc/group:ro \
    -v /etc/shadow:/etc/shadow:ro \
    -v ${PWD}:/app \
    -w /app \
    dev_container:latest \
    bash
    # bash -c "bash scripts/test.sh"