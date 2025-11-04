"""Download dataset for spam classification into data/ directory."""
from __future__ import annotations

import hashlib
import os
import urllib.request

URL = (
    "https://raw.githubusercontent.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity/refs/heads/master/Chapter03/datasets/sms_spam_no_header.csv"
)


def ensure_data_dir(path: str = "data") -> str:
    os.makedirs(path, exist_ok=True)
    return path


def download(url: str = URL, dest_dir: str = "data") -> str:
    dest = os.path.join(ensure_data_dir(dest_dir), os.path.basename(url))
    print(f"Downloading {url} → {dest}")
    urllib.request.urlretrieve(url, dest)
    sha = sha256(dest)
    print(f"Saved {dest} (sha256={sha})")
    return dest


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(8192), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    p = download()
    print("Done.")


if __name__ == "__main__":
    main()
