import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np

import yfinance as yf

import utils

# 산타랠리 윈도우 설정
## 산타랠리 : 연말장 종료 5영업일 ~ 연초장 2영업일(총 7영업일)
## before : 산타랠리 직전 7영업일
## after : 산타랠리 직후 7영업일
def create_period_event(
    _df, 
    col_event = 'event', 
    col_year = '귀속년도',
    values = ['santa', 'before', 'after'],
    values_default = '',
    len_dec = 5,
    len_jan = 2
):
    len_event = len_dec + len_jan
    
    df = _df.copy()
    df[col_event] = values_default

    years = df.index.year.unique()
    df[col_year] = df.index.year

    for year in years:
        year = str(year)
        if year+'-12' in df.index:
            # 산타랠리 기간
            df.loc[year+'-12', col_event].iloc[-len_dec:] = values[0]

            # 산타랠리 전 기간
            df.loc[year+'-12', col_event].iloc[-len_event-len_dec:-len_dec] = values[1] # before

        if year+'-01' in df.index:
            # 산타랠리 기간
            df.loc[year+'-01', col_event].iloc[:len_dec] = values[0]
            df.loc[year+'-01', col_year].iloc[:len_dec] = int(year)-1

            # 산타랠리 후 기간
            df.loc[year+'-01', col_event].iloc[len_jan:len_jan + len_event] = values[2] # after
            df.loc[year+'-01', col_year].iloc[len_jan:len_jan + len_event] = int(year)-1

    return df

# 경기 국면 설정
## KOSPI 수익률 > 정기예금금리 : 상승기
## KOSPI 수익률 < 정기예금금리 : 하락기
def create_period_economy(_df, col_economy = 'economy'):
    df = _df.copy()
    return df

def get_data(symbol='^KS11'):
    # symbol : default=코스피
    data = utils.create_rtn(
        _df = utils.load_ohlcv(symbol),
        col_rtn = 'rtn'
    )

    data = create_period_event(data, values_default='else')
    # data = create_period_economy(data)

    return data