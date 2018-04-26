"""
Module for time
"""
from datetime import timedelta
from lib import const as cst


def calc_jd(tt):
    """ ユリウス日の計算
        * 地球時 self.tt のユリウス日を計算し、self.jd に設定

    :param  datetime tt: 地球時
    :return float      : ユリウス日
    """
    year, month,  day    = tt.year, tt.month,  tt.day
    hour, minute, second = tt.hour, tt.minute, tt.second
    try:
        if month < 3:
            year  -= 1
            month += 12
        d = int(365.25 * year) + year // 400  - year // 100 \
          + int(30.59 * (month - 2)) + day + 1721088.5
        t  = (second / 3600 + minute / 60 + hour) / 24
        return d + t
    except Exception as e:
        raise

def calc_jc(jd):
    """ ユリウス世紀数の計算

    :param   float jd: Julian Day
    :return: float jc: Julian Centry Number
    """
    try:
        return (jd - cst.J2000) / cst.JC
    except Exception as e:
        raise

def calc_dt(tt):
    """ ΔT の計算
        * 1972-01-01 以降、うるう秒挿入済みの年+αまでは、以下で算出
            TT - UTC = ΔT + DUT1 = TAI + 32.184 - UTC = ΔAT + 32.184
          [うるう秒実施日一覧](http://jjy.nict.go.jp/QandA/data/leapsec.html)

    :param  datetime tt: 時刻オブジェクト
    :return float    dt: delta T
    """
    year, month = tt.year, tt.month
    try:
        ym = "{:04d}-{:02d}".format(year, month)
        y = year + (month - 0.5) / 12
        if year < -500:
            t = (y - 1820) / 100
            dt  = -20 + 32 * t ** 2
        elif -500 <= year and year < 500:
            t = y / 100
            dt =  10583.6           \
               + (-1014.41          \
               + (   33.78311       \
               + (   -5.952053      \
               + (   -0.1798452     \
               + (    0.022174192   \
               + (    0.0090316521) \
               * t) * t) * t) * t) * t) * t
        elif 500 <= year and year < 1600:
            t = (y - 1000) / 100
            dt =  1574.2           \
               + (-556.01          \
               + (  71.23472       \
               + (   0.319781      \
               + (  -0.8503463     \
               + (  -0.005050998   \
               + (   0.0083572073) \
               * t) * t) * t) * t) * t) * t
        elif 1600 <= year and year < 1700:
            t = y - 1600
            dt =  120           \
               + ( -0.9808      \
               + ( -0.01532     \
               + (  1.0 / 7129) \
               * t) * t) * t
        elif 1700 <= year and year < 1800:
            t = y - 1700
            dt =   8.83           \
               + ( 0.1603         \
               + (-0.0059285      \
               + ( 0.00013336     \
               + (-1.0 / 1174000) \
               * t) * t) * t) * t
        elif 1800 <= year and year < 1860:
            t = y - 1800
            dt =  13.72            \
               + (-0.332447        \
               + ( 0.0068612       \
               + ( 0.0041116       \
               + (-0.00037436      \
               + ( 0.0000121272    \
               + (-0.0000001699    \
               + ( 0.000000000875) \
               * t) * t) * t) * t) * t) * t) * t
        elif 1860 <= year and year < 1900:
            t = y - 1860
            dt =   7.62          \
               + ( 0.5737        \
               + (-0.251754      \
               + ( 0.01680668    \
               + (-0.0004473624  \
               + ( 1.0 / 233174) \
               * t) * t) * t) * t) * t
        elif 1900 <= year and year < 1920:
            t = y - 1900
            dt =  -2.79      \
               + ( 1.494119  \
               + (-0.0598939 \
               + ( 0.0061966 \
               + (-0.000197) \
               * t) * t) * t) * t
        elif 1920 <= year and year < 1941:
            t = y - 1920
            dt =  21.20       \
               + ( 0.84493    \
               + (-0.076100   \
               + ( 0.0020936) \
               * t) * t) * t
        elif 1941 <= year and year < 1961:
            t = y - 1950
            dt =  29.07        \
               + ( 0.407       \
               + (-1.0 / 233   \
               + ( 1.0 / 2547) \
               * t) * t) * t
        elif 1961 <= year and year < 1986:
            if ym < "{:04d}-{:02d}".format(1972, 1):
                t = y - 1975
                dt =  45.45       \
                   + ( 1.067      \
                   + (-1.0 / 260  \
                   + (-1.0 / 718) \
                   * t) * t) * t
            # NICT Ver.
            elif ym < "{:04d}-{:02d}".format(1972, 7):
                dt = cst.TT_TAI + 10
            elif ym < "{:04d}-{:02d}".format(1973, 1):
                dt = cst.TT_TAI + 11
            elif ym < "{:04d}-{:02d}".format(1974, 1):
                dt = cst.TT_TAI + 12
            elif ym < "{:04d}-{:02d}".format(1975, 1):
                dt = cst.TT_TAI + 13
            elif ym < "{:04d}-{:02d}".format(1976, 1):
                dt = cst.TT_TAI + 14
            elif ym < "{:04d}-{:02d}".format(1977, 1):
                dt = cst.TT_TAI + 15
            elif ym < "{:04d}-{:02d}".format(1978, 1):
                dt = cst.TT_TAI + 16
            elif ym < "{:04d}-{:02d}".format(1979, 1):
                dt = cst.TT_TAI + 17
            elif ym < "{:04d}-{:02d}".format(1980, 1):
                dt = cst.TT_TAI + 18
            elif ym < "{:04d}-{:02d}".format(1981, 7):
                dt = cst.TT_TAI + 19
            elif ym < "{:04d}-{:02d}".format(1982, 7):
                dt = cst.TT_TAI + 20
            elif ym < "{:04d}-{:02d}".format(1983, 7):
                dt = cst.TT_TAI + 21
            elif ym < "{:04d}-{:02d}".format(1985, 7):
                dt = cst.TT_TAI + 22
            elif ym < "{:04d}-{:02d}".format(1988, 1):
                dt = cst.TT_TAI + 23
        elif 1986 <= year and year < 2005:
            t = y - 2000
            dt =  63.86           \
               + ( 0.3345         \
               + (-0.060374       \
               + ( 0.0017275      \
               + ( 0.000651814    \
               + ( 0.00002373599) \
               * t) * t) * t) * t) * t
            # NICT Ver.
            if   ym < "{:04d}-{:02d}".format(1988, 1):
                dt = cst.TT_TAI + 23
            elif ym < "{:04d}-{:02d}".format(1990, 1):
                dt = cst.TT_TAI + 24
            elif ym < "{:04d}-{:02d}".format(1991, 1):
                dt = cst.TT_TAI + 25
            elif ym < "{:04d}-{:02d}".format(1992, 7):
                dt = cst.TT_TAI + 26
            elif ym < "{:04d}-{:02d}".format(1993, 7):
                dt = cst.TT_TAI + 27
            elif ym < "{:04d}-{:02d}".format(1994, 7):
                dt = cst.TT_TAI + 28
            elif ym < "{:04d}-{:02d}".format(1996, 1):
                dt = cst.TT_TAI + 29
            elif ym < "{:04d}-{:02d}".format(1997, 7):
                dt = cst.TT_TAI + 30
            elif ym < "{:04d}-{:02d}".format(1999, 1):
                dt = cst.TT_TAI + 31
            elif ym < "{:04d}-{:02d}".format(2006, 1):
                dt = cst.TT_TAI + 32
        elif 2005 <= year and year < 2050:
            if   ym < "{:04d}-{:02d}".format(2006, 1):
                dt = cst.TT_TAI + 32
            elif ym < "{:04d}-{:02d}".format(2009, 1):
                dt = cst.TT_TAI + 33
            elif ym < "{:04d}-{:02d}".format(2012, 7):
                dt = cst.TT_TAI + 34
            elif ym < "{:04d}-{:02d}".format(2015, 7):
                dt = cst.TT_TAI + 35
            elif ym < "{:04d}-{:02d}".format(2017, 1):
                dt = cst.TT_TAI + 36
            elif ym < "{:04d}-{:02d}".format(2019, 1):
                # 第28回うるう秒実施までの暫定措置
                dt = cst.TT_TAI + 37
            else:
                t = y - 2000
                dt =  62.92      \
                   + ( 0.32217   \
                   + ( 0.005589) \
                   * t) * t
        elif 2050 <= year and year <= 2150:
            dt = -20 \
               + 32 * ((y - 1820) / 100) ** 2 \
               - 0.5628 * (2150 - y)
        elif 2150 < year:
            t = (y - 1820) / 100.0
            dt = -20 + 32 * t ** 2
        return dt
    except Exception as e:
        raise

def tt2ut1(tt, dt):
    """ TT -> UT1

    param  datetime tt: 地球時の時刻オブジェクト
    param  float    dt: delta T
    return float   ut1: Universal Time 1, 世界時1
    """
    try:
        return tt - timedelta(seconds=dt)
    except Exception as e:
        raise

def deg2hms(deg):
    """ 99.999° -> 99h99m99s 変換

    :param  float deg: Degree
    :return string   : "99 h 99 m 99.999 s"
    """
    sign = ""
    try:
        h = int(deg / 15)
        _m = (deg - h * 15) * 4
        m = int(_m)
        s = (_m - m) * 60
        if s < 0:
            s *= -1
            sign = "-"
        return "{:s}{:2d} h {:02d} m {:06.3f} s".format(sign, h, m, s)
    except Exception as e:
        raise

