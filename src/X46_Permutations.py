'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]

        res = []
        nextPerms = self.permute(nums[1:])
        for perm in nextPerms:
            for i in range(len(nums)):
                curPerm = perm[:]
                curPerm.insert(i, nums[0])
                res.append(curPerm)

        return res

    @staticmethod
    def main():
        sol = Solution()

        nums = [1,2,3]
        print(sol.permute(nums))
        

if __name__ == "__main__":
    Solution.main() 
