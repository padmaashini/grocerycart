from sqlalchemy.orm import Session

from ..models.products import Products
from ..schemas.products import ProductsCreate

from ..utils.categories import Categories

def get_products(db: Session):
    return db.query(Products).first()

def get_product_by_id(db: Session, product_id: int):
    return db.query(Products).filter(Products.product_id == product_id).first()

def get_products_by_category(db: Session, category: Categories):
    return db.query(Products).filter(Products.category == category).first()

def get_products_by_name(db: Session, name: str):
    return db.query(Products).filter(Products.name == name).first()

def get_products_by_store_no(db: Session, store_no: int): 
    return db.query(Products).filter(Products.store_no == store_no).first()

def create_product(db: Session, product: ProductsCreate):
    db_item = Products(**product.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
