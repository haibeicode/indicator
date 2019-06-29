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
Transactional type
交易型
@author Tab
"""
from indicator.base import *


def MAJY(df, SHORT=5, LONG=20):
    """
    MA交易
    :param df:
    :param SHORT:
    :param LONG:
    :return:
    """
    CLOSE = df['close']
    MA1 = MA(CLOSE, SHORT)
    MA2 = MA(CLOSE, LONG)

    DUO = CROSS(MA1, MA2)
    KONG = CROSS(MA2, MA1)

    return pd.DataFrame({
        'DUO': DUO, 'KONG': KONG
    })


def MACDJY(df, SHORT=12, LONG=26, MID=9):
    """
    MA交易
    :param df:
    :param SHORT:
    :param LONG:
    :return:
    """
    CLOSE = df['close']
    DIFF = EMA(CLOSE, SHORT) - EMA(CLOSE, LONG)
    DEA = EMA(DIFF, MID)
    MACD = 2 * (DIFF - DEA)

    DUO = CROSS(MACD, 0)
    KONG = CROSS(0, MACD)

    return pd.DataFrame({
        'DUO': DUO, 'KONG': KONG
    })


def KDJJY(df, N=9, M1=3):
    """
    KDJ交易
    :param df:
    :param N:
    :param M1:
    :return:
    """
    CLOSE = df['close']
    HIGH = df['high']
    LOW = df['low']
    RSV = (CLOSE - LLV(LOW, N)) / (HHV(HIGH, N) - LLV(LOW, N)) * 100
    K = SMA(RSV, M1, 1)
    D = SMA(K, M1, 1)
    J = 3 * K - 2 * D

    DUO = CROSS(J, 0)
    KONG = CROSS(100, J)

    return pd.DataFrame({
        'DUO': DUO, 'KONG': KONG
    })


def TQAJY(df, X1=20, X2=10, NMIN=10):
    """
    唐奇安
    :param df:
    :param X1:
    :param X2:
    :param NMIN:
    :return:
    """
    HIGH = df['high']
    LOW = df['low']
    ZQGD = REF(HHV(HIGH, X1), 1)
    ZQDD = REF(LLV(LOW, X2), 1)

    DUO = HIGH >= ZQGD
    KONG = LOW <= ZQDD

    return pd.DataFrame({
        'DUO': DUO, 'KONG': KONG
    })


def KTNJY(df, AVGLENGTH=40, ATRLENGTH=40):
    """
    肯特纳通道交易
    :param df:
    :param AVGLENGTH:
    :param ATRLENGTH:
    :return:
    """
    # 真实波幅方法不确定
    pass
    # CLOSE = df['close']
    # HIGH = df['high']
    # LOW = df['low']
    # MA1 = REF(MA((HIGH + LOW + CLOSE) / 3, AVGLENGTH), 1)
    # UPPERBAND = MA1 + REF(MA(TR, ATRLENGTH), 1)
    # LOWERBAND = MA1 - REF(MA(TR, ATRLENGTH), 1)
    #
    # KDTJ = MA1 > REF(MA1, 1) and HIGH >= UPPERBAND
    # PDTJ = LOW <= MA1
    # KKTJ = MA1 < REF(MA1, 1) and LOW <= LOWERBAND
    # PKTJ = HIGH >= MA1
    # GL1 = NOT(KDTJ == 1 and PDTJ == 1)
    # GL2 = NOT(KKTJ == 1 and PKTJ == 1)
    #
    # return pd.DataFrame({
    #     'GL1': GL1, 'GL2': GL2
    # })


def RNTPJY(df, N=30, M=5):
    """
    日内突破交易
    :param df:
    :param N:
    :param M:
    :return:
    """
    # 日期方法不确定
    pass
    # HIGH = df['high']
    # LOW = df['low']
    # NBAR = BARSLAST(DATE != REF(DATE, 1)) + 1
    # T1 = TIME > 900 and TIME < 1455
    # T2 = TIME >= 1455
    #
    # HHN = REF(HHV(HIGH, N), 1)
    # LLN = REF(LLV(LOW, N), 1)
    # MID = (HHN + LLN) / 2
    #
    # DUO = HIGH > HHN and (HHN - MID) / MID < M / 1000 and NBAR >= 30 and T1
    # KONG = LOW < LLN and (MID - LLN) / MID < M / 1000 and NBAR >= 30 and T1
    # return pd.DataFrame({
    #     'DUO': DUO, 'KONG': KONG
    # })


def HANSJY(df, M=1, NMIN1=30, NMIN2=30):
    """
    日内突破交易
    :param df:
    :param N:
    :param M:
    :return:
    """
    # 日期方法不确定
    pass
    # CLOSE = df['close']
    # HIGH = df['high']
    # LOW = df['low']
    # N = BARSLAST(DATE != REF(DATE, 1)) + 1
    # HHH = VALUEWHEN(TIME <= 900 + NMIN1, HHV(HIGH, N))
    # LLL = VALUEWHEN(TIME <= 900 + NMIN1, LLV(LOW, N))
    #
    # SG = HHH + M * MINDIFF
    # XG = LLL - M * MINDIFF
    #
    # DUO = CLOSE > SG
    # KONG = CLOSE < XG
    # DUOTIME = TIME > 900 + NMIN1 and TIME < 1450
    # KONGTIME = TIME >= 1500 - NMIN2
    #
    # return pd.DataFrame({
    #     'DUO': DUO, 'KONG': KONG, 'DUOTIME': DUOTIME, 'KONGTIME': KONGTIME
    # })
