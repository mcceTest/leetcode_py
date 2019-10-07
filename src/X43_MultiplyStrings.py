'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1 = len(num1)
        len2 = len(num2)

        if len1 == 0 or len2 == 0:
            return ''

        res = [0] * (len1 + len2)

        for i in range(len1):
            n1 = int(num1[len1 - 1 - i])
            for j in range(len2):
                n2 = int(num2[len2 - 1 - j])
                cur = n1 * n2
                res[i + j] += cur
                carry = res[i + j] // 10
                res[i + j] -= carry * 10
                res[i + j + 1] += carry

        realEnd = len1 + len2 - 1
        while realEnd > 0 and res[realEnd] == 0:
            realEnd -= 1
        
        resStr = ''
        for i in range(realEnd, -1, -1):
            resStr += str(res[i])

        return resStr


    @staticmethod
    def main():
        sol = Solution()

        num1 = "12"
        num2 = "20"
        print(sol.multiply(num1, num2))
        

if __name__ == "__main__":
    Solution.main() 