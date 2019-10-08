'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''


## TODO: try to start the search from the end, since we need to get the length of the last word.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        lastLen = 0
        startIdx = 0
        endIdx = 0
        idx = 0
        while idx < len(s):
            while idx < len(s) and s[idx] == ' ':
                idx += 1
            if idx < len(s):
                startIdx = idx
                endIdx = idx
                while idx < len(s) and s[idx] != ' ':
                    idx += 1
                endIdx = idx
                lastLen = endIdx - startIdx

        return lastLen


    @staticmethod
    def main():
        sol = Solution()
        s = "Hello World"
        print(sol.lengthOfLastWord(s))

if __name__ == "__main__":
    Solution.main() 