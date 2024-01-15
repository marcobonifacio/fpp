"""
Apply map() to a sequence of values
"""
import doctest
from typing import Tuple

def model(o: float) -> float:
    """
    Model from observed to actual values.

    >>> model(800)
    630.0
    >>> model(900)
    720.0
    """
    return 0.9 * o - 90

def table(observed_values: Tuple[float]) -> None:
    """
    Print out a table of observed vs actual values.

    >>> table((800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500))
    Observed    Actual
         800       630
         900       720
        1000       810
        1100       900
        1200       990
        1300      1080
        1400      1170
        1500      1260
        1600      1350
        1700      1440
        1800      1530
        1900      1620
        2000      1710
        2100      1800
        2200      1890
        2300      1980
        2400      2070
        2500      2160
    """
    actual_values = map(model, observed_values)
    print('Observed    Actual')
    for o, a in zip(observed_values, actual_values):
        print(f'{o:>8}    {a:>6.0f}')

if __name__ == '__main__':
    doctest.testmod()