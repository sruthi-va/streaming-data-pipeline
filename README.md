# Streaming Data Pipeline

## Overview

A real-time IoT sensor data pipeline that ingests, processes, validates, and visualizes streaming data using:

- Python
- Apache Kafka
- Spark Structured Streaming
- TimescaleDB
- Grafana
- Docker

## Architecture

```text
Python Producer → Kafka → Spark Structured Streaming → TimescaleDB → Grafana