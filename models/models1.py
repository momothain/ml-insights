from flask_sqlalchemy import SQLAlchemy
from app import db

# store .mp4 together? = media URLs 
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    url = db.Column() # FIX ...
    backup_media = ...
    # Other video attributes...
    
    def __repr__(self):
        return f'<Video {self.id}>'

# 
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'))
    video = db.relationship('Video', backref='tags')
    category = # e.g. aggressivess, skin type
    
    def __repr__(self):
        return f'<Tag {self.id}>'
    
# class Summary()...


# representative examples. equivalence class representative 
class Cluster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    # Other cluster attributes...
    cluster_id = db.Column(db.Integer, db.ForeignKey('cluster.id'))
    cluster = db.relationship('Cluster', backref='tags')
    
    def __repr__(self):
        
        return f'<Cluster {self.id}>'
