'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        longestLen = 1
        startIdx = 0

        for i in range(len(s)):
            left = i - 1
            right = i + 1
            curLen = 1
            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    curLen += 2
                    left -= 1
                    right += 1
                else:
                    break

            if curLen > longestLen:
                longestLen = curLen
                startIdx = left + 1

            left = i
            right = i + 1
            curLen = 0
            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    curLen += 2
                    left -= 1
                    right += 1
                else:
                    break

            if curLen > longestLen:
                longestLen = curLen
                startIdx = left + 1

        return s[startIdx:(startIdx + longestLen)]
        
        
    @staticmethod
    def main():
        sol = Solution()

        print(sol.longestPalindrome("babad"))

        print(sol.longestPalindrome("cbbd"))


if __name__ == "__main__":
    Solution.main()
        