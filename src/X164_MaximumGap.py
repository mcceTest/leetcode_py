'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.
'''
from functools import partial
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

import math

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        minNum = min(nums)
        maxNum = max(nums)

        if minNum == maxNum:
            return 0

        # max diff is maxNum - minNum
        #    and the len(nums) elements, so the max gap should be at least the average gap
        gap = math.ceil((maxNum - minNum) / (len(nums) - 1))

        # divivde the numbers into buckets
        # for k bucket [minNum + k * gap, minNum + (k + 1) * gap), left inclusive
        nbuckets = math.floor((maxNum - minNum) / gap) + 1

        # print("gap:{0}, nbuckets:{1}".format(gap, nbuckets))
        buckets = [ [None, None] for _ in range(nbuckets) ]
        for num in nums:
            idx = (num - minNum) // gap
            # update min element
            if buckets[idx][0] is None or num < buckets[idx][0]:
                buckets[idx][0] = num

            # update max element
            if buckets[idx][1] is None or num > buckets[idx][1]:
                buckets[idx][1] = num

        # the max gap must be between numbers in different buckets, since the max diff within a bucket < gap
        preMax = None
        maxDiff = 0
        for bucket in buckets:
            if bucket[0] is not None:
                if preMax is not None:
                    diff = bucket[0] - preMax
                    if diff > maxDiff:
                        maxDiff = diff
                preMax = bucket[1]

        return maxDiff
                

    def maximumGap2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        nums = radixSort(nums)
        res = 0
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff > res:
                res = diff

        return res
        

    @staticmethod
    def main():
        sol = Solution()
        nums = [1,10000000]
        print(sol.maximumGap(nums))

if __name__ == "__main__":
    Solution.main()