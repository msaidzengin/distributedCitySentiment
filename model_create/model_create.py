import ktrain
from ktrain import text
import pandas as pd
from sklearn.model_selection import train_test_split

MODEL_NAME = 'dbmdz/bert-base-turkish-cased'

import numpy as np
import random as rn
import tensorflow as tf
import torch

tf.compat.v1.set_random_seed(0)
torch.manual_seed(0)
rn.seed(0)
np.random.seed(0)

df = pd.read_csv('data.csv', delimiter='\t', lineterminator='\n')

print(df)


dfx = list(df['Text'])
dfy = list(df['Sentiment'])

print(len(dfx))
print(len(dfy))

trainx, testx, trainy, testy = train_test_split(dfx, dfy, test_size = 0.2, random_state = 0, stratify = dfy)
print(len(trainx))
print(len(trainy))
print(len(testx))
print(len(testy))

#print(trainy)
#print(testy)



labels = list(set(dfy))

print("Len labels:" ,len(labels))

TARGET_CLASSES = labels
t = text.Transformer(MODEL_NAME, maxlen=500, classes=TARGET_CLASSES)

trn = t.preprocess_train(trainx, trainy)
val = t.preprocess_test(testx, testy)

model = t.get_classifier()
learner = ktrain.get_learner(model, train_data=trn, val_data=val, batch_size=6)

learner.fit_onecycle(5e-5, 1)

p = ktrain.get_predictor(learner.model, preproc=t) 

p.save("model")
print("Model saved")

from sklearn import metrics
preds = p.predict(testx)
act_preds = testy
#preds_proba = p.predict_proba(testx)

print(metrics.confusion_matrix(act_preds, preds))
print(metrics.classification_report(act_preds, preds, digits=3))
