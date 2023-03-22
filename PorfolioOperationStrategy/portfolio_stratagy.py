import yfinance as yf
import pandas as pd

tickers = ['^KS11', '039490.KS'] # 키움 증권 티커

all_data = {} # 주가가 들어갈 데이터 딕셔너리
for ticker in tickers: # 데이터 다운 받기
    all_data[ticker] = yf.download(ticker,
                                   start='2016-01-01',
                                   end='2022-12-31')
    
prices = pd.DataFrame({tic: data['Close'] for tic, data in all_data.items()}) # 종가를 가지고 데이터 프레임 만들기
ret = prices.pct_change().dropna()

print(ret)