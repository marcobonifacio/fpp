"""
Function vs. lambda design question
"""
import doctest

def model(o: float) -> float:
    """
    Proper def function.

    >>> model(800)
    630.0
    >>> model(900)
    720.0
    """
    return 0.9 * o - 90

def lambda_model() -> None:
    """
    Lambda object.

    >>> m = lambda o: 0.9 * o - 90
    >>> m(800)
    630.0
    >>> m(900)
    720.0
    """
    pass

class Model:
    """
    Class definition with __call__() method.

    >>> Model()(800)
    630.0
    >>> Model()(900)
    720.0
    """

    def __call__(self, o: float) -> float:
        return 0.9 * o - 90

if __name__ == '__main__':
    doctest.testmod()