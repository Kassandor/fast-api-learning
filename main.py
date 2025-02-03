import asyncio
import time

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Person(BaseModel):
    name: str
    age: int


@app.get("/person", response_model=Person)
def read_person():
    return Person(name="Alexander", age=27)


@app.post("/person", response_model=Person)
def create_person(person: Person):
    return Person(name=person.name, age=person.age)


async def get_users():
    await asyncio.sleep(3.0)


async def get_wiki():
    await asyncio.sleep(3.0)


@app.get('/test_async')
async def test_async():
    start_time = time.time()
    await asyncio.gather(get_users(), get_wiki())
    return f'time is {time.time() - start_time}'
