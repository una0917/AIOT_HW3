## Change ID
add-spam-email-classification

## Why
We want a reproducible machine-learning capability that classifies spam messages (SMS/email) so the project can evaluate, compare, and iterate on models. This change introduces an initial ML workflow for spam classification and establishes a baseline model and dataset so future improvements (phase 2+) can be well-scoped and measured.

## What Changes
- Phase 1: Setup baseline pipeline. Download the SMS spam dataset and implement a baseline SVM classifier, plus scripts/notebook to preprocess data, train, and evaluate metrics. The dataset used for Phase 1 is:
  - https://raw.githubusercontent.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity/refs/heads/master/Chapter03/datasets/sms_spam_no_header.csv
- Phase 2: (placeholders) Future phases will include migrating baseline to logistic regression, model serving, monitoring, and dataset expansion. Leave Phase 2 entries empty for now.

## Impact
- New files and folders (suggested): `src/ml/` (training scripts), `notebooks/` (analysis), `data/` (downloaded CSV), `tests/ml/` (integration tests). 
- New runtime/tooling: Python 3.10+ recommended, with `scikit-learn`, `pandas`, `numpy`, and `joblib` for model persistence. Provide a `requirements.txt` for reproducibility.
- No breaking changes to existing specs or runtime.

## Acceptance Criteria
- Dataset downloaded and checked into `data/` or script provided to fetch it reproducibly.
- A runnable script or notebook that trains an SVM baseline on the dataset and prints evaluation metrics (accuracy, precision, recall, F1, confusion matrix).
- Training artifacts (model file) saved under `artifacts/` or explained in README; reproducible locally via provided instructions.
- `openspec` spec delta exists for the capability and passes `openspec validate add-spam-email-classification --strict`.
- Phase 2 sections included but left empty for future work.

## Notes / Environment
- Development OS: Windows PowerShell (follow existing repo convention). Python tooling commands should be PowerShell friendly. Example to create environment:
  - `python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt`
- Although the main repo previously used Node, ML work will use Python due to ecosystem maturity. If you prefer JS/Node ML stacks, tell me and I will adapt.
