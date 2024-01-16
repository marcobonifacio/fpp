"""
Rewrite the some_function() function
"""
import doctest

global_adjustment: float = 17

def some_function(a: float, b: float, t: float) -> float:
    """
    A not pure function.

    >>> some_function(2, 3, 5)
    34
    """
    return a + b * t + global_adjustment

def main() -> None:
    """
    Convert in a pure function implementation.

    >>> main()
    some_function(2, 3, 5) = 30
    some_function(2, 3, 5) = 34
    """
    global global_adjustment
    global_adjustment = 13
    print(f'{some_function(2, 3, 5) = }')
    global_adjustment = 17
    print(f'{some_function(2, 3, 5) = }')

def some_function_rev(
        a: float, b: float, t: float, global_adjustment: float
    ) -> float:
    """
    A not pure function.

    >>> some_function_rev(2, 3, 5, 13)
    30
    >>> some_function_rev(2, 3, 5, 17)
    34
    """
    return a + b * t + global_adjustment

def main_rev() -> None:
    """
    Convert in a pure function implementation.

    >>> main_rev()
    some_function_rev(2, 3, 5, 13) = 30
    some_function_rev(2, 3, 5, 17) = 34
    """
    print(f'{some_function_rev(2, 3, 5, 13) = }')
    print(f'{some_function_rev(2, 3, 5, 17) = }')


if __name__ == '__main__':
    doctest.testmod()