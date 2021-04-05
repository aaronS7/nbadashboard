#!/bin/bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -o get-poetry.py
mkdir -p /workspace/poetry && POETRY_HOME=/workspace/poetry python get-poetry.py -y && rm get-poetry.py
echo "export PATH=/workspace/poetry/env:$PATH" >> /home/gitpod/.profile && source /workspace/poetry/env && echo "path is $(printenv PATH)"
poetry install