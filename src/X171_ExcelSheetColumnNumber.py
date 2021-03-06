'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        ordA = ord('A')
        factor = 1

        for c in reversed(s):
            res += factor * (ord(c) - ordA + 1)
            factor *= 26

        return res

    @staticmethod
    def main():
        sol = Solution()
        s = 'A'
        print(sol.titleToNumber(s))

        
if __name__ == "__main__":
    Solution.main()