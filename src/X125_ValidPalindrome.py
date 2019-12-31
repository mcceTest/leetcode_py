'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sLen = len(s)
        s = s.lower()

        start = 0
        end = sLen - 1
        
        while start < end:
            while start < sLen and not self.shouldConsider(s[start]):
                start += 1
            if start >= sLen:
                return True

            while end >= 0 and not self.shouldConsider(s[end]):
                end -= 1
            if end < 0:
                return True

            if start < end and s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True
            
    def shouldConsider(self, c):
        return (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9')

            

    @staticmethod
    def main():
        sol = Solution()
        s = "A man, a plan, a canal: Panama"
        print(sol.isPalindrome(s))


if __name__ == "__main__":
    Solution.main() 
        