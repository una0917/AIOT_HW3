"""Preprocessing helpers for spam classification."""
from __future__ import annotations

import pandas as pd
from typing import Iterable, Tuple


def load_csv(path: str) -> pd.DataFrame:
    # dataset has no header; assume format: label,text
    df = pd.read_csv(path, header=None, encoding="utf-8", names=["label", "text"])
    return df


def labels_to_binary(labels: Iterable[str]) -> list[int]:
    # common dataset: 'ham' vs 'spam'
    return [1 if str(l).strip().lower() == "spam" else 0 for l in labels]


def make_features(texts: Iterable[str], method: str = "tfidf"):
    """Create feature matrix using scikit-learn vectorizers.

    Note: import sklearn inside the function to avoid import-time failure when SKLearn
    is not installed; callers should handle ImportError.
    """
    if method not in ("tfidf", "count"):
        raise ValueError("method must be 'tfidf' or 'count'")

    try:
        from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
    except Exception as e:
        raise

    if method == "tfidf":
        vec = TfidfVectorizer(lowercase=True, stop_words="english", max_features=5000)
    else:
        vec = CountVectorizer(lowercase=True, stop_words="english", max_features=5000)

    X = vec.fit_transform(texts)
    return X, vec
