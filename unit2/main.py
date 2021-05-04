import matplotlib
import pandas as pd
import matplotlib.pyplot as  plt
import yfinance as yf

#%matplotlib in inline

aapl = yf.Ticker('AAPL')

#print(aapl.history())
#50日分取得する場合↓
#print(aapl.history(period='50d'))

hist = aapl.history()

#date がindexの役割をはたしている
#print(hist.columns)

#indexを振り分けてdateもデータ項目にすることができる↓
#print(hist.reset_index())

#microsoftの株価
hist_msft = yf.Ticker('MSFT').history(period='20d')
#print(hist_msft.head())

#pd.concat([hist, hist_msft], axis=1)

print(hist.head(3))

print(hist.index)

hist.index = hist.index.strftime('%d %B %Y')
print(hist.head())

hist = hist[['Close']]
hist.columns = ['apple']

print(hist.head())

hist = hist.T
print(hist)
