from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_home_returns_message():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Salam API"}


def test_multiply_returns_product():
    response = client.post("/multiply", params={"a": 6, "b": 7})

    assert response.status_code == 200
    assert response.json() == {"a": 6.0, "b": 7.0, "result": 42.0}


def test_division_returns_quotient():
    response = client.post("/division", params={"a": 15, "b": 3})

    assert response.status_code == 200
    assert response.json() == {"a": 15.0, "b": 3.0, "result": 5.0}
