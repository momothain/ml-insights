# <models.py>from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

db = SQLAlchemy()

# store .mp4 together? = media URLs
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.Float)
    end_time = db.Column(db.Float)
    shot_num = db.Column(db.Integer, nullable=False, default=1)
    __table_args__ = (CheckConstraint('shot_num > 0', name='positive_shot_num'),)
    tag_category_name = db.Column(db.Integer, db.ForeignKey('tag_category.tag_category'), nullable=False) # This is the foreign key for the relationship
    tag_category = db.relationship('TagCategory', back_populates='tags') # New relationship field
    # tag_category xw= db.Column(db.String(50), nullable=False)
    media_category = db.Column(db.String(50), nullable=False)
    num_ordinal_ranks = db.Column(db.Integer) # for low, med, high just show the number of ranks and we'll handle this as one-hots later
    source_API = db.Column(db.String(50))
    # Define the many-to-many relationship with Ad
    ads = db.relationship('Ad', secondary='ad_tag_association', back_populates='tags')
    clusters = db.relationship('Cluster', secondary='tag_cluster_association', back_populates='tags')

class TagCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_category = db.Column(db.String(50), nullable=False, unique=True)
    tags = db.relationship('Tag', back_populates='tag_category')

class Cluster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(100), nullable=False)
    ads = db.relationship('Ad', secondary='ad_cluster_association', back_populates='clusters')
    tags = db.relationship('Tag', secondary='tag_cluster_association', back_populates='clusters')

class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Define the many-to-many relationship with MLDataSpecsTag
    tags = db.relationship('Tag', secondary='ad_tag_association', back_populates='ads')
    clusters = db.relationship('Cluster', secondary='ad_cluster_association', back_populates='ads')


ad_tag_association = db.Table('ad_tag_association',
db.Column('ad_id', db.Integer, db.ForeignKey('ad.id'), primary_key=True),
db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

tag_cluster_association = \
    db.Table('tag_cluster_association',
        db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
        db.Column('cluster_id', db.Integer, db.ForeignKey('cluster.id'), primary_key=True)
    )
ad_cluster_association = db.Table('ad_cluster_association',
db.Column('ad_id', db.Integer, db.ForeignKey('ad.id'), primary_key=True),
db.Column('cluster_id', db.Integer, db.ForeignKey('cluster.id'), primary_key=True)
)
# </models.py>
