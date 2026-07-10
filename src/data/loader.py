import os

# Windows Hadoop Configuration

os.environ.setdefault("HADOOP_HOME", r"C:\hadoop")
os.environ.setdefault("hadoop.home.dir", r"C:\hadoop")


from pyspark.sql import SparkSession

def create_spark_session(app_name: str = "Spark Application"):

    spark = (
        SparkSession.builder
        .appName(app_name)
        .config("spark.sql.repl.eagerEval.enabled", "true")
        .config("spark.driver.extraJavaOptions", "-Djava.security.manager=allow")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

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
