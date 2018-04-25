"""
Module for matrixes
"""
import numpy as np


def init_r():
    """ Initialize an r-matrix to the identity matrix.

    :return np.matrix: Unit matrix
    """
    try:
        return np.eye(3, dtype="float64")
    except Exception as e:
        raise

def rotate_x(r_src, phi):
    """ Rotate an r-matrix about the x-axis.

        (  1        0            0      )
        (                               )
        (  0   + cos(phi)   + sin(phi)  )
        (                               )
        (  0   - sin(phi)   + cos(phi)  )

    :param  np.matrix r_src: Rotation matrix
    :param  float       phi: Angle (Unit: rad)
    :return np.matrix r_dst: Rotated matrix
    """
    try:
        s = np.sin(phi)
        c = np.cos(phi)
        r_mx = np.matrix([
            [1,  0, 0],
            [0,  c, s],
            [0, -s, c]
        ], dtype="float64")
        return r_mx * r_src
    except Exception as e:
        raise

def rotate_y(r_src, theta):
    """ Rotate an r-matrix about the y-axis.

        (  + cos(theta)     0      - sin(theta)  )
        (                                        )
        (       0           1           0        )
        (                                        )
        (  + sin(theta)     0      + cos(theta)  )

    :param  np.matrix r_src: Rotation matrix
    :param  float     theta: Angle (Unit: rad)
    :return np.matrix r_dst: Rotated matrix
    """
    try:
        s = np.sin(theta)
        c = np.cos(theta)
        r_mx = np.matrix([
            [c, 0, -s],
            [0, 1,  0],
            [s, 0,  c]
        ], dtype="float64")
        return r_mx * r_src
    except Exception as e:
        raise

def rotate_z(r_src, psi):
    """ Rotate an r-matrix about the z-axis.

        (  + cos(psi)   + sin(psi)     0  )
        (                                 )
        (  - sin(psi)   + cos(psi)     0  )
        (                                 )
        (       0            0         1  )

    :param  np.matrix r_src: Rotation matrix
    :param  float       psi: Angle (Unit: rad)
    :return np.matrix r_dst: Rotated matrix
    """
    try:
        s = np.sin(psi)
        c = np.cos(psi)
        r_mx = np.matrix([
            [ c, s, 0],
            [-s, c, 0],
            [ 0, 0, 1]
        ], dtype="float64")
        return r_mx * r_src
    except Exception as e:
        raise

