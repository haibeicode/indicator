"""

2.	反趋向指标
主要捕捉趋势的转折点

随机指标KDJ
乖离率 BIAS
变动速率 ROC
顺势指标 CCI
威廉指标 W&R
震荡量(变动速率) OSC
相对强弱指标 RSI
动态买卖指标 ADTM

"""

from common.indicator.base import *


def CCI(data_frame, N=14):
    """
    商品路径指标

    天数:Param#1天 14

    TYP赋值:(最高价+最低价+收盘价)/3
    输出CCI:(TYP-TYP的N日简单移动平均)/(0.015*TYP的N日平均绝对偏差)

    1.CCI 为正值时，视为多头市场；为负值时，视为空头市场；
    2.常态行情时，CCI 波动于±100 的间；强势行情，CCI 会超出±100 ；
    3.CCI>100 时，买进，直到CCI<100 时，卖出；
    4.CCI<-100 时，放空，直到CCI>-100 时，回补。

    :param data_frame:
    :param N: 天数
    :return:
    """
    typ = (data_frame['high'] + data_frame['low'] + data_frame['close']) / 3
    cci = ((typ - MA(typ, N)) / (0.015 * AVEDEV(typ, N)))
    a = 100
    b = -100

    return pd.DataFrame({
        'CCI': cci, 'a': a, 'b': b
    })


def KDJ(data_frame, N=9, M1=3, M2=3):
    """
    随机指标

    天数:Param#1天 9
    天数:Param#2天 3
    天数:Param#3天 3

    RSV赋值:(收盘价-N日内最低价的最低值)/(N日内最高价的最高值-N日内最低价的最低值)*100
    输出K:RSV的M1日[1日权重]移动平均
    输出D:K的M2日[1日权重]移动平均
    输出J:3*K-2*D

    1.指标>80 时，回档机率大；指标<20时，反弹机率大；
    2.K在20左右向上交叉D时，视为买进信号；
    3.K在80左右向下交叉D时，视为卖出信号；
    4.J>100 时，股价易反转下跌；J<0 时，股价易反转上涨；
    5.KDJ 波动于50左右的任何信号，其作用不大。

    :param data_frame:
    :param N:天数
    :param M1:天数
    :param M2:天数
    :return:
    """
    C = data_frame['close']
    H = data_frame['high']
    L = data_frame['low']

    RSV = (C - LLV(L, N)) / (HHV(H, N) - LLV(L, N)) * 100
    K = SMA(RSV, M1)
    D = SMA(K, M2)
    J = 3 * K - 2 * D
    DICT = {'KDJ_K': K, 'KDJ_D': D, 'KDJ_J': J}
    return pd.DataFrame(DICT)


def MFT(data_frame, N=9):
    """
    资金流量指标

    Param#1日资金流量 14
    Param#2日资金流量 6

    赋值: (最高价 + 最低价 + 收盘价)/3
    V1赋值:如果TYP>1日前的TYP,返回TYP*成交量(手),否则返回0的N日累和/如果TYP<1日前的TYP,返回TYP*成交量(手),否则返回0的N日累和
    输出资金流量指标:100-(100/(1+V1))

    1.MFI>80 为超买，当其回头向下跌破80 时，为短线卖出时机；
    2.MFI<20 为超卖，当其回头向上突破20 时，为短线买进时机；
    3.MFI>80，而产生背离现象时，视为卖出信号；
    4.MFI<20，而产生背离现象时，视为买进信号。
    :param data_frame:
    :param N:
    :return:
    """
    CLOSE = data_frame['close']
    HIGH = data_frame['high']
    LOW = data_frame['low']
    VOL = data_frame['volume']

    TYP = (HIGH + LOW + CLOSE) / 3
    V1 = SUM(IF(TYP > REF(TYP, 1), TYP * VOL, 0), N) / SUM(IF(TYP < REF(TYP, 1), TYP * VOL, 0), N)
    MFI = 100 - (100 / (1 + V1))
    return pd.DataFrame(MFI)


