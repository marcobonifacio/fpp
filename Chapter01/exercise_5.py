"""
Optimize the functional code
"""
import doctest
from math import cos, hypot, radians, sqrt, tau

def functional_distance(
    lat_1: float, lat_2: float, lon_1: float, lon_2: float, 
    R: float = 360 * 60 / tau
) -> float:
    """
    A redundant expression (page 23).

    >>> lat_1 = 32.82950
    >>> lon_1 = -79.93021
    >>> lat_2 = 32.74412
    >>> lon_2 = -79.85226
    >>> assert abs(functional_distance(lat_1, lat_2, lon_1, lon_2) - 6.4577) < 0.001
    """
    x = (R * (radians(lon_1) - radians(lon_2)) * cos(
        (radians(lat_1) + radians(lat_2)) / 2
    )) ** 2
    y = (R * (radians(lat_1) - radians(lat_2))) ** 2
    return sqrt(x + y)

def optimized_functional_distance(
    lat_1: float, lat_2: float, lon_1: float, lon_2: float, 
    R: float = 360 * 60 / tau
) -> float:
    """
    Also more functional implementation of Algorithm 2 (page 19).

    >>> lat_1 = 32.82950
    >>> lon_1 = -79.93021
    >>> lat_2 = 32.74412
    >>> lon_2 = -79.85226
    >>> assert abs(optimized_functional_distance(lat_1, lat_2, lon_1, lon_2) - 6.4577) < 0.001
    """
    dlat = radians(lat_1) - radians(lat_2)
    dlon = radians(lon_1) - radians(lon_2)
    return hypot(R * dlon * cos( radians(lat_2) + dlat / 2), R * dlat)

if __name__ == '__main__':
    doctest.testmod()