from fastapi.testclient import TestClient

from main import app



client = TestClient(app)


def test_myfunction1():
    response = client.get("/path/1")
    assert response.status_code == 200
    assert response.json() == {"item": "1"}
    assert response.text == '{"item":"1"}'

def test_myfunction2():
    response = client.get("/query/1?skip=5&limit=10")
    assert response.status_code == 200
    assert response.json() == {"item": "1", "skip": "5", "limit": "10"}

def test_myfunction3():
    item_data = {
        "name": "item_name",
        "description": "item_description",
        "price": 10.0,
        "tax": 1.5
    }
    response = client.post("/models/", json=item_data)
    assert response.status_code == 200
    assert response.json() == item_data




"""
https://fastapi.tiangolo.com/tutorial/testing/#separating-tests

pytest
uvicorn main:app
"""