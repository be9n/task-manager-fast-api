from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app import crud, models, schemas, database
from typing import List

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tasks/", response_model=schemas.StandardResponse[schemas.Task])
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = crud.create_task(db=db, task=task)
    response = schemas.StandardResponse(
        data=db_task,
        message="Task created successfully",
        status_code=201
    )
    return response

@router.get("/tasks/", response_model=schemas.StandardResponse[List[schemas.Task]])
def get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db=db, skip=skip, limit=limit)
    return schemas.StandardResponse(
        data=tasks,
        message="Tasks retrieved successfully"
    )

@router.get("/tasks/{task_id}", response_model=schemas.StandardResponse[schemas.Task])
def get_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db=db, task_id=task_id)
    if db_task is None:
        return schemas.StandardResponse(
            data=None,
            message="Task not found",
            status_code=404,
            success=False,
            errors=[{"detail": "Task not found"}]
        )
    
    return schemas.StandardResponse(
        data=db_task,
        message="Task retrieved successfully"
    )

@router.put("/tasks/{task_id}", response_model=schemas.StandardResponse[schemas.Task])
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = crud.update_task(db=db, task_id=task_id, task_update=task)
    if db_task is None:
        return schemas.StandardResponse(
            data=None,
            message="Task not found",
            status_code=404,
            success=False,
            errors=[{"detail": "Task not found"}]
        )
    
    return schemas.StandardResponse(
        data=db_task,
        message="Task updated successfully"
    )

@router.delete("/tasks/{task_id}", response_model=schemas.StandardResponse[schemas.Task])
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.delete_task(db=db, task_id=task_id)
    if db_task is None:
        return schemas.StandardResponse(
            data=None,
            message="Task not found",
            status_code=404,
            success=False,
            errors=[{"detail": "Task not found"}]
        )
    
    return schemas.StandardResponse(
        data=db_task,
        message="Task deleted successfully"
    )

@router.patch("/tasks/{task_id}/done", response_model=schemas.StandardResponse[schemas.Task])
def mark_task_done(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        return schemas.StandardResponse(
            data=None,
            message="Task not found",
            status_code=404,
            success=False,
            errors=[{"detail": "Task not found"}]
        )
    
    task.is_done = True
    db.commit()
    db.refresh(task)
    
    return schemas.StandardResponse(
        data=task,
        message="Task marked as done"
    )
