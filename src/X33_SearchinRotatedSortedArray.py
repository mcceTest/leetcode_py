'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        return self.bs(nums, 0, len(nums) - 1, target)
        


    def bs(self, nums, start, end, target):
        if start > end: return -1

        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[start]:
            if target > nums[mid]:
                return self.bs(nums, mid + 1, end, target)
            else:
                if target >= nums[start]:
                    return self.bs(nums, start, mid - 1, target)
                else:
                    return self.bs(nums, mid + 1, end, target)
        else:
            if target > nums[mid]:
                if target <= nums[end]:
                    return self.bs(nums, mid + 1, end, target)
                else:
                    return self.bs(nums, start, mid - 1, target)
            else:
                return self.bs(nums, start, mid - 1, target)


    @staticmethod
    def main():
        sol = Solution()
        nums = [3,1]
        target = 1
        print(sol.search(nums, target))


if __name__ == "__main__":
    Solution.main()   
            