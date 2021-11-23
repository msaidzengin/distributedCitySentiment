import glob
import datetime
import ktrain

start_time = datetime.datetime.now()

all_files = glob.glob("../data/*.txt") 
print("Total number of files:", len(all_files))

model = ktrain.load_predictor("../model")
print("Sentiment model loaded")

cities = {}
for filename in all_files:
    print("Opening file:", filename)
    # cities[filename] = []
    with open(filename) as myfile:
        tweets = [next(myfile) for x in range(10)]
    
    # model.predict(tweets)
    # cities[filename] = preedictions

# json.dump(cities, open("result.json", "w"))

end_time = datetime.datetime.now()
print("Total time:", end_time - start_time)
