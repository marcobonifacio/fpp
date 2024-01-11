"""
Convert an imperative algorithm to functional code
"""
import doctest
from typing import Tuple

def imperative_mean(V: Tuple[float]) -> float:
    """
    Imperative implementation of Algorithm 1 (page 18).

    >>> V = (7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73)
    >>> assert abs(imperative_mean(V) - 7.5) < 0.001
    """
    s = 0
    for v in V:
        s += v
    return s / len(V)

def functional_mean(V: Tuple[float]) -> float:
    """
    Functional implementation of Algorithm 1 (page 18).

    >>> V = (7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73)
    >>> assert abs(functional_mean(V) - 7.5) < 0.001
    """
    return sum(v for v in V) / len(V)

if __name__ == '__main__':
    doctest.testmod()