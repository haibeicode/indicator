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

import talib


################
# TA-LIB 量化分析基础数据
# Cycle Indicator Functions
################


def HT_DCPERIOD(df):
    """
    函数名：HT_DCPERIOD
    名称： 希尔伯特变换-主导周期

    简介：将价格作为信息信号，计算价格处在的周期的位置，作为择时的依据。

    [文库文档](https://wenku.baidu.com/view/0e35f6eead51f01dc281f18e.md)

    NOTE: The ``HT_DCPERIOD`` function has an unstable period.
    python API
    real=HT_DCPERIOD(close)
    :return:
    """
    close = df['close']
    return talib.HT_DCPERIOD(close)


def HT_DCPHASE(df):
    """
    函数名：HT_DCPHASE
    名称： 希尔伯特变换-主导循环阶段

    python API
    real=HT_DCPHASE(close)
    :return:
    """
    close = df['close']
    return talib.HT_DCPHASE(close)


def HT_PHASOR(df):
    """
    函数名：HT_DCPHASE
    名称： 希尔伯特变换-希尔伯特变换相量分量

    python API
    inphase, quadrature=HT_PHASOR(close)
    :return:
    """
    close = df['close']
    return talib.HT_PHASOR(close)


def HT_SINE(df):
    """
    函数名：HT_DCPHASE
    名称： 希尔伯特变换-正弦波

    python API
    sine, leadsine=HT_SINE(close)
    :return:
    """
    close = df['close']
    return talib.HT_SINE(close)


def HT_TRENDMODE(df):
    """
    函数名：HT_DCPHASE
    名称： 希尔伯特变换-趋势与周期模式

    python API
    integer=HT_TRENDMODE(close)
    :return:
    """
    close = df['close']
    return talib.HT_TRENDMODE(close)


################
# TA-LIB 量化分析数据
# Momentum Indicator Functions
# 数学运算符函数
#################


def ADD(df):
    """
    函数名：ADD
    名称：向量加法运算

    python API
    real=ADD(high, low)
    :return:
    """
    high = df['high']
    low = df['low']
    return talib.ADD(high, low)


def DIV(df):
    """
    函数名：DIV
    名称：向量除法运算

    python API
    real=DIV(high, low)
    :return:
    """
    high = df['high']
    low = df['low']
    return talib.DIV(high, low)


def MAXINDEX(df, time_period=30):
    """
    函数名：MAXINDEX
    名称：周期内最大值的索引

    python API
    integer=MAXINDEX(close, timeperiod=30)
    :param time_period:
    :return:
    """
    close = df['close']
    return talib.MAXINDEX(close, timeperiod=time_period)


def MININDEX(df, time_period=30):
    """
    函数名：MININDEX
    名称：周期内最小值的索引

    python API
    integer=MININDEX(close, timeperiod=30)
    :return:
    """
    close = df['close']
    return talib.MININDEX(close, timeperiod=time_period)


def MINMAX(df, time_period=30):
    """
    函数名：MINMAX
    名称：周期内最小值和最大值(返回元组`元组（array【最小】，array【最大】）)

    python API
    min, max=MINMAX(close, timeperiod=30)
    :return:
    """
    close = df['close']
    return talib.MINMAX(close, timeperiod=time_period)


def MINMAXINDEX(df, time_period=30):
    """
    函数名：MINMAX
    名称：周期内最小值和最大值索引(返回元组`元组（array【最小】，array【最大】）)

    python API
    minidx, maxidx=MINMAXINDEX(close, timeperiod=30)
    :return:
    """
    close = df['close']
    return talib.MINMAXINDEX(close, timeperiod=time_period)


def MULT(df):
    """
    函数名：MULT
    名称：向量乘法运算

    python API
    real=MULT(high, low)
    :return:
    """
    high = df['high']
    low = df['low']
    return talib.MULT(high, low)


def SUB(df):
    """
    函数名：SUB
    名称：向量减法运算

    python API
    real=SUB(high, low)
    :return:
    """
    high = df['high']
    low = df['low']
    return talib.SUB(high, low)


################
# TA-LIB 量化分析基础数据
# Math Transform Functions
################


def ACOS(df):
    """
    函数名：ACOS
    名称：acos函数是反余弦函数，三角函数

    python API
    real=ACOS(close)
    :return:
    """
    close = df['close']
    return talib.ACOS(close)


def ASIN(df):
    """
    函数名：ASIN
    名称：反正弦函数，三角函数

    python API
    real=ASIN(close)
    :return:
    """
    close = df['close']
    return talib.ASIN(close)


def ATAN(df):
    """
    函数名：ASIN
    名称：数字的反正切值，三角函数

    python API
    real=ATAN(close)
    :return:
    """
    close = df['close']
    return talib.ATAN(close)


def CEIL(df):
    """
    函数名：CEIL
    简介：向上取整数

    python API
    real=CEIL(close)
    :return:
    """
    close = df['close']
    return talib.CEIL(close)


def COS(df):
    """
    函数名：COS
    名称：余弦函数，三角函数

    python API
    real=COS(close)
    :return:
    """
    close = df['close']
    return talib.COS(close)


def COSH(df):
    """
    函数名：COSH
    名称：双曲正弦函数，三角函数

    python API
    real=COSH(close)
    :return:
    """
    close = df['close']
    return talib.COSH(close)


def EXP(df):
    """
    函数名：EXP
    名称：指数曲线，三角函数

    python API
    real=EXP(close)
    :return:
    """
    close = df['close']
    return talib.EXP(close)


def FLOOR(df):
    """
    函数名：FLOOR
    名称：向下取整数

    python API
    real=FLOOR(close)
    :return:
    """
    close = df['close']
    return talib.FLOOR(close)


def LN(df):
    """
    函数名：LN
    名称：自然对数

    python API
    real=LN(close)
    :return:
    """
    close = df['close']
    return talib.LN(close)


def LOG10(df):
    """
    函数名：LOG10
    名称：对数函数log

    python API
    real=LOG10(close)
    :return:
    """
    close = df['close']
    return talib.LOG10(close)


def SIN(df):
    """
    函数名：SIN
    名称：正弦函数，三角函数

    python API
    real=SIN(close)
    :return:
    """
    close = df['close']
    return talib.SIN(close)


def SINH(df):
    """
    函数名：SINH
    名称：双曲正弦函数，三角函数

    python API
    real=SINH(close)
    :return:
    """
    close = df['close']
    return talib.SINH(close)


def SQRT(df):
    """
     函数名：SQRT
    名称：非负实数的平方根

    python API
    real=SQRT(close)
    :return:
    """
    close = df['close']
    return talib.SQRT(close)


def TAN(df):
    """
    函数名：TAN
    名称：正切函数，三角函数

    python API
    real=TAN(close)
    :return:
    """
    close = df['close']
    return talib.TAN(close)


def TANH(df):
    """
    函数名：TANH
    名称：双曲正切函数，三角函数

    python API
    real=TANH(close)
    :return:
    """
    close = df['close']
    return talib.TANH(close)


################
# TA-LIB 量化分析数据
# Momentum Indicator Functions
# 动量指标
#################


