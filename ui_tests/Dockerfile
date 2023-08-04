FROM selenium/standalone-chrome

WORKDIR /code/test_sql_runner

COPY . /code/test_sql_runner

RUN sudo apt update && sudo apt install -y python3.9 && sudo apt install -y python3-pip
RUN pip install -r requirements.txt