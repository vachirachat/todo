# todo/services.py
# Natawut Nupairoj
# Department of Computer Engineering, Chulalongkorn University
# Created for 2110415 Software Defined Systems

from typing import List
from fastapi import APIRouter, HTTPException
from todo.models import Todo
from todo.db import Database


db = Database.getInstance()
todo_services = APIRouter()


@todo_services.get('/', response_model=List[Todo])
async def search(q: str = '', t: str = '', c: str = ''):
    if c == '':
        completed = None
    else:
        if c == '0':
            completed = False
        else:
            completed = True
    tags = []
    if t != '':
        tags = t.split(sep=',')
    return db.search(q, tags, completed)


@todo_services.get('/{id}', response_model=Todo)
async def get_todo(id: int):
    todo = db.get(id)
    if todo is not None:
        return todo
    raise HTTPException(status_code=404, detail="Todo with given id not found")


@todo_services.post('/', status_code=201)
async def add_todo(payload: Todo):
    todo = payload.dict()
    id = db.add(todo)
    return {'id': id}


