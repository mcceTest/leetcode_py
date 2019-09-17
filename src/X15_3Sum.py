'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        nums.sort()

        res = []
        idx = 0
        while idx < len(nums) - 2:
            rightPart = self.searchTwo(idx + 1, len(nums) - 1, nums,  -nums[idx], nums[idx])
            res.extend(rightPart)
            while idx < len(nums) -2 and nums[idx+1] == nums[idx]:
                idx += 1

            idx += 1

        return res


    def searchTwo(self, low, hi, nums, target, first):
        res = []
        while low < hi:
            total = nums[low] + nums[hi]

            if total == target:
                res.append([first, nums[low], nums[hi]])
                low = self.nextDiff(low, nums)
                hi  = self.preDiff(hi, nums)
            elif total > target:
                hi  = self.preDiff(hi, nums)
            else:
                low = self.nextDiff(low, nums)

        return res

    
    def nextDiff(self, idx, nums):
        while idx < len(nums) - 1:
            if nums[idx] != nums[idx + 1]:
                return idx + 1
            else:
                idx += 1

        return len(nums)


    def preDiff(self, idx, nums):
        while idx > 0:
            if nums[idx] != nums[idx - 1]:
                return idx - 1
            else:
                idx -= 1

        return -1

    
    @staticmethod
    def main():
        sol = Solution()

        print(sol.threeSum([-1, 0, 1, 2, -1, -4]))

        print(sol.threeSum([-2,0,0,2,2]))

        
if __name__ == "__main__":
    Solution.main()   