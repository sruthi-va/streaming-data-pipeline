# Streaming Pipeline Architecture

## Current Implementation (Day 1)

The current implementation tests the Kafka messaging layer.

Data flow:

Python Producer
        |
        v
Kafka Broker
        |
        v
iot-sensor-readings topic
        |
        v
Kafka Consumer


## Components

### Kafka Broker

Kafka is responsible for receiving, storing, and delivering event messages.

It acts as a buffer between producers and consumers.

### Topic

The project uses the topic:

iot-sensor-readings

The topic contains IoT sensor events.

Current configuration:

- Partitions: 1
- Replication factor: 1


### Producer

The producer will generate IoT sensor readings and send them to Kafka.

Example future event:

- sensor_id
- timestamp
- temperature
- humidity
- battery_level


### Consumer

The consumer reads events from Kafka.

Later, Spark Structured Streaming will replace this simple consumer.