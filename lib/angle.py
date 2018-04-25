"""
Module for angles
"""
from lib import const as cst


def norm_angle(angle):
    """ Normalize angle into the range 0 <= a < 2pi.

    :param  float angle: Before normalized
    :return float angle: Normalized angle
    """
    try:
        while angle < 0:
            angle += cst.PI2
        while angle > cst.PI2:
            angle -= cst.PI2
        return angle
    except Exception as e:
        raise

