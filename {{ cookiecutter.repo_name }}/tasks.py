from invoke import Collection, task
# Default tasks are in core.tasks
from core.tasks import app, notebooks
# Adds in default tasks
ns = Collection()
ns.add_collection(app)
ns.add_collection(notebooks)

### Add project-specific tasks below.
# See http://docs.pyinvoke.org/en/stable/getting-started.html
