from sqlalchemy import CheckConstraint, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from enum import Enum

from ..database import Base

class Categories(Enum):
    BEVERAGES: "BEVERAGES"
    FROZEN_FOODS: "FROZEN_FOODS"
    BAKERY: "BAKERY"
    DAIRY: "DAIRY"
    MEAT: "MEAT"
    PRODUCE: "PRODUCE"
    PAPER_GOODS: "PAPER_GOODS"
    PERSONAL_CARE: "PERSONAL_CARE"
    OTHER: "OTHER"

class Products(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=False)
    description = Column(String, default="")
    category = Column(Enum(Categories), nullable=False)
    quantity = Column(Integer, CheckConstraint('quantity >= 0'), nullable=False)
    price = Column(Float, CheckConstraint('price > 0.00'), nullable=False)
    store_no = Column(Integer, ForeignKey("stores.store_id"), nullable=False)
    
    store = relationship("Stores", back_populates="products")
