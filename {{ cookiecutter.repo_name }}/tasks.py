from invoke import Collection, task
import sys
import subprocess

@task(help={"relative_path": "Relative path to the notebook"})
def run(c, relative_path):
    """
    Run a notebook from the command line.
    """
    c.run("jupyter nbconvert --to notebook --ExecutePreprocessor.timeout=1000 --execute {}".format(relative_path))
    sys.stdout.flush()
nbs = Collection('notebooks')
nbs.add_task(run)

@task
def start(c):
    """
    Start the web service serving model inference.
    """
    c.run("honcho -f app/Procfile.dev start", pty=True)

def has_unstaged_changes():
    res=subprocess.check_output("git status --porcelain",shell=True, text=True)
    return ("\n" in res)

@task(help={'name': "Name of the Heroku app."})
def create(c,name):
    """
    Create a Heroku app for the web service.
    """
    if has_unstaged_changes():
        print("This project has uncommitted changes.\nPlease add and commit the files to the Git repo, then retry:\n\ngit add .\ngit commit -m 'First Commit'")
        exit(1)
    c.run("heroku create -a {}".format(name))
    c.run("heroku buildpacks:add -a {} https://github.com/heroku/heroku-buildpack-multi-procfile".format(name))
    c.run("heroku buildpacks:add heroku/python")
    c.run("heroku config:set PROCFILE=app/Procfile")
    c.run("git push heroku master")

@task
def destroy(c):
    """
    Delete the Heroku app.
    """
    c.run("heroku apps:destroy", pty=True)

@task
def test(c):
    """
    Run the web service unit tests.
    """
    c.run("python app/test.py")

app = Collection('app')
app.add_task(start)
app.add_task(test)
app.add_task(create)
app.add_task(destroy)


ns = Collection()
ns.add_collection(nbs)
ns.add_collection(app)
