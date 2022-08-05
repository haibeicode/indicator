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
Overbought and Oversold
超买超卖型
@author Tab
"""

from indicator.base import *
from indicator.technology.average import (EXPMEMA, HSL)


def CCI(df, N=14):
    """
    商品路径指标
    :param df:
    :param N:
    :return:
    """
    CLOSE = df['close']
    HIGH = df['high']
    LOW = df['low']

    TYP = (HIGH + LOW + CLOSE) / 3

    CCI = (TYP - MA(TYP, N)) / (0.015 * AVEDEV(TYP, N))
    return pd.DataFrame({
        'CCI': CCI
    })


def KDJ(df, N=9, M1=3, M2=3):
    """
    随机指标
    :param df:
    :param N:天数
    :param M1:天数
    :param M2:天数
    :return:
    """
    C = df['close']
    H = df['high']
    L = df['low']

    RSV = (C - LLV(L, N)) / (HHV(H, N) - LLV(L, N)) * 100

    KDJ_K = SMA(RSV, M1)
    KDJ_D = SMA(KDJ_K, M2)
    KDJ_J = 3 * KDJ_K - 2 * KDJ_D
    return pd.DataFrame({
        'KDJ_K': KDJ_K, 'KDJ_D': KDJ_D, 'KDJ_J': KDJ_J
    })


def MFT(df, N=9):
    """
    资金流量指标
    :param df:
    :param N:
    :return:
    """
    CLOSE = df['close']
    HIGH = df['high']
    LOW = df['low']
    VOL = df['volume']

    TYP = (HIGH + LOW + CLOSE) / 3
    V1 = SUM(IF(TYP > REF(TYP, 1), TYP * VOL, 0), N) / SUM(IF(TYP < REF(TYP, 1), TYP * VOL, 0), N)

    MFI = 100 - (100 / (1 + V1))
    return pd.DataFrame({
        'MFI': MFI
    })


def MTM(df, N=12, M=6):
    """
    动量线
    :param df:
    :param N:
    :param M:
    :return:
    """
    CLOSE = df['close']

    MTM = CLOSE - REF(CLOSE, N)
    MTMMA = MA(MTM, M)
    return pd.DataFrame({
        'MTM': MTM, 'MTMMA': MTMMA
    })


def KD(df, N=9, M1=3, M2=3):
    """
    随机指标
    :param df:
    :param N:
    :param M1:
    :param M2:
    :return:
    """
    CLOSE = df['close']
    LOW = df['low']
    HIGH = df['high']

    RSV = (CLOSE - LLV(LOW, N)) / (HHV(HIGH, N) - LLV(LOW, N)) * 100

    K = SMA(RSV, M1, 1)
    D = SMA(K, M2, 1)
    return pd.DataFrame({
        'K': K, 'D': D
    })


def SKDJ(df, N=9, M=3):
    """
    慢速随机指标
    :param df:
    :param N:
    :param M:
    :return:
    """
    CLOSE = df['close']
    LOWV = LLV(df['low'], N)
    HIGHV = HHV(df['high'], N)

    RSV = EMA((CLOSE - LOWV) / (HIGHV - LOWV) * 100, M)
    SKDJ_K = EMA(RSV, M)
    SKDJ_D = MA(SKDJ_K, M)
    return pd.DataFrame({
        'RSV': RSV, 'SKDJ_K': SKDJ_K, 'SKDJ_D': SKDJ_D
    })


def UDL(df, N1=3, N2=5, N3=10, N4=20, M=6):
    """
    引力线
    :param df:
    :param N1:
    :param N2:
    :param N3:
    :param N4:
    :param M:
    :return:
    """
    CLOSE = df['close']

    UDL = (MA(CLOSE, N1) + MA(CLOSE, N2) + MA(CLOSE, N3) + MA(CLOSE, N4)) / 4
    MAUDL = MA(UDL, M)
    return pd.DataFrame({
        'UDL': UDL, 'MAUDL': MAUDL
    })


def WR(df, N=10, N1=6):
    """
    威廉指标
    :param df:
    :param N:
    :param N1:
    :return:
    """
    HIGH = df['high']
    LOW = df['low']
    CLOSE = df['close']

    WR1 = 100 * (HHV(HIGH, N) - CLOSE) / (HHV(HIGH, N) - LLV(LOW, N))
    WR2 = 100 * (HHV(HIGH, N1) - CLOSE) / (HHV(HIGH, N1) - LLV(LOW, N1))
    return pd.DataFrame({
        'WR1': WR1, 'WR2': WR2
    })


def LWR(df, N=9, M1=3, M2=3):
    """
    威廉指标
    :param df:
    :param N:
    :param M1:
    :param M2:
    :return:
    """
    HIGH = df['high']
    LOW = df['low']
    CLOSE = df['close']
    RSV = (HHV(HIGH, N) - CLOSE) / (HHV(HIGH, N) - LLV(LOW, N)) * 100

    LWR1 = SMA(RSV, M1, 1)
    LWR2 = SMA(LWR1, M2, 1)
    return pd.DataFrame({
        'LWR1': LWR1, 'LWR2': LWR2
    })


def BIASQL(df, N=6, M=6):
    """
    乖离率-传统版
    :param df:
    :param N1:
    :param N2:
    :param N3:
    :return:
    """
    CLOSE = df['close']

    BIAS = (CLOSE - MA(CLOSE, N)) / MA(CLOSE, N) * 100
    BIASMA = MA(BIAS, M)
    return pd.DataFrame({
        'BIAS': BIAS,
        'BIASMA': BIASMA
    })


def BIAS(df, N1=6, N2=12, N3=24):
    """
    乖离率
    :param df:
    :param N1:
    :param N2:
    :param N3:
    :return:
    """
    CLOSE = df['close']

    BIAS1 = (CLOSE - MA(CLOSE, N1)) / MA(CLOSE, N1) * 100
    BIAS2 = (CLOSE - MA(CLOSE, N2)) / MA(CLOSE, N2) * 100
    BIAS3 = (CLOSE - MA(CLOSE, N3)) / MA(CLOSE, N3) * 100
    return pd.DataFrame({
        'BIAS1': BIAS1,
        'BIAS2': BIAS2,
        'BIAS3': BIAS3
    })


def BIAS36(df, M=6):
    """
    三六乖离
    :param df:
    :param M:
    :return:
    """
    CLOSE = df['close']

    BIAS36 = MA(CLOSE, 3) - MA(CLOSE, 6)
    BIAS612 = MA(CLOSE, 6) - MA(CLOSE, 12)
    MABIAS = MA(BIAS36, M)
    return pd.DataFrame({
        'BIAS36': BIAS36,
        'BIAS612': BIAS612,
        'MABIAS': MABIAS
    })


def ADTM(df, N=23, M=8):
    """
    动态买卖气指标
    :param df:
    :param N:
    :param M:
    :return:
    """
    HIGH = df['high']
    LOW = df['low']
    OPEN = df['open']

    DTM = IF(OPEN > REF(OPEN, 1), MAX((HIGH - OPEN), (OPEN - REF(OPEN, 1))), 0)
    DBM = IF(OPEN < REF(OPEN, 1), MAX((OPEN - LOW), (OPEN - REF(OPEN, 1))), 0)
    STM = SUM(DTM, N)
    SBM = SUM(DBM, N)

    ADTM1 = IF(STM > SBM, (STM - SBM) / STM, IF(STM != SBM, (STM - SBM) / SBM, 0))
    MAADTM = MA(ADTM1, M)
    return pd.DataFrame({
        'ADTM': ADTM1, 'MAADTM': MAADTM
    })


def ATR(df, N=14):
    """
    真实波幅
    :param df:
    :param N:
    :return:
    """
    CLOSE = df['close']
    HIGH = df['high']
    LOW = df['low']

    MTR = MAX(MAX((HIGH - LOW), ABS(REF(CLOSE, 1) - HIGH)), ABS(REF(CLOSE, 1) - LOW))
    ATR = MA(MTR, N)
    return pd.DataFrame({
        'MTR': MTR, 'ATR': ATR
    })


def DKX(df, M=10):
    """
    多空线
    :param df:
    :param M:
    :return:
    """
    CLOSE = df['close']
    LOW = df['low']
    OPEN = df['open']
    HIGH = df['high']

    MID = (3 * CLOSE + LOW + OPEN + HIGH) / 6

    DKX = (20 * MID + 19 * REF(MID, 1) + 18 * REF(MID, 2) + 17 * REF(MID, 3) +
           16 * REF(MID, 4) + 15 * REF(MID, 5) + 14 * REF(MID, 6) +
           13 * REF(MID, 7) + 12 * REF(MID, 8) + 11 * REF(MID, 9) +
           10 * REF(MID, 10) + 9 * REF(MID, 11) + 8 * REF(MID, 12) +
           7 * REF(MID, 13) + 6 * REF(MID, 14) + 5 * REF(MID, 15) +
           4 * REF(MID, 16) + 3 * REF(MID, 17) + 2 * REF(MID, 18) + REF(MID, 20)) / 210
    MADKX = MA(DKX, M)
    return pd.DataFrame({
        'DKX': DKX, 'MADKX': MADKX
    })


def TAPI(df, dp, M=6):
    """
    加权指数成交值(需下载日线)
    :param df:
    :param M:
    :return:
    """
    AMOUNT = df['amount']
    INDEXC = dp['close']

    TAPI = AMOUNT / INDEXC
    MATAIP = MA(TAPI, M)
    return pd.DataFrame({
        'TAPI': TAPI, 'MATAIP': MATAIP
    })


def RSI(df, N=6, M=12):
    """
    相对强弱指标
    :param df:
    :param N:
    :param M:
    :return:
    """
    CLOSE = df['close']

    OSC = 100 * (CLOSE - MA(CLOSE, N))
    MAOSC = EXPMEMA(OSC, M)
    return pd.DataFrame({
        'OSC': OSC, 'MAOSC': MAOSC
    })


def OSC(df, N=20, M=6):
    """
    变动速率线
    :param df:
    :param N:
    :param M:
    :return:
    """
    CLOSE = df['close']

    OSC = 100 * (CLOSE - MA(CLOSE, N))
    MAOSC = EXPMEMA(OSC, M)
    return pd.DataFrame({
        'OSC': OSC, 'MAOSC': MAOSC
    })


def ROC(df, N=12, M=6):
    """
    变动率指标
    :param df:
    :param N:
    :param M:
    :return:
    """
    CLOSE = df['close']
    OSC = 100 * (CLOSE - MA(CLOSE, N))
    MAOSC = EXPMEMA(OSC, M)

    return pd.DataFrame({
        'ROC': OSC, 'MAOSC': MAOSC
    })


def CYD(df, N=21):
    """
    承接因子
    :param df:
    :param N:
    :return:
    """
    # 获利盘比例方法不确定
    pass
    # VOL = df['volume']
    # CLOSE = df['close']
    # CYDS = WINNER(CLOSE) / (VOL / CAPITAL)
    # CYDN = WINNER(CLOSE) / MA(VOL / CAPITAL, N)
    # DICT = {'CYDS': CYDS, 'CYDN': CYDN}
    # return pd.DataFrame(DICT)


def CYF(df, N=21):
    """
    市场能量
    :param df:
    :param N:
    :param M:
    :return:
    """
    CYF = 100 - 100 / (1 + EMA(HSL, N))
    return pd.DataFrame(CYF)


def FSL(df):
    """
    分水岭
    :param df:
    :return:
    """
    # 当前流通股本方法不确定
    pass
    # VOL = df['volume']
    # CLOSE = df['close']
    # SWL = (EMA(CLOSE, 5) * 7 + EMA(CLOSE, 10) * 3) / 10
    # SWS = DMA(EMA(CLOSE, 12), MAX(1, 100 * (SUM(VOL, 5) / (3 * CAPITAL))))
    # DICT = {'SWL': SWL, 'MAADTM': SWS}
    #
    # return pd.DataFrame(DICT)


def MARSI(df, M1=10, M2=6):
    """
    相对强弱平均线
    :param df:
    :param M1:
    :param M2:
    :return:
    """
    CLOSE = df['close']
    DIF = CLOSE - REF(CLOSE, 1)
    VU = IF(DIF >= 0, DIF, 0)
    VD = IF(DIF < 0, -DIF, 0)
    MAU1 = MEMA(VU, M1)
    MAD1 = MEMA(VD, M1)
    MAU2 = MEMA(VU, M2)
    MAD2 = MEMA(VD, M2)

    RSI10 = MA(100 * MAU1 / (MAU1 + MAD1), M1)
    RSI6 = MA(100 * MAU2 / (MAU2 + MAD2), M2)
    DICT = {'RSI10': RSI10, 'RSI6': RSI6}

    return pd.DataFrame(DICT)
