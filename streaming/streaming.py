from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("IoTSensorStreaming")
    .master("local[*]")
    .getOrCreate()
)

print("Spark started successfully!")

df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "iot-sensor-readings")
    .option("startingOffsets", "earliest")
    .load()
)

print("Successfully connected to Kafka!")

spark.stop()