from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test-app.db'
db = SQLAlchemy(app)

# Import models and routes
from models.models2 import *
from routes import *

db.create_all()

if __name__ == '__main__':
    app.run()
    
    # TODO: Fetch data from media and ad (campaign) tables
    
    # TODO: ml insights API Code here
    ## prahsanhta and metao
    
    # TODO: Data cleaning / preprocessing
    
    # TODO: update tags tables
    
    # TODO: await GET request for URL
    # TODO: schedule request check for any media.is_processed=0

