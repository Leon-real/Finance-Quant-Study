import pandas as pd

# 국내 주식 엑셀 데이터 불러오기
df = pd.read_excel('yearmomentum.xlsx', engine='openpyxl')

print(df)
# 모멘텀 랭크 구하기
momentum_rank = df['return'].rank(axis=0, ascending=False)
momentum = df[momentum_rank <= 20]
# print(momentum)

# k-ratio 값 랭크 구하기
k_ratio_rank = df['res'].rank(axis=0, ascending=False)
r_ratio = df[k_ratio_rank <= 20]
print(r_ratio)