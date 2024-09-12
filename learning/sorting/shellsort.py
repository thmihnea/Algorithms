# h-sort an array for sequence values of h.
# An array is h-sorted if for any k, arr[k] < arr[k + h].
# Note: An h-sorted array remains h-sorted after k-sorting it.
# For this implementation of shellshort, we use the x_{n+1} = 3x_n + 1
# sequence. We sort it in large increments and eventually get to 1.
# Idea is that insertion sort is ~ O(n) if array is almost sorted.

def sort(array):
    size: int = len(array)
    h: int = 1
    while h < size // 3:
        h = 3 * h + 1
    
    while h >= 1:
        for i in range(h, size):
            for j in range(i, h - 1, -h):
                if array[j] < array[j - h]:
                    _temp = array[j - h]
                    array[j - h] = array[j]
                    array[j] = _temp
        h = h // 3

if __name__ == '__main__':
    arr = [2, 1, 3, 10, 7]
    sort(arr)
    print(arr)