from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class TaskIn(BaseModel):
    title: str
    priority: int = Field(default=3, ge=1, le=5)


class TaskUpdateIn(BaseModel):
    title: Optional[str] = None
    priority: Optional[int] = Field(default=None, ge=1, le=5)


class TaskOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    priority: int
