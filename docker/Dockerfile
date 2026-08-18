FROM apache/spark:4.0.0

USER root

WORKDIR /app

COPY streaming /app/streaming

CMD ["/opt/spark/bin/spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.13:4.0.0", "/app/streaming/streaming.py"]