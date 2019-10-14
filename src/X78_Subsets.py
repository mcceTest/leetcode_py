'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        nums.sort()

        return self.helper(nums, len(nums) - 1)
        

    def helper(self, nums, idx):
        if idx == -1:
            return [[]]

        result = []
        preSets = self.helper(nums, idx - 1)
        result.extend(preSets)

        for ps in preSets:
            tmp = ps[:]
            tmp.append(nums[idx])
            result.append(tmp)

        return result
        

    @staticmethod
    def main():
        sol = Solution()
        nums = [1,2,3]
        print(sol.subsets(nums))
        

if __name__ == "__main__":
    Solution.main() 