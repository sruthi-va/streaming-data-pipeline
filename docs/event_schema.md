# IoT Event Schema

## Scenario

This project simulates a smart warehouse monitoring system.

Multiple IoT sensors continuously monitor warehouse conditions and send telemetry events in real time.

The goal is to detect abnormal environmental conditions and monitor sensor health.

## Event Fields

| Field | Type | Description |
|--------|------|-------------|
| sensor_id | string | Unique identifier for each sensor |
| timestamp | datetime | Time when the sensor reading was taken |
| temperature | float | Temperature reading in °F |
| humidity | float | Humidity percentage |
| battery_level | integer | Remaining battery percentage |
| location | string | Warehouse where the sensor is installed |

## Example Event

```json
{
  "sensor_id": "sensor_001",
  "timestamp": "2026-08-08T08:30:00",
  "temperature": 72.5,
  "humidity": 45.2,
  "battery_level": 94,
  "location": "warehouse_A"
}
```