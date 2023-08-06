import requests
import matplotlib.pyplot as plt

'''Develop a stock market data analyzer that fetches historical 
stock data using a financial API like Alpha Vantage. 
The program can calculate various metrics such as moving 
averages, daily returns, and price correlations for selected 
stocks. It can visualize the data with graphs and charts using 
libraries like Matplotlib.'''

def fetch_stock_data(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data["Time Series (Daily)"]

def plot_stock_prices(data):
    dates = list(data.keys())
    prices = [float(data[date]["4. close"]) for date in dates]
    plt.plot(dates, prices)
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.title("Stock Price Over Time")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Usage example
symbol = "AAPL"  # Apple Inc. stock symbol
api_key = "YOUR_API_KEY"
stock_data = fetch_stock_data(symbol, api_key)
plot_stock_prices(stock_data)
