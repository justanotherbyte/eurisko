import random


def calc_min(arr: list[int]) -> int:
    minimum = arr[0]
    for n in arr:
        if n < minimum:
            minimum = n

    return minimum


def selection_sort(arr: list[int]) -> list[int]:
    copy = arr.copy()
    sorted_arr = []

    while len(copy) > 0:
        m = calc_min(copy)
        sorted_arr.append(m)
        copy.remove(m)

    return sorted_arr


def combine(*arr: list[int]):
    full = []
    for a in arr:
        full.extend(a)

    return selection_sort(full)


def quicksort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    pivot_idx = random.choice(range(len(arr)))
    pivot = arr[pivot_idx]
    pieces = [
        [n for n in arr if n < pivot],
        [n for n in arr if n == pivot],
        [n for n in arr if n > pivot],
    ]
    lt = quicksort(pieces[0])
    gt = quicksort(pieces[2])

    return combine(lt, pieces[1], gt)


arr = [5, 7, 1, 4, 0, -1, 23, 23]
arr = quicksort(arr)
print(arr)
