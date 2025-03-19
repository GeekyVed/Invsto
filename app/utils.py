import pandas as pd
import numpy as np
from .crud import get_all_stock_data

def calculate_moving_averages(data, short_window=10, long_window=50):
    df = pd.DataFrame(data, columns=['id', 'datetime', 'open', 'high', 'low', 'close', 'volume'])
    df['SMA_Short'] = df['close'].rolling(window=short_window).mean()
    df['SMA_Long'] = df['close'].rolling(window=long_window).mean()
    return df

def generate_signals(data):
    df = calculate_moving_averages(data)
    df['Signal'] = 0
    df.loc[df['SMA_Short'] > df['SMA_Long'], 'Signal'] = 1
    df.loc[df['SMA_Short'] < df['SMA_Long'], 'Signal'] = -1
    return df[['datetime', 'close', 'SMA_Short', 'SMA_Long', 'Signal']].dropna()

def calculate_strategy_performance(data):
    df = generate_signals(data)
    df['Daily_Return'] = df['close'].pct_change()
    df['Strategy_Return'] = df['Signal'].shift(1) * df['Daily_Return']
    cumulative_return = (1 + df['Strategy_Return']).cumprod().iloc[-1] - 1
    return {"cumulative_return": cumulative_return, "signals": df.to_dict(orient='records')}
