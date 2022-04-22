from fastapi import FastAPI

from .routers import products, stores

app = FastAPI()

app.include_router(products.router)
app.include_router(stores.router)

@app.get("/")
async def root(): 
    return {"message": "Welcome to GroceryCart Backend Application!"}