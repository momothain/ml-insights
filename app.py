# <app.py>
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import configurations
import argparse
from models.models2 import db # importing db here
# from routes import *

def create_app(env):
    app = Flask(__name__)
    app.config.from_object(configurations[env])
    
    # Initialize the SQLAlchemy extension with the created app
    db.init_app(app)  # initialize db with app here
    
    # Create database tables
    with app.app_context():  # This ensures the app context is pushed before using db
        db.create_all()
    
    return app


def main():
    parser = argparse.ArgumentParser(description="ML Data Processing App")
    parser.add_argument("config", choices=configurations.keys(), help="Choose a configuration: ")
    
    args = parser.parse_args()
    
    config_key = args.config
    env = configurations[config_key]
    
    # Create the app and db instances
    app, db = create_app(env)
    
    # Now you can use the app and db instances for further configuration or operations
    print(f"Selected configuration: {config_key}")
    
    # Run the Flask app
    app.run()

if __name__ == '__main__':
    main()
# </app.py>
