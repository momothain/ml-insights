from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
db = SQLAlchemy(app)


def init():
    load_dotenv()

class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    media_name = db.Column(db.String(150), nullable=False)
    media_url = db.Column(db.String(500), nullable=False)
    tag = db.Column(db.String(50), nullable=False)

@app.route('/add_media', methods=['POST'])
def add_media():
    data = request.json
    new_media = Media(
        media_name=data['media_name'],
        media_url=data['media_url'],
        tag=data['tag']
    )
    db.session.add(new_media)
    db.session.commit()
    return jsonify({"message": "Media added successfully!"}), 201


with app.app_context():
    db.create_all()


import pandas as pd

media_data = Media.query.all()
df = pd.DataFrame([(d.media_name, d.media_url, d.tag) for d in media_data], columns=['Media Name', 'Media URL', 'Tag'])

