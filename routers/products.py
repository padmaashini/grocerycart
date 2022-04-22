from tempfile import TemporaryFile
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/products/", response_model=schemas.Products)
async def create_product(product: schemas.ProductsCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)   