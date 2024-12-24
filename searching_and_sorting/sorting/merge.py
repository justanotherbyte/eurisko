def _split_array(arr: list[int]) -> tuple[list[int], list[int]]:
    length = len(arr)
    mid = length // 2
    return (arr[:mid], arr[mid:])


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


def merge(arr1: list[int], arr2: list[int]) -> list[int]:
    combined = arr1 + arr2
    selection_sort(combined)

    return combined


def merge_sort(arr: list[int]):
    if len(arr) == 1:
        return arr

    h1, h2 = _split_array(arr)
    return merge(merge_sort(h1), merge_sort(h2))


arr = [5, 7, 1, 4, 0, -1, 23, 23]
arr = merge_sort(arr)
print(arr)