def ADX(df, time_period=14):
    """
    函数名：ADX
    名称：平均趋向指数

    简介：使用ADX指标，指标判断盘整、振荡和单边趋势。

    # 公式：

    一、先决定股价趋势（Directional
    Movement，DM）是上涨或下跌：
    “所谓DM值，今日股价波动幅度大于昨日股价波动幅部分的最大值，可能是创高价的部分或创低价的部分；如果今日股价波动幅度较前一日小，则DM=0。”
    若股价高点持续走高，为上涨趋势，记作 + DM。
    若为下跌趋势，记作 - DM。-DM的负号（–）是表示反向趋势（下跌），并非数值为负数。
    其他状况：DM=0。

    二、寻找股价的真实波幅（True
    Range，TR）：
    所谓真实波幅（TR）是以最高价，最低价，及前一日收盘价三个价格做比较，求出当日股价波动的最大幅度。

    三、趋势方向需经由一段时间来观察，研判上才有意义。一般以14天为指标的观察周期：
    先计算出 + DM、–DM及TR的14日算术平均数，得到 + DM14、–DM14及TR14三组数据作为起始值，再计算各自的移动平均值（EMA）。

    +DI14=+DM/TR14 * 100
    -DI14=+DM/TR14 * 100

    DX=| (+DI14) - (-DI14) |/| (+DI14) + (-DI14) |
    DX运算结果取其绝对值，再将DX作移动平均，得到ADX。

    # 特点：
    *ADX无法告诉你趋势的发展方向。
    *如果趋势存在，ADX可以衡量趋势的强度。不论上升趋势或下降趋势，ADX看起来都一样。
    *ADX的读数越大，趋势越明显。衡量趋势强度时，需要比较几天的ADX读数，观察ADX究竟是上升或下降。ADX读数上升，代表趋势转强；如果ADX读数下降，意味着趋势转弱。
    *当ADX曲线向上攀升，趋势越来越强，应该会持续发展。如果ADX曲线下滑，代表趋势开始转弱，反转的可能性增加。
    *单就ADX本身来说，由于指标落后价格走势，所以算不上是很好的指标，不适合单就ADX进行操作。可是，如果与其他指标配合运用，ADX可以确认市场是否存在趋势，并衡量趋势的强度。

    # 指标应用：
    *+DI与–DI表示多空相反的二个动向，当据此绘出的两条曲线彼此纠结相缠时，代表上涨力道与下跌力道相当，多空势均力敌。当 + DI与–DI彼此穿越时，由下往上的一方其力道开始压过由上往下的另一方，此时出现买卖讯号。
    *ADX可作为趋势行情的判断依据，当行情明显朝多空任一方向进行时，ADX数值都会显著上升，趋势走强。若行情呈现盘整格局时，ADX会低于 + DI与–DI二条线。若ADX数值低于20，则不论DI表现如何，均显示市场没有明显趋势。
    *ADX持续偏高时，代表“超买”（Overbought）或“超卖”（Oversold）的现象，行情反转的机会将增加，此时则不适宜顺势操作。当ADX数值从上升趋势转为下跌时，则代表行情即将反转；若ADX数值由下跌趋势转为上升时，行情将止跌回升。
    *总言之，DMI指标包含4条线：+DI、-DI、ADX和ADXR。+DI代表买盘的强度、-DI代表卖盘的强度；ADX代表趋势的强度、ADXR则为ADX的移动平均。

    python API
    real=ADX(high, low, close, timeperiod=14)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.ADX(high, low, close, timeperiod=time_period)


def ACCER(df, N=8):
    """
    幅度涨速

    天数:Param#1天 8

    输出幅度涨速:收盘价的N日线性回归斜率/收盘价

    幅度涨速
    算法：
    先求出斜率，再对其价格进行归一
    :param df:
    :param N:
    :return:
    """
    CLOSE = df['close']
    return talib.LINEARREG_SLOPE(CLOSE, timeperiod=N)


def ADXR(df, time_period=14):
    """
    函数名：ADXR
    名称：平均趋向指数的趋向指数

    简介：使用ADXR指标，指标判断ADX趋势。

    python API
    real=ADXR(high, low, close, timeperiod=14)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.ADXR(high, low, close, timeperiod=time_period)


def APO(df, fast_period=12, slow_period=26, ma_type=0):
    """
    python API
    real=APO(close, fastperiod=12, slowperiod=26, matype=0)
    :return:
    """
    close = df['close']
    return talib.APO(close, fastperiod=fast_period, slowperiod=slow_period, matype=ma_type)


def AROON(df, time_period=14):
    """
    函数名：AROON
    名称：阿隆指标

    简介：该指标是通过计算自价格达到近期最高值和最低值以来所经过的期间数，阿隆指标帮助你预测价格趋势到趋势区域（或者反过来，从趋势区域到趋势）的变化。

    # 计算公式：
    Aroon(上升)=[(计算期天数 - 最高价后的天数)/计算期天数] * 100
    Aroon(下降)=[(计算期天数 - 最低价后的天数)/计算期天数] * 100

    # 指数应用
    1、极值0和100当UP线达到100时，市场处于强势；如果维持在70~100之间，表示一个上升趋势。同样，如果Down线达到0，表示处于弱势，如果维持在0~30之间，表示处于下跌趋势。如果两条线同处于极值水平，则表明一个更强的趋势。
    2、平行运动如果两条线平行运动时，表明市场趋势被打破。可以预期该状况将持续下去，只到由极值水平或交叉穿行西安市出方向性运动为止。
    3、交叉穿行当下行线上穿上行线时，表明潜在弱势，预期价格开始趋于下跌。反之，表明潜在强势，预期价格趋于走高。

    python API
    aroondown, aroonup=AROON(high, low, timeperiod=14)
    :return:
    """
    high = df['high']
    low = df['low']
    return talib.AROON(high, low, timeperiod=time_period)


def AROONOSC(df, time_period=14):
    """
    函数名：AROONOSC
    名称：阿隆振荡

    python API
    real=AROONOSC(high, low, timeperiod=14)
    :return:
    """
    high = df['high']
    low = df['low']
    return talib.AROONOSC(high, low, timeperiod=time_period)


