"""
Hands of cards
"""
from collections import Counter
import doctest
from typing import Sequence

def match_five(cards: Sequence[int]) -> bool:
	"""
	Check if the cards are all equal.

	>>> match_five((4, 4, 4, 4, 4))
	True
	>>> match_five((1, 5, 4, 6, 5))
	False
	"""
	return 5 in Counter(cards).values()

def match_four(cards: Sequence[int]) -> bool:
	"""
	Check if four cards are equal.

	>>> match_four((4, 4, 4, 4, 5))
	True
	>>> match_four((1, 5, 4, 6, 5))
	False
	"""
	return 4 in Counter(cards).values()

def match_three(cards: Sequence[int]) -> bool:
	"""
	Check if three cards are equal.

	>>> match_three((4, 4, 5, 4, 5))
	True
	>>> match_three((1, 5, 4, 6, 5))
	False
	"""
	return 3 in Counter(cards).values()

def match_two_pairs(cards: Sequence[int]) -> bool:
	"""
	Check if there are two pairs in the cards..

	>>> match_two_pairs((1, 4, 5, 4, 5))
	True
	>>> match_two_pairs((1, 5, 4, 6, 5))
	False
	"""
	return [1, 2, 2] == sorted(Counter(cards).values())

if __name__ == '__main__':
	doctest.testmod()