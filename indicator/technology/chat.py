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
图表型
@author Tab
"""
from indicator.base import *


def ZX(df):
    """
    重心线
    :param df:
    :return:
    """
    AMOUNT = df['amount']
    VOL = df['volume']

    AV = 0.01 * AMOUNT / VOL

    return pd.DataFrame({
        'AV': AV
    })


def PUCU(df, N=2):
    """
    逆时钟曲线
    :param df:
    :param N:
    :return:
    """
    CLOSE = df['close']
    VOL = df['volume']

    PU = MA(CLOSE, N)
    CU = MA(VOL, N)

    return pd.DataFrame({
        'PU': PU, 'CU': CU
    })
