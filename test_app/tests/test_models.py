import os
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Import your models here (e.g., Tag, TagCategory, etc.)
from app import Tag, TagCategory, Cluster, Ad
from config import TestLocalConfig  # Import your TestConfig class

# Define your test cases using pytest
def test_example():
    # Your test code here
    pass

@pytest.fixture
def app():
    # Create an instance of Flask app and set its configuration
    app = Flask(__name__)
    app.config.from_object(TestLocalConfig)  # Load TestConfig for testing
    db = SQLAlchemy(app)
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

def test_create_and_query_tag(app):
    with app.app_context():
        tag = Tag(tag='happy', tag_category='sentiment')
        db.session.add(tag)
        db.session.commit()
        
        queried_tag = Tag.query.filter_by(tag='happy').first()
        assert queried_tag is not None
        assert queried_tag.tag_category == 'sentiment'

def test_create_and_query_tag_category(app):
    with app.app_context():
        tag_category = TagCategory(tag_category='emotion')
        db.session.add(tag_category)
        db.session.commit()
        
        queried_category = TagCategory.query.filter_by(tag_category='emotion').first()
        assert queried_category is not None

def test_create_and_query_cluster(app):
    with app.app_context():
        cluster = Cluster(tag='important')
        db.session.add(cluster)
        db.session.commit()
        
        queried_cluster = Cluster.query.filter_by(tag='important').first()
        assert queried_cluster is not None

def test_create_and_query_ad(app):
    with app.app_context():
        ad = Ad()
        db.session.add(ad)
        db.session.commit()
        
        queried_ad = Ad.query.first()
        assert queried_ad is not None
