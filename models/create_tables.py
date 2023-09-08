# <create_tables.py>

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys
sys.path.append("..")
from models.models import MlTag, MlTagCategory, MlCluster, MlAd
from database import db
from config import configurations


app = Flask(__name__)
app.config.from_object(configurations['test'])

# db = SQLAlchemy()
db.init_app(app)

with app.app_context():
    db.create_all()

    # Now, we insert some sample data:

    # Create a tag category:
    tag_category_1 = MlTagCategory(ml_tag_category="Example Category 1")

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

# </create_tables.py>

