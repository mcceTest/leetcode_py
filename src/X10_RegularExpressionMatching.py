'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sLen = len(s)
        pLen = len(p)

        if pLen == 0:
            return sLen == 0

        dp = [ [False] * (pLen + 1) for _ in range(sLen + 1) ]
        dp[sLen][pLen] = True
        for i in range(sLen):
            dp[i][pLen] = False

        i = pLen - 1
        while i >= 0:
            pCur = p[i]
            if pCur == '*':
                repeatCur = p[i-1]
                i -= 1
                if repeatCur == '.':
                    for j in range(sLen, -1, -1):
                        for k in range(j, sLen+1):
                            if dp[k][i+2]:
                                dp[j][i] = True
                                break
                else:
                    for j in range(sLen, -1, -1):
                        if j == sLen:
                            dp[j][i] = dp[j][i+2]
                        else:
                            if dp[j][i+2]:
                                dp[j][i] = True
                            else:
                                for k in range(j, sLen):
                                    if s[k] == repeatCur and dp[k+1][i+2]:
                                        dp[j][i] = True
                                        break
            elif pCur == '.':
                for j in range(sLen, -1, -1):
                    if j == sLen:
                        dp[j][i] = False
                    else:
                        dp[j][i] = dp[j+1][i+1]
            else:
                for j in range(sLen, -1, -1):
                    if j == sLen:
                        dp[j][i] = False
                    else:
                        dp[j][i] = s[j] == p[i] and dp[j+1][i+1]

            i -= 1
            

        return dp[0][0]

    
    @staticmethod
    def main():
        sol = Solution()

        # print(sol.isMatch("aa", "a"))

        # print(sol.isMatch("aa", "a*"))

        # print(sol.isMatch("ab", ".*"))

        # print(sol.isMatch("aab", "c*a*b"))

        print(sol.isMatch("mississippi", "mis*is*p*."))


if __name__ == "__main__":
    Solution.main()     



