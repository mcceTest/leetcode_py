'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]

        res = []
        used = [False] * len(nums)
        curRes = []
        nums.sort()

        self.dfs(nums, 0, curRes, used, res)

        return res

    def dfs(self, nums, idx, curRes, used, res):
        if idx == len(nums):
            res.append(curRes[:])
            return

        curIdx = 0
        while curIdx < len(nums):
            if not used[curIdx]:
                curRes.append(nums[curIdx])
                used[curIdx] = True
                self.dfs(nums, idx + 1, curRes, used, res)
                used[curIdx] = False
                curRes.pop(-1)
                curIdx += 1
                while curIdx < len(nums) and nums[curIdx] == nums[curIdx - 1]:
                    curIdx += 1 
            else:
                curIdx += 1



        

    @staticmethod
    def main():
        sol = Solution()

        nums = [1,1,2]
        print(sol.permuteUnique(nums))
        

if __name__ == "__main__":
    Solution.main() 