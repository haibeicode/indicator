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
@author Tab
"""

from indicator.base import *


def ABI(M=10):
    """
    绝对广量指标

    Param#1日简单移动平均 10

    输出绝对广量指标:100*上涨家数-下跌家数的绝对值/(上涨家数+下跌家数)
    输出MAABI:ABI的M日指数移动平均

    1.ABI绝对广量主要用于扫瞄瞬间极端的多头或空头力道；
    2.ABI值数据只会在0～100之间波动，数据越高代表市场立即转折的概率越大；ABI值高于95以上时，市场行情将极容易产生短期转折点；
    3.越高的数据代表市场转向的机会越大；
    4.随著上市公司家数递增，ABI 的极限数据须伴随修正；
    5.本指标可设参考线,对ABI作了归一化处理以减少误差。
    :param M:
    :return:
    """
    ABI = 100 * ABS(ADVANCE - DECLINE) / (ADVANCE + DECLINE)
    MAABI = EMA(ABI, M)

    return pd.DataFrame({
        'ABI': ABI, 'MAABI': MAABI
    })


def ADL(M=7):
    """
    腾落指标

    Param#1日简单移动平均 7

    输出腾落指标:上涨家数-下跌家数的历史累和
    输出MAADL:ADL的M日简单移动平均

    1.ADL与指数顶背离时，指数向下反转机会大；
    2.ADL与指数底背离时，指数向上反转机会大；
    3.ADL须与ADR 、OBOS等指标配合使用。
    :param M:
    :return:
    """
    ADL = SUM(ADVANCE - DECLINE, 0)
    MAADL = MA(ADL, M)
    DICT = {'ADL': ADL, 'MAADL': MAADL}
    return pd.DataFrame(DICT)


def ADR(N=10, M=6):
    """
    涨跌比率

    Param#1日涨跌比率 10
    Param#2日简单移动平均 6

    输出涨跌比率:上涨家数的N日累和/下跌家数的N日累和
    输出MAADR:ADR的M日简单移动平均

    1.ADR一般常态分于0.5～1.5的间；
    2.ADR>1.5 ，大盘回档机会大；
    3.ADR<0.65，大盘反弹机会大；
    4.ADR<0.3或0.5，容易形成底部
    :param N:
    :param M:
    :return:
    """
    ADR = SUM(ADVANCE, N) / SUM(DECLINE, N)
    MAADR = MA(ADR, M)
    DICT = {'ADR': ADR, 'MAADR': MAADR}
    return pd.DataFrame(DICT)


def ARMS(N=10, M=6):
    """
    阿姆氏指标

    Param#1日阿姆氏
    Param#2日移动平均

    输出阿姆氏指标:上涨家数/下跌家数的N日指数移动平均 21
    输出MAARMS:ARMS的M日简单移动平均 6

    1.R＝上涨家数/下跌家数
    2.ARMS＝R的N日异同移动平均
    3.计算ARMS的M日简单移动平均
    4.参数N一般设置为21日参数M一般设置为6日

      ARMS指标绝大多数时候是在低位徘徊，这时候对大盘的超买超卖有一定提示作
    用，但这种提示只能说明股市在短时间的超买超卖情况，对大势的长期发展方向
    的提示作用不大。
      ARMS指标突然升高，意味股市即将构筑底部。这个突然升高的具体数值没有硬
    性规定，关键在于ARMS指标能否创出一段时间的新高。
      ARMS指标如果出现急剧增长，往往意味着股市将出现重大转变。这种急剧增长
    是指ARMS指标迅速升高到10以上，其在历史中出现的次数不多，但往往能准确预
    测股市的顶底。。
    :param N:
    :param M:
    :return:
    """
    ARMS = EMA(ADVANCE / DECLINE, N)
    MAARMS = MA(ARMS, M)
    DICT = {'ARMS': ARMS, 'MAARMS': MAARMS}
    return pd.DataFrame(DICT)


def BTI(N=10, M=6):
    """
    广量冲力指标

   Param#1日 10
    Param#2日 5

    输出广量冲力指标:100*上涨家数/(上涨家数+下跌家数)的N日指数移动平均
    输出MABTI:BTI的M日简单移动平均

    1.62～65为超买区；
    2.35～38为超卖区；
    3.当BTI 产生极大的冲力时，为大多头来临的前兆；
    4.本指标可设参考线。
    :param N:
    :param M:
    :return:
    """
    BTI = EMA(100 * ADVANCE / (ADVANCE + DECLINE), N)
    MABTI = MA(BTI, M)
    DICT = {'BTI': BTI, 'MABTI': MABTI}
    return pd.DataFrame(DICT)


def BTI(N1=10, N2=6):
    """
    麦克连指标

    Param#1日快线指数移动平均 19
    Param#2日慢线指数移动平均 39

    DIF赋值:上涨家数-下跌家数
    EMA1赋值:DIF的N1日指数移动平均
    EMA2赋值:DIF的N2日指数移动平均
    输出麦克连指标:EMA1-EMA2
    输出MAMCL1:EMA1
    输出MAMCL2:EMA2

    1.+25～+35的间为超买区，曲线穿越此区后再度反转跌破+25，为卖出信号；
    2.-25～-35的间为超卖区，曲线穿越此区后再度反转突破-25，为买进信号；
    3.以0轴为中心，正值时，为多头市场；负值时，为空头市场；
    4.本指标可设参考线。
    :param N1:
    :param N2:
    :return:
    """
    DIF = ADVANCE - DECLINE
    EMA1 = EMA(DIF, N1)
    EMA2 = EMA(DIF, N2)
    MCL = EMA1 - EMA2
    MAMCL1 = EMA1
    MAMCL2 = EMA2
    DICT = {'MCL': MCL, 'MAMCL1': MAMCL1, 'MAMCL2': MAMCL2}
    return pd.DataFrame(DICT)


def STIX(M=6):
    """
    超买超卖指标

    Param#1日指数移动平均

    输出TBR:100*上涨家数/(上涨家数+下跌家数)
    输出MATBR:TBR的M日指数移动平均

    1.常态行情时，STIX一般波动于45～56的间，强势行情波动于42～58之间；
    2.指标上升至56～58间时，短线应卖出；
    3.指标下降至42～45间时，短线应买进；
    4.本指标可设参考线。
    :param M:
    :return:
    """
    TBR = 100 * ADVANCE / (ADVANCE + DECLINE)
    MATBR = EMA(TBR, M)
    DICT = {'TBR': TBR, 'MATBR': MATBR}
    return pd.DataFrame(DICT)
