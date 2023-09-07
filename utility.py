import os
from dotenv import load_dotenv
from urllib.parse import quote_plus


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
        else:
            print(env_var + ": " + os.environ.get(env_var))

    HOST = os.environ.get("PGHOST")
    PORT = os.environ.get("PGPORT")
    USER = os.environ.get("PGUSER")
    PASSWORD = quote_plus(os.environ.get("PGPASSWORD"))
    POSTGRES_URL_BASE = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}"
    print(POSTGRES_URL_BASE)
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
