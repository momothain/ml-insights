from app.database import SessionLocal
from app.models.advertiser import Advertiser
import datetime

def test_create_advertiser():
    # Create a new session and add an advertiser
    session = SessionLocal()
    new_advertiser = Advertiser(
        created_at=datetime.datetime.now(),
        modified_at=datetime.datetime.now(),
        name="Test Advertiser",
        platform_name="Test Platform"
    )
    session.add(new_advertiser)
    session.commit()

    # Query the advertiser back and check its properties
    advertiser = session.query(Advertiser).filter_by(name="Test Advertiser").first()
    assert advertiser is not None
    assert advertiser.name == "Test Advertiser"
    assert advertiser.platform_name == "Test Platform"

    session.close()
