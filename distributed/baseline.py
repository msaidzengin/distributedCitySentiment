from pyspark import SparkContext
from predictor import CustomPredictor
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
import datetime
from pyspark.sql.functions import udf, col
import glob
import multiprocessing
from pyspark.sql.types import *
import pandas as pd
predictor = CustomPredictor()
spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

def predict(text):
    prediction = predictor.predict(text)
    return prediction


predict_udf = udf(predict, IntegerType())

if __name__ == '__main__':

    all_files = glob.glob("../data/*.txt")
    print("Total number of files:", len(all_files))

    all_tweets = {}
    for filename in all_files:
        city_name = filename.split("/")[-1].split(".")[0]
        print("Opening file:", filename, city_name)
        with open(filename) as myfile:
            tweets = [next(myfile) for x in range(10000)]
        all_tweets[city_name] = tweets

    start_time = datetime.datetime.now()

    for city, tweet in all_tweets.items():
        print(len(tweet))
        for t in tweet:
            predictor.predict(t)
        # pdd = pd.DataFrame(tweet)
        # df = spark.createDataFrame(pdd)
        # df = df.repartition(multiprocessing.cpu_count())
        # print("df.rdd.getNumPartitions()", df.rdd.getNumPartitions())
        # print("----------")
        #
        # df = df.withColumn('prediction', predict_udf(col('0')))
        #
        # df.show()
        break

    end_time = datetime.datetime.now()
    print("total time:", end_time - start_time)
