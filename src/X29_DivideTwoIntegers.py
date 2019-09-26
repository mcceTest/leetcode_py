'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''

## bit operation

import math

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0

        if dividend == - 2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        sign = -1 if ((dividend > 0) != (divisor > 0)) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        res = 0
        while dividend >= divisor:
            cur = 1
            curDivisor = divisor
            while curDivisor << 1 <= dividend:
                curDivisor <<= 1
                cur <<= 1
            res += cur
            dividend -= cur * divisor

        return res * sign


    @staticmethod
    def main():
        sol = Solution()

        dividend = 10
        divisor = 3
        
        print(sol.divide(dividend, divisor))

        dividend = 7
        divisor = -3

        print(sol.divide(dividend, divisor))
        

if __name__ == "__main__":
    Solution.main()   