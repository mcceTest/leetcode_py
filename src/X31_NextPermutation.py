'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        for idx in range(len(nums) - 1, 0, -1):
            if nums[idx] > nums[idx - 1]:
                swapIdx = idx
                for nextIdx in range(idx + 1, len(nums)):
                    if nums[nextIdx] <= nums[idx - 1]:
                        break
                    swapIdx = nextIdx
                    
                nums[idx - 1], nums[swapIdx] = nums[swapIdx], nums[idx - 1]

                self.reverseInPlace(nums, idx, len(nums) - 1)

                return

        self.reverseInPlace(nums, 0, len(nums) - 1)

        return


    def reverseInPlace(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


    @staticmethod
    def main():
        sol = Solution()

        nums = [1,3,2]
        sol.nextPermutation(nums)
        print(nums)

    

if __name__ == "__main__":
    Solution.main()  