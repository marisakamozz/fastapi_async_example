import asyncio

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/health")
async def health():
    return JSONResponse(content=jsonable_encoder({"status": 200, "server": "sv2"}))


@app.post("/wait/{waittime}")
async def wait(waittime: int):
    await asyncio.sleep(waittime)
    return JSONResponse(content=jsonable_encoder({"status": 200, "server": "sv2", "waittime": waittime}))
