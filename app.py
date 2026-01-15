
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI(title="Clean Microservice Demo")

class Item(BaseModel):
    name: str
    description: Optional[str] = None

db: Dict[int, Item] = {}
counter = 1

@app.get("/")
def root():
    return {"status": "running", "service": "clean-microservice"}

@app.post("/items")
def create_item(item: Item):
    global counter
    db[counter] = item
    counter += 1
    return {"id": counter - 1, "item": item}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]
    return {"status": "deleted"}

@app.get("/health")
def health():
    return {"status": "ok"}