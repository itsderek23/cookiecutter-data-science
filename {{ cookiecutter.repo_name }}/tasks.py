from invoke import Collection, task
# Default tasks are in core.tasks
import core.tasks.app as app
import core.tasks.notebooks as notebooks
# Add default task collections
ns = Collection()
ns.add_collection(app)
ns = Collection(app)
ns.add_collection(notebooks)

### Add project-specific tasks below. ###
# See http://docs.pyinvoke.org/en/stable/getting-started.html

from src.models.model_wrapper import ModelWrapper

@task(help={'data': "An array of data to perform model inference"})
def predict(c, data):
    """
    Invokes the model.
    """
    model = ModelWrapper()
    print(model.predict(data))

model = Collection('model')
model.add_task(predict)
ns.add_collection(model)
