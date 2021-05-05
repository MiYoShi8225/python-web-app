import matplotlib
import pandas as pd
import matplotlib.pyplot as  plt
import yfinance as yf

df = pd.DataFrame()
def tickere_func(company):
    aapl = yf.Ticker(tickers[company])
    hist = aapl.history(day)
    hist.index = hist.index.strftime('%d %B %Y')
    hist = hist[['Close']]
    hist.columns = [company]
    hist = hist.T
    return pd.concat([df, hist])

day = str('20d')
tickers = {
    'apple': 'AAPL',
    'facebook': 'FB',
    'google': 'GOOGL',
    'microsoft': 'MSFT',
    'netflix': 'NFLX',
    'amazon': 'AMZN'
}

for company in tickers.keys():
    df = tickere_func(company)

print(df)

#appleの株価
# aapl = yf.Ticker('AAPL')
# hist = aapl.history('20d')
# hist.index = hist.index.strftime('%d %B %Y')
# hist = hist[['Close']]
# hist.columns = ['apple']
# hist = hist.T
# print(hist)
