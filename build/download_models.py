#!/usr/bin/env python3
import os
from huggingface_hub import snapshot_download

def download_models():
    # Download HunyuanVideo without specifying local_dir
    print("Downloading HunyuanVideo...")
    snapshot_download(
        repo_id="hunyuanvideo-community/HunyuanVideo",
        local_dir_use_symlinks=False
    )

    # Download flux_redux_bfl
    print("Downloading flux_redux_bfl...")
    snapshot_download(
        repo_id="lllyasviel/flux_redux_bfl",
        local_dir_use_symlinks=False
    )

    # Download FramePackI2V_HY model
    print("Downloading FramePackI2V_HY...")
    snapshot_download(
        repo_id="lllyasviel/FramePackI2V_HY",
        local_dir_use_symlinks=False
    )

    print("All models downloaded successfully!")


if __name__ == '__main__':
    download_models()
