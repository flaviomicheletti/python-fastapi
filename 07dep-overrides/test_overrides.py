"""
https://fastapi.tiangolo.com/advanced/testing-dependencies/
"""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_override_in_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello Items!",
        "params": {"q": None, "skip": 0, "limit": 100},
    }


def test_override_in_items_with_q():
    response = client.get("/items/?q=foo")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello Items!",
        "params": {"q": "foo", "skip": 0, "limit": 100},
    }


def test_override_in_items_with_params():
    response = client.get("/items/?q=foo&skip=100&limit=200")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello Items!",
        "params": {"q": "foo", "skip": 100, "limit": 200},
    }

def test_foo():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello Users!",
        "params": {"q": None, "skip": 0, "limit": 100},
    }
