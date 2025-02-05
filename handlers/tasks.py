from fastapi import APIRouter
from fixtures import tasks as fixture_tasks
from fixtures import categories as fixture_categories
from schema.task import Task

router = APIRouter(prefix='/tasks', tags=['tasks'])


@router.post('/', response_model=Task)
async def create_task(task: Task):
    fixture_tasks.append(task)
    return task


@router.put('/{task_id}', response_model=Task)
async def update_task(task_id: str, task: Task):
    pass


@router.get('/', response_model=list[Task])
async def get_tasks():
    return fixture_tasks


@router.get('/{task_id}')
async def get_task(task_id):
    return {'task_id': task_id}
