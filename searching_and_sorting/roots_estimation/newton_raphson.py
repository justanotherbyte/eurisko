from typing import Callable


Number = int | float
Function = Callable[[Number], Number]


def newton_raphson(f: Function, fprime: Function, guess: Number) -> Number:
    while True:
        slope = fprime(guess)
        c = f(guess) - (guess * fprime(guess))
        new = -(c / slope)
        if new == guess:
            # this is True within python's default precision
            # we have converged
            return new

        guess = new


f = lambda x: (x**3) - 2
fprime = lambda x: 3 * (x**2)
print(newton_raphson(f, fprime, 2))


def calc_root_newton_raphson(a: Number, n: Number):
    f = lambda x: (x**n) - a
    fprime = lambda x: n * (x ** (n - 1))
    return newton_raphson(f, fprime, 1000)


print(calc_root_newton_raphson(2, 3))
