import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 연령별 성별인구
def age():
    age_pop = pd.read_csv('./202103_202106_연령별인구현황_월간.csv', encoding = 'cp949', thousands = ',')
    age_pop.drop(age_pop[age_pop['2021년03월_계_총인구수'] == 0].index, inplace = True)
    new_age_pop = pd.DataFrame()
    new_age_pop['행정구역'] = age_pop['행정구역'].apply(lambda x: x[:-13])

    new_age_pop['행정구역코드'] = age_pop['행정구역'].apply(lambda x: x[-11:-1])

    new_age_pop['2103 총인구수'] = age_pop['2021년03월_계_총인구수']
    new_age_pop['2104 총인구수'] = age_pop['2021년04월_계_총인구수']
    new_age_pop['2105 총인구수'] = age_pop['2021년05월_계_총인구수']
    new_age_pop['2106 총인구수'] = age_pop['2021년06월_계_총인구수']

    new_age_pop['2103 10대 미만 비율'] = age_pop.apply(lambda x: round(x['2021년03월_계_0~9세'] / x['2021년03월_계_총인구수'], 4), axis = 1)
    new_age_pop['2104 10대 미만 비율'] = age_pop.apply(lambda x: round(x['2021년04월_계_0~9세'] / x['2021년04월_계_총인구수'], 4), axis = 1)
    new_age_pop['2105 10대 미만 비율'] = age_pop.apply(lambda x: round(x['2021년05월_계_0~9세'] / x['2021년05월_계_총인구수'], 4), axis = 1)
    new_age_pop['2106 10대 미만 비율'] = age_pop.apply(lambda x: round(x['2021년06월_계_0~9세'] / x['2021년06월_계_총인구수'], 4), axis = 1)

    new_age_pop['2103 10대 비율'] = age_pop.apply(lambda x: round(x['2021년03월_계_10~19세'] / x['2021년03월_계_총인구수'], 4), axis = 1)
    new_age_pop['2104 10대 비율'] = age_pop.apply(lambda x: round(x['2021년04월_계_10~19세'] / x['2021년04월_계_총인구수'], 4), axis = 1)
    new_age_pop['2105 10대 비율'] = age_pop.apply(lambda x: round(x['2021년05월_계_10~19세'] / x['2021년05월_계_총인구수'], 4), axis = 1)
    new_age_pop['2106 10대 비율'] = age_pop.apply(lambda x: round(x['2021년06월_계_10~19세'] / x['2021년06월_계_총인구수'], 4), axis = 1)

    new_age_pop['2103 20대 비율'] = age_pop.apply(lambda x: round(x['2021년03월_계_20~29세'] / x['2021년03월_계_총인구수'], 4), axis = 1)
    new_age_pop['2104 20대 비율'] = age_pop.apply(lambda x: round(x['2021년04월_계_20~29세'] / x['2021년04월_계_총인구수'], 4), axis = 1)
    new_age_pop['2105 20대 비율'] = age_pop.apply(lambda x: round(x['2021년05월_계_20~29세'] / x['2021년05월_계_총인구수'], 4), axis = 1)
    new_age_pop['2106 20대 비율'] = age_pop.apply(lambda x: round(x['2021년06월_계_20~29세'] / x['2021년06월_계_총인구수'], 4), axis = 1)

    new_age_pop['2103 30대 비율'] = age_pop.apply(lambda x: round(x['2021년03월_계_30~39세'] / x['2021년03월_계_총인구수'], 4), axis = 1)
    new_age_pop['2104 30대 비율'] = age_pop.apply(lambda x: round(x['2021년04월_계_30~39세'] / x['2021년04월_계_총인구수'], 4), axis = 1)
    new_age_pop['2105 30대 비율'] = age_pop.apply(lambda x: round(x['2021년05월_계_30~39세'] / x['2021년05월_계_총인구수'], 4), axis = 1)
    new_age_pop['2106 30대 비율'] = age_pop.apply(lambda x: round(x['2021년06월_계_30~39세'] / x['2021년06월_계_총인구수'], 4), axis = 1)

    new_age_pop['2103 40대 비율'] = age_pop.apply(lambda x: round(x['2021년03월_계_40~49세'] / x['2021년03월_계_총인구수'], 4), axis = 1)
    new_age_pop['2104 40대 비율'] = age_pop.apply(lambda x: round(x['2021년04월_계_40~49세'] / x['2021년04월_계_총인구수'], 4), axis = 1)
    new_age_pop['2105 40대 비율'] = age_pop.apply(lambda x: round(x['2021년05월_계_40~49세'] / x['2021년05월_계_총인구수'], 4), axis = 1)
    new_age_pop['2106 40대 비율'] = age_pop.apply(lambda x: round(x['2021년06월_계_40~49세'] / x['2021년06월_계_총인구수'], 4), axis = 1)

    new_age_pop['2103 50대 비율'] = age_pop.apply(lambda x: round(x['2021년03월_계_50~59세'] / x['2021년03월_계_총인구수'], 4), axis = 1)
    new_age_pop['2104 50대 비율'] = age_pop.apply(lambda x: round(x['2021년04월_계_50~59세'] / x['2021년04월_계_총인구수'], 4), axis = 1)
    new_age_pop['2105 50대 비율'] = age_pop.apply(lambda x: round(x['2021년05월_계_50~59세'] / x['2021년05월_계_총인구수'], 4), axis = 1)
    new_age_pop['2106 50대 비율'] = age_pop.apply(lambda x: round(x['2021년06월_계_50~59세'] / x['2021년06월_계_총인구수'], 4), axis = 1)

    new_age_pop['2103 60대 비율'] = age_pop.apply(lambda x: round(x['2021년03월_계_60~69세'] / x['2021년03월_계_총인구수'], 4), axis = 1)
    new_age_pop['2104 60대 비율'] = age_pop.apply(lambda x: round(x['2021년04월_계_60~69세'] / x['2021년04월_계_총인구수'], 4), axis = 1)
    new_age_pop['2105 60대 비율'] = age_pop.apply(lambda x: round(x['2021년05월_계_60~69세'] / x['2021년05월_계_총인구수'], 4), axis = 1)
    new_age_pop['2106 60대 비율'] = age_pop.apply(lambda x: round(x['2021년06월_계_60~69세'] / x['2021년06월_계_총인구수'], 4), axis = 1)

    new_age_pop['2103 70대 비율'] = age_pop.apply(lambda x: round(x['2021년03월_계_70~79세'] / x['2021년03월_계_총인구수'], 4), axis = 1)
    new_age_pop['2104 70대 비율'] = age_pop.apply(lambda x: round(x['2021년04월_계_70~79세'] / x['2021년04월_계_총인구수'], 4), axis = 1)
    new_age_pop['2105 70대 비율'] = age_pop.apply(lambda x: round(x['2021년05월_계_70~79세'] / x['2021년05월_계_총인구수'], 4), axis = 1)
    new_age_pop['2106 70대 비율'] = age_pop.apply(lambda x: round(x['2021년06월_계_70~79세'] / x['2021년06월_계_총인구수'], 4), axis = 1)

    new_age_pop['2103 80대 비율'] = age_pop.apply(lambda x: round(x['2021년03월_계_80~89세'] / x['2021년03월_계_총인구수'], 4), axis = 1)
    new_age_pop['2104 80대 비율'] = age_pop.apply(lambda x: round(x['2021년04월_계_80~89세'] / x['2021년04월_계_총인구수'], 4), axis = 1)
    new_age_pop['2105 80대 비율'] = age_pop.apply(lambda x: round(x['2021년05월_계_80~89세'] / x['2021년05월_계_총인구수'], 4), axis = 1)
    new_age_pop['2106 80대 비율'] = age_pop.apply(lambda x: round(x['2021년06월_계_80~89세'] / x['2021년06월_계_총인구수'], 4), axis = 1)

    new_age_pop['2103 90대 비율'] = age_pop.apply(lambda x: round(x['2021년03월_계_90~99세'] / x['2021년03월_계_총인구수'], 4), axis = 1)
    new_age_pop['2104 90대 비율'] = age_pop.apply(lambda x: round(x['2021년04월_계_90~99세'] / x['2021년04월_계_총인구수'], 4), axis = 1)
    new_age_pop['2105 90대 비율'] = age_pop.apply(lambda x: round(x['2021년05월_계_90~99세'] / x['2021년05월_계_총인구수'], 4), axis = 1)
    new_age_pop['2106 90대 비율'] = age_pop.apply(lambda x: round(x['2021년06월_계_90~99세'] / x['2021년06월_계_총인구수'], 4), axis = 1)

    new_age_pop['2103 90대 초과 비율'] = age_pop.apply(lambda x: round(x['2021년03월_계_100세 이상'] / x['2021년03월_계_총인구수'], 4), axis = 1)
    new_age_pop['2104 90대 초과 비율'] = age_pop.apply(lambda x: round(x['2021년04월_계_100세 이상'] / x['2021년04월_계_총인구수'], 4), axis = 1)
    new_age_pop['2105 90대 초과 비율'] = age_pop.apply(lambda x: round(x['2021년05월_계_100세 이상'] / x['2021년05월_계_총인구수'], 4), axis = 1)
    new_age_pop['2106 90대 초과 비율'] = age_pop.apply(lambda x: round(x['2021년06월_계_100세 이상'] / x['2021년06월_계_총인구수'], 4), axis = 1)


    new_age_pop['2103 남성 비율'] = age_pop.apply(lambda x: round(x['2021년03월_남_총인구수'] / x['2021년03월_계_총인구수'], 4), axis = 1)
    new_age_pop['2104 남성 비율'] = age_pop.apply(lambda x: round(x['2021년04월_남_총인구수'] / x['2021년04월_계_총인구수'], 4), axis = 1)
    new_age_pop['2105 남성 비율'] = age_pop.apply(lambda x: round(x['2021년05월_남_총인구수'] / x['2021년05월_계_총인구수'], 4), axis = 1)
    new_age_pop['2106 남성 비율'] = age_pop.apply(lambda x: round(x['2021년06월_남_총인구수'] / x['2021년06월_계_총인구수'], 4), axis = 1)

    new_age_pop['2103 여성 비율'] = age_pop.apply(lambda x: round(x['2021년03월_여_총인구수'] / x['2021년03월_계_총인구수'], 4), axis = 1)
    new_age_pop['2104 여성 비율'] = age_pop.apply(lambda x: round(x['2021년04월_여_총인구수'] / x['2021년04월_계_총인구수'], 4), axis = 1)
    new_age_pop['2105 여성 비율'] = age_pop.apply(lambda x: round(x['2021년05월_여_총인구수'] / x['2021년05월_계_총인구수'], 4), axis = 1)
    new_age_pop['2106 여성 비율'] = age_pop.apply(lambda x: round(x['2021년06월_여_총인구수'] / x['2021년06월_계_총인구수'], 4), axis = 1)

    new_age_pop.to_csv('./외부 데이터/외부 데이터 전처리/연령별_성별_인구_전처리_1026.csv', encoding = 'utf-8', index = False)
    
    
    
