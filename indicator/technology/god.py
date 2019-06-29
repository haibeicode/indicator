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
Chat
神型
@author Tab
"""
from indicator.base import *


def SGXDT(df, dp, P1=5, P2=10):
    """
    心电图(需下载日线)
    :param df:
    :param P1:
    :param P2:
    :return:
    """
    CLOSE = df['close']
    INDEXC = dp['close']
    QR = CLOSE / INDEXC * 1000
    MQR1 = MA(QR, P1)
    MQR2 = MA(QR, P2)

    return pd.DataFrame({
        'QR': QR, 'MQR1': MQR1, 'MQR2': MQR2
    })


def SGSMX(df, dp, N=50):
    """
    生命线(需下载日线)
    :param df:
    :param N:
    :return:
    """
    CLOSE = df['close']
    HIGH = df['high']
    LOW = df['low']
    INDEXC = dp['close']
    INDEXH = dp['high']
    INDEXL = dp['low']

    H1 = HHV(HIGH, N)
    L1 = LLV(LOW, N)
    H2 = HHV(INDEXH, N)
    L2 = LLV(INDEXL, N)
    ZY = CLOSE / INDEXC * 2000

    ZY1 = EMA(ZY, 3)
    ZY2 = EMA(ZY, 17)
    ZY3 = EMA(ZY, 34)

    return pd.DataFrame({
        'ZY1': ZY1, 'ZY2': ZY2, 'ZY3': ZY3
    })


def SGLB(df, dp):
    """
    量比(需下载日线)
    :param df:
    :return:
    """
    VOL = df['volume']
    INDEXV = dp['volume']
    ZY2 = VOL / INDEXV * 1000

    LB = ZY2
    MA5 = MA(ZY2, 5)
    MA10 = MA(ZY2, 10)

    return pd.DataFrame({
        'LB': LB, 'MA5': MA5, 'MA10': MA10
    })


def SGPF(df, dp):
    """
    强势股评分(需下载日线)
    :param df:
    :return:
    """
    CLOSE = df['close']
    INDEXC = dp['close']
    ZY1 = CLOSE / INDEXC * 1000
    A1 = IF(ZY1 > HHV(ZY1, 3), 10, 0)
    A2 = IF(ZY1 > HHV(ZY1, 5), 15, 0)
    A3 = IF(ZY1 > HHV(ZY1, 10), 20, 0)
    A4 = IF(ZY1 > HHV(ZY1, 2), 10, 0)
    A5 = COUNT(ZY1 > REF(ZY1, 1), 9) * 5

    PF = A1 + A2 + A3 + A4 + A5

    return pd.DataFrame({
        'PF': PF
    })


def SGNDB(df, P1=5, P2=10):
    """
    脑电波(神系)
    :param df:
    :param P1:
    :param P2:
    :return:
    """
    # 有效数据周期数方法不确定
    pass

    # CLOSE = df['close']
    # H = df['high']
    # L = df['low']
    #
    # HH = IF(CLOSE / REF(CLOSE, 1) > 1.093 and L > REF(H, 1), 2 * CLOSE - REF(CLOSE, 1) - H, 2 * CLOSE - H - L)
    # V1 = BARSCOUNT(CLOSE)
    # V2 = 2 * REF(CLOSE, V1) - REF(H, V1) - REF(L, V1)
    #
    # DK = SUM(HH, 0) + V2
    # MDK5 = MA(DK, P1)
    # MDK10 = MA(DK, P2)
    #
    # return pd.DataFrame({
    #     'DK': DK, 'MDK5': MDK5, 'MDK10': MDK10
    # })
