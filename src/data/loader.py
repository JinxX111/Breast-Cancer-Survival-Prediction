import os
import sys

# Windows Hadoop Configuration
HADOOP_HOME = os.environ.get(
    "HADOOP_HOME",
    r"C:\hadoop"
)

os.environ["HADOOP_HOME"] = HADOOP_HOME
os.environ["hadoop.home.dir"] = HADOOP_HOME

os.environ["PATH"] = (
    HADOOP_HOME + r"\bin;"
    + os.environ["PATH"]
)


# Spark Python Environment
PYTHON_EXEC = sys.executable

os.environ["PYSPARK_PYTHON"] = PYTHON_EXEC
os.environ["PYSPARK_DRIVER_PYTHON"] = PYTHON_EXEC


from pyspark.sql import SparkSession


def create_spark_session(app_name="Spark Application"):

    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName(app_name)
        .config(
            "spark.sql.repl.eagerEval.enabled",
            "true"
        )
        .config(
            "spark.driver.extraJavaOptions",
            "-Djava.security.manager=allow"
        )
        .config(
            "spark.executor.extraJavaOptions",
            "-Djava.security.manager=allow"
        )
        .config(
            "spark.hadoop.hadoop.home.dir",
            HADOOP_HOME
        )
        .config(
            "spark.pyspark.python",
            PYTHON_EXEC
        )
        .config(
            "spark.pyspark.driver.python",
            PYTHON_EXEC
        )
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    return spark


def load_csv(spark, file_path):

    return (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .option("encoding", "UTF-8")
        .csv(file_path)
    )