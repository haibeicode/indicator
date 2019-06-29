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
Energy Indicator
能量型
@author Tab
"""
from indicator.base import *


def BRAR(df, N=26):
    """
    情绪指标
    :param df:
    :param N:
    :return:
    """
    OPEN = df['open']
    CLOSE = df['close']
    HIGH = df['high']
    LOW = df['low']
    BR = SUM(MAX(0, HIGH - REF(CLOSE, 1)), N) / SUM(MAX(0, REF(CLOSE, 1) - LOW), N) * 100
    AR = SUM(HIGH - OPEN, N) / SUM(OPEN - LOW, N) * 100
    return pd.DataFrame({
        'BR': BR, 'AR': AR
    })


def CR(df, N=26, M1=10, M2=20, M3=40, M4=62):
    """
    带状能量线
    :param df:
    :param N:
    :param M1:
    :param M2:
    :param M3:
    :return:
    """
    HIGH = df['high']
    LOW = df['low']

    MID = REF(HIGH + LOW, 1) / 2

    CR = SUM(MAX(0, HIGH - MID), N) / SUM(MAX(0, MID - LOW), N) * 100
    MA1 = REF(MA(CR, M1), M1 / 2.5 + 1)
    MA2 = REF(MA(CR, M2), M2 / 2.5 + 1)
    MA3 = REF(MA(CR, M3), M3 / 2.5 + 1)
    MA4 = REF(MA(CR, M4), M4 / 2.5 + 1)
    return pd.DataFrame({
        'CR': CR, 'MA1': MA1, 'MA2': MA2, 'MA3': MA3, 'MA4': MA4
    })


def MASS(df, N1=9, N2=25, M=6):
    """
    梅斯线
    :param df:
    :param N1:
    :param M2:
    :param M:
    :return:
    """
    HIGH = df['high']
    LOW = df['low']

    MASS = SUM(MA(HIGH - LOW, N1) / MA(MA(HIGH - LOW, N1), N1), N2)
    MAMASS = MA(MASS, M)
    return pd.DataFrame({
        'MASS': MASS, 'MAMASS': MAMASS
    })


def PSY(df, N=12, M=6):
    """
    心理线
    :param df:
    :param N1:
    :param M:
    :return:
    """

    CLOSE = df['close']

    PSY = COUNT(CLOSE > REF(CLOSE, 1), N) / N * 100
    PSYMA = MA(PSY, M)
    return pd.DataFrame({
        'PSY': PSY, 'PSYMA': PSYMA
    })


def VR(df, N=26, M=6):
    """
    成交量变异率
    :param df:
    :param N:
    :param M:
    :return:
    """
    VOL = df['volume']
    CLOSE = df['close']

    TH = SUM(IF(CLOSE > REF(CLOSE, 1), VOL, 0), N)
    TL = SUM(IF(CLOSE < REF(CLOSE, 1), VOL, 0), N)
    TQ = SUM(IF(CLOSE == REF(CLOSE, 1), VOL, 0), N)

    VR = 100 * (TH * 2 + TQ) / (TL * 2 + TQ)
    MAVR = MA(VR, M)
    return pd.DataFrame({
        'VR': VR, 'MAVR': MAVR
    })


def WAD(df, M=30):
    """
    威廉多空力度线
    :param df:
    :param M:
    :return:
    """
    LOW = df['low']
    HIGH = df['high']
    CLOSE = df['close']

    MIDA = CLOSE - MIN(REF(CLOSE, 1), LOW)
    MIDB = IF(CLOSE < REF(CLOSE, 1), CLOSE - MAX(REF(CLOSE, 1), HIGH), 0)

    WAD = SUM(IF(CLOSE > REF(CLOSE, 1), MIDA, MIDB), 0)
    MAWAD = MA(WAD, M)
    return pd.DataFrame({
        'WAD': WAD, 'MAWAD': MAWAD
    })


def PCNT(df, M=5):
    """
    幅度比
    :param df:
    :param M:
    :return:
    """
    CLOSE = df['close']

    PCNT = (CLOSE - REF(CLOSE, 1)) / CLOSE * 100
    MAPCNT = EXPMEMA(PCNT, M)
    return pd.DataFrame({
        'WAD': WAD, 'MAPCNT': MAPCNT
    })


def CYR(df, N=5, M=5):
    """
    市场强弱
    :param df:
    :param M:
    :return:
    """
    VOL = df['volume']
    AMOUNT = df['amount']
    DIVE = 0.01 * EMA(AMOUNT, N) / EMA(VOL, N)

    CRY = (DIVE / REF(DIVE, 1) - 1) * 100
    MACYR = MA(CRY, M)
    return pd.DataFrame({
        'CRY': CRY, 'MACYR': MACYR
    })
