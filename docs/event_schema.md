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

## Event Frequency

Each IoT sensor generates one telemetry event every 2 seconds.

For this project, multiple sensors will run simultaneously, creating a continuous stream of real-time events.

## Simulated Data Quality Issues

To make the streaming pipeline more realistic, the producer will occasionally generate imperfect data.

### Missing Values
- Some events will have a missing temperature value.
- Expected behavior: Reject the event and log it for later review.

### Temperature Spikes
- Some events will contain unrealistic temperature values.
- Expected behavior: Flag the event as an anomaly while keeping it in the data.

### Late Events
- Some events will arrive after a delay.
- Expected behavior: Accept late events if they arrive within the allowed processing window.

### Duplicate Events
- Some events will be sent more than once.
- Expected behavior: Detect and remove duplicate events before calculating metrics.