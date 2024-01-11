"""
Convert step-wise computation to functional code
"""
import doctest
from math import cos, hypot, radians, sqrt, tau
from typing import Tuple

def imperative_computation(
    lat_1: float, lat_2: float, lon_1: float, lon_2: float, 
    R: float = 360 * 60 / tau
) -> float:
    """
    Imperative implementation of Algorithm 2 (page 19).

    >>> lat_1 = 32.82950
    >>> lon_1 = -79.93021
    >>> lat_2 = 32.74412
    >>> lon_2 = -79.85226
    >>> assert abs(imperative_computation(lat_1, lat_2, lon_1, lon_2) - 6.4577) < 0.001
    """
    rlat_1 = radians(lat_1)
    rlat_2 = radians(lat_2)
    dlat = rlat_1 - rlat_2
    rlon_1 = radians(lon_1)
    rlon_2 = radians(lon_2)
    dlon = rlon_1 - rlon_2
    lat_m = rlat_1 + rlat_2
    lat_m = lat_m / 2
    c = cos(lat_m)
    x = R * dlon
    x = x * c
    y = R * dlat
    x_2 = x ** 2
    y_2 = y ** 2
    xy_2 = x_2 + y_2
    return sqrt(xy_2)

def functional_distance(
    lat_1: float, lat_2: float, lon_1: float, lon_2: float, 
    R: float = 360 * 60 / tau
) -> float:
    """
    More functional implementation of Algorithm 2 (page 19).

    >>> lat_1 = 32.82950
    >>> lon_1 = -79.93021
    >>> lat_2 = 32.74412
    >>> lon_2 = -79.85226
    >>> assert abs(functional_distance(lat_1, lat_2, lon_1, lon_2) - 6.4577) < 0.001
    """
    lat_m = (radians(lat_1) + radians(lat_2)) / 2
    x = R * (radians(lon_1) - radians(lon_2)) * cos(lat_m)
    y = R * (radians(lat_1) - radians(lat_2))
    return sqrt(x ** 2 + y ** 2)

def redundant_implementation(
    lat_1: float, lat_2: float, lon_1: float, lon_2: float, 
    R: float = 360 * 60 / tau
) -> float:
    """
    Also more functional implementation of Algorithm 2 (page 19).

    >>> lat_1 = 32.82950
    >>> lon_1 = -79.93021
    >>> lat_2 = 32.74412
    >>> lon_2 = -79.85226
    >>> assert abs(redundant_implementation(lat_1, lat_2, lon_1, lon_2) - 6.4577) < 0.001
    """
    return hypot(
        R * (radians(lon_1) - radians(lon_2)) * cos(
            (radians(lat_1) + radians(lat_2)) / 2
        ),
        R * (radians(lat_1) - radians(lat_2))
    )

if __name__ == '__main__':
    doctest.testmod()