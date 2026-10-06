from fastapi import APIRouter, Depends, HTTPException

from schemas import TaskIn, TaskOut, TaskUpdateIn
from services.tasks import TaskService

router = APIRouter(tags=["tasks"])


@router.get("/tasks", status_code=200, response_model=list[TaskOut])
def get_tasks(service: TaskService = Depends()):
    return service.get_all_tasks()


@router.get("/tasks/{task_id}", status_code=200, response_model=TaskOut)
def get_task(task_id: int, service: TaskService = Depends()):
    task = service.get_task_by_id(task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found.")

    return task


@router.post("/tasks", status_code=201, response_model=TaskOut)
def create_task(task: TaskIn, service: TaskService = Depends()):
    return service.create_task(task)


@router.patch("/tasks/{task_id}", status_code=200, response_model=TaskOut)
def update_task(task_id: int, upd_data: TaskUpdateIn, service: TaskService = Depends()):
    task = service.update_task(task_id, upd_data)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found.")

    return task


@router.delete("/tasks/{task_id}", status_code=200)
def delete_task(task_id: int, service: TaskService = Depends()):
    deleted_task = service.delete_task(task_id)

    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found.")

    return {"message": f"Task {task_id} was deleted."}
