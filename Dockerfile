FROM python:3.7-buster

WORKDIR /root
COPY . /root/todo
WORKDIR /root/todo

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 8000
CMD  python -m uvicorn --host=0.0.0.0 --port=8000 --reload app.todo.main:app

