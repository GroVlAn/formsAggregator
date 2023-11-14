import sys

from main.application import create_app
from main.config import config_by_name

args = sys.argv
mode = 'dev'

if '--prod' in args:
    mode = 'prod'

if '--dev' in args:
    mode = 'dev'

conf = config_by_name[mode]

app = create_app(
    conf=conf
)
app.app_context().push()

from .controllers import *
