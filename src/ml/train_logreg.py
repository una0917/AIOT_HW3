"""Train a LogisticRegression model and save artifacts expected by the template.

Generates:
 - models/spam_tfidf_vectorizer.joblib
 - models/spam_logreg_model.joblib
 - models/spam_label_mapping.json
"""
from __future__ import annotations

import json
import os
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report


import re
URL_RE = re.compile(r"https?://\S+|www\.\S+", re.IGNORECASE)
EMAIL_RE = re.compile(r"\b[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}\b")
PHONE_RE = re.compile(r"\b(?:\+?\d[\d\-\s]{7,}\d)\b")


def normalize_text(text: str, keep_numbers: bool = False) -> str:
    if not isinstance(text, str):
        text = "" if text is None else str(text)
    t = text.lower()
    t = URL_RE.sub("<URL>", t)
    t = EMAIL_RE.sub("<EMAIL>", t)
    t = PHONE_RE.sub("<PHONE>", t)
    if not keep_numbers:
        t = re.sub(r"\d+", "<NUM>", t)
    t = re.sub(r"[^\w\s<>]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def load_data(path: str = "data/sms_spam_no_header.csv") -> pd.DataFrame:
    df = pd.read_csv(path, header=None, names=["label", "text"], encoding="utf-8")
    return df


def main(data_path: str | None = None) -> int:
    data_path = data_path or "data/sms_spam_no_header.csv"
    if not os.path.exists(data_path):
        print(f"Data not found: {data_path}. Run scripts/download_data.py first.")
        return 1

    df = load_data(data_path)
    df["text_clean"] = df["text"].astype(str).apply(normalize_text)
    y = (df["label"].astype(str).str.lower() == "spam").astype(int).values

    vec = TfidfVectorizer(lowercase=True, stop_words="english", max_features=5000)
    X = vec.fit_transform(df["text_clean"].values)

    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    clf = LogisticRegression(max_iter=1000)
    clf.fit(Xtr, ytr)

    preds = clf.predict(Xte)
    print(classification_report(yte, preds))

    models_dir = Path("models")
    models_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(vec, models_dir / "spam_tfidf_vectorizer.joblib")
    joblib.dump(clf, models_dir / "spam_logreg_model.joblib")

    meta = {"positive": "spam", "negative": "ham"}
    with open(models_dir / "spam_label_mapping.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print(f"Saved artifacts to {models_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
