from app.utils import calculate_moving_averages, generate_signals, calculate_strategy_performance
from datetime import datetime
import decimal

sample_data = [
    (1, datetime(2025, 3, 18, 10, 0, 0), decimal.Decimal('100.5'), decimal.Decimal('105.0'), 
     decimal.Decimal('99.8'), decimal.Decimal('104.2'), 5000),
    (2, datetime(2025, 3, 19, 10, 0, 0), decimal.Decimal('104.2'), decimal.Decimal('106.5'), 
     decimal.Decimal('103.0'), decimal.Decimal('105.8'), 4500),
]

def test_calculate_moving_averages():
    df = calculate_moving_averages(sample_data, short_window=2, long_window=3)
    assert 'SMA_Short' in df.columns
    assert 'SMA_Long' in df.columns

def test_generate_signals():
    df = generate_signals(sample_data)
    assert 'Signal' in df.columns
    assert len(df) > 0

def test_calculate_strategy_performance():
    result = calculate_strategy_performance(sample_data)
    assert "cumulative_return" in result
    assert isinstance(result['cumulative_return'], float)
    assert "signals" in result
