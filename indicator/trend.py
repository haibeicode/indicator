"""
1.	趋向指标 
又叫趋势跟踪类指标,主要用于跟踪并预测股价的发展趋势

包含的主要指标
1. 移动平均线 MA
2. 指数平滑移动平均线 MACD
3. 趋向指标 DMI
4. 瀑布线 PBX
5. 平均线差 DMA
6. 动力指标(动量线)  MTM
7. 指数平均线 EXPMA
8. 佳庆指标 CHO
"""
from common.indicator.base import *


def MA(data_frame, *args, **kwargs):
    """
    MA
    :param data_frame:
    :param args:
    :param kwargs:
    :return:
    """

    CLOSE = data_frame['close']
    return pd.DataFrame({'MA{}'.format(N): MA(CLOSE, N) for N in list(args)})


def EMA(data_frame, N):
    """

    :param data_frame:
    :param N:
    :return:
    """
    CLOSE = data_frame['close']
    return pd.DataFrame({'EMA': EMA(CLOSE, N)})


def SMA(data_frame, N):
    """

    :param data_frame:
    :param N:
    :return:
    """
    CLOSE = data_frame['close']
    return pd.DataFrame({'SMA': SMA(CLOSE, N)})


def MACD(data_frame, short=12, long=26, mid=9):
    """
    MACD CALC
    :param data_frame:
    :param short:
    :param long:
    :param mid:
    :return:
    """
    CLOSE = data_frame['close']

    DIF = EMA(CLOSE, short) - EMA(CLOSE, long)
    DEA = EMA(DIF, mid)
    MACD = (DIF - DEA) * 2

    return pd.DataFrame({'DIF': DIF, 'DEA': DEA, 'MACD': MACD})


def DMI(data_frame, M1=14, M2=6):
    """
    趋向指标 DMI
    :param data_frame:
    :param M1:
    :param M2:
    :return:
    """
    HIGH = data_frame.high
    LOW = data_frame.low
    CLOSE = data_frame.close
    OPEN = data_frame.open

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


def DMA(data_frame, M1=10, M2=50, M3=10):
    """
    平均线差 DMA
    :param data_frame:
    :param M1:
    :param M2:
    :param M3:
    :return:
    """
    CLOSE = data_frame.close
    DDD = MA(CLOSE, M1) - MA(CLOSE, M2)
    AMA = MA(DDD, M3)
    return pd.DataFrame({
        'DDD': DDD, 'AMA': AMA
    })



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
    CLOSE = data_frame.close
    MA1 = EMA(CLOSE, P1)
    MA2 = EMA(CLOSE, P2)
    MA3 = EMA(CLOSE, P3)
    MA4 = EMA(CLOSE, P4)
    return pd.DataFrame({
        'MA1': MA1, 'MA2': MA2, 'MA3': MA3, 'MA4': MA4
    })


def CHO(data_frame, N1=10, N2=20, M=6):
    """
    佳庆指标 CHO
    :param data_frame:
    :param N1:
    :param N2:
    :param M:
    :return:
    """
    HIGH = data_frame.high
    LOW = data_frame.low
    CLOSE = data_frame.close
    VOL = data_frame.volume
    MID = SUM(VOL * (2 * CLOSE - HIGH - LOW) / (HIGH + LOW), 0)
    CHO = MA(MID, N1) - MA(MID, N2)
    MACHO = MA(CHO, M)
    return pd.DataFrame({
        'CHO': CHO, 'MACHO': MACHO
    })
