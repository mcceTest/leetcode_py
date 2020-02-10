'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Trick: make good use of the condition that the majority element always exists
        major = nums[0]
        count = 1

        for num in nums[1:]:
            if num == major:
                count += 1
            else:
                count -= 1
                if count < 0:
                    major = num
                    count = 1
        
        return major

    @staticmethod
    def main():
        sol = Solution()
        nums = [6,5,5]
        print(sol.majorityElement(nums))

        
if __name__ == "__main__":
    Solution.main()