def BOP(df):
    """
    函数名：BOP
    名称：均势指标

    python API
    real=BOP(open, high, low, close)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.BOP(open, high, low, close)


def CMO(df, time_period=14):
    """
    函数名：CMO
    名称：钱德动量摆动指标

    简介：与其他动量指标摆动指标如相对强弱指标（RSI）和随机指标（KDJ）不同，钱德动量指标在计算公式的分子中采用上涨日和下跌日的数据。

    计算公式：CMO =（Su－Sd）*100 /（Su + Sd）
    其中：Su是今日收盘价与昨日收盘价（上涨日）差值加总。若当日下跌，则增加值为0；Sd是今日收盘价与做日收盘价（下跌日）差值的绝对值加总。若当日上涨，则增加值为0；

    # 指标应用
    *本指标类似RSI指标。
    *当本指标下穿 - 50水平时是买入信号，上穿 + 50水平是卖出信号。
    *钱德动量摆动指标的取值介于 - 100和100之间。
    *本指标也能给出良好的背离信号。
    *当股票价格创出新低而本指标未能创出新低时，出现牛市背离；
    *当股票价格创出新高而本指标未能创出新高时，当出现熊市背离时。
    *我们可以用移动均值对该指标进行平滑。

    python API
    real=CMO(close, timeperiod=14)
    :return:
    """
    close = df['close']
    return talib.CMO(close, timeperiod=time_period)


def DX(df, time_period=14):
    """
    函数名：DX
    名称：动向指标或趋向指标

    简介：通过分析股票价格在涨跌过程中买卖双方力量均衡点的变化情况，即多空双方的力量的变化受价格波动的影响而发生由均衡到失衡的循环过程，从而提供对趋势判断依据的一种技术指标。

    分析和应用：
    [百度百科](https://baike.baidu.com/item/DMI%E6%8C%87%E6%A0%87/3423254?fr=aladdin)
    [维基百科](https://zh.wikipedia.org/wiki/% E5%8B%95%E5%90%91%E6%8C%87%E6%95%B8)
    [同花顺学院](http://www.iwencai.com/school/search?cg=100&w=DMI)

    python API
    real=DX(high, low, close, timeperiod=14)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.DX(high, low, close, timeperiod=time_period)


def MACDEXT(df, fast_period=12, fast_ma_type=0, slow_period=26, slow_ma_type=0, signal_period=9,
            signal_ma_type=0):
    """
    函数名：MACDEXT
    名称：

    python API
    macd, macdsignal, macdhist=MACDEXT(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
    :return:
    """
    close = df['close']
    return talib.MACDEXT(close, fastperiod=fast_period, fastmatype=fast_ma_type,
                         slowperiod=slow_period, slowmatype=slow_ma_type,
                         signalperiod=signal_period, signalmatype=signal_ma_type)


def MACDFIX(df, signal_period=9):
    """
    python API
    macd, macdsignal, macdhist=MACDFIX(close, signalperiod=9)
    :return:
    """
    close = df['close']
    return talib.MACDFIX(close, signalperiod=signal_period)


def MFI(df, time_period=14):
    """
    函数名：MFI
    名称：资金流量指标

    简介：属于量价类指标，反映市场的运行趋势

    分析和应用：
    [百度百科](https://baike.baidu.com/item/mfi/7429225?fr=aladdin)
    [同花顺学院](http://www.iwencai.com/school/search?cg=100&w=MFI)

    python API
    real=MFI(high, low, close, volume, timeperiod=14)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    volume = df['volume']
    return talib.MFI(high, low, close, volume, timeperiod=time_period)


def MINUS_DI(df, time_period=14):
    """
    函数名：DMI
    中的DI指标
    负方向指标

    名称：下升动向值(-DI 最低价减小的次数)
    简介：通过分析股票价格在涨跌过程中买卖双方力量均衡点的变化情况，即多空双方的力量的变化受价格波动的影响而发生由均衡到失衡的循环过程，从而提供对趋势判断依据的一种技术指标。

    分析和应用：
    [百度百科](https://baike.baidu.com/item/DMI%E6%8C%87%E6%A0%87/3423254?fr=aladdin)
    [维基百科](https://zh.wikipedia.org/wiki/% E5%8B%95%E5%90%91%E6%8C%87%E6%95%B8)
    [同花顺学院](http://www.iwencai.com/school/search?cg=100&w=DMI)

    python API
    real=MINUS_DI(high, low, close, timeperiod=14)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.MINUS_DI(high, low, close, timeperiod=time_period)


def MINUS_DM(df, time_period=14):
    """
    函数名：MINUS_DM
    名称： 上升动向值
    DMI中的DM代表正趋向变动值即上升动向值

    简介：通过分析股票价格在涨跌过程中买卖双方力量均衡点的变化情况，即多空双方的力量的变化受价格波动的影响而发生由均衡到失衡的循环过程，从而提供对趋势判断依据的一种技术指标。

    分析和应用：
    [百度百科](https://baike.baidu.com/item/DMI%E6%8C%87%E6%A0%87/3423254?fr=aladdin)
    [维基百科](https://zh.wikipedia.org/wiki/% E5%8B%95%E5%90%91%E6%8C%87%E6%95%B8)
    [同花顺学院](http://www.iwencai.com/school/search?cg=100&w=DMI)

    python API
    real=MINUS_DM(high, low, timeperiod=14)
    :return:
    """
    high = df['high']
    low = df['low']
    return talib.MINUS_DM(high, low, timeperiod=time_period)


def MOM(df, time_period=14):
    """
    函数名：MOM
    名称： 上升动向值

    简介：投资学中意思为续航，指股票(或经济指数)持续增长的能力。研究发现，赢家组合在牛市中存在着正的动量效应，输家组合在熊市中存在着负的动量效应。

    分析和应用：
    [维基百科](https://zh.wikipedia.org/wiki/% E5%8B%95%E9%87%8F%E6%8C%87%E6%A8%99)
    [同花顺学院](http://www.iwencai.com/yike/detail/auid/cb18b2dbe2f455e6)

    python API
    real=MOM(close, timeperiod=10)
    :return:
    """
    close = df['close']
    return talib.MOM(close, timeperiod=time_period)


def PLUS_DI(df, time_period=14):
    """
    +DI 最高价上涨的次数
    + di是真实范围的百分比。di是真实范围下降的百分比。当+ di越过di时，生成一个买入信号。当di越过+ di时，产生一个卖出信号。你应该等到交易进入极限点为止。也就是说，你应该等待进入一个长期的交易，直到价格达到高的酒吧上di di越过di，并等待进入短期贸易，直到价格达到低的酒吧上的di越过+ di。
    python API
    real=PLUS_DI(high, low, close, timeperiod=14)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.PLUS_DI(high, low, close, timeperiod=time_period)


def PLUS_DM(df, time_period=14):
    """
    python API
    real=PLUS_DM(high, low, timeperiod=14)
    :return:
    """
    high = df['high']
    low = df['low']
    return talib.PLUS_DM(high, low, timeperiod=time_period)


def PPO(df, fast_period=12, slow_period=26, ma_type=0):
    """
    函数名：PPO
    名称： 价格震荡百分比指数

    简介：价格震荡百分比指标（PPO）是一个和MACD指标非常接近的指标。PPO标准设定和MACD设定非常相似：12, 26, 9和PPO，和MACD一样说明了两条移动平均线的差距，但是它们有一个差别是PPO是用百分比说明。

    分析和应用：
    [参考](http://blog.sina.com.cn/s/blog_7542a31c0101aux9.html)

    python API
    real=PPO(close, fastperiod=12, slowperiod=26, matype=0)
    :return:
    """
    close = df['close']
    return talib.PPO(close, fastperiod=fast_period, slowperiod=slow_period, matype=ma_type)


def ROC(df, time_period=10):
    """
    函数名：ROC
    名称： 变动率指标

    简介：ROC是由当天的股价与一定的天数之前的某一天股价比较，其变动速度的大小, 来反映股票市变动的快慢程度

    分析和应用：
    [百度百科](https://baike.baidu.com/item/ROC%E6%8C%87%E6%A0%87/3081705?fr=aladdin)
    [同花顺学院](http://www.iwencai.com/yike/detail/auid/6ac184fdb20d2f59)

    python API
    real=ROC(close, timeperiod=10)
    :return:
    """
    close = df['close']
    return talib.ROC(close, timeperiod=time_period)


def ROCP(df, time_period=10):
    """
    python API
    real=ROCP(close, timeperiod=10)
    :return:
    """
    close = df['close']
    return talib.ROCP(close, timeperiod=time_period)


def ROCR(df, time_period=10):
    """
    python API
    real=ROCR(close, timeperiod=10)
    :return:
    """
    close = df['close']
    return talib.ROCR(close, timeperiod=time_period)


def ROCR100(df, time_period=10):
    """
    python API
    real=ROCR100(close, timeperiod=10)
    :return:
    """
    close = df['close']
    return talib.ROCR100(close, timeperiod=time_period)


def RSI(df, time_period=14):
    """
    函数名：RSI
    名称：相对强弱指数

    简介：是通过比较一段时期内的平均收盘涨数和平均收盘跌数来分析市场买沽盘的意向和实力，从而作出未来市场的走势。

    分析和应用：
    [百度百科](https://baike.baidu.com/item/RSI/6130115)
    [维基百科](https://zh.wikipedia.org/wiki/% E7%9B%B8%E5%B0%8D%E5%BC%B7%E5%BC%B1%E6%8C%87%E6%95%B8)
    [同花顺学院](http://www.iwencai.com/yike/detail/auid/6a280c6cebcf140a)

    python API
    real=RSI(close, timeperiod=14)
    :return:
    """
    close = df['close']
    return talib.RSI(close, timeperiod=time_period)


def STOCH(df, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0):
    """
    函数名：STOCH
    名称：随机指标, 俗称KD

    python API
    slowk, slowd=STOCH(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.STOCH(high, low, close, fastk_period=fastk_period, slowk_period=slowk_period,
                       slowk_matype=slowk_matype, slowd_period=slowd_period, slowd_matype=slowd_matype)


def STOCHF(df, fastk_period=5, fastd_period=3, fastd_matype=0):
    """
    python API
    fastk, fastd=STOCHF(high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.STOCHF(high, low, close, fastk_period=fastk_period, fastd_period=fastd_period,
                        fastd_matype=fastd_matype)


def STOCHRSI(df, time_period=14, fastk_period=5, fastd_period=3, fastd_matype=0):
    """
     python API
    fastk, fastd=STOCHRSI(close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
    :return:
    """
    close = df['close']
    return talib.STOCHRSI(close, timeperiod=time_period, fastk_period=fastk_period, fastd_period=fastd_period,
                          fastd_matype=fastd_matype)


def TRIX(df, time_period=30):
    """
    python API
    real=TRIX(close, timeperiod=30)
    :return:
    """
    close = df['close']
    return talib.TRIX(close, timeperiod=time_period)


def ULTOSC(df, time_period1=7, time_period2=14, time_period3=28):
    """
    函数名：ULTOSC
    名称：终极波动指标

    简介：UOS是一种多方位功能的指标，除了趋势确认及超买超卖方面的作用之外，它的“突破”讯号不仅可以提供最适当的交易时机之外，更可以进一步加强指标的可靠度。

    分析和应用：
    [百度百科](https://baike.baidu.com/item/% E7%BB%88%E6%9E%81%E6%B3%A2%E5%8A%A8%E6%8C%87%E6%A0%87/1982936?fr=aladdin&fromid=12610066&fromtitle=% E7%BB%88%E6%9E%81%E6%8C%87%E6%A0%87)
    [同花顺学院](http://www.iwencai.com/yike/detail/auid/e89b98d39da975e4)

    python API
    real=ULTOSC(high, low, close, timeperiod1=7, timeperiod2=14, timeperiod3=28)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.ULTOSC(high, low, close, timeperiod1=time_period1, timeperiod2=time_period2, timeperiod3=time_period3)


def WILLR(df, time_period=14):
    """
    函数名：WILLR
    名称：威廉指标

    简介：WMS表示的是市场处于超买还是超卖状态。股票投资分析方法主要有如下三种：基本分析、技术分析、演化分析。在实际应用中，它们既相互联系，又有重要区别。

    分析和应用：
    [百度百科](https://baike.baidu.com/item/% E5%A8%81%E5%BB%89%E6%8C%87%E6%A0%87?fr=aladdin)
    [维基百科](https://zh.wikipedia.org/wiki/% E5%A8%81%E5%BB%89%E6%8C%87%E6%A8%99)
    [同花顺学院](http://www.iwencai.com/yike/detail/auid/967febb0316c57c1)

    python API
    real=WILLR(high, low, close, timeperiod=14)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.WILLR(high, low, close, timeperiod=time_period)


################
# TA-LIB 量化分析数据
# Overlap Studies Functions
# 重叠研究指标
#################


def BBANDS(df, time_period=5, nb_de_vup=2, nb_dev_dn=2, ma_type=0):
    """
    函数名：BBANDS

    名称： 布林线指标
    简介：其利用统计原理，求出股价的标准差及其信赖区间，从而确定股价的波动范围及未来走势，利用波带显示股价的安全高低价位，因而也被称为布林带。

    分析和应用：
    [百度百科](https://baike.baidu.com/item/bollinger%20bands/1612394?fr=aladdin)
    [同花顺学院](http://www.iwencai.com/yike/detail/auid/56d0d9be66b4f7a0?rid=53)

    python API
    upperband, middleband, lowerband=BBANDS(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
    :return:
    """
    close = df['close']
    return talib.BBANDS(close, timeperiod=time_period, nbdevup=nb_de_vup, nbdevdn=nb_dev_dn, matype=ma_type)


def DEMA(df, time_period=30):
    """
    函数名：DEMA

    名称： 双移动平均线
    简介：两条移动平均线来产生趋势信号，较长期者用来识别趋势，较短期者用来选择时机。正是两条平均线及价格三者的相互作用，才共同产生了趋势信号。

    分析和应用：
    [百度百科](https://baike.baidu.com/item/%E5%8F%8C%E7%A7%BB%E5%8A%A8%E5%B9%B3%E5%9D%87%E7%BA%BF/1831921?fr=aladdin)
    [同花顺学院](http://www.iwencai.com/yike/detail/auid/a04d723659318237)

    python API
    real=DEMA(close, timeperiod=30)
    :return:
    """
    close = df['close']
    return talib.DEMA(close, timeperiod=time_period)


def HT_TRENDLINE(df):
    """
    函数名：HT_TRENDLINE
    名称： 希尔伯特瞬时变换

    简介：是一种趋向类指标，其构造原理是仍然对价格收盘价进行算术平均，并根据计算结果来进行分析，用于判断价格未来走势的变动趋势。

    分析和应用：
    [百度文库](https://wenku.baidu.com/view/0e35f6eead51f01dc281f18e.html)

    python API
    real=HT_TRENDLINE(close)
    :return:
    """
    close = df['close']
    return talib.HT_TRENDLINE(close)


def KAMA(df, time_period=30):
    """
    函数名：KAMA
    名称： 考夫曼的自适应移动平均线

    简介：短期均线贴近价格走势，灵敏度高，但会有很多噪声，产生虚假信号；长期均线在判断趋势上一般比较准确
    ，但是长期均线有着严重滞后的问题。我们想得到这样的均线，当价格沿一个方向快速移动时，短期的移动
    平均线是最合适的；当价格在横盘的过程中，长期移动平均线是合适的。

    分析和应用：
    [参考1](http://blog.sina.com.cn/s/blog_62d0bbc701010p7d.html)
    [参考2](https://wenku.baidu.com/view/bc4bc9c59ec3d5bbfd0a7454.html?from=search)

    python API
    real=KAMA(close, timeperiod=30)
    :return:
    """
    close = df['close']
    return talib.KAMA(close, timeperiod=time_period)


def MAMA(df, fast_limit=0, slow_limit=0):
    """
    python API
    mama, fama=MAMA(close, fastlimit=0, slowlimit=0)
    :return:
    """
    close = df['close']
    return talib.MAMA(close, fastlimit=fast_limit, slowlimit=slow_limit)


def MAVP(df, min_period=2, max_period=30, ma_type=0):
    """
     python API
    real=MAVP(close, periods, minperiod=2, maxperiod=30, matype=0)
    :return:
    """
    close = df['close']
    low = df['low']
    return talib.MAVP(close, low, minperiod=min_period, maxperiod=max_period, matype=ma_type)


def MIDPOINT(df, time_period=14):
    """
    python API
    real=MIDPOINT(close, timeperiod=14)
    :return:
    """
    close = df['close']
    return talib.MIDPOINT(close, timeperiod=time_period)


def MIDPRICE(df, time_period=14):
    """
    python API
    real=MIDPRICE(high, low, timeperiod=14)
    :return:
    """
    high = df['high']
    low = df['low']
    return talib.MIDPRICE(high, low, timeperiod=time_period)


def SAR(df, acceler_ation=0, max_imum=0):
    """
    函数名：SAR
    名称： 抛物线指标

    简介：抛物线转向也称停损点转向，是利用抛物线方式，随时调整停损点位置以观察买卖点。由于停损点（又称转向点SAR）以弧形的方式移动，故称之为抛物线转向指标。

    分析和应用：
    [百度百科](https://baike.baidu.com/item/SAR/2771135#viewPageContent)
    [同花顺学院](http://www.iwencai.com/yike/detail/auid/d9d94e65be7f6b5e)

    python API
    real=SAR(high, low, acceleration=0, maximum=0)
    :return:
    """
    high = df['high']
    low = df['low']
    return talib.SAR(high, low, acceleration=acceler_ation, maximum=max_imum)


def SAREXT(df, start_value=0, offset_onreverse=0, acceleration_init_long=0, acceleration_long=0,
           acceleration_max_long=0,
           acceleration_init_short=0, acceleration_short=0,
           acceleration_max_short=0):
    """
    python API
    real=SAREXT(high, low, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
    :return:
    """
    high = df['high']
    low = df['low']
    return talib.SAREXT(high, low, startvalue=start_value, offsetonreverse=offset_onreverse,
                        accelerationinitlong=acceleration_init_long, accelerationlong=acceleration_long,
                        accelerationmaxlong=acceleration_max_long, accelerationinitshort=acceleration_init_short,
                        accelerationshort=acceleration_short, accelerationmaxshort=acceleration_max_short)


def SMA(df, time_period=30):
    """
    函数名：SMA
    名称： 简单移动平均线

    简介：移动平均线，Moving Average，简称MA，原本的意思是移动平均，由于我们将其制作成线形，所以一般称之为移动平均线，简称均线。它是将某一段时间的收盘价之和除以该周期。 比如日线MA5指5天内的收盘价除以5 。

    分析和应用：
    [百度百科](https://baike.baidu.com/item/%E7%A7%BB%E5%8A%A8%E5%B9%B3%E5%9D%87%E7%BA%BF/217887?fromtitle=MA&fromid=1511750#viewPageContent)
    [同花顺学院](http://www.iwencai.com/yike/detail/auid/a04d723659318237?rid=96)

    python API
    real=SMA(close, timeperiod=30)
    :return:
    """
    close = df['close']
    return talib.SMA(close, timeperiod=time_period)


def T3(df, time_period=5, v_factor=0):
    """
    函数名：T3
    名称：三重指数移动平均线

    简介：TRIX长线操作时采用本指标的讯号，长时间按照本指标讯号交易，获利百分比大于损失百分比，利润相当可观。 比如日线MA5指5天内的收盘价除以5 。

    分析和应用：
    [百度百科](https://baike.baidu.com/item/%E4%B8%89%E9%87%8D%E6%8C%87%E6%95%B0%E5%B9%B3%E6%BB%91%E5%B9%B3%E5%9D%87%E7%BA%BF/15749345?fr=aladdin)
    [同花顺学院](http://www.iwencai.com/yike/detail/auid/6c22c15ccbf24e64?rid=80)

    python API
    real=T3(close, timeperiod=5, vfactor=0)
    :return:
    """
    close = df['close']
    return talib.T3(close, timeperiod=time_period, vfactor=v_factor)


def TEMA(df, time_period=30):
    """
    函数名：TEMA（T3 区别？）
    名称：三重指数移动平均线

    python API
    real=TEMA(close, timeperiod=30)
    :return:
    """
    close = df['close']
    return talib.TEMA(close, timeperiod=time_period)


def TRIMA(df, time_period=30):
    """
    python API
    real=TRIMA(close, timeperiod=30)
    :return:
    """
    close = df['close']
    return talib.TRIMA(close, timeperiod=time_period)


def WMA(df, time_period=30):
    """
    函数名：WMA
    名称：加权移动平均线

    简介：移动加权平均法是指以每次进货的成本加上原有库存存货的成本，除以每次进货数量与原有库存存货的数量之和，据以计算加权平均单位成本，以此为基础计算当月发出存货的成本和期末存货的成本的一种方法。

    分析和应用：
    [百度百科](https://baike.baidu.com/item/%E7%A7%BB%E5%8A%A8%E5%8A%A0%E6%9D%83%E5%B9%B3%E5%9D%87%E6%B3%95/10056490?fr=aladdin&fromid=16799870&fromtitle=%E5%8A%A0%E6%9D%83%E7%A7%BB%E5%8A%A8%E5%B9%B3%E5%9D%87)
    [同花顺学院](http://www.iwencai.com/yike/detail/auid/262b1dfd1c68ee30)

    python API
    real=WMA(close, timeperiod=30)
    :return:
    """
    close = df['close']
    return talib.WMA(close, timeperiod=time_period)


################
# TA-LIB 量化分析数据
# Pattern Recognition Functions
# 形态识别
#################


def CDL2CROWS(df):
    """
    函数名：CDL2CROWS
    名称：Two Crows 两只乌鸦

    简介：三日K线模式，第一天长阳，第二天高开收阴，第三天再次高开继续收阴，收盘比前一日收盘价低，预示股价下跌。

    python API
    integer=CDL2CROWS(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDL2CROWS(open, high, low, close)


def CDL3BLACKCROWS(df):
    """
    函数名：CDL3BLACKCROWS
    名称：Three Black Crows 三只乌鸦

    简介：三日K线模式，连续三根阴线，每日收盘价都下跌且接近最低价，每日开盘价都在上根K线实体内，预示股价下跌。

    python API
    integer=CDL3BLACKCROWS(open, high, low, close)
    :param df:
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDL3BLACKCROWS(open, high, low, close)


def CDL3INSIDE(df):
    """
    函数名：CDL3INSIDE
    名称： Three Inside Up/Down 三内部上涨和下跌

    简介：三日K线模式，母子信号 + 长K线，以三内部上涨为例，K线为阴阳阳，第三天收盘价高于第一天开盘价，第二天K线在第一天K线内部，预示着股价上涨。

    python API
    integer=CDL3INSIDE(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDL3INSIDE(open, high, low, close)


def CDL3LINESTRIKE(df):
    """
    函数名：CDL3LINESTRIKE
    名称： Three - Line Strike 三线打击

    简介：四日K线模式，前三根阳线，每日收盘价都比前一日高，开盘价在前一日实体内，第四日市场高开，收盘价低于第一日开盘价，预示股价下跌。

    python API
    integer=CDL3LINESTRIKE(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDL3LINESTRIKE(open, high, low, close)


def CDL3OUTSIDE(df):
    """
    函数名：CDL3OUTSIDE
    名称：Three Outside Up/Down 三外部上涨和下跌

    简介：三日K线模式，与三内部上涨和下跌类似，K线为阴阳阳，但第一日与第二日的K线形态相反，以三外部上涨为例，第一日K线在第二日K线内部，预示着股价上涨。

    python API
    integer=CDL3OUTSIDE(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDL3OUTSIDE(open, high, low, close)


def CDL3STARSINSOUTH(df):
    """
    函数名：CDL3STARSINSOUTH
    名称：Three Stars In The South 南方三星

    简介：三日K线模式，与大敌当前相反，三日K线皆阴，第一日有长下影线，第二日与第一日类似，K线整体小于第一日，第三日无下影线实体信号，成交价格都在第一日振幅之内，预示下跌趋势反转，股价上升。

    python API
    integer=CDL3STARSINSOUTH(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDL3STARSINSOUTH(open, high, low, close)


def CDL3WHITESOLDIERS(df):
    """
    函数名：CDL3WHITESOLDIERS
    名称：Three Advancing White Soldiers 三个白兵

    简介：三日K线模式，三日K线皆阳，每日收盘价变高且接近最高价，开盘价在前一日实体上半部，预示股价上升。

    python API
    integer=CDL3WHITESOLDIERS(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDL3WHITESOLDIERS(open, high, low, close)


def CDLABANDONEDBABY(df):
    """
    函数名：CDLABANDONEDBABY
    名称：Abandoned Baby 弃婴

    简介：三日K线模式，第二日价格跳空且收十字星（开盘价与收盘价接近，最高价最低价相差不大），预示趋势反转，发生在顶部下跌，底部上涨。

    python API
    integer=CDLABANDONEDBABY(open, high, low, close, penetration=0)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLABANDONEDBABY(open, high, low, close)


def CDLADVANCEBLOCK(df):
    """
    函数名：CDLADVANCEBLOCK
    名称：Advance Block 大敌当前

    简介：三日K线模式，三日都收阳，每日收盘价都比前一日高，开盘价都在前一日实体以内，实体变短，上影线变长。

    python API
    integer=CDLADVANCEBLOCK(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLADVANCEBLOCK(open, high, low, close)


def CDLBELTHOLD(df):
    """
    函数名：CDLBELTHOLD
    名称：Belt - hold 捉腰带线

    简介：两日K线模式，下跌趋势中，第一日阴线，第二日开盘价为最低价，阳线，收盘价接近最高价，预示价格上涨。

    python API
    integer=CDLBELTHOLD(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLBELTHOLD(open, high, low, close)


def CDLBREAKAWAY(df):
    """
    函数名：CDLBREAKAWAY
    名称：Breakaway 脱离
    简介：五日K线模式，以看涨脱离为例，下跌趋势中，第一日长阴线，第二日跳空阴线，延续趋势开始震荡，第五日长阳线，收盘价在第一天收盘价与第二天开盘价之间，预示价格上涨。

    python API
    integer=CDLBREAKAWAY(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLBREAKAWAY(open, high, low, close)


def CDLCLOSINGMARUBOZU(df):
    """
    函数名：CDLCLOSINGMARUBOZU
    名称：Closing Marubozu 收盘缺影线

    简介：一日K线模式，以阳线为例，最低价低于开盘价，收盘价等于最高价，预示着趋势持续。

    python API
    integer=CDLCLOSINGMARUBOZU(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLCLOSINGMARUBOZU(open, high, low, close)


def CDLCONCEALBABYSWALL(df):
    """
     函数名：CDLCONCEALBABYSWALL
    名称： Concealing Baby Swallow 藏婴吞没

    简介：四日K线模式，下跌趋势中，前两日阴线无影线，第二日开盘、收盘价皆低于第二日，第三日倒锤头，第四日开盘价高于前一日最高价，收盘价低于前一日最低价，预示着底部反转。

    python API
    integer=CDLCONCEALBABYSWALL(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLCONCEALBABYSWALL(open, high, low, close)


def CDLCOUNTERATTACK(df):
    """
    函数名：CDLCOUNTERATTACK
    名称：Counterattack 反击线
    简介：二日K线模式，与分离线类似。

    python API
    integer=CDLCOUNTERATTACK(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLCOUNTERATTACK(open, high, low, close)


def CDLDARKCLOUDCOVER(df):
    """
    函数名：CDLDARKCLOUDCOVER
    名称：Dark Cloud Cover 乌云压顶

    简介：二日K线模式，第一日长阳，第二日开盘价高于前一日最高价，收盘价处于前一日实体中部以下，预示着股价下跌。

    python API
    integer=CDLDARKCLOUDCOVER(open, high, low, close, penetration=0)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLDARKCLOUDCOVER(open, high, low, close)


def CDLDOJI(df):
    """
    函数名：CDLDOJI
    名称：Doji 十字

    简介：一日K线模式，开盘价与收盘价基本相同。

    python API
    integer=CDLDOJI(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLDOJI(open, high, low, close)


def CDLDOJISTAR(df):
    """
    函数名：CDLDOJISTAR
    名称：Doji Star 十字星
    简介：一日K线模式，开盘价与收盘价基本相同，上下影线不会很长，预示着当前趋势反转。

    python API
    integer=CDLDOJISTAR(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLDOJISTAR(open, high, low, close)


def CDLDRAGONFLYDOJI(df):
    """
    函数名：CDLDRAGONFLYDOJI
    名称：Dragonfly Doji
    蜻蜓十字/T形十字

    简介：一日K线模式，开盘后价格一路走低，之后收复，收盘价与开盘价相同，预示趋势反转。

    python API
    integer=CDLDRAGONFLYDOJI(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLDRAGONFLYDOJI(open, high, low, close)


def CDLENGULFING(df):
    """
    函数名：CDLENGULFING
    名称：Engulfing Pattern 吞噬模式

    简介：两日K线模式，分多头吞噬和空头吞噬，以多头吞噬为例，第一日为阴线，第二日阳线，第一日的开盘价和收盘价在第二日开盘价收盘价之内，但不能完全相同。

    python API
    integer=CDLENGULFING(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLENGULFING(open, high, low, close)


def CDLEVENINGDOJISTAR(df):
    """
    函数名：CDLEVENINGDOJISTAR
    名称：Evening Doji Star 十字暮星

    简介：三日K线模式，基本模式为暮星，第二日收盘价和开盘价相同，预示顶部反转。

    python API
    integer=CDLEVENINGDOJISTAR(open, high, low, close, penetration=0)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLEVENINGDOJISTAR(open, high, low, close)


def CDLEVENINGSTAR(df):
    """
    函数名：CDLEVENINGSTAR
    名称：Evening Star 暮星

    简介：三日K线模式，与晨星相反，上升趋势中,第一日阳线，第二日价格振幅较小，第三日阴线，预示顶部反转。

    python API
    integer=CDLEVENINGSTAR(open, high, low, close, penetration=0)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLEVENINGSTAR(open, high, low, close)


def CDLGAPSIDESIDEWHITE(df):
    """
    函数名：CDLGAPSIDESIDEWHITE
    名称：Up/Down - gap side - by - side white lines 向上/下跳空并列阳线

    简介：二日K线模式，上升趋势向上跳空，下跌趋势向下跳空,第一日与第二日有相同开盘价，实体长度差不多，则趋势持续。

    python API
    integer=CDLGAPSIDESIDEWHITE(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLGAPSIDESIDEWHITE(open, high, low, close)


def CDLGRAVESTONEDOJI(df):
    """
    函数名：CDLGRAVESTONEDOJI
    名称：Gravestone Doji 墓碑十字/倒T十字

    简介：一日K线模式，开盘价与收盘价相同，上影线长，无下影线，预示底部反转。

    python API
    integer=CDLGRAVESTONEDOJI(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLGRAVESTONEDOJI(open, high, low, close)


def CDLHAMMER(df):
    """
    函数名：CDLHAMMER
    名称：Hammer 锤头

    简介：一日K线模式，实体较短，无上影线，下影线大于实体长度两倍，处于下跌趋势底部，预示反转。

    python API
    integer=CDLHAMMER(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLHAMMER(open, high, low, close)


def CDLHANGINGMAN(df):
    """
    函数名：CDLHANGINGMAN
    名称：Hanging Man 上吊线

    简介：一日K线模式，形状与锤子类似，处于上升趋势的顶部，预示着趋势反转。

    python API
    integer=CDLHANGINGMAN(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLHANGINGMAN(open, high, low, close)


def CDLHARAMI(df):
    """
    函数名：CDLHARAMI
    名称：Harami Pattern 母子线

    简介：二日K线模式，分多头母子与空头母子，两者相反，以多头母子为例，在下跌趋势中，第一日K线长阴，第二日开盘价收盘价在第一日价格振幅之内，为阳线，预示趋势反转，股价上升。

    python API
    integer=CDLHARAMI(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLHARAMI(open, high, low, close)


def CDLHARAMICROSS(df):
    """
    函数名：CDLHARAMICROSS
    名称：Harami Cross Pattern 十字孕线

    简介：二日K线模式，与母子县类似，若第二日K线是十字线，便称为十字孕线，预示着趋势反转。

    python API
    integer=CDLHARAMICROSS(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLHARAMICROSS(open, high, low, close)


def CDLHIGHWAVE(df):
    """
    函数名：CDLHIGHWAVE
    名称：High - Wave Candle 风高浪大线

    简介：三日K线模式，具有极长的上/下影线与短的实体，预示着趋势反转。

    python API
    integer=CDLHIGHWAVE(open, high, low, close)
    :return:
    """
    close = df['close']
    return talib.CDLHIGHWAVE(open, high, low, close)


def CDLHIKKAKE(df):
    """
    函数名：CDLHIKKAKE
    名称：Hikkake Pattern 陷阱

    简介：三日K线模式，与母子类似，第二日价格在前一日实体范围内,第三日收盘价高于前两日，反转失败，趋势继续。

    python API
    integer=CDLHIKKAKE(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLHIKKAKE(open, high, low, close)


def CDLHIKKAKEMOD(df):
    """
    函数名：CDLHIKKAKEMOD
    名称：Modified Hikkake Pattern 修正陷阱

    简介：三日K线模式，与陷阱类似，上升趋势中，第三日跳空高开；下跌趋势中，第三日跳空低开，反转失败，趋势继续。

    python API
    integer=CDLHIKKAKEMOD(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLHIKKAKEMOD(open, high, low, close)


def CDLHOMINGPIGEON(df):
    """
    函数名：CDLHOMINGPIGEON
    名称：Homing Pigeon 家鸽

    简介：二日K线模式，与母子线类似，不同的的是二日K线颜色相同，第二日最高价、最低价都在第一日实体之内，预示着趋势反转。

    python API
    integer=CDLHOMINGPIGEON(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLHOMINGPIGEON(open, high, low, close)


def CDLIDENTICAL3CROWS(df):
    """
    函数名：CDLIDENTICAL3CROWS
    名称：Identical Three Crows 三胞胎乌鸦

    简介：三日K线模式，上涨趋势中，三日都为阴线，长度大致相等，每日开盘价等于前一日收盘价，收盘价接近当日最低价，预示价格下跌。

    python API
    integer=CDLIDENTICAL3CROWS(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLIDENTICAL3CROWS(open, high, low, close)


def CDLINNECK(df):
    """
    函数名：CDLINNECK
    名称：In - Neck Pattern 颈内线

    简介：二日K线模式，下跌趋势中，第一日长阴线，第二日开盘价较低，收盘价略高于第一日收盘价，阳线，实体较短，预示着下跌继续。

    python API
    integer=CDLINNECK(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLINNECK(open, high, low, close)


def CDLINVERTEDHAMMER(df):
    """
    函数名：CDLINVERTEDHAMMER
    名称：Inverted Hammer 倒锤头

    简介：一日K线模式，上影线较长，长度为实体2倍以上，无下影线，在下跌趋势底部，预示着趋势反转。

    python API
    integer=CDLINVERTEDHAMMER(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLINVERTEDHAMMER(open, high, low, close)


def CDLKICKING(df):
    """
    函数名：CDLKICKING
    名称：Kicking 反冲形态

    简介：二日K线模式，与分离线类似，两日K线为秃线，颜色相反，存在跳空缺口。

    python API
    integer=CDLKICKING(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLKICKING(open, high, low, close)


def CDLKICKINGBYLENGTH(df):
    """
    函数名：CDLKICKINGBYLENGTH
    名称：Kicking - bull/bear determined by the longer marubozu 由较长缺影线决定的反冲形态

    简介：二日K线模式，与反冲形态类似，较长缺影线决定价格的涨跌。

    python API
    integer=CDLKICKINGBYLENGTH(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLKICKINGBYLENGTH(open, high, low, close)


def CDLLADDERBOTTOM(df):
    """
    函数名：CDLLADDERBOTTOM
    名称：Ladder Bottom 梯底

    简介：五日K线模式，下跌趋势中，前三日阴线，开盘价与收盘价皆低于前一日开盘、收盘价，第四日倒锤头，第五日开盘价高于前一日开盘价，阳线，收盘价高于前几日价格振幅，预示着底部反转。

    python API
    integer=CDLLADDERBOTTOM(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLLADDERBOTTOM(open, high, low, close)


def CDLLONGLEGGEDDOJI(df):
    """
    函数名：CDLLONGLEGGEDDOJI
    名称：Long Legged Doji 长脚十字

    简介：一日K线模式，开盘价与收盘价相同居当日价格中部，上下影线长，表达市场不确定性。

    python API
    integer=CDLLONGLEGGEDDOJI(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLLONGLEGGEDDOJI(open, high, low, close)


def CDLLONGLINE(df):
    """
    函数名：CDLLONGLINE
    名称：Long Line Candle 长蜡烛
    简介：一日K线模式，K线实体长，无上下影线。

    python API
    integer=CDLLONGLINE(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLLONGLINE(open, high, low, close)


def CDLMARUBOZU(df):
    """
    函数名：CDLMARUBOZU
    名称：Marubozu 光头光脚/缺影线

    简介：一日K线模式，上下两头都没有影线的实体，阴线预示着熊市持续或者牛市反转，阳线相反。

    python API
    integer=CDLMARUBOZU(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLMARUBOZU(open, high, low, close)


def CDLMATCHINGLOW(df):
    """
    函数名：CDLMATCHINGLOW
    名称：Matching Low 相同低价

    简介：二日K线模式，下跌趋势中，第一日长阴线，第二日阴线，收盘价与前一日相同，预示底部确认，该价格为支撑位。

    python API
    integer=CDLMATCHINGLOW(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLMATCHINGLOW(open, high, low, close)


def CDLMATHOLD(df):
    """
    函数名：CDLMATHOLD
    名称：Mat Hold 铺垫

    简介：五日K线模式，上涨趋势中，第一日阳线，第二日跳空高开影线，第三、四日短实体影线，第五日阳线，收盘价高于前四日，预示趋势持续。

    python API
    integer=CDLMATHOLD(open, high, low, close, penetration=0)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLMATHOLD(open, high, low, close)


def CDLMORNINGDOJISTAR(df):
    """
    函数名：CDLMORNINGDOJISTAR
    名称：Morning Doji Star 十字晨星

    简介：三日K线模式，基本模式为晨星，第二日K线为十字星，预示底部反转。

    python API
    integer=CDLMORNINGDOJISTAR(open, high, low, close, penetration=0)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLMORNINGDOJISTAR(open, high, low, close)


def CDLMORNINGSTAR(df):
    """
    函数名：CDLMORNINGSTAR
    名称：Morning Star 晨星

    简介：三日K线模式，下跌趋势，第一日阴线，第二日价格振幅较小，第三天阳线，预示底部反转。

    python API
    integer=CDLMORNINGSTAR(open, high, low, close, penetration=0)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLMORNINGSTAR(open, high, low, close)


def CDLONNECK(df):
    """
    函数名：CDLONNECK
    名称：On - Neck Pattern 颈上线

    简介：二日K线模式，下跌趋势中，第一日长阴线，第二日开盘价较低，收盘价与前一日最低价相同，阳线，实体较短，预示着延续下跌趋势。

    python API
    integer=CDLONNECK(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLONNECK(open, high, low, close)


def CDLPIERCING(df):
    """
    函数名：CDLPIERCING
    名称：Piercing Pattern 刺透形态

    简介：两日K线模式，下跌趋势中，第一日阴线，第二日收盘价低于前一日最低价，收盘价处在第一日实体上部，预示着底部反转。

    python API
    integer=CDLPIERCING(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLPIERCING(open, high, low, close)


def CDLRICKSHAWMAN(df):
    """
    函数名：CDLRICKSHAWMAN
    名称：Rickshaw Man 黄包车夫

    简介：一日K线模式，与长腿十字线类似，若实体正好处于价格振幅中点，称为黄包车夫。

    python API
    integer=CDLRICKSHAWMAN(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLRICKSHAWMAN(open, high, low, close)


def CDLRISEFALL3METHODS(df):
    """
     函数名：CDLRISEFALL3METHODS
    名称：Rising/Falling Three Methods 上升/下降三法

    简介： 五日K线模式，以上升三法为例，上涨趋势中，第一日长阳线，中间三日价格在第一日范围内小幅震荡，第五日长阳线，收盘价高于第一日收盘价，预示股价上升。

    python API
    integer=CDLRISEFALL3METHODS(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLRISEFALL3METHODS(open, high, low, close)


def CDLSEPARATINGLINES(df):
    """
     函数名：CDLSEPARATINGLINES
    名称：Separating Lines 分离线

    简介：二日K线模式，上涨趋势中，第一日阴线，第二日阳线，第二日开盘价与第一日相同且为最低价，预示着趋势继续。

    python API
    integer=CDLSEPARATINGLINES(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLSEPARATINGLINES(open, high, low, close)


def CDLSHOOTINGSTAR(df):
    """
    函数名：CDLSHOOTINGSTAR
    名称：Shooting Star 射击之星

    简介：一日K线模式，上影线至少为实体长度两倍，没有下影线，预示着股价下跌

    python API
    integer=CDLSHOOTINGSTAR(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLSHOOTINGSTAR(open, high, low, close)


def CDLSHORTLINE(df):
    """
    函数名：CDLSHORTLINE
    名称：Short Line Candle 短蜡烛

    简介：一日K线模式，实体短，无上下影线

    python API
    integer=CDLSHORTLINE(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLSHORTLINE(open, high, low, close)


def CDLSPINNINGTOP(df):
    """
    函数名：CDLSPINNINGTOP
    名称：Spinning Top 纺锤

    简介：一日K线，实体小。

    python API
    integer=CDLSPINNINGTOP(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLSPINNINGTOP(open, high, low, close)


def CDLSTALLEDPATTERN(df):
    """
    函数名：CDLSTALLEDPATTERN
    名称：Stalled Pattern 停顿形态

    简介：三日K线模式，上涨趋势中，第二日长阳线，第三日开盘于前一日收盘价附近，短阳线，预示着上涨结束

    python API
    integer=CDLSTALLEDPATTERN(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLSTALLEDPATTERN(open, high, low, close)


def CDLSTICKSANDWICH(df):
    """
    函数名：CDLSTICKSANDWICH
    名称：Stick Sandwich 条形三明治

    简介：三日K线模式，第一日长阴线，第二日阳线，开盘价高于前一日收盘价，第三日开盘价高于前两日最高价，收盘价于第一日收盘价相同。

    python API
    integer=CDLSTICKSANDWICH(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLSTICKSANDWICH(open, high, low, close)


def CDLTAKURI(df):
    """
    函数名：CDLTAKURI
    名称：Takuri(Dragonfly Doji with very long lower shadow) 探水竿
    简介：一日K线模式，大致与蜻蜓十字相同，下影线长度长。

    python API
    integer=CDLTAKURI(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLTAKURI(open, high, low, close)


def CDLTASUKIGAP(df):
    """
    函数名：CDLTASUKIGAP
    名称：Tasuki Gap 跳空并列阴阳线

    简介：三日K线模式，分上涨和下跌，以上升为例，前两日阳线，第二日跳空，第三日阴线，收盘价于缺口中，上升趋势持续。

    python API
    integer=CDLTASUKIGAP(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLTASUKIGAP(open, high, low, close)


def CDLTHRUSTING(df):
    """
    函数名：CDLTHRUSTING
    名称：Thrusting Pattern 插入

    简介：二日K线模式，与颈上线类似，下跌趋势中，第一日长阴线，第二日开盘价跳空，收盘价略低于前一日实体中部，与颈上线相比实体较长，预示着趋势持续。

    python API
    integer=CDLTHRUSTING(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLTHRUSTING(open, high, low, close)


def CDLTRISTAR(df):
    """
    函数名：CDLTRISTAR
    名称：Tristar Pattern 三星

    简介：三日K线模式，由三个十字组成，第二日十字必须高于或者低于第一日和第三日，预示着反转。

    python API
    integer=CDLTRISTAR(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLTRISTAR(open, high, low, close)


def CDLUNIQUE3RIVER(df):
    """
    函数名：CDLUNIQUE3RIVER
    名称：Unique 3 River 奇特三河床

    简介：三日K线模式，下跌趋势中，第一日长阴线，第二日为锤头，最低价创新低，第三日开盘价低于第二日收盘价，收阳线，收盘价不高于第二日收盘价，预示着反转，第二日下影线越长可能性越大。

    python API
    integer=CDLUNIQUE3RIVER(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLUNIQUE3RIVER(open, high, low, close)


def CDLUPSIDEGAP2CROWS(df):
    """
    函数名：CDLUPSIDEGAP2CROWS
    名称：Upside Gap Two Crows 向上跳空的两只乌鸦

    简介：三日K线模式，第一日阳线，第二日跳空以高于第一日最高价开盘，收阴线，第三日开盘价高于第二日，收阴线，与第一日比仍有缺口。

    python API
    integer=CDLUPSIDEGAP2CROWS(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLUPSIDEGAP2CROWS(open, high, low, close)


def CDLXSIDEGAP3METHODS(df):
    """
    函数名：CDLXSIDEGAP3METHODS
    名称：Upside/Downside Gap Three Methods 上升/下降跳空三法

    简介：五日K线模式，以上升跳空三法为例，上涨趋势中，第一日长阳线，第二日短阳线，第三日跳空阳线，第四日阴线，开盘价与收盘价于前两日实体内，第五日长阳线，收盘价高于第一日收盘价，预示股价上升。

    python API
    integer=CDLXSIDEGAP3METHODS(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.CDLXSIDEGAP3METHODS(open, high, low, close)


################
# TA-LIB 量化分析数据
# Price Transform Functions
#################


def AVGPRICE(df):
    """
    函数名：AVGPRICE
    名称：平均价格函数

    python API
    real=AVGPRICE(open, high, low, close)
    :return:
    """
    open = df['open']
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.AVGPRICE(open, high, low, close)


def MEDPRICE(df):
    """
    函数名：MEDPRICE
    名称：中位数价格

    python API
    real=MEDPRICE(high, low)
    :return:
    """
    high = df['high']
    low = df['low']
    return talib.MEDPRICE(high, low)


def TYPPRICE(df):
    """
    函数名：TYPPRICE
    名称：代表性价格

    python API
    real=TYPPRICE(high, low, close)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.TYPPRICE(high, low, close)


def WCLPRICE(df):
    """
    函数名：WCLPRICE
    名称：加权收盘价

    python API
    real=WCLPRICE(high, low, close)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.WCLPRICE(high, low, close)


################
# TA-LIB 量化分析数据
# Statistic Functions
# 统计学指标
#################


def BETA(df, time_period=5):
    """
    函数名：BETA
    名称：β系数也称为贝塔系数

    简介：一种风险指数，用来衡量个别股票或
    股票基金相对于整个股市的价格波动情况
    贝塔系数衡量股票收益相对于业绩评价基准收益的总体波动性，是一个相对指标。 β 越高，意味着股票相对于业绩评价基准的波动性越大。 β 大于 1 ，
    则股票的波动性大于业绩评价基准的波动性。反之亦然。

    用途：
    1）计算资本成本，做出投资决策（只有回报率高于资本成本的项目才应投资）；
    2）计算资本成本，制定业绩考核及激励标准；
    3）计算资本成本，进行资产估值（Beta是现金流贴现模型的基础）；
    4）确定单个资产或组合的系统风险，用于资产组合的投资管理，特别是股指期货或其他金融衍生品的避险（或投机）

    python API
    real=BETA(high, low, timeperiod=5)
    :return:
    """
    high = df['high']
    low = df['low']
    return talib.BETA(high, low, timeperiod=time_period)


def CORREL(df, time_period=30):
    """
    函数名：CORREL
    名称：皮尔逊相关系数

    简介：用于度量两个变量X和Y之间的相关（线性相关），其值介于-1与1之间
    皮尔逊相关系数是一种度量两个变量间相关程度的方法。它是一个介于 1 和 -1 之间的值，
    其中，1 表示变量完全正相关， 0 表示无关，-1 表示完全负相关。

    python API
    real=CORREL(high, low, timeperiod=30)
    :return:
    """
    high = df['high']
    low = df['low']
    return talib.CORREL(high, low, timeperiod=time_period)


def LINEARREG(df, time_period=14):
    """
    直线回归方程：当两个变量x与y之间达到显著地线性相关关系时,应用最小二乘法原理确定一条最优直线的直线方程y=a+bx,这条回归直线与个相关点的距离比任何其他直线与相关点的距离都小,是最佳的理想直线.
    回归截距a：表示直线在y轴上的截距,代表直线的起点.
    回归系数b：表示直线的斜率,他的实际意义是说明x每变化一个单位时,影响y平均变动的数量.
    即x每增加1单位,y变化b个单位.

    函数名：LINEARREG
    名称：线性回归
    简介：来确定两种或两种以上变量间相互依赖的定量关系的一种统计分析方法
    其表达形式为y=w'x+e，e为误差服从均值为0的正态分布。

    python API
    real=LINEARREG(close, timeperiod=14)
    :return:
    """
    close = df['close']
    return talib.LINEARREG(close, timeperiod=time_period)


def LINEARREG_ANGLE(df, time_period=14):
    """
    函数名：LINEARREG_ANGLE
    名称：线性回归的角度

    简介：来确定价格的角度变化.
    [参考](http://blog.sina.com.cn/s/blog_14c9f45b20102vv8p.md)

    python API
    real=LINEARREG_ANGLE(close, timeperiod=14)
    :return:
    """
    close = df['close']
    return talib.LINEARREG_ANGLE(close, timeperiod=time_period)


def LINEARREG_INTERCEPT(df, time_period=14):
    """
    函数名：LINEARREG_INTERCEPT
    名称：线性回归截距

    python API
    real=LINEARREG_INTERCEPT(close, timeperiod=14)
    :return:
    """
    close = df['close']
    return talib.LINEARREG_INTERCEPT(close, timeperiod=time_period)


def LINEARREG_SLOPE(df, time_period=14):
    """
    函数名：LINEARREG_SLOPE
    名称：线性回归斜率指标

    python API
    real=LINEARREG_SLOPE(close, timeperiod=14)
    :return:
    """
    close = df['close']
    return talib.LINEARREG_SLOPE(close, timeperiod=time_period)


def STDDEV(df, time_period=5, nb_dev=1):
    """
    函数名：STDDEV
    名称：标准偏差
    简介：种量度数据分布的分散程度之标准，用以衡量数据值偏离算术平均值的程度。标准偏差越小，这些值偏离平均值就越少，反之亦然。标准偏差的大小可通过标准偏差与平均值的倍率关系来衡量。

    python API
    real=STDDEV(close, timeperiod=5, nbdev=1)
    :return:
    """
    close = df['close']
    return talib.STDDEV(close, timeperiod=time_period, nbdev=nb_dev)


def TSF(df, time_period=14):
    """
    函数名：TSF
    名称：时间序列预测
    简介：一种历史资料延伸预测，也称历史引伸预测法。是以时间数列所能反映的社会经济现象的发展过程和规律性，进行引伸外推，预测其发展趋势的方法

    python API
    real=TSF(close, timeperiod=14)
    :return:
    """
    close = df['close']
    return talib.TSF(close, timeperiod=time_period)


def VAR(df, time_period=5, nb_dev=1):
    """
    函数名：  VAR
    名称：方差
    简介：方差用来计算每一个变量（观察值）与总体均数之间的差异。为避免出现离均差总和为零，离均差平方和受样本含量的影响，统计学采用平均离均差平方和来描述变量的变异程度

    python API
    real=VAR(close, timeperiod=5, nbdev=1)
    :return:
    """
    close = df['close']
    return talib.VAR(close, timeperiod=time_period, nbdev=nb_dev)


################
# TA-LIB 量化分析数据
# Volatility Indicator Functions
# 波动率指标函数
#################


def ATR(df, time_period=14):
    """
    函数名：ATR
    名称：真实波动幅度均值
    简介：真实波动幅度均值（ATR)是
    以 N 天的指数移动平均数平均後的交易波动幅度。
    计算公式：一天的交易幅度只是单纯地 最大值 - 最小值。
    而真实波动幅度则包含昨天的收盘价，若其在今天的幅度之外：
    真实波动幅度=max(最大值,昨日收盘价) − min(最小值,昨日收盘价) 真实波动幅度均值便是「真实波动幅度」的 N 日 指数移动平均数。

    特性：
    * 波动幅度的概念表示可以显示出交易者的期望和热情。
    * 大幅的或增加中的波动幅度表示交易者在当天可能准备持续买进或卖出股票。
    * 波动幅度的减少则表示交易者对股市没有太大的兴趣。

    python API
    real=ATR(high, low, close, timeperiod=14)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.ATR(high, low, close, timeperiod=time_period)


def NATR(df, time_period=14):
    """
    函数名：NATR
    名称：归一化波动幅度均值

    简介：归一化波动幅度均值（NATR)是

    python API
    real=NATR(high, low, close, timeperiod=14)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.NATR(high, low, close, timeperiod=time_period)


def TRANGE(df):
    """
    函数名：TRANGE
    名称：真正的范围

    python API
    real=TRANGE(high, low, close)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    return talib.TRANGE(high, low, close)


################
# TA-LIB 量化分析数据
# Volume Indicators
# 成交量指标
#################


def AD(df):
    """
    函数名：AD
    名称：Chaikin A/D Line 累积/派发线（Accumulation/Distribution Line）
    简介：Marc Chaikin提出的一种平衡交易量指标，以当日的收盘价位来估算成交流量，用于估定一段时间内该证券累积的资金流量。

    计算公式：
    A/D=昨日A/D + 多空对比 * 今日成交量
    多空对比=[（收盘价- 最低价） - （最高价 - 收盘价）]/（最高价 - 最低价)
    若最高价等于最低价： 多空对比=（收盘价/昨收盘） - 1

    研判：
    1、A/D测量资金流向，向上的A/D表明买方占优势，而向下的A/D表明卖方占优势
    2、A/D与价格的背离可视为买卖信号，即底背离考虑买入，顶背离考虑卖出
    3、应当注意A/D忽略了缺口的影响，事实上，跳空缺口的意义是不能轻易忽略的
    A/D指标无需设置参数，但在应用时，可结合指标的均线进行分析

    Python API
    real=AD(high, low, close, volume)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    volume = df['volume']
    return talib.AD(high, low, close, volume)


def ADOSC(df, fast_period=3, slow_period=10):
    """
    函数名：ADOSC
    名称：Chaikin A/D Oscillator Chaikin震荡指标
    简介：将资金流动情况与价格行为相对比，检测市场中资金流入和流出的情况

    计算公式：fastperiod A/D - slowperiod A/D

    研判：
    1、交易信号是背离：看涨背离做多，看跌背离做空
    2、股价与90天移动平均结合，与其他指标结合
    3、由正变负卖出，由负变正买进

    Python API
    real=ADOSC(high, low, close, volume, fastperiod=3, slowperiod=10)
    :return:
    """
    high = df['high']
    low = df['low']
    close = df['close']
    volume = df['volume']
    return talib.ADOSC(high, low, close, volume, fastperiod=fast_period, slowperiod=slow_period)


def OBV(df):
    """
    函数名：OBV
    名称：On Balance Volume 能量潮
    简介：Joe Granville提出，通过统计成交量变动的趋势推测股价趋势

    计算公式：以某日为基期，逐日累计每日上市股票总成交量，若隔日指数或股票上涨
    ，则基期OBV加上本日成交量为本日OBV。隔日指数或股票下跌，
    则基期OBV减去本日成交量为本日OBV

    研判：
    1、以“N”字型为波动单位，一浪高于一浪称“上升潮”，下跌称“跌潮”；上升潮买进，跌潮卖出
    2、须配合K线图走势
    3、用多空比率净额法进行修正，但不知TA-Lib采用哪种方法

    计算公式： 多空比率净额= [（收盘价－最低价）－（最高价-收盘价）] ÷（ 最高价－最低价）×成交量

    Python API
    real=OBV(close, volume)
    :return:
    """
    close = df['close']
    volume = df['volume']
    return talib.OBV(close, volume)
