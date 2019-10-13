'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1

        p1 = 1
        p2 = 1

        for i in range(2, n + 1):
            cur = p1 + p2
            p1 = p2
            p2 = cur

        return p2

    @staticmethod
    def main():
        sol = Solution()
        n = 2

        print(sol.climbStairs(n))



if __name__ == "__main__":
    Solution.main() 
