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
python -m unittest discover -s tests
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

### 1. Screenshot of the `/data` Endpoint Response
![Data Endpoint Screenshot](./path/to/screenshot_data.png)

### 2. Screenshot of the `/strategy/performance` Endpoint Response
![Strategy Performance Screenshot](./path/to/screenshot_performance.png)

### 3. Screenshot of the Unit Test Results
![Unit Test Results Screenshot](./path/to/screenshot_tests.png)

---

## License

This project is licensed under the MIT License.

---

Thank you for reviewing the Invsto assignment! Feel free to reach out for any questions or clarifications.

```