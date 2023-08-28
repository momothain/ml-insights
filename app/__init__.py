from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import configurations
import os

def create_app(env='test'):
    app = Flask(__name__)
    # env = os.environ.get['FLASK_ENV']
    app.config.from_object(configurations[env])  # Load configurations

    # SQLAlchemy setup
    db = SQLAlchemy(app)
    # Initialize Flask extensions here

    # Register blueprints here


    db.create_all()

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app

# ... your routes, models, and other code ...

# if __name__ == '__main__':
#     app.run()
