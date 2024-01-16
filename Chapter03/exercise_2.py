"""
Alternative Mersenne class definition
"""
import doctest
from typing import Callable

class Mersenne1:

    def __init__(self, algorithm: Callable[[int], int]) -> None:
        self.pow2 = algorithm

    def __call__(self, arg: int) -> int:
        return self.pow2(arg) - 1

def shifty(b: int) -> int:
    return 1 << b

class Mersenne2:
    pow2: Callable[[int], int]

    def __call__(self, arg: int) -> int:
        return self.pow2(arg) - 1    

class ShiftyMersenne(Mersenne2):
    """
    >>> m2s = ShiftyMersenne()
    >>> m2s(17)
    131071
    """
    pow2 = staticmethod(shifty)


if __name__ == '__main__':
    doctest.testmod()