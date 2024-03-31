from typing import Union

from fastapi import APIRouter
from qualitative_app.models.project import Project

projects_router = APIRouter(prefix="/projects", tags=["Projects"])


@projects_router.get("/")
def index_projects():
    return {"message": "Projects Index"}


@projects_router.get("/{project_id}")
def read_project(project_id: int, q: Union[str, None] = None):
    return {"project_id": project_id, "q": q}


@projects_router.post("/create")
def create_project(project_id: int, project: Project):
    return {"project_id": project_id, "project": project}


@projects_router.put("/{project_id}")
def update_project(project_id: int, project: Project):
    return {"project_id": project_id, "project": project}


@projects_router.delete("/{project_id}")
def delete_project(project_id: int):
    return {"project_id": project_id}
