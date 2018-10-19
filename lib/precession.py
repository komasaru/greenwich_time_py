"""
Class for Precessions
"""
from lib import const as cst


class Precession:
    def __init__(self, t):
        """ Initialization

        :param float t: Julian Century
        """
        self.t = t

    def calc_pfw_06(self):
        """ Precession angles, IAU 2006 (Fukushima-Williams 4-angle formulation)

        :return list: [gam_b, phi_b, psi_b]
        """
        try:
            gam_b = (   -0.052928      \
                  + (   10.556378      \
                  + (    0.4932044     \
                  + (   -0.00031238    \
                  + (   -0.000002788   \
                  + (    0.0000000260) \
                  * self.t) * self.t) * self.t) * self.t) * self.t) * cst.AS2R
            phi_b = (84381.412819      \
                  + (  -46.811016      \
                  + (    0.0511268     \
                  + (    0.00053289    \
                  + (   -0.000000440   \
                  + (   -0.0000000176) \
                  * self.t) * self.t) * self.t) * self.t) * self.t) * cst.AS2R
            psi_b = (   -0.041775      \
                  + ( 5038.481484      \
                  + (    1.5584175     \
                  + (   -0.00018522    \
                  + (   -0.000026452   \
                  + (   -0.0000000148) \
                  * self.t) * self.t) * self.t) * self.t) * self.t) * cst.AS2R
            return [gam_b, phi_b, psi_b]
        except Exception as e:
            raise

    def calc_obl_06(self):
        """ Mean obliquity of the ecliptic, IAU 2006 precession model.

        :return Eps_A: Mean obliquity of the ecliptic
        """
        try:
            return (84381.406       \
                 + (  -46.836769    \
                 + (   -0.0001831   \
                 + (    0.00200340  \
                 + (   -0.000000576 \
                 + (   -0.0000000434) \
                 * self.t) * self.t) * self.t) * self.t) * self.t) * cst.AS2R
        except Exception as e:
            raise

