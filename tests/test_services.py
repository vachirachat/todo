# test/test_services.py
# Natawut Nupairoj
# Department of Computer Engineering, Chulalongkorn University
# Created for 2110415 Software Defined Systems
import logging
import os
import sys

import pytest
from xprocess import ProcessStarter

from datetime import datetime
import requests


# global process variable
service_url = 'http://localhost:8000/'


def test_connectivity(server):
    resp = requests.get(service_url)
    assert resp.status_code == 200


@pytest.mark.skip(reason="no way of currently testing this")
def test_post_and_get():
    resp = requests.get(service_url)
    existing = len(resp.json())

    tags = ['basic', 'high-priority', 'main']
    n = 3
    for i in range(n):
        title = 'todo#{}'.format(i)
        todo = {
            'title': title,
            'detail': 'this is the details for ' + title,
            'duedate': str(datetime.now()),
            'tags': tags[:i],
            'completed': i%2 == 0
        }
        resp = requests.post(service_url, json=todo)
        assert resp.status_code == 201
        assert resp.json()['id'] == (existing + i)

    resp = requests.get(service_url)
    assert resp.status_code == 200
    assert len(resp.json()) == (existing + n)


@pytest.fixture(scope='session')
def logger():
    log = logging.getLogger(__name__)
    return log


@pytest.fixture(autouse=True, scope='session')
def server(xprocess, logger):
    python_executable_full_path = sys.executable
    base_path = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_path, 'todo')
    logger.debug('using app path: ' + app_path)

    class Starter(ProcessStarter):
        pattern = 'startup complete'
        arg_str = '-m uvicorn main:app --app-dir {} --host=0.0.0.0 --port=8000'.format(app_path)
        args = [python_executable_full_path] + arg_str.split()

    logfile = xprocess.ensure('server', Starter)
    yield
    xprocess.getinfo("server").terminate()
