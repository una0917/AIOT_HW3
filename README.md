# AIOT_HW3 — Spam Classification Demo

此專案為一個以 SMS/Email spam 分類問題為主題的教學專案，包含資料下載腳本、模型訓練程式與一個 Streamlit 示範介面，用於展示資料分布、token 分析與模型評估/即時推論。

## 功能

*   **互動式儀表板:** 使用 Streamlit 建立，提供視覺化的數據分析與模型評估。
*   **資料探索:**
    *   顯示資料集的類別分佈 (spam/ham)。
    *   分析常用詞彙 (Top-N tokens)。
    *   顯示正規化過程中被替換的 token 數量 (URL, Email, Phone, Number)。
*   **模型評估:**
    *   顯示模型的混淆矩陣 (Confusion Matrix)。
    *   繪製 ROC 曲線與 Precision-Recall 曲線。
    *   提供不同決策閾值 (Decision Threshold) 下的精確率、召回率和 F1 分數。
*   **即時推論:** 提供一個文字輸入框，讓使用者可以輸入任意訊息，並立即看到模型的分類結果與 spam 機率。
*   **可擴展性:** 專案結構清晰，方便擴展與修改。

## Demo

您可以在以下網址體驗此專案的線上示範：

[https://aiothw3-kpbncczlchd8s6ychaxjcv.streamlit.app/](https://aiothw3-kpbncczlchd8s6ychaxjcv.streamlit.app/)

## 專案結構

```
.
├── data/                  # 存放資料集
├── models/                # 存放訓練好的模型
├── scripts/               # 存放輔助腳本
│   ├── download_data.py   # 下載資料集
│   └── setup_venv.ps1     # 設定虛擬環境 (PowerShell)
├── src/ml/                # 存放機器學習相關程式碼
│   ├── preprocess.py      # 資料前處理
│   ├── train_logreg.py    # 訓練羅吉斯迴歸模型
│   └── train_svm.py       # 訓練 SVM 模型
├── streamlit_app.py       # Streamlit 應用程式主程式
└── requirements.txt       # Python 依賴套件
```

## 安裝與設定

### 需求

*   Python 3.8+

### Windows (使用 PowerShell)

1.  **建立虛擬環境並安裝依賴套件:**

    執行 `scripts` 資料夾中的 `setup_venv.ps1` 腳本，此腳本會自動建立一個名為 `.venv` 的虛擬環境，並安裝 `requirements.txt` 中所有的依賴套件。

    ```powershell
    .\scripts\setup_venv.ps1
    ```

2.  **下載資料集:**

    啟用虛擬環境後，執行 `scripts` 資料夾中的 `download_data.py` 腳本，此腳本會將 SMS spam 資料集下載到 `data` 資料夾中。

    ```powershell
    .\.venv\Scripts\python.exe .\scripts\download_data.py
    ```

### 其他作業系統 (手動安裝)

1.  **建立並啟用虛擬環境:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2.  **安裝依賴套件:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **下載資料集:**

    ```bash
    python scripts/download_data.py
    ```

## 使用方法

### 啟動 Streamlit 應用程式

啟用虛擬環境後，執行以下命令來啟動 Streamlit 應用程式：

```powershell
# PowerShell
.\.venv\Scripts\python.exe -m streamlit run streamlit_app.py

# Bash
python -m streamlit run streamlit_app.py
```

應用程式將會在您的瀏覽器中開啟。

### 訓練模型 (選擇性)

如果您想要重新訓練模型，可以執行 `src/ml` 資料夾中的訓練腳本。

*   **訓練羅吉斯迴歸模型:**

    ```powershell
    # PowerShell
    .\.venv\Scripts\python.exe -m src.ml.train_logreg

    # Bash
    python -m src.ml.train_logreg
    ```

    此腳本會將訓練好的模型 (`spam_logreg_model.joblib`) 與 TF-IDF 向量化器 (`spam_tfidf_vectorizer.joblib`) 儲存到 `models` 資料夾中。

*   **訓練 SVM 模型:**

    ```powershell
    # PowerShell
    .\.venv\Scripts\python.exe -m src.ml.train_svm

    # Bash
    python -m src.ml.train_svm
    ```

    此腳本會將訓練好的模型 (`svm_baseline.joblib`) 儲存到 `artifacts` 資料夾中。

## 資料前處理

本專案的資料前處理流程包含以下步驟：

1.  **載入資料:** 從 `data/sms_spam_no_header.csv` 讀取資料，並將其轉換為 Pandas DataFrame。
2.  **標籤轉換:** 將 `ham` 與 `spam` 標籤轉換為二元數值 (0/1)。
3.  **文字正規化 (`normalize_text`):**
    *   將所有文字轉換為小寫。
    *   將 URL、Email 地址和電話號碼替換為特殊的 token (`<URL>`, `<EMAIL>`, `<PHONE>`)。
    *   將數字替換為 `<NUM>` token。
    *   移除所有非字母、數字的字元。
    *   移除多餘的空白字元。
4.  **特徵工程 (`make_features`):**
    *   使用 TF-IDF (Term Frequency-Inverse Document Frequency) 將文字轉換為數值特徵向量。
    *   移除了英文的停用詞 (Stop words)。
    *   限制最大特徵數量為 5000。

## 功能與視覺化 (Features and Visualizations)

Streamlit 應用程式提供了一個互動式的介面，讓使用者可以深入了解資料集和模型的表現。

*   **資料總覽 (Data Overview):**
    *   **類別分佈 (Class distribution):** 長條圖顯示了資料集中 `spam` 和 `ham` 兩種類別的訊息數量，讓使用者可以快速了解資料是否平衡。
    *   **Token 替換統計 (Token replacements):** 顯示在資料前處理過程中，URL、Email、電話號碼和數字被替換為特殊 token 的次數。

*   **各類別熱門詞彙 (Top Tokens by Class):**
    *   使用者可以透過滑桿選擇要顯示的熱門詞彙數量 (Top-N)。
    *   對於 `spam` 和 `ham` 兩個類別，分別顯示最常出現的詞彙及其頻率，有助於了解兩種類別訊息的用詞差異。

*   **模型表現 (Model Performance):**
    *   **混淆矩陣 (Confusion Matrix):** 顯示模型在測試集上的預測結果，包含 True Positives, True Negatives, False Positives, 和 False Negatives。
    *   **ROC 曲線 (ROC Curve):** 顯示在不同閾值下，模型的 True Positive Rate (TPR) 和 False Positive Rate (FPR) 的關係。曲線下面積 (AUC) 越大，代表模型表現越好。
    *   **Precision-Recall 曲線 (Precision-Recall Curve):** 顯示在不同閾值下，模型的 Precision 和 Recall 的關係，這在資料不平衡時是一個很重要的指標。
    *   **閾值掃描 (Threshold sweep):** 表格顯示了在一系列不同的決策閾值下，模型的 Precision, Recall, 和 F1-score。

*   **即時推論 (Live Inference):**
    *   使用者可以輸入任意文字訊息，並點擊 "Predict" 按鈕。
    *   應用程式會顯示模型預測的類別 (`spam` 或 `ham`)，以及該訊息為 `spam` 的機率。
    *   提供一個機率條，視覺化地呈現 spam 機率以及目前的決策閾值。

## 輸出結果 (Output Results)

當您執行訓練腳本 (`src/ml/train_logreg.py` 或 `src/ml/train_svm.py`)，將會產生以下檔案：

*   **`models/spam_logreg_model.joblib`:** 訓練好的羅吉斯迴歸模型。
*   **`models/spam_tfidf_vectorizer.joblib`:** 訓練資料集上學習到的 TF-IDF 向量化器。
*   **`models/spam_label_mapping.json`:** 標籤對應檔案，定義 `positive` 和 `negative` 的類別名稱。
*   **`artifacts/svm_baseline.joblib`:** (如果執行 `train_svm.py`) 訓練好的 SVM 模型與其對應的向量化器。

這些檔案將會被 Streamlit 應用程式用於載入模型並進行推論。

## 常見問題與解決方案 (FAQ)

**Q: 執行 `streamlit run streamlit_app.py` 時出現 `ModuleNotFoundError`。**

**A:** 這通常是因為您忘記啟用虛擬環境，或是沒有在虛擬環境中安裝依賴套件。請確認您已經依照 "安裝與設定" 的步驟啟用虛擬環境。

**Q: 執行訓練腳本或 Streamlit 應用程式時出現 `FileNotFoundError`。**

**A:** 這通常是因為您忘記下載資料集。請執行 `scripts/download_data.py` 腳本來下載資料集。

**Q: 在 PowerShell 中執行 `.\scripts\setup_venv.ps1` 時出現錯誤。**

**A:** 這可能是因為您的 PowerShell 執行原則 (Execution Policy) 禁止執行腳本。您可以嘗試在 PowerShell 中執行以下命令來暫時允許執行腳本：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
```

然後再重新執行 `.\scripts\setup_venv.ps1`。

**Q: Streamlit 應用程式顯示 "Model artifacts not found"。**

**A:** 這表示 `models` 資料夾中缺少模型檔案。您可以透過執行訓練腳本來產生模型檔案，或是點擊 Streamlit 應用程式中的 "Download model artifacts from GitHub" 按鈕來下載預先訓練好的模型。

## 部署到 Streamlit Cloud

1.  將您的專案推送到 GitHub repository。
2.  在 Streamlit Cloud 中建立一個新應用程式，並連結到您的 repository。
3.  將 `streamlit_app.py` 設定為 entry file。
4.  Streamlit Cloud 將會自動安裝 `requirements.txt` 中的依賴套件，並部署您的應用程式。

## 參考資料

此專案參考並擴展自 Packt 的 [Hands-On-Artificial-Intelligence-for-Cybersecurity](https://github.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity.git) 的 Chapter 3 範例資料與處理流程。