'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
'''


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, low, hi):
        if low == hi or nums[low] < nums[hi]:
            return nums[low]
        else:
            mid = (low + hi) // 2
            return min(self.helper(nums, low, mid), self.helper(nums, mid + 1, hi))
        

    @staticmethod
    def main():
        sol = Solution()
        nums = [2,2,2,0,1]
        print(sol.findMin(nums))

if __name__ == "__main__":
    Solution.main()