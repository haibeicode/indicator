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
Quantity and price Indicators
@author Tab
"""
from indicator.base import *


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
    CLOSE = data_frame['close']
    VOL = data_frame['volume']
    PVT = SUM((CLOSE - REF(CLOSE, 1)) / REF(CLOSE, 1) * VOL, 0)
    return pd.DataFrame({'PVT': PVT})


def OBV(data_frame):
    """
    能量潮
    :param data_frame:
    :return:
    """
    VOL = data_frame['volume']
    CLOSE = data_frame['close']
    return pd.DataFrame({
        'OBV': np.cumsum(IF(CLOSE > REF(CLOSE, 1), VOL, IF(CLOSE < REF(CLOSE, 1), -VOL, 0))) / 10000
    })

