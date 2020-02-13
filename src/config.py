class Config(object):
    ENV = "Production"
    DEBUG = False
    TESTING = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    SERVER_NAME = "127.0.0.1:5000"
    VIDEO_INPUT_PATH = None
    VIDEO_OUTPUT_PATH = None


class ProductionConfig(Config):
    SERVER_NAME = "0.0.0.0:8080"


class DevelopmentConfig(Config):
    ENV = "Development"
    DEBUG = True
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024
    SERVER_NAME = "127.0.0.1:3000"


class TestingConfig(Config):
    ENV = "Testing"
    TESTING = True
    SERVER_NAME = "127.0.0.1:8000"


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}