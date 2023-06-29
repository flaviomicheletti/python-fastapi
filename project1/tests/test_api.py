import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)

def test_my_endpoint(client, mocker):
    # Mock any dependencies or external services used by your API

    # Example 1: Mocking a dependency using the `mocker` fixture
    mocked_dependency = mocker.patch('app.main.my_dependency_function')
    mocked_dependency.return_value = "Mocked response"

    # Example 2: Mocking an external service using the `mocker` fixture
    mocked_service = mocker.patch('app.main.my_external_service')
    mocked_service.get_data.return_value = {"mocked_key": "mocked_value"}

    # Perform a request to your API endpoint
    response = client.get("/my-endpoint")

    # Assert the response
    assert response.status_code == 200
    assert response.json() == {
        "message": "Mocked response",
        "external_data": {"mocked_key": "mocked_value"}
    }
