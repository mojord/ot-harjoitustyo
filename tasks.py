from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/textinterface.py")

def test(ctx):
    ctx.run("pytest src")

def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

def coverage_report(ctx):
    ctx.run("coverage html")
