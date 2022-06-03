import requests
import aiohttp

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/health")
def health():
    return JSONResponse(content=jsonable_encoder({"status": 200, "server": "sv1"}))


@app.get("/sv2/health")
def sv2_health():
    response = requests.get("http://sv2:8000/health")
    return JSONResponse(content=jsonable_encoder(response.json()))


@app.post("/sv2/wait/{waittime}")
async def sv2_wait(waittime: int):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"http://sv2:8000/wait/{waittime}") as resp:
            response_json = await resp.json()
    return JSONResponse(content=jsonable_encoder(response_json))


@app.post("/sv2/block/{waittime}")
def sv2_block(waittime: int):
    response = requests.post(f"http://sv2:8000/block/{waittime}")
    return JSONResponse(content=jsonable_encoder(response.json()))
