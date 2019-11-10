'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
'''


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False


        dp = [ [False] * (len(s2) + 1) for _ in range(len(s1) + 1) ]
        dp[0][0] = True
        for i2 in range(1, len(s2) + 1):
            if s2[i2 - 1] == s3[i2 - 1]:
                dp[0][i2] = True
            else:
                break

        for i1 in range(1, len(s1) + 1):
            if s1[i1 - 1] == s3[i1 - 1]:
                dp[i1][0] = True
            else:
                break

        for i3 in range(1, len(s3) + 1):
            found = False
            for i1 in range(max(0, i3 - len(s2)), min(len(s1), i3) + 1):
                i2 = i3 - i1
                if i1 == 0 or i2 == 0:
                    found = found or dp[i1][i2] 
                else:
                    if (s1[i1 - 1] == s3[i3 - 1] and dp[i1 - 1][i3 - i1]) or (s2[i2 - 1] == s3[i3 - 1] and dp[i1][i2 - 1]):
                        dp[i1][i2] = True
                        found = True

            if not found:
                return False

        return True

    @staticmethod
    def main():
        sol = Solution()
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"

        print(sol.isInterleave(s1, s2, s3))
        

if __name__ == "__main__":
    Solution.main() 
                    
        