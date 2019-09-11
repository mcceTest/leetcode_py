'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        left = 0

        isNeg = x < 0 
        if isNeg:
            x = -1 * x

        while x != 0:
            left = x % 10
            res = res * 10 + left
            x = x // 10

        if isNeg:
            res = res * -1

        if res < - 2 ** 31 or res > 2 ** 31 - 1:
            return 0

        return res


    @staticmethod
    def main():
        sol = Solution()

        print(sol.reverse(123))

        print(sol.reverse(-123))

        print(sol.reverse(120))

        print(sol.reverse(0))



if __name__ == "__main__":
    Solution.main()     
