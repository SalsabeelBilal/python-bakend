from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator

app = FastAPI()

# --- Product Model with Validation ---
class Product(BaseModel):
    name: str
    price: float
    category: str

    @validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        return value


# Fake in-memory "database"
products = {}


# --- POST: Create a Product ---
@app.post("/products/")
def create_product(product: Product):
    product_id = len(products) + 1
    products[product_id] = product
    return {"success": True, "message": "Product created successfully!", "id": product_id}


# --- GET: Fetch Product by ID ---
@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"success": True, "product": products[product_id]}


# --- GET: List All Products ---
@app.get("/products/")
def list_products():
    return {"success": True, "products": products}