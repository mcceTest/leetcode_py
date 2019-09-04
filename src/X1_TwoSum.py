'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        elemIdxDic = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in elemIdxDic:
                return (elemIdxDic[comp], i)
            else:
                elemIdxDic[n] = i

    
    @staticmethod
    def main():
        sol = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        print(sol.twoSum(nums, target))


if __name__ == "__main__":
    Solution.main()