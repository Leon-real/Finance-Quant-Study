import pandas_datareader.data as web
from pandas_datareader.famafrench import get_available_datasets
import matplotlib.pyplot as plt
import numpy as np

datasets = get_available_datasets()

# PBR 데이터 받기
df_pbr = web.DataReader('Portfolios_Formed_on_BE-ME',
                        'famafrench',
                        start='1900-01-01')

# print(df_pbr)

plt.rc('font', family='AppleGothic')
plt.rc('axes', unicode_minus=False)

df_pbr_vw = df_pbr[0].loc[:, ['Lo 20', 'Qnt 2', 'Qnt 3', 'Qnt 4', 'Hi 20']] # 5분위로 나눈 열만 선택한 후 저장
df_pbr_cum = (1 + df_pbr_vw / 100).cumprod() # 누적 수익률 계산하기

# 로그 그래프로 나타내기
df_pbr_cum = np.log(1 + df_pbr_vw / 100).cumsum()
df_pbr_cum.plot(figsize=(10, 6),
                legend = 'reverse',
                title = 'PBR 별 포트폴리오의 누적 수익률')
# 그래프 보여주기
plt.show()