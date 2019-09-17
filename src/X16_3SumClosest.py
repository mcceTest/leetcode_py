'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return None

        nums.sort()

        first = 0
        closest = None
        diff = None
        
        while first < len(nums) - 2:
            second = first + 1
            third = len(nums) - 1
            curTarget = target - nums[first]
            while second < third:
                total = nums[second] + nums[third]
                if total == curTarget:
                    return target
                else:
                    curDiff = abs(curTarget - total)
                    if diff is None or diff > curDiff:
                        closest = total + nums[first]
                        diff = curDiff
                    
                    if total < curTarget:
                        second = self.nextDiff(second, nums)
                    else:
                        third = self.preDiff(third, nums)
            
            first = self.nextDiff(first, nums)

        return closest


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

        print(sol.threeSumClosest([-1, 2, 1, -4], 1))

        
if __name__ == "__main__":
    Solution.main()   