from main.config import conf
from main.config.config import NAME_DATABASE
from main.database.mongo import create_mongo

client = create_mongo(conf.MONGO_HOST, conf.MONGO_PORT)
db = client[NAME_DATABASE]