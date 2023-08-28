import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()
HOST = os.environ.get("POSTGRES_HOST")
PORT = os.environ.get("POSTGRES_PORT")
USER = os.environ.get("POSTGRES_USER")
quoted_password = quote_plus(os.environ.get("POSTGRES_PASSWORD"))
PASSWORD = quoted_password
POSTGRES_URL_BASE = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}"

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_precious')

class TestConfig(Config):
    TESTING = True
    POSTGRES_URL = POSTGRES_URL_BASE + "/testDB"

class DevelopmentConfig(Config):
    DEBUG = True
    POSTGRES_URL = POSTGRES_URL_BASE + "/developmentDB"

class StageConfig(Config):
    POSTGRES_URL = POSTGRES_URL_BASE + "/stageDB"

class ProductionConfig(Config):
    POSTGRES_URL = POSTGRES_URL_BASE + "/productionDB"

class LocalTestConfig(Config):
    TESTING = True
    LOCAL_SQLITE_URL = "sqlite:///local_test.db"  # SQLite URI for local testing

# Dictionary to map the environment name to the config class
configurations = {
    'local_test': LocalTestConfig,
    'test': TestConfig,
    'development': DevelopmentConfig,
    'stage': StageConfig,
    'production': ProductionConfig,
    'default': TestConfig
}

