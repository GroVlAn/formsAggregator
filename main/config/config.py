class Config:
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = ''
    CORS_HEADER = 'Content-Type'
    MONGO_PORT = 27017
    MONGO_HOST = ''


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 4040
    MONGO_HOST = 'forms-aggregator-db-dev'


class ProductionConfig(Config):
    DEBUG = False
    PORT = 4050
    MONGO_HOST = 'forms-aggregator-db'


config_by_name = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}

NAME_DATABASE = 'forms_aggregator_db'
FORM_DOCUMENT = 'form'
