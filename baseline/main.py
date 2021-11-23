import glob
import datetime
import ktrain
import json

start_time = datetime.datetime.now()

all_files = glob.glob("../data/*.txt") 
print("Total number of files:", len(all_files))

model = ktrain.load_predictor("../model")
print("Sentiment model loaded")

cities = {}
for filename in all_files:

    city_name = filename.split("/")[-1].split(".")[0]
    print("Opening file:", filename, city_name)

    with open(filename) as myfile:
        tweets = [next(myfile) for x in range(1)]
    
    predictions = model.predict(tweets)
    cities[city_name] = predictions

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(cities, f, ensure_ascii=False, indent=4)

end_time = datetime.datetime.now()
print("Total time:", end_time - start_time)
