from fastapi import FastAPI
from src.api import products
from src.api.products import router as products_router

app = FastAPI()

app.include_router(products_router)
app = FastAPI(title="E-Commerce Product API")

app.include_router(products.router)


# Include product routes
app.include_router(products.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "E-Commerce ETL API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}