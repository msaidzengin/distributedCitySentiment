import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
import pandas as pd
import datetime
import random, time

import multiprocessing

print(multiprocessing.cpu_count())
print("------------")


spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext


def predict(text):
    return text + ' ' + str(datetime.datetime.now())

predict_udf = udf(predict, StringType())

df = spark.read.csv('test.csv', header=True)
df = df.repartition(multiprocessing.cpu_count())
print("df.rdd.getNumPartitions()", df.rdd.getNumPartitions())
print("----------")
df = df.withColumn('prediction', predict_udf(col('text')))

df.show()

df.write.csv('result4', header=True)