from typing import List, Optional
from pydantic import BaseModel, Field

class ProductsBase(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: int = Field(..., ge = 0, description="Quantity must be a positive integer")
    price: float = Field(..., gt=0.00, description="The price must be greater than zero")
    store: int

# for creating a new instance
class ProductsCreate(ProductsBase):
    pass

# for getting instances
class Products(ProductsBase):
    id: int

    class Config: 
        orm_mode = True
