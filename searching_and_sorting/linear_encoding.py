def encode_string(string: str, a: int, b: int):
    charset = " abcdefghijklmnopqrstuvwxyz"

    def f(x: int):
        return (a * x) + b

    return [f(charset.index(c)) for c in string]


def decode_numbers(numbers: list[int], a: int, b: int):
    charset = " abcdefghijklmnopqrstuvwxyz"

    def f_inv(x: int):
        return (x - b) / a

    msg = ""
    for n in numbers:
        idx = f_inv(n)
        if idx >= len(charset) or idx < 0 or not idx.is_integer():
            return False

        msg += charset[int(idx)]

    return msg


message = "hello world"
a, b = 3, 4
cipher = encode_string(message, a, b)
print(cipher)
decoded = decode_numbers(cipher, a, b)
print(decoded)


def decode_exercise():
    exercise_cipher = [
        377,
        717,
        71,
        513,
        105,
        921,
        581,
        547,
        547,
        105,
        377,
        717,
        241,
        71,
        105,
        547,
        71,
        377,
        547,
        717,
        751,
        683,
        785,
        513,
        241,
        547,
        751,
    ]

    possible_messages = []

    for a in range(1, 101):
        for b in range(0, 101):
            message = decode_numbers(exercise_cipher, a, b)
            if message:
                possible_messages.append(message)

    return possible_messages


print(decode_exercise())
