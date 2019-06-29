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
Trend Indicators
趋势型
@author Tab
"""
from indicator.base import *


def CHO(df, N1=10, N2=20, M=6):
    """
    佳庆指标
    :param df:
    :param N1:
    :param N2:
    :param M:
    :return:
    """
    HIGH = df['high']
    LOW = df['low']
    CLOSE = df['close']
    VOL = df['volume']
    MID = SUM(VOL * (2 * CLOSE - HIGH - LOW) / (HIGH + LOW), 0)
    CHO = MA(MID, N1) - MA(MID, N2)
    MACHO = MA(CHO, M)
    return pd.DataFrame({
        'CHO': CHO, 'MACHO': MACHO
    })


def DMI(df, M1=14, M2=6):
    """
    趋向指标
    :param df:
    :param M1:
    :param M2:
    :return:
    """
    HIGH = df['high']
    LOW = df['low']
    CLOSE = df['close']

    TR = SUM(MAX(MAX(HIGH - LOW, ABS(HIGH - REF(CLOSE, 1))),
                 ABS(LOW - REF(CLOSE, 1))), M1)
    HD = HIGH - REF(HIGH, 1)
    LD = REF(LOW, 1) - LOW
    DMP = SUM(IFAND(HD > 0, HD > LD, HD, 0), M1)
    DMM = SUM(IFAND(LD > 0, LD > HD, LD, 0), M1)
    DI1 = DMP * 100 / TR
    DI2 = DMM * 100 / TR
    ADX = MA(ABS(DI2 - DI1) / (DI1 + DI2) * 100, M2)
    ADXR = (ADX + REF(ADX, M2)) / 2

    return pd.DataFrame({
        'DI1': DI1, 'DI2': DI2,
        'ADX': ADX, 'ADXR': ADXR
    })


def DPO(df, N=20, M=6):
    """
    区间震荡线
    :param df:
    :param N:
    :param M:
    :return:
    """
    CLOSE = df['close']
    DPO = CLOSE - REF(MA(CLOSE, N), N / 2 + 1)
    MADPO = MA(DPO, M)
    DICT = {'DPO': DPO, 'MADPO': MADPO}

    return pd.DataFrame(DICT)


def EMV(df, N=14, M=9):
    """
    简易波动指标
    :param df:
    :param N:
    :param M:
    :return:
    """
    VOL = df['volume']
    HIGH = df['high']
    LOW = df['low']

    VOLUME = MA(VOL, N) / VOL
    MID = 100 * (HIGH + LOW - REF(HIGH + LOW, 1)) / (HIGH + LOW)
    EMV = MA(MID * VOLUME * (HIGH - LOW) / MA(HIGH - LOW, N), N)
    MAEMV = MA(EMV, M)
    DICT = {'EMV': EMV, 'MAEMV': MAEMV}

    return pd.DataFrame(DICT)


def MACD(series, fast, slow, mid):
    """
    平滑异同平均
    :param series:
    :param fast:
    :param slow:
    :param mid:
    :return:
    """
    EMAFAST = EMA(series, fast)
    EMASLOW = EMA(series, slow)
    DIFF = EMAFAST - EMASLOW
    DEA = EMA(DIFF, mid)
    MACD = (DIFF - DEA) * 2

    return pd.DataFrame({'DIFF': DIFF, 'DEA': DEA, 'MACD': MACD})


def VMACD(df, SHORT=12, LONG=26, MID=9):
    """
    量平滑异同平均
    :param df:
    :param SHORT:
    :param LONG:
    :param MID:
    :return:
    """
    VOL = df['volume']
    DIF = EMA(VOL, SHORT) - EMA(VOL, LONG)
    DEA = EMA(DIF, MID)
    DICT = {'DIF': DIF, 'DEA': DEA}
    return pd.DataFrame(DICT)


def QACD(df, N1=12, N2=26, M=9):
    """
    快速异同平均
    :param df:
    :param N1:
    :param N2:
    :param M:
    :return:
    """
    CLOSE = df['close']
    DIF = EMA(CLOSE, N1) - EMA(CLOSE, N2)
    MACD = EMA(DIF, M)
    DDIF = DIF - MACD
    return pd.DataFrame({
        'DIF': DIF, 'MACD': MACD, 'DDIF': DDIF
    })


def VPT(df, N=51, M=6):
    """
    量价曲线
    :param df:
    :param N:
    :param M:
    :return:
    """
    VOL = df['volume']
    CLOSE = df['close']
    VPT = SUM(VOL * (CLOSE - REF(CLOSE, 1)) / REF(CLOSE, 1), N)
    MAVPT = MA(VPT, M)
    return pd.DataFrame({
        'VPT': VPT, 'MAVPT': MAVPT
    })


def WVAD(df, N=24, M=6):
    """
    威廉变异离散量
    :param df:
    :param N:
    :param M:
    :return:
    """
    CLOSE = df['close']
    OPEN = df['open']
    HIGH = df['high']
    LOW = df['low']
    VOL = df['volume']
    WVAD = SUM((CLOSE - OPEN) / (HIGH - LOW) * VOL, N) / 10000
    MAWVAD = MA(WVAD, M)
    DICT = {'WVAD': WVAD, 'MAWVAD': MAWVAD}
    return pd.DataFrame(DICT)


def DBQR(df, dp, N=5, M1=10, M2=20, M3=60):
    """
    对比强弱(需下载日线)
    :param df:
    :param N:
    :param M1:
    :param M2:
    :param M3:
    :return:
    """
    CLOSE = df['close']
    INDEXC = dp['close']
    ZS = (INDEXC - REF(INDEXC, N)) / REF(INDEXC, N)
    GG = (CLOSE - REF(CLOSE, N)) / REF(CLOSE, N)
    MADBQR1 = MA(GG, M1)
    MADBQR2 = MA(GG, M2)
    MADBQR3 = MA(GG, M3)
    DICT = {'ZS': ZS, 'GG': GG, 'MADBQR1': MADBQR1, 'MADBQR2': MADBQR2, 'MADBQR3': MADBQR3}
    return pd.DataFrame(DICT)


def JS(df, N=5, M1=5, M2=10, M3=20):
    """
    加速线
    :param df:
    :param N:
    :param M1:
    :param M2:
    :param M3:
    :return:
    """
    CLOSE = df['close']
    JS = 100 * (CLOSE - REF(CLOSE, N)) / (N * REF(CLOSE, N))
    MAJS1 = MA(JS, M1)
    MAJS2 = MA(JS, M2)
    MAJS3 = MA(JS, M3)
    DICT = {'JS': JS, 'MAJS1': MAJS1, 'MAJS2': MAJS2, 'MAJS3': MAJS3}
    return pd.DataFrame(DICT)


def CYE(df):
    """
    市场趋势
    :param df:
    :return:
    """
    CLOSE = df['close']
    MAL = MA(CLOSE, 5)
    MAS = MA(MA(CLOSE, 20), 5)
    CYEL = (MAL - REF(MAL, 1)) / REF(MAL, 1) * 100
    CYES = (MAS - REF(MAS, 1)) / REF(MAS, 1) * 100
    DICT = {'CYEL': CYEL, 'CYES': CYES}
    return pd.DataFrame(DICT)


def QR(df, dp, N=21):
    """
    强弱指标(需下载日线)
    :param df:
    :param N:
    :return:
    """
    CLOSE = df['close']
    INDEXC = dp['close']
    GG = (CLOSE - REF(CLOSE, N)) / REF(CLOSE, N) * 100;
    DP = (INDEXC - REF(INDEXC, N)) / REF(INDEXC, N) * 100;
    QRZ = EMA(GG - DP, 2)
    DICT = {'GG': GG, 'DP': DP, 'QRZ': QRZ}
    return pd.DataFrame(DICT)


def GDX(df, N=30, M=9):
    """
    轨道线
    :param df:
    :param N:
    :param M:
    :return:
    """
    CLOSE = df['close']
    HIGH = df['high']
    LOW = df['low']
    AA = ABS((2 * CLOSE + HIGH + LOW) / 4 - MA(CLOSE, N)) / MA(CLOSE, N)
    GD = DMA(CLOSE, AA)
    YLX = (1 + M / 100) * GD
    ZCX = (1 - M / 100) * GD
    DICT = {'GD': GD, 'YLX': YLX, 'ZCX': ZCX}
    return pd.DataFrame(DICT)


def JLHB(df, N=7, M=5):
    """
    绝路航标
    :param df:
    :param N:
    :param M:
    :return:
    """
    CLOSE = df['close']
    HIGH = df['high']
    LOW = df['low']
    VAR1 = (CLOSE - LLV(LOW, 60)) / (HHV(HIGH, 60) - LLV(LOW, 60)) * 80
    B = SMA(VAR1, N, 1)
    VAR2 = SMA(B, M, 1)
    JLHB = IF(CROSS(B, VAR2) and B < 40, 50, 0)
    DICT = {'B': B, 'VAR2': VAR2, 'JLHB': JLHB}
    return pd.DataFrame(DICT)


##############
#
##############


def ASI(df, M1=26, M2=10):
    """
    LC=REF(CLOSE,1);
    AA=ABS(HIGH-LC);
    BB=ABS(LOW-LC);
    CC=ABS(HIGH-REF(LOW,1));
    DD=ABS(LC-REF(OPEN,1));
    R=IF(AA>BB AND AA>CC,AA+BB/2+DD/4,IF(BB>CC AND BB>AA,BB+AA/2+DD/4,CC+DD/4));
    X=(CLOSE-LC+(CLOSE-OPEN)/2+LC-REF(OPEN,1));
    SI=16*X/R*MAX(AA,BB);
    ASI:SUM(SI,M1);
    ASIT:MA(ASI,M2);
    """
    CLOSE = df['close']
    HIGH = df['high']
    LOW = df['low']
    OPEN = df['open']
    LC = REF(CLOSE, 1)
    AA = ABS(HIGH - LC)
    BB = ABS(LOW - LC)
    CC = ABS(HIGH - REF(LOW, 1))
    DD = ABS(LC - REF(OPEN, 1))

    R = IFAND(AA > BB, AA > CC, AA + BB / 2 + DD / 4,
              IFAND(BB > CC, BB > AA, BB + AA / 2 + DD / 4, CC + DD / 4))
    X = (CLOSE - LC + (CLOSE - OPEN) / 2 + LC - REF(OPEN, 1))
    SI = 16 * X / R * MAX(AA, BB)
    ASI = SUM(SI, M1)
    ASIT = MA(ASI, M2)
    return pd.DataFrame({
        'ASI': ASI, 'ASIT': ASIT
    })


def PVT(df):
    """

    :param df:
    :return:
    """
    CLOSE = df['close']
    VOL = df['volume']
    PVT = SUM((CLOSE - REF(CLOSE, 1)) / REF(CLOSE, 1) * VOL, 0)
    return pd.DataFrame({'PVT': PVT})


def ARBR(df, M1=26, M2=70, M3=150):
    """

    :param df:
    :param M1:
    :param M2:
    :param M3:
    :return:
    """
    HIGH = df['high']
    LOW = df['low']
    CLOSE = df['close']
    OPEN = df['open']
    AR = SUM(HIGH - OPEN, M1) / SUM(OPEN - LOW, M1) * 100
    BR = SUM(MAX(0, HIGH - REF(CLOSE, 1)), M1) / \
         SUM(MAX(0, REF(CLOSE, 1) - LOW), M1) * 100
    a = M2
    b = M3
    return pd.DataFrame({
        'AR': AR, 'BR': BR, 'a': a, 'b': b
    })


def VSTD(df, N=10):
    """

    :param df:
    :param N:
    :return:
    """
    VOL = df['volume']
    vstd = STD(VOL, N)
    return pd.DataFrame({'VSTD': vstd})
