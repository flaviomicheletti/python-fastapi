"""
https://fastapi.tiangolo.com/advanced/testing-dependencies/
"""

from typing import Union

from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

#
# pay attention
#
async def override_dependency(q: Union[str, None] = None):
    return {"q": q, "skip": 5, "limit": 10}


#
# pay attention
#
app.dependency_overrides[app.common_parameters] = override_dependency


def test_override_in_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello Items!",
        "params": {"q": None, "skip": 5, "limit": 10},
    }


def test_override_in_items_with_q():
    response = client.get("/items/?q=foo")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello Items!",
        "params": {"q": "foo", "skip": 5, "limit": 10},
    }


def test_override_in_items_with_params():
    response = client.get("/items/?q=foo&skip=100&limit=200")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello Items!",
        "params": {"q": "foo", "skip": 5, "limit": 10},
    }
