# <ml_audio.py>
import sys
sys.path.append("..")
from database import db
from sqlalchemy.dialects.postgresql import ARRAY

# store .mp4 together? = media URLs
class MlAudio(db.Model):
    # __tablename__ = 'ml_audio'
    id = db.Column(db.Integer, primary_key=True)
    audio_categories = db.Column(ARRAY(db.String(100))) #Consider restructuring
    transcript = db.Column(db.String(1000))
    title = db.Column(db.String(100))
    artist = db.Column(db.String(100))
    spotify_features = db.Column(db.ARRAY(db.String(100))) #TODO: DEFINITELY restructure
    # audio_data = #.mp4 foreign key? #keep?


# TODO:
class MlAudioCategory(db.Model):
    __tablename__ = 'ml_audio_categories'
    audio_category = db.Column(db.String(100))
# TODO:
class MlAudioFeature(db.Model):
    __tablename__ = 'ml_audio_features'
    audio_category = db.Column(db.String(100))