#!/usr/bin/env bash

export PYTHONUNBUFFERED=1
echo "Starting FramePack-Studio"
source /venv/bin/activate
cd /FramePack-Studio
TCMALLOC="$(ldconfig -p | grep -Po "libtcmalloc.so.\d" | head -n 1)"
export LD_PRELOAD="${TCMALLOC}"
nohup python3 studio.py \
    --server 0.0.0.0 \
    --port 3001 > /var/log/framepack.log 2>&1 &
echo "FramePack-Studio started"
echo "Log file: /var/log/framepack.log"
deactivate
