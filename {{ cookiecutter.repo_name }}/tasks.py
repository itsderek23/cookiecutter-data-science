from invoke import Collection, task
import sys

@task
def run(c, relative_path):
    c.run("jupyter nbconvert --to notebook --ExecutePreprocessor.timeout=1000 --execute {}".format(relative_path))
    sys.stdout.flush()
nbs = Collection('notebooks')
nbs.add_task(run)

@task
def start(c):
    c.run("honcho -f app/Procfile.dev start", pty=True)

@task
def test(c):
    c.run("python app/test.py")

app = Collection('app')
app.add_task(start)
app.add_task(test)


ns = Collection()
ns.add_collection(nbs)
ns.add_collection(app)
