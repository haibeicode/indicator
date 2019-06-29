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
Quantity and price Indicators
成交量型
@author Tab
"""
from indicator.base import *


def AMO(df, M1=5, M2=10):
    """
    成交金额
    :param M1:
    :param M2:
    :return:
    """
    AMOUNT = df['amount']
    AMOW = AMOUNT / 10000.0
    AMO1 = MA(AMOW, M1)
    AMO2 = MA(AMOW, M2)
    return pd.DataFrame({
        'AMOW': AMOW, 'AMO1': AMO1, 'AMO2': AMO2
    })


def OBV(df, M=30):
    """
    累积能量线
    :param df:
    :param M:
    :return:
    """
    VOL = df['volume']
    CLOSE = df['close']
    VA = IF(CLOSE > REF(CLOSE, 1), VOL, -VOL)

    OBV = SUM(IF(CLOSE == REF(CLOSE, 1), 0, VA), 0)
    MAOBV = MA(OBV, M)

    return pd.DataFrame({
        'OBV': OBV, 'MAOBV': MAOBV
    })


def QVOL(df, M1=5, M2=10):
    """
    成交量
    :param M1:
    :param M2:
    :return:
    """
    VOL = df['volume']
    VOLUME = VOL
    MAVOL1 = MA(VOLUME, M1)
    MAVOL2 = MA(VOLUME, M2)
    return pd.DataFrame({
        'VOLUME': VOLUME, 'MAVOL1': MAVOL1, 'MAVOL2': MAVOL2
    })


def VRSI(df, N1=6, N2=12, N3=24):
    """
    相对强弱量
    :param df:
    :param N1:
    :param N2:
    :param N3:
    :return:
    """
    VOL = df['volume']
    LC = REF(VOL, 1)

    RSI1 = SMA(MAX(VOL - LC, 0), N1, 1) / SMA(ABS(VOL - LC), N1, 1) * 100
    RSI2 = SMA(MAX(VOL - LC, 0), N2, 1) / SMA(ABS(VOL - LC), N2, 1) * 100
    RSI3 = SMA(MAX(VOL - LC, 0), N3, 1) / SMA(ABS(VOL - LC), N3, 1) * 100

    return pd.DataFrame({
        'RSI1': RSI1, 'RSI2': RSI2, 'RSI3': RSI3
    })


def DBQRV(df, dp, N=5):
    """
    对比强弱量(需下载日线)
    :param df:
    :param N:
    :return:
    """
    VOL = df['volume']
    INDEXV = dp['volume']
    ZS = (INDEXV - REF(INDEXV, N)) / REF(INDEXV, N)
    GG = (VOL - REF(VOL, N)) / REF(VOL, N)
    return pd.DataFrame({
        'ZS': ZS, 'GG': GG
    })


def DBLB(df, dp, N=5, M=5):
    """
    对比量比(需下载日线)
    :param df:
    :param N:
    :param M:
    :return:
    """
    VOL = df['volume']
    INDEXV = dp['volume']
    GG = VOL / SUM(REF(VOL, 1), N)
    ZS = INDEXV / SUM(REF(INDEXV, 1), N)

    DBLB = GG / ZS;
    MADBLB = MA(DBLB, M);
    return pd.DataFrame({
        'DBLB': DBLB, 'MADBLB': MADBLB
    })


def QVOLTDX(df, M1=5, M2=10):
    """
    成交量(虚拟)
    :param M1:
    :param M2:
    :return:
    """
    # 分钟方法不确定
    pass
    # VOL = df['volume']
    # TOTAL = IF(PERIOD == 1, 5,
    #            IF(PERIOD == 2, 15, IF(PERIOD == 3, 30, IF(PERIOD == 4, 60, IF(PERIOD == 5, TOTALFZNUM, 1)))))
    # MTIME = MOD(FROMOPEN, TOTAL)
    # CTIME = IF(MTIME < 0.5, TOTAL, MTIME)
    #
    # VVOL = IF((CURRBARSCOUNT == 1 and DYNAINFO(8) > 1), VOL * (TOTAL + 3) / (CTIME + 3), DRAWNULL)
    # # STICKLINE((CURRBARSCOUNT = 1 and DYNAINFO(8) > 1), VVOL, 0, -1, -1), COLOR00C0C0
    # VOLUME = VOL
    # MAVOL1 = MA(VOLUME, M1)
    # MAVOL2 = MA(VOLUME, M2)
    # return pd.DataFrame({
    #     'VVOL': VVOL, 'VOLUME': VOLUME, 'MAVOL1': MAVOL1, 'MAVOL2': MAVOL2
    # })


def AMOTDX(df, M1=5, M2=10):
    """
    成交量(虚拟)
    :param M1:
    :param M2:
    :return:
    """
    # 分钟方法不确定
    pass
    # AMOUNT = df['amount']
    # TOTAL = IF(PERIOD == 1, 5,
    #            IF(PERIOD == 2, 15, IF(PERIOD == 3, 30, IF(PERIOD == 4, 60, IF(PERIOD == 5, TOTALFZNUM, 1)))))
    # MTIME = MOD(FROMOPEN, TOTAL)
    # CTIME = IF(MTIME < 0.5, TOTAL, MTIME)
    #
    # VAMO = IF((CURRBARSCOUNT == 1 and DYNAINFO(8) > 1), AMOUNT / 10000.0 * TOTAL / CTIME, DRAWNULL)
    # # STICKLINE((CURRBARSCOUNT = 1 and DYNAINFO(8) > 1), VAMO, 0, -1, -1), COLOR00C0C0
    # AMOW = AMOUNT / 10000.0
    # AMO1 = MA(AMOW, M1)
    # AMO2 = MA(AMOW, M2)
    # return pd.DataFrame({
    #     'VAMO': VAMO, 'AMOW': AMOW, 'AMO1': AMO1, 'AMO2': AMO2
    # })


def HSCOL(df, N=5):
    """
    换手柱
    :param df:
    :param N:
    :return:
    """
    # SETCODE函数方法不确定
    pass
    # VOL = df['volume']
    # HSCOL = IF((SETCODE == 0 or SETCODE == 1), 100 * VOL, VOL) / (FINANCE(7) / 100)
    # MAHSL = MA(HSCOL, N)
    # return pd.DataFrame({
    #     'HSCOL': HSCOL, 'MAHSL': MAHSL
    # })
