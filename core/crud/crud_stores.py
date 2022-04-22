from sqlalchemy.orm import Session

from ..models.stores import Stores
from ..schemas.stores import StoresCreate

def get_stores(db: Session):
    return db.query(Stores).first()

def get_store_by_no(db: Session, store_no: int):
    return db.query(Stores).filter(Stores.store_no == store_no).first()

def create_store(db: Session, store: StoresCreate):
    db_item = Stores(**store.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
