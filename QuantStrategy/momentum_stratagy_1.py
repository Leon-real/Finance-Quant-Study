import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
import requests as rq
from io import BytesIO
import re
import numpy as np
import statsmodels.api as sm

# 국내 주식 엑셀 데이터 불러오기
df = pd.read_excel('stocks.xlsx', engine='openpyxl')
tickers = df['종목코드']

new_df = df[['종목코드','종목명','종가']]
new_df.set_index('종목코드', inplace=True) # 인덱스 설정

# 1년 기간동안의 종가 데이터 받기
fr = (date.today() + relativedelta(years=-1)).strftime('%Y%m%d') # 1년간 기간
to = (date.today()).strftime('%Y%m%d') # 오늘 날짜

code_lists = []
return_values =[]
res_lists=[]
for ticker in tickers:
    real_ticker=ticker
    ticker = str(ticker).zfill(6)
    url = f'''https://fchart.stock.naver.com/siseJson.nhn?symbol={ticker}&requestType=1&startTime={fr}&endTime={to}&timeframe=day'''
    data = rq.get(url).content
    data_price = pd.read_csv(BytesIO(data), encoding='utf-8')

    # 데이터 전처리
    price = data_price.iloc[:, 0:6]
    price.columns = ['날짜','시가','고가','저가','종가','거래량']
    price = price.dropna()
    price['날짜'] = price['날짜'].str.extract('(\d+)')
    price['날짜'] = pd.to_datetime(price['날짜'])
    price = pd.DataFrame(price)
    
    # 1년간 누적 수익률 구하기
    return_value = (price['종가'].iloc[-1] / price['종가'].iloc[0]) - 1
#     print(ticker, return_value)
    code_lists.append(real_ticker)
    return_values.append(return_value)
    
    # 일간 수익률 구하기
    try:
        ret = price['종가'].pct_change()[1:]
        ret_cum = np.log(1 + ret).cumsum()

        x = np.array(range(len(ret)))
        y = ret_cum.iloc[:].values

        reg = sm.OLS(y,x).fit()
        res = float((reg.params / reg.bse))
    except:
        res = np.nan
    res_lists.append(res)
    print(f"{ticker} Saved.")
temp_df = pd.DataFrame({'종목코드':code_lists, 'return':return_values, 'res':res_lists})

data_bind = new_df.merge(temp_df, how='left', on='종목코드')
data_bind.to_excel('yearmomentum.xlsx')
print("Data Save Success.")