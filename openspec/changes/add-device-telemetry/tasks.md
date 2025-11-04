## 1. Implementation
- [ ] Scaffold change directory: `openspec/changes/add-device-telemetry/`
- [ ] Add spec delta: `specs/device-telemetry/spec.md`
- [ ] Implement ingestion endpoint (HTTP POST `/telemetry` handler) in `src/ingestion/` or MQTT receiver in `src/ingestion/mqtt.js`
- [ ] Implement storage adapter (dev: SQLite or local file) in `src/storage/`
- [ ] Add unit tests for parser/validator
- [ ] Add integration test that posts example telemetry and asserts persistence

## 2. Validation & Docs
- [ ] Run `openspec validate add-device-telemetry --strict` and fix issues
- [ ] Add usage examples to `README.md` (sample payloads and how to run integration test)

## 3. PR Checklist
- [ ] Link this proposal in the PR description
- [ ] All tasks above completed and tests passing locally
- [ ] Reviewer: @<your-reviewer-here>
