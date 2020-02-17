'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''

import functools

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ''

        strNums = map(str, nums)
        def greater(a, b):
            s1 = a + b
            s2 = b + a

            if s1 < s2:
                return 1
            elif s1 > s2:
                return -1
            else:
                return 0

        sortedNums = sorted(strNums, key=functools.cmp_to_key(greater))

        res = ''.join(sortedNums)
        if res[0] == '0':
            return '0'

        return res
        

    @staticmethod
    def main():
        sol = Solution()
        nums = [0, 0]
        print(sol.largestNumber(nums))
        
        
if __name__ == "__main__":
    Solution.main()