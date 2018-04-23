#! /usr/local/bin/ruby
# coding: utf-8
#---------------------------------------------------------------------------------
#= グリニジ視恒星時 GAST(= Greenwich Apparent Sidereal Time)等の計算
#  : IAU2006 による計算
#
#  * IAU SOFA(International Astronomical Union, Standards of Fundamental Astronomy)
#    の提供する C ソースコード "gst06.c" 等で実装されているアルゴリズムを使用する。
#  * 参考サイト
#    - [SOFA Library Issue 2016-05-03 for ANSI C: Complete List](http://www.iausofa.org/2016_0503_C/CompleteList.html)
#    - [USNO Circular 179](http://aa.usno.navy.mil/publications/docs/Circular_179.php)
#    - [IERS Conventions Center](http://62.161.69.131/iers/conv2003/conv2003_c5.html)
#
# Date          Author          Version
# 2016.06.21    mk-mode.com     1.00 新規作成
#
# Copyright(C) 2016 mk-mode.com All Rights Reserved.
#---------------------------------------------------------------------------------
# 引数 : 日時(TT（地球時）)
#          書式：YYYYMMDD or YYYYMMDDHHMMSS
#          無指定なら現在(システム日時)を地球時とみなす。
#---------------------------------------------------------------------------------
#++
$: << File.dirname(__FILE__)
require 'date'
require 'lib/greenwich'
include Greenwich

class CalcGreenwichTime
  def initialize
    @tt = get_arg
  end

  def calc
    begin
      # Time calculation
      jd     = calc_jd(@tt)
      jc     = calc_jc(jd)
      dt     = calc_dt(@tt)
      ut1    = tt2ut1(@tt, dt)
      jd_ut1 = calc_jd(ut1)
      puts @tt.strftime("     TT = %Y-%m-%d %H:%M:%S.%L")
      puts ut1.strftime("    UT1 = %Y-%m-%d %H:%M:%S.%L")
      puts " JD(TT) = #{jd}"
      puts "JD(UT1) = #{jd_ut1}"
      puts "     JC = #{jc}"
      puts "     DT = #{dt}"

      # Fukushima-Williams angles for frame bias and precession.
      #   Ref: iauPfw06(date1, date2, &gamb, &phib, &psib, &epsa)
      prec = Precession.new(jc)
      gam_b, phi_b, psi_b = prec.calc_pfw_06
      eps_a               = prec.calc_obl_06
      puts " GAMMA_ = #{gam_b}"
      puts "   PHI_ = #{phi_b}"
      puts "   PSI_ = #{psi_b}"
      puts "  EPS_A = #{eps_a}"

      # Nutation components.
      #   Ref: iauNut06a(date1, date2, &dp, &de)
      d_psi, d_eps = Nutation.new(jc).calc_nut_06_a
      puts "  D_PSI = #{d_psi}"
      puts "  D_EPS = #{d_eps}"

      # Equinox based nutation x precession x bias matrix.
      #   Ref: iauFw2m(gamb, phib, psib + dp, epsa + de, rnpb)
      r_mtx = RotationFw.new.fw2m(gam_b, phi_b, psi_b + d_psi, eps_a + d_eps)
      puts "  r_mtx = #{r_mtx}"

      # Extract CIP coordinates.
      #   Ref: iauBpn2xy(rnpb, &x, &y)
      cc = CipCio.new(jc)
      x, y = cc.bpn2xy(r_mtx)
      puts "      x = #{x}"
      puts "      y = #{y}"

      # The CIO locator, s.
      #   Ref: iauS06(tta, ttb, x, y)
      s = cc.calc_s_06(x, y)
      puts "      s = #{s}"

      # Greenwich time
      gt = GreenwichTime.new(jd_ut1)

      # Greenwich apparent sidereal time.
      #   Ref: iauEra00(uta, utb), iauEors(rnpb, s)
      era = gt.calc_era_00
      puts "    ERA = #{era} rad"
      eo = gt.calc_eors(r_mtx, s)
      puts "     EO = #{eo} rad"
      gast = gt.calc_gast(era, eo)
      gast_deg = gast / PI_180
      puts "   GAST = #{gast} rad"
      puts "        = #{gast_deg} °"
      puts "        = #{deg2hms(gast_deg)}"

      # Greenwich mean sidereal time, IAU 2006.
      #   Ref: iauGmst06(uta, utb, tta, ttb)
      gmst = gt.calc_gmst(era, jc)
      gmst_deg = gmst / PI_180
      puts "   GMST = #{gmst} rad"
      puts "        = #{gmst_deg} °"
      puts "        = #{deg2hms(gmst_deg)}"

      # Equation of Equinoxes
      ee = gt.calc_ee(gast, gmst)
      ee_deg = ee / PI_180
      puts "     EE = #{ee} rad"
      puts "        = #{ee_deg} °"
      puts "        = #{deg2hms(ee_deg)}"
    rescue => e
      msg = "[#{e.class}] #{e.message}\n"
      msg << e.backtrace.map { |tr| "\t#{tr}"}.join("\n")
      $stderr.puts msg
      exit 1
    end
  end

  private

  # コマンドライン引数の取得
  def get_arg
    unless arg = ARGV.shift
      t = Time.now
      return Time.new(t.year, t.month, t.day, t.hour, t.min, t.sec)
    end
    exit 0 unless arg =~ /^\d{8}$|^\d{14}$/
    year, month, day = arg[ 0, 4].to_i, arg[ 4, 2].to_i, arg[ 6, 2].to_i
    exit 0 unless Date.valid_date?(year, month, day)
    hour, min,   sec = arg[ 8, 2].to_i, arg[10, 2].to_i, arg[12, 2].to_i
    exit 0 if hour > 23 || min > 59 || sec > 59
    return Time.new(year, month, day, hour, min, sec)
  rescue => e
    raise
  end
end

exit 0 unless __FILE__ == $0
g = CalcGreenwichTime.new.calc

