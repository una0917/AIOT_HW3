# AIOT_HW3 — Spam Email Classifier

此專案為一個以 SMS/Email spam 分類問題為主題的專案，包含資料下載腳本、模型訓練程式與一個 Streamlit 示範介面，用於展示資料分布、token 分析與模型評估/即時推論。
This repository contains work for AIOT_HW3. It includes an OpenSpec-driven workflow and a Phase 1 machine-learning baseline for spam message classification.

## Key files:
- `streamlit_app.py` — Streamlit demo app (uses saved artifact `artifacts/svm_baseline.joblib`)
- `src/ml/train_svm.py` — Training script (SVM baseline)
- `scripts/download_data.py` — Download the dataset
- `requirements.txt` — Python dependencies
- `scripts/setup_venv.ps1` — PowerShell helper to create a `.venv` and install dependencies

## 重要檔案
- `streamlit_app.py` — Streamlit 前端（主程式）。
- `src/ml/` — 訓練與前處理腳本（`train_logreg.py`, `train_svm.py`, `preprocess.py`）。
- `scripts/download_teacher_datasets.py` — 下載教師提供的 demo CSV 到 `data/`。
- `models/` — 模型 artifacts（`.joblib`）與 `spam_label_mapping.json`（小型 demo artifacts 已放入 repo 以便部署示範）。

## 快速上手（PowerShell）
1. 建立虛擬環境並安裝依賴：

```powershell
.\scripts\setup_venv.ps1
```

2. 下載教師提供的資料：

```powershell
.\.venv\Scripts\python.exe .\scripts\download_teacher_datasets.py
```

3. （選擇性）訓練模型：

```powershell
.\.venv\Scripts\python.exe -m src.ml.train_logreg
```

4. 執行 Streamlit 應用：

```powershell
.\.venv\Scripts\python.exe -m streamlit run streamlit_app.py
```

## 部署到 Streamlit Cloud
1. 推上 GitHub 並在 Streamlit Cloud 建立新應用，連結對應的 repository 與 branch，entry file 設為 `streamlit_app.py`。
2. 本專案已提供一個 runtime fallback：若 `models/` 不存在，App 會提供按鈕從本 repo 的指定 branch raw URL 下載 artifacts；長期建議把模型存放在 Release 或雲端儲存，再在 app 以 env var 指定下載來源。

## Source Reference
此專案參考並擴展自 Packt 的 Chapter 3 範例資料與處理流程：

https://github.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity.git

## Demo Site
線上示範：

https://aiothw3-kpbncczlchd8s6ychaxjcv.streamlit.app/

