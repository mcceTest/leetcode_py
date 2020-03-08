'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
'''

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = m
        # if the m != n, then the last bit is 0
        mask = 1
        while m != n:
            res = res & (~mask)

            m >>= 1
            n >>= 1
            mask <<= 1

        return res 


    def rangeBitwiseAnd2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = m
        for i in range(m + 1, n + 1):
            res = res & i

        return res
        

    @staticmethod
    def main():
        sol = Solution()
        
        m = 0
        n = 2147483647
        print(sol.rangeBitwiseAnd(m, n))
        
        
if __name__ == "__main__":
    Solution.main()