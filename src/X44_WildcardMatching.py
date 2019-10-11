'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
'''


class Solution(object):
    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sLen = len(s)
        pLen = len(p)

        if pLen == 0 and sLen > 0:
            return False

        dp = [ [False] * (sLen + 1) for _ in range(pLen + 1)]
        dp[pLen][sLen] = True

        for i in range(sLen):
            dp[pLen][i] = False

        for pIdx in range(pLen - 1, -1, -1):
            for sIdx in range(sLen, -1, -1):
                if sIdx == sLen:
                    if p[pIdx] == '*':
                        dp[pIdx][sIdx] = dp[pIdx + 1][sIdx]
                    else:
                        dp[pIdx][sIdx] = False
                else:
                    if p[pIdx] == '?':
                        dp[pIdx][sIdx] = dp[pIdx + 1][sIdx + 1]
                    elif p[pIdx] == '*':
                        for i in range(sIdx, sLen + 1):
                            if dp[pIdx + 1][i]:
                                dp[pIdx][sIdx] = True
                                break
                    else:
                        dp[pIdx][sIdx] = (p[pIdx] == s[sIdx] and dp[pIdx + 1][sIdx + 1])

        return dp[0][0]


    def isMatch3(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sLen = len(s)
        pLen = len(p)

        if pLen == 0 and sLen > 0:
            return False

        dp = [ [None] * (sLen + 1) for _ in range(pLen + 1)]
        dp[pLen][sLen] = True

        for i in range(sLen):
            dp[pLen][i] = False

        return self.dfs(s, p, 0, 0, dp)

        
    def dfs(self, s, p, sIdx, pIdx, dp):
        if dp[pIdx][sIdx] is not None:
            return dp[pIdx][sIdx]

        result = False
        if p[pIdx] == '*':
            for i in range(sIdx, len(s) + 1):
                if self.dfs(s, p, i, pIdx + 1, dp):
                    result = True
                    break
        else:
            if sIdx == len(s):
                result = False
            else:
                if p[pIdx] == '?' or p[pIdx] == s[sIdx]:
                    result = self.dfs(s, p, sIdx + 1, pIdx + 1, dp)
               
        dp[pIdx][sIdx] = result
        return result



    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sLen = len(s)
        pLen = len(p)

        if pLen == 0 and sLen > 0:
            return False

        dp = [ [False] * (sLen + 1) for _ in range(pLen + 1)]
        dp[pLen][sLen] = True


        for i in range(pLen - 1, -1, -1):
            if p[i] == '*':
                dp[i][sLen] = True
            else:
                break

        for pIdx in range(pLen - 1, -1, -1):
            for sIdx in range(sLen - 1, -1, -1):
                if p[pIdx] == '*':
                    dp[pIdx][sIdx] = dp[pIdx][sIdx + 1] or dp[pIdx + 1][sIdx]
                elif p[pIdx] == '?' or p[pIdx] == s[sIdx]:
                    dp[pIdx][sIdx] = dp[pIdx + 1][sIdx + 1]

        return dp[0][0]

    
    @staticmethod
    def main():
        sol = Solution()

        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        p = "*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa*"
        print(sol.isMatch(s, p))
        

if __name__ == "__main__":
    Solution.main() 