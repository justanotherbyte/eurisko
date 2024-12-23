import itertools
from typing import Iterable


def _reset_square():
    square = [[None] * 3] * 3
    return square


square = _reset_square()
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_valid(square: list[list[int]]):
    # rows
    for row in square:
        if sum(row) != 15:
            return False

    # columns
    for col_idx in range(3):
        if sum(row[col_idx] for row in square) != 15:
            return False

    # diagonals
    d1 = (0, 1, 2)
    d2 = (2, 1, 0)
    for d in {d1, d2}:
        if sum(row[d[idx]] for idx, row in enumerate(square)) != 15:
            return False

    return True


def _is_hopeless(iterable: Iterable[int]) -> bool:
    tot = 0
    for n in iterable:
        if n is None:
            return False  # we don't know yet

        tot += n

    return tot != 15


def is_hopeless(square: list[list[int]]):
    # similar to is_valid, but doesn't make the assumption
    # that all slots have valid integers
    for row in square:
        if _is_hopeless(row):
            return True

    for col_idx in range(3):
        if _is_hopeless(row[col_idx] for row in square):
            return True

    d1 = (0, 1, 2)
    d2 = (2, 1, 0)
    for d in {d1, d2}:
        if _is_hopeless(row[d[idx]] for idx, row in enumerate(square)):
            return True

    return False


def gen_squares():
    for permutation in itertools.permutations(digits, r=9):
        square = [
            [permutation[0], permutation[1], permutation[2]],
            [permutation[3], permutation[4], permutation[5]],
            [permutation[6], permutation[7], permutation[8]],
        ]
        yield square


for square in gen_squares():
    if is_valid(square):
        print(square)

hopeless_square = [[1, 2, 3], [None, None, 9], [None, 6, None]]
assert is_hopeless(hopeless_square) is True

not_hopeless_square = [[2, None, None], [7, None, None], [6, None, 7]]
assert is_hopeless(not_hopeless_square) is False

# I'll leave it here. I'm not writing 9 nested loops :)
