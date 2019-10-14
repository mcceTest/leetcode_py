'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
'''


class Solution(object):
    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        count = [0] * 3
        for n in nums:
            count[n] += 1

        idx = 0
        for i in range(3):
            for _ in range(count[i]):
                nums[idx] = i
                idx += 1

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        zeroIdx = 0
        twoIdx = len(nums) - 1
        idx = 0
        while idx < len(nums):
            if nums[idx] == 0:
                if idx == zeroIdx:
                    zeroIdx += 1
                    idx += 1
                else:
                    nums[zeroIdx], nums[idx] = nums[idx], nums[zeroIdx]
                    zeroIdx += 1
            elif nums[idx] == 2:
                if idx >= twoIdx:
                    break
                else:
                    nums[twoIdx], nums[idx] = nums[idx], nums[twoIdx]
                    twoIdx -= 1
            else:
                idx += 1

    @staticmethod
    def main():
        sol = Solution()
        nums = [2,0,2,1,1,0]

        sol.sortColors(nums)
        print(nums)


if __name__ == "__main__":
    Solution.main()   


