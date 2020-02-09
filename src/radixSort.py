from functools import partial
from countSort import countSort
import copy

def f(d, num):
    return num // d % 10 

def radixSort(arr):
    '''
    Radix sort an array of numbers
    '''
    maxNum = max(arr)
    out = copy.copy(arr)
    d = 1
    while d <= maxNum:
        fd = partial(f, d)
        out = countSort(out, fd)
        d *= 10

    return out


if __name__ == "__main__":
    arr = [2, 10, 109,5]
    print(radixSort(arr))
    
    