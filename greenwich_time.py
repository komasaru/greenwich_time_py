#! /usr/local/bin/python3.6
"""
グリニジ視恒星時 GAST(= Greenwich Apparent Sidereal Time)等の計算
: IAU2006 による計算

  * IAU SOFA(International Astronomical Union, Standards of Fundamental Astronomy)
    の提供する C ソースコード "gst06.c" 等で実装されているアルゴリズムを使用する。
  * 参考サイト
    - [SOFA Library Issue 2016-05-03 for ANSI C: Complete List]
      (http://www.iausofa.org/2016_0503_C/CompleteList.html)
    - [USNO Circular 179]
      (http://aa.usno.navy.mil/publications/docs/Circular_179.php)
    - [IERS Conventions Center]
      (http://62.161.69.131/iers/conv2003/conv2003_c5.html)

  Date          Author          Version
  2016.06.21    mk-mode.com     1.00 新規作成

Copyright(C) 2016 mk-mode.com All Rights Reserved.
---
  引数: 日時(TT（地球時）)
          書式：YYYYMMDD or YYYYMMDDHHMMSS
          無指定なら現在(システム日時)を地球時とみなす。
"""
from datetime import datetime
import re
import sys
import traceback
# Original library
from lib import cip_cio     as lcc
from lib import const       as lcst
from lib import greenwich   as lgw
from lib import nutation    as lnt
from lib import precision   as lpr
from lib import rotation_fw as lfw
from lib import time        as ltm


class GreenwichTime:
    def __init__(self):
        self.__get_arg()

    def exec(self):
        try:
            # === Time calculation
            self.jd     = ltm.calc_jd(self.tt)
            self.jc     = ltm.calc_jc(self.jd)
            self.dt     = ltm.calc_dt(self.tt)
            self.ut1    = ltm.tt2ut1(self.tt, self.dt)
            self.jd_ut1 = ltm.calc_jd(self.ut1)
            # === Fukushima-Williams angles for frame bias and precession.
            #       Ref: iauPfw06(date1, date2, &gamb, &phib, &psib, &epsa)
            prec = lpr.Precision(self.jc)
            self.gam_b, self.phi_b, self.psi_b = prec.calc_pfw_06()
            self.eps_a = prec.calc_obl_06()
            # === Nutation components.
            #       Ref: iauNut06a(date1, date2, &dp, &de)
            nut = lnt.Nutation(self.jc)
            self.d_psi, self.d_eps = nut.calc_nut_06_a()
            # === Equinox based nutation x precession x bias matrix.
            #       Ref: iauFw2m(gamb, phib, psib + dp, epsa + de, rnpb)
            r_fw = lfw.RotationFw()
            self.r_mtx = r_fw.fw2m(
                self.gam_b, self.phi_b,
                self.psi_b + self.d_psi,
                self.eps_a + self.d_eps
            )
            # === Extract CIP coordinates.
            #       Ref: iauBpn2xy(rnpb, &x, &y)
            cc = lcc.CipCio(self.jc)
            self.x, self.y = cc.bpn2xy(self.r_mtx)
            # === The CIO locator, s.
            #       Ref: iauS06(tta, ttb, x, y)
            self.s = cc.s_06(self.x, self.y)
            # Greenwich time
            gw = lgw.Greenwich(self.jd_ut1)
            # === Greenwich apparent sidereal time.
            #       Ref: iauEra00(uta, utb), iauEors(rnpb, s)
            self.era = gw.era_00()
            self.eo = gw.eors(self.r_mtx, self.s)
            self.gast = gw.gast(self.era, self.eo)
            self.gast_deg = self.gast / lcst.PI_180
            # === Greenwich mean sidereal time, IAU 2006.
            #       Ref: iauGmst06(uta, utb, tta, ttb)
            self.gmst = gw.gmst(self.era, self.jc)
            self.gmst_deg = self.gmst / lcst.PI_180
            # === Equation of Equinoxes
            self.ee = gw.ee(self.gast, self.gmst)
            self.ee_deg = self.ee / lcst.PI_180
            # === Display
            self.__display()
        except Exception as e:
            raise

    def __get_arg(self):
        """ コマンドライン引数の取得
            * コマンドライン引数で指定した日時を self.tt に設定
            * コマンドライン引数が存在しなければ、現在時刻を self.tt に設定
        """
        try:
            if len(sys.argv) < 2:
                self.tt = datetime.now()
                return
            if re.search(r"^(\d{8}|\d{14}|\d{20})$", sys.argv[1]) is not(None):
                dt = sys.argv[1].ljust(20, "0")
            else:
                sys.exit(0)
            try:
                self.tt = datetime.strptime(dt, "%Y%m%d%H%M%S%f")
            except ValueError as e:
                print("Invalid date!")
                sys.exit(0)
        except Exception as e:
            raise

    def __display(self):
        """ Display """
        try:
            print((
                "     TT = {}\n"
                "    UT1 = {}\n"
                " JD(TT) = {}\n"
                "JD(UT1) = {}\n"
                "     JC = {}\n"
                "     DT = {}\n"
                " GAMMA_ = {}\n"
                "   PHI_ = {}\n"
                "   PSI_ = {}\n"
                "  EPS_A = {}\n"
                "  D_PSI = {}\n"
                "  D_EPS = {}\n"
                "  r_mtx = \n{}\n"
                "      x = {}\n"
                "      y = {}\n"
                "      s = {}\n"
                "    ERA = {} rad\n"
                "     EO = {} rad\n"
                "   GAST = {} rad\n"
                "        = {} °\n"
                "        = {}\n"
                "   GMST = {} rad\n"
                "        = {} °\n"
                "        = {}\n"
                "     EE = {} rad\n"
                "        = {} °\n"
                "        = {}"
            ).format(
                self.tt.strftime("%Y-%m-%d %H:%M:%S.%f"),
                self.ut1.strftime("%Y-%m-%d %H:%M:%S.%f"),
                self.jd,
                self.jd_ut1,
                self.jc,
                self.dt,
                self.gam_b,
                self.phi_b,
                self.psi_b,
                self.eps_a,
                self.d_psi,
                self.d_eps,
                self.r_mtx,
                self.x,
                self.y,
                self.s,
                self.era,
                self.eo,
                self.gast,
                self.gast_deg,
                ltm.deg2hms(self.gast_deg),
                self.gmst,
                self.gmst_deg,
                ltm.deg2hms(self.gmst_deg),
                self.ee,
                self.ee_deg,
                ltm.deg2hms(self.ee_deg)
            ))
        except Exception as e:
            raise


if __name__ == '__main__':
    try:
        GreenwichTime().exec()
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

