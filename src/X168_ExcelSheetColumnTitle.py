'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        remains = []
        ordA = ord('A')
        while n != 0:
            n -= 1
            d = n // 26
            remain = n - d * 26
            remains.append(chr(ordA + remain))
            n = d
        
        return ''.join(reversed(remains))
        

    @staticmethod
    def main():
        sol = Solution()
        n = 701
        print(sol.convertToTitle(n))

        
if __name__ == "__main__":
    Solution.main()
        