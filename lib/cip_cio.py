"""
Class for
  CIP(Celestial Intermediate Pole, 瞬時の極軸),
  CIO(Celestial Intermediate Origin, 非回転原点)
"""
import math
from lib import const as cst
from lib import fundamental_argument as fa


class CipCio:
    # Polynomial coefficients
    SP = [94.00e-6, 3808.65e-6, -122.68e-6, -72574.11e-6, 27.98e-6, 15.62e-6]
    # Terms of order t^0
    S_0 = [
        [[0,  0,  0,  0,  1,  0,  0,  0], -2640.73e-6,  0.39e-6],
        [[0,  0,  0,  0,  2,  0,  0,  0],   -63.53e-6,  0.02e-6],
        [[0,  0,  2, -2,  3,  0,  0,  0],   -11.75e-6, -0.01e-6],
        [[0,  0,  2, -2,  1,  0,  0,  0],   -11.21e-6, -0.01e-6],
        [[0,  0,  2, -2,  2,  0,  0,  0],     4.57e-6,  0.00e-6],
        [[0,  0,  2,  0,  3,  0,  0,  0],    -2.02e-6,  0.00e-6],
        [[0,  0,  2,  0,  1,  0,  0,  0],    -1.98e-6,  0.00e-6],
        [[0,  0,  0,  0,  3,  0,  0,  0],     1.72e-6,  0.00e-6],
        [[0,  1,  0,  0,  1,  0,  0,  0],     1.41e-6,  0.01e-6],
        [[0,  1,  0,  0, -1,  0,  0,  0],     1.26e-6,  0.01e-6],
        [[1,  0,  0,  0, -1,  0,  0,  0],     0.63e-6,  0.00e-6],
        [[1,  0,  0,  0,  1,  0,  0,  0],     0.63e-6,  0.00e-6],
        [[0,  1,  2, -2,  3,  0,  0,  0],    -0.46e-6,  0.00e-6],
        [[0,  1,  2, -2,  1,  0,  0,  0],    -0.45e-6,  0.00e-6],
        [[0,  0,  4, -4,  4,  0,  0,  0],    -0.36e-6,  0.00e-6],
        [[0,  0,  1, -1,  1, -8, 12,  0],     0.24e-6,  0.12e-6],
        [[0,  0,  2,  0,  0,  0,  0,  0],    -0.32e-6,  0.00e-6],
        [[0,  0,  2,  0,  2,  0,  0,  0],    -0.28e-6,  0.00e-6],
        [[1,  0,  2,  0,  3,  0,  0,  0],    -0.27e-6,  0.00e-6],
        [[1,  0,  2,  0,  1,  0,  0,  0],    -0.26e-6,  0.00e-6],
        [[0,  0,  2, -2,  0,  0,  0,  0],     0.21e-6,  0.00e-6],
        [[0,  1, -2,  2, -3,  0,  0,  0],    -0.19e-6,  0.00e-6],
        [[0,  1, -2,  2, -1,  0,  0,  0],    -0.18e-6,  0.00e-6],
        [[0,  0,  0,  0,  0,  8,-13, -1],     0.10e-6, -0.05e-6],
        [[0,  0,  0,  2,  0,  0,  0,  0],    -0.15e-6,  0.00e-6],
        [[2,  0, -2,  0, -1,  0,  0,  0],     0.14e-6,  0.00e-6],
        [[0,  1,  2, -2,  2,  0,  0,  0],     0.14e-6,  0.00e-6],
        [[1,  0,  0, -2,  1,  0,  0,  0],    -0.14e-6,  0.00e-6],
        [[1,  0,  0, -2, -1,  0,  0,  0],    -0.14e-6,  0.00e-6],
        [[0,  0,  4, -2,  4,  0,  0,  0],    -0.13e-6,  0.00e-6],
        [[0,  0,  2, -2,  4,  0,  0,  0],     0.11e-6,  0.00e-6],
        [[1,  0, -2,  0, -3,  0,  0,  0],    -0.11e-6,  0.00e-6],
        [[1,  0, -2,  0, -1,  0,  0,  0],    -0.11e-6,  0.00e-6]
    ]
    # Terms of order t^1
    S_1 = [
        [[0,  0,  0,  0,  2,  0,  0,  0], -0.07e-6,  3.57e-6],
        [[0,  0,  0,  0,  1,  0,  0,  0],  1.73e-6, -0.03e-6],
        [[0,  0,  2, -2,  3,  0,  0,  0],  0.00e-6,  0.48e-6]
    ]
    # Terms of order t^2
    S_2 = [
        [[0,  0,  0,  0,  1,  0,  0,  0], 743.52e-6, -0.17e-6],
        [[0,  0,  2, -2,  2,  0,  0,  0],  56.91e-6,  0.06e-6],
        [[0,  0,  2,  0,  2,  0,  0,  0],   9.84e-6, -0.01e-6],
        [[0,  0,  0,  0,  2,  0,  0,  0],  -8.85e-6,  0.01e-6],
        [[0,  1,  0,  0,  0,  0,  0,  0],  -6.38e-6, -0.05e-6],
        [[1,  0,  0,  0,  0,  0,  0,  0],  -3.07e-6,  0.00e-6],
        [[0,  1,  2, -2,  2,  0,  0,  0],   2.23e-6,  0.00e-6],
        [[0,  0,  2,  0,  1,  0,  0,  0],   1.67e-6,  0.00e-6],
        [[1,  0,  2,  0,  2,  0,  0,  0],   1.30e-6,  0.00e-6],
        [[0,  1, -2,  2, -2,  0,  0,  0],   0.93e-6,  0.00e-6],
        [[1,  0,  0, -2,  0,  0,  0,  0],   0.68e-6,  0.00e-6],
        [[0,  0,  2, -2,  1,  0,  0,  0],  -0.55e-6,  0.00e-6],
        [[1,  0, -2,  0, -2,  0,  0,  0],   0.53e-6,  0.00e-6],
        [[0,  0,  0,  2,  0,  0,  0,  0],  -0.27e-6,  0.00e-6],
        [[1,  0,  0,  0,  1,  0,  0,  0],  -0.27e-6,  0.00e-6],
        [[1,  0, -2, -2, -2,  0,  0,  0],  -0.26e-6,  0.00e-6],
        [[1,  0,  0,  0, -1,  0,  0,  0],  -0.25e-6,  0.00e-6],
        [[1,  0,  2,  0,  1,  0,  0,  0],   0.22e-6,  0.00e-6],
        [[2,  0,  0, -2,  0,  0,  0,  0],  -0.21e-6,  0.00e-6],
        [[2,  0, -2,  0, -1,  0,  0,  0],   0.20e-6,  0.00e-6],
        [[0,  0,  2,  2,  2,  0,  0,  0],   0.17e-6,  0.00e-6],
        [[2,  0,  2,  0,  2,  0,  0,  0],   0.13e-6,  0.00e-6],
        [[2,  0,  0,  0,  0,  0,  0,  0],  -0.13e-6,  0.00e-6],
        [[1,  0,  2, -2,  2,  0,  0,  0],  -0.12e-6,  0.00e-6],
        [[0,  0,  2,  0,  0,  0,  0,  0],  -0.11e-6,  0.00e-6]
    ]
    # Terms of order t^3
    S_3 = [
        [[0,  0,  0,  0,  1,  0,  0,  0],  0.30e-6, -23.42e-6],
        [[0,  0,  2, -2,  2,  0,  0,  0], -0.03e-6,  -1.46e-6],
        [[0,  0,  2,  0,  2,  0,  0,  0], -0.01e-6,  -0.25e-6],
        [[0,  0,  0,  0,  2,  0,  0,  0],  0.00e-6,   0.23e-6]
    ]
    # Terms of order t^4
    S_4 = [
        [[0,  0,  0,  0,  1,  0,  0,  0], -0.26e-6, -0.01e-6]
    ]

    def __init__(self, t):
        """ Initialization

        :param float t: Julian Century Number
        """
        self.t = t

    def bpn2xy(self, r):
        """ Extract from the bias-precession-nutation matrix the X,Y
            coordinates of the Celestial Intermediate Pole.

        :param  np.matrix r: Rotation Matrix
        :return list       : [x, y]  (x, y cordinates of CIP)
        """
        try:
            return [r[2, 0], r[2, 1]]
        except Exception as e:
            raise

    def s_06(self, x, y):
        """ The CIO locator s, positioning the Celestial Intermediate Origin on
            the equator of the Celestial Intermediate Pole, given the CIP's X,Y
            coordinates.  Compatible with IAU 2006/2000A precession-nutation.

        :param  float x: x coordinate of CIP
        :param  float y: y coordinate of CIP
        :return float s: CIO locator (Unit: rad)
        """
        try:
            # Fundamental Arguments (from IERS Conventions 2003)
            fas = [
                # Mean anomaly of the Moon.(Ref: iauFal03(t))
                fa.l_iers2003(self.t),
                # Mean anomaly of the Sun.(Ref: iauFalp03(t))
                fa.p_iers2003(self.t),
                # Mean longitude of the Moon minus that of the ascending node.(Ref: iauFaf03(t))
                fa.f_iers2003(self.t),
                # Mean elongation of the Moon from the Sun.(Ref: iauFad03(t))
                fa.d_iers2003(self.t),
                # Mean longitude of the ascending node of the Moon.(Ref: iauFaom03(t))
                fa.om_iers2003(self.t),
                # Mean longitude of Venus.(Ref: iauFave03(t))
                fa.ve_iers2003(self.t),
                # Mean longitude of Earth.(Ref: iauFae03(t))
                fa.ea_iers2003(self.t),
                # General precession in longitude.(Ref: iauFapa03(t))
                fa.pa_iers2003(self.t)
            ]
            # Evaluate s.
            w_0, w_1, w_2, w_3, w_4, w_5 = self.SP
            for i in list(reversed(range(len(self.S_0)))):
                a = 0.0
                for j in range(8):
                    a += self.S_0[i][0][j] * fas[j]
                w_0 += self.S_0[i][1] * math.sin(a) \
                     + self.S_0[i][2] * math.cos(a)
            for i in list(reversed(range(len(self.S_1)))):
                a = 0.0
                for j in range(8):
                    a += self.S_1[i][0][j] * fas[j]
                w_1 += self.S_1[i][1] * math.sin(a) \
                     + self.S_1[i][2] * math.cos(a)
            for i in list(reversed(range(len(self.S_2)))):
                a = 0.0
                for j in range(8):
                    a += self.S_2[i][0][j] * fas[j]
                w_2 += self.S_2[i][1] * math.sin(a) \
                     + self.S_2[i][2] * math.cos(a)
            for i in list(reversed(range(len(self.S_3)))):
                a = 0.0
                for j in range(8):
                    a += self.S_3[i][0][j] * fas[j]
                w_3 += self.S_3[i][1] * math.sin(a) \
                     + self.S_3[i][2] * math.cos(a)
            for i in list(reversed(range(len(self.S_4)))):
                a = 0.0
                for j in range(8):
                    a += self.S_4[i][0][j] * fas[j]
                w_4 += self.S_4[i][1] * math.sin(a) \
                     + self.S_4[i][2] * math.cos(a)
            return (w_0 + (w_1 + (w_2 + (w_3 + (w_4  +  w_5 \
                 * self.t) * self.t) * self.t) * self.t) * self.t) * cst.AS2R \
                 - x * y / 2
        except Exception as e:
            raise

