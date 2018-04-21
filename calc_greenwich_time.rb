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
# 2016.09.06    mk-mode.com     1.00 新規作成
#
# Copyright(C) 2016 mk-mode.com All Rights Reserved.
#---------------------------------------------------------------------------------
# 引数 : 日時(UTC（協定世界時）)
#          書式：YYYYMMDD or YYYYMMDDHHMMSS
#          無指定なら現在(システム日時)を UTC とみなす。
#---------------------------------------------------------------------------------
#++
require 'mk_greenwich'

class CalcGreenwichTime
  def initialize
    @utc = get_arg
  end

  def calc
    begin
      g = MkGreenwich.new(@utc.strftime("%Y%m%d%H%M%S"))
      puts g.utc.strftime(" UTC = %Y-%m-%d %H:%M:%S.%L")
      puts g.tt.strftime("  TT = %Y-%m-%d %H:%M:%S.%L")
      puts g.ut1.strftime(" UT1 = %Y-%m-%d %H:%M:%S.%L")
      puts g.tdb.strftime(" TDB = %Y-%m-%d %H:%M:%S.%L")
      puts " ERA = #{g.era}"
      puts "  EO = #{g.eo}"
      puts "GAST = #{g.gast} rad"
      puts "     = #{g.gast_deg} °"
      puts "     = #{g.gast_hms}"
      puts "GMST = #{g.gmst} rad"
      puts "     = #{g.gmst_deg} °"
      puts "     = #{g.gmst_hms}"
      puts "  EE = #{g.ee} rad"
      puts "     = #{g.ee_deg} °"
      puts "     = #{g.ee_hms}"
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

