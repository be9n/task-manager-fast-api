from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: str
    description: Optional[str] = None
    is_done: bool

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_done: bool

    model_config = {
        "from_attributes": True 
    } 