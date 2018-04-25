"""
Constant values
"""
import os


DIR_LIB = os.path.dirname(os.path.abspath(__file__))
DAT_LS  = DIR_LIB + "/nut_ls.txt"
DAT_PL  = DIR_LIB + "/nut_pl.txt"
J2000   = 2451545.0                      # Reference epoch (J2000.0), Julian Date
JC      = 36525.0                        # Days per Julian century
TT_TAI  = 32.184                         # TT - TAI
DAYSEC  = 86400.0                        # Seconds per a day
AS2R    = 4.848136811095359935899141e-6  # Arcseconds to radians
PI      = 3.141592653589793238462643     # PI
PI2     = 6.283185307179586476925287     # 2 * PI
PI_180  = 0.017453292519943295           # PI / 180
TURNAS  = 1296000.0                      # Arcseconds in a full circle
U2R     = AS2R / 1.0e7                   # Units of 0.1 microarcsecond to radians
R2D     = 57.29577951308232087679815     # Radians to degrees
D2S     = 3600.0                         # Degrees to seconds

