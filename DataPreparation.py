# Important packages
import pandas as pd
import numpy as np
import ta
from scipy.stats import linregress
import sys

currency = str(sys.argv[1])

try:
    print("starting preparing df now ...")
    # Load the raw data
    df = pd.read_csv('./FX_Data/' + currency + '.csv', names=['date','open','high','low','close'])
    df.dropna(inplace=True)

    # adding delta
    for i in range(len(df)-1):
        if df.at[i+1,'close'] > df.at[i,'close']:
            df.at[i,'delta'] = 1
        else:
            df.at[i,'delta'] = 0

    # technical analysis features
    def add_slope(i):
        for j in range(i - 1, len(df)):
            a = df['high'][j - (i - 1):j + 1]
            b = []
            for k in range(i):
                b.append(k)
            name = 'slope_%s' % (i)
            df.at[j, name] = linregress(a, b).slope

    def add_SO(i):
        ind_SO = ta.momentum.StochasticOscillator(high=df['high'],low=df['low'],close=df['close'],n=i)
        name = 'so_%s' %(i)
        df[name] = ind_SO.stoch()
        return

    def add_WR(i):
        ind_WR = ta.momentum.WilliamsRIndicator(high=df['high'],low=df['low'],close=df['close'],lbp=i)
        name = 'wr_%s' %(i)
        df[name] = ind_WR.wr()
        return

    def add_ROC(i):
        ind_ROC = ta.momentum.ROCIndicator(close=df['close'],n=i)
        name = 'roc_%s' %(i)
        df[name] = ind_ROC.roc()
        return

    def add_WCP(i):
        ind_WCP = ta.trend.EMAIndicator(close=df['wclose'],n=i)
        name = 'wcp_%s' %(i)
        df[name] = ind_WCP.ema_indicator()
        return

    def add_MACD(i,j):
        ind_MACD = ta.trend.MACD(close=df['close'],n_fast=i,n_slow=j)
        name ='macd_%s_%s' %(i,j)
        df[name] = ind_MACD.macd()
        return

    def add_CCI(i):
        ind_CCI = ta.trend.cci(high=df['high'],low=df['low'],close=df['close'],n=i)
        name = 'cci_%s' %(i)
        df[name] = ind_CCI
        return

    # process data
    for i in [3, 4, 5, 10, 20, 30]:
        add_slope(i)

    df['wclose'] = (df['close']*2+df['high']+df['low'])/4

    for i in [3,4,5,8,9,10]:
        add_SO(i)

    for i in [6,7,8,9,10]:
        add_WR(i)

    for i in [12,13,14,15]:
        add_ROC(i)

    add_WCP(15)
    add_MACD(15,30)
    add_CCI(15)

    # signal processing features
    for i in range(1,len(df)):
        df.at[i,'hi_avg_2'] =  (df.at[i-1,'high'] + df.at[i,'high'])/2
        df.at[i,'lo_avg_2'] =  (df.at[i-1,'low'] + df.at[i,'low'])/2
        df.at[i,'hilo_avg_2'] = (df.at[i,'hi_avg_2'] + df.at[i,'lo_avg_2'])/2
        df.at[i,'hilo_avg'] = (df.at[i,'high'] + df.at[i,'low'])/2

    df.dropna(inplace=True)
    df.to_parquet('./Dataframes/df_'+currency+'.parquet.gzip',compression='gzip')

    print("successfully prepared df and saved. quitting now.")
except:
    print("error happened while preparing for data. quitting now.")
