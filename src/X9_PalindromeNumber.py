'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''

class Solution:
    def isPalindrome1(self, x: int) -> bool:
        if x < 0:
            return False

        digits = []
        while x != 0:
            cur = x % 10
            x = x // 10
            digits.append(cur)

        for i in range(len(digits) // 2):
            if digits[i] != digits[len(digits) - 1 - i]:
                return False

        return True

    
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        res = 0
        while x > res:
            res = res * 10 + x % 10
            x = x // 10

        return x == res or x == res // 10

    @staticmethod
    def main():
        sol = Solution()

        print(sol.isPalindrome(121))

        print(sol.isPalindrome(-10))

        print(sol.isPalindrome(10))

if __name__ == "__main__":
    Solution.main()     

