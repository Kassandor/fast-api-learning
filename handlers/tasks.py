from fastapi import APIRouter

router = APIRouter(prefix='/tasks', tags=['tasks'])


@router.post('/')
async def create_task():
    return {'message': 'ok 200'}


@router.get('/')
async def get_tasks():
    return {'message': 'ok 200'}


@router.get('/{task_id}')
async def get_task(task_id):
    return {'task_id': task_id}
