# set_env_from_dotenv.py

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Print loaded environment variables
print("Environment variables loaded from .env:")
print("========================================")
for key, value in os.environ.items():
    print(f"{key}: {value}")

