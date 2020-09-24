# app/todo/main.py
# Natawut Nupairoj
# Department of Computer Engineering, Chulalongkorn University
# Created for 2110415 Software Defined Systems

from fastapi import FastAPI
from app.todo.services import todo_services


app = FastAPI()
app.include_router(todo_services)