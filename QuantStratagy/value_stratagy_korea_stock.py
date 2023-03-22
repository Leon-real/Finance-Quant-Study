import pandas as pd

# 국내 주식 엑셀 데이터 불러오기
df = pd.read_excel('stocks.xlsx', engine='openpyxl')

# 벨류 값이 0이하인 경우 nan로 변경해주기
df_pivot = df[['종목코드','종목명','BPS','PER','PBR','EPS','DIV','DPS']]
df_pivot.set_index('종목코드', inplace=True) # 인덱스 설정

print(df_pivot)