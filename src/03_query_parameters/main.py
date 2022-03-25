from fastapi import FastAPI
import uvicorn

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
]


@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# optional parameters
@app.get("/items2/{item_id}")
async def read_item2(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# Query parameter type conversion
@app.get("/items3/{item_id}")
async def read_item3(item_id: str, q: str | None = None, short: bool = False):
    description = "This is an amazing item that has a long description"
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": description})
    return item


# Multiple path and query parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int,
    item_id: str,
    q: str | None = None,
    short: bool = False,
):
    description = "This is an amazing item that has a long description"
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": description})
    return item


# Required query parameters
@app.get("/items4/{item_id}")
async def read_user_item2(
    item_id: str,
    needy: str,
):
    item = {"item_id": item_id, "needy": needy}
    return item


if __name__ == "__main__":
    uvicorn.run(
        "src.03_query_parameters.main:app",
        reload=True,
    )
