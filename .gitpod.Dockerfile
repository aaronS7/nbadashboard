FROM gitpod/workspace-full:latest

USER gitpod

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -o get-poetry.py
RUN POETRY_HOME=/workspace/poetry python get-poetry.py -y && rm get-poetry.py
