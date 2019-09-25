import os
import sys
import pandas as pd
import numpy as np
filename = sys.argv[1]
df = pd.read_csv(filename,encoding='big5',dtype={'成交日期' : str,
                                                 '商品代號' : str,
                                                 '到期月份(週別)' : str,
                                                 '成交時間' : int,
                                                 '成交價格' : float})
df['商品代號']=df['商品代號'].map(str.strip)
df['到期月份(週別)']=df['到期月份(週別)'].map(str.strip)
df = df[df['商品代號']=='TX']
df = df[df['成交時間']>=84500]
df = df[df['成交時間']<=134500]
df = df[df['到期月份(週別)'].map(len)==6]
mintime = (df['到期月份(週別)'].astype(np.int32).min())
df = df[df['到期月份(週別)'].astype(np.int32)==mintime]
try:
    op = df.loc[df['成交時間'].idxmin()]
    high = df.loc[df['成交價格'].idxmax()]
    low = df.loc[df['成交價格'].idxmin()]
    close = df[df['成交時間'] == df['成交時間'].max()]
    close = close.iloc[-1]
    print('{} {} {} {}'.format(int(op[4]), int(high[4]), int(low[4]), int(close[4])))
except:
    print('0 0 0 0')
