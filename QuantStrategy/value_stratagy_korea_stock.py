import pandas as pd

# 국내 주식 엑셀 데이터 불러오기
df = pd.read_excel('stocks.xlsx', engine='openpyxl')

# 벨류 값이 0이하인 경우 nan로 변경해주기
df_pivot = df[['종목코드','종목명','BPS','PER','PBR','EPS','DIV','DPS']]
df_pivot.set_index('종목코드', inplace=True) # 인덱스 설정

# print(df_pivot)

# value값 순위 구하기 PER, PBR 두개만 선택해서
# value_rank = df_pivot[['PER','PBR']].rank(axis = 0) #PER, PBR 열을 선택한 후 , 각열을 기준으로 순위를 구함
# value_sum = value_rank.sum(axis = 1, skipna = False).rank() # PER와 PBR이 더해진 값으로 랭킹을 다시 구함
# value = df_pivot.loc[value_sum <= 20, ['종목명', 'PER','PBR']] # PER와 PBR을 고려했을 때, 밸류에이션이 낮은 20개 종목

# print(value)

# 배당수익률 역순으로 재정렬하기 (배당수익률은 높으면 높을수록 좋은 내림차순에 해당하므로 순서가 맞지 않기 떄문에)
value_list_copy = df_pivot.copy()
value_list_copy['DIV'] = 1 / value_list_copy['DIV']

# 각 지표별 랭킹 구하기
value_rank_all = value_list_copy.rank(axis=0) # 각 지표별 랭킹 구하기 (열별로)
value_sum_all = value_rank_all.sum(axis=1, skipna=False).rank() # 행별로 각 지표를 합해서 랭킹 구하기
value_all = df_pivot.loc[value_sum_all <= 20] # 저평가된 20개 종목 구하기 

print(value_all)