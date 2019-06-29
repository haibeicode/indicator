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
Pressure support Indicators
@author Tab
"""
from indicator.base import *


def MIKE(df, N=12):
    """
    MIKE指标
    :param df:
    :param N:
    :return:
    """
    HIGH = df['high']
    LOW = df['low']
    CLOSE = df['close']

    TYP = (HIGH + LOW + CLOSE) / 3
    LL = LLV(LOW, N)
    HH = HHV(HIGH, N)

    WR = TYP + (TYP - LL)
    MR = TYP + (HH - LL)
    SR = 2 * HH - LL
    WS = TYP - (HH - TYP)
    MS = TYP - (HH - LL)
    SS = 2 * LL - HH
    return pd.DataFrame({
        'WR': WR, 'MR': MR, 'SR': SR,
        'WS': WS, 'MS': MS, 'SS': SS
    })


def MFI(df, N=14):
    """
    资金指标
    :param df:
    :param N:
    :return:
    """
    C = df['close']
    H = df['high']
    L = df['low']
    VOL = df['volume']
    TYP = (C + H + L) / 3
    V1 = SUM(IF(TYP > REF(TYP, 1), TYP * VOL, 0), N) / \
         SUM(IF(TYP < REF(TYP, 1), TYP * VOL, 0), N)
    mfi = 100 - (100 / (1 + V1))
    DICT = {'MFI': mfi}

    return pd.DataFrame(DICT)


def ATR(df, N=14):
    """
    简单移动平均
    :param df:
    :param N:
    :return:
    """
    C = df['close']
    H = df['high']
    L = df['low']
    TR = MAX(MAX((H - L), ABS(REF(C, 1) - H)), ABS(REF(C, 1) - L))
    atr = MA(TR, N)
    return pd.DataFrame({'TR': TR, 'ATR': atr})


def DDI(df, N=13, N1=26, M=1, M1=5):
    """
    方向标准离差指数 分析DDI柱状线，由红变绿(正变负)，卖出信号参考；由绿变红，买入信号参考。
    :param df:
    :param N:
    :param N1:
    :param M:
    :param M1:
    :return:
    """

    H = df['high']
    L = df['low']
    DMZ = IF((H + L) > (REF(H, 1) + REF(L, 1)),
             MAX(ABS(H - REF(H, 1)), ABS(L - REF(L, 1))), 0)
    DMF = IF((H + L) < (REF(H, 1) + REF(L, 1)),
             MAX(ABS(H - REF(H, 1)), ABS(L - REF(L, 1))), 0)
    DIZ = SUM(DMZ, N) / (SUM(DMZ, N) + SUM(DMF, N))
    DIF = SUM(DMF, N) / (SUM(DMF, N) + SUM(DMZ, N))
    ddi = DIZ - DIF
    ADDI = SMA(ddi, N1, M)
    AD = MA(ADDI, M1)
    DICT = {'DDI': ddi, 'ADDI': ADDI, 'AD': AD}

    return pd.DataFrame(DICT)


def shadow(df):
    """
    上下影线指标
    :param df:
    :return:
    """
    return {
        'LOW': lower_shadow(df), 'UP': upper_shadow(df),
        'BODY': body(df), 'BODY_ABS': body_abs(df), 'PRICE_PCG': price_pcg(df)
    }


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

    :param df:
    :return:
    """
    return abs(df['open'] - df['close'])


def body(df):
    """

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


def amplitude(df):
    """

    :param df:
    :return:
    """
    return (df['high'] - df['low']) / df['low']
