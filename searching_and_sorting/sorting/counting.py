def calc_min(arr: list[int]) -> int:
    minimum = arr[0]
    for n in arr:
        if n < minimum:
            minimum = n

    return minimum


def calc_max(arr: list[int]) -> int:
    maximum = arr[0]
    for n in arr:
        if n > maximum:
            maximum = n

    return maximum


def counting_sort(arr: list[int]):
    m = calc_min(arr)
    for idx, num in enumerate(arr):
        arr[idx] = num - m

    N = calc_max(arr)
    counts = [0] * (N + 1)
    for n in arr:
        counts[n] += 1

    new_arr = []
    for idx, _ in enumerate(counts):
        new_arr.extend([idx] * counts[idx])

    for idx, num in enumerate(new_arr):
        new_arr[idx] = num + m

    return new_arr


arr = [5, 7, 1, 4, 0, -1, 23, 23]
arr = counting_sort(arr)
print(arr)


# inefficient counting sort (9)
arr = [5, 7, 1, 4, 0, -1, 23, 23, 100000000000000000]
arr = counting_sort(arr)  # raises a MemoryError. Problem solved :)
print(arr)
