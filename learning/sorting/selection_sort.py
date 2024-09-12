# O(n^2) sorting algorithm. Bad, but easy to remember.

def sort(array):
    idx: int = 0
    min: int = 0
    size: int = len(array)

    while idx < size:
        for i in range(idx, size):
            min = i if array[i] < array[min] else min
        _temp = array[idx]
        array[idx] = array[min]
        array[min] = _temp
        idx += 1
        min = idx

if __name__ == '__main__':
    arr = [2, 1, 3, 10, 7]
    sort(arr)
    print(arr)