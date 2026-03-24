"""
FastAPI REST API Starter Code

This file provides a basic structure for building a REST API with FastAPI.
Complete the tasks by implementing the endpoints and models below.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Assignment API")

# =====================================================================
# TASK 1: DONE - Basic setup is complete!
# The FastAPI app is initialized and the welcome endpoint is ready.
# Run this file with: uvicorn starter-code:app --reload
# =====================================================================

@app.get("/")
def welcome():
    """Welcome endpoint to verify the server is running."""
    return {
        "message": "Welcome to the FastAPI Assignment!",
        "instructions": "Implement the CRUD endpoints for Task 2 and error handling for Task 3"
    }


# =====================================================================
# TASK 2: Implement CRUD Endpoints
# TODO: Define a Pydantic model for your resource (e.g., Item, Task, Book)
# =====================================================================

# Example model - replace with your own resource
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: Optional[float] = None


# TODO: Create an in-memory storage (could be a list or dictionary)
# Example: items_db = []

items_db = []
next_id = 1


# TODO: Implement GET /items - retrieve all items
@app.get("/items", response_model=List[Item])
def get_all_items():
    """Retrieve all items."""
    # IMPLEMENT THIS
    pass


# TODO: Implement GET /items/{item_id} - retrieve a single item
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    """Retrieve a specific item by ID."""
    # IMPLEMENT THIS - Handle case where item doesn't exist (Task 3)
    pass


# TODO: Implement POST /items - create a new item
@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    """Create a new item."""
    # IMPLEMENT THIS
    pass


# TODO: Implement PUT /items/{item_id} - update an item
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    """Update an existing item."""
    # IMPLEMENT THIS - Handle case where item doesn't exist (Task 3)
    pass


# TODO: Implement DELETE /items/{item_id} - delete an item
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    """Delete an item by ID."""
    # IMPLEMENT THIS - Handle case where item doesn't exist (Task 3)
    pass


# =====================================================================
# TASK 3: Error Handling and Validation
# The Pydantic models above handle request body validation automatically.
# Use HTTPException in your endpoint implementations to return proper
# error responses (400, 404, 500, etc.)
# =====================================================================
