'''
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
'''



class Solution(object):
    def numDistinct2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [ [-1] * (len(t) + 1) for _ in range(len(s) + 1) ]
        for i in range(len(s) + 1):
            dp[i][len(t)] = 1
        for i in range(len(t)):
            for j in range(max(len(s) - (len(t) - i) + 1, 0), len(s) + 1):
                dp[j][i] = 0

        return self.helper(s, 0, t, 0, dp)


    def helper(self, s, sidx, t, tidx, dp):
        if dp[sidx][tidx] >= 0:
            return dp[sidx][tidx]

        if sidx > len(s) or tidx > len(t):
            return 0

        count = self.helper(s, sidx + 1, t, tidx, dp)
        if sidx < len(s) and tidx < len(t) and s[sidx] == t[tidx]:
            count += self.helper(s, sidx + 1, t, tidx + 1, dp)

        dp[sidx][tidx] = count

        return count

    def numDistinct(self, s, t):
        """
        Bottom-up
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [0] * (len(t) + 1)
        dp[len(t)] = 1

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t)):
                if s[i] == t[j]:
                    dp[j] += dp[j + 1]

        return dp[0]


    @staticmethod
    def main():
        sol = Solution()
        S = "rabbbit"
        T = "rabbit"
        print(sol.numDistinct(S, T))


if __name__ == "__main__":
    Solution.main() 