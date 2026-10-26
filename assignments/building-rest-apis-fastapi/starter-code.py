from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Task API")
tasks: list[dict] = []
next_task_id = 1


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str
    completed: bool = False


@app.get("/")
def read_root():
    return {"message": "Task API is running"}


@app.get("/tasks")
def list_tasks():
    return tasks


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    raise NotImplementedError("Complete Task 2")


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    raise NotImplementedError("Complete Task 2")


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    raise NotImplementedError("Complete Task 3")


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    raise NotImplementedError("Complete Task 3")
