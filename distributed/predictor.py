import ktrain
class CustomPredictor:

    predictor = ktrain.load_predictor("../model")

    def predict(self, data):
        result = self.predictor.predict(data)
        print("Result:", result, "len data:", len(data))
        return result
