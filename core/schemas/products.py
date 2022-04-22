from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum

from ..utils.categories import Categories
class ProductsBase(BaseModel):
    name: str = Field(max_length=100)
    description: Optional[str] = None
    category: Categories
    quantity: int = Field(..., ge = 0, description="Quantity must be a positive integer")
    price: float = Field(..., gt=0.00, description="The price must be greater than zero")
    store: int

# for creating a new instance
class ProductsCreate(ProductsBase):
    pass

# for getting instances
class Products(ProductsBase):
    product_id: int

    class Config: 
        orm_mode = True
