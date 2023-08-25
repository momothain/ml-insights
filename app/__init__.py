from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import configurations

app = Flask(__name__)
app.config.from_object(Config)  # Load configurations

# SQLAlchemy setup
db = SQLAlchemy(app)



db.create_all()

# ... your routes, models, and other code ...

if __name__ == '__main__':
    app.run()
