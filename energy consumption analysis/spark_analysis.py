from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder \
    .appName("EnergyAnalysis") \
    .getOrCreate()

# Load dataset
df = spark.read.csv("data/energy.csv", header=True, inferSchema=True)

# Remove null values
df = df.dropna()

# Convert power column to float
df = df.withColumn("Global_active_power",
                   df["Global_active_power"].cast("float"))

# Average energy consumption
avg_power = df.select(avg("Global_active_power"))
avg_power.show()

# Daily average consumption
daily_avg = df.groupBy("Date").avg("Global_active_power")
daily_avg.show()

spark.stop()