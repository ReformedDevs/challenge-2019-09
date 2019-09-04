FROM node:11-alpine

RUN apk update && apk add \
    bash \
    build-base \
    cargo \
    python3 \
    rust

RUN pip3 install -U pip six

COPY . /home/
ENTRYPOINT python3 /home/run_tests.py
