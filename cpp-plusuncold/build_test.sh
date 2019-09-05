#!/bin/bash

# Put your build command here
# e.g. cargo build --release
g++ -march=native -Ofast -fomit-frame-pointer main.cpp timer.cpp
