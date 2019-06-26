# coding:utf-8

import math
import numpy as np
import pandas as pd
import talib

"""
基础函数
"""


def EMA(Series, N):
    return pd.Series.ewm(Series, span=N, min_periods=N - 1, adjust=True).mean()


def MEMA(Series, N):
    return pd.rolling_mean(Series, span=N)


def MA(Series, N):
    return pd.Series.rolling(Series, N).mean()


# 威廉SMA  参考https://www.joinquant.com/post/867


def SMA(Series, N, M=1):
    """
    威廉SMA算法

    本次修正主要是对于返回值的优化,现在的返回值会带上原先输入的索引index
    2018/5/3
    @yutiansut
    """
    ret = []
    i = 1
    length = len(Series)
    # 跳过X中前面几个 nan 值
    while i < length:
        if np.isnan(Series.iloc[i]):
            i += 1
        else:
            break
    preY = Series.iloc[i]  # Y'
    ret.append(preY)
    while i < length:
        Y = (M * Series.iloc[i] + (N - M) * preY) / float(N)
        ret.append(Y)
        preY = Y
        i += 1
    return pd.Series(ret, index=Series.tail(len(ret)).index)


def DIFF(Series, N=1):
    return pd.Series(Series).diff(N)


def HHV(Series, N):
    return pd.Series(Series).rolling(N).max()


def LLV(Series, N):
    return pd.Series(Series).rolling(N).min()


def SUM(Series, N):
    return pd.Series.rolling(Series, N).sum()


def ABS(Series):
    return abs(Series)


def MAX(A, B):
    var = IF(A > B, A, B)
    return var


def MIN(A, B):
    var = IF(A < B, A, B)
    return var


def SINGLE_CROSS(A, B):
    if A.iloc[-2] < B.iloc[-2] and A.iloc[-1] > B.iloc[-1]:
        return True
    else:
        return False


def CROSS(A, B):
    """A<B then A>B  A上穿B B下穿A

    Arguments:
        A {[type]} -- [description]
        B {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    var = np.where(A < B, 1, 0)
    return (pd.Series(var, index=A.index).diff() < 0).apply(int)


def COUNT(COND, N):
    """
    2018/05/23 修改

    参考https://github.com/QUANTAXIS/QUANTAXIS/issues/429

    现在返回的是series
    """
    return pd.Series(np.where(COND, 1, 0), index=COND.index).rolling(N).sum()


def IF(COND, V1, V2):
    var = np.where(COND, V1, V2)
    return pd.Series(var, index=V1.index)


def IFAND(COND1, COND2, V1, V2):
    var = np.where(np.logical_and(COND1, COND2), V1, V2)
    return pd.Series(var, index=V1.index)


def IFOR(COND1, COND2, V1, V2):
    var = np.where(np.logical_or(COND1, COND2), V1, V2)
    return pd.Series(var, index=V1.index)


def REF(Series, N):
    var = Series.diff(N)
    var = Series - var
    return var


def LAST(COND, N1, N2):
    """表达持续性
    从前N1日到前N2日一直满足COND条件

    Arguments:
        COND {[type]} -- [description]
        N1 {[type]} -- [description]
        N2 {[type]} -- [description]
    """
    N2 = 1 if N2 == 0 else N2
    assert N2 > 0
    assert N1 > N2
    return COND.iloc[-N1:-N2].all()


def STD(Series, N):
    return pd.Series.rolling(Series, N).std()


def AVEDEV(Series, N):
    """
    平均绝对偏差 mean absolute deviation
    修正: 2018-05-25

    之前用mad的计算模式依然返回的是单值
    """
    return Series.rolling(N).apply(lambda x: (np.abs(x - x.mean())).mean(), raw=True)


def MACD(Series, FAST, SLOW, MID):
    """macd指标 仅适用于Series
    对于DATAFRAME的应用请使用QA_indicator_macd
    """
    EMAFAST = EMA(Series, FAST)
    EMASLOW = EMA(Series, SLOW)
    DIFF = EMAFAST - EMASLOW
    DEA = EMA(DIFF, MID)
    MACD = (DIFF - DEA) * 2
    DICT = {'DIFF': DIFF, 'DEA': DEA, 'MACD': MACD}
    VAR = pd.DataFrame(DICT)
    return VAR


def BBIBOLL(Series, N1, N2, N3, N4, N, M):
    """
    多空布林线
    :param Series:
    :param N1:
    :param N2:
    :param N3:
    :param N4:
    :param N:
    :param M:
    :return:
    """

    bbiboll = BBI(Series, N1, N2, N3, N4)
    UPER = bbiboll + M * STD(bbiboll, N)
    DOWN = bbiboll - M * STD(bbiboll, N)
    DICT = {'BBIBOLL': bbiboll, 'UPER': UPER, 'DOWN': DOWN}
    VAR = pd.DataFrame(DICT)
    return VAR


def BBI(Series, N1, N2, N3, N4):
    """
    多空指标
    :param Series:
    :param N1:
    :param N2:
    :param N3:
    :param N4:
    :return:
    """

    bbi = (MA(Series, N1) + MA(Series, N2) +
           MA(Series, N3) + MA(Series, N4)) / 4
    DICT = {'BBI': bbi}
    VAR = pd.DataFrame(DICT)
    return VAR


def BARLAST(cond, yes=True):
    """支持MultiIndex的cond和DateTimeIndex的cond
    条件成立  yes= True 或者 yes=1 根据不同的指标自己定

    Arguments:
        cond {[type]} -- [description]
    """
    if isinstance(cond.index, pd.MultiIndex):
        return len(cond) - cond.index.levels[0].tolist().index(cond[cond != yes].index[-1][0]) - 1
    elif isinstance(cond.index, pd.DatetimeIndex):
        return len(cond) - cond.index.tolist().index(cond[cond != yes].index[-1]) - 1


XARROUND = lambda x, y: np.round(y * (round(x / y - math.floor(x / y) + 0.00000000001) + math.floor(x / y)), 2)


def RSTD(Series, N=250, M=10):
    # pd.ewma(Series, span=M)
    return pd.rolling_std(Series, span=N, min_periods=M)
