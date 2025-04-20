#!/usr/bin/env python3
import os
from huggingface_hub import hf_hub_download, snapshot_download


def download_models():
    # Create directories
    os.makedirs("pretrained_models/HunyuanVideo", exist_ok=True)
    os.makedirs("pretrained_models/flux_redux_bfl", exist_ok=True)
    os.makedirs("pretrained_models/FramePackI2V_HY", exist_ok=True)

    # For HunyuanVideo
    # First download the entire repo
    full_repo = snapshot_download(
        repo_id="hunyuanvideo-community/HunyuanVideo",
        local_dir="pretrained_models/HunyuanVideo_full",
        local_dir_use_symlinks=False
    )

    # Then move the needed subfolders
    subfolders = ["text_encoder", "text_encoder_2", "tokenizer", "tokenizer_2", "vae"]
    for subfolder in subfolders:
        source_path = os.path.join("pretrained_models/HunyuanVideo_full", subfolder)
        target_path = os.path.join("pretrained_models/HunyuanVideo", subfolder)

        # Move the directory if it exists
        if os.path.exists(source_path):
            os.system(f"mv {source_path} {target_path}")

    # For flux_redux_bfl
    # First download the entire repo
    full_repo = snapshot_download(
        repo_id="lllyasviel/flux_redux_bfl",
        local_dir="pretrained_models/flux_redux_bfl_full",
        local_dir_use_symlinks=False
    )

    # Then move the needed subfolders
    subfolders = ["feature_extractor", "image_encoder"]
    for subfolder in subfolders:
        source_path = os.path.join("pretrained_models/flux_redux_bfl_full", subfolder)
        target_path = os.path.join("pretrained_models/flux_redux_bfl", subfolder)

        # Move the directory if it exists
        if os.path.exists(source_path):
            os.system(f"mv {source_path} {target_path}")

    # Download FramePackI2V_HY model
    snapshot_download(
        repo_id="lllyasviel/FramePackI2V_HY",
        local_dir="pretrained_models/FramePackI2V_HY",
        local_dir_use_symlinks=False
    )

    # Delete the remaining files in the temporary directories
    os.system("rm -rf pretrained_models/HunyuanVideo_full")
    os.system("rm -rf pretrained_models/flux_redux_bfl_full")

    # Clean up any other temporary files that might have been created
    os.system("find pretrained_models -type f -name '*.lock' -delete")
    os.system("find pretrained_models -type f -name '.gitattributes' -delete")

    print("All models downloaded successfully!")


if __name__ == '__main__':
    download_models()
