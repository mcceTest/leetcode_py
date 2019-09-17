'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
## TODO: recursive solution

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return None

        nums.sort()

        res = []

        first = 0
        if 4 * nums[first] > target or 4 * nums[-1] < target:
            return res

        while first < len(nums) - 3:
            firstTarget = target - nums[first]
            
            second = first + 1
            if 3 * nums[second] > firstTarget:
                break
            if 3 * nums[-1] < firstTarget:
                first += 1
                continue

            while second < len(nums) - 2:
                secondTarget = firstTarget - nums[second]

                third = second + 1
                if 2 * nums[third] > secondTarget:
                    break
                if 2 * nums[-1] < secondTarget:
                    second += 1
                    continue

                fourth = len(nums) - 1
                while third < fourth:
                    total = nums[third] + nums[fourth]

                    if total == secondTarget:
                        res.append([nums[first], nums[second], nums[third], nums[fourth]])
                        third = self.nextDiff(third, nums)
                        fourth = self.preDiff(fourth, nums)
                    elif total > secondTarget:
                        fourth = self.preDiff(fourth, nums)
                    else:
                        third = self.nextDiff(third, nums)
                second = self.nextDiff(second, nums)
            first = self.nextDiff(first, nums)

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

        print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))
        print(sol.fourSum([-3,-2,-1,0,0,1,2,3], 0))


        
if __name__ == "__main__":
    Solution.main()   