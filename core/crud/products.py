from sqlalchemy.orm import Session
from . import models, schemas

def get_products_by_id(db: Session, product_id: int):
    return db.query(models.Products).filter(models.Products.id == product_id).first()

def create_product(db: Session, product: schemas.ProductsCreate):
    # db_item = models.Products(**product.dict())
    db_item = models.Products(description=product.description, name=product.name, quantity=product.quantity, price=product.price, store=product.store)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
