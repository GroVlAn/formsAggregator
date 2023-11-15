import sys

from flask_cors import CORS

from main.application import create_app
from main.config import config_by_name
from .database.mongo import create_mongo
from .logger.logger import Logger

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

appLogger = Logger(app=app)

CORS(app)

client = create_mongo(conf.MONGO_HOST, conf.MONGO_PORT)
db = client.forms_aggregator_db


from .controllers import *
