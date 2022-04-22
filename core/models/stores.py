from sqlalchemy import Boolean, CheckConstraint, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

class Stores(Base):
    __tablename__ = "stores"

    store_id = Column(Integer, primary_key=True, index=True)
    store_no = Column(Integer, CheckConstraint('store_no > 0'), unique=True, nullable=False)
    location = Column(String(200), nullable=False)

    products = relationship("Products", back_populates="owners")