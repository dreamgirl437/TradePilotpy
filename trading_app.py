import requests
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

# Alpha Vantage API key (replace with your actual key)
API_KEY = 'your_alpha_vantage_api_key'

# Initialize Alpha Vantage API
ts = TimeSeries(key=API_KEY, output_format='pandas')

# List of stock symbols to fetch
symbols = ['AAPL', 'GOOGL', 'MSFT']

# Dictionary to store stock data
stock_data = {}

# Fetch data for each symbol
for symbol in symbols:
    print(f"Fetching data for {symbol}...")
    data, meta_data = ts.get_intraday(symbol=symbol, interval='1min', outputsize='full')
    stock_data[symbol] = data  # Store the data in a dictionary
    data.to_csv(f'{symbol}_data.csv')  # Save each stock's data to a CSV file

# Display the first few rows for each stock
for symbol, data in stock_data.items():
    print(f"\n{symbol} Stock Data:\n", data.head())
