'''
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0

        if n == 0:
            return 1

        if n == 1:
            return x

        isNeg = False
        if n < 0:
            isNeg = True
            n = -n

        half = self.myPow(x, n // 2)
        cur = half * half
        if n % 2 == 1:
            cur *= x

        if isNeg:
            cur = 1 / cur

        return cur


        



    @staticmethod
    def main():
        sol = Solution()
        x = 2.00000
        n = 10
        print(sol.myPow(x, n))
        

if __name__ == "__main__":
    Solution.main() 