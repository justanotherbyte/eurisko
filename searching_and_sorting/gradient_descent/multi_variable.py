import inspect
from typing import Callable, Iterable
from math import sin, cos

Number = int | float
Function = (
    Callable[[Number], Number]
    | Callable[[Number, Number], Number]
    | Callable[[Number, Number, Number], Number]
)


def multi_variable_descent(
    f: Function, fprimes: tuple[Function], alpha: Number, guess: list[Number]
) -> list[Number]:
    n_parameters = len(inspect.signature(f).parameters)
    assert (
        len(fprimes) == n_parameters
    ), "Not enough partial derivative functions provided"

    assert n_parameters == len(
        guess
    ), f"Size of guess vector does not match. Expecting {n_parameters}x1 vector."

    while True:
        new = [
            guess[idx] - (alpha * fprimes[idx](*guess)) for idx in range(n_parameters)
        ]
        if new == guess:
            # converged
            return new

        guess = new


LEARNING_RATE = 0.001

f = lambda x, y: (x * sin(y)) + (x**2)
fprimes = (lambda x, y: sin(y) + (2 * x), lambda x, y: x * cos(y))
x_min = multi_variable_descent(f, fprimes, LEARNING_RATE, [1, 2])  # type: ignore
print(x_min, f(*x_min))

f = lambda x, y: (x - 1) ** 2 + 3 * (y**2)
fprimes = (lambda x, y: 2 * (x - 1), lambda x, y: 6 * y)
x_min = multi_variable_descent(f, fprimes, LEARNING_RATE, [1, 2])  # type: ignore
print(x_min, f(*x_min))

# Do the same for the other functions. Concept is the same.
