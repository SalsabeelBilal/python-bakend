from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# Fake in-memory "database"
items_db = {
    1: {"name": "Laptop", "price": 1200, "category": "Electronics"},
    2: {"name": "Book", "price": 20, "category": "Education"},
    3: {"name": "Headphones", "price": 100, "category": "Electronics"},
}

posts_db = {
    1: [
        {"id": 1, "title": "First Post", "status": "published"},
        {"id": 2, "title": "Draft Post", "status": "draft"},
    ],
    2: [
        {"id": 3, "title": "Another Post", "status": "published"},
    ],
}

# Pydantic model for item creation
class Item(BaseModel):
    name: str
    price: float
    category: str


# ---------------------------
# Hands-on
# ---------------------------

@app.get("/items/{item_id}")
def get_item(item_id: int, category: Optional[str] = Query(None)):
    """Fetch an item by ID and optionally filter by category"""
    item = items_db.get(item_id)
    if not item:
        return {"error": "Item not found"}
    if category and item["category"].lower() != category.lower():
        return {"error": f"Item found but does not match category '{category}'"}
    return item


@app.post("/items/")
def create_item(item: Item):
    """Create a new item using request body"""
    new_id = max(items_db.keys()) + 1
    items_db[new_id] = item.dict()
    return {"id": new_id, "item": items_db[new_id]}


# ---------------------------
# Exercise
# ---------------------------

@app.get("/users/{user_id}/posts")
def get_user_posts(user_id: int, status: Optional[str] = Query(None)):
    """Return posts by a user, optionally filtered by status"""
    user_posts = posts_db.get(user_id, [])
    if status:
        user_posts = [post for post in user_posts if post["status"] == status.lower()]
    return {"user_id": user_id, "posts": user_posts}
