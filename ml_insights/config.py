# <config.py>
import os
from dotenv import load_dotenv

# from utility import load_postgres_url_from_env, check_virtualenv

# from utility import load_postgres_url_from_env, check_virtualenv  # , check_dependencies

REQUIREMENTS_FILE = "requirements.txt"
POSTGRES_URL_BASE = ""


def load_postgres_url_from_env():
    load_dotenv()
    required_env_vars = [
        "PGHOST",
        "PGPORT",
        "PGUSER",
        "PGPASSWORD",
    ]  #'POSTGRES_DB_NAME',

    # Check if all required environment variables are set
    for env_var in required_env_vars:
        if os.environ.get(env_var) is None:
            raise EnvironmentError(
                f"Required environment variable {env_var} is not set. Please see EXAMPLE.env and create .env accordingly"
            )
        # else:
        # print(env_var + ": " + os.environ.get(env_var))
    from urllib.parse import quote

    password = os.environ.get("PGPASSWORD")
    print(password)
    encoded_password = quote(password)
    print(encoded_password)

    HOST = os.environ.get("PGHOST")
    PORT = os.environ.get("PGPORT")
    USER = os.environ.get("PGUSER")
    PASSWORD = encoded_password
    POSTGRES_URL_BASE = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}"
    return POSTGRES_URL_BASE


import sys

# import pkg_resources


def check_virtualenv():
    if hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    ):
        return True
    return False


# def check_dependencies(requirements_file):
#     required_packages = fetch_required_packages(requirements_file)
#     installed_packages = [pkg.key for pkg in pkg_resources.working_set]

#     missing_packages = [pkg for pkg in required_packages if pkg not in installed_packages]

#     if missing_packages:
#         return missing_packages
#     return None


def fetch_required_packages(requirements_file):
    required_packages = []

    with open(requirements_file, "r") as f:
        for line in f:
            package_name = line.strip().split("==")[0]
            required_packages.append(package_name)

    return required_packages


###############################


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
    # SECRET_KEY = os.environ.get("SECRET_KEY", "my_precious")
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

#################################################
