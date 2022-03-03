# CJ 미래기술 챌린지 (상품/물량 수요 예측)
#### 시계열 클러스터링과 머신러닝(ML)을 활용한 상품/물량 수요 예측

## Background

  
  

## Difference
- 기존 수요 예측과는 다르게 심리 변수, 외부 변수를 사용
	- 심리 변수는 하루 전, 이틀 전, 삼일 전의 수요를 통해 사람들의 소비 심리를 입력 변수로 사용하였고 유행에 따라 상품을 소비하는 현상, 밴드웨건 효과를 모델에 반영
	- 외부 데이터로 휴일여부/요일, 세대원수 별 세대수, 성별/연령대별 인구 수를 활용하여 지역별 특성이 반영되도록 하였다.

- 창고 관리자에게 제공할 창고 내 품목에 대한 수요 예측 뿐만 아니라 고객사 코드별 수요 예측을 통해 고객사에게 제공할 정보를 구축하였고 이를 통해 고객사 유치가 가능하도록 하였다.

- 한 가지 모델만 사용하지 않고 다양한 모델을 앙상블하여 모델의 정확도를 높였다. XGB, LGBM, SVR, GBR, ABR 5개의 모델을 사용하여 수요 예측을 시행
	- 단일 모델에서의 MAE가 작은 3가지 모델을 활용해 stacking
	- 단일 모델과 stacking 모델의 MAE 값을 비교하여 작은 값으로 모델링 결과를 반환, 정확도 높은 예측을 보였다.

- 시계열 클러스터링을 통해 품목별 수요 패턴을 구분
	- 수요 주기와 수요 패턴이 다른 품목들을 시계열 클러스터링을 통해 군집화
		- 각 품목의 수요 패턴에 적합한 재고 관리, 생산 관리 전략을 세울 수 있도록 하였다. 또한 얻은 수요 주기, 패턴 정보를 모델의 입력 변수로 활용해 예측의 정확도를 높였다.
  
  

## Participants

**연세대학교 산업공학과**
이유림(18학번), 김연재(19학번), 윤수진(18학번), 석민정(18학번)

## Directory Structure

<pre>
<code>
├── Data
│ ├── external-data
│ └── internal-data
├── Modeling
│ ├── modeling_cluster.ipynb
│ ├── modeling_cnee_addr.ipynb
│ ├── modeling_item_cd.ipynb
│ ├── modeling_shpr_cd.ipynb
├── Preprocessing
│ ├── data
│ ├── model
│ └── time-series-clustering
├── README.md
├── Tableau
│ └── CJ_EDA_Dashboard.twb
└── Time-Series-Clustering
├── spark-3.0.3-bin-hadoop2.7
└── time-series-clustering.ipynb
</code>
</pre>
