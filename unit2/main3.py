import matplotlib
import pandas as pd
import matplotlib.pyplot as  plt
import yfinance as yf

aapl = yf.Ticker('AAPL')
print(aapl.info)

print(aapl.actions.head())

aapl.dividends.plot()

aapl.actions['Stock Splits'].plot()
