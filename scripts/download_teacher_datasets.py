"""Download teacher's two datasets into data/ directory."""
from __future__ import annotations

import hashlib
import os
import urllib.request

BASE = "https://raw.githubusercontent.com/huanchen1107/2025ML-spamEmail/main"
FILES = [
    "datasets/sms_spam_no_header.csv",
    "datasets/processed/sms_spam_clean.csv",
]


def ensure_data_dir(path: str = "data") -> str:
    os.makedirs(path, exist_ok=True)
    return path


def sha256(path: str) -> str:
    import hashlib
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(8192), b""):
            h.update(block)
    return h.hexdigest()


def download_files(dest_dir: str = "data") -> list[str]:
    ensure_data_dir(dest_dir)
    saved = []
    for rel in FILES:
        url = f"{BASE}/{rel}"
        dest = os.path.join(dest_dir, os.path.basename(rel))
        print(f"Downloading {url} -> {dest}")
        urllib.request.urlretrieve(url, dest)
        s = sha256(dest)
        print(f"Saved {dest} (sha256={s})")
        saved.append(dest)
    return saved


if __name__ == "__main__":
    download_files()