def MTM(data_frame, N=12, M=6):
    """
    动量线

    Param#1日资金流量 14
    Param#2日资金流量 6

    输出动量线:收盘价-N日前的收盘价
    输出MTMMA:MTM的M日简单移动平均

    MTM线　:当日收盘价与N日前的收盘价的差；
    MTMMA线:对上面的差值求N日移动平均；
    参数：N 间隔天数，也是求移动平均的天数，一般取6
    用法：
    1.MTM从下向上突破MTMMA，买入信号；
    2.MTM从上向下跌破MTMMA，卖出信号；
    3.股价续创新高，而MTM未配合上升，意味上涨动力减弱；
    4.股价续创新低，而MTM未配合下降，意味下跌动力减弱；
    5.股价与MTM在低位同步上升，将有反弹行情；反之，从高位同步下降，将有回落走势。

    :param data_frame:
    :param N:
    :param M:
    :return:
    """
    C = data_frame.close
    mtm = C - REF(C, N)
    MTMMA = MA(mtm, M)
    DICT = {'MTM': mtm, 'MTMMA': MTMMA}
    return pd.DataFrame(DICT)


def OSC(data_frame, N=20, M=6):
    """
    变动速率线

    Param#1日变动速率 20
    Param#1日移动平均 6

    输出变动速率线:100*(收盘价-收盘价的N日简单移动平均)
    输出MAOSC:OSC的M日指数平滑移动平均

    1.OSC 以100 为中轴线，OSC>100 为多头市场；OSC<100 为空头市场；
    2.OSC 向上交叉其平均线时，买进；OSC 向下交叉其平均线时卖出；
    3.OSC 在高水平或低水平与股价产生背离时，应注意股价随时有反转的可能；
    4.OSC 的超买超卖界限值随个股不同而不同，使用者应自行调整

    :param data_frame:
    :param N:
    :param M:
    :return:
    """
    C = data_frame['close']
    OS = (C - MA(C, N)) * 100
    MAOSC = EMA(OS, M)
    DICT = {'OSC': OS, 'MAOSC': MAOSC}

    return pd.DataFrame(DICT)


def ROC(data_frame, N=12, M=6):
    """
    变动率指标

    Param#1日变动率 12
    Param#1日移动平均 6

    输出ROC:100*(收盘价-N日前的收盘价)/N日前的收盘价
    输出MAROC:ROC的M日简单移动平均

    1.本指标的超买超卖界限值随个股不同而不同，使用者应自行调整；
    2.本指标的超买超卖范围，一般介于±6.5之间；
    3.本指标用法请参考MTM 指标用法；
    4.本指标可设参考线。

    :param data_frame:
    :param N:
    :param M:
    :return:
    """
    C = data_frame['close']
    roc = 100 * (C - REF(C, N)) / REF(C, N)
    ROCMA = MA(roc, M)
    DICT = {'ROC': roc, 'ROCMA': ROCMA}

    return pd.DataFrame(DICT)


def RSI(data_frame, N1=12, N2=26, N3=9):
    """
    相对强弱指标

    Param#1日RSI[相对强弱] 6
    Param#2日RSI[相对强弱] 12
    Param#3日RSI[相对强弱] 24

    LC赋值:1日前的收盘价
    输出RSI1:收盘价-LC和0的较大值的N1日[1日权重]移动平均/收盘价-LC的绝对值的N1日[1日权重]移动平均*100
    输出RSI2:收盘价-LC和0的较大值的N2日[1日权重]移动平均/收盘价-LC的绝对值的N2日[1日权重]移动平均*100
    输出RSI3:收盘价-LC和0的较大值的N3日[1日权重]移动平均/收盘价-LC的绝对值的N3日[1日权重]移动平均*100

    1.RSI>80 为超买，RSI<20 为超卖；
    2.RSI 以50为中界线，大于50视为多头行情，小于50视为空头行情；
    3.RSI 在80以上形成Ｍ头或头肩顶形态时，视为向下反转信号；
    4.RSI 在20以下形成Ｗ底或头肩底形态时，视为向上反转信号；
    5.RSI 向上突破其高点连线时，买进；RSI 向下跌破其低点连线时，卖出。

    :param data_frame:
    :param N1:
    :param N2:
    :param N3:
    :return:
    """
    CLOSE = data_frame['close']
    LC = REF(CLOSE, 1)
    RSI1 = SMA(MAX(CLOSE - LC, 0), N1) / SMA(ABS(CLOSE - LC), N1) * 100
    RSI2 = SMA(MAX(CLOSE - LC, 0), N2) / SMA(ABS(CLOSE - LC), N2) * 100
    RSI3 = SMA(MAX(CLOSE - LC, 0), N3) / SMA(ABS(CLOSE - LC), N3) * 100
    DICT = {'RSI1': RSI1, 'RSI2': RSI2, 'RSI3': RSI3}

    return pd.DataFrame(DICT)


