import json
from prisma import Prisma
from prisma.models import StockData

def test_post_data(client):
    data = {
        "datetime": "2025-03-18T10:00:00",
        "open": 100.5,
        "high": 105.0,
        "low": 99.8,
        "close": 104.2,
        "volume": 5000
    }
    response = client.post("/data", json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Stock data added successfully"}

def test_post_invalid_data(client):
    invalid_data = {
        "datetime": "invalid_date",
        "open": "not_a_number",
        "volume": -10
    }
    response = client.post("/data", json=invalid_data)
    assert response.status_code == 422  # Unprocessable Entity

def test_get_data(client):
    response = client.get("/data")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_strategy_performance_no_data(client):
    response = client.get("/strategy/performance")
    print("Stamina nananaondkfjsjdfddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
    print(response.json())
    assert response.status_code == 404
    assert response.status_code == 200
    assert "404: No stock data available." in response.json().get("detail")
