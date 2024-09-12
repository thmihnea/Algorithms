from typing import List
import random

def swap(array: List[int], i: int, j: int):
    _temp = array[i]
    array[i] = array[j]
    array[j] = _temp

def shuffle(array: List[int]):
    for i in range(len(array)):
        r = random.randint(0, i)
        swap(array, i, r)

def partition(array: List[int], low: int, high: int):
    i: int = low + 1
    j: int = high - 1

    while True:
        while i < high and array[i] < array[low]:
            i += 1
        
        while j > low and array[j] > array[low]:
            j -= 1
        
        if i >= j:
            break
        swap(array, i, j)
    
    swap(array, low, j)
    return j

def _sort(array: List[int], low: int, high: int):
    if high <= low:
        return
    pivot: int = partition(array, low, high)
    _sort(array, low, pivot - 1)
    _sort(array, pivot + 1, high)

def sort(array: List[int]):
    shuffle(array)
    _sort(array, 0, len(array) - 1)

if __name__ == '__main__':
    a = [3, 2, 10, 1, 8, 5, 2]
    sort(a)
    print(a)
