import os
from dotenv import load_dotenv
import quote_plus

load_dotenv()
HOST = os.environ.get("POSTGRES_HOST")
PORT = os.environ.get("POSTGRES_PORT")
USER = os.environ.get("POSTGRES_USER")
quoted_password = quote_plus(os.environ.get("POSTGRES_PASSWORD"))
PASSWORD = quoted_password
POSTGRES_URL_STEM = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/"

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_precious')

class TestConfig(Config):
    TESTING = True
    POSTGRES_URL = POSTGRES_URL_STEM + "testDB"

class DevelopmentConfig(Config):
    DEBUG = True
    POSTGRES_URL = POSTGRES_URL_STEM + "developmentDB"

class StageConfig(Config):
    POSTGRES_URL = POSTGRES_URL_STEM + "stageDB"

class ProductionConfig(Config):
    POSTGRES_URL = POSTGRES_URL_STEM + "productionDB"

class TestLocalConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///local_test.db"  # SQLite URI for local testing

# Dictionary to map the environment name to the config class
configurations = {
    'test': TestConfig,
    'development': DevelopmentConfig,
    'stage': StageConfig,
    'production': ProductionConfig,
    'test_local': TestLocalConfig,  # Add the local test configuration
    'default': TestConfig
}
