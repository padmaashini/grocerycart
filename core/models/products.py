from sqlalchemy import CheckConstraint, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from enum import Enum

from ..database import Base
from ..utils import categories

class Products(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String, default="")
    category = Column(Enum(categories.Categories), nullable=False)
    quantity = Column(Integer, CheckConstraint('quantity >= 0'), nullable=False)
    price = Column(Float, CheckConstraint('price > 0.00'), nullable=False)
    store_no = Column(Integer, ForeignKey("stores.store_id"), nullable=False)
    
    store = relationship("Stores", back_populates="products")
