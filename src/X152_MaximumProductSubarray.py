'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        neg = None
        pos = None
        res = nums[0]

        for num in nums:
            if num == 0:
                neg = pos = None
            elif num > 0:
                if pos is None:
                    pos = num
                else:
                    pos *= num

                if neg is not None:
                    neg *= num
            else:
                if neg is None:
                    if pos is None:
                        neg = num
                    else:
                        neg = num * pos
                        pos = None
                else:
                    newPos = neg * num
                    if pos is None:
                        neg = num
                    else:
                        neg = num * pos
                    pos = newPos

            if pos is not None:
                if pos > res:
                    res = pos
            elif neg is not None:
                if neg > res:
                    res = neg
            else:
                if res < 0:
                    res = 0

        return res



    @staticmethod
    def main():
        sol = Solution()
        nums = [2,3,-2,4]
        print(sol.maxProduct(nums))

if __name__ == "__main__":
    Solution.main()
        