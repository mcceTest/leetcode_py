'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []

        cur = 1

        for idx in range(len(digits) - 1, -1, -1):
            cur += digits[idx]
            res.append(cur % 10)
            cur = cur // 10

        if cur != 0:
            res.append(cur)

        res.reverse()

        return res

    @staticmethod
    def main():
        sol = Solution()
        digits = [1,2,3]
        print(sol.plusOne(digits))

if __name__ == "__main__":
    Solution.main() 

