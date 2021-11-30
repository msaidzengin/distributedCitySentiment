from pyspark import SparkContext
from predictor import CustomPredictor
import glob

if __name__ == '__main__':

    all_files = glob.glob("../data/*.txt") 
    print("Total number of files:", len(all_files))

    all_tweets = {}
    for filename in all_files:

        city_name = filename.split("/")[-1].split(".")[0]
        print("Opening file:", filename, city_name)

        with open(filename) as myfile:
            tweets = [next(myfile) for x in range(50)]
        
        all_tweets[city_name] = tweets
    
    predictor = CustomPredictor()
    sc = SparkContext("local", "primes")

    for city, tweet in all_tweets.items():

        nums = sc.parallelize(tweet, 4)
        nums.filter(predictor.predict).count()
        break

    predictor.show_results()
