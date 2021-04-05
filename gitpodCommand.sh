#!/bin/bash
source /home/gitpod/.profile
echo "export POETRY_MODULES=$(realpath $(find $(POETRY_CACHE_DIR) -path "*/bin"))" >> /home/gitpod/.profile && source /home/gitpod/.profile
echo "export PATH=$POETRY_MODULES:$PATH" >> /home/gitpod/.profile