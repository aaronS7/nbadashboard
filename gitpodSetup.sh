#!/bin/bash
echo "export PIP_USER=no" >> /home/gitpod/.profile
echo "export POETRY_CACHE_DIR=/workspace/.cache/pypoetry" >> /home/gitpod/.profile
source /home/gitpod/.profile
