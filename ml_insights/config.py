# <config.py>
import os
from utility import load_postgres_url_from_env, check_virtualenv  # , check_dependencies


REQUIREMENTS_FILE = "requirements.txt"

POSTGRES_URL_BASE = ""


class Config:
    if not check_virtualenv():
        raise EnvironmentError(
            "Please activate your virtual environment. See README.md"
        )
    # missing_deps = check_dependencies(REQUIREMENTS_FILE)
    # if missing_deps:
    #     raise EnvironmentError(f"The following dependencies are missing: {', '.join(missing_deps)}. See README.md")

    POSTGRES_URL_BASE = load_postgres_url_from_env()

    DEBUG = False
    TESTING = False
    os.environ.setdefault("FLASK_APP", "app")
    os.environ.setdefault("FLASK_ENV", "test")
    SECRET_KEY = os.environ.get("SECRET_KEY", "my_precious")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestLocalConfig(Config):
    TESTING = True
    # LOCAL_SQLITE_URL

    SQLALCHEMY_DATABASE_URI = "sqlite:///localtest.db"


class TestConfig(Config):
    TESTING = True
    # POSTGRES_URL
    POSTGRES_URL_BASE = load_postgres_url_from_env()
    DATABASE_NAME = "/1"
    SQLALCHEMY_DATABASE_URI = POSTGRES_URL_BASE + DATABASE_NAME

    # Open a file in append mode ('a')
    file_path = "./postgres_url.txt"

    with open(file_path, "a") as file:
        file.write("\n" + SQLALCHEMY_DATABASE_URI + "\n")

    print(SQLALCHEMY_DATABASE_URI)


class DevelopmentConfig(Config):
    DEBUG = True
    # POSTGRES_URL
    POSTGRES_URL_BASE = load_postgres_url_from_env()
    SQLALCHEMY_DATABASE_URI = POSTGRES_URL_BASE + "/developmentDB"


class StageConfig(Config):
    # POSTGRES_URL
    POSTGRES_URL_BASE = load_postgres_url_from_env()
    SQLALCHEMY_DATABASE_URI = POSTGRES_URL_BASE + "/stageDB"


class ProductionConfig(Config):
    # POSTGRES_URL
    SQLALCHEMY_DATABASE_URI = POSTGRES_URL_BASE + "/productionDB"


# Dictionary to map the environment name to the config class
configurations = {
    "test_local": TestLocalConfig,
    "test": TestConfig,
    "development": DevelopmentConfig,
    "stage": StageConfig,
    "production": ProductionConfig,
    "default": TestConfig,
}
