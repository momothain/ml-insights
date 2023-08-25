from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Advertiser(Base):
    __tablename__ = 'advertiser'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime, nullable=False)
    ad_id = Column(String(255))
    buisness_domain = Column(String(255))
    end_date = Column(DateTime)
    is_active = Column(Boolean)
    is_data_sync = Column(Boolean)
    name = Column(String(255), unique=True)
    platform_id = Column(Integer)
    platform_name = Column(String(255))
    start_date = Column(DateTime)
