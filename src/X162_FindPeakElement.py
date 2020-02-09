'''
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.
'''


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        if len(nums) == 1:
            return 0

        # specail cases where points are at the end points
        if nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return len(nums) - 1
            
        # the index must be between 1 and len(nums) - 2 (inclusive)
        #   as there must be a index at peak (nums[-1] = nums[len(nums)] = - Infinity)
        return self.peakIndex(nums, 1, len(nums) - 2)


    def peakIndex(self, nums, lo, hi):
        mid = (lo + hi) // 2

        if nums[mid] > nums[mid - 1]:
            if nums[mid] > nums[mid + 1]:
                return mid
            else:
                return self.peakIndex(nums, mid + 1, hi)
        else:
            return self.peakIndex(nums, lo, mid - 1)


    @staticmethod
    def main():
        sol = Solution()
        nums = [1,2,3,1]
        print(sol.findPeakElement(nums))

if __name__ == "__main__":
    Solution.main()
        