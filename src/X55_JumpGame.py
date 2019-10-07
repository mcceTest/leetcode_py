'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''


class Solution(object):
    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True

        curStart = 0
        curEnd = 0
        
        while curEnd < len(nums) - 1:
            nextEnd = curEnd
            for idx in range(curStart, curEnd + 1):
                nextEnd = max(nextEnd, nums[idx] + idx)

            if nextEnd == curEnd:
                return False

            curStart = curEnd + 1
            curEnd = nextEnd

        return True


    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True

        curIdx = 0
        curFar = 0

        while curFar < len(nums) -1 and curIdx <= curFar:
            curFar = max(curFar, curIdx + nums[curIdx])
            curIdx += 1

        return curFar >= len(nums) - 1

        

    @staticmethod
    def main():
        sol = Solution()
        nums = [3,2,1,0,4]
        print(sol.canJump(nums))

if __name__ == "__main__":
    Solution.main() 