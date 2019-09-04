'''
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        curSet = set()
        startIdx = 0

        longestLen = 0
        for _, c in enumerate(s):
            if c in curSet:
                longestLen = max(longestLen, len(curSet))
                while s[startIdx] != c:
                    curSet.remove(s[startIdx])
                    startIdx += 1
                startIdx += 1
            else:
                curSet.add(c)

        longestLen = max(longestLen, len(curSet))

        return longestLen

    @staticmethod
    def main():
        sol = Solution()

        print(sol.lengthOfLongestSubstring("abcabcbb"))

        print(sol.lengthOfLongestSubstring("bbbbb"))

        print(sol.lengthOfLongestSubstring("pwwkew"))


if __name__ == "__main__":
    Solution.main()
            
