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


def VR(data_frame, M1=26, M2=100, M3=200):
    """

    :param data_frame:
    :param M1:
    :param M2:
    :param M3:
    :return:
    """
    VOL = data_frame['volume']
    CLOSE = data_frame['close']
    LC = REF(CLOSE, 1)
    VR = SUM(IF(CLOSE > LC, VOL, 0), M1) / SUM(IF(CLOSE <= LC, VOL, 0), M1) * 100
    a = M2
    b = M3
    return pd.DataFrame({
        'VR': VR, 'a': a, 'b': b
    })


def VRSI(data_frame, N=6):
    """

    :param data_frame:
    :param N:
    :return:
    """
    VOL = data_frame['volume']
    vrsi = SMA(MAX(VOL - REF(VOL, 1), 0), N, 1) / \
           SMA(ABS(VOL - REF(VOL, 1)), N, 1) * 100

    return pd.DataFrame({'VRSI': vrsi})


def CR(data_frame, N=26, M1=5, M2=10, M3=20):
    """

    :param data_frame:
    :param N:
    :param M1:
    :param M2:
    :param M3:
    :return:
    """
    HIGH = data_frame['high']
    LOW = data_frame['low']
    CLOSE = data_frame['close']
    VOL = data_frame['volume']
    MID = (HIGH + LOW + CLOSE) / 3

    CR = SUM(MAX(0, HIGH - REF(MID, 1)), N) / SUM(MAX(0, REF(MID, 1) - LOW), N) * 100
    MA1 = REF(MA(CR, M1), M1 / 2.5 + 1)
    MA2 = REF(MA(CR, M2), M2 / 2.5 + 1)
    MA3 = REF(MA(CR, M3), M3 / 2.5 + 1)
    return pd.DataFrame({
        'CR': CR, 'MA1': MA1, 'MA2': MA2, 'MA3': MA3
    })


def ARBR(data_frame, M1=26, M2=70, M3=150):
    """

    :param data_frame:
    :param M1:
    :param M2:
    :param M3:
    :return:
    """
    HIGH = data_frame['high']
    LOW = data_frame['low']
    CLOSE = data_frame['close']
    OPEN = data_frame['open']
    AR = SUM(HIGH - OPEN, M1) / SUM(OPEN - LOW, M1) * 100
    BR = SUM(MAX(0, HIGH - REF(CLOSE, 1)), M1) / \
         SUM(MAX(0, REF(CLOSE, 1) - LOW), M1) * 100
    a = M2
    b = M3
    return pd.DataFrame({
        'AR': AR, 'BR': BR, 'a': a, 'b': b
    })


def VSTD(data_frame, N=10):
    """

    :param data_frame:
    :param N:
    :return:
    """
    VOL = data_frame['volume']
    vstd = STD(VOL, N)
    return pd.DataFrame({'VSTD': vstd})
