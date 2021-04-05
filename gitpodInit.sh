#!/bin/bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -o get-poetry.py
mkdir -p /workspace/poetry && POETRY_HOME=/workspace/poetry python get-poetry.py -y && rm get-poetry.py
echo "export PATH=/workspace/poetry/bin:$PATH" >> /home/gitpod/.profile && source /home/gitpod/.profile
poetry install