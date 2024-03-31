
from pydantic import BaseModel


class Project(BaseModel):
    name: str
    description: str
    dataset: str
    classifier: str
    is_archived: bool = False
