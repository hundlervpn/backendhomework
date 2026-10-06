from fastapi import Depends

from models.task import Task
from repositories.tasks import TaskRepository
from schemas.tasks import TaskIn, TaskUpdateIn


class TaskService:
    def __init__(self, repository: TaskRepository = Depends()):
        self.repository = repository

    def create_task(self, task: TaskIn) -> Task:
        return self.repository.create(task)

    def get_all_tasks(self) -> list[Task]:
        return self.repository.get_all()

    def get_task_by_id(self, task_id: int) -> Task | None:
        return self.repository.get_by_id(task_id)

    def update_task(self, task_id: int, upd_data: TaskUpdateIn) -> Task | None:
        db_task = self.repository.get_by_id(task_id)

        if db_task is None:
            return None

        upd_dict = upd_data.model_dump(exclude_none=True)

        return self.repository.update(db_task, upd_dict)

    def delete_task(self, task_id: int) -> Task | None:
        db_task = self.repository.get_by_id(task_id)

        if db_task is None:
            return None

        self.repository.delete(db_task)

        return db_task
