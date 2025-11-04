"""Download multiple Packt Chapter03 datasets into data/ directory."""
from __future__ import annotations

import hashlib
import os
import urllib.request

BASE = "https://raw.githubusercontent.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity/refs/heads/master/Chapter03/datasets"
FILES = [
    "phishing_dataset.csv",
    "sms_spam_perceptron.csv",
    "sms_spam_svm.csv",
]


def ensure_data_dir(path: str = "data") -> str:
    os.makedirs(path, exist_ok=True)
    return path


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(8192), b""):
            h.update(block)
    return h.hexdigest()


def download_files(dest_dir: str = "data") -> list[str]:
    ensure_data_dir(dest_dir)
    saved = []
    for fname in FILES:
        url = f"{BASE}/{fname}"
        dest = os.path.join(dest_dir, fname)
        print(f"Downloading {url} -> {dest}")
        urllib.request.urlretrieve(url, dest)
        s = sha256(dest)
        print(f"Saved {dest} (sha256={s})")
        saved.append(dest)
    return saved


def main() -> None:
    download_files()


if __name__ == "__main__":
    main()
