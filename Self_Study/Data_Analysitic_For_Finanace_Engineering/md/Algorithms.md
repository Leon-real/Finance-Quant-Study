# 데이터학습을 위한 알고리즘 종류

##### 목차
- [데이터 분석에서 학습 알고리즘이란?](#데이터-분석에서-학습-알고리즘이란)  
- [학습 알고리즘 종류](#학습-알고리즘-종류)  
- [정리](#정리)  

## 데이터 분석에서 학습 알고리즘이란 ?
- 학습(Learning) : 데이터분석 과정을 컴퓨터/기계 스스로가 과거와 현재를 학습하게 하고 미래를 예측하게 하는 과정  
    - 과거 : 사람의 패턴을 모방하여 컴퓨터를 사람처럼 만들려고 노력  
        - 사람의 패턴이나 정답을 수학적으로 모델링(알고리즘화)  
        - 데이터보다는 사람의 패턴을 수학적으로 표현하여 문제를 해결  
    - 현재 : 사람의 학습방식을 모방하여 컴퓨터가 사람처럼 학습하도록 노력  
        - 사람의 패턴이나 정답을 찾지 않고 뇌의 작동방식을 모델링(알고리즘화)  
        - 사람의 패턴은 알 필요 없이 데이터를 컴퓨터에게 지속적으로 전달(학습)하면 스스로 문제를 해결  

## 학습 알고리즘 종류  
- 알고리즘을 하나 하나 배우는 것보다 중요한 것은
- `실제 내가 풀어야 하는 문제가 무엇인지`
- `어떤 알고리즘의 범주에 있는지 확인`하는게 가장 중요하다.
### 지도학습
- 해결문제 종류
    - 예측 문제
        - ex) 주관식 문제의 숫자형태의 정답을 해결  
    - 분류 문제
        - ex) 객관식 문제의 보기들 중 정답을 해결
- 알고리즘 종류
    - Regression Algorithms
        - Linear Regression
        - Logistic Regression
    - Instance-based Algorithms
        - K-Nearest Neightbor(KNN)
        - Self-Organizing Map(SOM)
    - Regularization Algorithms
        - Ridge Regression
        - Least Absolute Shrinkage and Selection Operator(LASSO)
        - Elastic Net
    - Decision Tree Algorithms
    - Bayesian Algorithms
    - Artificail Neural Network Algorithms
  
### 비지도학습
- 해결문제 종류
    - 군집 문제
        - ex) 시험문제에 어떤 유형들이 있는지 해결
    - 차원변환 문제
        - ex) 시험문제의 풀이법을 다양한 관점으로 변환
- 알고리즘 종류
    - Clustering Algorithms
    - Association Rule Learning Algorithms
    - Dimensionality Reduction Algorithms
    - Ensemble Algorithms
    - Deep Learning Algorithms
### 강화학습
- 스스로 지도학습/비지도학습 문제를 해결하고 오답노트도 스스로 만들고 학습하여 성적을 계속 끌어올림  

## 정리
- 알고리즘을 하나 하나 배우는 것보다 중요한 것은
- `실제 내가 풀어야 하는 문제가 무엇인지`
- `어떤 알고리즘의 범주에 있는지 확인`하는게 가장 중요하다.
- 이후 과정은 수둥적이기 때문에.
- 알고리즘은 크게 3-4가지 문제들을 해결하기 위해 만들어진다.
    1. 문제가 어디에 속하는지 -> 문제정의 및 분석기획(가설설정) 가능
    2. 알고리즘의 입력은 무엇인지 -> 분석기획(데이터준비 및 전처리) 가능
    3. 알고리즘의 출력은 무엇인지 -> 분석기획(가설검정) 및 성능검증 가능
- 내가 풀어야 할 문제가 무엇인지 알면 분석설정과 해결은 수동적인 작업(단순)
