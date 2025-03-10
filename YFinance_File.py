# -*- coding: utf-8 -*-
"""qGetReturns.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D4n5jMMaDfhqyinFzXdU6o9doOuFFSjy
"""

import pandas as pd
import yfinance as yf
import numpy as np

def YahooData2returns(data):

    if isinstance(data, pd.DataFrame):
        prices = data['Adj Close']
    else:
        prices = data

    returns = prices.pct_change()

    returns = returns.dropna()

    return returns

def get_stock_data(ticker, start=None, end=None):

    data = yf.download(ticker, start=start, end=end)

    adj_close = data['Adj Close']
    return adj_close

def get_returns(ticker, start=None, end=None):

    adj_close = get_stock_data(ticker, start=start, end=end)

    returns = YahooData2returns(adj_close)
    return returns

#Returns test

d = { 'Open': [100, 102, 101, 103],

'High': [105, 104, 103, 105],

'Low': [98, 100, 99, 101],

'Close': [101, 103, 102, 104],

'Adj Close': [101, 103, 102, 104],

'Volume': [1000, 1200, 900, 1100]}



index = pd.to_datetime(['2023-10-26', '2023-10-27', '2023-10-28', '2023-10-29'])

tempdata = pd.DataFrame(d, index=index)

returns = YahooData2returns(tempdata)

np.isclose(returns[0], 0.01980198, atol=0.01)

np.isclose(returns[1], -0.00970874, atol=0.01)

np.isclose(returns[2], 0.01960784, atol=0.01)

