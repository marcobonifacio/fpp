"""
Revise the sqrt() function
"""
import doctest
from typing import Iterator, Callable

def next_(n: float, x: float) -> float:
    """
    Compute a series of values converging to sqrt(n).

    >>> round(next_(2, 1), 4)
    1.5
    >>> round(next_(2, 1.5), 4)
    1.4167
    >>> round(next_(2, 1.4167), 4)
    1.4142
    """
    return (x + n / x) / 2

def repeat(f: Callable[[float], float], a: float) -> Iterator[float]:
    """
    Repeat a potentially infinite sequence of values from a function.

    >>> f = lambda x: next_(2, x)
    >>> i = repeat(f, 2)
    >>> round(next(i), 4)
    2
    >>> round(next(i), 4)
    1.5
    >>> round(next(i), 4)
    1.4167
    """
    yield a
    yield from repeat(f, f(a))

def within(eps: float, iterable: Iterator[float]) -> float:
    """
    Stop iteration at a convergence less than an epsilon.

    >>> f = lambda x: next_(2, x)
    >>> i = repeat(f, 2)
    >>> within(0.0001, i)
    1.4142135623746899
    """
    def head_tail(eps: float, a: float, iterable: Iterator[float]) -> float:
        b = next(iterable)
        if abs(a - b) <= eps:
            return b
        return head_tail(eps, b, iterable)
    return head_tail(eps, next(iterable), iterable)

def sqrt(n: float) -> float:
    """
    Compute the square root of a number

    >>> sqrt(2)
    1.4142135623746899
    """
    return within(eps=0.0001, iterable=repeat(lambda x: next_(n, x), 1))

def sqrt_rev(approx: float, eps: float, n: float) -> float:
    """
    Compute the square root of a number to a given approximation and a given
    convergence.

    >>> sqrt_rev(1, 0.000_01, 3)
    1.7320508075688772
    """
    return within(eps=eps, iterable=repeat(lambda x: next_(n, x), approx))

if __name__ == '__main__':
    doctest.testmod()