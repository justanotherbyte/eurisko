def calc_min(arr: list[int]) -> int:
    minimum = arr[0]
    for n in arr:
        if n < minimum:
            minimum = n

    return minimum


def insertion_sort(arr: list[int]):
    length = len(arr)
    while True:
        swap_made = False
        for idx in range(length - 1):
            n1 = arr[idx]
            n2 = arr[idx + 1]
            if n1 > n2:
                # swap
                arr[idx] = n2
                arr[idx + 1] = n1

                note = idx + 1
                swap_made = True

                for jdx in range(note, 0, -1):
                    j1 = arr[jdx]
                    j2 = arr[jdx - 1]
                    if j2 > j1:
                        # swap
                        arr[jdx - 1] = j1
                        arr[jdx] = j2
        if not swap_made:
            break


arr = [5, 7, 1, 4, 0, -1, 23, 23]
insertion_sort(arr)
print(arr)
