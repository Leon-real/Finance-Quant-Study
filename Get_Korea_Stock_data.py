import pandas as pd
import numpy as np
from pykrx import stock


today_date = "20230324"

stock_list = pd.DataFrame({'종목코드':stock.get_market_ticker_list(market="ALL")})
stock_list['종목명'] = stock_list['종목코드'].map(lambda x: stock.get_market_ticker_name(x))
stock_fud = pd.DataFrame(stock.get_market_fundamental_by_ticker(date=today_date, market="ALL"))
stock_fud = stock_fud.reset_index()
stock_fud.rename(columns={'티커':'종목코드'}, inplace=True)
result = pd.merge(stock_list, stock_fud, left_on='종목코드', right_on='종목코드', how='outer')
stock_price = stock.get_market_ohlcv_by_ticker(date=today_date, market="ALL")
stock_price = stock_price.reset_index()
stock_price.rename(columns={'티커':'종목코드'}, inplace=True)
result1 = pd.merge(result, stock_price, left_on='종목코드', right_on='종목코드', how='outer')
result1 = result1.replace([0], np.nan)
result1 = result1.dropna(axis=0)
result1['내재가치'] = (result1['BPS'] + (result1['EPS']) * 10) / 2
result1['내재가치/종가'] = (result1['내재가치'] / result1['종가'])
result1.to_excel("stocks.xlsx")
print("Complete")