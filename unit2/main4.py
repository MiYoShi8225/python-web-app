import matplotlib
import pandas as pd
import matplotlib.pyplot as  plt
import yfinance as yf

def tickere_func(tickers, day):
    df = pd.DataFrame()

    for company in tickers.keys():
        aapl = yf.Ticker(tickers[company])
        hist = aapl.history(day)
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        df = pd.concat([df, hist])
    return df

day = str('20d')
tickers = {
    'apple': 'AAPL',
    'facebook': 'FB',
    'google': 'GOOGL',
    'microsoft': 'MSFT',
    'netflix': 'NFLX',
    'amazon': 'AMZN'
}

df = tickere_func(tickers, day)

print(df)
