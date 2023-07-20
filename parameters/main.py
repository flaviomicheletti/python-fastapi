from fastapi import FastAPI
from models import Item

app = FastAPI()

#
# Path parameters
#
@app.get("/path/{item}")
async def myfunction1(item):
    return {"item": f"{item}"}

#
# Query parameters
#
@app.get("/query/{item}")
async def myfunction2(item, skip: int = 0, limit: int = 10):
    return {"item": f"{item}", "skip": f"{skip}", "limit": f"{limit}"}

#
# Request Body
#
@app.post("/models/")
async def myfunction3(item: Item):
    item_dict = item.dict()
    return item_dict

