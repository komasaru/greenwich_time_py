module Greenwich
  #===========================================================================
  # Class for
  #   ERA(Earth rotation angle (IAU 2000 model), 地球回転角),
  #   EORS(Equation of the origins, 原点差)
  #   GMST(Greenwich mean sidereal time, グリニッジ平均恒星時)
  #   GAST(Greenwich apparent sidereal time, グリニッジ視恒星時)
  #   EE(Equation of Equinoxes, 分点均差)
  #===========================================================================
  class GreenwichTime
    #-------------------------------------------------------------------------
    # Initialization
    #
    # @param:  jd  (Julian Day)
    #-------------------------------------------------------------------------
    def initialize(jd)
      @jd, @t = jd, jd - J2000  # JD, JD2000.0
    end

    #-------------------------------------------------------------------------
    # Earth rotation angle (IAU 2000 model).
    #
    # @param:  <none>
    # @return: ERA  (Earth rotation angle (Unit: rad, Range: 0-2pi), 地球回転角)
    #-------------------------------------------------------------------------
    def calc_era_00
      # Fractional part of T (days).
      f = @jd % 1.0
      # Earth rotation angle at this UT1.
      return norm_angle((f + 0.7790572732640 + 0.00273781191135448 * @t) * PI2)
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Equation of the origins, given the classical NPB matrix and the
    # quantity s.
    #
    # @param:  r   (Rotation matrix)
    # @param:  s   (CIO locator)
    # @return: EO  (Equation of the origin (Unit: rad), 原点差)
    #-------------------------------------------------------------------------
    def calc_eors(r_mtx, s)
      x = r_mtx[2][0]
      ax = x / (1.0 + r_mtx[2][2])
      xs = 1.0 - ax * x
      ys = -ax * r_mtx[2][1]
      zs = -x
      p = r_mtx[0][0] * xs + r_mtx[0][1] * ys + r_mtx[0][2] * zs
      q = r_mtx[1][0] * xs + r_mtx[1][1] * ys + r_mtx[1][2] * zs
      return (p != 0 || q != 0) ? s - Math.atan2(q, p) : s
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Greenwich apparent sidereal time
    #
    # @param:  era   (Earth rotation angle)
    # @param:  eo    (Equation of the origin)
    # @return: GAST  (Greenwich apparent sidereal time (Unit: rad), グリニッジ視恒星時)
    #-------------------------------------------------------------------------
    def calc_gast(era, eo)
      return norm_angle(era - eo)
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Greenwich mean sidereal time, IAU 2006.
    #
    # @param:  gast  (Greenwich apparent sidereal time, グリニッジ視恒星時)
    # @param:  t     (Julian Century)
    # @return: GMST  (Greenwich mean sidereal time (Unit: rad), グリニッジ平均恒星時)
    #-------------------------------------------------------------------------
    def calc_gmst(gast, t)
      return norm_angle(gast +
        (   0.014506    + \
        (4612.156534    + \
        (   1.3915817   + \
        (  -0.00000044  + \
        (  -0.000029956 + \
        (  -0.0000000368) \
        * t) * t) * t) * t) * t) * AS2R)
    rescue => e
      raise
    end
    #-------------------------------------------------------------------------
    # Equation of Equinoxes
    #
    # @param:  gast  (Greenwich apparent sidereal time, グリニッジ視恒星時)
    # @param:  gmst  (Greenwich mean sidereal time, グリニッジ平均恒星時)
    # @return: EE    (Equation of Equinoxes (Unit: rad), 分点均差)
    #-------------------------------------------------------------------------
    def calc_ee(gast, gmst)
      return gast - gmst
    rescue => e
      raise
    end
  end
end

