class Config:
    DEBUG = False
    HOST = '0.0.0.0'
    CORS_HEADER = 'Content-Type'
    MONGO_PORT = 27017


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 4040
    MONGO_HOST = 'forms-aggregator-db-dev'


class ProductionConfig(Config):
    DEBUG = False
    PORT = 4050
    MONGO_HOST = 'forms-aggregator-db'


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)
