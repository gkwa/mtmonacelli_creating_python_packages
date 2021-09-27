import argparse
import pathlib
import stat

import jinja2

parser = argparse.ArgumentParser()
parser.add_argument("--project", required=True, help="project name")
args = parser.parse_args()

env = jinja2.Environment(keep_trailing_newline=True)
env.loader = jinja2.FileSystemLoader(searchpath="./templates")

data = {
    "project_name": args.project,
}

path = pathlib.Path("step1.sh")
tpl = env.get_template("twine_credentials.j2")
rtpl = tpl.render(data=data)
path.write_text(rtpl)
path.chmod(path.stat().st_mode | stat.S_IEXEC)

path = pathlib.Path("step2.sh")
tpl = env.get_template("cookiecutter.j2")
rtpl = tpl.render(data=data)
path.write_text(rtpl)
path.chmod(path.stat().st_mode | stat.S_IEXEC)

path = pathlib.Path("test_locally.sh")
tpl = env.get_template(f"{path.stem}.j2")
rtpl = tpl.render(data=data)
path.write_text(rtpl)
path.chmod(path.stat().st_mode | stat.S_IEXEC)

path = pathlib.Path("upload_test.sh")
tpl = env.get_template(f"{path.stem}.j2")
rtpl = tpl.render(data=data)
path.write_text(rtpl)
path.chmod(path.stat().st_mode | stat.S_IEXEC)
