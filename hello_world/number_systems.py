def base_b_to_decimal(b: int, number: str) -> int:
    out = 0
    number = number[::-1]
    for idx in range(len(number)):
        digit = int(number[idx])
        out += digit * (b**idx)

    return out


def _get_largest_n(b: int, number: int) -> int:
    n = 0
    while True:
        if (b**n) > number:
            return n - 1

        n += 1


def _get_largest_multiple(b_n: int, number: int) -> int:
    n = 0
    while True:
        if (b_n * n) > number:
            return n - 1

        n += 1


def decimal_to_base_b(b: int, number: int) -> list[int]:
    coefficients = []
    power = _get_largest_n(b, number)
    while power >= 0:
        coef = _get_largest_multiple(b**power, number)
        coefficients.append(coef)
        number -= coef * (b**power)
        power -= 1

    return coefficients


print(base_b_to_decimal(2, "11010"))
print(decimal_to_base_b(2, 34))
