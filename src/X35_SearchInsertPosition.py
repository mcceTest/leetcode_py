'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        return self.bs(nums, 0, len(nums) - 1, target)

        
    def bs(self, nums, start, end, target):
        if start == end:
            if nums[start] == target:
                return start
            elif nums[start] > target:
                return start
            else:
                return start + 1

        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.bs(nums, start, mid, target)
        else:
            return self.bs(nums, mid + 1, end, target) 
        


    @staticmethod
    def main():
        sol = Solution()
        nums = [1,3,5,6]
        target = 5
        print(sol.searchInsert(nums, target))


if __name__ == "__main__":
    Solution.main()   