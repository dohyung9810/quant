import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import platform
if platform.system() == 'Darwin': # MAC
    plt.rc('font', family='AppleGothic')
else: # Windows
    plt.rc('font', family='Malgun Gothic')

import pandas as pd
import numpy as np
import FinanceDataReader as fdr

def create_rtn_by_ticker(
    ticker,
    _start=None,
    _end='2023-01-15',
    _roll_buy = 5,
    _roll_sell = 2
):
    df = fdr.DataReader(ticker, _start, _end)
    df['year'] = df.index.year

    df['Buy'] = df['Open'].shift(_roll_buy-1) # 연말장 종료 (_roll_buy)일전 Open
    df['Sell'] = df['Close'].shift(-_roll_sell) # 연초 (_roll_sell) 영업일 Close

    # 연말장 종료일 기준 수익률 계산
    df_change = df[df['year'] != df['year'].shift(-1)][:-1] # 연말 데이터 추출
    df_change.set_index('year', inplace=True)
    df_change['rtn'] = df_change['Sell'] / df_change['Buy']
    df_change['rtn(%)'] = (df_change['rtn']-1)*100 # %
    df_change = df_change[['Buy', 'Sell', 'rtn', 'rtn(%)']]

    # inf 제거
    df_change = df_change[~df_change.isin([np.inf]).any(axis=1)]

    # 시각화
    colors = list(map(lambda x: 'red' if x > 0 else 'blue', df_change['rtn(%)']))

    fig, ax1 = plt.subplots()

    ax1.set_xlabel('year')
    ax1.set_ylabel('rtn(%)')
    ax1.bar(df_change.index, df_change['rtn(%)'], color=colors)
    ax1.tick_params(axis='y')

    ax2 = ax1.twinx()
    ax2.set_ylabel('price')  # Sell(close)
    ax2.plot(df_change.index, df_change['Sell'], color='green', linestyle='--', label='price(sell)')
    ax2.plot(df_change.index, df_change['Buy'], color='orange', linestyle='--', label='price(buy)')
    ax2.tick_params(axis='y')

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.title(f'종목명:{ticker}, 누적수익률:{np.round(df_change['rtn'].cumprod().iloc[-1], 4)}')
    plt.legend()
    plt.show()

    return df_change