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


def IF(logic, a, b):
    """
    逻辑取值
    :param logic:
    :param a:
    :param b:
    :return:
    """
    if type(a) == int:
        return pd.Series(np.where(logic, a, b))
    else:
        return pd.Series(np.where(logic, a, b), index=a.index)


def IFAND(logic1, logic2, a, b):
    """
    逻辑和
    :param logic1:
    :param logic2:
    :param a:
    :param b:
    :return:
    """
    return pd.Series(np.where(np.logical_and(logic1, logic2), a, b), index=a.index)


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


def SUM(series, n=2):
    """
    求总和
    :param series:
    :param n:
    :return:
    """
    return pd.Series.rolling(series, n).sum()


def COUNT(logic, n=2):
    """
    统计满足条件的周期数
    :param logic:
    :param n:
    :return:
    """
    return pd.Series(np.where(logic, 1, 0), index=logic.index).rolling(n).sum()


def STD(series, n=2):
    """
    估算标准差
    :param series:
    :param n:
    :return:
    """
    return pd.Series.rolling(series, n).std()


def ABS(series):
    """
    求绝对值
    :param series:
    :return:
    """
    return abs(series)


def AVEDEV(series, n=2):
    """
    平均绝对偏差
    :param series:
    :param n:
    :return:
    """
    return series.rolling(n).apply(lambda x: (np.abs(x - x.mean())).mean(), raw=True)


def CROSS(a, b):
    """
    两条线交叉
    :param a:
    :param b:
    :return:
    """
    if type(a) == int:
        return (pd.Series(np.where(a < b, 1, 0)).diff() < 0).apply(int)
    else:
        return (pd.Series(np.where(a < b, 1, 0), index=a.index).diff() < 0).apply(int)


def MA(series, n=2):
    """
    简单移动平均
    :param series:
    :param n:
    :return:
    """
    return pd.Series.rolling(series, n).mean()


def SMA(series, n=2, m=1):
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
    while i < length:
        if np.isnan(series.iloc[i]):
            i += 1
        else:
            break
    preY = series.iloc[i]
    ret.append(preY)
    while i < length:
        Y = (m * series.iloc[i] + (n - m) * preY) / float(n)
        ret.append(Y)
        preY = Y
        i += 1
    return pd.Series(ret, index=series.tail(len(ret)).index)


def EMA(series, n=2):
    """
    指数移动平均
    :param series:
    :param n:
    :return:
    """
    return pd.Series.ewm(series, span=n, min_periods=n - 1, adjust=True).mean()


def HHV(series, n=2):
    """
    求最高值
    :param series:
    :param n:
    :return:
    """
    return pd.Series(series).rolling(n).max()


def LLV(series, n=2):
    """
    求最低值
    :param series:
    :param n:
    :return:
    """
    return pd.Series(series).rolling(n).min()


def REF(series, n=2):
    """
    引用若干周期前的数据
    :param series:
    :param n:
    :return:
    """
    return series - series.diff(n)


def lower_shadow(df):
    """
    下影线
    :param df:
    :return:
    """
    return abs(df['low'] - MIN(df['open'], df['close']))


def upper_shadow(df):
    """
    上影线
    :param df:
    :return:
    """
    return abs(df['high'] - MAX(df['open'], df['close']))


def body_abs(df):
    """
    波动绝对值
    :param df:
    :return:
    """
    return abs(df['open'] - df['close'])


def body(df):
    """
    波动
    :param df:
    :return:
    """
    return df['close'] - df['open']


def price_pcg(df):
    """

    :param df:
    :return:
    """
    return body(df) / df['open']


# def amplitude(df):
#     """
#     振幅
#     :param df:
#     :return:
#     """
#     return (df['high'] - df['low']) / df['low']
#
# def MEMA(series, n):
#     """
#     改良平滑移动平均
#     :param series:
#     :param n:
#     :return:
#     """
#     return pd.Series.ewma(series, span=n)
