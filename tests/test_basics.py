# <tests/test_models.py>
import pytest
from ml_insights.app.app import create_app
from ml_insights.models.models import *
from ml_insights.database import db as d

DATABASE = "test_local"

# Create a fixture for the app
@pytest.fixture(scope="module")
def test_app():
    app = create_app(env=DATABASE)
    with app.app_context():
        yield app


# Create a fixture for the database
@pytest.fixture(scope="module")
def db(test_app):
    d.create_all()
    yield d
    d.drop_all()


# Basic CRUD operations for the Tag model
def test_tag_crud(db):
    try:
        # start a new transaction
        db.session.begin()
        # Create
        tag = MlTag(
            ml_tag="TestTag", media_category="TestMedia", ml_tag_category_name="TestCategory"
        )
        db.session.add(tag)
        db.session.commit()

        # Read
        found_tag = MlTag.query.filter_by(ml_tag="TestTag").first()
        assert found_tag is not None

        # Update
        found_tag.tag = "UpdatedTestTag"
        db.session.commit()
        updated_tag = MlTag.query.filter_by(ml_tag="UpdatedTestTag").first()
        assert updated_tag is not None

        # Delete
        db.session.delete(updated_tag)
        db.session.commit()
        deleted_tag = MlTag.query.filter_by(ml_tag="UpdatedTestTag").first()
        assert deleted_tag is None
    except Exception as e:
        # rollback in case of any issues
        db.session.rollback()


# You can add similar CRUD tests for other models like TagCategory, Cluster, Ad
# ...


# Testing relationships
def test_tag_tagcategory_relationship(db):
    category = MlTagCategory(ml_tag_category="TestCategory")
    tag = MlTag(
        ml_tag="RelationshipTag",
        media_category="TestMedia",
        ml_tag_category_name="TestCategory",
    )

    db.session.add(category)
    db.session.add(tag)
    db.session.commit()

    found_tag = MlTag.query.filter_by(ml_tag="RelationshipTag").first()
    assert found_tag.ml_tag_category.ml_tag_category == "TestCategory"

    # Cleanup
    # db.session.delete(category)
    # db.session.delete(tag)
    db.session.commit()


# You can add similar relationship tests for other relationships
# ...
