from datetime import datetime, timedelta
import json
import logging
import random
import time

from kafka import KafkaProducer
from kafka.errors import KafkaError


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


sensors = {
    "sensor_001": "warehouse_A",
    "sensor_002": "warehouse_A",
    "sensor_003": "warehouse_B"
}


def generate_event(sensor_id, location):
    temperature = round(random.uniform(65, 80), 1)

    # Temperature spike
    if random.random() < 0.05:
        temperature = round(random.uniform(200, 300), 1)

    # Missing temperature
    if random.random() < 0.05:
        temperature = None

    humidity = round(random.uniform(30, 60), 1)

    # Missing humidity
    if random.random() < 0.05:
        humidity = None

    battery_level = random.randint(80, 100)

    timestamp = datetime.now()

    # Late timestamp
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


def create_producer():
    try:
        logger.info("Connecting to Kafka...")

        producer = KafkaProducer(
            bootstrap_servers="localhost:9092"
        )

        logger.info("Successfully connected to Kafka.")

        return producer

    except KafkaError as error:
        logger.error(f"Could not connect to Kafka: {error}")
        return None


producer = create_producer()

if producer is None:
    logger.error("Producer could not start. Exiting.")
    raise SystemExit(1)


try:
    while True:

        for sensor_id, location in sensors.items():

            event = generate_event(sensor_id, location)

            try:
                future = producer.send(
                    "iot-sensor-readings",
                    value=json.dumps(event).encode("utf-8")
                )

                # Wait for Kafka to confirm the message
                future.get(timeout=10)

                logger.info(
                    f"Sent event from {sensor_id}"
                )

            except KafkaError as error:
                logger.error(
                    f"Failed to send event from {sensor_id}: {error}"
                )

        time.sleep(2)


except KeyboardInterrupt:
    logger.info("Producer interrupted. Shutting down...")


finally:
    logger.info("Flushing remaining messages...")
    producer.flush()

    logger.info("Closing Kafka producer...")
    producer.close()

    logger.info("Producer shut down successfully.")