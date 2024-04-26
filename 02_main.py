
from fastapi import FastAPI, Query, Depends, Form

app = FastAPI()

async def common_param(p: str | None = None, q: int = 0, rr: int = 10):
    return {"p": p, "q": q, "rr": rr}

@app.get("/items_10")
async def read_items(data: dict = Depends(common_param)):
    return data

@app.get("/items_11")
async def read_items(p: str = Query(None), q: int = Query(0), r: int = Query(10), data: dict = Depends(common_param)):
    # http://127.0.0.1:8000/items_11?p=%22asas%22&q=458
    return data

@app.get("/items_12")
async def read_items(p: str | None = None, q: int = 0, r: int = 10):
    # http://127.0.0.1:8000/items_11?p=%22asas%22&q=458
    data = await common_param(p,q,r)
    return data