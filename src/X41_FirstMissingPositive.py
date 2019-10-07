'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
'''

## Idea:
##  Go through the array once to mark all the numbers in the range(1, length),
##    as only those number (plus length + 1) could be a possible missing number.
##  Then go through the array again to then which is the first one missing.
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        if length == 0:
            return 1

        idx = 0

        while idx < len(nums):
            cur = nums[idx]
            if cur == idx + 1 or cur < 1 or cur > length:
                idx += 1
            elif cur < idx + 1:
                nums[cur - 1] = cur
                idx += 1
            else:
                if nums[cur - 1] == cur:
                    idx += 1
                else:
                    nums[cur - 1], nums[idx] = nums[idx], nums[cur - 1]

        for idx, n in enumerate(nums):
            if idx + 1 != n:
                return idx + 1

        return length + 1

            



        
        

    @staticmethod
    def main():
        sol = Solution()

        nums = [1,2,0]

        print(sol.firstMissingPositive(nums))
        

if __name__ == "__main__":
    Solution.main()  