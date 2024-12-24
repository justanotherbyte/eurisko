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


arr = [5, 7, 1, 4, 0, -1, 23, 23]
print(selection_sort(arr))
