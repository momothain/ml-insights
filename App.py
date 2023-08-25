from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///media.db'  # Using SQLite for simplicity
db = SQLAlchemy(app)

class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    media_name = db.Column(db.String(150), nullable=False)
    media_url = db.Column(db.String(500), nullable=False)
    tag = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()


import pandas as pd

media_data = Media.query.all()
df = pd.DataFrame([(d.media_name, d.media_url, d.tag) for d in media_data], columns=['Media Name', 'Media URL', 'Tag'])

