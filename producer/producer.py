from datetime import datetime, timedelta
import json
import random
import time

from kafka import KafkaProducer


sensors = {
    "sensor_001": "warehouse_A",
    "sensor_002": "warehouse_A",
    "sensor_003": "warehouse_B"
}


def generate_event(sensor_id, location):
    # Generate a normal temperature
    temperature = round(random.uniform(65, 80), 1)

    # Occasionally create a temperature spike
    if random.random() < 0.05:
        temperature = round(random.uniform(200, 300), 1)

    # Occasionally create a missing temperature
    if random.random() < 0.05:
        temperature = None

    # Generate humidity
    humidity = round(random.uniform(30, 60), 1)

    # Occasionally create a missing humidity
    if random.random() < 0.05:
        humidity = None

    # Generate battery level
    battery_level = random.randint(80, 100)

    # Generate timestamp
    timestamp = datetime.now()

    # Occasionally create a late timestamp
    if random.random() < 0.05:
        timestamp = timestamp - timedelta(minutes=2)

    return {
        "sensor_id": sensor_id,
        "timestamp": timestamp.isoformat(),
        "temperature": temperature,
        "humidity": humidity,
        "battery_level": battery_level,
        "location": location
    }


# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers="localhost:9092"
)


# Continuously generate and send events
while True:

    for sensor_id, location in sensors.items():

        event = generate_event(sensor_id, location)

        producer.send(
            "iot-sensor-readings",
            value=json.dumps(event).encode("utf-8")
        )

        print(f"Sent: {event}")

    # Wait 2 seconds before generating the next batch
    time.sleep(2)