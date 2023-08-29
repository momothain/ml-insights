# <tests/test_models.py>
import pytest
from app import create_app
from models.models import db, Tag, TagCategory, Cluster, Ad

# Create a fixture for the app
@pytest.fixture(scope='module')
def test_app():
    app = create_app(env='test')
    with app.app_context():
        yield app

# Create a fixture for the database
@pytest.fixture(scope='module')
def test_database(test_app):
    db.create_all()
    yield db
    db.drop_all()

# Basic CRUD operations for the Tag model
def test_tag_crud(test_database):
    # Create
    tag = Tag(tag="TestTag", media_category="TestMedia", tag_category_name="TestCategory")
    test_database.session.add(tag)
    test_database.session.commit()

    # Read
    found_tag = Tag.query.filter_by(tag="TestTag").first()
    assert found_tag is not None

    # Update
    found_tag.tag = "UpdatedTestTag"
    test_database.session.commit()
    updated_tag = Tag.query.filter_by(tag="UpdatedTestTag").first()
    assert updated_tag is not None

    # Delete
    test_database.session.delete(updated_tag)
    test_database.session.commit()
    deleted_tag = Tag.query.filter_by(tag="UpdatedTestTag").first()
    assert deleted_tag is None

# You can add similar CRUD tests for other models like TagCategory, Cluster, Ad
# ...

# Testing relationships
def test_tag_tagcategory_relationship(test_database):
    category = TagCategory(tag_category="TestCategory")
    tag = Tag(tag="RelationshipTag", media_category="TestMedia", tag_category_name="TestCategory")

    test_database.session.add(category)
    test_database.session.add(tag)
    test_database.session.commit()

    found_tag = Tag.query.filter_by(tag="RelationshipTag").first()
    assert found_tag.tag_category.tag_category == "TestCategory"

    # Cleanup
    test_database.session.delete(tag)
    test_database.session.delete(category)
    test_database.session.commit()

# You can add similar relationship tests for other relationships
# ...
