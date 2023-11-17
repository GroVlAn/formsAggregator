import sys

from main.config.config import config_by_name

args = sys.argv
mode = 'dev'

if '--prod' in args:
    mode = 'prod'

if '--dev' in args:
    mode = 'dev'

conf = config_by_name[mode]