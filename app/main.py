from fastapi import FastAPI, HTTPException
from .schemas import StockDataCreate, StockDataResponse
from .crud import create_stock_data, get_all_stock_data
from .utils import calculate_strategy_performance

app = FastAPI()

@app.get("/data", response_model=list[StockDataResponse])
def read_data():
    data = get_all_stock_data()
    return [
        StockDataResponse(
            id=row[0],
            datetime=row[1],
            open=row[2],
            high=row[3],
            low=row[4],
            close=row[5],
            volume=row[6],
        ) for row in data
    ]

@app.post("/data", response_model=StockDataResponse)
def add_data(stock_data: StockDataCreate):
    try:
        record_id = create_stock_data(stock_data)
        return StockDataResponse(id=record_id, **stock_data.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/strategy/performance")
def strategy_performance():
    try:
        data = get_all_stock_data()
        if not data:
            raise HTTPException(status_code=404, detail="No stock data available.")
        performance = calculate_strategy_performance(data)
        return performance
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
