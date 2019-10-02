'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''



class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        dp = [0] * (len(s) + 1)

        maxLen = 0
        for i, c in enumerate(s):
            if len(st) == 0 or c == '(':
                st.append((c, i))
                dp[i + 1] = 0
            else:
                topElem = st[-1]
                if topElem[0] == ')':
                    st.append((c, i))
                    dp[i + 1] = 0
                else:
                    curLen = i - topElem[1] + 1 + dp[topElem[1]]
                    dp[i + 1] = curLen
                    st.pop(-1)
                    if curLen > maxLen: 
                        maxLen = curLen

        return maxLen


    @staticmethod
    def main():
        sol = Solution()
        s = ")()())"
        print(sol.longestValidParentheses(s))


if __name__ == "__main__":
    Solution.main()  