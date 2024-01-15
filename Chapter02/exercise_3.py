"""
Optimize a recursion
"""
import doctest
import math
import timeit

def isprimer(n: int) -> bool:
    """
    Test if a number is prime

    >>> isprimer(151)
    True
    >>> round(timeit.timeit(lambda: isprimer(151)), 0)
    2.0
    >>> isprimer(152)
    False
    """
    def iscoprime(k: int, a: int, b: int) -> bool:
        """ Is k coprime with a value in the given range? """
        if a == b: return True
        return (k % a != 0) and iscoprime(k, a + 1, b)
    return iscoprime(n, 2, int(math.sqrt(n)) + 1)

def isprimer_(n: int) -> bool:
    """
    Test if a number is prime

    >>> isprimer_(151)
    True
    >>> round(timeit.timeit(lambda: isprimer_(151)) / 10, 0) * 10
    30.0
    >>> isprimer_(152)
    False
    """
    def iscoprime(k: int, a: int, b: int) -> bool:
        """ Is k coprime with a value in the given range? """
        if a == b: return True
        return (k % b != 0) and iscoprime(k, a, b - 1)
    return iscoprime(n, int(math.sqrt(n)) + 1, n - 1)

if __name__ == '__main__':
    doctest.testmod()