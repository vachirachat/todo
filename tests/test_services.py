# test/test_services.py
# Natawut Nupairoj
# Department of Computer Engineering, Chulalongkorn University
# Created for 2110415 Software Defined Systems
from datetime import datetime
import requests

service_url = 'http://localhost:8000/'


def test_connectivity():
    resp = requests.get(service_url)
    assert resp.status_code == 200


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

