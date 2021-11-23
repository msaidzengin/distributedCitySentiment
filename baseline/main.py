import glob
import datetime
import ktrain
import json

start_time = datetime.datetime.now()

all_files = glob.glob("../data/*.txt") 
print("Total number of files:", len(all_files))

all_tweets = {}
for filename in all_files:

    city_name = filename.split("/")[-1].split(".")[0]
    print("Opening file:", filename, city_name)

    with open(filename) as myfile:
        tweets = [next(myfile) for x in range(2)]
    
    all_tweets[city_name] = tweets


model = ktrain.load_predictor("../model")
print("Sentiment model loaded")

results = {}
for city, tweet in all_tweets.items():
    print("\nCity:", city)
    res = []
    for t in tweet:
        print(t)
        prediction = model.predict(t)
        res.append(prediction)
    results[city] = res


with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

percents = {}
for city, res in results.items():
    percents[city] = sum(res) / len(res)

with open('percents.json', 'w', encoding='utf-8') as f:
    json.dump(percents, f, ensure_ascii=False, indent=4)

end_time = datetime.datetime.now()
print("Total time:", end_time - start_time)
