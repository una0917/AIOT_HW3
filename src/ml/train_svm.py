"""Train a simple SVM baseline for spam classification.

Usage:
  python -m src.ml.train_svm --sample
  python -m src.ml.train_svm --data data/sms_spam_no_header.csv
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


def ensure_path(p: str) -> str:
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    return p


def train_main(data_path: str, sample: bool = False) -> int:
    try:
        import joblib
        from sklearn.svm import LinearSVC
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import classification_report, confusion_matrix
    except Exception:
        print("scikit-learn (and joblib) are required. Please install with:\n  pip install scikit-learn joblib")
        return 2

    # Local import of preprocess to avoid import-time failure when pandas missing
    from src.ml.preprocess import load_csv, labels_to_binary, make_features

    df = load_csv(data_path)
    if sample:
        df = df.sample(n=min(400, len(df)), random_state=42)

    y = labels_to_binary(df["label"])
    X, vec = make_features(df["text"], method="tfidf")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = LinearSVC()
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)
    print(classification_report(y_test, preds))
    print("Confusion matrix:")
    print(confusion_matrix(y_test, preds))

    out_dir = ensure_path(os.path.join("artifacts", "svm_baseline.joblib"))
    joblib.dump({"model": clf, "vectorizer": vec}, out_dir)
    print(f"Saved model artifact to {out_dir}")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--data", default="data/sms_spam_no_header.csv")
    p.add_argument("--sample", action="store_true", help="Run on a small sample for quick validation")
    args = p.parse_args(argv)

    if not os.path.exists(args.data):
        print(f"Data file not found: {args.data}\nRun scripts/download_data.py to fetch the dataset.")
        return 1

    return train_main(args.data, sample=args.sample)


if __name__ == "__main__":
    raise SystemExit(main())
