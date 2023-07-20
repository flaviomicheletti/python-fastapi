from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_item():
    response = client.get("/items/foo", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }


def test_read_item_bad_token():
    response = client.get("/items/foo", headers={"X-Token": "hailhydra"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_read_inexistent_item():
    response = client.get("/items/baz", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_create_item():
    input = {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    } 
    # is the same!
    output = {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }

    response = client.post("/items/", headers={"X-Token": "coneofsilence"}, json=input)
    assert response.status_code == 200
    assert response.json() == output


def test_create_item_bad_token():
    input = {"id": "bazz", "title": "Bazz", "description": "Drop the bazz"}
    output = {"detail": "Invalid X-Token header"}

    response = client.post(
        "/items/",
        headers={"X-Token": "hailhydra"},
        json=input,
    )

    assert response.status_code == 400
    assert response.json() == output


def test_create_existing_item():

    input = {
        "id": "foo",
        "title": "The Foo ID Stealers",
        "description": "There goes my stealer",
    }
    output = {"detail": "Item already exists"}

    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json=input,
    )
    assert response.status_code == 400
    assert response.json() == output
