"""
5.	压力支撑指标
主要用于分析股价目前收到的压力和支撑
布林带 BOLL
麦克指标 MIKE
"""
from common.indicator.base import *


def BOLL(data_frame, N=20, P=2):
    """
    布林线
    :param data_frame:
    :param N:
    :param P:
    :return:
    """
    C = data_frame['close']
    boll = MA(C, N)
    UB = boll + P * STD(C, N)
    LB = boll - P * STD(C, N)
    DICT = {'BOLL': boll, 'UB': UB, 'LB': LB}

    return pd.DataFrame(DICT)


def MIKE(data_frame, N=12):
    """
    MIKE指标
    指标说明
    MIKE是另外一种形式的路径指标。
    买卖原则
    1  WEAK-S，MEDIUM-S，STRONG-S三条线代表初级、中级、强力支撑。
    2  WEAK-R，MEDIUM-R，STRONG-R三条线代表初级、中级、强力压力。
    :param data_frame:
    :param N:
    :return:
    """
    HIGH = data_frame.high
    LOW = data_frame.low
    CLOSE = data_frame.close

    TYP = (HIGH + LOW + CLOSE) / 3
    LL = LLV(LOW, N)
    HH = HHV(HIGH, N)

    WR = TYP + (TYP - LL)
    MR = TYP + (HH - LL)
    SR = 2 * HH - LL
    WS = TYP - (HH - TYP)
    MS = TYP - (HH - LL)
    SS = 2 * LL - HH
    return pd.DataFrame({
        'WR': WR, 'MR': MR, 'SR': SR,
        'WS': WS, 'MS': MS, 'SS': SS
    })


def BBI(data_frame, N1=3, N2=6, N3=12, N4=24):
    """
    多空指标
    :param data_frame:
    :param N1:
    :param N2:
    :param N3:
    :param N4:
    :return:
    """
    C = data_frame['close']
    bbi = (MA(C, N1) + MA(C, N2) + MA(C, N3) + MA(C, N4)) / 4
    DICT = {'BBI': bbi}

    return pd.DataFrame(DICT)


def MFI(data_frame, N=14):
    """
    资金指标
    TYP := (HIGH + LOW + CLOSE)/3;
    V1:=SUM(IF(TYP>REF(TYP,1),TYP*VOL,0),N)/SUM(IF(TYP<REF(TYP,1),TYP*VOL,0),N);
    MFI:100-(100/(1+V1));
    赋值: (最高价 + 最低价 + 收盘价)/3
    V1赋值:如果TYP>1日前的TYP,返回TYP*成交量(手),否则返回0的N日累和/如果TYP<1日前的TYP,返回TYP*成交量(手),否则返回0的N日累和
    输出资金流量指标:100-(100/(1+V1))
    :param data_frame:
    :param N:
    :return:
    """
    C = data_frame['close']
    H = data_frame['high']
    L = data_frame['low']
    VOL = data_frame['volume']
    TYP = (C + H + L) / 3
    V1 = SUM(IF(TYP > REF(TYP, 1), TYP * VOL, 0), N) / \
         SUM(IF(TYP < REF(TYP, 1), TYP * VOL, 0), N)
    mfi = 100 - (100 / (1 + V1))
    DICT = {'MFI': mfi}

    return pd.DataFrame(DICT)


def ATR(data_frame, N=14):
    """
    输出TR:(最高价-最低价)和昨收-最高价的绝对值的较大值和昨收-最低价的绝对值的较大值
    输出真实波幅:TR的N日简单移动平均
    算法：今日振幅、今日最高与昨收差价、今日最低与昨收差价中的最大值，为真实波幅，求真实波幅的N日移动平均

    参数：N　天数，一般取14
    :param data_frame:
    :param N:
    :return:
    """
    C = data_frame['close']
    H = data_frame['high']
    L = data_frame['low']
    TR = MAX(MAX((H - L), ABS(REF(C, 1) - H)), ABS(REF(C, 1) - L))
    atr = MA(TR, N)
    return pd.DataFrame({'TR': TR, 'ATR': atr})



def DDI(data_frame, N=13, N1=26, M=1, M1=5):
    """
    方向标准离差指数 分析DDI柱状线，由红变绿(正变负)，卖出信号参考；由绿变红，买入信号参考。
    :param data_frame:
    :param N:
    :param N1:
    :param M:
    :param M1:
    :return:
    """

    H = data_frame['high']
    L = data_frame['low']
    DMZ = IF((H + L) > (REF(H, 1) + REF(L, 1)),
             MAX(ABS(H - REF(H, 1)), ABS(L - REF(L, 1))), 0)
    DMF = IF((H + L) < (REF(H, 1) + REF(L, 1)),
             MAX(ABS(H - REF(H, 1)), ABS(L - REF(L, 1))), 0)
    DIZ = SUM(DMZ, N) / (SUM(DMZ, N) + SUM(DMF, N))
    DIF = SUM(DMF, N) / (SUM(DMF, N) + SUM(DMZ, N))
    ddi = DIZ - DIF
    ADDI = SMA(ddi, N1, M)
    AD = MA(ADDI, M1)
    DICT = {'DDI': ddi, 'ADDI': ADDI, 'AD': AD}

    return pd.DataFrame(DICT)


def shadow(data_frame):
    """
    上下影线指标
    :param data_frame:
    :return:
    """
    return {
        'LOW': lower_shadow(data_frame), 'UP': upper_shadow(data_frame),
        'BODY': body(data_frame), 'BODY_ABS': body_abs(data_frame), 'PRICE_PCG': price_pcg(data_frame)
    }


def lower_shadow(data_frame):
    """
    下影线
    :param data_frame:
    :return:
    """
    return abs(data_frame.low - MIN(data_frame.open, data_frame.close))


def upper_shadow(data_frame):
    """
    上影线
    :param data_frame:
    :return:
    """
    return abs(data_frame.high - MAX(data_frame.open, data_frame.close))


def body_abs(data_frame):
    """

    :param data_frame:
    :return:
    """
    return abs(data_frame.open - data_frame.close)


def body(data_frame):
    """

    :param data_frame:
    :return:
    """
    return data_frame.close - data_frame.open


def price_pcg(data_frame):
    """

    :param data_frame:
    :return:
    """
    return body(data_frame) / data_frame.open


def amplitude(data_frame):
    """

    :param data_frame:
    :return:
    """
    return (data_frame.high - data_frame.low) / data_frame.low
