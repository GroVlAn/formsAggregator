from main.app.application import create_app
from .config import conf
from .config.config import config_by_name
from .database.mongo import create_mongo
from .logger import appLogger
from .logger.logger import Logger

app = create_app(conf=conf)
appLogger.set_app(app=app)
