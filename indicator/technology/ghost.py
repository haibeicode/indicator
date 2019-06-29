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
鬼型
@author Tab
"""
from indicator.base import *


def CYS(df):
    """
    市场盈亏
    :param df:
    :return:
    """
    CLOSE = df['close']
    VOL = df['volume']
    AMOUNT = df['amount']

    CYC13 = 0.01 * EMA(AMOUNT, 13) / EMA(VOL, 13)
    CYS = (CLOSE - CYC13) / CYC13 * 100
    return pd.DataFrame({
        'CYC13': CYC13, 'CYS': CYS
    })


def CYS(df):
    """
    主力控盘
    :param df:
    :return:
    """
    CLOSE = df['close']
    OPEN = df['open']
    LOW = df['low']
    HIGH = df['high']
    VOL = df['volume']

    VAR1 = CLOSE - LOW
    VAR2 = HIGH - LOW
    VAR3 = CLOSE - HIGH
    VAR4 = IF(HIGH > LOW, (VAR1 / VAR2 + VAR3 / VAR2) * VOL, 0)

    CYW = SUM(VAR4, 10) / 10000

    return pd.DataFrame({
        'CYW': CYW
    })


def CYC(df, P1=5, P2=13, P3=34):
    """
    成本均线
    :param df:
    :param P1:
    :param P2:Dragon
    :param P3:
    :return:
    """
    # 即时行情函数方法不确定
    pass
    # CLOSE = df['close']
    # HIGH = df['high']
    # LOW = df['low']
    # VOL = df['volume']
    # AMOUNT = df['amount']
    # JJJ = IF(DYNAINFO(8) > 0.01, 0.01 * DYNAINFO(10) / DYNAINFO(8), DYNAINFO(3))
    # DDD = (DYNAINFO(5) < 0.01 or DYNAINFO(6) < 0.01)
    # JJJT = IF(DDD, 1, (JJJ < (DYNAINFO(5) + 0.01) and JJJ > (DYNAINFO(6) - 0.01)))
    #
    # CYC1 = IF(JJJT, 0.01 * EMA(AMOUNT, P1) / EMA(VOL, P1), EMA((HIGH + LOW + CLOSE) / 3, P1))
    # CYC2 = IF(JJJT, 0.01 * EMA(AMOUNT, P2) / EMA(VOL, P2), EMA((HIGH + LOW + CLOSE) / 3, P2))
    # CYC3 = IF(JJJT, 0.01 * EMA(AMOUNT, P3) / EMA(VOL, P3), EMA((HIGH + LOW + CLOSE) / 3, P3))
    # CYC = IF(JJJT, DMA(AMOUNT / (100 * VOL), 100 * VOL / FINANCE(7)), EMA((HIGH + LOW + CLOSE) / 3, 120))
    #
    # return pd.DataFrame({
    #     'CYC1': CYC1, 'CYC2': CYC2, 'CYC3': CYC3, 'CYC': CYC
    # })


def CYW(df):
    """
    博弈K线长度
    :param df:
    :return:
    """
    # 获利盘比例方法不确定
    pass
    # CLOSE = df['close']
    # OPEN = df['open']
    #
    # KL = 100 * (WINNER(CLOSE) - WINNER(OPEN))
    # return pd.DataFrame({
    #     'KL': KL
    # })