def KD(data_frame, N=9, M1=3, M2=3):
    """
    随机指标

    天数:Param#1天 9
    天数:Param#2天 3
    天数:Param#3天 3

    RSV赋值:(收盘价-N日内最低价的最低值)/(N日内最高价的最高值-N日内最低价的最低值)*100
    输出K:RSV的M1日[1日权重]移动平均
    输出D:K的M2日[1日权重]移动平均

    :param data_frame:
    :param N:
    :param M1:
    :param M2:
    :return:
    """
    CLOSE = data_frame['close']
    LOW = data_frame['low']
    HIGH = data_frame['high']
    RSV = (CLOSE - LLV(LOW, N)) / (HHV(HIGH, N) - LLV(LOW, N)) * 100
    K = SMA(RSV, M1, 1)
    D = SMA(K, M2, 1)
    DICT = {'K': K, 'D': D}
    return pd.DataFrame(DICT)


def SKDJ(data_frame, N=9, M=3):
    """
    慢速随机指标

    天数:Param#1天 9
    天数:Param#2天 3

    LOWV赋值:N日内最低价的最低值
    HIGHV赋值:N日内最高价的最高值
    RSV赋值:(收盘价-LOWV)/(HIGHV-LOWV)*100的M日指数移动平均
    输出K:RSV的M日指数移动平均
    输出D:K的M日简单移动平均

    1.指标>80 时，回档机率大；指标<20 时，反弹机率大；
    2.K在20左右向上交叉D时，视为买进信号；
    3.K在80左右向下交叉D时，视为卖出信号；
    4.SKDJ波动于50左右的任何讯号，其作用不大

    :param data_frame:
    :param N:
    :param M:
    :return:
    """
    CLOSE = data_frame['close']
    LOWV = LLV(data_frame['low'], N)
    HIGHV = HHV(data_frame['high'], N)
    RSV = EMA((CLOSE - LOWV) / (HIGHV - LOWV) * 100, M)
    K = EMA(RSV, M)
    D = MA(K, M)
    DICT = {'RSV': RSV, 'SKDJ_K': K, 'SKDJ_D': D}

    return pd.DataFrame(DICT)


def UDL(data_frame, N1=3, N2=5, N3=10, N4=20, M=6):
    """
    引力线

    天数:Param#1天 3
    天数:Param#2天 5
    天数:Param#3天 10
    天数:Param#4天 20
    Param#5天移动平均 6

    输出引力线:(收盘价的N1日简单移动平均+收盘价的N2日简单移动平均+收盘价的N3日简单移动平均+收盘价的N4日简单移动平均)/4
    输出MAUDL:UDL的M日简单移动平均

    1.本指标的超买超卖界限值随个股不同而不同，使用者应自行调整；
    2.使用时，可列出一年以上走势图，观察其常态性分布范围，然
      后用参考线设定其超买超卖范围。通常UDL 高于某个极限时，
      短期股价会下跌；UDL 低于某个极限时，短期股价会上涨；
    3.本指标可设参考线。

    :param data_frame:
    :param N1:
    :param N2:
    :param N3:
    :param N4:
    :param M:
    :return:
    """
    CLOSE = data_frame['close']
    UDL = (MA(CLOSE, N1) + MA(CLOSE, N2) + MA(CLOSE, N3) + MA(CLOSE, N4)) / 4
    MAUDL = MA(UDL, M)
    DICT = {'UDL': UDL, 'MAUDL': MAUDL}

    return pd.DataFrame(DICT)


