import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np

import yfinance as yf

# ohlcv 데이터 수집 및 전처리
def load_ohlcv(symbol, drop=False, col_price='Adj Close'):
    # ohlcv 데이터 수집 (전체 기간)
    df = yf.download(symbol)

    # 결측치 처리 : 이전 값으로 채우고 제거
    df = df.fillna(method='ffill').dropna()

    if drop:
        return df[[col_price]] # price 컬럼만 남기고 모두 제거
    return df

# 일일 수익률 계산
def create_rtn(
    _df, 
    col_price='Adj Close', 
    col_rtn='Daily Returns'
):
    df = _df.copy()
    if col_price not in df.columns:
        col_price = df.columns[0] # 첫번째 열로 수익률 계산
    df[col_rtn] = df[col_price].pct_change() * 100
    df = df.dropna()
    return df

# cagr 계산
def calc_cagr(
    _df, 
    col_price = 'Adj Close',
    rtn_days=1,
    col_cagr='cagr',
):
    df = _df.copy()

    col_rtn = 'rtn_'+str(rtn_days)
    df[col_rtn] = df[col_price]/(df[col_price].shift(rtn_days))
    df = df.dropna()
    df[col_rtn] -= 1
    
    df[col_cagr] = ((1+df[col_rtn])**(365/rtn_days) - 1)*100
    # df[col_cagr] = (1+df[col_rtn])**(365/rtn_days) - 1
    df = df.dropna()
    return df

# 데이터 기간 설정
def filter_date(df, date_start, date_end):
    if type(df.index)==pd.DatetimeIndex:
        return df.loc[date_start:date_end]
    else:
        print("인덱스를 날짜로 설정 후 다시 실행해주세요")

# 데이터 기간 설정
def filter_range(df, col, range_start=None, range_end=None):
    if range_start is None:
        range_start = min(df[col])
    if range_end is None:
        range_end = max(df[col])
    return df[(range_start<=df[col]) & (df[col]<=range_end)]