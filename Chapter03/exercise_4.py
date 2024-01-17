"""
Raw data cleanup
"""
import csv
import doctest
from pathlib import Path
from typing import Generator, Tuple

def lbyl(file: Path) -> Generator[Tuple[float, ...] | str, None, None]:
    """
    >>> reader = lbyl(Path('../Anscombe.txt'))
    >>> next(reader)
    'Row discarded'
    >>> next(reader)
    'Row discarded'
    >>> next(reader)
    'Row discarded'
    >>> next(reader)
    (10.0, 8.04, 10.0, 9.14, 10.0, 7.46, 8.0, 6.58)
    """
    with file.open('r', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if all(str(r).replace('.', '').isnumeric() for r in row):
                yield tuple(float(r) for r in row)
            else:
                yield 'Row discarded'

def eafp(file: Path) -> Generator[Tuple[float, ...] | str, None, None]:
    """
    >>> reader = eafp(Path('../Anscombe.txt'))
    >>> next(reader)
    'Row discarded'
    >>> next(reader)
    'Row discarded'
    >>> next(reader)
    'Row discarded'
    >>> next(reader)
    (10.0, 8.04, 10.0, 9.14, 10.0, 7.46, 8.0, 6.58)
    """
    with file.open('r', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            try:
                yield tuple(float(r) for r in row)
            except ValueError:
                yield 'Row discarded'


if __name__ == '__main__':
    doctest.testmod()