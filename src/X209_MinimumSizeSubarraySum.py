'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''



class Solution(object):



    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if sum(nums) < s:
            return 0

        minLen = len(nums)
        total = 0
        start = 0
        
        for cur, num in enumerate(nums):
            total += num
            while total >= s:
                curLen = cur - start + 1
                if curLen < minLen:
                    minLen = curLen
                total -= nums[start]
                start += 1

        return minLen

        

    ## O(nlgn) solution, binary search
    def minSubArrayLen2(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        for num in nums:
            if num >= s:
                return 1

        sums = [0] * len(nums)
        sums[0] = nums[0]
        for i in range(1, len(nums)):
            sums[i] = sums[i-1] + nums[i]

        if sums[len(nums) - 1] < s:
            return 0

        lo = 1
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            midSum = self.maxSumRange(nums, sums, mid)
            if midSum < s:
                lo = mid + 1
            else:
                hi = mid

        return hi


    def maxSumRange(self, nums, sums, l):
        res = 0
        for i in range(0, len(nums) - l + 1):
            cur = self.getRangeSum(nums, sums, i, i + l - 1)
            if cur > res:
                res = cur
        return res


    def getRangeSum(self, nums, sums, start, end):
        return sums[end] - sums[start] + nums[start]


    @staticmethod
    def main():
        sol = Solution()
        s = 7
        nums = [2,3,1,2,4,3]
        print(sol.minSubArrayLen(s, nums))
        

if __name__ == "__main__":
    Solution.main()
        