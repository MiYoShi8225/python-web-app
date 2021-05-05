import altair as alt
from altair.vegalite.v4.schema.channels import Opacity
import matplotlib
import pandas as pd
import matplotlib.pyplot as  plt
import yfinance as yf
import streamlit as st

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

#print(df)

companiers= ['apple', 'facebook']
# locでcompaniersに入っている会社名だけを抽出
data = df.loc[companiers]

data = data.T.reset_index()
#print(data)

#日付-企業名-株価の並びにデータを整理した
#print(pd.melt(data, id_vars=['Date']))

data = pd.melt(data, id_vars=['Date']).rename(
    columns={'value': 'stock prices(USD)'}
)

print(data)

chart = (
    alt.Chart(data)
    .mark_line(opacity=0.8, clip=True)
    .encode(
        x="Date:T",
        y=alt.Y("stock prices(USD):Q", stack=None, scale=alt.Scale(domain=[50,400])),
        color='variable:N'
    )
)

st.write(chart)
