import pickle
import pandas as pd

#Vectorizer
with open('../tfidfmodel.pickle', 'rb') as f:
    vectorizer = pickle.load(f)
    
#Model
with open('../classifier.pickle', 'rb') as f:
    classifier = pickle.load(f)

df = pd.read_csv('test2.csv', encoding='utf-8', sep='#################;;')
print(df)

total_pos = 0
total_neg = 0

import datetime
start_time = datetime.datetime.now()

for tweet in df.text:
    #Predicting The Reslts
    sent = classifier.predict(vectorizer.transform([tweet]).toarray())
    if sent[0] == 1:
        total_pos += 1
    else:
        total_neg += 1

end_time = datetime.datetime.now()
print("Total time taken: ", end_time - start_time)


print("Positive: ", total_pos)
print("Negative: ", total_neg)
