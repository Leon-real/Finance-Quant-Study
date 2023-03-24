# How to Invest Using Quant

1. Optimization Portfolio (최적의 포트폴리오 구성하기) : OptimizationPortfolio.py   
- 일반적으로 많이 사용되는 `최대샤프지수 포트폴리오`, `최소분산 포트폴리오`, `위험균형 포트폴리오` 구현  


- 글로벌 자산 데이터의 상관관계 보기  
    미국 주식, 유럽 주식, 일본 주식, 이머징 주식, 미국 장기채, 미국 중기채, 미국 리츠, 글로벌 리츠, 금, 원자재
    위 상품들간의 상관관계 보기
> 검은 박스 : 주식 부분  
    노란 박스 : 채권 부분  
    초록 박스 : 리츠 부분  
    보라 박스 : 금  
    파란 박스 : 원자재  
    
<img src="../img/OptimizationPortfoilo.png" width="600px" height="600px" title="Optimization Portfoilo" alt="OptimizationPortfoilo"></img><br/>  

해당 사진에서 확인할 수 있듯, 주식부분은 서로 상관관계가 높고, 채권은 주식과 상관관계가 낮은 것을 확인할 수 있다.

