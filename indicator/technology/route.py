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
Route
路径
@author Tab
"""
from indicator.base import *


def BOLL(df, N=20, P=2):
    """
    布林线
    :param df:
    :param N:
    :param P:
    :return:
    """
    C = df['close']
    boll = MA(C, N)
    UB = boll + P * STD(C, N)
    LB = boll - P * STD(C, N)
    DICT = {'BOLL': boll, 'UB': UB, 'LB': LB}

    return pd.DataFrame(DICT)


def PBX(df, N1=3, N2=5, N3=8, N4=13, N5=18, N6=24):
    """
    瀑布线
    :param df:
    :param N1:
    :param N2:
    :param N3:
    :param N4:
    :param N5:
    :param N6:
    :return:
    """
    C = df['close']
    PBX1 = (EMA(C, N1) + EMA(C, 2 * N1) + EMA(C, 4 * N1)) / 3
    PBX2 = (EMA(C, N2) + EMA(C, 2 * N2) + EMA(C, 4 * N2)) / 3
    PBX3 = (EMA(C, N3) + EMA(C, 2 * N3) + EMA(C, 4 * N3)) / 3
    PBX4 = (EMA(C, N4) + EMA(C, 2 * N4) + EMA(C, 4 * N4)) / 3
    PBX5 = (EMA(C, N5) + EMA(C, 2 * N5) + EMA(C, 4 * N5)) / 3
    PBX6 = (EMA(C, N6) + EMA(C, 2 * N6) + EMA(C, 4 * N6)) / 3
    DICT = {'PBX1': PBX1, 'PBX2': PBX2, 'PBX3': PBX3,
            'PBX4': PBX4, 'PBX5': PBX5, 'PBX6': PBX6}
    return pd.DataFrame(DICT)


def ENE(df, N=25, M1=6, M2=6):
    """
    轨道线
    :param df:
    :param N:
    :param M1:
    :param M2:
    :return:
    """
    CLOSE = df['close']
    UPPER = (1 + M1 / 100) * MA(CLOSE, N)
    LOWER = (1 - M2 / 100) * MA(CLOSE, N)
    ENE = (UPPER + LOWER) / 2
    DICT = {'UPPER': UPPER, 'ENE': ENE, 'ENE': ENE}
    return pd.DataFrame(DICT)


def MIKE(df, N=10):
    """
    麦克支撑压力
    :param df:
    :param N:
    :return:
    """
    CLOSE = df['close']
    HIGH = df['high']
    LOW = df['low']
    HLC = REF(MA((HIGH + LOW + CLOSE) / 3, N), 1)
    HV = EMA(HHV(HIGH, N), 3)
    LV = EMA(LLV(LOW, N), 3)

    STOR = EMA(2 * HV - LV, 3)
    MIDR = EMA(HLC + HV - LV, 3)
    WEKR = EMA(HLC * 2 - LV, 3)
    WEKS = EMA(HLC * 2 - HV, 3)
    MIDS = EMA(HLC - HV + LV, 3)
    STOS = EMA(2 * LV - HV, 3)

    return pd.DataFrame({
        'STOR': STOR, 'MIDR': MIDR, 'WEKR': WEKR,
        'WEKS': WEKS, 'MIDS': MIDS, 'STOS': STOS
    })


def XS(df, N=13):
    """
    薛斯通道
    :param df:
    :param N:
    :return:
    """
    CLOSE = df['close']
    VOL = df['volume']

    VAR2 = CLOSE * VOL
    VAR3 = EMA((EMA(VAR2, 3) / EMA(VOL, 3) + EMA(VAR2, 6) / EMA(VOL, 6) + EMA(VAR2, 12) / EMA(VOL, 12) + EMA(VAR2,
                                                                                                             24) / EMA(
        VOL, 24)) / 4, N)

    SUP = 1.06 * VAR3
    SDN = VAR3 * 0.94
    VAR4 = EMA(CLOSE, 9)
    LUP = EMA(VAR4 * 1.14, 5)
    LDN = EMA(VAR4 * 0.86, 5)

    return pd.DataFrame({
        'SUP': SUP, 'SDN': SDN, 'VAR4': VAR4,
        'LUP': LUP, 'LDN': LDN
    })


def XS2(df, N=102, M=7):
    """
    薛斯通道II
    :param df:
    :param N:
    :param M:
    :return:
    """
    CLOSE = df['close']
    HIGH = df['high']
    LOW = df['low']

    AA = MA((2 * CLOSE + HIGH + LOW) / 4, 5)
    CC = ABS((2 * CLOSE + HIGH + LOW) / 4 - MA(CLOSE, 20)) / MA(CLOSE, 20)
    DD = DMA(CLOSE, CC)

    TD1 = AA * N / 100;
    TD2 = AA * (200 - N) / 100;
    TD3 = (1 + M / 100) * DD;
    TD4 = (1 - M / 100) * DD;

    return pd.DataFrame({
        'TD1': TD1, 'TD2': TD2, 'TD3': TD3, 'TD4': TD4
    })
