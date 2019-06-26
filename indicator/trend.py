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
@author Tab
"""
from indicator.base import *


def CHO(data_frame, N1=10, N2=20, M=6):
    """
    佳庆指标 CHO

    Param#1日快线移动平均 N1=10
    Param#2日慢线移动平均 N2=20
    Param#3日移动平均 M=6

    MID赋值:成交量(手)*(2*收盘价-最高价-最低价)/(最高价+最低价)的历史累和
    输出佳庆指标:MID的N1日简单移动平均-MID的N2日简单移动平均
    输出MACHO:CHO的M日简单移动平均

    1.CHO 曲线产生急促的「凸起」时，代表行情即将向上或向下反转；
    2.股价>90 天平均线，CHO由负转正时，买进；
    3.股价<90 天平均线，CHO由正转负时，卖出；
    4.本指标也可设参考线，自定超买超卖的界限值；
    5.本指标可配合OBOS、ENVELOPE同时使用。
    :param data_frame:
    :param N1:
    :param N2:
    :param M:
    :return:
    """
    HIGH = data_frame['high']
    LOW = data_frame['low']
    CLOSE = data_frame['close']
    VOL = data_frame['volume']
    MID = SUM(VOL * (2 * CLOSE - HIGH - LOW) / (HIGH + LOW), 0)
    CHO = MA(MID, N1) - MA(MID, N2)
    MACHO = MA(CHO, M)
    return pd.DataFrame({
        'CHO': CHO, 'MACHO': MACHO
    })


def DMI(data_frame, M1=14, M2=6):
    """
    趋向指标

    Param#1日DMI; N=10
    Param#2日移动平均 M=6

    MTR赋值:最高价-最低价和最高价-1日前的收盘价的绝对值的较大值和1日前的收盘价-最低价的绝对值的较大值的N日累和
    赋值:最高价-1日前的最高价
    赋值:1日前的最低价-最低价
    DMP赋值:如果HD>0并且HD>LD,返回HD,否则返回0的N日累和
    DMM赋值:如果LD>0并且LD>HD,返回LD,否则返回0的N日累和
    输出PDI: DMP*100/MTR
    输出MDI: DMM*100/MTR
    输出ADX: MDI-PDI的绝对值/(MDI+PDI)*100的M日简单移动平均
    输出ADXR:(ADX+M日前的ADX)/2

    用法：市场行情趋向明显时，指标效果理想。
    PDI(上升方向线)    MDI(下降方向线)  ADX(趋向平均值)
    1.PDI线从下向上突破MDI线，显示有新多头进场，为买进信号；
    2.PDI线从上向下跌破MDI线，显示有新空头进场，为卖出信号；
    3.ADX值持续高于前一日时，市场行情将维持原趋势；
    4.ADX值递减，降到20以下，且横向行进时，市场气氛为盘整；
    5.ADX值从上升倾向转为下降时，表明行情即将反转。
    参数：N　统计天数； M  间隔天数，一般为14、6
    :param data_frame:
    :param M1:
    :param M2:
    :return:
    """
    HIGH = data_frame['high']
    LOW = data_frame['low']
    CLOSE = data_frame['close']

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


def DPO(data_frame, N=20, M=6):
    """
    区间震荡线

    Param#1日区间震荡线; N=20
    Param#2日移动平均; M=6

    输出区间震荡线:收盘价-N/2+1日前的收盘价的N日简单移动平均
    输出MADPO:DPO的M日简单移动平均

    1.DOP>0 ，表示目前处于多头市场；DOP<0 ，表示目前处于空头市场；
    2.在0 轴上方设定一条超买线，当股价波动至超买线时，会形成短期高点；
    3.在0 轴下方设定一条超卖线，当股价波动至超卖线时，会形成短期低点；
    4.超买超卖的范围随个股不同而不同，使用者应自行调整；
    5.本指标可设参考线。
    :param data_frame:
    :param N:
    :param M:
    :return:
    """
    CLOSE = data_frame['close']
    DPO = CLOSE - REF(MA(CLOSE, N), N / 2 + 1)
    MADPO = MA(DPO, M)
    DICT = {'DPO': DPO, 'MADPO': MADPO}

    return pd.DataFrame(DICT)


def EMV(data_frame, N=14, M=9):
    """
    简易波动指标

    Param#1日EMV; N=14
    Param#2日移动平均 M=9

    VOLUME赋值:成交量(手)的N日简单移动平均/成交量(手)
    MID赋值:100*(最高价+最低价-1日前的最高价+最低价)/(最高价+最低价)
    输出EMV:MID*VOLUME*(最高价-最低价)/最高价-最低价的N日简单移动平均的N日简单移动平均
    输出MAEMV:EMV的M日简单移动平均

    1.EMV 由下往上穿越0 轴时，视为中期买进信号；
    2.EMV 由上往下穿越0 轴时，视为中期卖出信号；
    3.EMV 的平均线穿越0 轴，产生假信号的机会较少；
    4.当ADX 低于±DI时，本指标失去效用；
    5.须长期使用EMV 指标才能获得最佳利润。
    :param data_frame:
    :param N:
    :param M:
    :return:
    """
    VOL = data_frame['volume']
    HIGH = data_frame['high']
    LOW = data_frame['low']

    VOLUME = MA(VOL, N) / VOL
    MID = 100 * (HIGH + LOW - REF(HIGH + LOW, 1)) / (HIGH + LOW)
    EMV = MA(MID * VOLUME * (HIGH - LOW) / MA(HIGH - LOW, N), N)
    MAEMV = MA(EMV, M)
    DICT = {'EMV': EMV, 'MAEMV': MAEMV}

    return pd.DataFrame(DICT)


def VMACD(data_frame, SHORT=12, LONG=26, MID=9):
    """
    量平滑异同平均

    Param#1日快线移动平均; SHORT=12
    Param#2日慢线移动平均; LONG=26
    Param#3日移动平均; MID=9

    输出DIF:成交量(手)的SHORT日指数移动平均-成交量(手)的LONG日指数移动平均
    输出DEA:DIF的MID日指数移动平均
    输出平滑异同平均:DIF-DEA,COLORSTICK
    :param data_frame:
    :param SHORT:
    :param LONG:
    :param MID:
    :return:
    """
    VOL = data_frame['volume']
    DIF = EMA(VOL, SHORT) - EMA(VOL, LONG)
    DEA = EMA(DIF, MID)  # , COLORSTICK
    DICT = {'DIF': DIF, 'DEA': DEA}
    return pd.DataFrame(DICT)


def QACD(data_frame, N1=12, N2=26, M=9):
    """
    快速异同平均

    Param#1日快线移动平均; N1=12
    Param#2日慢线移动平均; N2=26
    Param#3日移动平均; M=9

    输出DIF:收盘价的N1日指数移动平均-收盘价的N2日指数移动平均
    输出平滑异同平均:DIF的M日指数移动平均
    输出DDIF:DIF-MACD

    1.DIF 向上交叉MACD，买进；DIF 向下交叉MACD，卖出；
    2.DIF 连续两次向下交叉MACD，将造成较大的跌幅；
    3.DIF 连续两次向上交叉MACD，将造成较大的涨幅；
    4.DIF 与股价形成背离时所产生的信号，可信度较高；
    5.DMA、MACD、TRIX 三者构成一组指标群，互相验证。
    :param data_frame:
    :param N1:
    :param N2:
    :param M:
    :return:
    """
    CLOSE = data_frame['close']
    DIF = EMA(CLOSE, N1) - EMA(CLOSE, N2)
    MACD = EMA(DIF, M)
    DDIF = DIF - MACD
    return pd.DataFrame({
        'DIF': DIF, 'MACD': MACD, 'DDIF': DDIF
    })


def VPT(data_frame, N=51, M=6):
    """
    量价曲线

    Param#1日量价曲线; N=51
    Param#2日移动平均 M=6

    输出量价曲线:成交量(手)*(收盘价-1日前的收盘价)/1日前的收盘价的N日累和
    输出MAVPT:VPT的M日简单移动平均

    1.VPT 由下往上穿越0 轴时，为买进信号；
    2.VPT 由上往下穿越0 轴时，为卖出信号；
    3.股价一顶比一顶高，VPT 一顶比一顶低时，暗示股价将反转下跌；
    4.股价一底比一底低，VPT 一底比一底高时，暗示股价将反转上涨；
    5.VPT 可搭配EMV 和WVAD指标使用效果更佳。

    :param data_frame:
    :param N:
    :param M:
    :return:
    """
    VOL = data_frame['volume']
    CLOSE = data_frame['close']
    VPT = SUM(VOL * (CLOSE - REF(CLOSE, 1)) / REF(CLOSE, 1), N)
    MAVPT = MA(VPT, M)
    return pd.DataFrame({
        'VPT': VPT, 'MAVPT': MAVPT
    })


def WVAD(data_frame, N=24, M=6):
    """
    威廉变异离散量

    Param#1日威廉变异离散量; N=24
    Param#2日移动平均 M=6

    输出WVAD:(收盘价-开盘价)/(最高价-最低价)*成交量(手)的N日累和/10000
    输出MAWVAD:WVAD的M日简单移动平均

    1.WVAD由下往上穿越0 轴时，视为长期买进信号；
    2.WVAD由上往下穿越0 轴时，视为长期卖出信号；
    3.当ADX 低于±DI时，本指标失去效用；
    4.长期使用WVAD指标才能获得最佳利润；
    5.本指标可与EMV 指标搭配使用。
    :param data_frame:
    :param N:
    :param M:
    :return:
    """
    CLOSE = data_frame['close']
    OPEN = data_frame['open']
    HIGH = data_frame['high']
    LOW = data_frame['low']
    VOL = data_frame['volume']
    WVAD = SUM((CLOSE - OPEN) / (HIGH - LOW) * VOL, N) / 10000
    MAWVAD = MA(WVAD, M)
    DICT = {'WVAD': WVAD, 'MAWVAD': MAWVAD}
    return pd.DataFrame(DICT)


def DBQR(data_frame, N=5, M1=10, M2=20, M3=60):
    """
    对比强弱(需下载日线)
    Param#1日对比强弱; N=5
    Param#2日移动平均; M1=10
    Param#3日移动平均; M2=20
    Param#4日移动平均; M3=60

    输出ZS:(大盘的收盘价-N日前的大盘的收盘价)/N日前的大盘的收盘价
    输出GG:(收盘价-N日前的收盘价)/N日前的收盘价
    输出MADBQR1:GG的M1日简单移动平均
    输出MADBQR2:GG的M2日简单移动平均
    输出MADBQR3:GG的M3日简单移动平均

    对比强弱指标包含有两条指标线,一条是对应指数的强弱
    线。另外一条是个股的强弱线。当个股强弱线与指数强弱
    线发生金叉时，表明个股开始强过大盘，是买入时机。
    当个股强弱线与指数强弱线发生死叉时，表明个股开始弱
    于大盘，是卖出时机。对比强弱指标是一个短线指标。

    注意：此指标使用到了大盘的数据，所以需要下载完整的
    日线数据,否则显示可能不正确
    :param data_frame:
    :param N:
    :param M1:
    :param M2:
    :param M3:
    :return:
    """
    CLOSE = data_frame['close']
    ZS = (INDEXC - REF(INDEXC, N)) / REF(INDEXC, N)
    GG = (CLOSE - REF(CLOSE, N)) / REF(CLOSE, N)
    MADBQR1 = MA(GG, M1)
    MADBQR2 = MA(GG, M2)
    MADBQR3 = MA(GG, M3)
    DICT = {'ZS': ZS, 'GG': GG, 'MADBQR1': MADBQR1, 'MADBQR2': MADBQR2, 'MADBQR3': MADBQR3}
    return pd.DataFrame(DICT)


def JS(data_frame, N=5, M1=5, M2=10, M3=20):
    """
    加速线

    Param#1日加速线; N=5
    Param#2日移动平均; M1=5
    Param#3日移动平均; M2=10
    Param#4日移动平均; M3=20

    输出加速线:100*(收盘价-N日前的收盘价)/(N*N日前的收盘价)
    输出MAJS1:JS的M1日简单移动平均
    输出MAJS2:JS的M2日简单移动平均
    输出MAJS3:JS的M3日简单移动平均

    加速线指标是衡量股价涨速的工具,加速线指标上升表明
    股价上升动力增加,加速线指标下降表明股价下降压力增加。
    加速线适用于DMI表明趋势明显时(DMI.ADX大于20)使用:
    1.如果加速线在0值附近形成平台，则表明既不是最好的
      买入时机也不是最好的卖入时机；
    2.在加速线发生金叉后,均线形成底部是买入时机。
    3.在加速线发生死叉后,均线形成顶部是卖出时机。
    :param data_frame:
    :param N:
    :param M1:
    :param M2:
    :param M3:
    :return:
    """
    CLOSE = data_frame['close']
    JS = 100 * (CLOSE - REF(CLOSE, N)) / (N * REF(CLOSE, N))
    MAJS1 = MA(JS, M1)
    MAJS2 = MA(JS, M2)
    MAJS3 = MA(JS, M3)
    DICT = {'JS': JS, 'MAJS1': MAJS1, 'MAJS2': MAJS2, 'MAJS3': MAJS3}
    return pd.DataFrame(DICT)


def CYE(data_frame):
    """
    市场趋势

    MAL赋值:收盘价的5日简单移动平均
    MAS赋值:收盘价的20日简单移动平均的5日简单移动平均
    输出CYEL:(MAL-1日前的MAL)/1日前的MAL*100
    输出CYES:(MAS-1日前的MAS)/1日前的MAS*100

    1. CYE指标又叫趋势指标,是计算机模拟人的感觉用数值分析的方法对即日的K线进行一次拟合和趋势的判断;
    2.CYE以 0轴为界，其上为上升趋势,否则为下降趋势.
    :param data_frame:
    :return:
    """
    CLOSE = data_frame['close']
    MAL = MA(CLOSE, 5)
    MAS = MA(MA(CLOSE, 20), 5)
    CYEL = (MAL - REF(MAL, 1)) / REF(MAL, 1) * 100
    CYES = (MAS - REF(MAS, 1)) / REF(MAS, 1) * 100
    DICT = {'CYEL': CYEL, 'CYES': CYES}
    return pd.DataFrame(DICT)


def QR(data_frame, N=21):
    """
    强弱指标(需下载日线)

    参数1:Param#1; N=21

    输出个股: (收盘价-N日前的收盘价)/N日前的收盘价*100
    输出 大盘: (大盘的收盘价-N日前的大盘的收盘价)/N日前的大盘的收盘价*100
    输出 强弱值:个股-大盘的2日指数移动平均,COLORSTICK

    指标攀升表明个股走势渐强于大盘，后市看好；指标滑落
    表明个股走势弱于大盘，可择机换股。同时要结合大盘走
    势研判，应选择大盘转暖或走牛时出击。

    注意：此指标使用到了大盘的数据，所以需要下载完整的
    日线数据,否则显示可能不正确
    :param data_frame:
    :param N:
    :return:
    """
    CLOSE = data_frame['close']
    GG = (CLOSE - REF(CLOSE, N)) / REF(CLOSE, N) * 100;
    DP = (INDEXC - REF(INDEXC, N)) / REF(INDEXC, N) * 100;
    QRZ = EMA(GG - DP, 2)  # , COLORSTICK;
    DICT = {'GG': GG, 'DP': DP, 'QRZ': QRZ}
    return pd.DataFrame(DICT)


def GDX(data_frame, N=30, M=9):
    """
    轨道线

    参数1:Param#1; N=30
    参数2:Param#2; M=9

    AA赋值:(2*收盘价+最高价+最低价)/4-收盘价的N日简单移动平均的绝对值/收盘价的N日简单移动平均
    输出 轨道:以AA为权重收盘价的动态移动平均
    输出压力线:(1+M/100)*轨道
    输出 支撑线:(1-M/100)*轨道

    通道理论公式，是一种用技术手段和经验判断来决定买
    卖股票的方法。该公式对趋势线做了平滑和修正处理，
    更精确的反应了股价运行规律。当股价上升到压力线时，
    投资者就卖出股票，而当股价下跌到支撑线时，投资者
    就进行相应的补进。
    :param data_frame:
    :param N:
    :param M:
    :return:
    """
    CLOSE = data_frame['close']
    HIGH = data_frame['high']
    LOW = data_frame['low']
    AA = ABS((2 * CLOSE + HIGH + LOW) / 4 - MA(CLOSE, N)) / MA(CLOSE, N)
    GD: DMA(CLOSE, AA)
    YLX: (1 + M / 100) * GD
    ZCX: (1 - M / 100) * GD
    DICT = {'GD': GD, 'YLX': YLX, 'ZCX': ZCX}
    return pd.DataFrame(DICT)


def JLHB(data_frame, N=7, M=5):
    """
    绝路航标

    参数1:Param#1; N=7
    参数2:Param#2; M=5

    VAR1赋值:(收盘价-60日内最低价的最低值)/(60日内最高价的最高值-60日内最低价的最低值)*80
    输出 B:VAR1的N日[1日权重]移动平均
    输出 VAR2:B的M日[1日权重]移动平均
    输出 绝路航标:如果B上穿VAR2ANDB<40,返回50,否则返回0

    反趋势类选股指标。综合了动量观念、强弱指标与移动
    平均线的优点，在计算过程中主要研究高低价位与收市
    价的关系，反映价格走势的强弱和超买超卖现象。在市
    场短期超买超卖的预测方面又较敏感。
    :param data_frame:
    :param N:
    :param M:
    :return:
    """
    CLOSE = data_frame['close']
    HIGH = data_frame['high']
    LOW = data_frame['low']
    VAR1 = (CLOSE - LLV(LOW, 60)) / (HHV(HIGH, 60) - LLV(LOW, 60)) * 80
    B = SMA(VAR1, N, 1)
    VAR2 = SMA(B, M, 1)
    JLHB = IF(CROSS(B, VAR2) and B < 40, 50, 0)
    DICT = {'B': B, 'VAR2': VAR2, 'JLHB': JLHB}
    return pd.DataFrame(DICT)


##############
#
##############

def PBX(data_frame, N1=3, N2=5, N3=8, N4=13, N5=18, N6=24):
    """
    瀑布线
    :param data_frame:
    :param N1:
    :param N2:
    :param N3:
    :param N4:
    :param N5:
    :param N6:
    :return:
    """
    C = data_frame['close']
    PBX1 = (EMA(C, N1) + EMA(C, 2 * N1) + EMA(C, 4 * N1)) / 3
    PBX2 = (EMA(C, N2) + EMA(C, 2 * N2) + EMA(C, 4 * N2)) / 3
    PBX3 = (EMA(C, N3) + EMA(C, 2 * N3) + EMA(C, 4 * N3)) / 3
    PBX4 = (EMA(C, N4) + EMA(C, 2 * N4) + EMA(C, 4 * N4)) / 3
    PBX5 = (EMA(C, N5) + EMA(C, 2 * N5) + EMA(C, 4 * N5)) / 3
    PBX6 = (EMA(C, N6) + EMA(C, 2 * N6) + EMA(C, 4 * N6)) / 3
    DICT = {'PBX1': PBX1, 'PBX2': PBX2, 'PBX3': PBX3,
            'PBX4': PBX4, 'PBX5': PBX5, 'PBX6': PBX6}
    return pd.DataFrame(DICT)


def EXPMA(data_frame, P1=5, P2=10, P3=20, P4=60):
    """
    指数平均线 EXPMA
    :param data_frame:
    :param P1:
    :param P2:
    :param P3:
    :param P4:
    :return:
    """
    CLOSE = data_frame['close']
    MA1 = EMA(CLOSE, P1)
    MA2 = EMA(CLOSE, P2)
    MA3 = EMA(CLOSE, P3)
    MA4 = EMA(CLOSE, P4)
    return pd.DataFrame({
        'MA1': MA1, 'MA2': MA2, 'MA3': MA3, 'MA4': MA4
    })
