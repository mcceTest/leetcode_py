'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
'''
## TODO:
##  iterative approach


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return self.rotatedSearch(nums, 0, len(nums) - 1, target)

    def rotatedSearch(self, nums, low, high, target):
        if low > high:
            return False

        mid = (low + high) // 2

        if nums[mid] == target:
            return True
        else:
            if nums[mid] < nums[high]:
                if nums[mid] > target:
                    return self.rotatedSearch(nums, low, mid - 1, target)
                else:
                    return self.bSearch(nums, mid + 1, high, target) or self.rotatedSearch(nums, low, mid - 1, target)
            elif nums[mid] > nums[high]:
                if nums[mid] > target:
                    return self.bSearch(nums, low, mid - 1, target) or self.rotatedSearch(nums, mid + 1, high, target)
                else:
                    return self.rotatedSearch(nums, mid + 1, high, target)
            else:
                rightLow = mid
                while rightLow <= high and nums[rightLow] == nums[mid]:
                    rightLow += 1
                if rightLow <= high:
                    if nums[rightLow] == target:
                        return True
                    
                    if nums[rightLow] < nums[high]:
                        if nums[rightLow] > target:
                            return self.bSearch(nums, low, mid - 1, target)
                        else:
                            return self.bSearch(nums, rightLow + 1, high, target) or self.bSearch(nums, low, mid - 1, target)
                    else:
                        return self.bSearch(nums, low, mid - 1, target) or self.rotatedSearch(nums, rightLow + 1, high, target)
                else:
                    return self.rotatedSearch(nums, low, mid - 1, target)




    def bSearch(self, nums, low, high, target):
        if low > high:
            return False
        else:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                return self.bSearch(nums, mid + 1, high, target)
            else:
                return self.bSearch(nums, low, mid - 1, target)

    




            

    






    @staticmethod
    def main():
        sol = Solution()
        nums = [2,5,6,0,0,1,2]
        target = 0
        print(sol.search(nums, target))
        

if __name__ == "__main__":
    Solution.main() 