from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_create_product():
    response = client.post(
        "/products",
        json={
            "name": "Test Product",
            "price": 99.99,
            "availability": "In Stock",
            "description": "Test description",
            "rating": 5
        }
    )

    assert response.status_code == 200


def test_get_products():
    response = client.get("/products")

    assert response.status_code == 200
    assert isinstance(response.json(), list)