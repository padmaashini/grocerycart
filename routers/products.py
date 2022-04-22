from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get("/")
def get_products():
    return 1



from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from ..core.crud import crud_products

from ..core.schemas import products

from ..sql_app import models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/products/", response_model=crud_products.Products)
async def create_product(product: crud_products.ProductsCreate, db: Session = Depends(get_db)):

    return crud_products.create_product(db=db, product=product)   