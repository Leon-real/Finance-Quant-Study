import pandas as pd

# 국내 주식 엑셀 데이터 불러오기
df = pd.read_excel('yearmomentum.xlsx', engine='openpyxl')

print(df)