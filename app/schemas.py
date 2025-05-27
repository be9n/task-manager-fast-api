from pydantic import BaseModel
from typing import Optional, Any, List, Dict, Generic, TypeVar

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

T = TypeVar('T')

class StandardResponse(BaseModel, Generic[T]):
    data: Optional[T] = None
    message: str = "Success"
    status_code: int = 200
    success: bool = True
    errors: Optional[List[Dict[str, Any]]] = None 