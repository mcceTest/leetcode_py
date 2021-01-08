'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
'''


class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[0]
            else:
                return nums[1]
        else:
            op1 = nums[0] + self.robLinear(nums, 2, len(nums) - 2)
            op2 = nums[1] + self.robLinear(nums, 3, len(nums) - 1)
            op3 = nums[2] + self.robLinear(nums, 4, len(nums) - 1)

            return max([op1, op2, op3])     
        

    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[0]
            else:
                return nums[1]
        else:
            # could be simpler. the end point is only either len(nums) - 1 or len(nums) - 2
            dp = [ [-1] * len(nums) for _ in range(len(nums))]
            op1 = nums[0] + self.helper(nums, 2, len(nums) - 2, dp)
            op2 = nums[1] + self.helper(nums, 3, len(nums) - 1, dp)
            op3 = nums[2] + self.helper(nums, 4, len(nums) - 1, dp)

            return max([op1, op2, op3])     

    def helper(self, nums, start, end, dp):
        
        if start > end:
            return 0
        else:
            if start == end:
                return nums[start]
            else:
                if dp[start][end] >= 0:
                    return dp[start][end]

                op1 = nums[start] + self.helper(nums, start + 2, end, dp)
                op2 = nums[start + 1] + self.helper(nums, start + 3, end, dp)
                if op1 > op2:
                    dp[start][end] = op1
                else:
                    dp[start][end] = op2

                return dp[start][end]

    def robLinear(self, nums, start, end):
        '''
        Rob houses in a line
        '''
        preInclude = preExclude = 0
        for idx in range(start, end + 1):
            num = nums[idx]
            curInclude = preExclude + num
            curExclude = max(preInclude, preExclude)

            preInclude = curInclude
            preExclude = curExclude

        return max(preInclude, preExclude)

    @staticmethod
    def main():
        sol = Solution()
        nums = [226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,55,209,18,55,122,65,66,177,101,63,201,172,130,103,225,142,46,86,185,62,138,212,192,125,77,223,188,99,228,90,25,193,211,84,239,119,234,85,83,123,120,131,203,219,10,82,35,120,180,249,106,37,169,225,54,103,55,166,124]
        print(sol.rob(nums))

if __name__ == "__main__":
    Solution.main()