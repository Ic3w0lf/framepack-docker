#!/usr/bin/env bash

export PYTHONUNBUFFERED=1
echo "Starting FramePack"
source /venv/bin/activate
cd /workspace/FramePack
TCMALLOC="$(ldconfig -p | grep -Po "libtcmalloc.so.\d" | head -n 1)"
export LD_PRELOAD="${TCMALLOC}"
export HF_HOME="/workspace"
nohup python3 demo_gradio.py \
    --server 0.0.0.0 \
    --port 3001 > /workspace/logs/framepack.log 2>&1 &
echo "FramePack started"
echo "Log file: /workspace/logs/framepack.log"
deactivate
