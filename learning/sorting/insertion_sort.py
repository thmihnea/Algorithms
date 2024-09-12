def sort(array):
    size = len(array)
    for i in range(size):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                _temp = array[j - 1]
                array[j - 1] = array[j]
                array[j] = _temp

if __name__ == '__main__':
    arr = [2, 1, 3, 10, 7]
    sort(arr)
    print(arr)