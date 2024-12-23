def check_if_symmetric(string: str) -> bool:
    opposite = ""
    for idx in range(len(string) - 1, -1, -1):
        opposite += string[idx]

    return opposite == string


def convert_to_numbers(string: str) -> list[int]:
    characters = " abcdefghijklmnopqrstuvwxyz"
    return [characters.index(c) for c in string]


def convert_to_letters(string: list[int]) -> str:
    characters = " abcdefghijklmnopqrstuvwxyz"
    return "".join(characters[idx] for idx in string)


def get_intersection(array1: list, array2: list) -> list:
    intersection = []
    for item in array1:
        if item in array2 and item not in intersection:
            intersection.append(item)

    return intersection


def get_union(array1: list, array2: list) -> list:
    union = []
    for item in array1:
        if item not in union:
            union.append(item)

    for item in array2:
        if item not in union:
            union.append(item)

    return union


def count_characters(string: str) -> dict[str, int]:
    counter = {}
    for c in string:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1

    return counter


def is_prime(num: int) -> bool:
    for i in range(2, 10):
        if num % i == 0:
            return True

    return False
