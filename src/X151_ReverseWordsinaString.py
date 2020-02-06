'''
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.
'''



class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = []
        start = -1
        for idx, c in enumerate(s):
            if c == ' ':
                if start > -1:
                    words.append(s[start:idx])
                    start = -1
            else:
                if start == -1:
                    start = idx

        if start > -1:
            words.append(s[start:])

        words.reverse()

        return ' '.join(words)
        

    @staticmethod
    def main():
        sol = Solution()
        s = "the sky is blue"
        print(sol.reverseWords(s))

if __name__ == "__main__":
    Solution.main()