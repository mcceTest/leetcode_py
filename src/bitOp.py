'''
Some common bit operations.
'''


def setBit(n, k):
    '''
    set the kth bit of number n to 1
    '''
    n = n | (1 << k)


def clearBit(n, k):
    '''
    set the kth bit to 0
    '''
    n = n & (~(1 << k))


def toggleBit(n, k):
    '''
    toggle the kth bit. ie. 0 -> 1 or 1 -> 0
    Use XOR:
        With mask 1, bit is toggled
        0 ^ 1 = 1
        1 ^ 1 = 0
        With mask 0, bit is unchanged
        0 ^ 0 = 1
        1 ^ 0 = 1
    '''
    n = n ^ (1 << k)
