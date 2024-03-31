from fastapi import FastAPI
from qualitative_app.routes.api_v1 import api_v1

app = FastAPI()
app.mount("/api/v1", api_v1)


@app.get("/")
def read_root():
    return {"Hello": "World"}
