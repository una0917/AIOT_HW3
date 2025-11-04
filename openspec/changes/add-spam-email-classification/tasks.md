## Phase 1 — Baseline (SVM)
- [ ] 1.1 Create change directory: `openspec/changes/add-spam-email-classification/`
- [ ] 1.2 Add spec delta: `specs/spam-classification/spec.md`
- [ ] 1.3 Create `requirements.txt` with Python deps: scikit-learn, pandas, numpy, joblib
- [ ] 1.4 Add data download script `scripts/download_data.py` to fetch dataset from URL and save to `data/sms_spam_no_header.csv`
- [ ] 1.5 Implement preprocessing and feature extraction script `src/ml/preprocess.py` (tokenization, TF-IDF or CountVectorizer)
- [ ] 1.6 Implement training script `src/ml/train_svm.py` that trains SVM baseline and writes model to `artifacts/svm_baseline.joblib`
- [ ] 1.7 Add evaluation script/notebook `notebooks/phase1_baseline.ipynb` demonstrating metrics and confusion matrix
- [ ] 1.8 Add integration test `tests/ml/test_train_baseline.py` that runs training with a small sample and asserts metrics computed

## Phase 2 — Future Improvements (placeholders)
- [ ] 2.1 Phase 2.1: (empty) Migrate baseline to logistic regression and compare metrics
- [ ] 2.2 Phase 2.2: (empty) Model serving prototype (HTTP inference endpoint)
- [ ] 2.3 Phase 2.3: (empty) Monitoring and drift detection

## Validation & PR
- [ ] Run `openspec validate add-spam-email-classification --strict`
- [ ] Update `README.md` with instructions to run training locally
- [ ] Link this proposal in the PR description
