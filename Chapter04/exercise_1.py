"""
Palindromic numbers
"""
import doctest
from typing import Iterator

def digits(x: int, base: int) -> Iterator[int]:
	"""
	Extract digits from a number, from the least significant.

	>>> d = digits(456, 10)
	>>> next(d)
	6
	>>> next(d)
	5
	>>> next(d)
	4
	"""
	if x == 0: return
	yield x % base
	yield from digits(x // base, base)

def check_palindrome1(digits: Iterator[int]) -> bool:
	"""
	First palindrome check algorithm.

	>>> check_palindrome1(digits(87654, 10))
	False
	>>> check_palindrome1(digits(12344321, 10))
	True
	"""
	sequence = tuple(digits)
	return all(sequence[n] == sequence[-1-n] for n in range((len(sequence) + 1) // 2))

def check_palindrome2(digits: Iterator[int]) -> bool:
	"""
	Second palindrome check algorithm.

	>>> check_palindrome2(digits(87654, 10))
	False
	>>> check_palindrome2(digits(12344321, 10))
	True
	"""
	sequence = tuple(digits)
	return all(d == s for d, s in zip(sequence, reversed(sequence)))

if __name__ == '__main__':
	doctest.testmod()