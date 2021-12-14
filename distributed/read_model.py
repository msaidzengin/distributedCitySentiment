import pickle
import ktrain

model = ktrain.load_predictor('../model')


picke_out = open('model.pkl', 'wb')
pickle.dump(model, picke_out)
picke_out.close()
