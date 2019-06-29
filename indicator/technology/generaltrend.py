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
General Trend
大势型
@author Tab
"""

from indicator.base import *


def ABI(df, M=10):
    """
    绝对广量指标
    :param M:
    :return:
    """
    ADVANCE = df['advance']
    DECLINE = df['decline']
    ABI = 100 * ABS(ADVANCE - DECLINE) / (ADVANCE + DECLINE)
    MAABI = EMA(ABI, M)

    return pd.DataFrame({
        'ABI': ABI, 'MAABI': MAABI
    })


def ADL(df, M=7):
    """
    腾落指标
    :param M:
    :return:
    """
    ADVANCE = df['advance']
    DECLINE = df['decline']
    ADL = SUM(ADVANCE - DECLINE, 0)
    MAADL = MA(ADL, M)
    DICT = {'ADL': ADL, 'MAADL': MAADL}
    return pd.DataFrame(DICT)


def ADR(df, N=10, M=6):
    """
    涨跌比率
    :param N:
    :param M:
    :return:
    """
    ADVANCE = df['advance']
    DECLINE = df['decline']
    ADR = SUM(ADVANCE, N) / SUM(DECLINE, N)
    MAADR = MA(ADR, M)
    DICT = {'ADR': ADR, 'MAADR': MAADR}
    return pd.DataFrame(DICT)


def ARMS(df, N=10, M=6):
    """
    阿姆氏指标
    :param N:
    :param M:
    :return:
    """
    ADVANCE = df['advance']
    DECLINE = df['decline']
    ARMS = EMA(ADVANCE / DECLINE, N)
    MAARMS = MA(ARMS, M)
    DICT = {'ARMS': ARMS, 'MAARMS': MAARMS}
    return pd.DataFrame(DICT)


def BTI(df, N=10, M=6):
    """
    广量冲力指标
    :param N:
    :param M:
    :return:
    """
    ADVANCE = df['advance']
    DECLINE = df['decline']
    BTI = EMA(100 * ADVANCE / (ADVANCE + DECLINE), N)
    MABTI = MA(BTI, M)
    DICT = {'BTI': BTI, 'MABTI': MABTI}
    return pd.DataFrame(DICT)


def BTI(df, N1=10, N2=6):
    """
    麦克连指标
    :param N1:
    :param N2:
    :return:
    """
    ADVANCE = df['advance']
    DECLINE = df['decline']
    DIF = ADVANCE - DECLINE
    EMA1 = EMA(DIF, N1)
    EMA2 = EMA(DIF, N2)
    MCL = EMA1 - EMA2
    MAMCL1 = EMA1
    MAMCL2 = EMA2
    DICT = {'MCL': MCL, 'MAMCL1': MAMCL1, 'MAMCL2': MAMCL2}
    return pd.DataFrame(DICT)


def STIX(df, M=6):
    """
    超买超卖指标
    :param M:
    :return:
    """
    ADVANCE = df['advance']
    DECLINE = df['decline']
    TBR = 100 * ADVANCE / (ADVANCE + DECLINE)
    MATBR = EMA(TBR, M)
    DICT = {'TBR': TBR, 'MATBR': MATBR}
    return pd.DataFrame(DICT)
