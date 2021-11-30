import ktrain
class CustomPredictor:

    predictor = ktrain.load_predictor("../model")


    def predict(self, data):
        data = str(data)
        return self.predictor.predict(data)

