import os
from dotenv import load_dotenv
import quote_plus

# Load environment variables from .env file
load_dotenv()
# DB_NAME = os.environ.get("POSTGRES_DB_NAME")
HOST = os.environ.get("POSTGRES_HOST")
PORT = os.environ.get("POSTGRES_PORT")
USER = os.environ.get("POSTGRES_USER")
quoted_password = quote_plus(os.environ.get("POSTGRES_PASSWORD"))
PASSWORD = quoted_password
POSTGRES_URL_STEM = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/"

class Config:
    """Base configuration class. Contains default settings."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_precious')

class TestConfig(Config):
    """Configurations for Testing."""
    TESTING = True
    POSTGRES_URL = POSTGRES_URL_STEM + "testDB"

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    POSTGRES_URL = POSTGRES_URL_STEM + "developmentDB"


class StageConfig(Config):
    """Configurations for Staging."""
    POSTGRES_URL = POSTGRES_URL_STEM + "stageDB"


class ProductionConfig(Config):
    """Configurations for Production."""
    POSTGRES_URL = POSTGRES_URL_STEM + "productionDB"
    

# Dictionary to map the environment name to the config class
configurations = {
    'test': TestConfig,
    'development': DevelopmentConfig,
    'stage': StageConfig,
    'production': ProductionConfig,
    'default': TestConfig
}
