module Greenwich
  #===========================================================================
  # Class for nutations
  #===========================================================================
  class Nutation
    #-------------------------------------------------------------------------
    # Initialization
    #
    # @param: t  (Julian Centry)
    #-------------------------------------------------------------------------
    def initialize(t)
      @t = t
      @dat_ls = get_data(DAT_LS)
      @dat_pl = get_data(DAT_PL)
    end

    #-------------------------------------------------------------------------
    # IAU 2000A nutation with adjustments to match the IAU 2006 precession.
    #
    # @param:  <none>
    # @return: [delta Psi, delta Eps]
    #-------------------------------------------------------------------------
    def calc_nut_06_a
      # Factor correcting for secular variation of J2.
      fj2 = -2.7774e-6 * @t
      # Calculation
      d_psi_ls, d_eps_ls = calc_lunisolar(@t)
      d_psi_pl, d_eps_pl = calc_planetary(@t)
      d_psi, d_eps = d_psi_ls + d_psi_pl, d_eps_ls + d_eps_pl
      # Apply P03 adjustments (Wallace & Capitaine, 2006, Eqs.5).
      d_psi += d_psi * (0.4697e-6 + fj2);
      d_eps += d_eps * fj2;
      return [d_psi, d_eps]
    rescue => e
      raise
    end

    private

    #-------------------------------------------------------------------------
    # テキストファイルからデータ取得
    #
    # * luni-solar の最初の5列、planetary の最初の14列は整数に、
    #   残りの列は浮動小数点*10000にする
    #
    # @param:  file  (Textfile's name)
    # @return: data  (Array)
    #-------------------------------------------------------------------------
    def get_data(file)
      c = file == DAT_LS ? 5 : 14
      return File.open(file, "r").read.split("\n")[1..-1].map do |l|
        l = l.sub(/^\s+/, "").split(/\s+/)
        l[0, c].map(&:to_i) + l[c..-1].map { |a| a.sub(/\./, "").to_i }
      end
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # 日月章動(luni-solar nutation)の計算
    #
    # @param:  t  (Julian Century)
    # @return: [delta Psi, delta Eps]
    #-------------------------------------------------------------------------
    def calc_lunisolar(t)
      dp, de = 0.0, 0.0

      begin
        l  = calc_l_iers2003(t)
        lp = calc_lp_mhb2000(t)
        f  = calc_f_iers2003(t)
        d  = calc_d_mhb2000(t)
        om = calc_om_iers2003(t)
        @dat_ls.reverse.each do |x|
          arg = (x[0] * l + x[1] * lp + x[2] * f +
                 x[3] * d + x[4] * om) % PI2
          sarg, carg = Math.sin(arg), Math.cos(arg)
          dp += (x[5] + x[6] * t) * sarg + x[ 7] * carg
          de += (x[8] + x[9] * t) * carg + x[10] * sarg
        end
        return [dp * U2R, de * U2R]
      rescue => e
        raise
      end
    end

    #-------------------------------------------------------------------------
    # 惑星章動(planetary nutation)
    #
    # @param:  t  (Julian Century)
    # @return: [delta Psi, delta Eps]
    #-------------------------------------------------------------------------
    def calc_planetary(t)
      dp, de = 0.0, 0.0

      begin
        l   = calc_l_mhb2000(t)
        f   = calc_f_mhb2000(t)
        d   = calc_d_mhb2000_2(t)
        om  = calc_om_mhb2000(t)
        pa  = calc_pa_iers2003(t)
        me = calc_me_iers2003(t)
        ve = calc_ve_iers2003(t)
        ea = calc_ea_iers2003(t)
        ma = calc_ma_iers2003(t)
        ju = calc_ju_iers2003(t)
        sa = calc_sa_iers2003(t)
        ur = calc_ur_iers2003(t)
        ne = calc_ne_mhb2000(t)
        @dat_pl.reverse.each do |x|
          arg = (x[ 0] * l  + x[ 2] * f  + x[ 3] * d  + x[ 4] * om +
                 x[ 5] * me + x[ 6] * ve + x[ 7] * ea + x[ 8] * ma +
                 x[ 9] * ju + x[10] * sa + x[11] * ur + x[12] * ne +
                 x[13] * pa) % PI2
          sarg, carg = Math.sin(arg), Math.cos(arg)
          dp += x[14] * sarg + x[15] * carg
          de += x[16] * sarg + x[17] * carg
        end
        return [dp * U2R, de * U2R]
      rescue => e
        raise
      end
    end
  end
end

