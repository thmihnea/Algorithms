# Shuffling algorithm.
# The idea is that normally, the naive approach to shuffling
# would be to generate a random number in [0, 1] for each object,
# and then sort the array to produce a uniformly-shuffled array.
# This results in ~ O(nlogn) performance.
# However, we can use Knuth Shuffling to shuffle an
# array in linear time!

import random

def shuffle(array):
    """
    Using a loop, pick a random number r
    from [[0, i]] and swap array[i] and array[r].
    """
    size: int = len(array)
    for i in range(size):
        r: int = random.randint(0, i)
        _temp = array[r]
        array[r] = array[i]
        array[i] = _temp

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    shuffle(arr)
    print(arr)
