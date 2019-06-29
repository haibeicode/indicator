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
Counter Trend Indicator
Overbought and Oversold
超买超卖型
@author Tab
"""

from indicator.base import *


def CCI(df, N=14):
    """
    商品路径指标
    :param df:
    :param N:
    :return:
    """
    typ = (df['high'] + df['low'] + df['close']) / 3
    cci = ((typ - MA(typ, N)) / (0.015 * AVEDEV(typ, N)))
    a = 100
    b = -100

    return pd.DataFrame({
        'CCI': cci, 'a': a, 'b': b
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
    K = SMA(RSV, M1)
    D = SMA(K, M2)
    J = 3 * K - 2 * D
    DICT = {'KDJ_K': K, 'KDJ_D': D, 'KDJ_J': J}
    return pd.DataFrame(DICT)


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
    return pd.DataFrame(MFI)


def MTM(df, N=12, M=6):
    """
    动量线
    :param df:
    :param N:
    :param M:
    :return:
    """
    C = df['close']
    mtm = C - REF(C, N)
    MTMMA = MA(mtm, M)
    DICT = {'MTM': mtm, 'MTMMA': MTMMA}
    return pd.DataFrame(DICT)


def OSC(df, N=20, M=6):
    """
    变动速率线
    :param df:
    :param N:
    :param M:
    :return:
    """
    C = df['close']
    OS = (C - MA(C, N)) * 100
    MAOSC = EMA(OS, M)
    DICT = {'OSC': OS, 'MAOSC': MAOSC}

    return pd.DataFrame(DICT)


def ROC(df, N=12, M=6):
    """
    变动率指标
    :param df:
    :param N:
    :param M:
    :return:
    """
    C = df['close']
    roc = 100 * (C - REF(C, N)) / REF(C, N)
    ROCMA = MA(roc, M)
    DICT = {'ROC': roc, 'ROCMA': ROCMA}

    return pd.DataFrame(DICT)


def RSI(df, N1=12, N2=26, N3=9):
    """
    相对强弱指标
    :param df:
    :param N1:
    :param N2:
    :param N3:
    :return:
    """
    CLOSE = df['close']
    LC = REF(CLOSE, 1)
    RSI1 = SMA(MAX(CLOSE - LC, 0), N1) / SMA(ABS(CLOSE - LC), N1) * 100
    RSI2 = SMA(MAX(CLOSE - LC, 0), N2) / SMA(ABS(CLOSE - LC), N2) * 100
    RSI3 = SMA(MAX(CLOSE - LC, 0), N3) / SMA(ABS(CLOSE - LC), N3) * 100
    DICT = {'RSI1': RSI1, 'RSI2': RSI2, 'RSI3': RSI3}

    return pd.DataFrame(DICT)


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
    DICT = {'K': K, 'D': D}
    return pd.DataFrame(DICT)


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
    K = EMA(RSV, M)
    D = MA(K, M)
    DICT = {'RSV': RSV, 'SKDJ_K': K, 'SKDJ_D': D}

    return pd.DataFrame(DICT)


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
    DICT = {'UDL': UDL, 'MAUDL': MAUDL}

    return pd.DataFrame(DICT)


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
    DICT = {'WR1': WR1, 'WR2': WR2}

    return pd.DataFrame(DICT)


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
    DICT = {'LWR1': LWR1, 'LWR2': LWR2}

    return pd.DataFrame(DICT)


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
    DICT = {'BIAS': BIAS, 'BIASMA': BIASMA}
    return pd.DataFrame(DICT)


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
    DICT = {'BIAS1': BIAS1, 'BIAS2': BIAS2, 'BIAS3': BIAS3}

    return pd.DataFrame(DICT)


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
    ADTM1 = IF(STM > SBM, (STM - SBM) / STM,
               IF(STM != SBM, (STM - SBM) / SBM, 0))
    MAADTM = MA(ADTM1, M)
    DICT = {'ADTM': ADTM1, 'MAADTM': MAADTM}

    return pd.DataFrame(DICT)


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
    DICT = {'MTR': MTR, 'ATR': ATR}

    return pd.DataFrame(DICT)


def ATR(df, M=10):
    """
    真实波幅
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
    DICT = {'DKX': DKX, 'MADKX': MADKX}
    return pd.DataFrame(DICT)


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
    DICT = {'TAPI': TAPI, 'MATAIP': MATAIP}

    return pd.DataFrame(DICT)


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
    # 换手线函数方法不确定
    pass
    # CYF = 100 - 100 / (1 + EMA(HSL, N))
    # return pd.DataFrame(CYF)


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
