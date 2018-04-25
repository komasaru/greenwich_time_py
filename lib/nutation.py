"""
Class for nutations
"""
import math
import re
from lib import const as cst
from lib import fundamental_argument as fa


class Nutation:
    def __init__(self, t):
        """ Initialization

        :param float t: Julian Centry Number
        """
        self.t = t
        self.dat_ls = []
        self.dat_pl = []
        self.__get_data()

    def calc_nut_06_a(self):
        """ IAU 2000A nutation with adjustments to match the IAU 2006 precession.

        :return list: [delta Psi, delta Eps]
        """
        try:
            # Factor correcting for secular variation of J2.
            fj2 = -2.7774e-6 * self.t
            # Calculation
            d_psi_ls, d_eps_ls = self.__calc_lunisolar()
            d_psi_pl, d_eps_pl = self.__calc_planetary()
            d_psi, d_eps = d_psi_ls + d_psi_pl, d_eps_ls + d_eps_pl
            # Apply P03 adjustments (Wallace & Capitaine, 2006, Eqs.5).
            d_psi += d_psi * (0.4697e-6 + fj2)
            d_eps += d_eps * fj2
            return [d_psi, d_eps]
        except Exception as e:
            raise

    def __get_data(self):
        """ テキストファイル(DAT_LS, DAT_PL)からデータ取得
            * luni-solar の最初の5列、planetary の最初の14列は整数に、
              残りの列は浮動小数点*10000にする
            * 読み込みデータは self.dat_ls, self.dat_pl に格納
        """
        try:
            with open(cst.DAT_LS, "r") as f:
                data = f.read()
                for l in re.split('\n', data)[1:]:
                    l = re.sub(r'^\s+', "", l)
                    items = re.split(r'\s+', l)
                    if len(items) < 2:
                        break
                    items = [int(x) for x in items[:5]] \
                          + [int(re.sub(r'\.', "", x)) for x in items[5:]]
                    self.dat_ls.append(items)
            with open(cst.DAT_PL, "r") as f:
                data = f.read()
                for l in re.split('\n', data)[1:]:
                    l = re.sub(r'^\s+', "", l)
                    items = re.split(r'\s+', l)
                    if len(items) < 2:
                        break
                    items = [int(x) for x in items[:14]] \
                          + [int(re.sub(r'\.', "", x)) for x in items[14:]]
                    self.dat_pl.append(items)
        except Exception as e:
            raise

    def __calc_lunisolar(self):
        """ 日月章動(luni-solar nutation)の計算

        :return list: [delta Psi, delta Eps]
        """
        dp, de = 0.0, 0.0
        try:
            l  = fa.l_iers2003(self.t)
            lp = fa.lp_mhb2000(self.t)
            f  = fa.f_iers2003(self.t)
            d  = fa.d_mhb2000(self.t)
            om = fa.om_iers2003(self.t)
            for x in reversed(self.dat_ls):
                arg = (x[0] * l + x[1] * lp + x[2] * f \
                     + x[3] * d + x[4] * om) % cst.PI2
                sarg, carg = math.sin(arg), math.cos(arg)
                dp += (x[5] + x[6] * self.t) * sarg + x[ 7] * carg
                de += (x[8] + x[9] * self.t) * carg + x[10] * sarg
            return [dp * cst.U2R, de * cst.U2R]
        except Exception as e:
            raise

    def __calc_planetary(self):
        """ 惑星章動(planetary nutation)

        :return list: [delta Psi, delta Eps]
        """
        dp, de = 0.0, 0.0
        try:
            l  = fa.l_mhb2000(self.t)
            f  = fa.f_mhb2000(self.t)
            d  = fa.d_mhb2000_2(self.t)
            om = fa.om_mhb2000(self.t)
            pa = fa.pa_iers2003(self.t)
            me = fa.me_iers2003(self.t)
            ve = fa.ve_iers2003(self.t)
            ea = fa.ea_iers2003(self.t)
            ma = fa.ma_iers2003(self.t)
            ju = fa.ju_iers2003(self.t)
            sa = fa.sa_iers2003(self.t)
            ur = fa.ur_iers2003(self.t)
            ne = fa.ne_mhb2000(self.t)
            for x in reversed(self.dat_pl):
                arg = (x[ 0] * l  + x[ 2] * f  + x[ 3] * d  + x[ 4] * om \
                     + x[ 5] * me + x[ 6] * ve + x[ 7] * ea + x[ 8] * ma \
                     + x[ 9] * ju + x[10] * sa + x[11] * ur + x[12] * ne \
                     + x[13] * pa) % cst.PI2
                sarg, carg = math.sin(arg), math.cos(arg)
                dp += x[14] * sarg + x[15] * carg
                de += x[16] * sarg + x[17] * carg
            return [dp * cst.U2R, de * cst.U2R]
        except Exception as e:
            raise

