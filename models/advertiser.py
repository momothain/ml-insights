from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, BigInteger
from your_sqlalchemy_setup_module import db  # Import your SQLAlchemy db object here


class Advertiser(db.Model):
    __tablename__ = "advertiser"

    id = Column(BigInteger, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    modified_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    ad_id = Column(String(255))
    business_domain = Column(String(255))
    end_date = Column(DateTime)
    is_active = Column(Boolean)
    is_data_sync = Column(Boolean)
    name = Column(String(255))
    platform_id = Column(BigInteger)
    platform_name = Column(String(255))
    start_date = Column(DateTime)
