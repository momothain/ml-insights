# <models.py>
from sqlalchemy import CheckConstraint
from ml_insights.database import db

# store .mp4 together? = media URLs
class MlTag(db.Model):
    __tablename__ = 'ml_tags'  # Using a pluralized table name
    id = db.Column(db.Integer, primary_key=True)
    ml_tag = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.Float)
    end_time = db.Column(db.Float)
    shot_num = db.Column(db.Integer, nullable=False, default=1)
    __table_args__ = (CheckConstraint('shot_num > 0', name='positive_shot_num'),)
    ml_tag_category_name = db.Column(db.String(50), db.ForeignKey('ml_tag_categories.ml_tag_category'), nullable=False) # This is the foreign key for the relationship
    ml_tag_category = db.relationship('MlTagCategory', back_populates='ml_tags') # New relationship field
    # tag_category xw= db.Column(db.String(50), nullable=False)
    media_category = db.Column(db.String(50), nullable=False)
    num_ordinal_ranks = db.Column(db.Integer) # for low, med, high just show the number of ranks and we'll handle this as one-hots later
    source_API = db.Column(db.String(50))
    # Define the many-to-many relationship with Ad
    ml_ads = db.relationship('MlAd', secondary='ml_ad_tag_association', back_populates='ml_tags')
    ml_clusters = db.relationship('MlCluster', secondary='ml_tag_cluster_association', back_populates='ml_tags')

class MlTagCategory(db.Model):
    __tablename__ = 'ml_tag_categories'
    id = db.Column(db.Integer, primary_key=True)
    ml_tag_category = db.Column(db.String(50), nullable=False, unique=True)
    ml_tags = db.relationship('MlTag', back_populates='ml_tag_category', cascade="all, delete-orphan")

class MlCluster(db.Model):
    __tablename__ = 'ml_clusters'
    id = db.Column(db.Integer, primary_key=True)
    ml_tag = db.Column(db.String(100), nullable=False)
    ml_ads = db.relationship('MlAd', secondary='ml_ad_cluster_association', back_populates='ml_clusters')
    ml_tags = db.relationship('MlTag', secondary='ml_tag_cluster_association', back_populates='ml_clusters')

class MlAd(db.Model):
    __tablename__ = 'ml_ads'
    id = db.Column(db.Integer, primary_key=True)
    # Define the many-to-many relationship with MLDataSpecsTag
    ml_tags = db.relationship('MlTag', secondary='ml_ad_tag_association', back_populates='ml_ads')
    ml_clusters = db.relationship('MlCluster', secondary='ml_ad_cluster_association', back_populates='ml_ads')

ml_ad_tag_association = db.Table('ml_ad_tag_association',
                                 db.Column('ml_ad_id', db.Integer, db.ForeignKey('ml_ads.id'), primary_key=True),
                                 db.Column('ml_tag_id', db.Integer, db.ForeignKey('ml_tags.id'), primary_key=True)
                                 )

ml_tag_cluster_association = \
    db.Table('ml_tag_cluster_association',
        db.Column('ml_tag_id', db.Integer, db.ForeignKey('ml_tags.id'), primary_key=True),
        db.Column('ml_cluster_id', db.Integer, db.ForeignKey('ml_clusters.id'), primary_key=True)
    )
ml_ad_cluster_association = db.Table('ml_ad_cluster_association',
                                     db.Column('ml_ad_id', db.Integer, db.ForeignKey('ml_ads.id'), primary_key=True),
                                     db.Column('ml_cluster_id', db.Integer, db.ForeignKey('ml_clusters.id'), primary_key=True)
                                     )
# </models.py>
