class DummyModel:
    """
    A placeholder for a real ML Model. Returns the number of features in each row.

    Example:

        DummyModel().predict([[1,2],[3,4]]) => [2,2]
    """
    def predict(self,X):
        return list(map(lambda instance: len(instance), X))

class ModelWrapper:
    def __init__(self):
        """
        Load the model + required pre-processing artifacts from disk.
        Use paths relative to the project root directory.

        Tensorflow example:

            self.model = load_model("models/model.h5")
        """
        # REPLACE ME - add your loading logic
        self.model = DummyModel()

    def predict(self,data):
        return self.model.predict(data)
