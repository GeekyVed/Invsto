# Invsto - Technical Assignment

Welcome to the Invsto technical assignment repository! This project demonstrates the implementation of a PostgreSQL database, FastAPI application, simple trading strategy, and unit tests.

## Table of Contents
- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Endpoints](#endpoints)
- [Trading Strategy](#trading-strategy)
- [Unit Testing](#unit-testing)
- [Docker](#docker)
- [Screenshots](#screenshots)
- [License](#license)

---

## Project Overview

This project consists of four main parts:

1. **Database Setup**: A PostgreSQL table is created to store financial data (timestamp, open, high, low, close, volume) for a single ticker symbol.
2. **API Development**: A FastAPI application is created with endpoints to interact with the database.
3. **Trading Strategy**: A Moving Average Crossover Strategy is implemented to generate buy/sell signals based on moving averages.
4. **Unit Testing**: Unit tests ensure input validation, correctness of calculations, and the overall reliability of the system.

---

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **ORM**: Prisma
- **Testing**: unittest
- **Containerization**: Docker

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/invsto-assignment.git
cd invsto-assignment
```

### 2. Set up the Database
Make sure you have PostgreSQL installed and running. Use Prisma to manage the database schema.

#### Prisma Setup:
- Install Prisma CLI: 
  ```bash
  npm install @prisma/cli
  ```
- Generate the Prisma client:
  ```bash
  npx prisma generate
  ```
- Apply the migrations to your PostgreSQL database:
  ```bash
  npx prisma migrate dev
  ```

### 3. Install Dependencies
Install Python dependencies using `pip`:
```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Application
Run the FastAPI app locally:
```bash
uvicorn app.main:app --reload
```
Visit `http://127.0.0.1:8000` to access the API.

---

## Endpoints

### `GET /data`
- **Description**: Fetch all records from the database.
- **Response**:
  ```json
  [
    {
      "datetime": "2025-03-19T15:00:00Z",
      "open": 100.5,
      "high": 105.0,
      "low": 99.0,
      "close": 102.0,
      "volume": 5000
    },
    
  ]
  ```

### `POST /data`
- **Description**: Add new records to the database.
- **Request Body**:
  ```json
  {
    "datetime": "2025-03-19T15:00:00Z",
    "open": 100.5,
    "high": 105.0,
    "low": 99.0,
    "close": 102.0,
    "volume": 5000
  }
  ```
- **Response**:
  ```json
  {
    "message": "Record added successfully"
  }
  ```

### `GET /strategy/performance`
- **Description**: Calculate the performance of a simple moving average crossover strategy.
- **Response**:
  ```json
  {
    "buy_signals": 5,
    "sell_signals": 4,
    "performance": "15%"
  }
  ```

---

## Trading Strategy

A **Moving Average Crossover Strategy** is implemented to generate buy and sell signals based on short-term and long-term moving averages of the stock data.

- **Short-term Moving Average**: 10-period
- **Long-term Moving Average**: 50-period
- **Buy Signal**: When the short-term moving average crosses above the long-term moving average.
- **Sell Signal**: When the short-term moving average crosses below the long-term moving average.

The performance of the strategy is calculated as the percentage of successful trades.

---

## Unit Testing

Unit tests are written using Python's `unittest` framework to validate:
- Input validation for the `/data` endpoint (e.g., checking proper data types for each field).
- Correctness of moving average calculations.
- Test coverage for the system (80%+).

Run the tests with:
```bash
pytest tests/ --cov=app                                         
```

---

## Docker

The FastAPI application is containerized using Docker for easy deployment.

### Build the Docker Image
```bash
docker build -t invsto-app .
```

### Run the Docker Container
```bash
docker run -p 8000:8000 invsto-app
```

The FastAPI app will be accessible at `http://localhost:8000`.

---

## Screenshots

![Image](https://github.com/user-attachments/assets/15e42539-38e5-44cd-a0b6-1ad95b3939ad)

### 1. Screenshot of the `/data` Endpoint Response
![Image](https://github.com/user-attachments/assets/30caf672-4631-441f-9118-dac8ff71db94)

### 2. Screenshot of the `/strategy/performance` Endpoint Response
![Image](https://github.com/user-attachments/assets/ef7f926f-cead-4cff-845b-6523f6225cb0)

### 3. Screenshot of the Unit Test Results
![Image](https://github.com/user-attachments/assets/743d9a59-67b5-4925-b664-d62c2777c6d1)

---

## License

This project is licensed under the MIT License.
