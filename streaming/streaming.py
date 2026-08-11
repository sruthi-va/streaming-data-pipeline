from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("IoTSensorStreaming")
    .master("local[*]")
    .getOrCreate()
)

print("Spark started successfully!")
print(f"Spark version: {spark.version}")

spark.stop()
print("Spark stopped.")