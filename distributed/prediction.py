import ktrain
model = ktrain.load_predictor("../model")

def predict(text):
    return model.predict(text)
