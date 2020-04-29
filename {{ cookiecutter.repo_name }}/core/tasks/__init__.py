from invoke import Collection
import app, notebooks

ns = Collection()
ns.add_collection(app)
ns.add_collection(notebooks)
