# AIOT_HW3 — Spam Classification & Telemetry

This repository contains work for AIOT_HW3. It includes an OpenSpec-driven workflow and a Phase 1 machine-learning baseline for spam message classification.

Key files:
- `streamlit_app.py` — Streamlit demo app (uses saved artifact `artifacts/svm_baseline.joblib`)
- `src/ml/train_svm.py` — Training script (SVM baseline)
- `scripts/download_data.py` — Download the dataset
- `requirements.txt` — Python dependencies
- `scripts/setup_venv.ps1` — PowerShell helper to create a `.venv` and install dependencies

## Run locally (PowerShell)
1. Create venv and install deps (or run the helper script):

```powershell
.\scripts\setup_venv.ps1
```

2. (Optional) download dataset:

```powershell
.\.venv\Scripts\python.exe .\scripts\download_data.py
```

3. Train a quick sample model:

```powershell
.\.venv\Scripts\python.exe -m src.ml.train_svm --sample
```

4. Run Streamlit locally:

```powershell
.\.venv\Scripts\python.exe -m streamlit run streamlit_app.py
```

## Deploy to Streamlit Cloud
1. Push this repository to GitHub.
2. On Streamlit Cloud, click "New app" → connect the GitHub repository → set the main file to `streamlit_app.py` → Deploy.
3. Ensure `requirements.txt` is present in repo root (it is). If your model artifact is large, consider storing the model in a small storage (S3) and modifying the app to download at startup; for demo purposes the artifact is included in `artifacts/`.

## Notes
- The current baseline uses LinearSVC which does not provide calibrated probabilities. The app shows the decision function score as a confidence proxy. In Phase 2 we can retrain with `LogisticRegression` and serve calibrated probabilities.
