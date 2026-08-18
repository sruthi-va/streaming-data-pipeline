from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    TimestampType,
    DoubleType,
    IntegerType
)
from pyspark.sql.functions import from_json, col


# Spark Session

spark = (
    SparkSession.builder
    .appName("IoTSensorStreaming")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

print("Spark started successfully!")


# JSON Schema

schema = StructType([
    StructField("sensor_id", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("temperature", DoubleType(), True),
    StructField("humidity", DoubleType(), True),
    StructField("battery_level", IntegerType(), True),
    StructField("location", StringType(), True)
])


# Read from Kafka

df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "kafka:29092")
    .option("subscribe", "iot-sensor-readings")
    .option("startingOffsets", "latest")
    .load()
)

print("Connected to Kafka!")


# Parse JSON

parsed_df = df.select(
    from_json(
        col("value").cast("string"),
        schema
    ).alias("data")
)


# Flatten JSON into columns

parsed_df = parsed_df.select("data.*")

# Validate events
valid_df = parsed_df.filter(
    col("sensor_id").isNotNull()
    & col("timestamp").isNotNull()
    & col("temperature").isNotNull()
    & col("temperature").between(-50, 100)
    & col("humidity").isNotNull()
    & col("humidity").between(0, 100)
    & col("battery_level").isNotNull()
    & col("battery_level").between(0, 100)
)


# Write to console

query = (
    valid_df.writeStream
    .format("console")
    .outputMode("append")
    .option("truncate", False)
    .option("checkpointLocation", "/tmp/checkpoints/kafka_parsed")
    .start()
)

print("Streaming started!")


query.awaitTermination()