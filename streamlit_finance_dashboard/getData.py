import sqlalchemy
import yfinance as yf
import pandas as pd

tickers = pd.read_html("https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average")[1]
#tickers meaning -> AAPL, AMZN, MSFT etc

tickers = tickers.Symbol.to_list()

print(tickers) #op -> ['MMM', 'AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'KO', 'DIS', 'DOW', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'MCD', 'MRK', 'MSFT', 'NKE', 'PG', 'CRM', 'TRV', 'UNH', 'VZ', 'V', 'WBA', 'WMT']

