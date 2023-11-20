import sys

from main.app.application import FormsApplication
from main.config.config import NAME_DATABASE, config_by_name
from main.database.mongo import create_mongo
from main.logger import Logger

args = sys.argv
mode = 'dev'

if '--prod' in args:
    mode = 'prod'

if '--dev' in args:
    mode = 'dev'

conf = config_by_name[mode]

client = create_mongo(conf.MONGO_HOST, conf.MONGO_PORT)
db = client[NAME_DATABASE]

application = FormsApplication()
application.set_config()

application.create_app()
logger = Logger()
logger.set_app(application.get_app())


