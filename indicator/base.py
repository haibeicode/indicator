# coding:utf-8
#
# Copyright 2019-2029 shenzhen haibei Media .Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Indicator Fundamental Function
@author Tab
"""

import math
import numpy as np
import pandas as pd


def IF(cond, v1, v2):
    """
    :param cond:
    :param v1:
    :param v2:
    :return:
    """
    var = np.where(cond, v1, v2)
    return pd.Series(var, index=v1.index)


def IFAND(cond1, cond2, v1, v2):
    """
    :param cond1:
    :param cond2:
    :param v1:
    :param v2:
    :return:
    """
    var = np.where(np.logical_and(cond1, cond2), v1, v2)
    return pd.Series(var, index=v1.index)


def IFOR(cond1, cond2, v1, v2):
    """
    :param cond1:
    :param cond2:
    :param v1:
    :param v2:
    :return:
    """
    var = np.where(np.logical_or(cond1, cond2), v1, v2)
    return pd.Series(var, index=v1.index)


def MAX(a, b):
    """
    :param a:
    :param b:
    :return:
    """
    return IF(a > b, a, b)


def MIN(a, b):
    """
    :param a:
    :param b:
    :return:
    """
    return IF(a < b, a, b)


def SINGLE_CROSS(a, b):
    """
    :param a:
    :param b:
    :return:
    """
    if a.iloc[-2] < b.iloc[-2] and a.iloc[-1] > b.iloc[-1]:
        return True
    else:
        return False


def XARROUND(x, y):
    """
    :param x:
    :param y:
    :return:
    """
    return np.round(y * (round(x / y - math.floor(x / y) + 0.00000000001) + math.floor(x / y)), 2)


def REF(series, n):
    """
    :param series:
    :param n:
    :return:
    """
    var = series.diff(n)
    return series - var


def LAST(cond, n1, n2):
    """
    表达持续性
    :param cond:
    :param n1:
    :param n2:
    :return:
    """
    n2 = 1 if n2 == 0 else n2
    assert n2 > 0
    assert n1 > n2
    return cond.iloc[-n1:-n2].all()


def MA(series, n):
    """
    :param series:
    :param n:
    :return:
    """
    return pd.Series.rolling(series, n).mean()


def EMA(series, n):
    """
    :param series:
    :param n:
    :return:
    """
    return pd.Series.ewm(series, span=n, min_periods=n - 1, adjust=True).mean()


def MEMA(series, n):
    """
    :param series:
    :param n:
    :return:
    """
    return pd.rolling_mean(series, span=n)


def SMA(series, n, m=1):
    """
    威廉SMA算法
    :param series:
    :param n:
    :param m:
    :return:
    """
    ret = []
    i = 1
    length = len(series)
    # 跳过X中前面几个 nan 值
    while i < length:
        if np.isnan(series.iloc[i]):
            i += 1
        else:
            break
    preY = series.iloc[i]  # Y'
    ret.append(preY)
    while i < length:
        Y = (m * series.iloc[i] + (n - m) * preY) / float(n)
        ret.append(Y)
        preY = Y
        i += 1
    return pd.Series(ret, index=series.tail(len(ret)).index)


def DIFF(series, n=1):
    """
    :param series:
    :param n:
    :return:
    """
    return pd.Series(series).diff(n)


def HHV(series, n):
    """
    :param series:
    :param n:
    :return:
    """
    return pd.Series(series).rolling(n).max()


def LLV(series, n):
    """
    :param series:
    :param n:
    :return:
    """
    return pd.Series(series).rolling(n).min()


def SUM(series, n):
    """
    :param series:
    :param n:
    :return:
    """
    return pd.Series.rolling(series, n).sum()


def ABS(series):
    """
    :param series:
    :return:
    """
    return abs(series)


def CROSS(a, b):
    """
    A上穿B B下穿A
    :param a:
    :param b:
    :return:
    """

    var = np.where(a < b, 1, 0)
    return (pd.Series(var, index=a.index).diff() < 0).apply(int)


def COUNT(cond, n):
    """
    :param cond:
    :param n:
    :return:
    """
    return pd.Series(np.where(cond, 1, 0), index=cond.index).rolling(n).sum()


def STD(series, n):
    """
    :param series:
    :param n:
    :return:
    """
    return pd.Series.rolling(series, n).std()


def AVEDEV(series, n):
    """
    平均绝对偏差
    :param series:
    :param n:
    :return:
    """
    return series.rolling(n).apply(lambda x: (np.abs(x - x.mean())).mean(), raw=True)


def MACD(series, fast, slow, mid):
    """
    函数名：MACD
    名称：平滑异同移动平均线

    简介：利用收盘价的短期（常用为12日）指数移动平均线与长期（常用为26日）指数移动平均线之间的聚合与分离状况，对买进、卖出时机作出研判的技术指标。

    分析和应用：
    [百度百科](https://baike.baidu.com/item/MACD%E6%8C%87%E6%A0%87?fromtitle=MACD&fromid=3334786)
    [维基百科](https://zh.wikipedia.org/wiki/MACD)
    [同花顺学院](http://www.iwencai.com/school/search?cg=100&w=MACD)
    :param series:
    :param fast:
    :param slow:
    :param mid:
    :return:
    """
    EMAFAST = EMA(series, fast)
    EMASLOW = EMA(series, slow)
    DIFF = EMAFAST - EMASLOW
    DEA = EMA(DIFF, mid)
    MACD = (DIFF - DEA) * 2

    return pd.DataFrame({'DIFF': DIFF, 'DEA': DEA, 'MACD': MACD})


def BBIBOLL(series, n1, n2, n3, n4, n, m):
    """
    多空布林线
    :param series:
    :param n1:
    :param n2:
    :param n3:
    :param n4:
    :param n:
    :param m:
    :return:
    """

    bbiboll = BBI(series, n1, n2, n3, n4)
    UPER = bbiboll + m * STD(bbiboll, n)
    DOWN = bbiboll - m * STD(bbiboll, n)
    return pd.DataFrame({'BBIBOLL': bbiboll, 'UPER': UPER, 'DOWN': DOWN})


def BBI(series, n1, n2, n3, n4):
    """
    多空指标
    :param series:
    :param n1:
    :param n2:
    :param n3:
    :param n4:
    :return:
    """

    bbi = (MA(series, n1) + MA(series, n2) +
           MA(series, n3) + MA(series, n4)) / 4
    return pd.DataFrame({'BBI': bbi})


def BARLAST(cond, yes=True):
    """
    :param cond:
    :param yes:
    :return:
    """
    if isinstance(cond.index, pd.MultiIndex):
        return len(cond) - cond.index.levels[0].tolist().index(cond[cond != yes].index[-1][0]) - 1
    elif isinstance(cond.index, pd.DatetimeIndex):
        return len(cond) - cond.index.tolist().index(cond[cond != yes].index[-1]) - 1


def RSTD(series, n=250, m=10):
    """
    :param series:
    :param n:
    :param m:
    :return:
    """
    return pd.rolling_std(series, span=n, min_periods=m)


def DMA(data_frame, M1=10, M2=50, M3=10):
    """
    平均线差 DMA
    :param data_frame:
    :param M1:
    :param M2:
    :param M3:
    :return:
    """
    CLOSE = data_frame['close']
    DDD = MA(CLOSE, M1) - MA(CLOSE, M2)
    AMA = MA(DDD, M3)
    return pd.DataFrame({
        'DDD': DDD, 'AMA': AMA
    })


def WINNER(series):
    """
    :param series:
    :return:
    """
    return


def DYNAINFO(series):
    """
    :param series:
    :return:
    """
    return


def CAPITAL():
    """
    :return:
    """
    return 1


def AMOUNT():
    """
    :param series:
    :return:
    """
    return 1


def INDEXC():
    """
    :return:
    """
    return 1


def ADVANCE():
    """
    :return:
    """
    return 1


def DECLINE():
    """
    :return:
    """
    return 1
