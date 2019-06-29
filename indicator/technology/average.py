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
Moving Average
均线
@author Tab
"""
from indicator.base import *


def ACD(df, M=20):
    """
    升降线
    :param df:
    :param M:
    :return:
    """
    CLOSE = df['close']
    LOW = df['low']
    HIGH = df['high']
    LC = REF(CLOSE, 1)
    DIF = CLOSE - IF(CLOSE > LC, MIN(LOW, LC), MAX(HIGH, LC))

    ACD = SUM(IF(CLOSE == LC, 0, DIF), 0)
    MAACD = EXPMEMA(ACD, M)
    return pd.DataFrame({
        'ACD': ACD, 'MAACD': MAACD
    })


def BBI(df, M1=3, M2=6, M3=12, M4=24):
    """
    多空均线
    :param df:
    :param M1:
    :param M2:
    :param M3:
    :param M4:
    :return:
    """
    CLOSE = df['close']

    BBI = (MA(CLOSE, M1) + MA(CLOSE, M2) + MA(CLOSE, M3) + MA(CLOSE, M4)) / 4
    return pd.DataFrame({
        'BBI': BBI
    })


def EXPMA(df, P1=5, P2=10, P3=20, P4=60):
    """
    指数平均线
    :param df:
    :param P1:
    :param P2:
    :param P3:
    :param P4:
    :return:
    """
    CLOSE = df['close']
    MA1 = EMA(CLOSE, P1)
    MA2 = EMA(CLOSE, P2)
    MA3 = EMA(CLOSE, P3)
    MA4 = EMA(CLOSE, P4)
    return pd.DataFrame({
        'MA1': MA1, 'MA2': MA2, 'MA3': MA3, 'MA4': MA4
    })


def EXPMAS(df, M1=12, M2=50):
    """
    指数平均线-副图
    :param df:
    :param M1:
    :param M2:
    :return:
    """
    CLOSE = df['close']

    EXP1 = EMA(CLOSE, M1)
    EXP2 = EMA(CLOSE, M2)
    return pd.DataFrame({
        'EXP1': EXP1, 'EXP2': EXP2
    })


def HMA(df, M1=6, M2=12, M3=30, M4=72, M5=144):
    """
    高价平均线
    :param df:
    :param M1:
    :param M2:
    :param M3:
    :param M4:
    :param M5:
    :return:
    """
    HIGH = df['high']
    HMA1 = MA(HIGH, M1)
    HMA2 = MA(HIGH, M2)
    HMA3 = MA(HIGH, M3)
    HMA4 = MA(HIGH, M4)
    HMA5 = MA(HIGH, M5)
    return pd.DataFrame({
        'HMA1': HMA1, 'HMA2': HMA2, 'HMA3': HMA3, 'HMA4': HMA4, 'HMA5': HMA5
    })


def LMA(df, M1=6, M2=12, M3=30, M4=72, M5=144):
    """
    低价平均线
    :param df:
    :param M1:
    :param M2:
    :param M3:
    :param M4:
    :param M5:
    :return:
    """
    LOW = df['low']
    LMA1 = MA(LOW, M1)
    LMA2 = MA(LOW, M2)
    LMA3 = MA(LOW, M3)
    LMA4 = MA(LOW, M4)
    LMA5 = MA(LOW, M5)
    return pd.DataFrame({
        'LMA1': LMA1, 'LMA2': LMA2, 'LMA3': LMA3, 'LMA4': LMA4, 'LMA5': LMA5
    })


def VMA(df, M1=6, M2=12, M3=30, M4=72, M5=144):
    """
    变异平均线
    :param df:
    :param M1:
    :param M2:
    :param M3:
    :param M4:
    :param M5:
    :return:
    """
    HIGH = df['high']
    OPEN = df['open']
    LOW = df['low']
    CLOSE = df['close']
    VV = (HIGH + OPEN + LOW + CLOSE) / 4

    VMA1 = MA(VV, M1)
    VMA2 = MA(VV, M2)
    VMA3 = MA(VV, M3)
    VMA4 = MA(VV, M4)
    VMA5 = MA(VV, M5)
    return pd.DataFrame({
        'VMA1': VMA1, 'VMA2': VMA2, 'VMA3': VMA3, 'VMA4': VMA4, 'VMA5': VMA5
    })


def VMA(df, M1=5, M2=13, M3=34, M4=60):
    """
    成本价均线
    :param df:
    :param M1:
    :param M2:
    :param M3:
    :param M4:
    :return:
    """
    OPEN = df['open']
    VOL = df['volume']
    CLOSE = df['close']
    AMOV = VOL * (OPEN + CLOSE) / 2

    AMV1 = SUM(AMOV, M1) / SUM(VOL, M1)
    AMV2 = SUM(AMOV, M2) / SUM(VOL, M2)
    AMV3 = SUM(AMOV, M3) / SUM(VOL, M3)
    AMV4 = SUM(AMOV, M4) / SUM(VOL, M4)
    return pd.DataFrame({
        'AMV1': AMV1, 'AMV2': AMV2, 'AMV3': AMV3, 'AMV4': AMV4
    })


def BBIBOLL(df, N=11, M=6):
    """
    多空布林线
    :param df:
    :param N:
    :param M:
    :return:
    """
    CLOSE = df['close']

    BBIBOLL = (MA(CLOSE, 3) + MA(CLOSE, 6) + MA(CLOSE, 12) + MA(CLOSE, 24)) / 4
    UPR = BBIBOLL + M * STD(BBIBOLL, N)
    DWN = BBIBOLL - M * STD(BBIBOLL, N)

    return pd.DataFrame({
        'BBIBOLL': BBIBOLL, 'UPR': UPR, 'DWN': DWN
    })


def ALLIGAT(df, N=11, M=6):
    """
    多空布林线
    :param df:
    :param N:
    :param M:
    :return:
    """
    HIGH = df['high']
    LOW = df['low']

    NN = (HIGH + LOW) / 2

    SC = REF(MA(NN, 5), 3)
    YC = REF(MA(NN, 8), 5)
    XE = REF(MA(NN, 13), 8)

    return pd.DataFrame({
        'SC': SC, 'YC': YC, 'XE': XE
    })
