'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
'''

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0

        curStart = 0
        curEnd = 0

        steps = 0
        while curEnd < len(nums) - 1:
            steps += 1
            nextStart = curEnd + 1
            nextEnd = curEnd
            for idx in range(curStart, curEnd + 1):
                nextIdx = idx + nums[idx]
                if nextIdx > nextEnd:
                    nextEnd = nextIdx
                    if nextEnd >= len(nums) - 1:
                        return steps

            curStart = nextStart
            curEnd = nextEnd

        return steps
        

        

    @staticmethod
    def main():
        sol = Solution()

        nums = [2,3,1,1,4]
        print(sol.jump(nums))
        

if __name__ == "__main__":
    Solution.main() 