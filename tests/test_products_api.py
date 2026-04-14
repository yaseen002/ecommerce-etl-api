import pytest
from httpx import AsyncClient
from src.main import app


@pytest.mark.anyio
async def test_create_product():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/products",
            json={
                "name": "Test Product",
                "price": 99.99,
                "availability": "In Stock",
                "description": "Test description",
                "rating": 5
            }
        )

    assert response.status_code in (200, 201)


@pytest.mark.anyio
async def test_get_products():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/products")

    assert response.status_code == 200