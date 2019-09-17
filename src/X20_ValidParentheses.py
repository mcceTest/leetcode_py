'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        q = []
        
        if len(s) % 2 == 1:
            return False

        LEFT_PARENTHESE = set(['(', '[', '{'])
        RIGHT_PAIR = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if not q or c in LEFT_PARENTHESE:
                q.append(c)
            else:
                lastElem = q[-1]
                if lastElem in LEFT_PARENTHESE:
                    if lastElem == RIGHT_PAIR[c]:
                        q.pop()
                    else:
                        # early return
                        return False
                else:
                    q.append(c)

        return len(q) == 0


    @staticmethod
    def main():
        sol = Solution()

        print(sol.isValid("()"))

        print(sol.isValid("()[]{}"))

        print(sol.isValid("(]"))

        print(sol.isValid("([)]"))

        print(sol.isValid("{[]}"))
        


        
if __name__ == "__main__":
    Solution.main()   


