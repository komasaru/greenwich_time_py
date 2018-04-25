"""
Class for Rotation given the Fukushima-Williams angles
"""
from lib import matrix as mx
import sys


class RotationFw:
    """ Form rotation matrix given the Fukushima-Williams angles.

    :param   float gam_b
    :param   float phi_b
    :param   float psi
    :param   float eps
    :return  float r:  Rotation matrix
    """
    def fw2m(self, gam_b, phi_b, psi, eps):
        try:
            r = mx.init_r()
            r = mx.rotate_z(r, gam_b)
            r = mx.rotate_x(r, phi_b)
            r = mx.rotate_z(r, -1 * psi)
            r = mx.rotate_x(r, -1 * eps)
            return r
        except Exception as e:
            raise

