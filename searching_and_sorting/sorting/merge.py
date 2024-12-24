def _split_array(arr: list[int]) -> tuple[list[int], list[int]]:
    length = len(arr)
    mid = length // 2
    return (arr[:mid], arr[mid:])


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


def merge(arr1: list[int], arr2: list[int]) -> list[int]:
    combined = arr1 + arr2
    insertion_sort(combined)
    return combined


def merge_sort(arr: list[int]):
    if len(arr) == 1:
        return arr

    h1, h2 = _split_array(arr)
    print(h1, h2)
    return merge(merge_sort(h1), merge_sort(h2))


arr = [5, 7, 1, 4, 0, -1, 23, 23]
arr = merge_sort(arr)
print(arr)
