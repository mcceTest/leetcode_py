import copy

def countSort(arr, f=None):
    '''
    Count sort not in place, but stable
    '''
    
    out = copy.copy(arr)
    keys = None
    if f is None:
        keys = arr
    else:
        keys = list(map(f, arr))

    maxNum = max(keys)
    count = [0] * (maxNum + 1)
    for n in keys:
        count[n] += 1
    for i in range(1, maxNum + 1):
        count[i] += count[i - 1]
    
    for i in range(len(arr) - 1, -1, -1):
        n = keys[i]
        out[count[n] - 1] = arr[i]
        count[n] -= 1

    return out
    




if __name__ == "__main__":
    arr = [2,1,3, 1, 1]
    print(countSort(arr, lambda x: x % 2)) 