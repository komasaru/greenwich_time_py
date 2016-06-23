module Greenwich
  #===========================================================================
  # Module for time
  #===========================================================================
  module Time
    module_function

    #-------------------------------------------------------------------------
    # ユリウス日の計算
    #
    # @param:  tt  (Terrestrial Time, 地球時の時刻オブジェクト)
    # @return: jd  (Julian Day)
    #-------------------------------------------------------------------------
    def calc_jd(tt)
      year, month, day = tt.year, tt.month, tt.day
      hour, min, sec   = tt.hour, tt.min, tt.sec

      begin
        # 1月,2月は前年の13月,14月とする
        if month < 3
          year  -= 1
          month += 12
        end
        # 日付(整数)部分計算
        jd  = (365.25 * year).floor       \
            + (year / 400.0).floor        \
            - (year / 100.0).floor        \
            + (30.59 * (month - 2)).floor \
            + day                         \
            + 1721088.5
        # 時間(小数)部分計算
        t  = (sec / 3600.0 + min / 60.0 + hour) / 24.0
        return jd + t
      rescue => e
        raise
      end
    end

    #-------------------------------------------------------------------------
    # ユリウス世紀数の計算
    #
    # @param:  jd  (Julian Day)
    # @return: jc  (Julian Centry)
    #-------------------------------------------------------------------------
    def calc_jc(jd)
      return (jd - J2000) / JC
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # ΔT の計算
    #
    # * 1972-01-01 以降、うるう秒挿入済みの年+αまでは、以下で算出
    #     TT - UTC = ΔT + DUT1 = TAI + 32.184 - UTC = ΔAT + 32.184
    #   [うるう秒実施日一覧](http://jjy.nict.go.jp/QandA/data/leapsec.html)
    #
    # @param:  tt  (時刻オブジェクト)
    # @return: dt  (delta T)
    #-------------------------------------------------------------------------
    def calc_dt(tt)
      year, month = tt.year, tt.month
      ym = sprintf("%04d-%02d", year, month)
      y = year + (month - 0.5) / 12
      case
      when year < -500
        t = (y - 1820) / 100.0
        dt  = -20 + 32 * t ** 2
      when -500 <= year && year < 500
        t = y / 100.0
        dt  = 10583.6
             (-1014.41        + \
             (   33.78311     + \
             (   -5.952053    + \
             (   -0.1798452   + \
             (    0.022174192 + \
             (    0.0090316521) \
             * t) * t) * t) * t) * t) * t
      when 500 <= year && year < 1600
        t = (y - 1000) / 100.0
        dt  = 1574.2         + \
             (-556.01        + \
             (  71.23472     + \
             (   0.319781    + \
             (  -0.8503463   + \
             (  -0.005050998 + \
             (   0.0083572073) \
             * t) * t) * t) * t) * t) * t
      when 1600 <= year && year < 1700
        t = y - 1600
        dt  = 120           + \
             ( -0.9808      + \
             ( -0.01532     + \
             (  1.0 / 7129.0) \
             * t) * t) * t
      when 1700 <= year && year < 1800
        t = y - 1700
        dt  =  8.83           + \
             ( 0.1603         + \
             (-0.0059285      + \
             ( 0.00013336     + \
             (-1.0 / 1174000.0) \
             * t) * t) * t) * t
      when 1800 <= year && year < 1860
        t = y - 1800
        dt  = 13.72          + \
             (-0.332447      + \
             ( 0.0068612     + \
             ( 0.0041116     + \
             (-0.00037436    + \
             ( 0.0000121272  + \
             (-0.0000001699  + \
             ( 0.000000000875) \
             * t) * t) * t) * t) * t) * t) * t
      when 1860 <= year && year < 1900
        t = y - 1860
        dt  =  7.62          + \
             ( 0.5737        + \
             (-0.251754      + \
             ( 0.01680668    + \
             (-0.0004473624  + \
             ( 1.0 / 233174.0) \
             * t) * t) * t) * t) * t
      when 1900 <= year && year < 1920
        t = y - 1900
        dt  = -2.79      + \
             ( 1.494119  + \
             (-0.0598939 + \
             ( 0.0061966 + \
             (-0.000197  ) \
             * t) * t) * t) * t
      when 1920 <= year && year < 1941
        t = y - 1920
        dt  = 21.20     + \
             ( 0.84493  + \
             (-0.076100 + \
             ( 0.0020936) \
             * t) * t) * t
      when 1941 <= year && year < 1961
        t = y - 1950
        dt  = 29.07      + \
             ( 0.407     + \
             (-1 / 233.0 + \
             ( 1 / 2547.0) \
             * t) * t) * t
      when 1961 <= year && year < 1986
        case
        when ym < sprintf("%04d-%02d", 1972, 1)
          t = y - 1975
          dt = 45.45      + \
              ( 1.067     + \
              (-1 / 260.0 + \
              (-1 / 718.0)  \
              * t) * t) * t
        # NICT Ver.
        when ym < sprintf("%04d-%02d", 1972, 7); dt = TT_TAI + 10
        when ym < sprintf("%04d-%02d", 1973, 1); dt = TT_TAI + 11
        when ym < sprintf("%04d-%02d", 1974, 1); dt = TT_TAI + 12
        when ym < sprintf("%04d-%02d", 1975, 1); dt = TT_TAI + 13
        when ym < sprintf("%04d-%02d", 1976, 1); dt = TT_TAI + 14
        when ym < sprintf("%04d-%02d", 1977, 1); dt = TT_TAI + 15
        when ym < sprintf("%04d-%02d", 1978, 1); dt = TT_TAI + 16
        when ym < sprintf("%04d-%02d", 1979, 1); dt = TT_TAI + 17
        when ym < sprintf("%04d-%02d", 1980, 1); dt = TT_TAI + 18
        when ym < sprintf("%04d-%02d", 1981, 7); dt = TT_TAI + 19
        when ym < sprintf("%04d-%02d", 1982, 7); dt = TT_TAI + 20
        when ym < sprintf("%04d-%02d", 1983, 7); dt = TT_TAI + 21
        when ym < sprintf("%04d-%02d", 1985, 7); dt = TT_TAI + 22
        when ym < sprintf("%04d-%02d", 1988, 1); dt = TT_TAI + 23
        end
      when 1986 <= year && year < 2005
        #t = y - 2000
        #dt  = 63.86         + \
        #     ( 0.3345       + \
        #     (-0.060374     + \
        #     ( 0.0017275    + \
        #     ( 0.000651814  + \
        #     ( 0.00002373599) \
        #     * t) * t) * t) * t) * t
        # NICT Ver.
        case
        when ym < sprintf("%04d-%02d", 1988, 1); dt = TT_TAI + 23
        when ym < sprintf("%04d-%02d", 1990, 1); dt = TT_TAI + 24
        when ym < sprintf("%04d-%02d", 1991, 1); dt = TT_TAI + 25
        when ym < sprintf("%04d-%02d", 1992, 7); dt = TT_TAI + 26
        when ym < sprintf("%04d-%02d", 1993, 7); dt = TT_TAI + 27
        when ym < sprintf("%04d-%02d", 1994, 7); dt = TT_TAI + 28
        when ym < sprintf("%04d-%02d", 1996, 1); dt = TT_TAI + 29
        when ym < sprintf("%04d-%02d", 1997, 7); dt = TT_TAI + 30
        when ym < sprintf("%04d-%02d", 1999, 1); dt = TT_TAI + 31
        when ym < sprintf("%04d-%02d", 2006, 1); dt = TT_TAI + 32
        end
      when 2005 <= year && year < 2050
        case
        when ym < sprintf("%04d-%02d", 2006, 1); dt = TT_TAI + 32
        when ym < sprintf("%04d-%02d", 2009, 1); dt = TT_TAI + 33
        when ym < sprintf("%04d-%02d", 2012, 7); dt = TT_TAI + 34
        when ym < sprintf("%04d-%02d", 2015, 7); dt = TT_TAI + 35
        when ym < sprintf("%04d-%02d", 2018, 1); dt = TT_TAI + 36  # <= 第27回うるう秒実施までの暫定措置
        else
          t = y - 2000
          dt  = 62.92    + \
               ( 0.32217 + \
               ( 0.005589) \
               * t) * t
        end
      when 2050 <= year && year <= 2150
        dt  = -20 \
            + 32 * ((y - 1820) / 100.0) ** 2
            - 0.5628 * (2150 - y)
      when 2150 < year
        t = (y - 1820) / 100.0
        dt  = -20 + 32 * t ** 2
      end
      return dt
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # TT -> UT1
    #
    # @param:  tt   (地球時の時刻オブジェクト)
    # @param:  dt   (delta T)
    # @return: ut1  (Universal Time 1, 世界時1)
    #-------------------------------------------------------------------------
    def tt2ut1(tt, dt)
      return tt - dt
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # 99.999° -> 99h99m99s 変換
    #
    # @param:  deg  (Degree)
    # @return: "99 h 99 m 99.999 s"
    #-------------------------------------------------------------------------
    def deg2hms(deg)
      sign = ""

      begin
        h = (deg / 15.0).truncate
        _m = (deg - h * 15.0) * 4.0
        m = _m.truncate
        s = (_m - m) * 60.0
        if s < 0
          s *= -1
          sign = "-"
        end
        return sprintf("%s%2d h %02d m %06.3f s", sign, h, m, s)
      rescue => e
        raise
      end
    end
  end
end

