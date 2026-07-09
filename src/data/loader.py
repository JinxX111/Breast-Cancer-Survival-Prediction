from pyspark.sql import SparkSession

def create_spark_session(app_name="SEER Breats Cancer Survival Prediction"):
    # Create Spark Session
    spark = (SparkSession.builder.appName(app_name).getOrCreate())
    return spark

def load_csv(spark, file_path):
    # Load dữ liệu vào Spark DataFrame
    df = (spark.read
          .option("header", True)
          .option("inferSchema", True)
          .option("encoding", "UTF-8")
          .csv(file_path)
        )
    return df
