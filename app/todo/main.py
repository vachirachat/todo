# app/todo/main.py
# Natawut Nupairoj
# Department of Computer Engineering, Chulalongkorn University
# Created for 2110415 Software Defined Systems

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.todo.services import todo_services


print('Init todo-service version 0.1.4')
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)
app.include_router(todo_services)