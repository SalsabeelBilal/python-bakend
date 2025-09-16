from fastapi import FastAPI
from pydantic import BaseModel, validator
from typing import Literal

app = FastAPI()

class Product(BaseModel):
    name: str | None = None
    price: float
    category: Literal["Electronics", "Clothing", "Food", "Books"]

    # ---------------------------
    # Exercise: Custom Validator
    # ---------------------------
    @validator("price")
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Price must be greater than 0")
        return v


products_db = []


@app.post("/products/")
def create_product(product: Product):
    """Validate and store product"""
    products_db.append(product.dict())
    return {"message": "Product added successfully!", "product": product}