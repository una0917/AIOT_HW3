# AIOT_HW3 — Spam Classification Demo

這個專案包含一個以教師範例為基底的 spam/ham 訊息分類範例，搭配可互動的 Streamlit 前端，以及簡單的訓練腳本和資料下載輔助。主要用途為教學示範：如何從資料準備、訓練模型到在 Streamlit 上展示模型預測與評估指標。

目錄重點
- `streamlit_app.py` — Streamlit 應用程式（主介面）。
- `src/ml/train_logreg.py`, `src/ml/train_svm.py` — 訓練/建立模型的腳本。
- `scripts/download_teacher_datasets.py` — 下載教師提供的 demo CSV（會存到 `data/`）。
- `models/` — 放置模型藝術檔（`.joblib`）與 `spam_label_mapping.json`（本 repo demo 有把少量模型檔放進 repo，以便 Cloud demo）。
- `data/` — 範例資料（教師提供的 CSV）。
- `requirements.txt` — Python 相依套件。

快速開始（Windows PowerShell）
1. 建立虛擬環境並安裝依賴（或執行 helper）：

```powershell
.\scripts\setup_venv.ps1
```

2. 下載教師提供的範例資料（會放到 `data/`）：

```powershell
.\.venv\Scripts\python.exe .\scripts\download_teacher_datasets.py
```

3. （選擇性）訓練模型（Logistic Regression 範例）：

```powershell
.\.venv\Scripts\python.exe -m src.ml.train_logreg
```

訓練後會輸出到 `models/`（`spam_tfidf_vectorizer.joblib`, `spam_logreg_model.joblib`, `spam_label_mapping.json`）。

4. 在本機執行 Streamlit 應用：

```powershell
.\.venv\Scripts\python.exe -m streamlit run streamlit_app.py
```

在本機運行時應能看到 Data Overview、Top Tokens、Model Performance（若 `models/` 存在）與 Live Inference。若 `models/` 不存在，App 會提示並提供下載按鈕以從本 repo 的 branch 下載 artifacts。

部署到 Streamlit Cloud（建議流程）
1. 推上 GitHub。建議把要部署的 branch 設為包含 model artifacts 或實作下載邏輯的分支（本專案示範使用 `feature/add-streamlit-deploy`）。
2. 在 Streamlit Cloud 建立新 App，連接 GitHub repo，並把 Entry file 設為 `streamlit_app.py`。
3. 若不想把二進位模型加入 Git（更乾淨的做法）：
   - 把模型檔上傳到 GitHub Releases、S3/GCS，然後在 Streamlit Cloud 的 Secrets/Env 中設定 `STREAMLIT_MODELS_BASE_URL`（或直接把下載 URL 填入程式設定）。
   - 我已在 `streamlit_app.py` 裡加入了「若 models/ 不存在，按鈕可從 repo raw 下載」的 fallback，也可以輕易改為從環境變數指定的 URL 下載（推薦）。

常見問題與排查
- 404（按下載後某些模型檔抓不到）：表示該檔案尚未被推到遠端 branch（raw.githubusercontent 會回 404）。解法：把模型檔 commit & push，或把模型上傳到 Release/S3 並更新下載 URL。
- Streamlit Cloud 上按鈕點了會出現 AttributeError / "original error message is redacted": 我在 app 裡已用 try/except 包裹 `st.experimental_rerun()`，若自動 reload 失敗會提示手動刷新；若仍報錯，請抓取 Cloud 的 logs（Manage app → Logs）並貼上來，我會協助解析。
- evaluation crash（confusion matrix 或 ROC 出錯）：若 train_test_split 產生的測試集只有單一類別，原本會在建立 2×2 confusion matrix 或 roc_curve 時丟錯。我已加入 guard 檢查（若 y_test 唯一值小於 2，會顯示提示並跳過那些視覺化）。

建議的長期處理（模型檔管理）
- 最佳作法：不要把大型二進位檔放到 Git。建議把模型上傳到 GitHub Releases 或雲端儲存（S3/GCS），並在應用於啟動時從該位置下載。
- 若你想我幫忙：我可以幫你建立一個上傳到 Release 的 script，或把 app 改為讀取 env var（`STREAMLIT_MODELS_BASE_URL`）並用該 URL 下載模型。

程式碼結構（快速導覽）
- `streamlit_app.py` — 主程式（資料讀取、欄位推斷、token 統計、模型評估、live inference、models 下載 fallback）。
- `src/ml/preprocess.py` — 前處理工具。
- `src/ml/train_logreg.py`, `src/ml/train_svm.py` — 訓練腳本。
- `scripts/download_teacher_datasets.py` — 下載教師提供的 CSV 到 `data/`。

開發與測試
- 建議把變更推到 feature branch（例如 `feature/add-streamlit-deploy`），在本機測試後再合併到主要分支。若要在 CI 檢查，至少包含：語法檢查（python -m py_compile）、基本單元測試（若新增）與 requirements 安裝驗證。

聯絡與貢獻
- 若要我代為處理：例如把模型上傳到 Release、修改 app 以使用 env var、或把 branch 合併到主分支，請在 issue 或這裡指示具體動作，我會代為執行。

授權
- 本範例程式碼以 MIT-like 條款示範（請依專案或授課需求調整 LICENSE）。

最後備註
- 本 repo 為教學示範，故在某些步驟（例如把小型模型 commit 到 repo）採取了方便性優先的做法；在生產環境請改用雲端儲存與版本化資產的策略。
