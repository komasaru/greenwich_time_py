module Greenwich
  #===========================================================================
  # Module for Fundamental arguments
  #===========================================================================
  module FundamentalArgument
    module_function

    #-------------------------------------------------------------------------
    # Mean anomaly of the Moon (IERS 2003)
    #
    # @param:  t  (Julian Centry)
    # @return: l  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_l_iers2003(t)
      return ((    485868.249036  + \
              (1717915923.2178    + \
              (        31.8792    + \
              (         0.051635  + \
              (        -0.00024470) \
              * t) * t) * t) * t) % TURNAS) * AS2R
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Mean anomaly of the Sun (IERS 2003)
    #
    # @param:  t  (Julian Centry)
    # @return: p  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_p_iers2003(t)
      return ((   1287104.793048  + \
              ( 129596581.0481    + \
              (       - 0.5532    + \
              (         0.000136  + \
              (       - 0.00001149) \
              * t) * t) * t) * t) % TURNAS) * AS2R
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Mean longitude of the Moon minus that of the ascending node (IERS 2003)
    #
    # @param:  t  (Julian Centry)
    # @return: f  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_f_iers2003(t)
      return ((     335779.526232 + \
              (1739527262.8478    + \
              (       -12.7512    + \
              (        -0.001037  + \
              (         0.00000417) \
              * t) * t) * t) * t) % TURNAS) * AS2R
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # mean elongation of the Moon from the Sun (IERS 2003)
    #
    # @param:  t  (Julian Centry)
    # @return: d  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_d_iers2003(t)
      return ((   1072260.703692  + \
              (1602961601.2090    + \
              (       - 6.3706    + \
              (         0.006593  + \
              (       - 0.00003169) \
              * t) * t) * t) * t) % TURNAS ) * AS2R
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Mean longitude of the ascending node of the Moon (IERS 2003)
    #
    # @param:  t   (Julian Centry)
    # @return: om  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_om_iers2003(t)
     return ((    450160.398036  + \
             (  -6962890.5431    + \
             (         7.4722    + \
             (         0.007702  + \
             (        -0.00005939) \
             * t) * t) * t) * t) % TURNAS) * AS2R
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Venus longitudes (IERS 2003)
    #
    # @param:  t   (Julian Centry)
    # @return: ve  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_ve_iers2003(t)
      return (3.176146697 + 1021.3285546211 * t) % PI2
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Earth longitudes (IERS 2003)
    #
    # @param:  t   (Julian Centry)
    # @return: ea  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_ea_iers2003(t)
      return (1.753470314 + 628.3075849991 * t) % PI2
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # General accumulated precession in longitude (IERS 2003)
    #
    # @param:  t   (Julian Centry)
    # @return: pa  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_pa_iers2003(t)
      return (0.024381750 + 0.00000538691 * t) * t
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Mercury longitudes (IERS 2003)
    #
    # @param:  t   (Julian Centry)
    # @return: me  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_me_iers2003(t)
      return (4.402608842 + 2608.7903141574 * t) % PI2
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Mars longitudes (IERS 2003)
    #
    # @param:  t   (Julian Centry)
    # @return: ma  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_ma_iers2003(t)
      return (6.203480913 + 334.0612426700 * t) % PI2
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Jupiter longitudes (IERS 2003)
    #
    # @param:  t   (Julian Centr()
    # @return: ju  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_ju_iers2003(t)
      return (0.599546497 + 52.9690962641 * t) % PI2
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Saturn longitudes (IERS 2003)
    #
    # @param:  t   (Julian Centry)
    # @return: sa  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_sa_iers2003(t)
      return (0.874016757 + 21.3299104960 * t) % PI2
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Uranus longitudes (IERS 2003)
    #
    # @param:  t   (Julian Centry)
    # @return: ur  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_ur_iers2003(t)
      return (5.481293872 + 7.4781598567 * t) % PI2
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Mean anomaly of the Sun (MHB2000)
    #
    # @param:  t   (Julian Centry)
    # @return: lp  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_lp_mhb2000(t)
      return ((  1287104.79305   + \
              (129596581.0481    + \
              (       -0.5532    + \
              (        0.000136  + \
              (       -0.00001149) \
              * t) * t) * t) * t) % TURNAS) * AS2R
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Mean elongation of the Moon from the Sun (MHB2000)
    #
    # @param:  t  (Julian Centry)
    # @return: d  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_d_mhb2000(t)
      return ((   1072260.70369   + \
              (1602961601.2090    + \
              (        -6.3706    + \
              (         0.006593  + \
              (        -0.00003169) \
              * t) * t) * t) * t) % TURNAS) * AS2R
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Mean anomaly of the Moon (MHB2000)
    #
    # @param:  t  (Julian Centry)
    # @return: l  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_l_mhb2000(t)
      return (2.35555598 + 8328.6914269554 * t) % PI2
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Mean longitude of the Moon minus that of the ascending node (MHB2000)
    #
    # @param:  t  (Julian Centry)
    # @return: f  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_f_mhb2000(t)
      return (1.627905234 + 8433.466158131 * t) % PI2
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Mean elongation of the Moon from the Sun (MHB2000)
    #
    # @param:  t  (Julian Centry)
    # @return: d  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_d_mhb2000_2(t)
      return (5.198466741 + 7771.3771468121 * t) % PI2
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Mean longitude of the ascending node of the Moon (MHB2000)
    #
    # @param:  t   (Julian Centry)
    # @return: om  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_om_mhb2000(t)
      return (2.18243920 - 33.757045 * t) % PI2
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Neptune longitude (MHB2000)
    #
    # @param:  t   (Julian Centry)
    # @return: ne  (Unit: rad)
    #-------------------------------------------------------------------------
    def calc_ne_mhb2000(t)
      return (5.321159000 + 3.8127774000 * t) % PI2
    rescue => e
      raise
    end
  end
end