# 세대원수별 세대수

    
def household():
    household = pd.read_csv('./202103_202106_주민등록인구기타현황(세대원수별 세대수)_households.csv', encoding = 'cp949', thousands = ',')
    new_household = pd.DataFrame()
    new_household['행정구역'] = household['행정구역'].apply(lambda x: x[:-13])

    new_household['행정구역코드'] = household['행정구역'].apply(lambda x: x[-11:-1])

    new_household['2103 전체세대'] = household['2021년03월_전체세대']
    new_household['2104 전체세대'] = household['2021년03월_전체세대']
    new_household['2105 전체세대'] = household['2021년05월_전체세대']
    new_household['2106 전체세대'] = household['2021년06월_전체세대']

    new_household['2103 1인세대 비율'] = household.apply(lambda x: round(x['2021년03월_1인세대'] / x['2021년03월_전체세대'], 4), axis = 1)
    new_household['2104 1인세대 비율'] = household.apply(lambda x: round(x['2021년04월_1인세대'] / x['2021년04월_전체세대'], 4), axis = 1)
    new_household['2105 1인세대 비율'] = household.apply(lambda x: round(x['2021년05월_1인세대'] / x['2021년05월_전체세대'], 4), axis = 1)
    new_household['2106 1인세대 비율'] = household.apply(lambda x: round(x['2021년06월_1인세대'] / x['2021년06월_전체세대'], 4), axis = 1)

    new_household['2103 2인세대 비율'] = household.apply(lambda x: round(x['2021년03월_2인세대'] / x['2021년03월_전체세대'], 4), axis = 1)
    new_household['2104 2인세대 비율'] = household.apply(lambda x: round(x['2021년04월_2인세대'] / x['2021년04월_전체세대'], 4), axis = 1)
    new_household['2105 2인세대 비율'] = household.apply(lambda x: round(x['2021년05월_2인세대'] / x['2021년05월_전체세대'], 4), axis = 1)
    new_household['2106 2인세대 비율'] = household.apply(lambda x: round(x['2021년06월_2인세대'] / x['2021년06월_전체세대'], 4), axis = 1)

    new_household['2103 3인세대 비율'] = household.apply(lambda x: round(x['2021년03월_3인세대'] / x['2021년03월_전체세대'], 4), axis = 1)
    new_household['2104 3인세대 비율'] = household.apply(lambda x: round(x['2021년04월_3인세대'] / x['2021년04월_전체세대'], 4), axis = 1)
    new_household['2105 3인세대 비율'] = household.apply(lambda x: round(x['2021년05월_3인세대'] / x['2021년05월_전체세대'], 4), axis = 1)
    new_household['2106 3인세대 비율'] = household.apply(lambda x: round(x['2021년06월_3인세대'] / x['2021년06월_전체세대'], 4), axis = 1)

    new_household['2103 4인세대 비율'] = household.apply(lambda x: round(x['2021년03월_4인세대'] / x['2021년03월_전체세대'], 4), axis = 1)
    new_household['2104 4인세대 비율'] = household.apply(lambda x: round(x['2021년04월_4인세대'] / x['2021년04월_전체세대'], 4), axis = 1)
    new_household['2105 4인세대 비율'] = household.apply(lambda x: round(x['2021년05월_4인세대'] / x['2021년05월_전체세대'], 4), axis = 1)
    new_household['2106 4인세대 비율'] = household.apply(lambda x: round(x['2021년06월_4인세대'] / x['2021년06월_전체세대'], 4), axis = 1)

    new_household['2103 5인이상세대 비율'] = new_household.apply(lambda x: (1 - x['2103 1인세대 비율'] - x['2103 2인세대 비율'] - x['2103 3인세대 비율'] - x['2103 4인세대 비율']), axis = 1)
    new_household['2104 5인이상세대 비율'] = new_household.apply(lambda x: (1 - x['2104 1인세대 비율'] - x['2104 2인세대 비율'] - x['2104 3인세대 비율'] - x['2104 4인세대 비율']), axis = 1)
    new_household['2105 5인이상세대 비율'] = new_household.apply(lambda x: (1 - x['2105 1인세대 비율'] - x['2105 2인세대 비율'] - x['2105 3인세대 비율'] - x['2105 4인세대 비율']), axis = 1)
    new_household['2106 5인이상세대 비율'] = new_household.apply(lambda x: (1 - x['2106 1인세대 비율'] - x['2106 2인세대 비율'] - x['2106 3인세대 비율'] - x['2106 4인세대 비율']), axis = 1)
        
    new_household.to_csv('./세대원수별 세대수 전처리.csv', encoding = 'utf-8', index = False)
    
    
    
    