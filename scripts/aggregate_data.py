from pyspark.sql import SparkSession

def aggregate_data():
    spark = SparkSession.builder.appName("AggregateBreweryData").getOrCreate()
    silver_data = spark.read.parquet("/app/data/silver_breweries.parquet")
    aggregated_data = silver_data.groupBy("state", "brewery_type").count()
    aggregated_data.write.parquet("/app/data/gold_breweries.parquet")
