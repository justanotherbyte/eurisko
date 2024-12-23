def seq1(n: int) -> int:
    if n == 1:
        return 5

    prev = seq1(n - 1)
    return (3 * prev) - 4


def collatz(n: int) -> int:
    if n == 1:
        return 25

    prev = collatz(n - 1)
    return int(prev / 2 if prev % 2 == 0 else (3 * prev) + 1)


def fibonacci(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1

    prev1 = fibonacci(n - 1)
    prev2 = fibonacci(n - 2)
    return prev1 + prev2


def seq2(n: int) -> int:
    if n == 1:
        return 2
    if n == 2:
        return -3

    prev1 = seq2(n - 1)
    prev2 = seq2(n - 2)
    return prev1 * prev2
