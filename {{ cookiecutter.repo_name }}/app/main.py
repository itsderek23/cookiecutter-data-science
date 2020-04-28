import flask
from src.models.model_wrapper import ModelWrapper
import sys
import os

def dvc_pull():
    # The deployed app isn't a git repo but needs to be for dvc
    os.system("git init")
    # Pull the training output (the serialized model) when running on a deployed server.
    #os.system("dvc pull train.dvc")

# initialize the Flask application
app = flask.Flask(__name__)
dvc_pull()
model = ModelWrapper()

@app.route("/predict", methods=["POST"])
def predict():
    input = flask.request.json['data']
    result = model.predict(input)
    return flask.jsonify(result)

if __name__ == "__main__":
    app.run()
