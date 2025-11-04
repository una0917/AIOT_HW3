## ADDED Requirements

### Requirement: Device Telemetry Ingestion
The system SHALL accept telemetry from devices and persist it for later query and analysis.

#### Scenario: Telemetry ingestion (HTTP)
- **GIVEN** a device that can perform an HTTP POST
- **WHEN** the device sends a POST to `/telemetry` with a JSON body containing `deviceId`, `timestamp`, and `readings` (object)
- **THEN** the server SHALL respond 200 OK (or 202 Accepted for async processing)
- **AND** the telemetry SHALL be persisted idempotently (duplicate messages for same deviceId+timestamp SHALL not create duplicate records)

#### Scenario: Telemetry ingestion (MQTT)
- **GIVEN** a device publishing to topic `devices/<deviceId>/telemetry`
- **WHEN** the broker forwards a message with valid JSON payload containing `timestamp` and `readings`
- **THEN** the ingestion component SHALL accept and persist the message with the same idempotency guarantees as HTTP

#### Scenario: Malformed payload
- **GIVEN** a device sends a telemetry message without the required fields
- **WHEN** the message is received
- **THEN** the system SHALL reject the message with 4xx and log the error for analytics

#### Scenario: Offline buffering / retry
- **GIVEN** a device re-sends telemetry messages that were previously not acknowledged
- **WHEN** the ingestion service receives a retried message with the same `deviceId` and `timestamp`
- **THEN** the system SHALL detect it as a duplicate and avoid double-storage; the service SHALL record a retry metadata entry (optional)

### Requirement: Retention and Queryability
The system SHALL retain telemetry for a configurable retention window (default: 30 days) and provide a simple query interface to retrieve time series by `deviceId` and time range.

#### Scenario: Query by device and time range
- **WHEN** a client requests `/telemetry?deviceId=abc&from=2025-01-01T00:00:00Z&to=2025-01-02T00:00:00Z`
- **THEN** the system SHALL return a paginated list of telemetry points for device `abc` within the time window
