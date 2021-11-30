import ktrain
class CustomPredictor:

    predictor = ktrain.load_predictor("../model")
    results = []

    def predict(self, data):
        data = str(data)
        result = self.predictor.predict(data)
        self.results.append([data, result])
        print(result, data)
        return result

    def show_results(self):
        print(self.results)

