FROM ubuntu:latest
USER root
WORKDIR /home/app

RUN apt-get update
RUN apt-get install -y \
    bash \
    build-essential \
    cargo \
    python3 \
    rustc \
    curl \
    gnupg \
    python3-pip

RUN pip3 install -U pip six

RUN curl -sL https://deb.nodesource.com/setup_11.x  | bash -
RUN apt-get -y install nodejs
RUN npm install

COPY . /home/
ENTRYPOINT python3 /home/run_tests.py
