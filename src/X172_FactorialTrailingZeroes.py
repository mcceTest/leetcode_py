'''
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
'''


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## Trick: count number of 5, since 1= 2 * 5, and there are more 2 than 5
        factor = 5
        count = 0

        while factor <= n:
            count += n // factor
            factor *= 5

        return count

        

    @staticmethod
    def main():
        sol = Solution()
        n = 3
        print(sol.trailingZeroes(n))

        
if __name__ == "__main__":
    Solution.main()