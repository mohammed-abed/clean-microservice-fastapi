from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_and_get_item():
    response = client.post(
        "/items",
        json={"name": "Test Item", "description": "Test"}
    )
    assert response.status_code == 200
    item_id = response.json()["id"]

    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 200