# Quick start

Given, that [Docker](https://www.docker.com/get-started/). installed

    docker build --tag tests . --no-cache
    docker run -it tests python3 -m pytest