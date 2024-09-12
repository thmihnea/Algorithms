from typing import List

def is_sorted(array: List[int], low: int, high: int) -> bool:
    for i in range(low, high):
        if array[i] > array[i + 1]:
            return False
    return True

def merge(array: List[int], aux: List[int], low: int, mid: int, high: int):
    assert is_sorted(array, low, mid)
    assert is_sorted(array, mid + 1, high)

    i: int = low
    j: int = mid + 1

    for k in range(low, high + 1):
        if i > mid:
            # Left array is exhausted.
            array[k] = aux[j]
            j += 1
        elif j > high:
            # Right array is exhausted.
            array[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            # Right element is smaller.
            array[k] = aux[j]
            j += 1
        else:
            # Left element is smaller.
            array[k] = aux[i]
            i += 1
    
    assert is_sorted(array, low, high)

def _sort(array: List[int], aux: List[int], low: int, high: int):
    if high <= low:
        return
    mid: int = (low + high) // 2
    _sort(array, aux, low, mid)
    _sort(array, aux, mid + 1, high)
    merge(array, aux, low, mid, high)

def sort(array: List[int]):
    aux: List[int] = [array[i] for i in range(len(array))]
    _sort(array, aux, 0, len(arr) - 1)

if __name__ == '__main__':
    arr = [3, 5, 7, 1, 2]
    sort(arr)
    print(arr)