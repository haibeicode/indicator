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

import numpy as np
import pandas as pd


# 算术函数

def NOT(b):
    """
    取反
    :param b:
    :return:
    """
    if b == 0:
        return 1
    else:
        return 0


def IF(cond, a, b):
    """
    逻辑取值
    :param cond:
    :param a:
    :param b:
    :return:
    """
    return pd.Series(np.where(cond, a, b), index=a.index)


def IFAND(cond1, cond2, v1, v2):
    """
    逻辑和
    :param cond1:
    :param cond2:
    :param v1:
    :param v2:
    :return:
    """
    return pd.Series(np.where(np.logical_and(cond1, cond2), v1, v2), index=v1.index)


def MAX(a, b):
    """
    求最大值
    :param a:
    :param b:
    :return:
    """
    return IF(a > b, a, b)


def MIN(a, b):
    """
    求最小值
    :param a:
    :param b:
    :return:
    """
    return IF(a < b, a, b)


# 逻辑函数

def CROSS(a, b):
    """
    两条线交叉
    :param a:
    :param b:
    :return:
    """
    return (pd.Series(np.where(a < b, 1, 0), index=a.index).diff() < 0).apply(int)


def SMA(series, n, m=1):
    """
    移动平均
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


def MA(series, n):
    """
    简单移动平均
    :param series:
    :param n:
    :return:
    """
    return pd.Series.rolling(series, n).mean()


def EMA(series, n):
    """
    指数移动平均
    :param series:
    :param n:
    :return:
    """
    return pd.Series.ewm(series, span=n, min_periods=n - 1, adjust=True).mean()


def MEMA(series, n):
    """
    平滑移动平均
    :param series:
    :param n:
    :return:
    """
    return pd.rolling_mean(series, span=n)


def EXPMEMA(df, P1=5, P2=10, P3=20, P4=60):
    """
    指数平滑移动平均
    :param df:
    :param P1:
    :param P2:
    :param P3:
    :param P4:
    :return:
    """
    CLOSE = df['close']
    MA1 = MEMA(CLOSE, P1)
    MA2 = MEMA(CLOSE, P2)
    MA3 = MEMA(CLOSE, P3)
    MA4 = MEMA(CLOSE, P4)
    return pd.DataFrame({
        'MA1': MA1, 'MA2': MA2, 'MA3': MA3, 'MA4': MA4
    })


def HHV(series, n):
    """
    求最高值
    :param series:
    :param n:
    :return:
    """
    return pd.Series(series).rolling(n).max()


def LLV(series, n):
    """
    求最低值
    :param series:
    :param n:
    :return:
    """
    return pd.Series(series).rolling(n).min()


def SUM(series, n):
    """
    求总和
    :param series:
    :param n:
    :return:
    """
    return pd.Series.rolling(series, n).sum()


# 数学函数
def ABS(series):
    """
    求绝对值
    :param series:
    :return:
    """
    return abs(series)


def REF(series, n):
    """
    引用若干周期前的数据
    :param series:
    :param n:
    :return:
    """
    return series - series.diff(n)


def COUNT(cond, n):
    """
    统计满足条件的周期数
    :param cond:
    :param n:
    :return:
    """
    return pd.Series(np.where(cond, 1, 0), index=cond.index).rolling(n).sum()


def STD(series, n):
    """
    估算标准差
    :param series:
    :param n:
    :return:
    """
    return pd.Series.rolling(series, n).std()


# 统计函数
def AVEDEV(series, n):
    """
    平均绝对偏差
    :param series:
    :param n:
    :return:
    """
    return series.rolling(n).apply(lambda x: (np.abs(x - x.mean())).mean(), raw=True)


def DMA(df, M1=10, M2=50, M3=10):
    """
    平均线差 DMA
    :param df:
    :param M1:
    :param M2:
    :param M3:
    :return:
    """
    CLOSE = df['close']
    DDD = MA(CLOSE, M1) - MA(CLOSE, M2)
    AMA = MA(DDD, M3)
    return pd.DataFrame({
        'DDD': DDD, 'AMA': AMA
    })

# def HSL(df, N=5):
#     """
#     换手线
#     :param df:
#     :param N:
#     :return:
#     """
#
#     VOL = df['volume']
#     HSL = IF((SETCODE == 0 or SETCODE == 1), 100 * VOL, VOL) / (FINANCE(7) / 100)
#     MAHSL = MA(HSL, N)
#     return pd.DataFrame({
#         'HSL': HSL, 'MAHSL': MAHSL
#     })
