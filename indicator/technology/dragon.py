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
Dragon
龙型
@author Tab
"""
from indicator.base import *


def RAD(df, dp, D=3, S=30, M=30):
    """
    威力雷达(需下载日线)
    :param df:
    :param D:
    :param S:
    :param M:
    :return:
    """
    OPEN = df['open']
    CLOSE = df['close']
    HIGH = df['high']
    LOW = df['low']

    INDEXO = dp['open']
    INDEXC = dp['close']
    INDEXH = dp['high']
    INDEXL = dp['low']

    SM = (OPEN + HIGH + CLOSE + LOW) / 4
    SMID = MA(SM, D)
    IM = (INDEXO + INDEXH + INDEXL + INDEXC) / 4
    IMID = MA(IM, D)
    SI1 = (SMID - REF(SMID, 1)) / SMID
    II = (IMID - REF(IMID, 1)) / IMID

    RADER1 = SUM((SI1 - II) * 2, S) * 1000
    RADERMA = SMA(RADER1, M, 1)

    return pd.DataFrame({
        'RADER1': RADER1, 'RADERMA': RADERMA
    })


def LON(df, N=10):
    """
    龙系长线
    :param df:
    :param N:
    :return:
    """
    VOL = df['volume']
    CLOSE = df['close']
    HIGH = df['high']
    LOW = df['low']

    LC = REF(CLOSE, 1)
    VID = SUM(VOL, 2) / (((HHV(HIGH, 2) - LLV(LOW, 2))) * 100)
    RC = (CLOSE - LC) * VID
    LONG = SUM(RC, 0)
    DIFF = SMA(LONG, 10, 1)
    DEA = SMA(LONG, 20, 1)

    LON = DIFF - DEA
    LONMA = MA(LON, N)

    return pd.DataFrame({
        'LON': LON, 'LONMA': LONMA
    })


def SHT(df, N=5):
    """
    龙系短线
    :param df:
    :param N:
    :return:
    """
    VOL = df['volume']
    CLOSE = df['close']

    VAR1 = MA((VOL - REF(VOL, 1)) / REF(VOL, 1), 5)
    VAR2 = (CLOSE - MA(CLOSE, 24)) / MA(CLOSE, 24) * 100

    MY = VAR2 * (1 + VAR1)
    SHTMA = MA(SHT, N)

    return pd.DataFrame({
        'MY': MY, 'SHTMA': SHTMA
    })


def ZLJC(df):
    """
    主力进出
    :param df:
    :return:
    """
    VOL = df['volume']
    CLOSE = df['close']
    LOW = df['low']
    HIGH = df['high']
    VAR1 = (CLOSE + LOW + HIGH) / 3
    VAR2 = SUM(((VAR1 - REF(LOW, 1)) - (HIGH - VAR1)) * VOL / 100000 / (HIGH - LOW), 0)
    VAR3 = EMA(VAR2, 1)

    JCS = VAR3
    JCM = MA(VAR3, 12)
    JCL = MA(VAR3, 26)

    return pd.DataFrame({
        'JCS': JCS, 'JCM': JCM, 'JCL': JCL
    })


def ZLMM(df):
    """
    主力买卖
    :param df:
    :return:
    """
    CLOSE = df['close']
    LC = REF(CLOSE, 1)
    RSI2 = SMA(MAX(CLOSE - LC, 0), 12, 1) / SMA(ABS(CLOSE - LC), 12, 1) * 100
    RSI3 = SMA(MAX(CLOSE - LC, 0), 18, 1) / SMA(ABS(CLOSE - LC), 18, 1) * 100

    MMS = MA(3 * RSI2 - 2 * SMA(MAX(CLOSE - LC, 0), 16, 1) / SMA(ABS(CLOSE - LC), 16, 1) * 100, 3)
    MMM = EMA(MMS, 8)
    MML = MA(3 * RSI3 - 2 * SMA(MAX(CLOSE - LC, 0), 12, 1) / SMA(ABS(CLOSE - LC), 12, 1) * 100, 5)

    return pd.DataFrame({
        'MMS': MMS, 'MMM': MMM, 'MML': MML
    })


def ADVOL(df):
    """
    龙系离散量
    :param df:
    :return:
    """
    VOL = df['volume']
    CLOSE = df['close']
    HIGH = df['high']
    LOW = df['low']

    ADVOL = SUM(((CLOSE - LOW) - (HIGH - CLOSE)) * VOL / 10000 / (HIGH - LOW), 0)
    MA1 = MA(ADVOL, 30)
    MA2 = MA(MA1, 100)

    return pd.DataFrame({
        'ADVOL': ADVOL, 'MA1': MA1, 'MA2': MA2
    })


def SLZT(df):
    """
    神龙在天
    :param df:
    :return:
    """
    # 抛物转向方法不确定
    pass
    #
    # CLOSE = df['close']
    # HIGH = df['high']
    #
    # VAR2 = HHV(HIGH, 70)
    # VAR3 = HHV(HIGH, 20)
    #
    # BL = MA(CLOSE, 125)
    # HL = BL + 2 * STD(CLOSE, 170)
    # ZL = BL - 2 * STD(CLOSE, 145)
    # QL = SAR(125, 1, 7)
    # RL = VAR2 * 0.83
    # LL = VAR3 * 0.91
    #
    # return pd.DataFrame({
    #     'BL': BL, 'HL': HL, 'ZL': ZL, 'QL': QL, 'RL': RL, 'LL': LL
    # })
