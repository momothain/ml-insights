from sqlalchemy import Column, Integer, String, BigInteger, SmallInteger, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Media(Base):
    __tablename__ = 'media'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime, nullable=False)
    advertiser_id = Column(String(255))
    asset_identifier = Column(String(150))
    asset_url = Column(String(2048))
    asset_url_expired_at = Column(DateTime)
    is_processed = Column(Integer, default=0)
    media_id = Column(String(255))
    refreshed_at = Column(DateTime)
    thumbnail = Column(String(512))
    thumbnail_identifier = Column(String(150))
    thumbnil_refreshed_at = Column(DateTime)
    type = Column(SmallInteger)
    campaigns_id = Column(BigInteger, ForeignKey('campaigns.id'))
    ad_id = Column(BigInteger, ForeignKey('ad.id'))
    
    # Establish relationships
    campaigns = relationship("Campaign")
    ad = relationship("Ad")