def WR(data_frame, N=10, N1=6):
    """
    威廉指标

    Param#1日威廉指标 10
    Param#2日威廉指标 6

    输出WR1:100*(N日内最高价的最高值-收盘价)/(N日内最高价的最高值-N日内最低价的最低值)
    输出WR2:100*(N1日内最高价的最高值-收盘价)/(N1日内最高价的最高值-N1日内最低价的最低值)

    1.WR波动于0 - 100，100置于顶部，0置于底部。
    2.本指标以50为中轴线，高于50视为股价转强；低于50视为股价转弱
    3.本指标高于20后再度向下跌破20，卖出；低于80后再度向上突破80，买进。
    4.WR连续触底3 - 4次，股价向下反转机率大；连续触顶3 - 4次，股价向上反转机率大。

    :param data_frame:
    :param N:
    :param N1:
    :return:
    """
    HIGH = data_frame['high']
    LOW = data_frame['low']
    CLOSE = data_frame['close']
    WR1 = 100 * (HHV(HIGH, N) - CLOSE) / (HHV(HIGH, N) - LLV(LOW, N))
    WR2 = 100 * (HHV(HIGH, N1) - CLOSE) / (HHV(HIGH, N1) - LLV(LOW, N1))
    DICT = {'WR1': WR1, 'WR2': WR2}

    return pd.DataFrame(DICT)


def LWR(data_frame, N=9, M1=3, M2=3):
    """
    威廉指标

    RSV:100*(N(Param#1)日内最高价-今日收盘价)/(N日内最高价-N日内最低价) 9
    LWR1:RSV的Param#2日指数移动平均 3
    LWR2:LWR1的Param#3日指数移动平均 3

    RSV赋值: (N日内最高价的最高值-收盘价)/(N日内最高价的最高值-N日内最低价的最低值)*100
    输出LWR1:RSV的M1日[1日权重]移动平均

    :param data_frame:
    :param N:
    :param M1:
    :param M2:
    :return:
    """
    HIGH = data_frame['high']
    LOW = data_frame['low']
    CLOSE = data_frame['close']
    RSV = (HHV(HIGH, N) - CLOSE) / (HHV(HIGH, N) - LLV(LOW, N)) * 100
    LWR1 = SMA(RSV, M1, 1)
    LWR2 = SMA(LWR1, M2, 1)
    DICT = {'LWR1': LWR1, 'LWR2': LWR2}

    return pd.DataFrame(DICT)


def MARSI(data_frame, M1=10, M2=6):
    """
    相对强弱平均线

    Param#1日MARSI[相对强弱平均线] 10
    Param#2日MARSI[相对强弱平均线] 6

    DIF赋值:收盘价-1日前的收盘价
    VU赋值:如果DIF>=0,返回DIF,否则返回0
    VD赋值:如果DIF<0,返回-DIF,否则返回0
    MAU1赋值:VU的M1日平滑移动平均
    MAD1赋值:VD的M1日平滑移动平均
    MAU2赋值:VU的M2日平滑移动平均
    MAD2赋值:VD的M2日平滑移动平均
    输出RSI10:100*MAU1/(MAU1+MAD1)的M1日简单移动平均
    输出RSI6:100*MAU2/(MAU2+MAD2)的M2日简单移动平均


    RSV赋值: (N日内最高价的最高值-收盘价)/(N日内最高价的最高值-N日内最低价的最低值)*100
    输出LWR1:RSV的M1日[1日权重]移动平均

    1.RSI>20 为超买；RSI<20 为超卖；
    2.RSI 以50为中界线，大于50视为多头行情，小于50视为空头行情；
    3.RSI 在80以上形成Ｍ头或头肩顶形态时，视为向下反转信号；
    4.RSI 在20以下形成Ｗ底或头肩底形态时，视为向上反转信号；
    5.RSI 向上突破其高点连线时，买进；RSI 向下跌破其低点连线时，卖出。

    :param data_frame:
    :param M1:
    :param M2:
    :return:
    """
    CLOSE = data_frame['close']
    DIF = CLOSE - REF(CLOSE, 1)
    VU = IF(DIF >= 0, DIF, 0)
    VD = IF(DIF < 0, -DIF, 0)
    MAU1 = MEMA(VU, M1)
    MAD1 = MEMA(VD, M1)
    MAU2 = MEMA(VU, M2)
    MAD2 = MEMA(VD, M2)

    RSI10 = MA(100 * MAU1 / (MAU1 + MAD1), M1)
    RSI6 = MA(100 * MAU2 / (MAU2 + MAD2), M2)
    DICT = {'RSI10': RSI10, 'RSI6': RSI6}

    return pd.DataFrame(DICT)


