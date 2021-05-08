
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date, timedelta

portfolio = [
    'MSFT',
    'AAPL',
    'TSLA',
    'AMZN',
    'GOOG',
    'GOOGL',
    'NVDA',
    'INTC',
    'CSCO',
    'NFLX',
    'AVGO',
    'COST',
    'QCOM',
    'AMGN',
    'SBUX',
    'AMD',
    'GILD',
    'ZM',
    'NXPI',
    'REGN',
    'EBAY',
    'LULU',
    'CTAS',
    'DOCU',
    'MRVL',
    'XLNX',
    'OKTA',
]

endDate = date.today()
startDate = endDate - timedelta(days=180)
endDate = endDate.strftime("%Y-%m-%d")
startDate = startDate.strftime("%Y-%m-%d")

for tckr in portfolio:
    hist = yf.Ticker(tckr).history(period='6mo')
    hist.to_csv("{}.csv".format(tckr), encoding='utf-8')