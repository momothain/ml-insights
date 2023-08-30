# <app.py>
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import configurations
import argparse
# from routes import *

def create_app(env='test_local'):
    app = Flask(__name__)
    app.config.from_object(configurations[env])

    from models.models import db
    # Initialize the SQLAlchemy extension with the created app
    db.init_app(app) # initialize db with app here

    # Create database tables
    with app.app_context(): # This ensures the app context is pushed before using db
        db.create_all()

    return app

def main():
    parser = argparse.ArgumentParser(description="ML Data Processing App")
    parser.add_argument("-e", choices=configurations.keys(), default="test_local", help="Choose an environment: ")
    
    
    args = parser.parse_args()

    env = args.e

    # Create the app and db instances
    app = create_app(env)

    # Now you can use the app and db instances for further configuration or operations
    print(f"Selected environment: {env}")

    # Run the Flask app
    app.run()

if __name__ == '__main__':
    main()  
# </app.py>
