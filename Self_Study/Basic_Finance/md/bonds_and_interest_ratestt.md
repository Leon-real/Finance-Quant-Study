# 이자율, 채권가격 및 듀레이션
##### 목차
- [채권의 구성요소](#채권의-구성요소)  
- [채권의 수익률과 가격](#채권의-수익률과-가격)
- [듀레이션(Duration)](#듀레이션)
- [채권가격 정리](#채권가격-정리)
## 채권의 구성요소
### 현금 흐름
- `투자자(채권자)`는 `발행자(채무자)`에게 투자(원금)하고 이자와 원금을 받는다.
### 원금(액면금액)
- 채무자가 만기에 상환하여야 할 금액
### 이자(표면이자율)
- 원금 x 이자율의 금액을 매년(매반기 또는 매분기) 지급
    - 고정금리
    - 변동금리
    - 이자가 없는 경우(할인채)
    - 표면이자율 = 액면 이자율 = Coupon rate
### 만기
- 투자 기간, 영구채(만기가 없음)

## 채권의 수익률과 가격
### 만기 수익률(YTM : Yield To Maturity)
- 만기까지 보유할 경우 채권 현금흐름의 현재가치를 채권가격과 일치시켜주는 수익률 => 채권금리, 채권 수익률, 만기수익률, 이자율
- 채권가격과 금리(이자율)는 반비례한다.
    - 금리가 오르면 `신규투자자`는 미래이득이 증가하고
    - `이전 투자자`는 평가손실이 증가한다.
- YTM : 만기별로 이자율이 동일하다고 가정한다.
### 현물이자율(Spot Rate)
- 만기 전에는 이자를 지급하지 않는 무이표채 또는 할인채에 적용되는 만기수익률
### 내재선도이자율(Implied Forward Rate)
- 만기별 현물이자율의 관계에서 도출되는 미래기대이자율 => 현재시점에서 결정되는 미래 일정기간 동안의 이자율

## 듀레이션(Duration)
- 듀레이션의 정의 : 채권의 실질적인 만기로 채권투자시 발생하는 현금흐름의 `가중평균기간`을 의미한다. => 가중평균만기
### 듀레이션의 속성
1. 만기가 길수록 듀레이션 증가
2. 액면이자율이 높을수록 듀레이션 감소(현금흐름이 앞에서 많이 발생하기 때문에)
3. 만기수익률이 높을수록 듀레이션 감소(할인되는 폭이 원금에서 가장 크기 때문에)
4. 할인채의 경우 만기 = 듀레이션
5. 시간이 지나면서 듀레이션 감소
### 수정듀레이션(Modified Duration)
- `이자율 변동에 따른 채권가격의 변동률`로 듀레이션에 1/(1+YTM)을 곱해 산출한다.
### 금액듀레이션(Dollar Duration)
- 이자율 1bp변동에 따른 채권가격의 변동금액으로 현재가치 / 수정듀레이션 / 100으로 산출한다.

## 채권가격 정리
- 채권가격은 이자율과 역의 관계
    - 이자율 상승시 채권가격 하락
- 만기가 길수록 이자율 변동에 대한 채권가격 변동폭이 커진다.
    - 만기가 길수록 듀레이션 증가
    - 즉, 장기채의 가격이 단기채의 가격보다 이자율변동에 민감하다.
        - 이자율 상승 예측 => 듀레이션 축소 운용
        - 이자율 하락 예측 => 듀레이션 확대 운용
- 채권수익률 변동에의한 채권가격 변동폭은 만기가 길어질수록 증가하나 그 증감률은 체감한다.
- 만기가 일정할 때, 채권 수익률 하락으로 인한 가격 상승폭은 채권 수익률 상승으로 인한 가격 하락폭보다 크다.
- 액면이자율이 낮을수록 동일 이자율 변동의 채권가치변동률이 크다.

## 수익률곡선(Yield Curve)
- 한 시점에서 동일한 발행주체가 발행한 채권에 대한 만기별 이자율을 연결한 곡선(Term Structure of interest rates)
    - x축 자존만기, y축 채권 수익률
        - 상승형
        - 하강형
        - 수평형
        - 낙타형
### 수익률곡선 설명 이론
- 불편기대이론
- 유동성프리미엄 이론
- 시장분할 이론