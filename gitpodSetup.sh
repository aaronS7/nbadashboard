#!/bin/bash
touch /workspace/aarpn.txt
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -o get-poetry.py && POETRY_HOME=/workspace/poetry python get-poetry.py -y && rm get-poetry.py
echo "export PIP_USER=no" >> /home/gitpod/.profile && echo "export POETRY_CACHE_DIR=/workspace/.cache/pypoetry" >> /home/gitpod/.profile
source /home/gitpod/.profile