from pydantic import BaseModel
from typing import Optional

# Request data (for creating a task)
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

# Response data (for returning a task)
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

    model_config = {
        "from_attributes": True  # same as `orm_mode = True` in v1
    } # Tells Pydantic to work with SQLAlchemy models