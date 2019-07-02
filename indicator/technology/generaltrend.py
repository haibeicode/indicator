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
General Trend
大势型
@author Tab
"""

from indicator.base import *


def ABI(dp, M=10):
    """
    绝对广量指标
    :param M:
    :return:
    """
    # 广量指标方法未做
    pass
    # ADVANCE = dp['advance']
    # DECLINE = dp['decline']
    #
    # ABI = 100 * ABS(ADVANCE - DECLINE) / (ADVANCE + DECLINE)
    # MAABI = EMA(ABI, M)
    # return pd.DataFrame({
    #     'ABI': ABI, 'MAABI': MAABI
    # })


def ADL(dp, M=7):
    """
    腾落指标
    :param M:
    :return:
    """
    # 广量指标方法未做
    pass
    # ADVANCE = dp['advance']
    # DECLINE = dp['decline']
    #
    # ADL = SUM(ADVANCE - DECLINE, 0)
    # MAADL = MA(ADL, M)
    # return pd.DataFrame({
    #     'ADL': ADL, 'MAADL': MAADL
    # })


def ADR(dp, N=10, M=6):
    """
    涨跌比率
    :param N:
    :param M:
    :return:
    """
    # 广量指标方法未做
    pass
    # ADVANCE = dp['advance']
    # DECLINE = dp['decline']
    #
    # ADR = SUM(ADVANCE, N) / SUM(DECLINE, N)
    # MAADR = MA(ADR, M)
    # return pd.DataFrame({
    #     'ADR': ADR, 'MAADR': MAADR
    # })


def ARMS(dp, N=10, M=6):
    """
    阿姆氏指标
    :param N:
    :param M:
    :return:
    """
    # 广量指标方法未做
    pass
    # ADVANCE = dp['advance']
    # DECLINE = dp['decline']
    #
    # ARMS = EMA(ADVANCE / DECLINE, N)
    # MAARMS = MA(ARMS, M)
    # return pd.DataFrame({
    #     'ARMS': ARMS, 'MAARMS': MAARMS
    # })


def BTI(dp, N=10, M=6):
    """
    广量冲力指标
    :param N:
    :param M:
    :return:
    """
    # 广量指标方法未做
    pass
    # ADVANCE = dp['advance']
    # DECLINE = dp['decline']
    #
    # BTI = EMA(100 * ADVANCE / (ADVANCE + DECLINE), N)
    # MABTI = MA(BTI, M)
    # return pd.DataFrame({
    #     'BTI': BTI, 'MABTI': MABTI
    # })


def BTI(dp, N1=10, N2=6):
    """
    麦克连指标
    :param N1:
    :param N2:
    :return:
    """
    # 广量指标方法未做
    pass
    # ADVANCE = dp['advance']  # 上涨家数
    # DECLINE = dp['decline']  # 下跌家数
    #
    # DIF = ADVANCE - DECLINE
    #
    # MAMCL1 = EMA(DIF, N1)
    # MAMCL2 = EMA(DIF, N2)
    # MCL = MAMCL1 - MAMCL2
    # return pd.DataFrame({
    #     'MCL': MCL, 'MAMCL1': MAMCL1, 'MAMCL2': MAMCL2
    # })


def STIX(dp, M=6):
    """
    超买超卖指标
    :param M:
    :return:
    """
    # 广量指标方法未做
    pass
    # ADVANCE = dp['advance']
    # DECLINE = dp['decline']
    #
    # TBR = 100 * ADVANCE / (ADVANCE + DECLINE)
    # MATBR = EMA(TBR, M)
    # return pd.DataFrame({
    #     'TBR': TBR, 'MATBR': MATBR
    # })
