from pyspark.sql import SparkSession
import json

def transform_data():
    spark = SparkSession.builder.appName("TransformBreweryData").getOrCreate()
    raw_data = spark.read.json("/app/data/raw_breweries.json")
    raw_data.write.parquet("/app/data/bronze_breweries.parquet")
    silver_data = raw_data.repartition("state")
    silver_data.write.parquet("/app/data/silver_breweries.parquet")
