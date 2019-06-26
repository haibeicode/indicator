

"""
4.	量价指标
通过成交量和股价变动关系分析未来趋势
震荡升降指标ASI
价量趋势PVT`
能量潮OBV
量价趋势VPT
"""
from common.indicator.base import *


def ASI(data_frame, M1=26, M2=10):
    """
    LC=REF(CLOSE,1);
    AA=ABS(HIGH-LC);
    BB=ABS(LOW-LC);
    CC=ABS(HIGH-REF(LOW,1));
    DD=ABS(LC-REF(OPEN,1));
    R=IF(AA>BB AND AA>CC,AA+BB/2+DD/4,IF(BB>CC AND BB>AA,BB+AA/2+DD/4,CC+DD/4));
    X=(CLOSE-LC+(CLOSE-OPEN)/2+LC-REF(OPEN,1));
    SI=16*X/R*MAX(AA,BB);
    ASI:SUM(SI,M1);
    ASIT:MA(ASI,M2);
    """
    CLOSE = data_frame['close']
    HIGH = data_frame['high']
    LOW = data_frame['low']
    OPEN = data_frame['open']
    LC = REF(CLOSE, 1)
    AA = ABS(HIGH - LC)
    BB = ABS(LOW - LC)
    CC = ABS(HIGH - REF(LOW, 1))
    DD = ABS(LC - REF(OPEN, 1))

    R = IFAND(AA > BB, AA > CC, AA + BB / 2 + DD / 4,
              IFAND(BB > CC, BB > AA, BB + AA / 2 + DD / 4, CC + DD / 4))
    X = (CLOSE - LC + (CLOSE - OPEN) / 2 + LC - REF(OPEN, 1))
    SI = 16 * X / R * MAX(AA, BB)
    ASI = SUM(SI, M1)
    ASIT = MA(ASI, M2)
    return pd.DataFrame({
        'ASI': ASI, 'ASIT': ASIT
    })


def PVT(data_frame):
    """

    :param data_frame:
    :return:
    """
    CLOSE = data_frame.close
    VOL = data_frame.volume
    PVT = SUM((CLOSE - REF(CLOSE, 1)) / REF(CLOSE, 1) * VOL, 0)
    return pd.DataFrame({'PVT': PVT})


def OBV(data_frame):
    """
    能量潮
    :param data_frame:
    :return:
    """
    VOL = data_frame.volume
    CLOSE = data_frame.close
    return pd.DataFrame({
        'OBV': np.cumsum(IF(CLOSE > REF(CLOSE, 1), VOL, IF(CLOSE < REF(CLOSE, 1), -VOL, 0))) / 10000
    })


def VPT(data_frame, N=51, M=6):
    """

    :param data_frame:
    :param N:
    :param M:
    :return:
    """
    VOL = data_frame.volume
    CLOSE = data_frame.close
    VPT = SUM(VOL * (CLOSE - REF(CLOSE, 1)) / REF(CLOSE, 1), 0)
    MAVPT = MA(VPT, M)
    return pd.DataFrame({
        'VPT': VPT, 'MAVPT': MAVPT
    })