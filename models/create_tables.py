# import logging
#
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys
sys.path.append("..")

# Import the models to make sure SQLAlchemy knows about them
# import models.models
# import models.visual_models
# import models.audio_models
from models.models import *
# from models.audio_models import *
# from models.visual_models import *

from database import db
from config import configurations

app = Flask(__name__)
app.config.from_object(configurations['test'])

db.init_app(app)

def p():
    # Create a tag category:
    tag_category_1 = MlTagCategory(ml_tag_category="Example22 Category 1")

    # Create tags:
    tag_1 = MlTag(ml_tag="Sample Tag 1", ml_tag_category=tag_category_1, media_category="Media1", source_API="API1", shot_num=1)
    tag_2 = MlTag(ml_tag="Sample Tag 2", ml_tag_category=tag_category_1, media_category="Media2", source_API="API2", shot_num=2)

    # Create an Ad:
    ad_1 = MlAd()
    ad_1.ml_tags.append(tag_1)
    ad_1.ml_tags.append(tag_2)

    # Create a cluster:
    cluster_1 = MlCluster(ml_tag="Sample Cluster 1")
    cluster_1.ml_tags.append(tag_1)
    cluster_1.ml_ads.append(ad_1)

    # Add the created objects to the session and commit:
    db.session.add(tag_category_1)
    db.session.add(tag_1)
    db.session.add(tag_2)
    db.session.add(ad_1)
    db.session.add(cluster_1)
    db.session.commit()


with app.app_context():
    db.create_all()
    db.session.commit()
    # p()
# </create_tables.py>