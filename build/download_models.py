#!/usr/bin/env python3
import os
from huggingface_hub import snapshot_download


def download_models():
    # Define the specific subfolders for HunyuanVideo
    hunyuanvideo_subfolders = [
        "text_encoder/*",
        "text_encoder_2/*",
        "tokenizer/*",
        "tokenizer_2/*",
        "vae/*"
    ]

    # Download HunyuanVideo components
    hunyuanvideo_path = snapshot_download(
        repo_id="hunyuanvideo-community/HunyuanVideo",
        allow_patterns=hunyuanvideo_subfolders,
        repo_type="model"
    )
    print(f"Downloaded HunyuanVideo components to: {hunyuanvideo_path}")

    # Download flux_redux_bfl components
    flux_redux_subfolders = [
        "feature_extractor/*",
        "image_encoder/*"
    ]

    flux_redux_path = snapshot_download(
        repo_id="lllyasviel/flux_redux_bfl",
        allow_patterns=flux_redux_subfolders,
        repo_type="model"
    )
    print(f"Downloaded flux_redux_bfl components to: {flux_redux_path}")

    # Download FramePackI2V_HY components
    framepacked_path = snapshot_download(
        repo_id="lllyasviel/FramePackI2V_HY",
        repo_type="model"
    )
    print(f"Downloaded FramePackI2V_HY to: {framepacked_path}")

    # Download FramePackI2V_F1_HY components
    framepacked_path = snapshot_download(
        repo_id="lllyasviel/FramePack_F1_I2V_HY_20250503",
        repo_type="model"
    )
    print(f"Downloaded FramePackI2V_F1_HY to: {framepacked_path}")

if __name__ == '__main__':
    download_models()
