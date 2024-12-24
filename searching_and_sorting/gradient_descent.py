from math import sin, cos, e
from typing import Callable


Number = int | float
Function = Callable[[Number], Number]


def single_variable_descent(fprime: Function, alpha: Number, guess: Number):
    while True:
        new = guess - (alpha * fprime(guess))
        if new == guess:
            # converged
            return new

        guess = new


def single_variable_ascent(fprime: Function, alpha: Number, guess: Number):
    while True:
        new = guess + (alpha * fprime(guess))
        if new == guess:
            # converged
            return new

        guess = new


LEARNING_RATE = 0.001

f = lambda x: (x**2) + x + 1
fprime = lambda x: (2 * x) + 1
x_min = single_variable_descent(fprime, LEARNING_RATE, 0.5)
print(x_min, f(x_min))

f = lambda x: (x**3) - (x**4) - (x**2)
fprime = lambda x: (3 * (x**2)) - (4 * (x**3)) - (2 * x)
x_min = single_variable_ascent(fprime, LEARNING_RATE, 0.5)
print(x_min, f(x_min))

# the following derivatives were calculated on paper

f = lambda x: sin(x) / (1 + (x**2))
fprime = lambda x: ((1 + (x**2)) * (cos(x)) - ((2 * x) * sin(x))) / (1 + (x**2)) ** 2
x_min = single_variable_descent(fprime, LEARNING_RATE, 0.5)
x_max = single_variable_ascent(fprime, LEARNING_RATE, 0.5)
print(x_min, f(x_min))
print(x_max, f(x_max))

f = lambda x: (3 * cos(x)) + ((x**2) * (e ** sin(x)))
fprime = (
    lambda x: (-3 * sin(x))
    + ((x**2) * (cos(x) * (e ** sin(x))))
    + ((2 * x) * (e ** sin(x)))
)

x_min = single_variable_descent(fprime, LEARNING_RATE, 0.5)
x_max = single_variable_ascent(fprime, LEARNING_RATE, 2)  # local maxiumum
print(x_min, f(x_min))
print(x_max, f(x_max))
