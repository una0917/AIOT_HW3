## Change ID
add-device-telemetry

## Why
Devices in this AIoT project need a standard, testable way to send telemetry into the system so we can ingest, store, and analyze sensor data. Currently there is no documented capability in `openspec/specs/` describing telemetry ingestion behavior. Adding a device telemetry capability will make requirements explicit and guide implementation and testing.

## What Changes
- Add a new capability spec: `device-telemetry` (delta under `changes/add-device-telemetry/specs/device-telemetry/spec.md`) describing required ingestion behavior, scenarios, and basic retention rules.
- Add implementation tasks and tests for a lightweight ingestion endpoint (HTTP and/or MQTT receiver depending on device support).
- Provide example payloads and an integration test that demonstrates ingestion → storage → query.

**Breaking changes:** None expected. This adds a new capability only.

## Impact
- Affected specs: `device-telemetry` (new)
- Affected code (suggested locations): `src/ingestion/` (HTTP handler or MQTT client), `src/storage/` (persistence adapter), `tests/integration/telemetry.spec.js`
- Documentation: update `README.md` and `openspec/project.md` to reference the new capability

## Acceptance Criteria
- A spec delta exists under `openspec/changes/add-device-telemetry/specs/device-telemetry/spec.md` and passes `openspec validate add-device-telemetry --strict`.
- Implementation includes at least one automated integration test that sends a telemetry payload and verifies it is persisted and queryable.
- Tasks in `tasks.md` completed and PR includes link to this proposal.
