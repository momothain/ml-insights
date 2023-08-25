from sqlalchemy import Column, Integer, String, BigInteger, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Campaigns(Base):
    __tablename__ = 'campaigns'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime, nullable=False)
    ad_content = Column(String(1024))
    ad_created_date = Column(String(30))
    ad_id = Column(String(255))
    ad_name = Column(String(255))
    ad_title = Column(String(512))
    ad_updated_date = Column(String(30))
    ad_url = Column(String(512))
    adset_id = Column(String(255))
    adset_name = Column(String(512))
    advertiser_id = Column(BigInteger, ForeignKey('advertiser.id'))
    campaign_id = Column(String(255), nullable=False)
    name = Column(String(512))
    platform_id = Column(BigInteger, ForeignKey('platform.id'))
    
    # Establish relationships
    advertiser = relationship("Advertiser")
    platform = relationship("Platform")