def BIASQL(data_frame, N=6, M=6):
    """
    乖离率-传统版
    Param#1日乖离率 6
    Param#2日平均乖离率 6

    输出乖离率 :(收盘价-收盘价的N日简单移动平均)/收盘价的N日简单移动平均*100
    输出BIASMA :乖离率的M日简单移动平均
    :param data_frame:
    :param N1:
    :param N2:
    :param N3:
    :return:
    """
    CLOSE = data_frame['close']
    BIAS = (CLOSE - MA(CLOSE, N)) / MA(CLOSE, N) * 100
    BIASMA = MA(BIAS, M)
    DICT = {'BIAS': BIAS, 'BIASMA': BIASMA}
    return pd.DataFrame(DICT)


def BIAS(data_frame, N1=6, N2=12, N3=24):
    """
    乖离率

    Param#1日乖离率 6
    Param#2日乖离率 12
    Param#3日乖离率 24

    输出BIAS1 :(收盘价-收盘价的N1日简单移动平均)/收盘价的N1日简单移动平均*100
    输出BIAS2 :(收盘价-收盘价的N2日简单移动平均)/收盘价的N2日简单移动平均*100
    输出BIAS3 :(收盘价-收盘价的N3日简单移动平均)/收盘价的N3日简单移动平均*100# 乖离率-传统版 BIAS-QL
    :param data_frame:
    :param N1:
    :param N2:
    :param N3:
    :return:
    """
    CLOSE = data_frame['close']
    BIAS1 = (CLOSE - MA(CLOSE, N1)) / MA(CLOSE, N1) * 100
    BIAS2 = (CLOSE - MA(CLOSE, N2)) / MA(CLOSE, N2) * 100
    BIAS3 = (CLOSE - MA(CLOSE, N3)) / MA(CLOSE, N3) * 100
    DICT = {'BIAS1': BIAS1, 'BIAS2': BIAS2, 'BIAS3': BIAS3}

    return pd.DataFrame(DICT)


def ACCER(data_frame, N=8):
    """
    幅度涨速

    天数:Param#1天 8

    输出幅度涨速:收盘价的N日线性回归斜率/收盘价

    幅度涨速
    算法：
    先求出斜率，再对其价格进行归一
    :param data_frame:
    :param N:
    :return:
    """
    CLOSE = data_frame['close']
    DICT = talib.LINEARREG_SLOPE(CLOSE, timeperiod=N)
    return pd.DataFrame(DICT)


def ADTM(data_frame, N=23, M=8):
    """
    动态买卖气指标
    :param data_frame:
    :param N:
    :param M:
    :return:
    """
    HIGH = data_frame.high
    LOW = data_frame.low
    OPEN = data_frame.open
    DTM = IF(OPEN > REF(OPEN, 1), MAX((HIGH - OPEN), (OPEN - REF(OPEN, 1))), 0)
    DBM = IF(OPEN < REF(OPEN, 1), MAX((OPEN - LOW), (OPEN - REF(OPEN, 1))), 0)
    STM = SUM(DTM, N)
    SBM = SUM(DBM, N)
    ADTM1 = IF(STM > SBM, (STM - SBM) / STM,
               IF(STM != SBM, (STM - SBM) / SBM, 0))
    MAADTM = MA(ADTM1, M)
    DICT = {'ADTM': ADTM1, 'MAADTM': MAADTM}

    return pd.DataFrame(DICT)
