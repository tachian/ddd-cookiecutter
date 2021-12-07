#!/bin/bash

apt-get update && apt-get install -qq -y \
    libpq-dev libssl-dev build-essential \
    openssh-client libcurl4-openssl-dev && \
pip install flask-shell-ipython
