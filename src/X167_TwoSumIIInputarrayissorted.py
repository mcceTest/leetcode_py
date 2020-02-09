'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = 0
        hi = len(numbers) - 1

        while lo < hi:
            cur = numbers[lo] + numbers[hi]
            if cur == target:
                return [lo + 1, hi + 1]
            elif cur < target:
                # lo can not be part of the solution
                lo += 1
            else:
                hi -= 1

        return [None, None]
        
    
    @staticmethod
    def main():
        sol = Solution()
        numbers = [2,7,11,15]
        target = 9
        print(sol.twoSum(numbers, target))

        
if __name__ == "__main__":
    Solution.main()