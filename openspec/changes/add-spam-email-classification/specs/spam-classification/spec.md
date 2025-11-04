## ADDED Requirements

### Requirement: Spam Message Classification Capability
The system SHALL provide a reproducible machine-learning pipeline to classify text messages (SMS/email) as spam or ham for experimentation and evaluation.

#### Scenario: Train SVM baseline
- **GIVEN** the dataset is available at the provided URL and preprocessed into features
- **WHEN** the training script is executed for Phase 1
- **THEN** the system SHALL train an SVM classifier and output evaluation metrics (accuracy, precision, recall, F1) and a persisted model artifact

#### Scenario: Evaluate on holdout data
- **GIVEN** a holdout test split
- **WHEN** the evaluation script runs
- **THEN** the system SHALL produce a confusion matrix and per-class metrics and save a human-readable report

#### Scenario: Reproducible data pull
- **WHEN** `scripts/download_data.py` is run
- **THEN** the dataset SHALL be fetched from the canonical URL and saved to `data/sms_spam_no_header.csv` with checksum recorded

#### Scenario: Phase 2 placeholders
- **GIVEN** future requirements (logistic regression, serving, monitoring)
- **WHEN** Phase 2 proposals are created
- **THEN** they SHALL be added under this change or in follow-up changes with explicit deltas
