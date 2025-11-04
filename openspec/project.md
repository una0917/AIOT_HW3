# Project Context

## Purpose
This repository contains the deliverables for AIOT_HW3 — an AIoT (Artificial Intelligence + Internet of Things) homework/project focused on building device telemetry ingestion, processing, and basic analytics pipelines. The goal is to define clear specs for device capabilities, build a small ingestion service, and provide reproducible tests and documentation so future contributors (including AI assistants) can reason about and extend the system.

## Tech Stack (assumptions)
- Runtime: Node.js (tested with v22.x)
- Package manager: npm (v10+)
- Language: JavaScript (ES202X); TypeScript is optional — adopt if we add a build step
- Spec tooling: OpenSpec (`@fission-ai/openspec`)
- Testing: Jest for unit tests; simple integration tests via Node scripts
- Storage: lightweight local file or SQLite for dev; production may target PostgreSQL or cloud time-series DB
- Messaging/ingestion: MQTT or HTTP-based ingestion depending on device capability

If any of the above assumptions are incorrect, update this file or tell the assistant which stack you'd prefer.

## Project Conventions

### Code Style
- Use consistent formatting tools: Prettier for formatting and ESLint for linting if we adopt TypeScript/ESLint later.
- Naming: camelCase for variables/functions, PascalCase for classes and React components (if applicable), kebab-case for filenames and change-ids.

### Architecture Patterns
- Single-repo, capability-oriented layout using OpenSpec:
	- `openspec/specs/` holds the current truth of capabilities
	- `openspec/changes/` holds active proposals
	- `openspec/changes/archive/` holds archived changes
- Keep components small and focused: device ingestion, storage, processing, and API layers should be decoupled where reasonable.

### Testing Strategy
- Unit tests for core logic (parsers, validators, transforms).
- Small integration tests to exercise ingestion → store → query flows.
- When adding specs, add at least one automated test that demonstrates the new behavior.

### Git Workflow
- Branching: feature branches named `feature/<short-desc>` or `chore/<short-desc>`; change proposals use `changes/<change-id>` directories.
- Commits: use short, descriptive messages; prefer conventional commits (e.g., `feat: add telemetry ingestion`) if convenient.
- PRs: include link to the OpenSpec `changes/<change-id>/proposal.md` and `tasks.md` in the PR description.

## Domain Context
- Devices: constrained IoT devices will send periodic telemetry (JSON or binary) via MQTT or HTTP.
- Telemetry payloads commonly include: deviceId, timestamp, sensor readings (temperature, humidity, battery), and optional metadata.
- Offline behavior: devices may buffer and re-send telemetry; ingestion must be idempotent when possible.

## Important Constraints
- Development environment is Windows (PowerShell) — scripts should be cross-platform when possible.
- Keep the runtime footprint small for local dev.
- Privacy: telemetry may contain PII in metadata. Avoid storing unnecessary personal data and follow data minimization.

## External Dependencies
- Optional MQTT broker for device testing (e.g., Mosquitto)
- Optional cloud services: S3/Blob, PostgreSQL, or time-series DB for production
- 3rd-party libs: OpenSpec CLI for spec validation; Jest for testing

---

Notes:
- I made a few reasonable assumptions about language, storage, and messaging based on the repository name and the environment (Node.js is available). If you'd like different choices (TypeScript, different DB, or a specific messaging protocol), tell me which and I will update this file and the change proposals accordingly.
