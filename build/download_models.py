#!/usr/bin/env python3
import os
from huggingface_hub import hf_hub_download, snapshot_download


def download_models():
    # Create directories
    os.makedirs("pretrained_models/HunyuanVideo", exist_ok=True)
    os.makedirs("pretrained_models/flux_redux_bfl", exist_ok=True)
    os.makedirs("pretrained_models/FramePackI2V_HY", exist_ok=True)

    # Download HunyuanVideo subfolders
    snapshot_download(
        repo_id="hunyuanvideo-community/HunyuanVideo",
        subfolder="text_encoder",
        local_dir="pretrained_models/HunyuanVideo/text_encoder",
        local_dir_use_symlinks=False
    )

    snapshot_download(
        repo_id="hunyuanvideo-community/HunyuanVideo",
        subfolder="text_encoder_2",
        local_dir="pretrained_models/HunyuanVideo/text_encoder_2",
        local_dir_use_symlinks=False
    )

    snapshot_download(
        repo_id="hunyuanvideo-community/HunyuanVideo",
        subfolder="tokenizer",
        local_dir="pretrained_models/HunyuanVideo/tokenizer",
        local_dir_use_symlinks=False
    )

    snapshot_download(
        repo_id="hunyuanvideo-community/HunyuanVideo",
        subfolder="tokenizer_2",
        local_dir="pretrained_models/HunyuanVideo/tokenizer_2",
        local_dir_use_symlinks=False
    )

    snapshot_download(
        repo_id="hunyuanvideo-community/HunyuanVideo",
        subfolder="vae",
        local_dir="pretrained_models/HunyuanVideo/vae",
        local_dir_use_symlinks=False
    )

    # Download flux_redux_bfl subfolders
    snapshot_download(
        repo_id="lllyasviel/flux_redux_bfl",
        subfolder="feature_extractor",
        local_dir="pretrained_models/flux_redux_bfl/feature_extractor",
        local_dir_use_symlinks=False
    )

    snapshot_download(
        repo_id="lllyasviel/flux_redux_bfl",
        subfolder="image_encoder",
        local_dir="pretrained_models/flux_redux_bfl/image_encoder",
        local_dir_use_symlinks=False
    )

    # Download FramePackI2V_HY model
    snapshot_download(
        repo_id="lllyasviel/FramePackI2V_HY",
        local_dir="pretrained_models/FramePackI2V_HY",
        local_dir_use_symlinks=False
    )

    print("All models downloaded successfully!")


if __name__ == '__main__':
    download_models()
