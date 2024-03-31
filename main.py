from typing import Union

from fastapi import FastAPI, APIRouter
from routes.api_v1 import api_v1

app = FastAPI()
app.mount("/api/v1", api_v1)


@app.get("/")
def read_root():
    return {"Hello": "World"}


# app.include_router(router, prefix="/api/v1", tags=["projects"])
