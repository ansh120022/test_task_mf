This is the test task from Mayflower (or WiseBits)

# Quick start

Given that [Docker](https://www.docker.com/get-started/) installed, perform the following commands:

    1. docker build --tag tests . --no-cache
    2. docker run -it tests python3 -m pytest

The log expected to contain test's status (2 PASSED results)