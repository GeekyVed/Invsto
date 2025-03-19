from .database import get_db_connection
from .schemas import StockDataCreate
from psycopg2 import sql

def create_stock_data(data: StockDataCreate):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = sql.SQL(
        "INSERT INTO \"StockData\" (datetime, open, high, low, close, volume) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    )

    cursor.execute(query, (data.datetime, data.open, data.high, data.low, data.close, data.volume))
    record_id = cursor.fetchone()[0]
    conn.commit()

    cursor.close()
    conn.close()
    return record_id

def get_all_stock_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    query = sql.SQL("SELECT * FROM \"StockData\"")
    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conn.close()
    return results
