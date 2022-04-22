from pydantic import BaseModel, Field

class StoresBase(BaseModel):
    store_no: int = Field(..., gt=0, description="Store number must be greater than 0")
    location: str = Field(max_length=200, description="Location must be no longer than 200 characters")

class StoresCreate(StoresBase): 
    pass

class Stores(StoresBase):
    store_id: int

    class Config:
        orm_mode = True
