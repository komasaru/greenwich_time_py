"""
Module for Fundamental arguments
"""
from lib import const as cst


def l_iers2003(t):
    """ Mean anomaly of the Moon (IERS 2003)

    :param  float t: Julian Centry
    :return float l: Unit: rad
    """
    try:
        return ((    485868.249036    \
              + (1717915923.2178      \
              + (        31.8792      \
              + (         0.051635    \
              + (        -0.00024470) \
              * t) * t) * t) * t) % cst.TURNAS) * cst.AS2R
    except Exception as e:
        raise

def p_iers2003(t):
    """ Mean anomaly of the Sun (IERS 2003)

    :param  float t: Julian Centry
    :return float p: Unit: rad
    """
    try:
        return ((   1287104.793048    \
              + ( 129596581.0481      \
              + (       - 0.5532      \
              + (         0.000136    \
              + (       - 0.00001149) \
              * t) * t) * t) * t) % cst.TURNAS) * cst.AS2R
    except Exception as e:
        raise

def f_iers2003(t):
    """ Mean longitude of the Moon minus that of the ascending node (IERS 2003)

    :param  float t: Julian Centry
    :return float f: Unit: rad
    """
    try:
        return ((    335779.526232    \
              + (1739527262.8478      \
              + (       -12.7512      \
              + (        -0.001037    \
              + (         0.00000417) \
              * t) * t) * t) * t) % cst.TURNAS) * cst.AS2R
    except Exception as e:
        raise

def d_iers2003(t):
    """ Mean elongation of the Moon from the Sun (IERS 2003)

    :param  float t: Julian Centry
    :return float d: Unit: rad
    """
    try:
        return ((   1072260.703692    \
              + (1602961601.2090      \
              + (       - 6.3706      \
              + (         0.006593    \
              + (       - 0.00003169) \
              * t) * t) * t) * t) % cst.TURNAS ) * cst.AS2R
    except Exception as e:
        raise

def om_iers2003(t):
    """ Mean longitude of the ascending node of the Moon (IERS 2003)

    :param  float  t: Julian Centry
    :return float om: Unit: rad
    """
    try:
       return ((    450160.398036    \
             + (  -6962890.5431      \
             + (         7.4722      \
             + (         0.007702    \
             + (        -0.00005939) \
             * t) * t) * t) * t) % cst.TURNAS) * cst.AS2R
    except Exception as e:
        raise

def ve_iers2003(t):
    """ Venus longitudes (IERS 2003)

    :param  float  t: Julian Centry
    :return float ve: Unit: rad
    """
    try:
        return (3.176146697 + 1021.3285546211 * t) % cst.PI2
    except Exception as e:
        raise

def ea_iers2003(t):
    """ Earth longitudes (IERS 2003)

    :param  float  t: Julian Centry
    :return float ea: Unit: rad
    """
    try:
        return (1.753470314 + 628.3075849991 * t) % cst.PI2
    except Exception as e:
        raise

def pa_iers2003(t):
    """ General accumulated precession in longitude (IERS 2003)

    :param  float  t: Julian Centry
    :return float pa: Unit: rad
    """
    try:
        return (0.024381750 + 0.00000538691 * t) * t
    except Exception as e:
        raise

def me_iers2003(t):
    """ Mercury longitudes (IERS 2003)

    :param  float  t: Julian Centry
    :return float me: Unit: rad
    """
    try:
        return (4.402608842 + 2608.7903141574 * t) % cst.PI2
    except Exception as e:
        raise

def ma_iers2003(t):
    """ Mars longitudes (IERS 2003)

    :param  float  t: Julian Centry
    :return float ma: Unit: rad
    """
    try:
        return (6.203480913 + 334.0612426700 * t) % cst.PI2
    except Exception as e:
        raise

def ju_iers2003(t):
    """ Jupiter longitudes (IERS 2003)

    :param  float  t: Julian Centry
    :return float ju: Unit: rad
    """
    try:
        return (0.599546497 + 52.9690962641 * t) % cst.PI2
    except Exception as e:
        raise

def sa_iers2003(t):
    """ Saturn longitudes (IERS 2003)

    :param  float  t: Julian Centry
    :return float sa: Unit: rad
    """
    try:
        return (0.874016757 + 21.3299104960 * t) % cst.PI2
    except Exception as e:
        raise

def ur_iers2003(t):
    """ Uranus longitudes (IERS 2003)

    :param  float  t: Julian Centry
    :return float ur: Unit: rad
    """
    try:
        return (5.481293872 + 7.4781598567 * t) % cst.PI2
    except Exception as e:
        raise

def lp_mhb2000(t):
    """ Mean anomaly of the Sun (MHB2000)

    :param  float  t: Julian Centry
    :return float lp: Unit: rad
    """
    try:
        return ((  1287104.79305     \
              + (129596581.0481      \
              + (       -0.5532      \
              + (        0.000136    \
              + (       -0.00001149) \
              * t) * t) * t) * t) % cst.TURNAS) * cst.AS2R
    except Exception as e:
        raise

def d_mhb2000(t):
    """ Mean elongation of the Moon from the Sun (MHB2000)

    :param  float t: Julian Centry
    :return float d: Unit: rad
    """
    try:
        return ((   1072260.70369     \
              + (1602961601.2090      \
              + (        -6.3706      \
              + (         0.006593    \
              + (        -0.00003169) \
              * t) * t) * t) * t) % cst.TURNAS) * cst.AS2R
    except Exception as e:
        raise

def l_mhb2000(t):
    """ Mean anomaly of the Moon (MHB2000)

    :param  float t: Julian Centry
    :return float l: Unit: rad
    """
    try:
        return (2.35555598 + 8328.6914269554 * t) % cst.PI2
    except Exception as e:
        raise

def f_mhb2000(t):
    """ Mean longitude of the Moon minus that of the ascending node (MHB2000)

    :param  float t: Julian Centry
    :return float f: Unit: rad
    """
    try:
        return (1.627905234 + 8433.466158131 * t) % cst.PI2
    except Exception as e:
        raise

def d_mhb2000_2(t):
    """ Mean elongation of the Moon from the Sun (MHB2000)

    :param  float t: Julian Centry
    :return float d: Unit: rad
    """
    try:
        return (5.198466741 + 7771.3771468121 * t) % cst.PI2
    except Exception as e:
        raise

def om_mhb2000(t):
    """ Mean longitude of the ascending node of the Moon (MHB2000)

    :param  float  t:Julian Centry
    :return float om: Unit: rad
    """
    try:
        return (2.18243920 - 33.757045 * t) % cst.PI2
    except Exception as e:
        raise

def ne_mhb2000(t):
    """ Neptune longitude (MHB2000)

    :param  float  t: Julian Centry
    :return float ne: Unit: rad
    """
    try:
        return (5.321159000 + 3.8127774000 * t) % cst.PI2
    except Exception as e:
        raise

