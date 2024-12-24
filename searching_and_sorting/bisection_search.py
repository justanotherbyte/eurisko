from typing import Callable


Number = int | float


def bisection_search(
    f: Callable[[Number], Number], upper: Number, lower: Number
) -> Number:
    assert f(upper) > f(lower), "f(upper) > f(lower) not met (cannot be equal)"

    while True:
        midpoint = (upper + lower) / 2
        if f(midpoint) > 0:
            upper = midpoint
        elif f(midpoint) < 0:
            lower = midpoint
        else:
            # returns if zero within Python's default precision
            return midpoint


f = lambda x: (x**3) - 2
f2 = lambda x: (2 * x) + 1

print(bisection_search(f, 3, 1))
print(bisection_search(f2, 10, -10))


def calc_root_bisection(a: Number, n: Number):
    f = lambda x: (x**n) - a
    return bisection_search(f, 10000, -10000)


print(calc_root_bisection(2, 3))
