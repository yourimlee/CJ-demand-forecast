# CJ 미래기술 챌린지 (최우수상 수상)

#### 시계열 클러스터링과 머신러닝(ML)을 활용한 상품/물량 수요 예측

## Participants
**연세대학교 산업공학과**  
이유림, 김연재, 윤수진, 석민정

## Significance
**시계열적 수요 패턴을 파악하여 각 품목별 수요 특징을 찾아내고, 다양한 내외부 변수를 활용하여 수요 예측의 정확도를 높이는 것**

- 기존 수요 예측과는 다르게 심리 변수, 외부 변수를 사용
	- 심리 변수는 하루 전, 이틀 전, 삼일 전의 수요를 통해 사람들의 소비 심리를 입력 변수로 사용하였고 유행에 따라 상품을 소비하는 현상, 밴드웨건 효과를 모델에 반영

	- 외부 데이터로 휴일여부/요일, 세대원수 별 세대수, 성별/연령대별 인구 수를 활용하여 지역별 특성을 반영

- 창고 관리자에게 제공할 창고 내 품목에 대한 수요 예측 뿐만 아니라 고객사 코드별 수요 예측을 통해 고객사에게 제공할 정보를 구축

- 다양한 모델을 앙상블하여 모델의 정확도를 높이고자 함
	- XGB, LGBM, SVR, GBR, ABR 5개의 모델을 사용하여 수요 예측을 시행
	- 단일 모델에서의 MAE가 작은 3가지 모델을 stacking 모델에 활용
	- 단일 모델과 stacking 모델의 MAE 값을 비교하여 작은 값으로 모델링 결과를 반환, 정확도 높은 예측을 보임
- 시계열 클러스터링을 통해 품목별 수요 패턴을 구분
	- 수요 주기와 수요 패턴이 다른 품목들을 시계열 클러스터링을 통해 군집화
	- 각 품목의 수요 패턴에 적합한 재고 관리, 생산 관리 전략을 세움
	- 수요 주기, 패턴 정보를 모델의 입력 변수로 활용해 예측의 정확도를 높임

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

## Data
- __내부 데이터__
	- CJ 대한통운에서 제공한 '이커머스 FC 주문 데이터 2021.03 ~ 2021.06'
- __외부 데이터__
	- 휴일 여부 / 요일
	- 지역별 월별 가구원수 비율, 성별 연령 비율 (2021년 기준)

## Result
### Clustering
<img width="1007" alt="스크린샷 2022-03-03 오후 11 13 20" src="https://user-images.githubusercontent.com/67430267/156581875-55679665-97ae-4b84-9135-52eabfb326eb.png">

__뚜렷한 수요 주기의 차이__
-  **1번 클러스터**
	- 급진적인 수요 변동을 볼 수 있으며 갑작스럽게 수요가 증가했다가 다시 감소하는 것을 보아 유행성 제품으로 판단
-  **8번 클러스터**
	- 꾸준한 수요가 보이는 것을 보아 생필품과 같은 비유행성 제품으로 판단
-  **3번 클러스터**
	- 이전까지의 수요가 0에 수렴하다가 갑작스럽게 6월 말에 급증한 제품으로, 신상품 혹은 새롭게 주문을 다루게 된 제품으로 판단

---
### Modeling
모델링은 크게 4가지 **(고객사별, 클러스터별, 품목별, 지역별)** 로 나누어 진행

<img width="634" alt="KakaoTalk_Photo_2022-03-03-23-00-37" src="https://user-images.githubusercontent.com/67430267/156579621-ccf4d0d5-115e-4d41-832e-321dda194170.png">

- 위 그림은 학습된 모델의 예측값 일부만을 나타내었다
- 좌측은 **고객사별**, 우측은 **지역별**로의 모델링 결과이다
- 주황색이 **실제값**, 초록색이 **예측값**을 나타낸다

****

### Dashboard
__Tableau를 이용하여 대시보드에 들어갈 그래프를 생성하고, 대시보드의 형태로 활용 방안 제시__

**Customer Dashboard**

<img width="563" alt="스크린샷 2022-03-03 오후 11 29 04" src="https://user-images.githubusercontent.com/67430267/156584774-aa7cd23e-151b-4e13-8de3-cd45fff857f0.png">

-	전체 대비 해당 고객사의 판매 점유율
-	고객사의 주차별 인기 품목과 수요 패턴 분석
-	대표 품목의 판매량과 주차별 현황 및 예측
-	고객사 전체 판매량의 주차별 예측
-	주별 판매 수량 및 증가율 히스토리

__Manager Dashboard__

<img width="569" alt="스크린샷 2022-03-03 오후 11 30 27" src="https://user-images.githubusercontent.com/67430267/156585011-fb62e4ff-bad4-45d6-852c-b2a6ce838363.png">

-	풀필먼트 센터의 수요 패턴별 품목 분포 현황
-	수요 패턴별 수요 예측 정보
-	풀필먼트 센터 – 배송지 별 배송량 현황
-	주차별 배송량 예측을 통한 배차 관리
