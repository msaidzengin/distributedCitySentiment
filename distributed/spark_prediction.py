import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType, DoubleType
import pandas as pd
import datetime
import random, time

import multiprocessing

print(multiprocessing.cpu_count())
print("------------")
import pickle

spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext



model_rdd_pkl = sc.binaryFiles("../classifier.pickle")
model_rdd_data = model_rdd_pkl.collect()

tfidf = sc.binaryFiles("../tfidfmodel.pickle")
tfidf_rdd_data = tfidf.collect()


# Load and broadcast python object over spark nodes
creditcardfrauddetection_model = pickle.loads(model_rdd_data[0][1])
broadcast_creditcardfrauddetection_model = sc.broadcast(creditcardfrauddetection_model)
print(broadcast_creditcardfrauddetection_model.value)

tfidf_model = pickle.loads(tfidf_rdd_data[0][1])
broadcast_tfidf_model = sc.broadcast(tfidf_model)
print(broadcast_tfidf_model.value)


def predict(text):
    vector = broadcast_tfidf_model.value.transform([text]).toarray()
    sent = broadcast_creditcardfrauddetection_model.value.predict_proba(vector)
    return str(sent)

import datetime



predict_udf = udf(predict, StringType())

df = spark.read.csv('test2.csv', header=True)
df = df.repartition(multiprocessing.cpu_count())
print("df.rdd.getNumPartitions()", df.rdd.getNumPartitions())
print("----------")
start_time = datetime.datetime.now()
df = df.withColumn('prediction', predict_udf(col('text')))
end_time = datetime.datetime.now()
df.show()



print("Time taken: ", end_time - start_time)

#df.write.csv('result_text', header=True)

