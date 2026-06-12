from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from fastapi import Query as query

app = FastAPI()

class Item(BaseModel):
    name : str
    price : float 
    brand : Optional[str] = None



inventory = {}

@app.get("/get-item/{item_id}")
def get_item(name: str = query(None, title="Name of the item", description="This is the name of the item you want to get")):
    if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Error": "Item not found"}

        

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}
    
    inventory[item_id] = item
    return inventory[item_id]


@app.update("/update-item/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        return {"Error": "Item ID does not exist"}
    


    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]

@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    if item_id not in inventory:
        return {"Error": "Item ID does not exist"}
    
    del inventory[item_id]
    return {"Success": "Item deleted successfully"}




