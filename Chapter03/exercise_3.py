"""
Alternative algorithm implementations
"""
import doctest
from typing import Tuple

def for_implementation(V: Tuple[float]) -> float:
    """
    Implementation with for cycle that updates stateful variables.

    >>> V = (7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73)
    >>> assert abs(for_implementation(V)) < 0.001
    """
    s = 0
    for v in V:
        s += (v - 7.5) / 2.031
    return s / len(V)

def genex_implementation(V: Tuple[float]) -> float:
    """
    Implementation with generator expression.

    >>> V = (7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73)
    >>> assert abs(genex_implementation(V)) < 0.001
    """
    return sum((v - 7.5) / 2.031 for v in V) / len(V)

def map_implementation(V: Tuple[float]) -> float:
    """
    Implementation with map() operation.

    >>> V = (7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73)
    >>> assert abs(map_implementation(V)) < 0.001
    """
    return sum(map(lambda v: (v - 7.5) / 2.031, V)) / len(V)

if __name__ == '__main__':
    doctest.testmod()