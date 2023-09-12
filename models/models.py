# <models.py>
from sqlalchemy import CheckConstraint
import sys
from ml_insights.database import db

class MlTag(db.Model):
    """ Represents a specific ML tag with associated metadata. """
    __tablename__ = 'ml_tags'
    id = db.Column(db.Integer, primary_key=True)
    ml_tag = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.Float)
    end_time = db.Column(db.Float)
    shot_num = db.Column(db.Integer, nullable=False, default=1)
    __table_args__ = (CheckConstraint('shot_num > 0', name='positive_shot_num'),)

    # ForeignKey for the relationship with MlTagCategory
    ml_tag_category_name = db.Column(db.String(50), db.ForeignKey('ml_tag_categories.ml_tag_category'), nullable=False)
    ml_tag_category = db.relationship('MlTagCategory', back_populates='ml_tags')

    media_category = db.Column(db.String(50), nullable=False)
    num_ordinal_ranks = db.Column(db.Integer)  # Handles ranks as one-hots externally
    source_API = db.Column(db.String(50))

    # Many-to-many relationships
    ml_ads = db.relationship('MlAd', secondary='ml_ads_tags_associations', back_populates='ml_tags')
    ml_clusters = db.relationship('MlCluster', secondary='ml_tags_clusters_associations', back_populates='ml_tags')

class MlTagCategory(db.Model):
    """ Represents categories for ML tags. """
    __tablename__ = 'ml_tag_categories'
    id = db.Column(db.Integer, primary_key=True)
    ml_tag_category = db.Column(db.String(50), nullable=False, unique=True)
    ml_tags = db.relationship('MlTag', back_populates='ml_tag_category', cascade="all, delete-orphan")

class MlCluster(db.Model):
    """ Represents a cluster of ML tags. """
    __tablename__ = 'ml_clusters'
    id = db.Column(db.Integer, primary_key=True)
    ml_tag = db.Column(db.String(100), nullable=False)

    # Many-to-many relationships
    ml_ads = db.relationship('MlAd', secondary='ml_ads_clusters_associations', back_populates='ml_clusters')
    ml_tags = db.relationship('MlTag', secondary='ml_tags_clusters_associations', back_populates='ml_clusters')

class MlAd(db.Model):
    """ Represents an advertisement linked with ML tags and clusters. """
    __tablename__ = 'ml_ads'
    id = db.Column(db.Integer, primary_key=True)

    # Many-to-many relationships
    ml_tags = db.relationship('MlTag', secondary='ml_ads_tags_associations', back_populates='ml_ads')
    ml_clusters = db.relationship('MlCluster', secondary='ml_ads_clusters_associations', back_populates='ml_ads')

# Association tables for many-to-many relationships
ml_ads_tags_associations = db.Table('ml_ads_tags_associations',
                                    db.Column('ml_ad_id', db.Integer, db.ForeignKey('ml_ads.id'), primary_key=True),
                                    db.Column('ml_tag_id', db.Integer, db.ForeignKey('ml_tags.id'), primary_key=True)
                                    )

ml_tags_clusters_associations = \
    db.Table('ml_tags_clusters_associations',
             db.Column('ml_tag_id', db.Integer, db.ForeignKey('ml_tags.id'), primary_key=True),
             db.Column('ml_cluster_id', db.Integer, db.ForeignKey('ml_clusters.id'), primary_key=True)
             )

ml_ads_clusters_associations = db.Table('ml_ads_clusters_associations',
                                        db.Column('ml_ad_id', db.Integer, db.ForeignKey('ml_ads.id'), primary_key=True),
                                        db.Column('ml_cluster_id', db.Integer, db.ForeignKey('ml_clusters.id'), primary_key=True)
                                        )
# </models.py>
