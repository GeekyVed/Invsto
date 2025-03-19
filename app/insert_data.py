import requests
from datetime import datetime, timedelta
import random

# API Endpoint
url = "http://localhost:8000/data"

# Generate sample data for 60 days
def generate_sample_data():
    start_date = datetime.now() - timedelta(days=60)
    data = []
    price = 100.0

    for i in range(60):
        price += random.uniform(-2, 2)  # Simulate stock price change
        data_point = {
            "datetime": (start_date + timedelta(days=i)).isoformat(),
            "open": round(price, 2),
            "high": round(price + random.uniform(0, 5), 2),
            "low": round(price - random.uniform(0, 5), 2),
            "close": round(price, 2),
            "volume": random.randint(1000, 10000),
        }
        data.append(data_point)

    return data

# Insert data using API
def insert_data():
    data = generate_sample_data()
    for record in data:
        response = requests.post(url, json=record)
        if response.status_code == 200:
            print(f"Inserted record: {record['datetime']}")
        else:
            print(f"Failed to insert data: {response.json()}")

insert_data()
