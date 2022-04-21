from fastapi import FastAPI, Path
from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: int = Field(..., ge = 0, description="Quantity must be a positive integer")
    price: float = Field(..., gt=0.00, description="The price must be greater than zero")
    store: int

app = FastAPI()

@app.get("/products")
async def get_products():
    return {"message": "Hello World"}


@app.get("/products/{product_id}")
async def get_product(product_id: int = Path(..., title="The ID of the product to get", ge=1)):
    return {"message": product_id}

@app.post("/products/")
async def create_product(product: Product):
    return product

@app.put("/products/{product_id}")
async def update_product(
    *, 
    product_id: int = Path(..., title="The ID of the product to get", ge=1), 
    product: Product
):
    return product