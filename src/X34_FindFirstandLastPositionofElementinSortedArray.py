'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''


## TODO: can first search for the lower bound and then use the result to find the higher bound

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        lowIdx = self.bs(nums, 0, len(nums) - 1, target, True)

        if lowIdx == -1:
            return [-1, -1]
        highIdx = self.bs(nums, 0, len(nums) - 1, target, False)

        return [lowIdx, highIdx]
        

    def bs(self, nums, start, end, target, isLow):
        if start > end:
            return -1

        mid = (start + end) // 2
        if nums[mid] == target:
            if isLow:
                nextIdx = self.bs(nums, start, mid - 1, target, isLow)
            else:
                nextIdx = self.bs(nums, mid + 1, end, target, isLow)
            if nextIdx == -1:
                return mid
            else:
                return nextIdx
        elif nums[mid] < target:
            return self.bs(nums, mid + 1, end, target, isLow)
        else:
            return self.bs(nums, start, mid - 1, target, isLow)


    @staticmethod
    def main():
        sol = Solution()
        nums = [1]
        target = 1
        print(sol.searchRange(nums, target))


if __name__ == "__main__":
    Solution.main()   