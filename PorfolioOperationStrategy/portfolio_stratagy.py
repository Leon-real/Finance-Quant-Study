import yfinance as yf
import pandas as pd
import statsmodels.api as sm # 회기모델 


# 주가 데이터 데이터 받기
tickers = ['^KS11', '039490.KS'] # 키움 증권 티커

all_data = {} # 주가가 들어갈 데이터 딕셔너리
for ticker in tickers: # 데이터 다운 받기
    all_data[ticker] = yf.download(ticker,
                                   start='2016-01-01',
                                   end='2022-12-31')
    
prices = pd.DataFrame({tic: data['Close'] for tic, data in all_data.items()}) # 종가를 가지고 데이터 프레임 만들기
ret = prices.pct_change().dropna() # 수익률 나타내기 + Nan 값 제거

# 회기 모델 사용하기
ret['intercept'] = 1 # 절편(알파)에 해당하는 부분을 만들기 위해 해당 열에 1을 입력
# 선형 회기 분석 : y축은 개별 주식의 수익률, x축에서는 코스피 수익률과 절편 부분 입력
reg = sm.OLS(ret[['039490.KS']], ret[['^KS11', 'intercept']]).fit() 

print(reg.summary()) # 선형회기 분석 결과 보기