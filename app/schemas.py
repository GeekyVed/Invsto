from pydantic import BaseModel
from datetime import datetime

class StockDataCreate(BaseModel):
    datetime: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int

class StockDataResponse(StockDataCreate):
    id: int

    class Config:
        from_attributes = True
