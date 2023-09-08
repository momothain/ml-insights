# <ml_audio.py>
from sqlalchemy import CheckConstraint
from ml_insights.database import db
from sqlalchemy.dialects.postgresql import ARRAY

# store .mp4 together? = media URLs
class MlVideo(db.Model):
    # __tablename__ = 'ml_audio'
    id = db.Column(db.Integer, primary_key=True)
    in_video_text = db.Column(db.ARRAY(db.String(1000)))
    duration = db.Column(db.Integer)
    key_frames = db.Column(db.Integer) #TODO: how store?


# TODO:
class MlAudioCategory(db.Model):
    __tablename__ = 'ml_audio_categories'
    audio_category = db.Column(db.String(100))
# TODO:
class MlAudioFeature(db.Model):
    __tablename__ = 'ml_audio_features'
    audio_category = db.Column(db.String(100))





    # ml_tag = db.Column(db.String(100), nullable=False)
    # start_time = db.Column(db.Float)
    # end_time = db.Column(db.Float)
    # shot_num = db.Column(db.Integer, nullable=False, default=1)
    # __table_args__ = (CheckConstraint('shot_num > 0', name='positive_shot_num'),)
    # ml_tag_category_name = db.Column(db.String(50), db.ForeignKey('ml_tag_categories.ml_tag_category'), nullable=False) # This is the foreign key for the relationship
    # ml_tag_category = db.relationship('MlTagCategory', back_populates='ml_tags') # New relationship field
    # # tag_category xw= db.Column(db.String(50), nullable=False)
    # media_category = db.Column(db.String(50), nullable=False)
    # num_ordinal_ranks = db.Column(db.Integer) # for low, med, high just show the number of ranks and we'll handle this as one-hots later
    # source_API = db.Column(db.String(50))
    # # Define the many-to-many relationship with Ad
    # ml_ads = db.relationship('MlAd', secondary='ml_ad_tag_association', back_populates='ml_tags')
    # ml_clusters = db.relationship('MlCluster', secondary='ml_tag_cluster_association', back_populates='ml_tags')
