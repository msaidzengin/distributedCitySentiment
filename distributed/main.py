from pyspark import SparkContext
from predictor import CustomPredictor
import glob
import datetime

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

if __name__ == '__main__':

    start_time = datetime.datetime.now()

    all_files = glob.glob("../data/*.txt") 
    print("Total number of files:", len(all_files))

    all_tweets = {}
    for filename in all_files:

        city_name = filename.split("/")[-1].split(".")[0]
        print("Opening file:", filename, city_name)

        with open(filename) as myfile:
            tweets = [next(myfile) for x in range(5000)]
        
        all_tweets[city_name] = tweets
    
    predictor = CustomPredictor()
    sc = SparkContext("local", "primes")

    tweets = all_tweets["Ankara"]
    tw_list = chunks(tweets, 100)

   
    nums = sc.parallelize(tw_list, 4)
    nums.filter(predictor.predict).count()

    end_time = datetime.datetime.now()
    print("Total time:", end_time - start_time)
