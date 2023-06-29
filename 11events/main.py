from fastapi import FastAPI

app = FastAPI()

items = {}


@app.on_event("startup")
async def startup_event():
    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}


@app.on_event("shutdown")
def shutdown_event():
    with open("log.txt", mode="a") as log:
        log.write("Application shutdown")


@app.get("/items/")
async def read_all_items():
    return items


@app.get("/items/{item_id}")
async def read_items(item_id: str):
    return items[item_id]



"""
https://fastapi.tiangolo.com/advanced/events/#events-startup-shutdown
"""