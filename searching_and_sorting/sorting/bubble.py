def calc_min(arr: list[int]) -> int:
    minimum = arr[0]
    for n in arr:
        if n < minimum:
            minimum = n

    return minimum


def bubble_sort(arr: list[int]):
    length = len(arr)
    while True:
        swap_made = False
        for idx in range(length - 1):
            n1 = arr[idx]
            n2 = arr[idx + 1]
            if n1 > n2:
                # swap
                swap_made = True
                arr[idx] = n2
                arr[idx + 1] = n1

        if swap_made is False:
            break


arr = [5, 7, 1, 4, 0, -1, 23, 23]
bubble_sort(arr)
print(arr)
