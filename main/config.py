class Config:
    DEBUG = False
    HOST = '0.0.0.0'
    CORS_HEADER = 'Content-Type'


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 4040


class ProductionConfig(Config):
    DEBUG = False
    PORT = 4050


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)
