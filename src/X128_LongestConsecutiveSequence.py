'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        curMap = {}
        longestLength = 1
        # make sure the numbers are unique
        for num in nums:
            if num in curMap:
                continue

            left = curMap.get(num - 1, 0)
            right = curMap.get(num + 1, 0)

            curLen = left + right + 1
            longestLength = max(longestLength, curLen)
            # avoid duplicates
            curMap[num] = curLen
            # think of each range as disjoined set
            # length of the set is represented by the start and end number
            curMap[num - left] = curLen
            curMap[num + right] = curLen

        return longestLength


    def longestConsecutive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        numsSet = set(nums)
        longestLength = 1

        for num in nums:
            if num not in numsSet:
                continue

            curLen = 1
            curNum = num - 1
            while curNum in numsSet:
                numsSet.remove(curNum)
                curLen += 1
                curNum -= 1

            curNum = num + 1
            while curNum in numsSet:
                numsSet.remove(curNum)
                curLen += 1
                curNum += 1

            longestLength = max(longestLength, curLen)

        return longestLength


    @staticmethod
    def main():
        sol = Solution()
        nums = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
        print(sol.longestConsecutive(nums))


if __name__ == "__main__":
    Solution.main() 