"""
Class for
  ERA(Earth rotation angle (IAU 2000 model), 地球回転角),
  EORS(Equation of the origins, 原点差)
  GMST(Greenwich mean sidereal time, グリニッジ平均恒星時)
  GAST(Greenwich apparent sidereal time, グリニッジ視恒星時)
  EE(Equation of Equinoxes, 分点均差)
"""
import math
import numpy as np
from lib import angle as ang
from lib import const as cst


class Greenwich:
    def __init__(self, jd):
        """ Initialization

        :param float jd: Julian Day
        """
        self.jd, self.t = jd, jd - cst.J2000

    def era_00(self):
        """ Earth rotation angle (IAU 2000 model).

        :return float: ERA(Earth rotation angle (Unit: rad, Range: 0-2pi), 地球回転角)
        """
        try:
            # Fractional part of T (days).
            f = self.jd % 1
            # Earth rotation angle at this UT1.
            return ang.norm_angle(
                (f + 0.7790572732640 + 0.00273781191135448 * self.t) * cst.PI2
            )
        except Exception as e:
            raise

    def eors(self, r_mtx, s):
        """ Equation of the origins, given the classical NPB matrix and the
            quantity s.

        :param  np.matrix r: Rotation matrix
        :param  float     s: CIO locator
        :return float    EO: Equation of the origin (Unit: rad), 原点差
        """
        try:
            x = r_mtx[2, 0]
            ax = x / (1 + r_mtx[2, 2])
            xs = 1 - ax * x
            ys = -ax * r_mtx[2, 1]
            zs = -x
            p = r_mtx[0, 0] * xs + r_mtx[0, 1] * ys + r_mtx[0, 2] * zs
            q = r_mtx[1, 0] * xs + r_mtx[1, 1] * ys + r_mtx[1, 2] * zs
            return s - math.atan2(q, p) if p != 0 or q != 0 else s
        except Exception as e:
            raise

    def gast(self, era, eo):
        """ Greenwich apparent sidereal time

        :param  float  era: Earth rotation angle
        :param  float   eo: Equation of the origin
        :return float GAST: Greenwich apparent sidereal time (Unit: rad), グリニッジ視恒星時
        """
        try:
            return ang.norm_angle(era - eo)
        except Exception as e:
            raise

    def gmst(self, gast, t):
        """ Greenwich mean sidereal time, IAU 2006.

        :param  float gast: Greenwich apparent sidereal time, グリニッジ視恒星時
        :param  float    t: Julian Century Number
        :return float GMST: Greenwich mean sidereal time (Unit: rad), グリニッジ平均恒星時
        """
        try:
            return ang.norm_angle(
                gast \
                + (   0.014506      \
                + (4612.156534      \
                + (   1.3915817     \
                + (  -0.00000044    \
                + (  -0.000029956   \
                + (  -0.0000000368) \
                * t) * t) * t) * t) * t) * cst.AS2R
            )
        except Exception as e:
            raise

    def ee(self, gast, gmst):
        """" Equation of Equinoxes

        :param  float gast: Greenwich apparent sidereal time, グリニッジ視恒星時
        :param  float gmst: Greenwich mean sidereal time, グリニッジ平均恒星時
        :return float   EE: Equation of Equinoxes (Unit: rad), 分点均差
        """
        try:
            return gast - gmst
        except Exception as e:
            raise

