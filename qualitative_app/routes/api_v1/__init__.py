from fastapi import FastAPI

from .projects import projects_router

api_v1 = FastAPI()
api_v1.include_router(projects_router)
