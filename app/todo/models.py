# app/todo/models.py
# Natawut Nupairoj
# Department of Computer Engineering, Chulalongkorn University
# Created for 2110415 Software Defined Systems

from typing import List
from datetime import datetime
from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    detail: str
    duedate: datetime
    tags: List[str]
