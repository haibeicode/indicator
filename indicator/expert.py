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
@author Tab
"""
from indicator.base import *
from indicator.technology.countertrend import (CCI, MTM, ROC)
from indicator.technology.energy import (PSY)


def MACDZJ(df, LONG=5, SHORT=4, M=1):
    """
    MACD专家系统
    :param df:
    :param LONG:
    :param SHORT:
    :param M:
    :return:
    """
    CLOSE = df['close']
    DIFF = EMA(CLOSE, SHORT) - EMA(CLOSE, LONG)
    DEA = EMA(DIFF, M)
    MACD = 2 * (DIFF - DEA)

    ENTERLONG = CROSS(MACD, 0)
    EXITLONG = CROSS(0, MACD)
    return pd.DataFrame({
        'ENTERLONG': ENTERLONG, 'EXITLONG': EXITLONG
    })


def KDJZJ(df, N=4, M1=1):
    """
    KDJ专家系统
    :param df:
    :param N:
    :param M1:
    :return:
    """
    CLOSE = df['close']
    LOW = df['low']
    HIGH = df['high']
    RSV = (CLOSE - LLV(LOW, N)) / (HHV(HIGH, N) - LLV(LOW, N)) * 100
    K = SMA(RSV, M1, 1)
    D = SMA(K, M1, 1)
    J = 3 * K - 2 * D

    ENTERLONG = CROSS(J, 0)
    EXITLONG = CROSS(100, J)
    return pd.DataFrame({
        'ENTERLONG': ENTERLONG, 'EXITLONG': EXITLONG
    })


def BOLLZJ(df, N=2):
    """
    布林带专家系统
    :param df:
    :param N:
    :return:
    """
    CLOSE = df['close']
    MID = MA(CLOSE, N)
    UPPER = MID + 2 * STD(CLOSE, N)
    LOWER = MID - 2 * STD(CLOSE, N)

    ENTERLONG = CROSS(CLOSE, LOWER)
    EXITLONG = CROSS(CLOSE, UPPER)
    return pd.DataFrame({
        'ENTERLONG': ENTERLONG, 'EXITLONG': EXITLONG
    })


def MAZJ(df, SHORT=1, LONG=4):
    """
    均线专家系统
    :param df:
    :param SHORT:
    :param LONG:
    :return:
    """
    CLOSE = df['close']
    ENTERLONG = CROSS(MA(CLOSE, SHORT), MA(CLOSE, LONG))
    EXITLONG = CROSS(MA(CLOSE, LONG), MA(CLOSE, SHORT))
    return pd.DataFrame({
        'ENTERLONG': ENTERLONG, 'EXITLONG': EXITLONG
    })


def EXPMAZJ(df, M1=2, M2=2):
    """
    EXPMA专家系统
    :param df:
    :param M1:
    :param M2:
    :return:
    """
    CLOSE = df['close']
    EXP1 = EMA(CLOSE, M1)
    EXP2 = EMA(CLOSE, M2)

    ENTERLONG = CROSS(EXP1, EXP2)
    EXITLONG = CROSS(EXP2, EXP1)
    return pd.DataFrame({
        'ENTERLONG': ENTERLONG, 'EXITLONG': EXITLONG
    })


def CCIZJ(df, N=1):
    """
    CCI专家系统
    :param df:
    :param N:
    :return:
    """
    INDEX = CCI(df, N)

    ENTERLONG = CROSS(INDEX, -100)
    EXITLONG = CROSS(100, INDEX)
    return pd.DataFrame({
        'ENTERLONG': ENTERLONG, 'EXITLONG': EXITLONG
    })


def BIASZJ(df, N=6, LL=3, LH=2):
    """
    乖离率专家系统
    :param df:
    :param N:
    :param LL:
    :param LH:
    :return:
    """
    CLOSE = df['close']
    BIAS = (CLOSE - MA(CLOSE, N)) / MA(CLOSE, N) * 100
    ENTERLONG = CROSS(-LL, BIAS)
    EXITLONG = CROSS(BIAS, LH)
    return pd.DataFrame({
        'ENTERLONG': ENTERLONG, 'EXITLONG': EXITLONG
    })


def DMIZJ(df, N=1):
    """
    趋向专家系统
    :param df:
    :param N:
    :return:
    """
    CLOSE = df['close']
    HIGH = df['high']
    LOW = df['low']
    MTR = SUM(MAX(MAX(HIGH - LOW, ABS(HIGH - REF(CLOSE, 1))), ABS(LOW - REF(CLOSE, 1))), N)
    HD = HIGH - REF(HIGH, 1)
    LD = REF(LOW, 1) - LOW
    PDM = SUM(IF(HD > 0 and HD > LD, HD, 0), N)
    MDM = SUM(IF(LD > 0 and LD > HD, LD, 0), N)
    PDI = PDM * 100 / MTR
    MDI = MDM * 100 / MTR

    ENTERLONG = CROSS(PDI, MDI)
    EXITLONG = CROSS(MDI, PDI)
    return pd.DataFrame({
        'ENTERLONG': ENTERLONG, 'EXITLONG': EXITLONG
    })


def KDZJ(df, N=1, M1=1, M2=1):
    """
    KD指标专家系统
    :param df:
    :param N:
    :param M1:
    :param M2:
    :return:
    """
    CLOSE = df['close']
    HIGH = df['high']
    LOW = df['low']
    WRSV = (CLOSE - LLV(LOW, N)) / (HHV(HIGH, N) - LLV(LOW, N)) * 100
    WK = SMA(WRSV, M1, 1)
    D = SMA(WK, M2, 1)

    ENTERLONG = CROSS(WK, D) and WK < 20
    EXITLONG = CROSS(D, WK) and WK > 80

    return pd.DataFrame({
        'ENTERLONG': ENTERLONG, 'EXITLONG': EXITLONG
    })


def RSIZJ(df, N=3, LL=6, LH=6):
    """
    相对强弱专家系统
    :param df:
    :param N:
    :param LL:
    :param LH:
    :return:
    """
    CLOSE = df['close']
    LC = REF(CLOSE, 1)
    WRSI = SMA(MAX(CLOSE - LC, 0), N, 1) / SMA(ABS(CLOSE - LC), N, 1) * 100

    ENTERLONG = CROSS(WRSI, LL)
    EXITLONG = CROSS(LH, WRSI)
    return pd.DataFrame({
        'ENTERLONG': ENTERLONG, 'EXITLONG': EXITLONG
    })


def MTMZJ(df, N=12, M=6):
    """
    动力指标专家系统
    :param df:
    :param N:
    :param M:
    :return:
    """
    WMTM = MTM(df, N, M)

    ENTERLONG = CROSS(WMTM, 0)
    EXITLONG = CROSS(0, WMTM)
    return pd.DataFrame({
        'ENTERLONG': ENTERLONG, 'EXITLONG': EXITLONG
    })


def MTMZJ(df, N=12, M=6):
    """
    动力指标专家系统
    :param df:
    :param N:
    :param M:
    :return:
    """
    WMTM = MTM(df, N, M)

    ENTERLONG = CROSS(WMTM, 0)
    EXITLONG = CROSS(0, WMTM)
    return pd.DataFrame({
        'ENTERLONG': ENTERLONG, 'EXITLONG': EXITLONG
    })


def PSYZJ(df, N=1, LL=2, LH=5):
    """
    PSY心理线专家系统
    :param df:
    :param N:
    :param LL:
    :param LH:
    :return:
    """
    MYPSY = PSY(df, N, 1)

    ENTERLONG = CROSS(LL, MYPSY)
    EXITLONG = CROSS(MYPSY, LH)
    return pd.DataFrame({
        'ENTERLONG': ENTERLONG, 'EXITLONG': EXITLONG
    })


def ROCZJ(df, N=1, M=1):
    """
    变动速率专家系统
    :param df:
    :param N:
    :param M:
    :return:
    """
    WROC = ROC(df, N, M)

    ENTERLONG = CROSS(WROC, 0)
    EXITLONG = CROSS(0, WROC)
    return pd.DataFrame({
        'ENTERLONG': ENTERLONG, 'EXITLONG': EXITLONG
    })


def VRZJ(df, N=5, LL=5, LH=20):
    """
    VR容量比率专家系统
    :param df:
    :param N:
    :param LL:
    :param LH:
    :return:
    """
    CLOSE = df['close']
    OPEN = df['open']
    VOL = df['volume']
    AA = SUM((IF(CLOSE > OPEN, VOL, 0) + IF(CLOSE == OPEN, VOL / 2, 0)), N)
    BB = SUM((IF(CLOSE < OPEN, VOL, 0) + IF(CLOSE == OPEN, VOL / 2, 0)), N)
    WVR = AA / BB * 100

    ENTERLONG = CROSS(LL, WVR)
    EXITLONG = CROSS(WVR, LH)
    return pd.DataFrame({
        'ENTERLONG': ENTERLONG, 'EXITLONG': EXITLONG
    })


def DPSLZJ(dp, N1=2, N2=1):
    """
    大盘随机专家系统
    :param df:
    :param N1:
    :param N2:
    :return:
    """
    # 换手线函数方法不确定
    pass
    # INDEXC = dp['close']
    # INDEXL = dp['low']
    # INDEXH = dp['high']
    # RSV = (INDEXC - LLV(INDEXL, N1)) / (HHV(INDEXH, N1) - LLV(INDEXL, N1)) * 100
    # K = SMA(RSV, N2, 1)
    #
    # ENTERLONG = CROSS(K, 20)
    # EXITLONG = (CROSS(HSL, 5) or CROSS(K, 80))
    # return pd.DataFrame({
    #     'ENTERLONG': ENTERLONG, 'EXITLONG': EXITLONG
    # })
