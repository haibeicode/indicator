from indicator.base import *
import tushare as ts

data = ts.get_hist_data('600848')
CLOSE = data['close']


SHORT=12
LONG=2
MID=9
DIF=EMA(CLOSE,SHORT)-EMA(CLOSE,LONG)
DEA=EMA(DIF,MID)
MACD=(DIF-DEA)*2



import pandas as pd

madc = pd.DataFrame()

madc['DIF'] = DIF
madc['DEA'] = DEA
madc['MACD'] = MACD
# MADC = {"DIF":DIF,"DEA":DEA,"MACD":MACD}

print(madc)