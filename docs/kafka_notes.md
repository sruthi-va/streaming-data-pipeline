# Kafka Notes

## Topic

A topic is a named stream of events. 
This project uses the topic:

iot-sensor-readings


## Partition

A partition is a subdivision of a topic that allows Kafka to scale.

This project currently uses:

1 topic
1 partition


## Data Flow

Python Producer
        |
        v
iot-sensor-readings topic
        |
        v
Spark Structured Streaming consumer