from flask_sqlalchemy import SQLAlchemy
from app import db

# store .mp4 together? = media URLs 
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime)
    tag_category = db.Column(db.String(50), nullable=False)
    media_category = db.Column(db.String(50), nullable=False)
    ordinal_tag = db.Column(db.Integer) # for low, med, high just show the number of ranks and we'll handle this as one-hots later
    source_API = db.Column(db.String(50))
    # Define the many-to-many relationship with Ad/Video
    ad_ids = db.relationship('Ad', secondary='tag_ad', back_populates='tag_ids')

class TagCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_category = db.Column(db.String(50), nullable=False)
    tag_ids = db.relationship('Tag', back_populates='category')

class Cluster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(100), nullable=False)
    tag_ids = db.relationship('Tag', secondary='tag_cluster', back_populates='clusters')

class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Define the many-to-many relationship with MLDataSpecsTag
    tag_ids = db.relationship('Tag', secondary='tag_ad', back_populates='ad_ids')
    cluster_ids = db.relationship('Cluster', secondary='ad_cluster', back_populates='ads')

tag_ad = db.Table('tag_ad',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('ad_id', db.Integer, db.ForeignKey('ad.id'), primary_key=True)
)

tag_cluster = db.Table('tag_cluster',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('cluster_id', db.Integer, db.ForeignKey('cluster.id'), primary_key=True)
)

ad_cluster = db.Table('ad_cluster',
    db.Column('ad_id', db.Integer, db.ForeignKey('ad.id'), primary_key=True),
    db.Column('cluster_id', db.Integer, db.ForeignKey('cluster.id'), primary_key=True)
)
